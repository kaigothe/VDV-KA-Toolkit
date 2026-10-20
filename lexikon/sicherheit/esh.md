---
titel: ESH
abkuerzung: ESH
englisch: e-Ticket Security Hub
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/asm.md, lexikon/rollen/ah.md, lexikon/kontrolle/hotlist-service.md, lexikon/transaktionen/nachrichten-in-ka-1-x-und-eticore.md]
quellen: [Q49, Q50]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › ESH
<!-- /GEN:breadcrumb -->

# ESH

Der ESH, der e-Ticket Security Hub, ist „the successor to the ASM“ ([Q49](../../QUELLEN.md#q49), Glossar). Er trägt den Rollencode 4 ([Q50](../../QUELLEN.md#q50), WSDL `esh`). Seine Web-Service-Schnittstelle hat vier Operationen:

| Operation | Aufrufer | Zweck |
|---|---|---|
| `getAppInstanceIdForMediumId` | CCP, SO | App-Instanz zu einer Medium-ID |
| `getOrganisationList` | CCP, PO, SO, Hotlist | Organisationen und ihre Rollen |
| `terminateUmApplication` | CCP | den Scheme Manager über eine beendete Applikation unterrichten |
| `ping` | alle Systeme | Verfügbarkeit |

([Q50](../../QUELLEN.md#q50), WSDL `esh`.)

Die Altbezeichner zeigen, woher die Aufgaben kommen: `getAppInstanceIdForMediumId` fasst `TXKNAWDM` (Namensraum `ah/2`), `TXASAINF` (`alise/2`) und die Antwort `TXADM` (`kvp-dl-pv/2`) zusammen; `getOrganisationList` stammt von `TXLKAORG` und `terminateUmApplication` von `TXRA`, beide aus `ah/2` ([Q50](../../QUELLEN.md#q50), `esh-messaging_xsd`). Abfragen, die in der KA 1.x auf [AH](../rollen/ah.md) und ALISE verteilt waren, liegen in etiCORE beim ESH (abgeleitet).

Für Medien gibt es zusätzlich eine OpenAPI-Schnittstelle (Version 1.0.0-rc.1): Individualisierungsdaten importieren, Medientypen und die Rechte abfragen, die ein Teilnehmer („TSP“) zur Produktausgabe und SAM-Aktivierung hat; Authentisierung per Mutual TLS ([Q50](../../QUELLEN.md#q50), `SAM-Server/esh`).

Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Stellen wir uns vor, der Bären-Verkehrsbund arbeitet nach etiCORE. Dann gibt es eine zentrale Stelle, die den Überblick über Organisationen und Medien hat, den ESH. Man kann ihn sich wie das Einwohnermeldeamt des Systems vorstellen.

Denkbar ist dieser Fall: Im Kundencenter am Honigmarkt hält Bodo Bärlauch Pias BärenKarte ans Gerät. Es kennt die Nummer des Mediums, braucht aber die zugehörige App-Instanz. Also fragt die BVB den ESH: `getAppInstanceIdForMediumId`. Zurück kommt die App-Instanz, hier 90000042 der BVB.

Auch die BVB selbst muss wissen, welche Organisationen es gibt und in welcher Rolle. Dafür ist `getOrganisationList` da: Die BVB erscheint darin als CCP und als SO, der BVV als PO.

Gibt Pia ihre Karte zurück und die BVB beendet die Applikation, meldet sie das dem Scheme Manager mit `terminateUmApplication`.

Hinter den neuen Namen steckt ein Umbau: Was früher mal beim Applikationsherausgeber, mal beim Aktionslistenservice abgefragt wurde, geht nun an einen Ort.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: WSDL `esh` (Operationen, Aufrufer, Rolle 4), `esh-messaging_xsd` (Beschreibungen, `meta:old`), OpenAPI `SAM-Server/esh` · *Release-Kandidat*
- [Q49](../../QUELLEN.md#q49) – etiCORE Specification, Glossar, Eintrag *ESH*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [ASM](asm.md) – der Vorgänger
- [Applikationsherausgeber](../rollen/ah.md) – dessen Aufgaben der ESH übernimmt
- [Hotlist Service](../kontrolle/hotlist-service.md) – ESH pflegt Schlüssel und Organisationen in der Hotlist
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md) – Altnamen

<!-- GEN:siehe_auch -->
## Siehe auch

- [ASM](asm.md)
- [Applikationsherausgeber](../rollen/ah.md) (AH)
- [Hotlist Service](../kontrolle/hotlist-service.md)
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
