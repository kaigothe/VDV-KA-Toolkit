---
titel: Gültigkeitsbereich (ASN.1)
englisch: validity area in ASN.1
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/gueltigkeit.md, lexikon/datenformate/geraete-orte-und-subjekte-asn-1.md, lexikon/berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: zu prüfen
offene_fragen: [O21]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Gültigkeitsbereich (ASN.1)
<!-- /GEN:breadcrumb -->

# Gültigkeitsbereich (ASN.1)

Der räumliche Geltungsbereich eines Fahrscheins ist im Modul `et` ([Q51](../../QUELLEN.md#q51)) als `ValidityAreaList` (Tag `0xB6`) beschrieben, einer Auswahl (`CHOICE`) aus **neun Varianten** A bis I. Alle bauen auf einer `StationIdList` aus Orts-Kennungen ([Geräte, Orte und Subjekte](../datenformate/geraete-orte-und-subjekte-asn-1.md)) auf.

| Variante | Inhalt |
|---|---|
| A | Gebietsnummer (Schlüssel in der Datenbank), Anfangs- und Endstation, Zwischenstationen |
| B | Gebietsnummer und die vollständige Aufzählung aller Stationen |
| C | Anfangs- und Endstation und die Kette der Stationen dazwischen |
| D | nur die vollständige Aufzählung der Stationen |
| E bis H | wie A bis D, zusätzlich mit einer Startstation, die die Fahrtrichtung festlegt |
| I | Startstation und die Aufzählung aller möglichen Zielstationen |

Der Product Owner legt fest, welche Stationen zu einer Gebietsnummer gehören. Eingebettet wird die Liste in eine `OriginalValidityAreaList` (`0xB7`) oder eine `AlternativeValidityAreaList` (`0x30`), jeweils mit einer Typangabe (`typeDefinition`), der Organisation des Product Owners und der Liste. Die Quelle nennt nicht, was eine alternative Liste neben der ursprünglichen bedeutet (zu prüfen, O21). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Pias ABO Azubi gilt für die Linie 4 zwischen Waldsiedlung und Berufsschule Tannenweg. Wie beschreibt man das?

Der einfachste Weg ist Variante D: eine Liste aller Haltestellen, an denen das Abo gilt. Wer die Liste hat, braucht nichts nachzuschlagen. Sie ist aber lang, und jede Änderung des Fahrplans ändert die Liste.

Kürzer ist Variante A. Dort steht nur: Gebiet Nummer so-und-so, von der Waldsiedlung bis zur Berufsschule, mit den Haltestellen dazwischen. Die Gebietsnummer ist ein Schlüssel, der Bären-Verkehrsbund legt in seiner Datenbank fest, was dazugehört.

Die Varianten E bis H sind dasselbe mit einer Startstation. Sie legen fest, in welcher Richtung gefahren wird. Variante I passt zu einem Einzelfahrschein: ab dem Hauptbahnhof, und dazu eine Liste aller Orte, die man damit erreichen kann.

Eine Besonderheit bleibt: Wozu die Quelle zwei Listen vorsieht, die ursprüngliche und eine alternative, erklärt sie nicht. Das steht deshalb hier als offene Stelle.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `et`: `ValidityAreaList`, `ValidityAreaListVariantA` bis `…VariantI`, `StationIdList`, `OriginalValidityAreaList`, `AlternativeValidityAreaList` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Gültigkeit](gueltigkeit.md) – die zeitliche Gültigkeit
- [Geräte, Orte und Subjekte (ASN.1)](../datenformate/geraete-orte-und-subjekte-asn-1.md) – die Ortskennungen
- [Fahrgast, Linie und Identifikationsmedium (ASN.1)](fahrgast-linie-und-identifikationsmedium-asn-1.md) – die übrigen Angaben des Fahrscheins
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Gültigkeit](gueltigkeit.md)
- [Geräte, Orte und Subjekte (ASN.1)](../datenformate/geraete-orte-und-subjekte-asn-1.md)
- [Fahrgast, Linie und Identifikationsmedium (ASN.1)](fahrgast-linie-und-identifikationsmedium-asn-1.md)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
