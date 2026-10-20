---
titel: Nachrichten in KA 1.x und etiCORE
englisch: messages in KA 1.x and etiCORE
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/rollen/rollennamen-in-eticore.md, lexikon/transaktionen/txaml.md, lexikon/aktionsmanagement/aktionsfreigabe.md, lexikon/grundlagen/eticore.md]
quellen: [Q02, Q49, Q50]
status: zu prüfen
offene_fragen: [O14, O20]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Nachrichten in KA 1.x und etiCORE
<!-- /GEN:breadcrumb -->

# Nachrichten in KA 1.x und etiCORE

In den XSDs der etiCORE-Schnittstellen trägt ein großer Teil der Elemente und Typen den Vermerk `meta:old`: den Namen in der KA 1.x samt Namensraum ([Q50](../../QUELLEN.md#q50), `po-oa-management-messaging_xsd`). Er belegt, **welcher etiCORE-Name an die Stelle des alten tritt**. Dass die Bedeutung gleich bleibt, belegt er nicht (abgeleitet).

Für das Aktionsmanagement führt der Namensraum `http://vdv/ka/alise/2` zu den Schnittstellen `po-oa-management` und `ccp-oa-ordering`:

| KA 1.x | etiCORE |
|---|---|
| `TXAAUFBER` | `orderEntitlementIssuance` |
| `TXEAUFBER` | `orderEntitlementUnblocking` |
| `TXRAUFBER` | `orderEntitlementTermination` |
| `TXASAML` / `TXAML` | `getActionList` / `getActionListResponse` |
| `TXASAMDL` / `TXAMDL` | `getIncrementalActionList` / `…Response` |
| `TXAFREIBER` | `cancelOrder` (zu prüfen, O20) |

Die Listeneinträge `TXALISBER_Type` und Verwandte heißen in etiCORE `EntitlementIssuanceActionListEntry` und so fort; `txalisber` ist demnach vermutlich ein Eintrag der `TXAML` (abgeleitet, O14).

Ohne Entsprechung in der KA 1.x sind `orderEntitlementBlocking` („Nur für etiCORE“, [Q02](../../QUELLEN.md#q02), S. 19), `orderGroup` und `verifyActionListUpdatedViaIncrements` (seit 3.0.0, [Q50](../../QUELLEN.md#q50)).

Das Muster gilt auch für andere Namensräume, etwa `http://vdv/ka/kose/2` für die Hotlist-Aufträge. Mit rund 850 Paaren ist die Tabelle in [exzerpte/Q50.md](../../exzerpte/Q50.md) die einzige öffentliche Brücke zwischen den Nachrichten beider Versionen. Quelle ist ein Release-Kandidat (3.0.0-rc.6, [Q49](../../QUELLEN.md#q49)).

## Einfach erklärt – Beispiel aus Bärstadt

Bodo Bärlauch im Kundencenter am Honigmarkt hat einen alten Ordner mit Auszügen aus dem Nachrichtenverkehr. Darin steht immer wieder `TXAAUFBER`: Die BVB beauftragt, ein Produkt auf eine BärenKarte zu schreiben, zum Beispiel Pias ABO Azubi.

Stellen wir uns vor, der Bären-Verkehrsbund stellt auf etiCORE um. Bodo bekommt eine neue Beschreibung der Schnittstelle und liest dort `orderEntitlementIssuance`. Der Name ist ein anderer, die Aufgabe klingt gleich: Eine Berechtigung soll ausgegeben werden.

Woher weiß Bodo, dass beide Namen zusammengehören? Die etiCORE-Beschreibung nennt bei `orderEntitlementIssuance` den alten Namen `TXAAUFBER` ausdrücklich. Das ist ein Wegweiser, so wie ein Schild „Früher: Bahnhofstraße“ unter einem neuen Straßennamen.

Der Wegweiser sagt aber nur, dass die Straße umbenannt wurde. Ob an der Ecke noch dasselbe Haus steht, sagt er nicht. Bei `TXAFREIBER` zeigt der Wegweiser auf `cancelOrder`, eine Stornierung. Bodo kennt aus seinem Alltag eher eine „Freigabe“. Beides muss er nicht verwechseln, aber er sollte nachfragen, bevor er beide gleichsetzt.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management-messaging_xsd` und `ccp-oa-ordering-messaging_xsd`, Vermerk `meta:old` an den genannten Elementen
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19
- [Q49](../../QUELLEN.md#q49) – etiCORE Specification, Version 3.0.0-rc.6 (Release Candidate)

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md) – die Übersetzung der Rollen
- [TXAML](txaml.md) – die Aktionsliste der KA 1.x
- [Aktionsfreigabe](../aktionsmanagement/aktionsfreigabe.md) – die Nachricht `TXAFREIBER`
- [etiCORE](../grundlagen/eticore.md) – die Version 3 des Standards

<!-- GEN:siehe_auch -->
## Siehe auch

- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md)
- [TXAML](txaml.md)
- [Aktionsfreigabe](../aktionsmanagement/aktionsfreigabe.md)
- [etiCORE](../grundlagen/eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
