---
titel: TXA/TXB
englisch: rejection and confirmation record
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/duplikaterkennung.md]
quellen: [Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes:
  - wert: 0
    bedeutung: packageerrorcode – ok
    quelle: Q06
    fundstelle: Kap. 4.8 (PDF-S. 36)
    status: belegt
    verbundspezifisch: true
  - wert: 1
    bedeutung: packageerrorcode – ZIP-Datei lässt sich nicht öffnen
    quelle: Q06
    fundstelle: Kap. 4.8 (PDF-S. 36)
    status: belegt
    verbundspezifisch: true
  - wert: 2
    bedeutung: packageerrorcode – ZIP-Datei enthält unerwarteten Inhalt
    quelle: Q06
    fundstelle: Kap. 4.8 (PDF-S. 36)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › TXA/TXB
<!-- /GEN:breadcrumb -->

# TXA/TXB

`TXA` und `TXB` sind die Antworten des Hintergrundsystems auf eingereichte Transaktionen: Für jede **abzulehnende** Transaktion wird ein Ablehnungsdatensatz `TXA` ausgestellt, für jede **akzeptierte** ein Bestätigungsdatensatz `TXB` ([Q06](../../QUELLEN.md#q06), Kap. 3.1).

Als Ablehnungsgründe nennt [Q06](../../QUELLEN.md#q06), Kap. 3.1, ausdrücklich fehlerhafte Formate, ein negatives Ergebnis der MAC-Prüfung und inkonsistente Daten; hinzu kommt die [Duplikaterkennung](duplikaterkennung.md) ([Q06](../../QUELLEN.md#q06), Kap. 5.3).

Der Ablauf ist paketweise ([Q06](../../QUELLEN.md#q06), Kap. 3.1) · *verbundspezifisch*: Der Aufrufer sendet ein Paket mit Transaktionsdaten; das Hintergrundsystem speichert es, erzeugt eine **Paketnummer** und gibt sie zurück. Ein Scheduler startet die Verarbeitung. Anschließend werden Zusammenfassung, `TXB`, `TXA` und `ERR`-Dateien als **Paket-Quittung** bereitgestellt. Der Aufrufer erfährt über die Manifest-Datei von der neuen Quittung, holt sie ab, ordnet sie über die Paketnummer zu und bestätigt den Erhalt; danach entfernt das Hintergrundsystem die Quittung aus dem Manifest.

Die Quittung selbst heißt `PACKAGEACK` und trägt `packagenumber`, `packageerrorcode` (0 = ok, 1 = ZIP-Datei lässt sich nicht öffnen, 2 = ZIP-Datei enthält unerwarteten Inhalt), `rejectedsize` und `acceptedsize` ([Q06](../../QUELLEN.md#q06), Kap. 4.8).

Wichtig: Der `packageerrorcode` betrifft das **gesamte Paket**, nicht einzelne Transaktionen ([Q06](../../QUELLEN.md#q06), Kap. 4.8).

## Einfach erklärt – Beispiel aus Bärstadt

Wer Belege einreicht, möchte wissen, was damit passiert ist. Genau das leisten `TXA` und `TXB`.

Die Bärstädter Verkehrsbetriebe sammeln die Rückmeldungen ihrer Terminals und schicken sie als **Paket** ans Hintergrundsystem — nicht einzeln, sondern gebündelt. Das Hintergrundsystem nimmt das Paket an, gibt ihm eine Paketnummer und bestätigt damit zunächst nur den Eingang. Verarbeitet ist noch nichts.

Das passiert etwas später, wenn die Verarbeitung anläuft. Dann wird jede einzelne Meldung geprüft, und für jede gibt es ein Urteil:

- **`TXB`** heißt angenommen. Der Vorgang ist verbucht.
- **`TXA`** heißt abgelehnt. Etwa weil das Format nicht stimmt, weil der Prüfcode nicht passt, weil die Daten sich widersprechen — oder weil dieselbe Meldung schon einmal da war.

Alle diese Urteile kommen gesammelt in einer **Paket-Quittung** zurück. Dabei fällt etwas auf: Die BVB bekommt die Quittung nicht zugeschickt, sondern muss sie abholen. Sie schaut regelmäßig in eine Übersichtsdatei, das Manifest, und sieht dort: Für Paket Nummer 4711 liegt eine Antwort bereit.

Das Zusammenspiel von Paketnummer und Quittung ist der Grund, warum die BVB ihre Belege überhaupt archivieren oder löschen darf. Erst wenn sie weiß, was mit Paket 4711 geschah, ist der Vorgang abgeschlossen. Danach bestätigt sie den Erhalt — und das Hintergrundsystem nimmt die Quittung aus dem Manifest, damit sie nicht wieder und wieder abgeholt wird.

Eine Unterscheidung lohnt noch: Es gibt einen Fehlercode für das **ganze Paket**. Der sagt Dinge wie „die ZIP-Datei lässt sich nicht öffnen“. Wenn der anspricht, ist nichts verarbeitet worden — dann hilft kein Blick auf einzelne Belege, sondern nur ein neuer Versand.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 3.1 „Allgemeiner Ablauf“ (PDF-S. 18 f.): Paketversand, Paketnummer, Scheduler, `TXA` für abzulehnende und `TXB` für akzeptierte Transaktionen, Ablehnungsgründe, Bereitstellung und Abholung der Paket-Quittung über das Manifest, Bestätigung des Erhalts; Kap. 3.8 (KA-Transaktionen hochladen), Kap. 3.9 (Paket-Quittung herunterladen), Kap. 4.8 `PACKAGEACK` (PDF-S. 36): `packagenumber`, `packageerrorcode` mit den Werten 0, 1 und 2, `rejectedsize`, `acceptedsize` · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
