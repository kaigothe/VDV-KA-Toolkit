---
titel: Aktionsfreigabe
englisch: action release
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktion.md, lexikon/aktionsmanagement/aktionsliste.md, lexikon/rollen/alise.md, lexikon/transaktionen/nachrichten-in-ka-1-x-und-eticore.md]
quellen: [Q02, Q25, Q39, Q50]
status: abgeleitet
offene_fragen: [O20]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktionsfreigabe
<!-- /GEN:breadcrumb -->

# Aktionsfreigabe

Die Aktionsfreigabe ist ein eigener Schritt im Aktionsmanagement, neben Beauftragung und Ausführung. Das eTicket-Regelwerk führt dafür zwei Anwendungsfälle des Kundenvertragspartner-Systems: „Aktionsfreigabe senden“ und „Aktionsfreigabemitteilung entgegennehmen“ ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38).

[Q39](../../QUELLEN.md#q39), Kap. 3.2.5, benennt die zugehörigen **Nachrichten** und ihre Richtung · *verbundspezifisch*:

| Nachricht | Richtung | Bedeutung |
|---|---|---|
| `TXAFREIBER` | KVP → PV/ALISE | Aktionsfreigabeauftrag des Verkehrsunternehmens als **beauftragender** KVP, asynchron |
| `TXAFREIMITBER` | PV/ALISE → KVP | Aktionsfreigabemitteilung des ALISE an den beauftragenden KVP, asynchron |

Die Freigabe ist damit ein **zweiseitiger Vorgang zwischen beauftragendem Kundenvertragspartner und ALISE** und vom Aktionsauftrag getrennt: Die Auftragsnachrichten `TXAAUFBER`, `TXRAUFBER` und `TXEAUFBER` stehen in derselben Tabelle als eigene Nachrichten daneben ([Q39](../../QUELLEN.md#q39), Kap. 3.2.5).

Das Glossar [Q02](../../QUELLEN.md#q02) enthält **keinen** Eintrag „Aktionsfreigabe“ (geprüft am Inhaltsverzeichnis, S. 2–13), und das dort beschriebene Statusmodell der Aktion — „bestellt“, „aktiv“, „ausgeführt“ ([Q02](../../QUELLEN.md#q02), S. 20 f.) — nennt die Freigabe nicht. Wo genau sie in diesem Modell ansetzt, ist aus den öffentlichen Quellen nicht zu entscheiden (abgeleitet: zwischen „bestellt“ und „aktiv“).

In etiCORE tragen `cancelOrder` (Stornierung eines Auftrags) und `notifyOrderSeemsToBeObsolete` (Meldung, ein Entsperrauftrag scheine erledigt) die Altbezeichner `TXAFREIBER` und `TXAFREIMITBER` ([Q50](../../QUELLEN.md#q50), `po-oa-management-messaging_xsd` und `ccp-oa-ordering-messaging_xsd`). Auch die Richtung passt zur NRW-Tabelle. Danach wäre die Freigabe eher die **Rücknahme** eines Auftrags und ihre Mitteilung (abgeleitet, O20).

Normquelle bleibt die nicht öffentliche KA AktM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 41).

## Einfach erklärt – Beispiel aus Bärstadt

Zwischen „die Bärstädter Verkehrsbetriebe bestellen etwas“ und „der Auftrag steht in der Aktionsliste“ liegt ein weiterer Handgriff: die Freigabe.

Der Ablauf hat damit drei Nachrichten statt einer. Zuerst schickt die BVB den **Auftrag**: „Schreibe Produkt 2001 auf die Karte 90000042.“ Dann schickt sie die **Freigabe**: „Dieser Auftrag darf wirksam werden.“ Und schließlich bekommt sie eine **Mitteilung** vom Aktionslistenservice zurück: „Freigabe verarbeitet.“

Warum zwei Schritte für eine Sache? Weil Bestellen und Gültigmachen verschiedene Zeitpunkte haben können. Bodo Bärlauch kann Pias Abo im Juli erfassen, obwohl ihre Ausbildung erst am 1. September beginnt. Oder ein Abo ist erfasst, aber die erste Abbuchung noch nicht bestätigt — dann will man den Auftrag vorbereitet haben, ohne ihn schon scharf zu stellen.

Die Trennung gibt also Kontrolle über das **Wann**. Der Auftrag beschreibt, *was* passieren soll. Die Freigabe entscheidet, *ab wann*.

**Ein Vorbehalt zu dieser Lesart:** Sie ist aus den Namen gewonnen, nicht aus einer Beschreibung. Die etiCORE-Schnittstellen führen `TXAFREIBER` auf eine **Stornierung** zurück. Dann hieße „Freigabe“ eher, einen Auftrag wieder aus dem Verkehr zu ziehen, und das Beispiel unten beschriebe das Gegenteil des Gemeinten. Bis das geklärt ist, bitte nur die Nachrichtennamen und ihre Richtung als gesichert nehmen.

Dass es für die Rückmeldung eine eigene Nachricht gibt, ist ebenfalls folgerichtig. Die BVB hat die Freigabe abgeschickt, aber asynchron — also ohne sofortige Antwort. Ohne Rückmeldung wüsste sie nicht, ob die Freigabe angekommen und verarbeitet ist. Und das muss sie wissen, denn sie hat Pia versprochen, dass das Abo zum 1. September gilt.

Eine Einschränkung zum Schluss, die für dieses Lexikon typisch ist: Die Nachrichtennamen und ihre Richtung sind belegt — aber aus dem Pflichtenheft **eines** Verbunds. Dass die Freigabe dort als eigener Schritt existiert, heißt nicht zwingend, dass jedes KA-System sie so einsetzt. Und was das Statusmodell des Standards dazu sagt, bleibt offen: Das Glossar kennt den Begriff gar nicht.

## Quellen

- [Q39](../../QUELLEN.md#q39) – RMV vHGS-Vertrag, Anlage 6 „Konzept Externer Mandant“, Kap. 3.2.5 (PDF-S. 52 f.): `TXAFREIBER` als Aktionsfreigabeauftrag des beauftragenden KVP und `TXAFREIMITBER` als Aktionsfreigabemitteilung des ALISE, beide asynchron; daneben die Auftragsnachrichten `TXAAUFBER`, `TXRAUFBER`, `TXEAUFBER` · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 239): Anwendungsfälle „Aktionsfreigabe senden“ und „Aktionsfreigabemitteilung entgegennehmen“; Kap. 3 (KA AktM-SPEC, Inventarnummer 41)
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management-messaging_xsd` (Element `cancelOrder`) und `ccp-oa-ordering-messaging_xsd` (Element `notifyOrderSeemsToBeObsolete`), jeweils mit `meta:old` · *Release-Kandidat*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE: **kein** Eintrag „Aktionsfreigabe“ (geprüft am Inhaltsverzeichnis, S. 2–13); S. 20 f. zum Statusmodell der Aktion

<!-- GEN:siehe_auch -->
## Siehe auch

- [Aktion](aktion.md)
- [Aktionsliste](aktionsliste.md) (TXAML)
- [Aktionslistenservice](../rollen/alise.md) (ALISE)
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
