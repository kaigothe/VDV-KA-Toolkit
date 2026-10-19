#!/usr/bin/env python3
"""Erzeugt die Navigation des Lexikons aus dem Frontmatter.

Geschrieben werden ausschließlich die Blöcke zwischen den GEN-Markern sowie
REGISTER.md und ABKUERZUNGEN.md. Fließtext wird nie angefasst.

    python3 tools/gen.py           schreibt
    python3 tools/gen.py --pruefen schreibt nicht, meldet nur Abweichungen
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lexikon import (GEN_BLOECKE, HOME, REPO, baue_baum, lade_artikel,
                     lies_block, pfad_nach_home, setze_block, sortkey)

REGISTER = "REGISTER.md"
ABKUERZUNGEN = "ABKUERZUNGEN.md"
BESCHAFFUNG = "BESCHAFFUNG.md"

# Nicht öffentliche KA-Dokumente und die Schreibweisen, unter denen sie in den
# Artikeln auftreten. Inventarnummern aus dem eTicket-Regelwerk, Kap. 3 (Q25).
NICHT_OEFFENTLICH = [
    ("41", "KA AktM-SPEC", ["KA AktM-SPEC", "KA_SPEC_AktM"]),
    ("4", "KA SST-SPEC", ["KA SST-SPEC", "KA_SPEC_SST"]),
    ("1", "KA BOM-SPEC", ["KA BOM-SPEC", "KA_SPEC_BOM"]),
    ("5", "KA XML-Schemata und WSDL", ["KA XML-Schemata", "KA XML-Schema"]),
    ("—", "ALISE-Schnittstelle und ALISE-XSD", ["ALISE-XSD", "ALISE-Schnittstellenbeschreibung"]),
    ("2", "Anlage TLV EFS", ["Anlage TLV EFS"]),
    ("40", "KA MultiBER-SPEC", ["KA MultiBER-SPEC", "KA_SPEC_MULTIBER"]),
    ("8", "KA SAM-SPEC", ["KA SAM-SPEC", "KA_SPEC_SAM"]),
    ("6", "KA SEC-SPEC", ["KA SEC-SPEC"]),
    ("11", "KA KOSES-Spec", ["KA KOSES-Spec"]),
    ("42", "KA STB-Spec", ["KA STB-Spec"]),
    ("33", "KA TXx-Prüfungs-ANW", ["KA TXx-Prüfungs-ANW"]),
    ("35", "KA PROD_ID-ANW", ["KA PROD_ID-ANW"]),
    ("3", "Anlage Datenschutz", ["Anlage Datenschutz"]),
    ("7", "KA NM-SPEC", ["KA NM-SPEC"]),
    ("9", "KA ION-SPEC", ["KA ION-SPEC"]),
    ("12–21", "KA SysLH", ["KA SysLH", "SYSLH_", "SysLH"]),
]


def breadcrumb(a, artikel):
    teile = [f"[Home]({a.rel(HOME)})"]
    for eltern in pfad_nach_home(a, artikel):
        teile.append(f"[{eltern.titel}]({a.rel(eltern.pfad)})")
    teile.append(a.titel)
    return " › ".join(teile)


def siehe_auch(a, artikel):
    """Querverweise aus dem Frontmatter als sichtbaren Abschnitt.

    Die Titel kommen aus den Zielartikeln, bleiben also bei Umbenennungen
    korrekt. Ohne Eintraege bleibt der Block leer.
    """
    ziele = [str(z) for z in (a.fm.get("siehe_auch") or []) if str(z).strip()]
    if not ziele:
        return ""
    zeilen = ["## Siehe auch", ""]
    for ziel in ziele:
        andere = artikel.get(ziel)
        if andere is None:
            zeilen.append(f"- [{ziel}]({a.rel(ziel)})")
            continue
        kuerzel = andere.fm.get("abkuerzung")
        zusatz = f" ({kuerzel})" if kuerzel and str(kuerzel) != andere.titel else ""
        zeilen.append(f"- [{andere.titel}]({a.rel(ziel)}){zusatz}")
    return "\n".join(zeilen)


def unterartikel(a):
    if not a.kinder:
        return ""
    zeilen = ["## Unterartikel", ""]
    for kind in sorted(a.kinder, key=lambda x: sortkey(x.titel)):
        zeilen.append(f"- [{kind.titel}]({a.rel(kind.pfad)})")
    return "\n".join(zeilen)


def navigation(a, artikel):
    teile = [f"[Home]({a.rel(HOME)})"]
    if a.parent and a.parent != HOME and a.parent in artikel:
        eltern = artikel[a.parent]
        teile.append(f"[{eltern.titel}]({a.rel(eltern.pfad)})")
    teile.append(f"[Register]({a.rel(REGISTER)})")
    return "---\n\n**Navigation:** " + " · ".join(teile)


def baue_register(artikel):
    zeilen = [
        "# Alphabetisches Register", "",
        "Erzeugt von `tools/gen.py` aus dem Frontmatter. **Nicht von Hand ändern.**",
        "", f"{len(artikel)} Eintrag" + ("" if len(artikel) == 1 else "räge"), "",
    ]
    letzter = None
    for a in sorted(artikel.values(), key=lambda x: sortkey(x.titel)):
        anfang = sortkey(a.titel)[0].upper()
        if anfang != letzter:
            zeilen += ["", f"## {anfang}", ""]
            letzter = anfang
        kuerzel = a.fm.get("abkuerzung")
        zusatz = f" — {kuerzel}" if kuerzel else ""
        status = a.fm.get("status", "")
        marke = "" if status == "belegt" else f" *({status})*"
        zeilen.append(f"- [{a.titel}]({a.pfad}){zusatz}{marke}")
    zeilen += ["", "---", "", f"**Navigation:** [Home]({HOME})"]
    return "\n".join(zeilen) + "\n"


def baue_abkuerzungen(artikel):
    mit = [a for a in artikel.values() if a.fm.get("abkuerzung")]
    zeilen = [
        "# Abkürzungsverzeichnis", "",
        "Erzeugt von `tools/gen.py` aus dem Frontmatter. **Nicht von Hand ändern.**",
        "", f"{len(mit)} Abkürzung" + ("" if len(mit) == 1 else "en") + ".", "",
        "| Abkürzung | Begriff | Englisch |",
        "|---|---|---|",
    ]
    for a in sorted(mit, key=lambda x: sortkey(str(x.fm["abkuerzung"]))):
        englisch = a.fm.get("englisch", "") or ""
        zeilen.append(f"| **{a.fm['abkuerzung']}** | [{a.titel}]({a.pfad}) | {englisch} |")
    zeilen += ["", "---", "", f"**Navigation:** [Home]({HOME})"]
    return "\n".join(zeilen) + "\n"


def baue_verwendung(artikel):
    """Verwendungsnachweis: welcher Artikel nennt welches nicht öffentliche Dokument."""
    import re as _re

    def link(a):
        return f"[{a.titel}]({a.pfad})"

    zeilen = []

    # Tabelle 1: Dokument -> Artikel
    treffer = []
    for inv, name, muster in NICHT_OEFFENTLICH:
        nennend = []
        gesamt = 0
        for a in sorted(artikel.values(), key=lambda x: sortkey(x.titel)):
            n = sum(a.rumpf.count(m) for m in muster)
            if n:
                nennend.append(a)
                gesamt += n
        if nennend:
            treffer.append((gesamt, inv, name, nennend))
    treffer.sort(key=lambda t: (-t[0], t[1]))

    zeilen += [
        f"**{len(treffer)} nicht öffentliche Dokumente** werden derzeit in "
        f"{len(artikel)} Artikeln als Normquelle genannt, nach Häufigkeit:",
        "",
        "| Nennungen | Inv.-Nr. | Dokument | genannt in |",
        "|---:|---:|---|---|",
    ]
    for gesamt, inv, name, nennend in treffer:
        wo = ", ".join(link(a) for a in nennend)
        zeilen.append(f"| {gesamt} | {inv} | **{name}** | {wo} |")

    # Tabelle 2: Artikel, die auf ein Dokument warten
    wartend = [a for a in artikel.values() if a.fm.get("status") == "zu prüfen"]
    zeilen += ["", "### Artikel, die ohne diese Dokumente unvollständig bleiben", ""]
    if wartend:
        zeilen += ["| Artikel | offene Fragen |", "|---|---|"]
        for a in sorted(wartend, key=lambda x: sortkey(x.titel)):
            offen = ", ".join(str(o) for o in (a.fm.get("offene_fragen") or [])) or "—"
            zeilen.append(f"| {link(a)} | {offen} |")
    else:
        zeilen.append("Derzeit keine.")

    # Tabelle 3: offene Frage -> Artikel
    fragen = {}
    for a in artikel.values():
        for o in a.fm.get("offene_fragen") or []:
            fragen.setdefault(str(o), []).append(a)
    zeilen += ["", "### Offene Fragen und die betroffenen Artikel", ""]
    if fragen:
        zeilen += ["| Frage | betrifft |", "|---|---|"]
        for o in sorted(fragen, key=lambda x: int(_re.sub(r"\D", "", x) or 0)):
            wo = ", ".join(link(a) for a in
                           sorted(fragen[o], key=lambda x: sortkey(x.titel)))
            zeilen.append(f"| **{o}** | {wo} |")
    else:
        zeilen.append("Derzeit keine.")

    zeilen += ["", f"*Erzeugt aus {len(artikel)} Artikeln. Die Links führen in das Lexikon.*"]
    return "\n".join(zeilen)


def main():
    pruefen = "--pruefen" in sys.argv
    artikel = lade_artikel()
    if not artikel:
        print("Keine Artikel gefunden. Läuft tools/gen.py im Repository?")
        return 1

    _, baumfehler = baue_baum(artikel)
    for f in baumfehler:
        print(f"WARNUNG {f}")

    geaendert, fehlende = [], []
    for a in sorted(artikel.values(), key=lambda x: x.pfad):
        inhalte = {
            "breadcrumb": breadcrumb(a, artikel),
            "siehe_auch": siehe_auch(a, artikel),
            "unterartikel": unterartikel(a),
            "navigation": navigation(a, artikel),
        }
        text = a.roh
        # Einmalige Migration: fehlende Blöcke vor der Navigation einfügen
        for name in ("siehe_auch",):
            if inhalte[name] and f"GEN:{name}" not in text and "<!-- GEN:navigation -->" in text:
                text = text.replace(
                    "<!-- GEN:navigation -->",
                    f"<!-- GEN:{name} -->\n<!-- /GEN:{name} -->\n\n<!-- GEN:navigation -->", 1)
        for name in GEN_BLOECKE:
            alt = lies_block(text, name)
            if alt is None:
                if name == "unterartikel" and not a.kinder:
                    continue           # Blattartikel brauchen den Block nicht
                fehlende.append(f"{a.pfad}: Block GEN:{name} fehlt")
                continue
            text, _ = setze_block(text, name, inhalte[name])
        if text != a.roh:
            geaendert.append(a.pfad)
            if not pruefen:
                with open(os.path.join(REPO, a.pfad), "w", encoding="utf-8") as f:
                    f.write(text)

    # Verwendungsnachweis in BESCHAFFUNG.md einsetzen
    bpfad = os.path.join(REPO, BESCHAFFUNG)
    if os.path.isfile(bpfad):
        with open(bpfad, encoding="utf-8") as f:
            btext = f.read()
        neu, gefunden = setze_block(btext, "verwendung", baue_verwendung(artikel))
        if not gefunden:
            print(f"WARNUNG {BESCHAFFUNG}: Block GEN:verwendung fehlt")
        elif neu != btext:
            geaendert.append(BESCHAFFUNG)
            if not pruefen:
                with open(bpfad, "w", encoding="utf-8") as f:
                    f.write(neu)

    dateien = {REGISTER: baue_register(artikel),
               ABKUERZUNGEN: baue_abkuerzungen(artikel)}
    for name, inhalt in dateien.items():
        pfad = os.path.join(REPO, name)
        alt = ""
        if os.path.isfile(pfad):
            with open(pfad, encoding="utf-8") as f:
                alt = f.read()
        if alt != inhalt:
            geaendert.append(name)
            if not pruefen:
                with open(pfad, "w", encoding="utf-8") as f:
                    f.write(inhalt)

    for f in fehlende:
        print(f"WARNUNG {f}")

    if pruefen:
        if geaendert:
            print(f"Nicht aktuell ({len(geaendert)}): " + ", ".join(geaendert[:10]))
            return 1
        print(f"Navigation aktuell ({len(artikel)} Artikel).")
        return 0

    print(f"{len(artikel)} Artikel geprüft, {len(geaendert)} Datei(en) geschrieben.")
    if geaendert:
        for g in geaendert:
            print(f"  geschrieben {g}")
    return 1 if fehlende or baumfehler else 0


if __name__ == "__main__":
    sys.exit(main())
