---
titel: Berechtigungen
englisch: entitlements and products
parent: README.md
siehe_auch: [lexikon/rollen/pv.md]
quellen: [Q02, Q05, Q35]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../README.md) › Berechtigungen
<!-- /GEN:breadcrumb -->

# Berechtigungen

Diese Kategorie behandelt, **was** ein Fahrgast besitzt und **woraus** es gemacht ist.

Eine **[Berechtigung](berechtigungen/berechtigung.md)** basiert auf hinterlegten Daten, die zur Inanspruchnahme einer ÖPV-Leistung berechtigen; sie besteht unter anderem aus einer eindeutigen ID und einem Gültigkeitszeitraum ([Q02](../QUELLEN.md#q02), S. 30).

Davon zu trennen ist das **[Produkt](berechtigungen/produkt.md)**: Der Begriff wird in der Kernapplikation im Sinne eines ÖPV-Tarifprodukts **oder** eines EFM-Produkts verwendet ([Q02](../QUELLEN.md#q02), S. 73). Das Produkt definiert der Produktverantwortliche, die Berechtigung ist die Ausprägung davon beim Kunden (abgeleitet).

Die Beziehung ist also: Ein Produkt wird einmal definiert, eine Berechtigung entsteht je Kunde. Das Produkt legt zugleich als **Produkt-Template** fest, wie seine Tarifparameter innerhalb einer Berechtigung auf dem Nutzermedium abgelegt werden ([Q02](../QUELLEN.md#q02), S. 36).

**Ablageformen** einer Berechtigung ([Q02](../QUELLEN.md#q02), S. 30): binär in einer chip-basierten oder emulierten Applikation, kopiergeschützt in einem Smartphone, als statischer Barcode auf Papier oder im Smartphone — oder **in einer Cloud, auf die mit Hilfe einer eindeutigen ID zugegriffen wird**. Die letzte Form ist bereits im Glossar des Standards vorgesehen und die Brücke zum Account Based Ticketing (abgeleitet).

Die Struktur einer Berechtigung im RMV-EFS ist bis auf die Byteebene belegt ([Q05](../QUELLEN.md#q05), Kap. 2.1), die Parameter eines Produkts je Tarif ebenso ([Q35](../QUELLEN.md#q35)) — jeweils **verbundspezifisch**.

## Einfach erklärt – Beispiel aus Bärstadt

Zwei Begriffe, die im Alltag ständig verwechselt werden, sind hier streng getrennt: Produkt und Berechtigung.

Das **Produkt** ist das Angebot. Der Bären-Verkehrsbund hat entschieden, dass es ein ABO Azubi gibt — mit bestimmten Bedingungen, einem Preis und einem Geltungsbereich. Dieses Produkt trägt die Nummer 2001 und existiert genau einmal, unabhängig davon, ob es jemand kauft.

Die **Berechtigung** ist das, was Pia Brummbär dann besitzt. Sie trägt die Nummer 400815, gilt vom 1. September 2026 bis zum 31. August 2029 und liegt auf ihrer BärenKarte. Hätte ihre Mitschülerin dasselbe Abo, wäre das dasselbe Produkt, aber eine andere Berechtigung mit anderer Nummer und anderem Zeitraum.

Der Vergleich mit einem Buch trifft es: Das Produkt ist der Titel, die Berechtigung das Exemplar im Regal.

Wichtig ist, was das Produkt über die Berechtigung hinaus bestimmt. Es legt nicht nur den Preis fest, sondern auch, **welche Felder in welcher Reihenfolge** auf der Karte stehen. Das Glossar nennt es ein „Produkt-Template“. Beim ABO Azubi gehören dazu Name und Geburtsdatum — bei einem übertragbaren Einzelfahrschein nicht.

Besonders bemerkenswert ist die Liste der Orte, an denen eine Berechtigung liegen kann. Chipkarte, Smartphone, Barcode auf Papier — und ausdrücklich auch: **in einer Cloud**, auf die man mit einer eindeutigen Kennung zugreift.

Dieser letzte Punkt steht im Glossar des Standards, nicht in einem Zukunftspapier. Account Based Ticketing ist also keine Abkehr von der Kernapplikation, sondern eine ihrer vorgesehenen Ablageformen. Das ist eine der nützlichsten Einsichten dieser Kategorie.

## Quellen

- [Q02](../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 30 („Berechtigung“: Definition, eindeutige ID und Gültigkeitszeitraum, die vier Ablageformen einschließlich Cloud), S. 36 (EFM-Produkt als Produkt-Template, Ablage der Tarifparameter im erweiterten Datenteil als TLV-EFS), S. 73 („Produkt“ als Tarifprodukt oder EFM-Produkt)
- [Q05](../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (vollständige Datenstruktur „Berechtigung“ für den RMV-EFS) · *verbundspezifisch*
- [Q35](../QUELLEN.md#q35) – KCD NRW, Produktparameter der Tarife in NRW · *verbundspezifisch*

<!-- GEN:unterartikel -->
## Unterartikel

- [Berechtigung](berechtigungen/berechtigung.md)
- [berStatus](berechtigungen/berstatus.md)
- [berSynchronNummer](berechtigungen/bersynchronnummer.md)
- [Elektronischer Fahrschein](berechtigungen/efs.md)
- [Fahrgast, Linie und Identifikationsmedium (ASN.1)](berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md)
- [Gültigkeit](berechtigungen/gueltigkeit.md)
- [Gültigkeitsbereich (ASN.1)](berechtigungen/gueltigkeitsbereich-asn-1.md)
- [Multiberechtigung](berechtigungen/multiberechtigung.md)
- [Produkt](berechtigungen/produkt.md)
- [Produktnummer](berechtigungen/produktnummer.md)
- [Produktspezifischer Teil](berechtigungen/produktspezifischer-teil.md)
- [Statische Berechtigung](berechtigungen/statische-berechtigung.md)
- [Statische Berechtigung in etiCORE](berechtigungen/statische-berechtigung-in-eticore.md)
<!-- /GEN:unterartikel -->

<!-- GEN:siehe_auch -->
## Siehe auch

- [Produktverantwortlicher](rollen/pv.md) (PV)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../README.md) · [Register](../REGISTER.md)
<!-- /GEN:navigation -->
