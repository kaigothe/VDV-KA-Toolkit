---
titel: Tarif
englisch: tariff
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/produkt.md, lexikon/berechtigungen/gueltigkeitsbereich-asn-1.md, lexikon/datenformate/tarifaufzaehlungen-asn-1.md, lexikon/transaktionen/fehlercodes-eticore.md]
quellen: [Q02, Q50, Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Tarif
<!-- /GEN:breadcrumb -->

# Tarif

Ein **Tarif** ist im ÖPV „ein Vertrag oder ein Vertragsbestandteil mit einer Aufzählung von festen Bedingungen für das Erbringen von Leistungen im Rahmen eines Beförderungsvertrages“. Die Bedingungen heißen Tarif, wenn ein Anbieter sie einseitig vielen möglichen Vertragspartnern gleichermaßen anbietet ([Q02](../../QUELLEN.md#q02), S. 93).

Ein **Tarifprodukt** ist ein „standardisiertes Leistungsangebot für die Nutzung des ÖPV“. Es wird bestimmt durch den Leistungsanspruch (zeitlich-räumliche Gültigkeit u. a.), die Produktart, die beförderungsrechtlichen Bedingungen (etwa Alter oder Status wie Schüler und Rentner) und den Produktpreis. Zusatznutzen wie Ersatz bei Verlust können es erweitern ([Q02](../../QUELLEN.md#q02), S. 94).

In etiCORE tauchen diese Bestandteile als Felder und Aufzählungen auf ([Q51](../../QUELLEN.md#q51)): Gültigkeit und [Gültigkeitsbereich](gueltigkeitsbereich-asn-1.md), Produktart (`ProductTypeEnum`), Fahrgastart (`PassengerTypeEnum`), Beförderungsklasse und Verkehrsmittel (siehe [Tarifaufzählungen](../datenformate/tarifaufzaehlungen-asn-1.md)) sowie in den `ProductProperties` Preis in Eurocent, Mehrwertsteuersatz und Preiskategorie. Ein Verstoß der Produktparameter gegen die Tarifregeln wird mit `E_POOAM_INVALID_PRODUCT_PARAMETERS` abgewiesen ([Q50](../../QUELLEN.md#q50)). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Ein Tarif ist das Preisschild mit dem Kleingedruckten. Wer ihn anbietet, bietet ihn jedem an, zu denselben Bedingungen.

Der Bären-Verkehrsbund hat Tarife für die Stadt Bärstadt. Aus ihnen macht er Produkte: das ABO Azubi, den Einzelfahrschein Bärstadt, die Monatskarte, die Tageskarte Familie. Jedes Produkt beantwortet vier Fragen. Was darf man damit? (Linie 4, Bärstadt, ein Monat.) Was für ein Produkt ist es? (Abo, Einzelfahrt.) Wer darf es nutzen? (Auszubildende, Familien.) Und was kostet es?

Das ABO Azubi ist an einen Status geknüpft. Deshalb prüft Bodo Bärlauch im Kundencenter einen Ausbildungsnachweis, bevor er es ausstellt.

Ein Produkt kann einen Zusatz bekommen, zum Beispiel Ersatz bei Verlust. Als Pia ihre Karte verliert, zeigt sich, ob das dazugehört.

In etiCORE sind diese vier Fragen Felder auf der Karte und im Auftrag. Ist darin etwas, das gegen die Tarifregeln verstößt, etwa eine Angabe, die der Tarif nicht zulässt, lehnt das Aktionsmanagement den Auftrag mit einem eigenen Fehlercode ab.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 93 (*Tarif*), S. 94 (*Tarifprodukt / Tariff Product*) (wörtliche Definitionen)
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Module `common`, `et`, `tariff` · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management-event-enums_xsd`: `E_POOAM_INVALID_PRODUCT_PARAMETERS` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Produkt](produkt.md) – das Produkt im Fahrgeldmanagement
- [Gültigkeitsbereich (ASN.1)](gueltigkeitsbereich-asn-1.md) – die räumliche Gültigkeit
- [Tarifaufzählungen (ASN.1)](../datenformate/tarifaufzaehlungen-asn-1.md) – Fahrgastart, Klasse, Verkehrsmittel
- [Fehlercodes (etiCORE)](../transaktionen/fehlercodes-eticore.md) – Abweisung bei Tarifverstoß

<!-- GEN:siehe_auch -->
## Siehe auch

- [Produkt](produkt.md)
- [Gültigkeitsbereich (ASN.1)](gueltigkeitsbereich-asn-1.md)
- [Tarifaufzählungen (ASN.1)](../datenformate/tarifaufzaehlungen-asn-1.md)
- [Fehlercodes (etiCORE)](../transaktionen/fehlercodes-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
