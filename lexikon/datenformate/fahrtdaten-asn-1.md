---
titel: Fahrtdaten (ASN.1)
englisch: trip data in ASN.1
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/zahlungsmittel-asn-1.md, lexikon/berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Fahrtdaten (ASN.1)
<!-- /GEN:breadcrumb -->

# Fahrtdaten (ASN.1)

Für Check-in, Check-out und Validierung bündelt das Modul `payment` ([Q51](../../QUELLEN.md#q51)) die Angaben zur Fahrt.

- `CicoPaymentParameters` (`0x7F39`) enthält Linienvariante, Fahrt, aktuelle Haltestelle und den bereits bezahlten Betrag der Fahrt in kleinster Währungseinheit. Dieser Betrag ist zu Beginn null, wird bei einem fortgesetzten Check-in vom Check-out übernommen und nur beim Check-out neu berechnet.
- `InitialTripSegment` (`0xB5`) kennzeichnet das erste Teilstück der Reise: Zeitstempel, Haltestelle und Aktionszähler des Anfangs. Es ist Pflicht bei Check-out-Bescheinigungen und fortsetzenden Check-in-Bescheinigungen.
- `LineId`, `LineVariantId` und `TripId` machen Linie, Linienvariante und Fahrt eindeutig; jede besteht aus einer Nummer und der Organisation, die sie vergibt. `CurrentStopId` ist eine Orts-Kennung.

Daneben stehen `Line` und `LineTripNumber` im Modul `et` ([Fahrgast, Linie und Identifikationsmedium](../berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md)). Dass beides nebeneinander besteht, deutet auf zwei Einsatzzwecke hin, den Fahrschein und den Nachweis einer Fahrt (abgeleitet). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Olli Tapsig fährt mit seinem Guthaben. Beim Einsteigen an der Haltestelle meldet er sich an, beim Aussteigen ab; abgerechnet wird nach der Fahrt.

Beim Anmelden hält das System fest, auf welcher Linie er fährt, in welcher Variante der Linie und mit welcher Fahrt. Jede dieser Angaben besteht aus einer Nummer und dem Betrieb, der sie vergeben hat, denn Liniennummern sind nur zusammen mit ihrem Vergeber eindeutig. Dazu kommt die Haltestelle, an der er gerade ist, und bisher bezahlt ist null.

Steigt er um, ohne dass die Reise endet, hängt das System an das erste Teilstück an: Wann und wo ging die Reise los? Das merkt sich das erste Teilstück mit Zeit, Haltestelle und Aktionszähler. Beim Abmelden rechnet es den Preis der ganzen Reise aus und trägt den Betrag ein. Setzt Olli die Reise später fort, übernimmt die Anmeldung diesen Betrag.

Warum so umständlich? Weil kein einzelner Moment die ganze Reise kennt. Jede Bescheinigung enthält deshalb gerade so viel Vorgeschichte, dass die nächste daran anknüpfen kann.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `payment`: `CicoPaymentParameters`, `InitialTripSegment`, `LineId`, `LineVariantId`, `TripId`, `CurrentStopId` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Zahlungsmittel (ASN.1)](zahlungsmittel-asn-1.md) – die übrigen Zahlungsparameter
- [Fahrgast, Linie und Identifikationsmedium (ASN.1)](../berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md) – `Line` und `LineTripNumber`
- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Zahlungsmittel (ASN.1)](zahlungsmittel-asn-1.md)
- [Fahrgast, Linie und Identifikationsmedium (ASN.1)](../berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md)
- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
