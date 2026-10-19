---
titel: Nachweis
englisch: attestation
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/transaktion.md, lexikon/aktionsmanagement/entsperrnachweis.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Nachweis
<!-- /GEN:breadcrumb -->

# Nachweis

Ein Nachweis protokolliert **authentisch** eine zuvor ausgeführte Transaktion auf Nutzermedium-Ebene. Anlass können eine Ausgabe einer Berechtigung, Check-In oder Check-Out, Kontrolle, Sperrung, Entsperrung, Entwertung oder die Aufladung von Werteinheiten sein. Der Nachweis wird zur weiteren Verarbeitung an die Hintergrundsysteme weitergeleitet ([Q02](../../QUELLEN.md#q02), S. 65).

Für (((etiCORE ergänzt das Glossar: Nur bestimmte Nachweise werden zusätzlich noch auf dem Nutzermedium gespeichert ([Q02](../../QUELLEN.md#q02), S. 65).

„Authentisch“ ist der Kern des Begriffs: Der Nachweis ist kryptografisch gesichert und damit mehr als eine Mitteilung. Deshalb lehnt ein Hintergrundsystem Transaktionen mit negativem Ergebnis der MAC-Prüfung ab ([Q06](../../QUELLEN.md#q06), Kap. 3.1).

Der Nachweis ist ein Oberbegriff. Das Glossar führt mehrere Arten als eigene Einträge: Entsperrnachweis (S. 39), Leistungsnachweis (S. 61) und Sperrnachweis (S. 90). Hinzu kommen die Ausgabenachweise und Kontrollnachweise, die in den Projektdokumenten als `TXABER`, `TXRBER`, `TXSNAWB`, `TXEBER` und `TXKNAW*` auftreten ([Q06](../../QUELLEN.md#q06), Kap. 4.2.3, 4.3.2, 4.4.1).

Die wichtigste Unterscheidung in der Praxis: Ein **Auftrag** sagt, was geschehen soll; ein **Nachweis** belegt, dass es geschehen ist. Im Aktionsmanagement sind das zwei verschiedene Nachrichten zu verschiedenen Zeitpunkten (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Der Unterschied zwischen einem Auftrag und einem Nachweis entscheidet darüber, wem man am Ende Geld schuldet.

Als die Bärstädter Verkehrsbetriebe den Auftrag erteilen, Pias ABO Azubi auf die Karte zu schreiben, ist das eine Absichtserklärung. Sie sagt: So soll es sein. Sie sagt nicht: So ist es.

Erst wenn das Lesegerät T-4712 am Hauptbahnhof die Berechtigung tatsächlich geschrieben hat, entsteht der Nachweis. Er sagt: Es ist geschehen, am Gerät T-4712, zu dieser Uhrzeit, auf dieser Karte.

Zwei Eigenschaften machen ihn wertvoll.

Erstens ist er **gesichert**. Das SAM im Terminal berechnet dabei einen Prüfcode, der sich nicht nachträglich passend fälschen lässt. Käme beim Bären-Verkehrsbund ein Nachweis an, dessen Prüfcode nicht stimmt, würde er abgelehnt. Ein Nachweis ist also keine Behauptung, sondern ein Beleg.

Zweitens **entsteht er am Ort des Geschehens**. Niemand im Rechenzentrum schreibt ihn; das Gerät an der Haltestelle tut es. Das ist der einzige Ort, an dem man wirklich weiß, was mit der Karte passiert ist.

Nachweise gibt es für vieles, nicht nur fürs Ausgeben: fürs Entsperren, fürs Zurücknehmen, fürs Sperren, für eine Kontrolle. Wenn Petra Pranke in der Linie 4 Pias Karte prüft, entsteht ebenfalls ein Nachweis — und der ist später erstaunlich nützlich. Geht nämlich der Ausgabenachweis unterwegs verloren, kann der Kontrollnachweis belegen, dass das Abo auf der Karte ist. Genau davon lebt das Aktionsclearing.

Ein Satz zum Mitnehmen: Der Auftrag ist der Plan, der Nachweis die Quittung. Wer beides verwechselt, hält offene Aufträge für erledigte Arbeit.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 65 („Nachweis / Attestation“: authentisches Protokoll einer zuvor ausgeführten Transaktion auf Nutzermedium-Ebene, Anlässe, Weiterleitung an die Hintergrundsysteme, Hinweis für (((etiCORE). Eigene Glossareinträge bestehen für Entsperrnachweis (S. 39), Leistungsnachweis (S. 61) und Sperrnachweis (S. 90); die Seitenangaben stammen aus dem Inhaltsverzeichnis, S. 2–13.
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 3.1 (Ablehnung bei negativem Ergebnis der MAC-Prüfung), Kap. 4.2.3 (Kontrollnachweise), Kap. 4.3.2 (Transaktionsnachweise aus Aktionsausführung), Kap. 4.4.1 (Ausgabenachweise aus Verkauf) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Transaktion](transaktion.md)
- [Entsperrnachweis](../aktionsmanagement/entsperrnachweis.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
