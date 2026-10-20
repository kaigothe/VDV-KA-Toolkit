---
titel: eBezahlberechtigung
abkuerzung: eBezBer
englisch: ePaymentMethod
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/berechtigung.md, lexikon/berechtigungen/werteinheitenberechtigung.md, lexikon/berechtigungen/fahrtberechtigung.md, lexikon/transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md]
quellen: [Q02, Q50, Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › eBezahlberechtigung
<!-- /GEN:breadcrumb -->

# eBezahlberechtigung

Die **eBezahlberechtigung** wird mit den Datenstrukturen einer in der Applikation hinterlegten [Berechtigung](berechtigung.md) realisiert. Sie ist die Instanz eines Bezahlmittels, mit dem man ÖPV-Tickets bezahlt oder das als [Automatisierte Fahrtberechtigung](fahrtberechtigung.md) in einem IN-OUT-System dient ([Q02](../../QUELLEN.md#q02), S. 15).

Ihr Typ legt fest, ob sie **kontobasiert** ist (prepaid oder postpaid) oder mit **Werteinheiten** auf dem Medium arbeitet ([Werteinheitenberechtigung](werteinheitenberechtigung.md)). Anonym ist sie nur als Werteinheiten-Variante ohne Autoload; kontobasierte sind nie anonym, weil das Hintergrundsystem den Kunden kennt ([Q02](../../QUELLEN.md#q02), S. 15). Sie ist noch keine Fahrtberechtigung: Die entsteht erst durch einen Check-in ([Q02](../../QUELLEN.md#q02), S. 28 f.). Kürzel: PM, eBezBer.

In etiCORE sind es vier Produkttypen: interoperables und nicht interoperables kontobasiertes Zahlungsmittel (2, 3) und ebensolches Guthaben-Zahlungsmittel (4, 5) ([Q51](../../QUELLEN.md#q51), `ProductTypeEnum`; [Organisation und Produkt](../datenformate/organisation-und-produkt-asn-1.md)). Aktionen darauf bescheinigen die [Bescheinigungen zu Zahlungsmitteln](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md). Ein Guthaben-Zahlungsmittel kann nicht entwertet werden (`E_EUI_WRONG_PRODUCT_TYPE_FOR_ACTION`, [Q50](../../QUELLEN.md#q50)). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Olli Tapsig fährt nur gelegentlich und will keine Spuren hinterlassen. Er lädt Guthaben auf seine BärenKarte, ohne einen Vertrag abzuschließen. Das ist eine eBezahlberechtigung mit Werteinheiten, anonym: Für das Hintergrundsystem der BVB ist er ein Unbekannter.

Anders bei einer kontobasierten eBezahlberechtigung: Hätte Pia ein Konto bei der BVB, wüsste das Hintergrundsystem, wer sie ist, denn ohne Konto geht es nicht. Dafür kann sie alles nachträglich abrechnen lassen.

Möchte Olli später eine Automatik, die sein Guthaben von selbst auffüllt, braucht er dazu ein Konto. Die Automatik verlangt einen Vertrag, also ist er nicht mehr anonym.

Wichtig für den Alltag: Die eBezahlberechtigung allein bringt Olli noch nicht in die Linie 4. Sie ist der Geldbeutel, nicht die Fahrkarte. Erst wenn er sich beim Einsteigen anmeldet, entsteht die Berechtigung für diese eine Fahrt.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 15 f. (*eBezahlberechtigung / ePaymentMethod*), S. 28 f. (Kürzel PM und eBezBer)
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `common`: `ProductTypeEnum` · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `eui-event-enums_xsd`: `E_EUI_WRONG_PRODUCT_TYPE_FOR_ACTION` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Berechtigung](berechtigung.md) – der Oberbegriff
- [Werteinheitenberechtigung](werteinheitenberechtigung.md) – die Variante mit Werteinheiten
- [Fahrtberechtigung](fahrtberechtigung.md) – was daraus beim Check-in wird
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md) – die Nachweise in etiCORE

<!-- GEN:siehe_auch -->
## Siehe auch

- [Berechtigung](berechtigung.md)
- [Werteinheitenberechtigung](werteinheitenberechtigung.md) (WEB)
- [Fahrtberechtigung](fahrtberechtigung.md)
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
