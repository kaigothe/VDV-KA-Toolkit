---
titel: Aktionslistenservice
abkuerzung: ALISE
englisch: Action List Service
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/pv.md, lexikon/aktionsmanagement/aktionsliste.md, lexikon/transaktionen/txalisber.md]
quellen: [Q02, Q06, Q39]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes:
  - wert: 31
    codeliste: KA-Rollencode
    bedeutung: Rollencode ALISE — ab KA 1.3.0 nur für einen aus dem PV-System ausgelagerten zentralen ALISE-Server
    quelle: Q06
    fundstelle: Fußnote 7 (PDF-S. 39)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Aktionslistenservice
<!-- /GEN:breadcrumb -->

# Aktionslistenservice

Der Aktionslistenservice (ALISE) wird **vom System des Produktverantwortlichen angeboten**. Über diesen Service laden Systeme der ausführenden Kundenvertragspartner die Aktionslisten herunter und verteilen sie auf ihre Terminals. Umgekehrt können beauftragende Kundenvertragspartner Aktionen beim Produktverantwortlichen bestellen, wodurch sie auf dessen Aktionsliste gesetzt werden ([Q02](../../QUELLEN.md#q02), S. 21).

[Q39](../../QUELLEN.md#q39) wird im Glossarteil noch deutlicher: „Der ALISE ist eine **Spezialisierung der Rolle PV**, die bei Anwendung des Aktionsmanagements die entsprechende Funktionalität eines Aktionslistenservice-Systems (ALISES) in ihrem PVS vorzuhalten hat.“ ALISE ist also kein eigener Marktteilnehmer, sondern eine Ausprägung des PV. [Q06](../../QUELLEN.md#q06), Kap. 1.2.2, beschreibt den Abruf entsprechend: Jedes KVP-System führt einen Aktionslistenabruf gegen das **ALISES** durch · *verbundspezifisch*.

**Zum Rollencode 31 — hier ist Vorsicht geboten.** In der Schnittstellenversion KA 1.1.07 wurde für solche Transaktionen alternativ auch der Rollencode 31 (ALISE) akzeptiert. Ab KA 1.3.0 ist 31 seitens der VDV eTS „für einen aus dem PVS ausgelagerten eigenständigen zentralen ALISE-Server reserviert“; ist ALISE in das PV-System integriert, ist stattdessen die **Rolle 3** zu verwenden. In der TMS-Schnittstellenversion KA 1.3.0 ist für Transaktionen aus Aktionsausführungen **zwingend der Rollencode 3** zu verwenden ([Q06](../../QUELLEN.md#q06), Fußnote 7, PDF-S. 39). Die Versionshistorie nennt das „Wegfall des Rollen-Code 31 ALISE in KA 1.3.0“. **Unabhängig bestätigt** wird das durch [Q39](../../QUELLEN.md#q39), Kap. 3.3.2: Die dortige Rollentabelle führt „vHGS als ALISE PV“ mit dem **Rollencode 3**.

**Folge für die Auswertung:** Aus dem Rollencode allein lässt sich nicht auf ALISE schließen. Eine 31 deutet auf eine ältere Schnittstellenversion oder einen ausgelagerten ALISE-Server (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

ALISE klingt wie eine Organisation, ist aber ein Schalter.

Beim Bären-Verkehrsbund liegt die Aktionsliste. Damit die Bärstädter Verkehrsbetriebe sie abholen können, braucht es eine Stelle, an die sie sich wenden — und die heißt Aktionslistenservice. Der Schalter arbeitet in beide Richtungen: Die Verkehrsbetriebe holen dort die Liste ab, und sie geben dort auch ihre Aufträge auf, etwa den für Pias ABO Azubi.

In Bärstadt gibt es für diesen Schalter kein eigenes Haus. Er sitzt im System des Verkehrsbunds, so wie der Postschalter im Supermarkt sitzt. Das ist der übliche Fall.

Genau daraus folgt eine Falle, über die man leicht stolpert. In älteren Unterlagen liest man, ALISE habe die Rollennummer 31. Das stimmt so nicht mehr, und zwar aus einem nachvollziehbaren Grund: Wenn der Schalter im Haus des Verkehrsbunds sitzt, ist der Absender einer Nachricht eben der Verkehrsbund — Rolle 3. Eine eigene Nummer braucht es nur dann, wenn jemand den Schalter aus dem Haus **auslagert** und einen eigenen, zentralen Server dafür betreibt.

Für diesen Sonderfall ist die 31 reserviert. Für den Normalfall gilt die 3, und zwar ab Version 1.3.0 verbindlich.

Praktisch heißt das: Wer eine Nachricht aus dem Aktionsmanagement liest und darin die Rolle 3 findet, darf nicht schließen „also kommt sie nicht von ALISE“. Und wer eine 31 findet, hat entweder eine alte Nachricht vor sich oder einen ausgelagerten Dienst.

Das ist ein gutes Beispiel dafür, warum dieses Lexikon Fundstellen angibt. Die Aussage „ALISE hat Rollencode 31“ ist nicht falsch erfunden — sie stand so in einer Spezifikationsversion. Sie ist nur nicht mehr aktuell.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 21 („Aktionslistenservice / Action List Service“: Angebot durch das PV-System, Download durch die ausführenden KVP, Bestellung von Aktionen durch die beauftragenden KVP; Abkürzung ALISE)
- [Q39](../../QUELLEN.md#q39) – RMV vHGS-Vertrag, Glossarteil (ALISE als Spezialisierung der Rolle PV, ALISES im PVS) und Kap. 3.3.2, PDF-S. 53 (Rollentabelle „vHGS als ALISE PV“ mit Rollencode 3) · *verbundspezifisch: eTicket RheinMain*
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 1.2.2 (Aktionslistenabruf des KVP-Systems gegen das ALISES), Fußnote 7, PDF-S. 39 (Rollencode 31 in KA 1.1.07 alternativ akzeptiert; ab KA 1.3.0 für einen aus dem PVS ausgelagerten zentralen ALISE-Server reserviert; bei Integration in das PVS zwingend Rolle 3), Versionshistorie zu v2.2 („Hinweis auf Wegfall des Rollen-Code 31 ALISE in KA 1.3.0“) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Produktverantwortlicher](pv.md) (PV)
- [Aktionsliste](../aktionsmanagement/aktionsliste.md) (TXAML)
- [txalisber](../transaktionen/txalisber.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
