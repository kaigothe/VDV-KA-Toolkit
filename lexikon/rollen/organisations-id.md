---
titel: Organisations-ID
abkuerzung: Org-ID
englisch: Organisation ID
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/rollencodes.md, lexikon/transaktionen/duplikaterkennung.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Organisations-ID
<!-- /GEN:breadcrumb -->

# Organisations-ID

Die Organisations-ID kennzeichnet eine Organisation **eindeutig im gesamten Geltungsbereich der Kernapplikation** ([Q02](../../QUELLEN.md#q02), S. 69).

Vergeben wird sie von der **Registrierung des Scheme Manager** über das Applikations- und Sicherheitsmanagement, und zwar beim Abschluss eines eTicket-Vertrages ([Q02](../../QUELLEN.md#q02), S. 69). Eine Org-ID ist damit nicht nur eine Nummer, sondern der technische Ausdruck einer vertraglichen Teilnahme.

Die mit einer ID versehenen Organisationen sind **juristische Personen**, typischerweise Verkehrsunternehmen und Verkehrsverbünde. Im Ausnahmefall können dies auch klar abgegrenzte Betriebsteile eines großen Unternehmens sein ([Q02](../../QUELLEN.md#q02), S. 69).

Daraus folgt die wichtigste Eigenschaft für die Praxis: Viele Kennungen in der KA sind **nur in Verbindung mit einer Org-ID eindeutig**. Produktnummer, Berechtigungsnummer und Applikationsinstanz-ID gelten jeweils im Nummernraum ihrer Organisation. Eine Produktnummer ohne Organisation ist eine halbe Angabe (abgeleitet).

Auch die Transaktionsidentität baut darauf auf: Die `IONTransaktion_ID` besteht aus `transSender_ID` (Org-ID), `transSenderRolle` ([Rollencode](rollencodes.md)) und `transSequenznummer` ([Q06](../../QUELLEN.md#q06), Kap. 5.3). Betreibt ein Absender mehrere Systeme, sind für die Sequenznummern Nummernkreise zu bilden, damit die Eindeutigkeit erhalten bleibt ([Q06](../../QUELLEN.md#q06), Kap. 5.3) · *verbundspezifisch*.

Eine Organisation kann **mehrere Org-IDs** besitzen ([Q06](../../QUELLEN.md#q06), Kap. 4.10).

## Einfach erklärt – Beispiel aus Bärstadt

Zahlen in KA-Nachrichten kommen fast immer paarweise. Das ist der wichtigste Lesehinweis dieses Artikels.

Pias Berechtigung trägt die Nummer 400815. Diese Zahl gilt aber nur bei den Bärstädter Verkehrsbetrieben, Organisation 9010. Der Luchs-Verkehrsverbund könnte dieselbe 400815 für etwas völlig anderes verwenden, ohne dass ein Konflikt entsteht. Erst `400815 / 9010` ist eindeutig.

Dasselbe gilt für das Produkt: Das ABO Azubi ist Produkt 2001 **des Bären-Verkehrsbunds**, also `2001 / 9020`. Und für die Karte: Applikationsinstanz `90000042 / 9010`.

Wer aus einer Nachricht nur die erste Zahl mitschreibt, hat die Information halbiert. Das ist einer der häufigsten Fehler beim Auswerten — und einer, der lange unentdeckt bleibt, weil innerhalb eines Verbunds alles zu passen scheint.

Woher kommen diese Nummern? Nicht aus einer freien Wahl. Sie werden von der zentralen Registrierungsstelle vergeben, und zwar genau dann, wenn eine Organisation einen Teilnahmevertrag abschließt. Die Org-ID ist damit gleichzeitig ein Mitgliedsausweis: Wer keine hat, nimmt nicht teil.

Vergeben werden sie an juristische Personen — Unternehmen und Verbünde. Im Ausnahmefall kann ein großes Unternehmen auch für einen klar abgegrenzten Betriebsteil eine eigene ID erhalten. Umgekehrt kann eine Organisation mehrere IDs haben.

Daraus folgt übrigens, dass man aus einer Org-ID allein nicht ablesen kann, in welcher Funktion jemand handelt. Dafür braucht es den Rollencode daneben.

Und noch ein praktischer Punkt: Betreiben die BVB zwei Terminalsysteme, dürfen beide ihre Nachrichtennummern nicht unabhängig vergeben — sonst entstehen zwei Nachrichten mit identischer Kennung. Deshalb teilt man den Nummernraum vorher auf.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 69 („Organisations-ID / Organisation ID“: Eindeutigkeit im Geltungsbereich der Kernapplikation, Vergabe durch die Registrierung des Scheme Manager über das Applikations- und Sicherheitsmanagement beim Abschluss eines eTicket-Vertrages, juristische Personen als Träger, Ausnahme für abgegrenzte Betriebsteile; Abkürzung Org-ID)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.10 (Org-IDs und Rollencodes im `TX_BASE`, Hinweis auf Mandanten mit mehreren Org-IDs), Kap. 5.3 (`IONTransaktion_ID` aus Org-ID, Rollencode und Sequenznummer; Pflicht zur Bildung von Nummernkreisen) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Rollencodes](rollencodes.md)
- [Duplikaterkennung](../transaktionen/duplikaterkennung.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
