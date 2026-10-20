---
titel: Referenz-Berechtigung
englisch: reference entitlement
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/efs.md, lexikon/berechtigungen/ebezahlberechtigung.md, lexikon/berechtigungen/produktspezifischer-teil.md, lexikon/datenformate/kundendaten-und-parameter-asn-1.md]
quellen: [Q02, Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Referenz-Berechtigung
<!-- /GEN:breadcrumb -->

# Referenz-Berechtigung

Die **Referenz-Berechtigung** ist ein „Oberbegriff für verschiedene definierte Strukturen“, die je nach Ausprägung als [eBezahlberechtigung](ebezahlberechtigung.md), [Automatisierte Fahrtberechtigung](fahrtberechtigung.md) oder für einen [Elektronischen Fahrschein](efs.md) dienen ([Q02](../../QUELLEN.md#q02), S. 75 f.).

- Als Referenz-WEB oder Referenz-AFB (POB/PEB) ist sie eine empfohlene Vorgabe für eine Automatisierte Fahrtberechtigung mit fest definierten produktspezifischen Strukturen zur interoperablen Nutzung; sie kann auch als eBezahlberechtigung genutzt werden.
- Als Referenz-EFS ist sie ein Vorschlag mit vordefinierten produktspezifischen Strukturen, den der Product Owner beim Umsetzen von eTickets verwenden kann. Das TLV-ET ist eine etwas flexiblere, speicheroptimierte Alternative.

Die Referenz-Berechtigung samt TLV-EFS ist in etiCORE und in der KA nutzbar ([Q02](../../QUELLEN.md#q02), S. 75 f.). Dazu passt, dass die Produktparameter in etiCORE ihre Inhaltsart nennen: `tlvEfs`, `referenzEfs`, `referenzPobPeb`, `referenzPlatzreservierung`, `referenzPlatzgruppenreservierung` und `referenzEfsStb` bedeuten Datenobjekte nach der KA 1.x; `etiCoreEt` steht für die etiCORE-ET-Vorgaben ([Q51](../../QUELLEN.md#q51), Modul `user-medium`; [Kundendaten und Parameter](../datenformate/kundendaten-und-parameter-asn-1.md)). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Ein Verbund muss nicht jedes Mal von vorn überlegen, wie ein Fahrschein aussehen soll. Für den Anfang gibt es Vorlagen, wie bei einem Formular aus dem Schreibwarenladen.

Denkbar ist, dass der Bären-Verkehrsbund für sein ABO Azubi die Referenz-EFS nimmt: ein vorgefertigter Aufbau mit festen Fächern für Gültigkeit, Produkt und weitere Angaben. Er spart sich das Entwerfen.

Wer es schlanker will, wählt das TLV-ET, eine etwas flexiblere Form mit weniger Speicherbedarf. Für ein Guthaben-Produkt wie Ollis Karte gibt es entsprechend eine Referenz-WEB.

Das Praktische: Die Vorlagen gelten in beiden Welten. Wer heute eine Referenz-EFS nutzt, muss sie beim Umstieg auf etiCORE nicht wegwerfen. Auf der Karte steht lediglich im Etikett der Produktparameter, nach welcher Vorlage der Inhalt gebaut ist, etwa „wie in der KA 1.x, TLV-EFS“.

Eine Pflicht, die Vorlagen zu benutzen, nennt das Glossar nicht. Es spricht von einer Empfehlung und einem Vorschlag.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 75 f. (*Referenz-Berechtigung / Reference Entitlement*) (enthält die Hinweise zu Referenz-WEB, Referenz-AFB und Referenz-EFS)
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `ProductParametersContentTypeEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Elektronischer Fahrschein](efs.md) – die Form als Fahrschein
- [eBezahlberechtigung](ebezahlberechtigung.md) – die Form als Bezahlmittel
- [Produktspezifischer Teil](produktspezifischer-teil.md) – die produktspezifischen Strukturen der KA 1.x
- [Kundendaten und Parameter (ASN.1)](../datenformate/kundendaten-und-parameter-asn-1.md) – die Inhaltsart in etiCORE

<!-- GEN:siehe_auch -->
## Siehe auch

- [Elektronischer Fahrschein](efs.md) (EFS)
- [eBezahlberechtigung](ebezahlberechtigung.md) (eBezBer)
- [Produktspezifischer Teil](produktspezifischer-teil.md)
- [Kundendaten und Parameter (ASN.1)](../datenformate/kundendaten-und-parameter-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
