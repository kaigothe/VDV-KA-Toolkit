---
titel: Produkt
englisch: product
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/produktnummer.md, lexikon/rollen/pv.md]
quellen: [Q02, Q35]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Produkt
<!-- /GEN:breadcrumb -->

# Produkt

„Der Begriff Produkt wird in der Kernapplikation im Sinne eines **ÖPV-Tarifprodukts** oder eines **EFM-Produkts** verwendet.“ ([Q02](../../QUELLEN.md#q02), S. 73) Beide Bedeutungen sind zu trennen.

Ein **EFM-Produkt** wird vom [Produktverantwortlichen](../rollen/pv.md) definiert und kann **ein oder mehrere Tarifprodukte** für die Verwendung im EFM abbilden. Es muss für diesen Produktverantwortlichen eine eindeutige Nummer besitzen und zusammen mit dessen Organisations-ID **im gesamten EFM-System eindeutig** sein ([Q02](../../QUELLEN.md#q02), S. 36).

Definiert wird es hinsichtlich seiner **Nutzungsregeln und Preisbildung**. Zugleich legt es als **Produkt-Template** fest, wie die Tarifparameter in Form der spezifizierten Datenelemente auf dem Nutzermedium innerhalb einer Berechtigung abgelegt werden; diese Daten sind Bestandteil der Berechtigung und liegen im erweiterten Datenteil in der Regel als [TLV-EFS](produktspezifischer-teil.md) ([Q02](../../QUELLEN.md#q02), S. 36).

Damit ermöglichen die abgelegten Produktdaten drei Funktionen ([Q02](../../QUELLEN.md#q02), S. 36): die Preisberechnung, die Durchführung der automatischen Kontrolle sowie Kontrolle und automatisierte Preisberechnung in IN-OUT-Systemen.

Die Praxis in NRW bestätigt die Zweiteilung und zeigt sie als getrennte Parameter: **Tarifproduktnummer** je Produktverantwortlichem — im VRS auch „Servicenummer“, im WestfalenTarif als „TicketArtCode“ bezeichnet — und **EFM-Produktnummer**. „Mehrere Tarifprodukte können zu einem EFM-Produkt zusammengefasst werden.“ ([Q35](../../QUELLEN.md#q35)) · *verbundspezifisch*

## Einfach erklärt – Beispiel aus Bärstadt

„Produkt“ heißt in der VDV-KA zwei verschiedene Dinge, und wer das übersieht, redet schnell aneinander vorbei.

Das **Tarifprodukt** ist die kaufmännische Sicht. Es steht im Tarif des Bären-Verkehrsbunds, hat einen Preis und Bedingungen, und Pia hat es im Kundencenter gekauft: „ABO Azubi“.

Das **EFM-Produkt** ist die technische Sicht. Es ist der Datensatz, der beschreibt, wie dieses Abo auf eine Karte kommt — welche Felder, welche Nummern, welche Gültigkeitsregeln.

Meist entspricht eines dem anderen. Es muss aber nicht: **Mehrere Tarifprodukte können zu einem EFM-Produkt zusammengefasst werden.** Hätte der Verkehrsbund ein ABO Azubi und ein ABO Schüler mit gleichem technischen Aufbau und nur verschiedenen Preisen, könnten beide dasselbe EFM-Produkt verwenden. Für Pia zwei Angebote, für die Karte eine Struktur.

Besonders folgenreich ist die Rolle des Produkts als **Vorlage**. Das EFM-Produkt bestimmt nicht nur, was etwas kostet, sondern welche Felder auf der Karte stehen und in welcher Reihenfolge. Beim ABO Azubi gehören Name und Geburtsdatum dazu — sonst könnte Petra Pranke bei der Kontrolle nicht prüfen, ob Pia die Berechtigte ist.

Das erklärt eine Beobachtung, die beim Auswerten von Nachrichten immer wiederkehrt: Ohne das Produktschema lässt sich der produktspezifische Teil einer Berechtigung nicht deuten. Dort liegen Bytes, deren Bedeutung ausschließlich im Produkt definiert ist. Wer das Schema nicht hat, sieht Hexadezimalzahlen und kann raten.

Und schließlich: Die Produktnummer allein genügt nie. Produkt 2001 heißt beim Bären-Verkehrsbund ABO Azubi — beim Nachbarverbund könnte 2001 etwas völlig anderes sein.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 73 („Produkt“ als Tarifprodukt oder EFM-Produkt), S. 36 („EFM Produkt“: Definition durch den PV, Abbildung eines oder mehrerer Tarifprodukte, Eindeutigkeit der Nummer je PV und gemeinsam mit der Org-ID im gesamten EFM-System, Definition über Nutzungsregeln und Preisbildung, Produkt-Template für die Ablage der Tarifparameter als TLV-EFS, die drei ermöglichten Funktionen), S. 94 („Tarifprodukt“)
- [Q35](../../QUELLEN.md#q35) – KCD NRW, Produktparameter der Tarife in NRW, V1.0 (Tarifproduktnummer bzw. Verkaufsproduktnummer je PV, im VRS „Servicenummer“, im WestfalenTarif „TicketArtCode“; EFM-Produktnummer; Zusammenfassung mehrerer Tarifprodukte zu einem EFM-Produkt) · *verbundspezifisch: NRW*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Produktnummer](produktnummer.md)
- [Produktverantwortlicher](../rollen/pv.md) (PV)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
