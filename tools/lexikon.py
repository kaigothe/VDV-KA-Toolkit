#!/usr/bin/env python3
"""Gemeinsame Basis für gen.py und check.py.

Enthält den Frontmatter-Parser, die Slug-Regel, das Einlesen aller Artikel und
den Aufbau des Begriffsbaums. Nur Standardbibliothek — siehe CLAUDE.md, Regel 10.

Pfadkonvention: `parent` und `siehe_auch` sind **immer relativ zur
Repository-Wurzel**, z. B. `lexikon/aktionsmanagement.md`. Das ist eindeutig und
unabhängig davon, wo die Datei selbst liegt.
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = "README.md"
ARTIKEL_WURZELN = ("lexikon",)
QUELLEN_DATEI = "QUELLEN.md"
PLAN_DATEI = "PLAN.md"

LIMIT_FACHLICH = 250
LIMIT_BEISPIEL = 600
BEISPIEL_H2 = "## Einfach erklärt"

GEN_BLOECKE = ("breadcrumb", "unterartikel", "navigation")

UMLAUTE = {
    "ä": "ae", "ö": "oe", "ü": "ue",
    "Ä": "ae", "Ö": "oe", "Ü": "ue",
    "ß": "ss", "é": "e", "è": "e", "á": "a", "à": "a",
}


SORT_UMLAUTE = {"ä": "a", "ö": "o", "ü": "u", "ß": "ss",
                "Ä": "a", "Ö": "o", "Ü": "u", "é": "e", "è": "e"}


def sortkey(text):
    """Deutsche Sortierung: Umlaute wie der Grundvokal, Ä vor B."""
    s = (text or "").lower()
    for k, v in SORT_UMLAUTE.items():
        s = s.replace(k.lower(), v)
    return s


def slug(text):
    """Dateinamen-Slug nach CLAUDE.md, Regel 6."""
    s = text.strip().lower()
    for k, v in UMLAUTE.items():
        s = s.replace(k.lower(), v)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


# --------------------------------------------------------------------------
# Frontmatter
# --------------------------------------------------------------------------

def _skalar(wert):
    w = wert.strip()
    if w.startswith("#"):
        return ""
    w = re.sub(r"\s+#\s.*$", "", w)          # Zeilenkommentar
    if len(w) >= 2 and w[0] == w[-1] and w[0] in "\"'":
        w = w[1:-1]
    if re.fullmatch(r"-?\d+", w):
        return int(w)
    if w in ("true", "false"):
        return w == "true"
    if w in ("[]", "~", "null"):
        return [] if w == "[]" else None
    return w


def _inline_liste(wert):
    inner = wert.strip()[1:-1].strip()
    if not inner:
        return []
    return [_skalar(t) for t in inner.split(",") if t.strip()]


def parse_frontmatter(text):
    """Liest eine bewusst kleine YAML-Teilmenge.

    Unterstützt Skalare, Inline-Listen `[a, b]`, Blocklisten aus Skalaren und
    Blocklisten aus Objekten (für `codes:`). Mehr braucht das Lexikon nicht.
    """
    if not text.startswith("---"):
        return {}, text
    ende = text.find("\n---", 3)
    if ende == -1:
        return {}, text
    kopf = text[3:ende].strip("\n")
    rest = text[ende + 4:].lstrip("\n")

    daten = {}
    schluessel = None
    for zeile in kopf.split("\n"):
        if not zeile.strip() or zeile.lstrip().startswith("#"):
            continue
        einzug = len(zeile) - len(zeile.lstrip())
        strip = zeile.strip()

        if strip.startswith("- "):
            if schluessel is None:
                continue
            eintrag = strip[2:].strip()
            if ":" in eintrag and not eintrag.startswith("["):
                k, _, v = eintrag.partition(":")
                daten[schluessel].append({k.strip(): _skalar(v)})
            else:
                daten[schluessel].append(_skalar(eintrag))
            continue

        if einzug > 0 and schluessel and daten.get(schluessel) and isinstance(
                daten[schluessel][-1], dict) and ":" in strip:
            k, _, v = strip.partition(":")
            daten[schluessel][-1][k.strip()] = _skalar(v)
            continue

        if ":" not in strip:
            continue
        k, _, v = strip.partition(":")
        k, v = k.strip(), v.strip()
        if v == "":
            daten[k] = []
            schluessel = k
        elif v.startswith("["):
            daten[k] = _inline_liste(v)
            schluessel = None
        else:
            daten[k] = _skalar(v)
            schluessel = None
    return daten, rest


# --------------------------------------------------------------------------
# Artikel
# --------------------------------------------------------------------------

class Artikel:
    def __init__(self, pfad, fm, rumpf, roh):
        self.pfad = pfad                     # relativ zur Repo-Wurzel
        self.fm = fm
        self.rumpf = rumpf
        self.roh = roh
        self.kinder = []

    @property
    def titel(self):
        return self.fm.get("titel") or os.path.basename(self.pfad)[:-3]

    @property
    def parent(self):
        p = self.fm.get("parent")
        return p if isinstance(p, str) and p else None

    @property
    def ist_kategorie(self):
        """Kategorie, wenn der gleichnamige Ordner neben der Datei existiert."""
        return os.path.isdir(os.path.join(REPO, self.pfad[:-3]))

    @property
    def quellen(self):
        q = self.fm.get("quellen") or []
        return [str(x) for x in q] if isinstance(q, list) else [str(q)]

    def rel(self, ziel):
        """Relativer Link von diesem Artikel zu einem wurzelrelativen Ziel."""
        start = os.path.dirname(os.path.join(REPO, self.pfad)) or REPO
        return os.path.relpath(os.path.join(REPO, ziel), start).replace(os.sep, "/")


def lade_artikel():
    """Alle Artikel unter den Artikelwurzeln einlesen."""
    artikel = {}
    for wurzel in ARTIKEL_WURZELN:
        basis = os.path.join(REPO, wurzel)
        if not os.path.isdir(basis):
            continue
        for ordner, _, dateien in os.walk(basis):
            for name in sorted(dateien):
                if not name.endswith(".md"):
                    continue
                voll = os.path.join(ordner, name)
                rel = os.path.relpath(voll, REPO).replace(os.sep, "/")
                with open(voll, encoding="utf-8") as f:
                    roh = f.read()
                fm, rumpf = parse_frontmatter(roh)
                artikel[rel] = Artikel(rel, fm, rumpf, roh)
    return artikel


def baue_baum(artikel):
    """children aus parent berechnen. Gibt (wurzeln, fehler) zurück."""
    fehler = []
    for a in sorted(artikel.values(), key=lambda x: x.pfad):
        p = a.parent
        if p is None:
            fehler.append(f"{a.pfad}: kein 'parent' im Frontmatter")
            continue
        if p == HOME:
            continue
        if p not in artikel:
            fehler.append(f"{a.pfad}: parent '{p}' existiert nicht")
            continue
        artikel[p].kinder.append(a)

    wurzeln = [a for a in artikel.values() if a.parent == HOME]
    return sorted(wurzeln, key=lambda x: x.titel.lower()), fehler


def pfad_nach_home(a, artikel, grenze=20):
    """Kette vom Artikel bis Home, ohne den Artikel selbst. Von oben nach unten."""
    kette, aktuell, gesehen = [], a, {a.pfad}
    while aktuell.parent and aktuell.parent != HOME and len(kette) < grenze:
        eltern = artikel.get(aktuell.parent)
        if eltern is None or eltern.pfad in gesehen:
            break
        kette.append(eltern)
        gesehen.add(eltern.pfad)
        aktuell = eltern
    return list(reversed(kette))


# --------------------------------------------------------------------------
# Generierte Blöcke
# --------------------------------------------------------------------------

def block_muster(name):
    return re.compile(
        r"<!--\s*GEN:" + name + r"\s*-->(.*?)<!--\s*/GEN:" + name + r"\s*-->",
        re.DOTALL)


def lies_block(text, name):
    m = block_muster(name).search(text)
    return m.group(1) if m else None


def setze_block(text, name, inhalt):
    """Blockinhalt ersetzen. Gibt (neuer_text, gefunden) zurück."""
    neu = f"<!-- GEN:{name} -->\n{inhalt.strip()}\n<!-- /GEN:{name} -->"
    if inhalt.strip() == "":
        neu = f"<!-- GEN:{name} -->\n<!-- /GEN:{name} -->"
    muster = block_muster(name)
    if not muster.search(text):
        return text, False
    return muster.sub(lambda _: neu, text, count=1), True


def ohne_gen_bloecke(text):
    """Text ohne generierte Blöcke und ohne HTML-Kommentare."""
    for name in GEN_BLOECKE:
        text = block_muster(name).sub("", text)
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


# --------------------------------------------------------------------------
# Abschnitte und Wortzählung
# --------------------------------------------------------------------------

def abschnitte(artikel):
    """Gibt (fachlich, beispiel) als Text zurück, ohne generierte Blöcke."""
    text = ohne_gen_bloecke(artikel.rumpf)
    zeilen = text.split("\n")

    start_h1 = None
    start_beispiel = None
    ende_beispiel = len(zeilen)
    for i, z in enumerate(zeilen):
        if start_h1 is None and z.startswith("# "):
            start_h1 = i + 1
        elif start_beispiel is None and z.startswith(BEISPIEL_H2):
            start_beispiel = i + 1
        elif start_beispiel is not None and z.startswith("## "):
            ende_beispiel = i
            break

    if start_h1 is None:
        return "", ""
    fachlich_ende = start_beispiel - 1 if start_beispiel else len(zeilen)
    fachlich = "\n".join(zeilen[start_h1:fachlich_ende])
    beispiel = ("\n".join(zeilen[start_beispiel:ende_beispiel])
                if start_beispiel else "")
    return fachlich, beispiel


def zaehle_woerter(text):
    """Wörter zählen: ohne Codeblöcke, Tabellen und Linkziele."""
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = "\n".join(z for z in text.split("\n") if not z.strip().startswith("|"))
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)   # Linktext behalten
    text = re.sub(r"[`*_>#-]", " ", text)
    return len([w for w in text.split() if any(c.isalnum() for c in w)])


# --------------------------------------------------------------------------
# Quellen
# --------------------------------------------------------------------------

def lade_q_nummern():
    """Alle in QUELLEN.md als Überschrift definierten Q-Nummern."""
    pfad = os.path.join(REPO, QUELLEN_DATEI)
    if not os.path.isfile(pfad):
        return set()
    with open(pfad, encoding="utf-8") as f:
        inhalt = f.read()
    return set(re.findall(r"^#{1,6}\s+(Q\d+[a-z]?)\s*$", inhalt, re.MULTILINE))


def lade_offene_fragen():
    pfad = os.path.join(REPO, PLAN_DATEI)
    if not os.path.isfile(pfad):
        return set()
    with open(pfad, encoding="utf-8") as f:
        return set(re.findall(r"\*\*(O\d+)\*\*", f.read()))


def meldung(art, text):
    print(f"{art}: {text}")


def main():
    artikel = lade_artikel()
    print(f"{len(artikel)} Artikel, {len(lade_q_nummern())} Q-Nummern")
    return 0


if __name__ == "__main__":
    sys.exit(main())
