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


def breadcrumb(a, artikel):
    teile = [f"[Home]({a.rel(HOME)})"]
    for eltern in pfad_nach_home(a, artikel):
        teile.append(f"[{eltern.titel}]({a.rel(eltern.pfad)})")
    teile.append(a.titel)
    return " › ".join(teile)


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
            "unterartikel": unterartikel(a),
            "navigation": navigation(a, artikel),
        }
        text = a.roh
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
