#!/usr/bin/env python3
"""Prüft das Lexikon auf die Regeln aus CLAUDE.md.

    python3 tools/check.py          alle Prüfungen
    python3 tools/check.py --kurz   nur die Zusammenfassung

Geprüft wird: Frontmatter, Dateinamen, Baumkonsistenz, Wortlimits, relative
Links, Q-Nummern, offene Fragen und ob die generierte Navigation aktuell ist.
Rückgabewert 1, sobald ein Fehler gefunden wurde.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lexikon import (ARTIKEL_WURZELN, BEISPIEL_H2, GEN_BLOECKE, HOME,
                     LIMIT_BEISPIEL, LIMIT_FACHLICH, QUELLEN_DATEI, REPO,
                     abschnitte, baue_baum, lade_artikel, lade_offene_fragen,
                     lade_q_nummern, lies_block, parse_frontmatter,
                     pfad_nach_home, slug, zaehle_woerter)
import gen

PFLICHT = ("titel", "parent", "quellen", "status", "stand")
STATUS_WERTE = ("belegt", "abgeleitet", "zu prüfen")
LINK = re.compile(r"\[([^\]^]*?)\]\(([^)\s]+)\)")
Q_IM_TEXT = re.compile(r"\bQ\d+[a-z]?\b")

fehler, warnungen = [], []


def F(pfad, text):
    fehler.append(f"{pfad}: {text}")


def W(pfad, text):
    warnungen.append(f"{pfad}: {text}")


# --------------------------------------------------------------------------

def pruefe_frontmatter(a):
    for key in PFLICHT:
        if key not in a.fm:
            F(a.pfad, f"Frontmatter: '{key}' fehlt")
    status = a.fm.get("status")
    if status and status not in STATUS_WERTE:
        F(a.pfad, f"status '{status}' unbekannt, erlaubt: {', '.join(STATUS_WERTE)}")
    if "children" in a.fm:
        W(a.pfad, "'children' wird berechnet und gehört nicht ins Frontmatter")
    stand = str(a.fm.get("stand", ""))
    if stand and not re.fullmatch(r"\d{4}-\d{2}(-\d{2})?", stand):
        W(a.pfad, f"stand '{stand}' nicht im Format JJJJ-MM-TT")
    for i, c in enumerate(a.fm.get("codes") or [], 1):
        if not isinstance(c, dict):
            F(a.pfad, f"codes[{i}] ist kein Objekt")
            continue
        for key in ("wert", "bedeutung", "quelle", "status"):
            if key not in c:
                F(a.pfad, f"codes[{i}] ('{c.get('bedeutung', '?')}'): '{key}' fehlt")


def pruefe_dateiname(a):
    name = os.path.basename(a.pfad)[:-3]
    erwartet = slug(a.titel)
    if name != erwartet:
        F(a.pfad, f"Dateiname '{name}.md' passt nicht zum Titel "
                  f"'{a.titel}' — erwartet '{erwartet}.md'")


def pruefe_h1(a):
    """Die H1 muss wortgleich zum Frontmatter-Titel sein.

    Sonst weichen Breadcrumb, Register und Seitentitel voneinander ab.
    """
    m = re.search(r"^#\s+(.+?)\s*$", a.rumpf, re.MULTILINE)
    if not m:
        F(a.pfad, "keine H1 gefunden")
    elif m.group(1).strip() != str(a.titel).strip():
        F(a.pfad, f"H1 '{m.group(1).strip()}' weicht vom Titel '{a.titel}' ab")


def pruefe_baum(artikel):
    for a in artikel.values():
        if a.parent is None:
            continue
        if a.parent == a.pfad:
            F(a.pfad, "ist sein eigener Parent")
        # Erreichbarkeit von Home
        gesehen, aktuell, tiefe = {a.pfad}, a, 0
        while aktuell.parent and aktuell.parent != HOME:
            if aktuell.parent in gesehen:
                F(a.pfad, f"Zyklus über '{aktuell.parent}'")
                break
            naechster = artikel.get(aktuell.parent)
            if naechster is None:
                break
            gesehen.add(naechster.pfad)
            aktuell = naechster
            tiefe += 1
            if tiefe > 15:
                F(a.pfad, "Baum tiefer als 15 Ebenen")
                break
        else:
            pass

    # Kategorieordner ohne Kategorieartikel
    for wurzel in ARTIKEL_WURZELN:
        basis = os.path.join(REPO, wurzel)
        if not os.path.isdir(basis):
            continue
        for ordner, unterordner, _ in os.walk(basis):
            for u in unterordner:
                voll = os.path.join(ordner, u)
                rel = os.path.relpath(voll, REPO).replace(os.sep, "/")
                if not os.path.isfile(os.path.join(REPO, rel + ".md")):
                    F(rel + "/", f"Ordner ohne Kategorieartikel '{rel}.md'")

    # Kinder müssen im Ordner der Kategorie liegen
    for a in artikel.values():
        if not a.parent or a.parent == HOME:
            continue
        erwarteter_ordner = a.parent[:-3]
        if os.path.dirname(a.pfad) != erwarteter_ordner:
            W(a.pfad, f"liegt nicht im Ordner des Parents ('{erwarteter_ordner}/')")


def pruefe_wortlimits(a):
    fachlich, beispiel = abschnitte(a)
    if not fachlich.strip():
        F(a.pfad, "fachliche Erklärung fehlt oder keine H1 gefunden")
    if BEISPIEL_H2 not in a.rumpf:
        F(a.pfad, f"Abschnitt '{BEISPIEL_H2} – Beispiel aus Bärstadt' fehlt")
    n1, n2 = zaehle_woerter(fachlich), zaehle_woerter(beispiel)
    if n1 > LIMIT_FACHLICH:
        F(a.pfad, f"fachliche Erklärung {n1} Wörter, erlaubt {LIMIT_FACHLICH}")
    if n2 > LIMIT_BEISPIEL:
        F(a.pfad, f"Beispiel {n2} Wörter, erlaubt {LIMIT_BEISPIEL}")
    return n1, n2


def ohne_code(text):
    """Code-Blöcke und Codespans entfernen.

    Links darin sind Beispiele und zeigen bewusst Pfade, die relativ zu einem
    anderen Ort gelten — etwa in CLAUDE.md oder in den Vorlagen.
    """
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"~~~.*?~~~", " ", text, flags=re.DOTALL)
    text = re.sub(r"``[^`]*``", " ", text)
    return re.sub(r"`[^`\n]*`", " ", text)


def pruefe_links(pfad, text, anker):
    basis = os.path.dirname(os.path.join(REPO, pfad))
    for titel, ziel in LINK.findall(ohne_code(text)):
        if re.match(r"^(https?:|mailto:|tel:)", ziel):
            continue
        datei, _, fragment = ziel.partition("#")
        if not datei:
            continue
        voll = os.path.normpath(os.path.join(basis, datei))
        if not os.path.exists(voll):
            F(pfad, f"toter Link: [{titel}]({ziel})")
            continue
        rel = os.path.relpath(voll, REPO).replace(os.sep, "/")
        if fragment and rel == QUELLEN_DATEI and fragment.lower() not in anker:
            F(pfad, f"Anker '#{fragment}' in {QUELLEN_DATEI} nicht vorhanden "
                    f"(Link [{titel}]({ziel}))")


def pruefe_quellen(a, q_nummern):
    for q in a.quellen:
        if q not in q_nummern:
            F(a.pfad, f"Frontmatter quellen: '{q}' steht nicht in {QUELLEN_DATEI}")
    im_text = set(Q_IM_TEXT.findall(a.rumpf))
    for q in sorted(im_text - q_nummern):
        F(a.pfad, f"Text nennt '{q}', das nicht in {QUELLEN_DATEI} definiert ist")
    nicht_deklariert = sorted(q for q in im_text & q_nummern
                              if q not in a.quellen)
    if nicht_deklariert:
        W(a.pfad, "im Text zitiert, aber nicht im Frontmatter 'quellen': "
                  + ", ".join(nicht_deklariert))


def pruefe_offene_fragen(a, bekannte):
    genannt = set(a.fm.get("offene_fragen") or [])
    genannt |= set(re.findall(r"\b(O\d+)\b", a.rumpf))
    for o in sorted(genannt):
        if o not in bekannte:
            W(a.pfad, f"offene Frage '{o}' steht nicht in PLAN.md")


def pruefe_siehe_auch(a, artikel):
    for ziel in a.fm.get("siehe_auch") or []:
        if not isinstance(ziel, str):
            continue
        if ziel not in artikel and not os.path.exists(os.path.join(REPO, ziel)):
            F(a.pfad, f"siehe_auch: '{ziel}' existiert nicht")


def pruefe_gen_bloecke(a, artikel):
    inhalte = {
        "breadcrumb": gen.breadcrumb(a, artikel),
        "unterartikel": gen.unterartikel(a),
        "navigation": gen.navigation(a, artikel),
    }
    for name in GEN_BLOECKE:
        ist = lies_block(a.roh, name)
        if ist is None:
            if name == "unterartikel" and not a.kinder:
                continue
            F(a.pfad, f"Block GEN:{name} fehlt")
            continue
        if ist.strip() != inhalte[name].strip():
            F(a.pfad, f"Block GEN:{name} nicht aktuell — 'python3 tools/gen.py' ausführen")


def pruefe_verwaiste_dateien(artikel):
    for wurzel in ARTIKEL_WURZELN:
        basis = os.path.join(REPO, wurzel)
        if not os.path.isdir(basis):
            continue
        for ordner, _, dateien in os.walk(basis):
            for name in dateien:
                if not name.endswith(".md"):
                    continue
                rel = os.path.relpath(os.path.join(ordner, name),
                                      REPO).replace(os.sep, "/")
                if rel not in artikel:
                    F(rel, "nicht eingelesen — fehlt das Frontmatter?")
                elif not artikel[rel].fm:
                    F(rel, "kein Frontmatter")


# --------------------------------------------------------------------------

def main():
    kurz = "--kurz" in sys.argv
    artikel = lade_artikel()
    if not artikel:
        print("Keine Artikel gefunden — noch kein Lexikon angelegt.")
        print("Das ist in Phase 0 normal. Nichts zu prüfen.")
        return 0

    _, baumfehler = baue_baum(artikel)
    for f in baumfehler:
        fehler.append(f)

    q_nummern = lade_q_nummern()
    anker = {q.lower() for q in q_nummern}
    offene = lade_offene_fragen()
    if not q_nummern:
        fehler.append(f"{QUELLEN_DATEI}: keine Q-Nummern als Überschrift gefunden")

    pruefe_verwaiste_dateien(artikel)
    pruefe_baum(artikel)

    summe_fachlich = summe_beispiel = 0
    for a in sorted(artikel.values(), key=lambda x: x.pfad):
        pruefe_frontmatter(a)
        pruefe_dateiname(a)
        pruefe_h1(a)
        n1, n2 = pruefe_wortlimits(a)
        summe_fachlich += n1
        summe_beispiel += n2
        pruefe_links(a.pfad, a.roh, anker)
        pruefe_quellen(a, q_nummern)
        pruefe_offene_fragen(a, offene)
        pruefe_siehe_auch(a, artikel)
        pruefe_gen_bloecke(a, artikel)

    # Links in den Dokumenten der Wurzel
    for name in ("README.md", "PLAN.md", "STRUKTUR.md", "CLAUDE.md",
                 "BESCHAFFUNG.md", QUELLEN_DATEI, "REGISTER.md",
                 "ABKUERZUNGEN.md"):
        pfad = os.path.join(REPO, name)
        if os.path.isfile(pfad):
            with open(pfad, encoding="utf-8") as f:
                pruefe_links(name, f.read(), anker)

    if not kurz:
        for w in warnungen:
            print(f"WARNUNG  {w}")
        for f in fehler:
            print(f"FEHLER   {f}")
        print()

    print(f"Artikel:     {len(artikel)}")
    print(f"Q-Nummern:   {len(q_nummern)}")
    print(f"Wörter:      {summe_fachlich} fachlich, {summe_beispiel} Beispiel")
    print(f"Warnungen:   {len(warnungen)}")
    print(f"Fehler:      {len(fehler)}")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
