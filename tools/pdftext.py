#!/usr/bin/env python3
"""Minimaler PDF-Textextraktor, nur Standardbibliothek.

Aufruf: python3 -I pdftext.py DATEI.pdf [VON_SEITE] [BIS_SEITE]
Gibt den Text seitenweise aus, mit Marker '=== [SEITE n] ==='.
"""
import re
import sys
import zlib

obj_re = re.compile(rb"(\d+)\s+(\d+)\s+obj\b")


def load_objects(data):
    objs = {}
    for m in obj_re.finditer(data):
        num = int(m.group(1))
        end = data.find(b"endobj", m.end())
        objs[num] = data[m.end():end if end != -1 else len(data)]
    objs.update(load_objstm(objs))
    return objs


def load_objstm(objs):
    """Objekte aus komprimierten Objektströmen (/Type /ObjStm) auspacken.

    PDF 1.5 und neuer verpacken Objekte in solche Ströme. Ohne diesen Schritt
    bleibt der Textextraktor bei modernen PDFs leer, weil er die Objekte im
    Rohbytestrom nicht mehr findet.
    """
    gefunden = {}
    for body in list(objs.values()):
        if not re.search(rb"/Type\s*/ObjStm", body):
            continue
        daten = stream_bytes(body)
        if not daten:
            continue
        mn = re.search(rb"/N\s+(\d+)", body)
        mf = re.search(rb"/First\s+(\d+)", body)
        if not (mn and mf):
            continue
        anzahl, erster = int(mn.group(1)), int(mf.group(1))
        zahlen = re.findall(rb"(\d+)\s+(\d+)", daten[:erster])
        paare = [(int(a), int(b)) for a, b in zahlen][:anzahl]
        for i, (num, off) in enumerate(paare):
            start = erster + off
            ende = erster + paare[i + 1][1] if i + 1 < len(paare) else len(daten)
            if num not in objs and 0 <= start < ende <= len(daten):
                gefunden[num] = daten[start:ende]
    return gefunden


def stream_bytes(body):
    i = body.find(b"stream")
    if i == -1:
        return b""
    j = i + len(b"stream")
    if body[j:j + 2] == b"\r\n":
        j += 2
    elif body[j:j + 1] in (b"\n", b"\r"):
        j += 1
    k = body.find(b"endstream", j)
    raw = body[j:k if k != -1 else len(body)]
    if b"FlateDecode" in body[:i]:
        for cut in (0, -1, -2):
            try:
                return zlib.decompress(raw[:len(raw) + cut] if cut else raw)
            except zlib.error:
                continue
        try:
            return zlib.decompressobj().decompress(raw)
        except zlib.error:
            return b""
    return raw


def refs(body, key):
    """Alle Objektnummern hinter einem Schlüssel, z. B. /Contents 12 0 R."""
    m = re.search(key.encode() + rb"\s*(\[[^\]]*\]|\d+\s+\d+\s+R)", body)
    if not m:
        return []
    return [int(x) for x in re.findall(rb"(\d+)\s+\d+\s+R", m.group(1))]


def page_order(objs):
    """Seitenreihenfolge aus dem Seitenbaum, mit Fallback auf Objektreihenfolge."""
    pages, seen = [], set()

    def walk(num, depth=0):
        if num in seen or depth > 60 or num not in objs:
            return
        seen.add(num)
        body = objs[num]
        if re.search(rb"/Type\s*/Page\b(?!s)", body):
            pages.append(num)
            return
        for kid in refs(body, "/Kids"):
            walk(kid, depth + 1)

    root = None
    for num, body in objs.items():
        if re.search(rb"/Type\s*/Pages\b", body) and b"/Parent" not in body:
            root = num
            break
    if root is not None:
        walk(root)
    if not pages:
        pages = [n for n, b in sorted(objs.items())
                 if re.search(rb"/Type\s*/Page\b(?!s)", b)]
    return pages


def parse_tounicode(daten):
    """ToUnicode-CMap auswerten: Zeichencode -> Unicode.

    Moderne PDFs kodieren Text als CID, also als Zeichennummer der Schrift
    statt als Zeichensatzwert. Ohne diese Zuordnung kommt Buchstabensalat
    heraus - oder Steuerzeichen, die Textwerkzeuge die Datei für binär
    halten lassen.
    """
    text = daten.decode("latin-1", "replace")
    karte = {}
    for block in re.findall(r"beginbfchar(.*?)endbfchar", text, re.DOTALL):
        for src, dst in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            karte[int(src, 16)] = _utf16(dst)
    for block in re.findall(r"beginbfrange(.*?)endbfrange", text, re.DOTALL):
        for lo, hi, dst in re.findall(
                r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            start, ende, ziel = int(lo, 16), int(hi, 16), int(dst, 16)
            if ende - start > 65535:
                continue
            for i in range(ende - start + 1):
                karte[start + i] = chr(ziel + i) if ziel + i < 0x110000 else ""
        # Variante mit Array: <lo> <hi> [<d1> <d2> ...]
        for lo, hi, arr in re.findall(
                r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*\[(.*?)\]", block, re.DOTALL):
            ziele = re.findall(r"<([0-9A-Fa-f]+)>", arr)
            for i, z in enumerate(ziele):
                karte[int(lo, 16) + i] = _utf16(z)
    return karte


def _utf16(hexstr):
    try:
        roh = bytes.fromhex(hexstr if len(hexstr) % 2 == 0 else "0" + hexstr)
    except ValueError:
        return ""
    if len(roh) >= 2:
        return roh.decode("utf-16-be", "replace")
    return roh.decode("latin-1", "replace")


def seiten_fontkarten(objs, seitenobj):
    """Je Fontname der Seite die ToUnicode-Zuordnung, soweit vorhanden."""
    karten = {}
    m = re.search(rb"/Font\s*<<(.*?)>>", seitenobj, re.DOTALL)
    if not m:
        return karten
    for name, num in re.findall(rb"/([A-Za-z0-9#+.-]+)\s+(\d+)\s+\d+\s+R", m.group(1)):
        font = objs.get(int(num))
        if not font:
            continue
        refs = refs_(font, "/ToUnicode")
        if not refs or refs[0] not in objs:
            continue
        daten = stream_bytes(objs[refs[0]])
        if daten:
            karte = parse_tounicode(daten)
            if karte:
                karten[name.decode("latin-1")] = karte
    return karten


def refs_(body, key):
    m = re.search(key.encode() + rb"\s*(\d+)\s+\d+\s+R", body)
    return [int(m.group(1))] if m else []


ESC = {b"n": b"\n", b"r": b"\r", b"t": b"\t", b"b": b"\b", b"f": b"\f",
       b"(": b"(", b")": b")", b"\\": b"\\"}


def unescape(s):
    out, i = bytearray(), 0
    while i < len(s):
        c = s[i:i + 1]
        if c == b"\\" and i + 1 < len(s):
            nxt = s[i + 1:i + 2]
            if nxt in ESC:
                out += ESC[nxt]
                i += 2
                continue
            if nxt.isdigit():
                oct_digits = s[i + 1:i + 4]
                m = re.match(rb"[0-7]{1,3}", oct_digits)
                if m:
                    out.append(int(m.group(), 8) & 0xFF)
                    i += 1 + len(m.group())
                    continue
            i += 2
            continue
        out += c
        i += 1
    return bytes(out)


str_re = re.compile(rb"\((?:\\\\.|[^\\\\()]|\((?:\\\\.|[^\\\\()])*\))*\)|<[0-9A-Fa-f\s]+>")
num_re = rb"[-+]?[0-9]*\.?[0-9]+"
tok_re = re.compile(
    str_re.pattern + rb"|(?P<num>" + num_re + rb")"
    rb"|(?P<op>T[fjJdDLwsmz*]|TJ|Tj|Td|TD|Tm|T\*|TL|BT|ET|'|\")"
    rb"|(?P<arr>\[)|(?P<arrend>\])"
)


def _ueber_karte(roh, karte):
    """Bytefolge über eine ToUnicode-Karte in Text wandeln.

    Zweibyte-Codes zuerst, weil CID-Schriften meist zweibytig kodieren.
    """
    if len(roh) >= 2 and all((roh[i] << 8 | roh[i + 1]) in karte
                             for i in range(0, len(roh) - 1, 2)):
        return "".join(karte[roh[i] << 8 | roh[i + 1]]
                       for i in range(0, len(roh) - 1, 2))
    return "".join(karte.get(b, chr(b) if b >= 32 else "") for b in roh)


def decode_hex(tok, shift=0, karte=None):
    h = re.sub(rb"\s", b"", tok[1:-1])
    if len(h) % 2:
        h += b"0"
    raw = bytes.fromhex(h.decode("ascii"))
    if karte:
        return _ueber_karte(raw, karte)
    if len(raw) > 1 and raw[0::2].count(0) > len(raw) // 4:
        return raw.decode("utf-16-be", "replace")
    return apply_shift(raw.decode("latin-1", "replace"), shift)


def apply_shift(s, shift):
    if not shift:
        return s
    return "".join(chr(ord(c) + shift) if 32 <= ord(c) < 127 else c for c in s)


def extract(content, shift=0, ygap=2.0, xgap=0.28, fontkarten=None):
    """Textruns nach Position zu Zeilen zusammensetzen.

    Zeilenumbruch nur bei Sprung der Y-Position, Leerzeichen bei X-Lücke.
    """
    runs = []            # (y, x, text, fs)
    x = y = 0.0
    leading = 0.0
    fs = 12.0
    in_array = False
    nums = []
    fontkarten = fontkarten or {}
    karte = None
    for m in tok_re.finditer(content):
        tok = m.group()
        if m.group("num") is not None:
            val = float(tok)
            if in_array:          # Kerning in 1/1000 em
                x -= val / 1000.0 * fs
            else:
                nums.append(val)
            continue
        if m.group("arr") is not None:
            in_array = True
            nums = []
            continue
        if m.group("arrend") is not None:
            in_array = False
            nums = []
            continue
        op = m.group("op")
        if op is None:                      # String-Token
            if tok.startswith(b"("):
                roh = unescape(tok[1:-1])
                txt = (_ueber_karte(roh, karte) if karte
                       else apply_shift(roh.decode("latin-1", "replace"), shift))
            else:
                txt = decode_hex(tok, shift, karte)
            if txt:
                runs.append((y, x, txt, fs))
                x += len(txt) * 0.5 * fs    # Vorschub aus Schriftgröße
            nums = []
            continue
        if op == b"Tf" and nums:
            fs = abs(nums[-1]) or 12.0
            mf = re.search(rb"/([A-Za-z0-9#+.-]+)\s*$", content[:m.start()].rstrip())
            karte = fontkarten.get(mf.group(1).decode("latin-1")) if mf else None
        elif op == b"Tm" and len(nums) >= 6:
            x, y = nums[-2], nums[-1]
            if abs(nums[0]) > 0.01:        # Skalierung der Textmatrix
                fs = fs * abs(nums[0]) if abs(nums[0]) < 0.2 else fs
        elif op in (b"Td", b"TD") and len(nums) >= 2:
            if op == b"TD":
                leading = -nums[-1]
            x += nums[-2]
            y += nums[-1]
        elif op == b"TL" and nums:
            leading = nums[-1]
        elif op in (b"T*", b"'", b'"'):
            y -= leading or 12.0
            x = 0.0
        elif op == b"BT":
            x = y = 0.0
        nums = []

    # nach Zeilen gruppieren: absteigende Y-Position, innerhalb der Zeile nach X
    runs.sort(key=lambda r: (-r[0], r[1]))
    lines, cur, cur_y, cur_x = [], [], None, None
    for ry, rx, txt, rfs in runs:
        if cur_y is None or abs(ry - cur_y) > max(ygap, rfs * 0.35):
            if cur:
                lines.append("".join(cur))
            cur, cur_y = [txt], ry
        else:
            if (cur_x is not None and rx - cur_x > rfs * xgap
                    and cur and not cur[-1].endswith(" ") and not txt.startswith(" ")):
                cur.append(" ")
            cur.append(txt)
        cur_x = rx + len(txt) * 0.5 * rfs
    if cur:
        lines.append("".join(cur))
    out = "\n".join(re.sub(r"[ \t]{2,}", " ", l).strip() for l in lines)
    return re.sub(r"\n{3,}", "\n\n", out).strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    shift = 0
    for a in sys.argv[1:]:
        if a.startswith("--shift="):
            shift = int(a.split("=", 1)[1])
    path = args[0]
    first = int(args[1]) if len(args) > 1 else 1
    last = int(args[2]) if len(args) > 2 else 10 ** 9
    data = open(path, "rb").read()
    objs = load_objects(data)
    pages = page_order(objs)
    sys.stderr.write(f"[{len(objs)} Objekte, {len(pages)} Seiten]\n")
    for idx, num in enumerate(pages, 1):
        if idx < first or idx > last:
            continue
        content = b"".join(stream_bytes(objs[c]) for c in refs(objs[num], "/Contents") if c in objs)
        if not content:
            content = stream_bytes(objs[num])
        karten = seiten_fontkarten(objs, objs[num])
        print(f"=== [SEITE {idx}] ===")
        print(extract(content, shift=shift, fontkarten=karten))


if __name__ == "__main__":
    main()
