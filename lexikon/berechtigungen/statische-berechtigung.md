---
titel: Statische Berechtigung
abkuerzung: StatBer
englisch: Static Entitlement
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/efs.md, lexikon/berechtigungen/berechtigung.md]
quellen: [Q02, Q07, Q25, Q37]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Statische Berechtigung
<!-- /GEN:breadcrumb -->

# Statische Berechtigung

„Der Begriff Statische Berechtigung bezieht sich hier auf einen **mit einer digitalen Signatur ausgestatteten** elektronischen Fahrschein, der als **nicht veränderbarer Datensatz** auf verschiedene, auch einfache Medien ausgegeben werden kann.“ ([Q02](../../QUELLEN.md#q02), S. 92)

Als Medien nennt das Glossar ([Q02](../../QUELLEN.md#q02), S. 92):

- einen auf Papier gedruckten oder auf einem mobilen Endgerät gespeicherten **2D-Barcode**,
- einen auf einem **kostengünstigen Speicherchip oder NFC-Handy** gespeicherten und über eine ISO-14443-Schnittstelle lesbaren Datensatz.

Die beiden Eigenschaften hängen zusammen: Weil der Datensatz nicht veränderbar ist, kann er nicht wie ein normaler EFS über ein SAM beschrieben werden — stattdessen trägt er eine **digitale Signatur**, die seine Echtheit belegt (abgeleitet). Damit genügt ein Medium ohne Sicherheitsfunktion.

Normquelle ist die nicht öffentliche **KA STB-Spec**, „Spezifikation statischer Berechtigungen für 2D-Barcode-Tickets“, Inventarnummer 42 ([Q25](../../QUELLEN.md#q25), Kap. 3). Ein Prüfbericht von 2024 nennt daneben eine **KA STB-SPEC mobile plus** für den „kryptographischen Kopierschutz für statische Berechtigungen VDV-Barcode mobile+“ ([Q37](../../QUELLEN.md#q37)).

Die statische Berechtigung ist eine **optionale Ergänzung** zu den Ausbauvarianten und kann im Bereich des Handy- oder Onlinetickets auch als „autarke Lösung“ eingesetzt werden ([Q25](../../QUELLEN.md#q25), Anlage 2).

Ein Datenlayout einer verbundspezifischen Ausprägung liegt mit [Q07](../../QUELLEN.md#q07) vor (Auswertung offen).

Abkürzungen: **StatBer** (deutsch), **STE** (englisch).

## Einfach erklärt – Beispiel aus Bärstadt

Eine statische Berechtigung ist ein Fahrschein, der nichts können muss — außer echt sein.

Der Unterschied zu Pias BärenKarte ist grundlegend. Auf ihrer Karte sitzt ein Chip, der rechnen kann. Beim Schreiben arbeitet er mit dem Sicherheitsbaustein des Terminals zusammen, und bei der Kontrolle lässt sich prüfen, ob beide sich einig sind. Dafür braucht es eine teure Karte und ein Gerät mit Sicherheitsmodul.

Die statische Berechtigung dreht das um: Sie ist nur ein **Datensatz mit einer Unterschrift**. Man kann ihn auf Papier drucken, als Barcode aufs Handy legen oder auf einen billigen Chip schreiben. Der Träger muss nichts können, weil die Sicherheit im Datensatz selbst steckt.

Das Prinzip kennt man vom Siegel auf einer Urkunde. Das Papier ist gewöhnlich, aber das Siegel beweist die Herkunft. Verändert jemand den Text, passt das Siegel nicht mehr.

Daraus folgt die wichtigste Eigenschaft, die auch im Namen steckt: Eine statische Berechtigung ist **nicht veränderbar**. Man kann sie nicht sperren wie ein Abo auf einer Karte, man kann sie nicht nachträglich verlängern. Was einmal signiert ist, bleibt wie es ist.

Für Olli Tapsig, der sein Ticket in der App kauft, ist das bequem: kein Kartenleser, kein Terminalbesuch, sofort gültig. Für den Verbund ist es ein Tausch. Er spart Medien und Geräte, verliert aber die Möglichkeit, nachträglich eingreifen zu können — und muss sich stattdessen auf Sperrlisten und nachgelagerte Prüfungen verlassen.

Genau deshalb gibt es inzwischen eine zusätzliche Spezifikation für den **Kopierschutz**. Ein Datensatz, der sich beliebig vervielfältigen lässt, ist sonst eine offene Flanke.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 92 („Statische Berechtigung / Static Entitlement“: EFS mit digitaler Signatur als nicht veränderbarer Datensatz, 2D-Barcode auf Papier oder mobilem Endgerät, Datensatz auf kostengünstigem Speicherchip oder NFC-Handy über ISO-14443-Schnittstelle; Abkürzungen StatBer und STE)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA STB-Spec, Inventarnummer 42: Spezifikation statischer Berechtigungen für 2D-Barcode-Tickets); Anlage 2 (statische Berechtigung als optionale Ergänzung und „autarke Lösung“ im Handy- und Onlineticket)
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht (2024), S. 4 (KA STB-SPEC und KA STB-SPEC mobile plus für den kryptographischen Kopierschutz, beide in Version 1.12.0)
- [Q07](../../QUELLEN.md#q07) – RMV, Statische Berechtigung RMV-EFS, Spezifikation Datenlayout, v1.9 · *verbundspezifisch, Auswertung offen*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
