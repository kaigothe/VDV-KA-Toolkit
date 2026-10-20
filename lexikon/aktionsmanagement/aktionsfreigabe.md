---
titel: Aktionsfreigabe
englisch: action release
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/kontrolle/sperranforderung.md, lexikon/aktionsmanagement/aktion.md, lexikon/aktionsmanagement/aktionsliste.md, lexikon/rollen/alise.md, lexikon/transaktionen/nachrichten-in-ka-1-x-und-eticore.md]
quellen: [Q02, Q25, Q39, Q40, Q49, Q50]
status: zu prüfen
offene_fragen: [O20]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktionsfreigabe
<!-- /GEN:breadcrumb -->

# Aktionsfreigabe

Die Aktionsfreigabe ist ein eigener Schritt im Aktionsmanagement, neben Beauftragung und Ausführung. Das eTicket-Regelwerk führt dafür zwei Anwendungsfälle des Kundenvertragspartner-Systems: „Aktionsfreigabe senden“ und „Aktionsfreigabemitteilung entgegennehmen“ ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38).

[Q39](../../QUELLEN.md#q39), Kap. 3.2.5, benennt die zugehörigen **Nachrichten** und ihre Richtung · *verbundspezifisch: eTicket RheinMain*:

| Nachricht | Richtung | Bedeutung |
|---|---|---|
| `TXAFREIBER` | KVP → PV/ALISE | Aktionsfreigabeauftrag des Verkehrsunternehmens als **beauftragender** KVP, asynchron |
| `TXAFREIMITBER` | PV/ALISE → KVP | Aktionsfreigabemitteilung des ALISE an den beauftragenden KVP, asynchron |

Die Freigabe ist damit ein **zweiseitiger Vorgang zwischen beauftragendem Kundenvertragspartner und ALISE** und vom Aktionsauftrag getrennt: Die Auftragsnachrichten `TXAAUFBER`, `TXRAUFBER` und `TXEAUFBER` stehen in derselben Tabelle daneben.

**Was „Freigabe“ meint, zeigt das Benennungsmuster der KA.** Im Sperrmanagement steht dem Sperrauftrag `TXSAUFB` der **Sperrfreigabeauftrag** `TXSFREIB` gegenüber, bei der NmApplikation entsprechend `TXSAUFA` und `TXSFREIA` ([Q39](../../QUELLEN.md#q39), Kap. 3.2.1 f., PDF-S. 50 f.). Eine „Freigabe“ **nimmt dort zurück, was der Auftrag bewirkt hat**; das Glossar definiert den Sperrfreigabeauftrag als Auftrag, „ein Objekt von der jeweiligen Sperrliste zu nehmen“ ([Q02](../../QUELLEN.md#q02), S. 87 f.; [Sperranforderung](../kontrolle/sperranforderung.md)). Ein NRW-Rahmenlastenheft führt Sperraufhebungsanforderung und Sperrfreigabeauftrag als Paar ([Q40](../../QUELLEN.md#q40), PDF-S. 16 und 20) · *verbundspezifisch: NRW*.

**Dazu passt etiCORE.** `cancelOrder` — „Cancel an order“, einziges Feld `orderId` — trägt den Altbezeichner `TXAFREIBER` ([Q50](../../QUELLEN.md#q50)); im Modell wird der Auftrag „im Auftragsbestand als storniert markiert und aus der nächsten Aktionsliste entfernt“ ([Q49](../../QUELLEN.md#q49)). Auch `TXSFREIB` heißt dort `removeEntitlementFromHotlist` ([Q50](../../QUELLEN.md#q50), `hotlist-messaging_xsd`).

Danach ist die Aktionsfreigabe die **Rücknahme eines noch nicht ausgeführten Auftrags** und nicht dessen Scharfstellen (abgeleitet). Eine ausdrückliche Definition fehlt in allen vorliegenden Quellen; das Glossar [Q02](../../QUELLEN.md#q02) kennt den Begriff Aktionsfreigabe nicht (zu prüfen, O20). Normquelle bleibt die nicht öffentliche KA AktM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 41).

## Einfach erklärt – Beispiel aus Bärstadt

Pias Abo-Antrag ist erfasst, der Auftrag ist beim Bären-Verkehrsbund eingegangen — und dann stellt Bodo Bärlauch im Kundencenter fest, dass der Ausbildungsnachweis nicht gültig ist.

Der Auftrag muss weg. Aber er ist schon unterwegs: Er steht im Auftragsbestand des Aktionslistenservices und würde beim nächsten Listenlauf an die Terminals verteilt. Pia hielte ihre BärenKarte an das Lesegerät T-4712, und die Berechtigung wäre auf dem Chip.

**Genau dafür ist die Freigabe da.** Die Bärstädter Verkehrsbetriebe schicken eine Nachricht an den Aktionslistenservice: „Der Auftrag zur Berechtigung 400815 ist freizugeben.“ Der Auftrag wird im Bestand als storniert vermerkt und kommt in die nächste Aktionsliste nicht mehr hinein. Kurz darauf trifft die Gegenbestätigung ein — die Aktionsfreigabemitteilung.

**Warum „Freigabe“ und nicht „Stornierung“?** Weil die KA das Wort anders benutzt, als man zunächst denkt. Freigeben heißt hier: etwas aus einer Bindung lösen. Bei einer Sperre ist das offensichtlich — ein Sperrfreigabeauftrag hebt die Sperre auf und gibt die Karte wieder frei. Bei einem Auftrag ist es dasselbe Muster: Die Berechtigung wird von dem Auftrag freigegeben, der auf ihr liegt.

Wer das Wort im Alltagssinn liest, kommt auf die umgekehrte Bedeutung — „der Auftrag wird zur Ausführung freigegeben“ — und damit auf das Gegenteil. Das ist eine der Stellen, an denen die KA-Begriffe eine Falle stellen.

**Warum es eine eigene Rückmeldung gibt.** Die BVB schickt die Freigabe asynchron, bekommt also keine unmittelbare Antwort. Ohne Mitteilung wüsste sie nicht, ob die Freigabe rechtzeitig angekommen ist — und das muss sie wissen. Kommt sie zu spät, ist die Berechtigung schon auf Pias Karte, und dann hilft nur noch eine Rücknahme über die Aktionsliste, also der umgekehrte Weg mit einem neuen Auftrag.

**Was daran noch offen ist.** Diese Lesart stützt sich auf das Benennungsmuster und auf die etiCORE-Nachfolgenachricht, nicht auf eine Definition. Keine der vorliegenden Quellen schreibt aus, was eine Aktionsfreigabe bewirkt; das Glossar kennt den Begriff nicht einmal. Für ein Prüfwerkzeug heißt das: Die Nachrichtennamen und ihre Richtung sind belegt, die Wirkung ist erschlossen.

Und wie immer bei diesen Nachrichten gilt der Vorbehalt des Verbunds: Dass die Freigabe als eigener Schritt existiert, ist aus dem Pflichtenheft **eines** Verbunds belegt.

## Quellen

- [Q39](../../QUELLEN.md#q39) – RMV vHGS-Vertrag, Anlage 6 „Konzept Externer Mandant“, Kap. 3.2.5 (PDF-S. 52 f.): `TXAFREIBER` als Aktionsfreigabeauftrag des beauftragenden KVP und `TXAFREIMITBER` als Aktionsfreigabemitteilung des ALISE, beide asynchron; daneben die Auftragsnachrichten `TXAAUFBER`, `TXRAUFBER`, `TXEAUFBER` · *verbundspezifisch: eTicket RheinMain*; Kap. 3.2.1 (PDF-S. 50) und Kap. 3.2.2 (PDF-S. 51): `TXSAUFB` als Sperrauftrag und `TXSFREIB` als Sperrfreigabeauftrag für eine Berechtigung, `TXSAUFA` und `TXSFREIA` entsprechend für eine NmApplikation. Die Kapitelüberschrift lautet „Aktionsmanagement RMV-EFS“ — das Dokument ist eine RMV-Quelle, keine aus NRW
- [Q40](../../QUELLEN.md#q40) – KCD NRW, Rahmenlastenheft DL-System v2.4, PDF-S. 16 (Elementarprozesse `EP_Sperrfreigabeauftrag_Applikation`, `_SAM`, `_Key`, `_Berechtigung` neben `EP_Sperraufhebungsanforderung_Applikation` und `_SAM`), PDF-S. 17 ff. (Anwendungsfälle „… Sperrfreigabemitteilung entgegennehmen“), PDF-S. 20 (Sperraufhebungsanforderungen und „die zugehörigen Sperrmitteilungen und Sperrfreigabemitteilungen“ in einem Satz) · *verbundspezifisch: NRW*
- [Q49](../../QUELLEN.md#q49) – etiCORE-Spezifikationsmodell, *Ordered action management › Ordering › Cancel order*: Markierung als storniert im Auftragsbestand und Entfernen aus der nächsten Aktionsliste
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 239): Anwendungsfälle „Aktionsfreigabe senden“ und „Aktionsfreigabemitteilung entgegennehmen“; Kap. 3 (KA AktM-SPEC, Inventarnummer 41)
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management-messaging_xsd` (Element `cancelOrder`) und `ccp-oa-ordering-messaging_xsd` (Element `notifyOrderSeemsToBeObsolete`), jeweils mit `meta:old` · *Release-Kandidat*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE: **kein** Eintrag „Aktionsfreigabe“ (geprüft am Inhaltsverzeichnis, S. 2–13); S. 20 f. zum Statusmodell der Aktion; S. 87 f. *Sperrfreigabeauftrag / Hotlisting Removal Order*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Sperranforderung](../kontrolle/sperranforderung.md)
- [Aktion](aktion.md)
- [Aktionsliste](aktionsliste.md) (TXAML)
- [Aktionslistenservice](../rollen/alise.md) (ALISE)
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
