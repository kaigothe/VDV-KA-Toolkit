---
titel: Fahrgast, Linie und Identifikationsmedium (ASN.1)
englisch: passenger, line and identification medium in ASN.1
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/gueltigkeitsbereich-asn-1.md, lexikon/datenformate/tag-0xdb-fahrgast.md, lexikon/grundlagen/datenschutz.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 0
    codeliste: IdentificationMediumTypeEnum
    bedeutung: unspecified
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: IdentificationMediumTypeEnum
    bedeutung: girocard — Girocard (kind of of German debit card)
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: IdentificationMediumTypeEnum
    bedeutung: creditcard — Credit card
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 3
    codeliste: IdentificationMediumTypeEnum
    bedeutung: public-transport-customer-card — Public transport customer card
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 4
    codeliste: IdentificationMediumTypeEnum
    bedeutung: identify-card — Identify card
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 5
    codeliste: IdentificationMediumTypeEnum
    bedeutung: passport
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 6
    codeliste: IdentificationMediumTypeEnum
    bedeutung: telephone-number — Telephone number
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 7
    codeliste: IdentificationMediumTypeEnum
    bedeutung: social-passport — Social passport
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 8
    codeliste: IdentificationMediumTypeEnum
    bedeutung: pupil-id — Student ID for pupils
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 9
    codeliste: IdentificationMediumTypeEnum
    bedeutung: student-id — Student ID
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 10
    codeliste: IdentificationMediumTypeEnum
    bedeutung: client-id — Client ID (classifies the client device itself as medium)
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 11
    codeliste: IdentificationMediumTypeEnum
    bedeutung: device-id — Device ID (IMEI-Number)
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 12
    codeliste: IdentificationMediumTypeEnum
    bedeutung: only-valid-on-security-paper — Only valid on security paper
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 13
    codeliste: IdentificationMediumTypeEnum
    bedeutung: only-valid-on-security-paper-for-validatable-tickets — Only valid on security paper (for validatable tickets)
    quelle: Q51
    fundstelle: Modul et, Typ IdentificationMediumTypeEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Fahrgast, Linie und Identifikationsmedium (ASN.1)
<!-- /GEN:breadcrumb -->

# Fahrgast, Linie und Identifikationsmedium (ASN.1)

Weitere Angaben des elektronischen Fahrscheins im Modul `et` ([Q51](../../QUELLEN.md#q51)); alle Felder sind optional.

- `Passenger` (`0xB2`): Vorname, Nachname, Geburtsdatum und Geschlecht. Das sind personenbezogene Daten, siehe [Datenschutz](../grundlagen/datenschutz.md).
- `IdentificationMedium` (`0xB3`): Art des Mediums, mit dem sich der Fahrgast ausweist, und dessen interne Nummer. `IdentificationMediumTypeEnum` hat 14 Werte, von Girocard und Kreditkarte über Schüler- und Studierendenausweis bis zum Gerätekennzeichen und dem Hinweis, ein Fahrschein sei nur auf Sicherheitspapier gültig.
- `Line` (`0xBA`): Linie mit Betreiber, Liniennummer, Product Owner und Zielhaltestelle. `LineTripNumber`: Betreiber, Linie und Fahrtnummer.
- `ProductProperties` (`0xB0`): Zahlungsmittel, Fahrgastart, Begleitpersonen, Fahrzeugart, Beförderungsklasse, Preis in Eurocent, Mehrwertsteuersatz in Hundertstel Prozent (1900 heißt 19 %), Preiskategorie und eine interne Produktnummer.
- `ProductOwnerContainer` (`0xBC`): Bytefolgen, in denen der Product Owner „requirements on a product“ unterbringt.

Die Aufzählungen zu Fahrgastart, Fahrzeug, Klasse und Zahlungsmittel stehen in den Artikeln zu [Tarif](../datenformate/tarifaufzaehlungen-asn-1.md) und [Zahlungsmittel](../datenformate/zahlungsmittel-asn-1.md). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Der Fahrschein ist wie ein Formular mit vielen Kästchen, die alle freiwillig sind. Welche ausgefüllt werden, bestimmt das Produkt.

Pias ABO Azubi ist tariflich personalisiert: Name und Geburtsdatum stehen auf dem Medium. Im Formular sind das die Kästchen für Vor- und Nachnamen und das Geburtsdatum. Für Olli Tapsigs Einzelfahrschein bleiben sie leer, er ist nicht personalisiert und übertragbar. Gerade weil es um Personendaten geht, ist die Freiwilligkeit kein Zufall.

Die Tageskarte Familie zeigt die Kästchen für Begleitpersonen: Eine Mutter reist mit zwei Kindern. Im Formular stünde als Begleitart „Kind“ und als Anzahl 2. Wie das für die Familie Tatze im Bärenland tatsächlich festgelegt ist, regelt der Bären-Verkehrsbund.

Manche Produkte verlangen, dass man sich ausweist. Dann steht im Formular die Art des Ausweises, etwa ein Schülerausweis, und dessen Nummer. Und es gibt Kästchen für den Preis in Cent, den Steuersatz und die Preiskategorie, die man auf einem Beleg ablesen könnte.

Zuletzt gibt es ein freies Fach, in dem der Verbund Anforderungen an das Produkt unterbringen kann, die kein Standard vorhersehen konnte.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `et`: `Passenger`, `IdentificationMedium`, `IdentificationMediumTypeEnum`, `Line`, `LineTripNumber`, `ProductProperties`, `ProductOwnerContainer`, `Accompaniments` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Gültigkeitsbereich (ASN.1)](gueltigkeitsbereich-asn-1.md) – der räumliche Geltungsbereich
- [Tag 0xDB Fahrgast](../datenformate/tag-0xdb-fahrgast.md) – die Fahrgastdaten im VDV-Barcode
- [Datenschutz](../grundlagen/datenschutz.md) – Grundsätze zu personenbezogenen Daten
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Gültigkeitsbereich (ASN.1)](gueltigkeitsbereich-asn-1.md)
- [Tag 0xDB Fahrgast](../datenformate/tag-0xdb-fahrgast.md)
- [Datenschutz](../grundlagen/datenschutz.md)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
