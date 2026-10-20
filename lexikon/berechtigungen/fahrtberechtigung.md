---
titel: Fahrtberechtigung
englisch: trip entitlement
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/ebezahlberechtigung.md, lexikon/berechtigungen/werteinheitenberechtigung.md, lexikon/abt/account.md, lexikon/datenformate/fahrtdaten-asn-1.md]
quellen: [Q02]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Fahrtberechtigung
<!-- /GEN:breadcrumb -->

# Fahrtberechtigung

Die **Fahrtberechtigung** (Trip-Entitlement) verweist im Glossar auf die [Berechtigung](berechtigung.md) ([Q02](../../QUELLEN.md#q02), S. 42). Im Account Based Ticketing sind Fahrtberechtigungen „nicht mehr auf physischen Nutzermedien gespeichert“, sondern über eine eindeutige ID mit dem Kundenkonto verknüpft ([Q02](../../QUELLEN.md#q02), S. 16).

Die **Automatisierte Fahrtberechtigung** (AFB, IN-OUT-Payment-Method) berechtigt den Kunden, ÖPV-Leistungen in Anspruch zu nehmen, und regelt, wie er sie bezahlt. Sie setzt eine [eBezahlberechtigung](ebezahlberechtigung.md) voraus und ist deren Nutzungsart. Beim Erfassen von Ein- und Ausstiegen entsteht ein Leistungsnachweis. Sie ist entweder kontobasiert (prepaid oder postpaid, abgerechnet im Hintergrundsystem) oder mediumbasiert als [Werteinheitenberechtigung](werteinheitenberechtigung.md) ([Q02](../../QUELLEN.md#q02), S. 28 f.).

Die eBezahlberechtigung ist „noch keine Fahrtberechtigung“; die Berechtigung für die aktuelle Fahrt entsteht erst durch den **Check-in** zusammen mit der dann als AFB genutzten eBezahlberechtigung ([Q02](../../QUELLEN.md#q02), S. 28 f.).

In etiCORE bescheinigen Check-in und Check-out `CheckinAttestation` und `CheckoutAttestation`; die Parameter der Fahrt sind `CicoPaymentParameters` ([Bescheinigungen zu Zahlungsmitteln](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md), [Fahrtdaten](../datenformate/fahrtdaten-asn-1.md)). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Man kann es sich wie bei einem Skipass vorstellen, wenn der Pass nicht gleich Zutritt ist, sondern nur die Berechtigung, überhaupt Zutritt zu bekommen.

Olli Tapsigs BärenKarte trägt seine eBezahlberechtigung mit Guthaben. Damit ist er noch nicht unterwegs, er hat nur die Grundlage. Steigt er in die Linie 4 und hält die Karte ans Lesegerät, meldet er sich an, und erst jetzt entsteht eine Berechtigung für diese Fahrt: der Check-in. Das Gerät merkt sich Linie, Haltestelle und Zeit. Je nach Verfahren wird schon ein Abschlagsbetrag erhoben, ein anteiliger Fahrpreis beim Einsteigen.

Beim Aussteigen meldet er sich ab, und das System rechnet die Fahrt aus und bucht den Betrag vom Guthaben. Der Beleg darüber ist der Leistungsnachweis.

Im Account Based Ticketing geht das noch weiter: Dort liegt gar nichts mehr auf der Karte. Die Fahrtberechtigung hängt am Kundenkonto, und die Karte oder das Handy dient nur noch zum Ausweisen. Das ist der Unterschied zum bisherigen Ticketing.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 42 (*Fahrtberechtigung*), S. 28 f. (*Automatisierte Fahrtberechtigung / IN-OUT-Payment Method*), S. 16 (*Account Based Ticketing*, *Abschlagsbetrag*) (Kürzel AFB)

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [eBezahlberechtigung](ebezahlberechtigung.md) – die Voraussetzung
- [Werteinheitenberechtigung](werteinheitenberechtigung.md) – die mediumbasierte Variante
- [Fahrtdaten (ASN.1)](../datenformate/fahrtdaten-asn-1.md) – Check-in und Check-out in etiCORE
- [Account](../abt/account.md) – das Konto im Account Based Ticketing

<!-- GEN:siehe_auch -->
## Siehe auch

- [eBezahlberechtigung](ebezahlberechtigung.md) (eBezBer)
- [Werteinheitenberechtigung](werteinheitenberechtigung.md) (WEB)
- [Account](../abt/account.md)
- [Fahrtdaten (ASN.1)](../datenformate/fahrtdaten-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
