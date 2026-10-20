---
titel: Check-in und Check-out
abkuerzung: CICO
englisch: check-in and check-out
parent: lexikon/abt.md
siehe_auch: [lexikon/berechtigungen/fahrtberechtigung.md, lexikon/berechtigungen/bezahlart.md, lexikon/datenformate/fahrtdaten-asn-1.md, lexikon/transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md]
quellen: [Q02, Q36, Q50, Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Account Based Ticketing](../abt.md) › Check-in und Check-out
<!-- /GEN:breadcrumb -->

# Check-in und Check-out

In einem **IN-OUT-System** legt das Medium beim Einsteigen automatisch einen *teilweisen* Erfassungsnachweis in der Applikation an und ergänzt ihn im Lauf der Fahrt, meist beim Aussteigen. Möglich sind Check-in/Check-out (CICO), Be-in/Be-out (BIBO) und Check-in/Be-out (CIBO). Der Teilnachweis vom Fahrtbeginn gilt als Nachweis einer gültigen Berechtigung ([Q02](../../QUELLEN.md#q02), S. 47).

Ein **erneuter Check-in innerhalb einer Reise** folgt auf einen Check-out nach einem Umstieg. Das Terminal prüft nach den Regeln des Product Owners, ob es noch dieselbe Reise ist, etwa an „Check-in-Ort = vorhergehender Check-out-Ort + erlaubte Zeitspanne“ ([Q02](../../QUELLEN.md#q02), S. 32). Beim Preis ermöglicht die trip-priced-Ermittlung mit einem Nutzungszähler die Bestpreisberechnung ([Q02](../../QUELLEN.md#q02), S. 42 f.; [Bezahlart](../berechtigungen/bezahlart.md)).

Für die eTarife in NRW gilt, dass ein automatischer Check-out einem aktiven gleichsteht und die Tarifierung der Fahrt abschließt. Gibt es sieben Stunden nach dem Check-in keinen Check-out und wird eine Fahrt durchgeführt, endet die Fahrt an der letzten erfassten Haltestelle ([Q36](../../QUELLEN.md#q36), S. 23, 26) · *verbundspezifisch: NRW*.

In etiCORE bescheinigen `CheckinAttestation` und `CheckoutAttestation` die Vorgänge; `CicoPaymentParameters` tragen Linienvariante, Fahrt, Haltestelle und den bereits bezahlten Betrag ([Q51](../../QUELLEN.md#q51), Modul `user-medium`; [Fahrtdaten](../datenformate/fahrtdaten-asn-1.md)). Fehler wie `E_EUI_NO_CHECKIN_FOUND` und `E_CCP_REFERENCED_CICO_NOTIFICATION_NOT_FOUND_IN_DATABASE` prüfen die Zusammengehörigkeit ([Q50](../../QUELLEN.md#q50)). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Olli Tapsig steigt am Hauptbahnhof in die Linie 4 und hält seine Karte ans Lesegerät: Check-in. Das Gerät schreibt einen halben Beleg auf die Karte, wo und wann er eingestiegen ist. Dieser halbe Beleg genügt schon als Nachweis, dass er fahren darf.

An der Berufsschule Tannenweg steigt er aus und meldet sich ab: Check-out. Der Beleg ist jetzt vollständig, die Fahrt lässt sich abrechnen.

Wechselt er unterwegs die Bahn, meldet er sich wieder an. Das Gerät fragt nach den Regeln des Verbunds: Ist die neue Haltestelle dieselbe wie die letzte Abmeldung, und ist nicht zu viel Zeit vergangen? Dann gilt es als dieselbe Reise, und der Preis wird für die ganze Reise berechnet, nicht für zwei einzelne Fahrten.

Vergisst Olli sich abzumelden, hilft in manchen Systemen die Automatik. In NRW etwa endet die Fahrt nach sieben Stunden an der zuletzt erfassten Haltestelle, und das System stellt eine neue Berechtigung aus. Wie das im Bärenland geregelt ist, regelt der Bären-Verkehrsbund selbst.

Und noch ein Wort zum Namen: Bei BIBO, Be-in/Be-out, ist kein bewusstes Anmelden nötig. Das Glossar nennt als Beispiel eine Funkverbindung über Bluetooth Low Energy ([Q02](../../QUELLEN.md#q02), S. 99).

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 47 (*IN-OUT-System*), S. 32 (*Check-in innerhalb einer Reise*), S. 42 f. (*Automatisierte Fahrpreisermittlung*), S. 99 (*Wide Range*)
- [Q36](../../QUELLEN.md#q36) – KCD NRW, Vertriebliche Umsetzung der eTarife in NRW v1.8 (04.03.2026), Kap. 4, S. 23 und S. 26 (automatischer Check-out, Sieben-Stunden-Regel) · *verbundspezifisch: NRW*
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium` und `payment`: `CheckinAttestation`, `CheckoutAttestation`, `CicoPaymentParameters` · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `eui-event-enums_xsd`, `ccp-event-enums_xsd`: Fehlercodes zu Check-in/Check-out · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Fahrtberechtigung](../berechtigungen/fahrtberechtigung.md) – was beim Check-in entsteht
- [Bezahlart](../berechtigungen/bezahlart.md) – wann der Preis festgelegt wird
- [Fahrtdaten (ASN.1)](../datenformate/fahrtdaten-asn-1.md) – die Daten in etiCORE
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md) – die Nachweise

<!-- GEN:siehe_auch -->
## Siehe auch

- [Fahrtberechtigung](../berechtigungen/fahrtberechtigung.md)
- [Bezahlart](../berechtigungen/bezahlart.md)
- [Fahrtdaten (ASN.1)](../datenformate/fahrtdaten-asn-1.md)
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Account Based Ticketing](../abt.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
