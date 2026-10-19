---
titel: Terminalaktionsliste
englisch: terminal action list
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktionsliste.md, lexikon/aktionsmanagement/aktionsdifferenzliste.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Terminalaktionsliste
<!-- /GEN:breadcrumb -->

# Terminalaktionsliste

Eine Terminalaktionsliste ist eine Aktionsliste, die nicht für den gesamten Kundenvertragspartner gilt, sondern für ein einzelnes Terminal oder eine Terminalgruppe.

Das eTicket-Regelwerk führt für das Kundenvertragspartner-System die Anwendungsfälle „Terminalaktionslisten bereitstellen“ und „Terminalaktionsdifferenzlisten bereitstellen“ ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38). Dieselbe Tabelle nennt die Verwaltung der Gruppen selbst: „TG_Terminal anlegen“, „TG_Terminal entfernen“, „TG_Terminal ändern“, „TG_Status aktivieren“ und „TG_Status deaktivieren“. Die Terminalgruppe ist damit ein eigenständig verwaltetes Objekt (abgeleitet).

Die Grundlage dafür liegt in der Version: In KA 1.X kann der ausführende Kundenvertragspartner die Aktionsliste über die Konfiguration von Terminalgruppen und Produkten für sich aufbereiten ([Q02](../../QUELLEN.md#q02), S. 19).

[Q06](../../QUELLEN.md#q06), Kap. 2.1.5, nennt „spezifische Aktionslisten für einzelne Terminals bzw. Terminalgruppen“ als Mechanismus der KA AktM-SPEC, der **zum Systemstart des eTicket RheinMain nicht eingesetzt** wird · *verbundspezifisch*.

Das erklärt, warum in Aktionslisteneinträgen die Felder `amTerminalGruppe_ID` und `amTerminal_ID` den Wert 0 tragen können: Die Aktion ist dann an kein bestimmtes Terminal gebunden und an jedem berechtigten Gerät ausführbar (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Bisher galt: Der Auftrag für Pias ABO Azubi liegt auf der Liste, und jedes Gerät der Bärstädter Verkehrsbetriebe kann ihn ausführen — der Automat am Hauptbahnhof genauso wie das Gerät in der Linie 4. Das ist der einfache Fall, und es ist der Fall, den Bärstadt tatsächlich nutzt.

Der Standard erlaubt aber auch, Aufträge an bestimmte Geräte zu binden. Dafür gibt es Terminalgruppen: In Bärstadt ist die Gruppe TG-40 für die Fahrzeuge der Linie 4 angelegt.

Wozu ist das gut? Ein Beispiel: Die BVB möchte, dass ein neues Produkt zunächst nur im Kundencenter am Honigmarkt ausgegeben wird, damit Bodo Bärlauch im Zweifel helfen kann. Dann bekommt nur das Terminal T-4711 die entsprechenden Aufträge. Oder umgekehrt: Ein Gerät wird gewartet und soll vorübergehend keine Aufträge mehr abarbeiten — dafür gibt es das Deaktivieren eines Gruppenstatus.

Die Kehrseite ist Verwaltungsaufwand. Jedes Gerät muss einer Gruppe zugeordnet, jede Zuordnung gepflegt und jede Gruppe aktuell gehalten werden. Und man braucht nicht mehr eine Liste, sondern viele — eine je Gruppe.

Deshalb gilt in Bärstadt wie im eTicket RheinMain: Der Mechanismus bleibt zunächst ungenutzt. In den Aufträgen stehen dann bei Terminal und Terminalgruppe schlicht Nullen.

Diese Nullen sind also keine fehlende Angabe und kein Fehler. Sie sind eine Aussage, und zwar eine nützliche: „Gilt überall.“ Wer eine solche Nachricht liest, sollte sie genau so verstehen — nicht als Lücke, sondern als bewusste Entscheidung für den einfachen Weg.

## Quellen

- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2 „KA Migrationsszenarien“ V1.6.0, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 238): „Terminalaktionslisten bereitstellen“, „Terminalaktionsdifferenzlisten bereitstellen“, „TG_Terminal anlegen/entfernen/ändern“, „TG_Status aktivieren/deaktivieren“
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19 (Aufbereitung der Liste über Terminalgruppen und Produkte in KA 1.X)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (spezifische Aktionslisten für einzelne Terminals bzw. Terminalgruppen; zum Systemstart nicht eingesetzt) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
