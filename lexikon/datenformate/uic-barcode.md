---
titel: UIC-Barcode
englisch: UIC barcode
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/vdv-barcode.md, lexikon/berechtigungen/statische-berechtigung.md]
quellen: [Q34, Q46]
status: belegt
offene_fragen: [O17]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › UIC-Barcode
<!-- /GEN:breadcrumb -->

# UIC-Barcode

Der UIC-Barcode ist der **Barcodestandard des internationalen Eisenbahnverbands** Union Internationale des Chemins de fer. Eisenbahnverkehrsunternehmen betreiben damit ihr Online- und Mobile-Ticketing; er ermöglicht die gegenseitige Kontrolle im internationalen und nationalen Eisenbahnverkehr ([Q46](../../QUELLEN.md#q46), Kap. 2 und 5, PDF-S. 5, S. 12).

**Er steht neben dem [VDV-Barcode](vdv-barcode.md), nicht an seiner Stelle.** Daraus ergibt sich die Notwendigkeit, beide standardisierten Barcodes in Kontrollgeräten zu unterstützen ([Q46](../../QUELLEN.md#q46), Kap. 2, PDF-S. 5).

**Die Brücke zwischen beiden Welten**, abgestimmt mit dem VDV und dem VDV eTicket Service ([Q46](../../QUELLEN.md#q46), Kap. 5, PDF-S. 12):

- Erweiterungen an **UIC 918-3** stellen die Kompatibilität zum VDV-Barcode her; die erweiterte Fassung heißt **UIC 918-3\***.
- Dazu wird ein **zusätzlicher Datensatz** entsprechend der [statischen Berechtigung](../berechtigungen/statische-berechtigung.md) in die UIC-Barcode-Darstellung integriert — ebenfalls ein **Aztec-Code**.
- Die Kontrollsoftware der DB AG erzeugt daraus und aus dem Datensatz **0080BL** eine statische Berechtigung nach KA STB-SPEC.
- Mit **918-3 zu 918-9** wurde eine Aktualisierung nötig: **UIC 918-9\*** sichert die Kompatibilität weiter, verwendet aber anstelle von 0080BL einen anderen Datensatz (welchen, ist nicht lesbar — zu prüfen, O17).

**Sicherheit über Zertifikate:** Wer UIC-Tickets vertreibt, muss seinen Partnern das Zertifikat zur Kontrolle bereitstellen — über eine Key-Management-Website der UIC oder im deutschen SPNV direkt durch das ausgebende Unternehmen; der Abruf ist auch ohne UIC-Mitgliedschaft möglich ([Q46](../../QUELLEN.md#q46), Kap. 5.1, PDF-S. 13).

**Empfohlen** werden der VDV-Barcode für Verbund-, Haus- und Landestarife, der UIC-Barcode für Tarife des Eisenbahnverkehrs ([Q46](../../QUELLEN.md#q46), Kap. 6, PDF-S. 14 f.).

## Einfach erklärt – Beispiel aus Bärstadt

Petra Pranke kontrolliert in der Linie 4. Was sie dort vorgehalten bekommt, kommt aus zwei verschiedenen Häusern.

Das eine ist das Haus des Bären-Verkehrsbunds: Pias ABO Azubi, Ollis Einzelfahrschein, die Monatskarte — alles nach dem VDV-Standard. Das andere ist das Haus der Eisenbahn. Wer mit der Regionalbahn aus Luchsstadt kommt und anschließend in die Straßenbahn steigt, hat womöglich ein Ticket, das nach dem UIC-Standard aufgebaut ist.

Für Petras Gerät sind das zwei Sprachen. Und darum muss es beide verstehen.

**Der Trick mit dem eingebetteten Datensatz.** Hier wird es für ein Prüfwerkzeug interessant. Die beiden Standards wurden nicht vereinheitlicht — das wäre bei einem internationalen Eisenbahnstandard auch illusorisch. Stattdessen wurde in den UIC-Barcode ein **zusätzlicher Datensatz hineingelegt**, der dem entspricht, was eine statische Berechtigung nach VDV-Art enthält.

Die Kontrollsoftware setzt daraus bei der Kontrolle eine statische Berechtigung zusammen. Das Gerät liest also einen UIC-Barcode und erhält am Ende etwas, das es wie einen VDV-Datensatz behandeln kann.

Das ist eine elegante Lösung, und sie erklärt eine Beobachtung, die sonst verwirrt: Derselbe Barcode kann je nach Lesart zwei verschiedene Dinge sein — ein Eisenbahnticket und eine statische Berechtigung.

**Der Stern im Namen.** `918-3` ist der gewöhnliche UIC-Barcode. `918-3*` ist derselbe Barcode mit dem eingelegten VDV-Datensatz. Der Stern bedeutet also nicht „neuer“, sondern „zusätzlich VDV-kontrollierbar“. Später wurde aus 918-3 die 918-9, und entsprechend aus `918-3*` die `918-9*`.

Wer die Zahlen durcheinanderbringt, liest den falschen Datensatz. Ein Grund, bei einem Werkzeug die Version nicht zu erraten, sondern aus dem Datensatz zu bestimmen.

## Quellen

- [Q46](../../QUELLEN.md#q46) – Whitepaper Barcodes im ÖPNV (2021): Kap. 2, PDF-S. 5 (UIC-Standardbarcode des internationalen Eisenbahnverbands, gegenseitige Kontrolle im internationalen und nationalen Eisenbahnverkehr, Notwendigkeit beide Barcodes in Kontrollgeräten zu unterstützen), Kap. 3, PDF-S. 6 (bisherige Anwendung), Kap. 5, PDF-S. 12 (Union Internationale des Chemins de fer als Basis; Abstimmung mit der AG Barcode des VDV und dem VDV eTicket Service; Erweiterung UIC 918-3 zu 918-3\*; zusätzlicher Datensatz entsprechend der statischen Berechtigung, Aztec-Code; Kontrollsoftware der DB AG erzeugt daraus und aus 0080BL eine statische Berechtigung nach KA STB-SPEC; 918-9\* mit anderem Datensatz), Kap. 5.1, PDF-S. 13 (Zertifikatsaustausch, Key-Management-Website, Abruf ohne UIC-Mitgliedschaft), Kap. 6, PDF-S. 14 f. (Empfehlung zur Anwendung beider Barcodes)
- [Q34](../../QUELLEN.md#q34) – KCD NRW, Ergebnisdokument Deutschlandticket / UIC · *Auswertung offen*

<!-- GEN:siehe_auch -->
## Siehe auch

- [VDV-Barcode](vdv-barcode.md)
- [Statische Berechtigung](../berechtigungen/statische-berechtigung.md) (StatBer)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
