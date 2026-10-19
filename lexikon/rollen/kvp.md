---
titel: Kundenvertragspartner
abkuerzung: KVP
englisch: Customer Contract Partner
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/pv.md, lexikon/rollen/rollencodes.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Kundenvertragspartner
<!-- /GEN:breadcrumb -->

# Kundenvertragspartner

Der Kundenvertragspartner (KVP) ist die Rolle, die die Kundenbeziehung trägt. Das Glossar bezeichnet sie als **spezielle Rolle der Kernapplikation**, die mehrere in der ISO 24014-1 definierte Rollen zusammenfasst: Product Retailer, Application Retailer, Customer Service, Identity Provider, Account Provider und Payment Provider — letzteren übernimmt der KVP selbst oder er nimmt die Dienste eines Payment Providers in Anspruch ([Q02](../../QUELLEN.md#q02), S. 58 f.).

Der KVP reguliert die Verkaufsprozesse unter Berücksichtigung der vertraglichen Abhängigkeiten gegenüber dem Scheme Manager und dem Produktverantwortlichen. Insbesondere ist er für **Buchhaltung, Ticketing und Abrechnung** der Mobilitätsdienste gegenüber dem Kunden verantwortlich ([Q02](../../QUELLEN.md#q02), S. 59).

Der Kundenvertrag ist **immer qualifiziert durch die Organisations-ID des Kundenvertragspartners** ([Q02](../../QUELLEN.md#q02), S. 58). Das macht den KVP zum Bezugspunkt jeder Berechtigung.

Ein KVP kann in der Rolle **Primär-Kundenvertragspartner** oder **Fremd-Kundenvertragspartner** auftreten ([Q02](../../QUELLEN.md#q02), S. 59). Im Aktionsmanagement kommen die Unterscheidungen **beauftragender** und **ausführender** KVP hinzu; dauerhaft gespeichert werden die Transaktionsnachweise beim beauftragenden KVP, der die wirtschaftliche Verantwortung trägt ([Q06](../../QUELLEN.md#q06), Kap. 1.2.2) · *verbundspezifisch*.

Im `TX_BASE` trägt der KVP den [Rollencode](rollencodes.md) **1** ([Q06](../../QUELLEN.md#q06), Kap. 4.10) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Der Kundenvertragspartner ist derjenige, an den Pia Brummbär sich wendet, wenn etwas nicht stimmt.

In Bärstadt sind das die Bärstädter Verkehrsbetriebe. Sie haben Pia die BärenKarte gegeben, sie haben den Abo-Vertrag mit ihr geschlossen, sie buchen monatlich ab, und wenn die Karte nicht funktioniert, sitzt Bodo Bärlauch im Kundencenter am Honigmarkt und kümmert sich.

Das Glossar listet dafür sechs Einzelrollen auf — Produktverkäufer, Applikationsverkäufer, Kundenservice, Identitätsgeber, Kontoführer und Zahlungsabwickler. In Bärstadt macht das alles dieselbe Stelle. Genau das ist der Gedanke: Für Pia soll es **einen** Ansprechpartner geben, auch wenn hinter den Kulissen sechs verschiedene Funktionen zusammenwirken.

Besonders folgenreich ist ein Detail: Ihre Berechtigungsnummer 400815 gilt nur **im Nummernraum der BVB**. Ein anderes Verkehrsunternehmen könnte dieselbe Zahl für eine ganz andere Berechtigung verwenden, ohne dass es zu einer Verwechslung käme. Erst die Kombination aus Nummer und der Organisations-ID 9010 ist eindeutig. Wer eine Berechtigungsnummer ohne ihre Organisation notiert, hat eine halbe Information.

Interessant wird es, wenn mehrere Unternehmen beteiligt sind. Fährt Pia nach Luchsstadt, bleiben die BVB ihr Kundenvertragspartner — auch wenn dort ein anderes Unternehmen fährt und ein anderer Verbund das Produkt verantwortet. Der Kundenvertragspartner wechselt nicht mit dem Ort.

Im Aktionsmanagement gibt es noch zwei Spielarten: den **beauftragenden** und den **ausführenden** Kundenvertragspartner. In Bärstadt ist das dieselbe Organisation. Es muss aber nicht so sein — und dann gilt: Die Nachweise werden dauerhaft bei dem gespeichert, der den Auftrag erteilt hat. Denn der zahlt.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 58 („Kundenvertrag“: Qualifizierung durch die Organisations-ID des KVP; Beginn des Eintrags „Kundenvertragspartner“), S. 59 (deutsche Beschreibung: Zusammensetzung aus sechs ISO-24014-1-Rollen, Verantwortung für Buchhaltung, Ticketing und Abrechnung, Primär- und Fremd-KVP)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 1.2.2 (beauftragender und ausführender KVP, dauerhafte Speicherung beim beauftragenden KVP mit der wirtschaftlichen Verantwortung), Kap. 4.10 (Rollencode KVP = 1) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
