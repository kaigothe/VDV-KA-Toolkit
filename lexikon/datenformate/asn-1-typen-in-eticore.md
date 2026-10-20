---
titel: ASN.1-Typen in etiCORE
englisch: ASN.1 types in etiCORE
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/tlv.md, lexikon/datenformate/xsd.md, lexikon/grundlagen/spezifikationsmodell.md, lexikon/berechtigungen/statische-berechtigung-in-eticore.md]
quellen: [Q50, Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › ASN.1-Typen in etiCORE
<!-- /GEN:breadcrumb -->

# ASN.1-Typen in etiCORE

ASN.1 beschreibt in etiCORE die **binären Datenstrukturen** auf dem Nutzermedium und im SAM. Die Systemschnittstellen sind getrennt als WSDL und XSD dokumentiert ([Q50](../../QUELLEN.md#q50)). Die Beschreibung ist in neun Module gegliedert ([Q51](../../QUELLEN.md#q51), Index): *Ticketing* mit Electronic Ticket (`et`), Payment, Static Entitlement (`ste`), Tariff und User Medium (`user-medium`), sowie *Common and Security* mit `common`, `cv-certificates`, MOTICS (`motics`) und `sam`. Zusammen sind es 220 Typen.

Jeder Typ hat dieselbe Gestalt ([Q51](../../QUELLEN.md#q51), etwa Modul `ste`): Name, kurze Beschreibung, **Tag** in Hexadezimalschreibweise und die Art des Typs. Es gibt `SEQUENCE` (Folge benannter Felder), `SEQUENCE OF` (Liste mit Anzahlangabe, etwa `[1, *]`), `CHOICE` (Auswahl), `ENUMERATED` (Aufzählung mit Wert und Bezeichner) und `RESTRICTION` (eingeschränkter Grundtyp wie `INTEGER` oder `OCTET STRING`, teils mit Längenbereich). Eine Feldtabelle nennt je Feld Tag, Namen, Typ, ob es optional ist, und eine Beschreibung.

Dieselbe Tag-Nummer kommt in verschiedenen Typen vor, etwa `0x81` bei `ProductNumber`, `DeviceTypeCode` und `LocationSchemaTypeCode`. Welches Feld ein Tag meint, hängt demnach vom umgebenden Typ ab (abgeleitet).

Mehrere Aufzählungen verweisen auf EN 1545-1:2015 oder -2:2015, etwa `DeviceTypeEnum` und `AppStatusEnum` ([Q51](../../QUELLEN.md#q51)). Das Format ähnelt dem [TLV](tlv.md) der KA 1.x; ein Vergleich steht hier nicht an. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Wenn Pia ihre BärenKarte beim Kundencenter am Honigmarkt abgibt, sieht der Bildschirm von Bodo Bärlauch eine Liste von Feldern: Produkt, Gültigkeit, Status. Dahinter liegt auf der Karte ein dichter Datensatz, in dem jedes Feld eine Nummer trägt, das Tag.

Man kann sich die Beschreibung wie einen Bauplan für Schubladen vorstellen. Jede Schublade hat eine Nummer, einen Namen, einen Inhaltstyp und ein Schild „darf leer bleiben“ oder „muss befüllt sein“. Manche Schubladen enthalten wieder Schubladen. Das ist die `SEQUENCE`. Andere enthalten viele gleiche Fächer in einer Reihe, das ist die `SEQUENCE OF`.

Ein Kniff: Die Nummer allein sagt nicht, was in der Schublade liegt. Die Nummer `0x81` steht bei der Produktnummer, beim Gerätetyp und beim Ortsschema. Erst der Schrank, in dem sie hängt, macht sie eindeutig. Wer einen Datensatz liest, muss also immer wissen, in welchem Schrank er gerade steht.

Für das spätere Auswertungswerkzeug ist das der Grund, warum die Typbeschreibung die Grundlage ist: Ohne sie sind Nummern nur Nummern.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6: Index und Typbeschreibungen der Module `ste`, `common`, `user-medium` · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: Systemschnittstellen als WSDL und XSD

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [TLV](tlv.md) – das Format der KA 1.x
- [XSD](xsd.md) – die Schemasprache der Systemschnittstellen
- [Spezifikationsmodell](../grundlagen/spezifikationsmodell.md) – woher die Typen stammen
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md) – das Modul `ste`

<!-- GEN:siehe_auch -->
## Siehe auch

- [TLV-Kodierung](tlv.md) (TLV)
- [XSD und WSDL](xsd.md) (XSD)
- [Spezifikationsmodell](../grundlagen/spezifikationsmodell.md)
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
