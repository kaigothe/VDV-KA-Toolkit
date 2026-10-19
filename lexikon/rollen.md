---
titel: Rollen
englisch: roles
parent: README.md
siehe_auch: [lexikon/transaktionen/tx-base.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../README.md) › Rollen
<!-- /GEN:breadcrumb -->

# Rollen

Die VDV-Kernapplikation beschreibt ihre Beteiligten nicht als Unternehmen, sondern als **Rollen**. Das Rollenmodell stützt sich auf die ISO 24014-1; das Glossar verweist für die Rollenbeschreibungen auf das Hauptdokument der Spezifikation ([Q02](../QUELLEN.md#q02), S. 23, S. 58).

Die Trennung ist wesentlich: Eine Rolle ist eine Funktion im System, kein Rechtsträger. Dieselbe Organisation kann **mehrere Rollen** einnehmen — ein Verkehrsunternehmen ist typischerweise Kundenvertragspartner und Dienstleister zugleich. [Q06](../QUELLEN.md#q06), Kap. 4.10, trägt dem Rechnung und unterscheidet in seiner Übersicht ausdrücklich danach, ob ein Verkehrsunternehmen DL, KVP oder beides ist · *verbundspezifisch*.

Identifiziert werden Organisationen über die **Organisations-ID**, die eine Organisation eindeutig im gesamten Geltungsbereich der Kernapplikation kennzeichnet ([Q02](../QUELLEN.md#q02), S. 69). In einer Nachricht steht sie gemeinsam mit einem **Rollencode** im [`TX_BASE`](transaktionen/tx-base.md) ([Q06](../QUELLEN.md#q06), Kap. 4.10).

Die zentralen Rollen und ihr Verhältnis: Der **Applikationsherausgeber** gewährt Produktverantwortlichem, Kundenvertragspartner und Dienstleister das Recht zur Teilnahme ([Q02](../QUELLEN.md#q02), S. 23). Der **Produktverantwortliche** entwickelt aus seinen Tarifen die Produkte ([Q02](../QUELLEN.md#q02), S. 74). Der **Kundenvertragspartner** verkauft sie und verantwortet die Abrechnung gegenüber dem Kunden ([Q02](../QUELLEN.md#q02), S. 58 f.). Der **Dienstleister** befördert ([Q02](../QUELLEN.md#q02), S. 34).

Die vollständigen Rollenbeschreibungen stehen in der nicht öffentlichen KA SST-SPEC und im Hauptdokument ([Q25](../QUELLEN.md#q25), Kap. 3).

## Einfach erklärt – Beispiel aus Bärstadt

In Bärstadt lässt sich das Rollenmodell an drei Organisationen durchspielen.

Die **Bärstädter Verkehrsbetriebe** fahren die Straßenbahn. Sie betreiben die Linie 4, sie haben Fahrzeuge und Personal. In dieser Funktion sind sie Dienstleister.

Dieselben Bärstädter Verkehrsbetriebe betreiben aber auch das Kundencenter am Honigmarkt. Dort schließt Pia Brummbär ihren Abo-Vertrag, dort bekommt sie ihre BärenKarte, dorthin geht ihr Geld. In dieser Funktion sind sie Kundenvertragspartner.

Das ist ein Unternehmen mit einer Steuernummer — aber zwei Rollen. Und das ist kein Schönheitsfehler des Modells, sondern sein Zweck. Denn die Fragen, die sich stellen, sind verschieden: Wer schuldet wem Geld für die Beförderung? Wer haftet für den Kundenvertrag? Wer darf die Karte beschreiben? Je nach Frage antwortet eine andere Rolle.

Der **Bären-Verkehrsbund** fährt dagegen gar nichts. Er legt die Tarife fest und schnürt daraus Produkte — das ABO Azubi etwa, mit der Nummer 2001. Er ist Produktverantwortlicher. Wenn die Verkehrsbetriebe das Abo verkaufen, verkaufen sie ein fremdes Produkt.

Darüber steht der **Bärenland eTicket Service**, der niemandem ein Ticket verkauft und niemanden befördert. Er vergibt die Kennungen, erlaubt die Teilnahme und verwaltet die Schlüssel. Ohne seine Erlaubnis dürfte keine der anderen Organisationen mitspielen.

Der praktische Nutzen zeigt sich, wenn Pia nach Luchsstadt fährt. Dort befördert sie ein anderer Dienstleister, mit einem Produkt eines anderen Verkehrsbunds, auf einer Karte ihres Bärstädter Kundenvertragspartners. Drei Organisationen, die sich nie abgesprochen haben — und es funktioniert, weil jede weiß, welche Rolle sie hat und was daraus folgt.

## Quellen

- [Q02](../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 23 (Applikationsherausgeber, Verweis auf die Rollenbeschreibungen im Hauptdokument), S. 34 (Dienstleister), S. 58 f. (Kundenvertragspartner, Zusammensetzung aus ISO-24014-1-Rollen), S. 69 (Organisations-ID), S. 74 (Produktverantwortlicher)
- [Q06](../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.10 (Org-IDs und Rollencodes in `TX_BASE`, Unterscheidung nach der Rolle des Verkehrsunternehmens) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SST-SPEC und Hauptdokument als Normquellen der Rollenbeschreibungen)

<!-- GEN:unterartikel -->
## Unterartikel

- [Aktionslistenservice](rollen/alise.md)
- [Akzeptanzterminal](rollen/akzeptanzterminal.md)
- [Applikationsherausgeber](rollen/ah.md)
- [Dienstleister](rollen/dl.md)
- [Hintergrundsystem](rollen/hintergrundsystem.md)
- [Kontroll- und Sperrlistenservice](rollen/kose.md)
- [Kundenvertragspartner](rollen/kvp.md)
- [Organisations-ID](rollen/organisations-id.md)
- [Produktverantwortlicher](rollen/pv.md)
- [Rollencodes](rollen/rollencodes.md)
- [Rollennamen in etiCORE](rollen/rollennamen-in-eticore.md)
<!-- /GEN:unterartikel -->

<!-- GEN:siehe_auch -->
## Siehe auch

- [TX_BASE](transaktionen/tx-base.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../README.md) · [Register](../REGISTER.md)
<!-- /GEN:navigation -->
