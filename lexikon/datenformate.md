---
titel: Datenformate
englisch: data formats and encoding
parent: README.md
siehe_auch: [lexikon/berechtigungen.md, lexikon/transaktionen.md]
quellen: [Q02, Q05, Q06, Q12, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../README.md) › Datenformate
<!-- /GEN:breadcrumb -->

# Datenformate

Die VDV-KA verwendet **zwei getrennte Formatwelten**, und das Auseinanderhalten ist die wichtigste Einsicht dieser Kategorie.

Auf dem **Nutzermedium** liegen Daten binär, als geschachtelte **[TLV](datenformate/tlv.md)**-Strukturen mit Tags, Längen und Werten ([Q05](../QUELLEN.md#q05), Kap. 2.1). Dort zählt jedes Byte, Nullwerte sind nicht immer eine Null ([Q06](../QUELLEN.md#q06), Kap. 5.2), und Namen werden gekürzt und maskiert ([Q12](../QUELLEN.md#q12)).

Zwischen den **Hintergrundsystemen** laufen dieselben Sachverhalte als **XML**, beschrieben durch [XSD und WSDL](datenformate/xsd.md) mit festgelegten Dateinamen und [Namensräumen](datenformate/xml-namensraum.md) ([Q25](../QUELLEN.md#q25), Kap. 4.3.2 f.).

Die Brücke zwischen beiden Welten ist das **[Basisobjektmodell](datenformate/bom.md)**: Es definiert Datentypen und Codelisten, auf die beide Formate zurückgreifen ([Q25](../QUELLEN.md#q25), Kap. 3, Inventarnummer 1).

Eine dritte Form steht daneben: Der **[VDV-Barcode](datenformate/vdv-barcode.md)** nimmt eine statische Berechtigung als signierten Datensatz auf und bringt sie auf Papier oder Smartphone ([Q02](../QUELLEN.md#q02), S. 92).

Für das geplante Analysewerkzeug ist diese Kategorie die eigentliche Grundlage: Eine Nachricht lesen heißt, XML zu zerlegen, darin Bytestrings zu finden, diese als TLV zu deuten — und bei jedem Schritt zu wissen, welche Codeliste gilt (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Wer eine KA-Nachricht zum ersten Mal sieht, erlebt eine Überraschung: Es sind zwei Formate ineinander.

Außen ist es XML — Spitze Klammern, Elementnamen, lesbar. Man erkennt `berStatus`, `prodProdukt_ID`, Datumsangaben. Das ist die Sprache, in der die Rechenzentren miteinander reden.

Dann kommt ein Feld, in dem nur noch Hexadezimalzahlen stehen: `85 57 00 00 4D 78 …`. Hier endet die lesbare Welt und beginnt die der Chipkarte.

Der Grund für diesen Bruch ist Platz. Auf Pias BärenKarte stehen für eine ganze Berechtigung vielleicht 225 Byte zur Verfügung. XML wäre dort völlig ausgeschlossen — allein der Elementname `berGueltigkeitsbeginn` verbraucht mehr Zeichen als das Datum selbst Bytes.

Also wird auf der Karte radikal gespart. Statt Namen gibt es Zahlen-Kennungen, sogenannte Tags. Statt Trennzeichen gibt es Längenangaben. Statt Klartext gibt es Codelisten, in denen eine 7 „aktiv" bedeutet.

Wenn eine Nachricht ans Rechenzentrum geht, wird dieser Byteblock nicht übersetzt, sondern **mitgenommen** — als ein Feld innerhalb des XML. Das hat einen guten Grund: Über genau diese Bytes wurde die kryptografische Sicherung gebildet. Würde man sie umformatieren, wäre die Prüfsumme nicht mehr gültig.

Daraus folgt die Arbeitsweise für jedes Auswertungswerkzeug: erst das XML zerlegen, dann die darin eingebetteten Bytes als TLV lesen, und bei jedem Wert in der richtigen Codeliste nachschlagen.

Die Unterartikel gehen diese Schritte einzeln durch — und benennen jeweils, was belegt ist und was nicht.

## Quellen

- [Q05](../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (TLV-Struktur der Berechtigung) · *verbundspezifisch*
- [Q06](../QUELLEN.md#q06) – RMV PH 06-02, Kap. 5.2 (Kodierung von Nullwerten in Bytestrings) · *verbundspezifisch*
- [Q12](../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings (feldweise Abbildung mit Verweisen in KA HD_BOM-Spec, Anlage TLV EFS und KA STB-SPEC) · *Herstellerquelle*
- [Q25](../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA BOM-SPEC Inv. 1, Anlage TLV EFS Inv. 2, KA XML-Schemata und WSDL Inv. 5, KA STB-Spec Inv. 42), Kap. 4.3.2 f. (Namenskonventionen für XSD, WSDL und Namensräume)
- [Q02](../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 92 (statische Berechtigung), S. 96 (TLV-EFS)

<!-- GEN:unterartikel -->
## Unterartikel

- [Basisobjektmodell](datenformate/bom.md)
- [Kürzungsregel für Namen](datenformate/kuerzungsregel-fuer-namen.md)
- [Nullwerte](datenformate/nullwerte.md)
- [Tag 0xDB Fahrgast](datenformate/tag-0xdb-fahrgast.md)
- [TLV-Kodierung](datenformate/tlv.md)
- [UIC-Barcode](datenformate/uic-barcode.md)
- [VDV-Barcode](datenformate/vdv-barcode.md)
- [XML-Namensraum](datenformate/xml-namensraum.md)
- [XSD und WSDL](datenformate/xsd.md)
<!-- /GEN:unterartikel -->

<!-- GEN:siehe_auch -->
## Siehe auch

- [Berechtigungen](berechtigungen.md)
- [Transaktionen](transaktionen.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../README.md) · [Register](../REGISTER.md)
<!-- /GEN:navigation -->
