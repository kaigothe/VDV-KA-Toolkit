#!/usr/bin/env python3
"""Prüft Stichproben der PDF-Seitenangaben gegen die Quellen.

    python3 tools/fundstellen.py

Hintergrund: Seitenangaben hängen daran, wie der Extraktor den Seitenbaum
liest. Als `pdftext.py` um die Unterstützung komprimierter Objektströme
erweitert wurde, verschob sich die Zählung mehrerer Quellen um eine Seite —
77 Fundstellen im Lexikon waren danach falsch, ohne dass eine Prüfung das
gemeldet hätte. Dieses Skript schließt die Lücke.

Die Liste PROBEN enthält je Quelle und Seite einen Marker, der genau dort
stehen muss. Sie ist von Hand gepflegt: Wer eine neue Fundstelle zitiert,
die einen bisher ungeprüften Bereich betrifft, ergänzt hier einen Eintrag.
Das Skript ist bewusst eine Stichprobe und keine vollständige Prüfung —
eine solche wäre nur mit maschinenlesbaren Zitaten möglich.

Schlägt eine Probe fehl, werden die Nachbarseiten durchsucht; das Skript
nennt dann die tatsächliche Seite. Rückgabewert 1 bei Abweichungen.
"""
import glob
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRAKTOR = os.path.join(REPO, "tools", "pdftext.py")
UMGEBUNG = 3   # so viele Seiten in jede Richtung bei einem Fehlschlag

# (Q-Nummer, zitierte PDF-Seite, erwarteter Marker als regulärer Ausdruck)
# Die Marker berücksichtigen, dass die Extraktion Umlaute verlieren kann.
PROBEN = [
    ("Q02",  19, r"Aktionsliste / Action Lis"),
    ("Q02",  52, r"Kontrolle / Inspection"),
    ("Q02",  66, r"Nutzermedium / User Medium"),
    ("Q02",  92, r"Statische Berechtigung / Static Entitlement"),
    ("Q05",   8, r"2\.1 Berechtigung"),
    ("Q05",   9, r"WertobjektStatus_CODE"),
    ("Q05",  22, r"4\.4\.4 logTransaktionsTyp"),
    ("Q06",  14, r"Ausgabe EFS .{0,4}ber Aktionsliste = 37"),
    ("Q06",  19, r"3\.1 Allgemeiner Ablauf"),
    ("Q06",  36, r"4\.7 Zertifikatsliste"),
    ("Q06",  37, r"PACKAGE ?ACK"),
    ("Q06",  38, r"4\.10"),
    ("Q06",  40, r"Rollen-Code 31 ALI"),
    ("Q06",  41, r"5\.1\.2 Datenschutz"),
    ("Q06",  42, r"5\.3 Duplikate"),
    ("Q06",  44, r"Ticketinfo Mobil"),
    ("Q25",  35, r"Kapitel 3: VDV-KA"),
    ("Q25",  39, r"Markenbuch"),
    ("Q25", 114, r"XSD- Bereich"),
    ("Q25", 115, r"NamensraumBereich"),
    ("Q25", 159, r"Ausbauvariante 1: eBezahlen"),
    ("Q25", 239, r"Tabelle 38"),
    ("Q37",   4, r"1\.12\.0"),
    ("Q39",  52, r"TXAAUFBER"),
    ("Q39",  50, r"TXSFREIB"),
    ("Q39",  51, r"TXSFREIA"),
    ("Q39",  52, r"TXAFREIBER"),
    ("Q39",  53, r"vHGS als ALISE"),
    ("Q40",  16, r"EP_Sperrfreigabeauftrag"),
    ("Q40",  20, r"Sperrfreigabemitteilun"),
    # Q43 bis Q48: ergaenzt mit den Artikeln zu etiCORE, Datenschutz und Barcode
    ("Q43",   4, r"Release Kandidat 6"),
    ("Q43",  23, r"daraus exportierte Dok"),
    ("Q43",  25, r"CipherSuite"),
    ("Q43",  26, r"Motics Specificat"),
    ("Q43",  27, r"Anlage Datenschutz"),
    ("Q43",  31, r"Mobile Ticketing Crypto Service"),
    ("Q43",  33, r"Central Routing Engi"),
    ("Q43",  35, r"CCP / KVP"),
    ("Q43",  36, r"ohne Motics"),
    ("Q45",   8, r"Zus.{0,2}zliches SAM"),
    ("Q45",  10, r"eTicket Ready Vertrag"),
    ("Q45",  12, r"Authentisierungsschl"),
    ("Q45",  19, r"Key - Identifier"),
    ("Q45",  23, r"Level - 1"),
    ("Q45",  27, r"PKI - Webschnittstelle"),
    ("Q45",  35, r"zSAM - Zertifikat"),
    ("Q46",   5, r"signierte Barcode dynami"),
    ("Q46",   7, r"CIBO-S"),
    ("Q46",   8, r"Identifikationsmerkmal"),
    ("Q46",   9, r"Sperrlistenservice"),
    ("Q46",  11, r"Kurzzeitzertifikate"),
    ("Q46",  12, r"918-3\* bezeichnet"),
    ("Q46",  13, r"railpublickey"),
    ("Q46",  15, r"asmtool"),
    ("Q48",   2, r"Vorabkontrolle"),
    ("Q48",   7, r"SAM ID: Muss"),
    ("Q48",  10, r"ORG - IDs"),
    ("Q48",  12, r"PIN - Eingabe"),
    ("Q48",  13, r"Datenschutz - Grund"),
    ("Q48",  16, r"Landesbeauftragter"),
]


def quelle_pfad(q):
    treffer = sorted(glob.glob(os.path.join(REPO, "QUELLEN", f"{q}_*.pdf")))
    if not treffer:   # auch der Unterordner QUELLEN/docs/ ist zugelassen
        treffer = sorted(glob.glob(os.path.join(REPO, "QUELLEN", "docs", f"{q}_*.pdf")))
    return treffer[0] if treffer else None


def seite(pfad, nr):
    try:
        return subprocess.run(
            [sys.executable, "-I", EXTRAKTOR, pfad, str(nr), str(nr)],
            capture_output=True, text=True, timeout=300).stdout
    except subprocess.TimeoutExpired:
        return ""


def main():
    fehler, fehlende = [], []
    print(f"{'Quelle':7} {'Seite':>5}  Befund")
    for q, nr, marker in PROBEN:
        pfad = quelle_pfad(q)
        if pfad is None:
            fehlende.append(q)
            print(f"{q:7} {nr:>5}  Quelle nicht in QUELLEN/ — übersprungen")
            continue
        if re.search(marker, seite(pfad, nr)):
            print(f"{q:7} {nr:>5}  ok")
            continue
        tatsaechlich = None
        for d in range(1, UMGEBUNG + 1):
            for kandidat in (nr - d, nr + d):
                if kandidat >= 1 and re.search(marker, seite(pfad, kandidat)):
                    tatsaechlich = kandidat
                    break
            if tatsaechlich:
                break
        if tatsaechlich:
            print(f"{q:7} {nr:>5}  ABWEICHUNG — Marker steht auf S. {tatsaechlich}")
            fehler.append((q, nr, tatsaechlich))
        else:
            print(f"{q:7} {nr:>5}  Marker nicht gefunden (±{UMGEBUNG}) — Probe prüfen")
            fehler.append((q, nr, None))

    print()
    if fehlende:
        print(f"Übersprungen, weil die Quelle lokal fehlt: {', '.join(sorted(set(fehlende)))}")
    if not fehler:
        print(f"Alle {len(PROBEN) - len(fehlende)} geprüften Fundstellen stimmen.")
        return 0
    print(f"{len(fehler)} Abweichung(en). Zu korrigieren sind die Angaben "
          "'PDF-S. …' in den Artikeln und im Frontmatter:")
    for q, alt, neu in fehler:
        print(f"  {q}: PDF-S. {alt} -> {neu if neu else '?'}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
