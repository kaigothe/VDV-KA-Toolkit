---
titel: Bezahlart
englisch: payment means
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/ebezahlberechtigung.md, lexikon/berechtigungen/werteinheitenberechtigung.md, lexikon/datenformate/zahlungsmittel-asn-1.md, lexikon/abt/account.md]
quellen: [Q02, Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Bezahlart
<!-- /GEN:breadcrumb -->

# Bezahlart

Die **Bezahlart** ist die „Art und Weise wie, d. h. mit welchem Zahlungsmittel, die Forderung für die Erbringung der Beförderungsleistung gegenüber dem Kunden ausgeglichen wird“ ([Q02](../../QUELLEN.md#q02), S. 31).

Bezahlzeitpunkt und Bezahlart sind zu unterscheiden. Bei der automatisierten Fahrpreisermittlung gibt es drei Varianten ([Q02](../../QUELLEN.md#q02), S. 42 f.):
- **pre-priced:** Der Fahrpreis steht vor der Fahrt fest, meist beim Ticketkauf. Gültige Bezahlarten: Belastung einer [eBezahlberechtigung](ebezahlberechtigung.md), Barzahlung, Kreditkarte, Debitkarte, Geldkarte.
- **trip-priced:** Der Preis wird nach der Fahrt festgelegt, in der Regel beim Check-out. Gültig ist die Belastung einer [Werteinheitenberechtigung](werteinheitenberechtigung.md).
- **post-priced:** Der Preis wird später im Hintergrundsystem festgelegt, nur so ist eine Bestpreisberechnung möglich. Gültig ist die Belastung eines Postpaid- oder Prepaid-Kontos.

Beim Einsteigen kann ein **Abschlagsbetrag**, ein anteiliger Fahrpreis, erhoben werden ([Q02](../../QUELLEN.md#q02), S. 16).

In etiCORE klassifiziert `PaymentMeansEnum` die Bezahlart mit 37 Werten nach EN 1545-1:2015, von „nicht angegeben“ und Bargeld über Kreditkarte, SEPA-Lastschrift und Rechnung bis zur kontobasierten Autorisierung ([Q51](../../QUELLEN.md#q51), Modul `payment`; [Zahlungsmittel](../datenformate/zahlungsmittel-asn-1.md)). Das Aufladen eines Guthabens nennt das genutzte Zahlungsmittel, die automatische Aufladung den Wert 12. Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Zwei Fragen werden gern verwechselt: Wann wird der Preis festgelegt, und womit wird bezahlt?

Familie Tatze kauft am Automaten am Hauptbahnhof eine Tageskarte Familie. Der Preis steht fest, bevor sie einsteigt: pre-priced. Die Mutter zahlt bar oder mit Karte. Das ist die Bezahlart.

Olli Tapsig dagegen steigt in die Linie 4 und meldet sich mit seiner Karte an. Wie viel die Fahrt kostet, steht erst fest, wenn er ausgestiegen ist: trip-priced. Abgebucht wird vom Guthaben auf der Karte.

Würde die BVB die Fahrten eines Monats sammeln und am Monatsende den günstigsten Preis ermitteln, wäre das post-priced. Nur so kann das System rückwirkend den Bestpreis rechnen. Bezahlt wird von einem Konto.

Beim Einsteigen kann schon ein Abschlag fällig sein, ein anteiliger Fahrpreis.

Die Zahlungsmittelliste in etiCORE ist das Wörterbuch dazu: Bargeld, Karte, Lastschrift und weitere, jedes mit einer Nummer.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 31 (*Bezahlart / Payment Means*), S. 42 f. (*Automatisierte Fahrpreisermittlung*), S. 16 (*Abschlagsbetrag*) (Kürzel AFE)
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `payment`: `PaymentMeansEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [eBezahlberechtigung](ebezahlberechtigung.md) – das Bezahlmittel
- [Werteinheitenberechtigung](werteinheitenberechtigung.md) – die Bezahlart bei trip-priced
- [Zahlungsmittel (ASN.1)](../datenformate/zahlungsmittel-asn-1.md) – die Aufzählung in etiCORE
- [Account](../abt/account.md) – das Konto

<!-- GEN:siehe_auch -->
## Siehe auch

- [eBezahlberechtigung](ebezahlberechtigung.md) (eBezBer)
- [Werteinheitenberechtigung](werteinheitenberechtigung.md) (WEB)
- [Zahlungsmittel (ASN.1)](../datenformate/zahlungsmittel-asn-1.md)
- [Account](../abt/account.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
