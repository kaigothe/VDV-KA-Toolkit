---
titel: Werteinheitenberechtigung
abkuerzung: WEB
englisch: stored value payment method
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/ebezahlberechtigung.md, lexikon/berechtigungen/fahrtberechtigung.md, lexikon/transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md, lexikon/transaktionen/warnungen-in-eticore.md]
quellen: [Q02, Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Werteinheitenberechtigung
<!-- /GEN:breadcrumb -->

# Werteinheitenberechtigung

Die **Werteinheitenberechtigung** (WEB) ist „die Möglichkeit bzw. Erlaubnis, auf dem Nutzermedium ÖPV zweckgebundene Werteeinheiten für ÖPV-Leistungen zu nutzen“ ([Q02](../../QUELLEN.md#q02), S. 98). Sie ist einerseits eine [Automatisierte Fahrtberechtigung](fahrtberechtigung.md) mit integriertem Werteinheitenspeicher: Bei automatisierter Fahrpreisermittlung im Terminal bleibt der Zugriff auf das Medium beschränkt, und die Buchung der Werteinheiten läuft mit der Erfassungstransaktion zusammen. Andererseits ist sie außerhalb von IN-OUT-Systemen eine [eBezahlberechtigung](ebezahlberechtigung.md).

Zwei Nutzungsarten ([Q02](../../QUELLEN.md#q02), S. 98 f.): **WE-preload**, bei der der Saldo nie negativ sein darf und vor der Nutzung aufzuladen ist; und **WE-postload**, bei der er bis zu einer Untergrenze negativ sein darf, in etiCORE aber nicht möglich ist. Mit preload ist eine anonyme Teilnahme möglich; die Autoload-Funktion verlangt einen Vertrag, also nicht anonym.

Die etiCORE-Typen spiegeln das: `StoredValueParameters` führt Kontostand (nicht negativ) und Höchstbetrag (positiv), `StoredValueAutoloadParameters` Schwelle und festen Betrag ([Q51](../../QUELLEN.md#q51), Modul `user-medium`; [Bescheinigungen zu Zahlungsmitteln](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md)). Die Warncodes `W_CO_STORED_VALUE_…` prüfen die Parameter ([Warnungen](../transaktionen/warnungen-in-eticore.md)). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Die Werteinheitenberechtigung ist ein Geldbeutel mit einem Aufdruck „nur für den Nahverkehr“.

Olli Tapsig lädt 20 Euro auf. Der Saldo steht auf der Karte, nicht beim Hintergrundsystem. Das ist die preload-Variante, und ein Minus gibt es nicht. Ist das Guthaben verbraucht, geht nichts mehr, bis er wieder auflädt. Damit er nicht an der Haltestelle strandet, könnte er eine Automatik einrichten, die bei einer Schwelle einen festen Betrag nachlädt. Dafür braucht es einen Vertrag, und anonym ist er dann nicht mehr.

Eine postload-Variante, bei der man ins Minus rutschen dürfte, bis eine Untergrenze erreicht ist, kennt das Glossar für die KA 1.x. In etiCORE gibt es sie nicht.

Der Vorteil beim Fahren: Das Terminal braucht für die Abbuchung nur die Karte. Es muss nicht erst beim Hintergrundsystem anfragen, und die Abbuchung läuft gleich mit der Erfassung der Fahrt zusammen.

Eine Grenze setzt der Bären-Verkehrsbund: den Höchstbetrag. Würde eine Aufladung ihn überschreiten, lehnt die Karte sie ab.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 98 f. (*Werteinheitenberechtigung / Stored Value Unit Payment Method*), S. 97 (*Werteinheiten WE*) (Kürzel WEB, SVPM)
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `StoredValueParameters`, `StoredValueAutoloadParameters` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [eBezahlberechtigung](ebezahlberechtigung.md) – der Oberbegriff
- [Fahrtberechtigung](fahrtberechtigung.md) – Nutzung im IN-OUT-System
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md) – Aufladung, Belastung, Autoload
- [Warnungen in etiCORE](../transaktionen/warnungen-in-eticore.md) – die Prüfungen der Parameter

<!-- GEN:siehe_auch -->
## Siehe auch

- [eBezahlberechtigung](ebezahlberechtigung.md) (eBezBer)
- [Fahrtberechtigung](fahrtberechtigung.md)
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md)
- [Warnungen in etiCORE](../transaktionen/warnungen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
