---
titel: Aktionsliste
abkuerzung: TXAML
englisch: action list
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktionsdifferenzliste.md, lexikon/aktionsmanagement/terminalaktionsliste.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktionsliste
<!-- /GEN:breadcrumb -->

# Aktionsliste

Eine Aktionsliste ist eine Liste von auszuführenden Aktionen am Kundenvertragspartner-Terminal als Spezialisierung eines Akzeptanzterminals, die beim nächsten Kontakt mit einem Nutzermedium durchgeführt werden sollen. Sie wird vom System des Produktverantwortlichen zur Verfügung gestellt, von den ausführenden Kundenvertragspartnern abgerufen und dann auf deren Akzeptanzterminals verteilt. Liegt bei Kontakt mit einem Nutzermedium für dieses eine Aktion vor, so wird diese ausgeführt ([Q02](../../QUELLEN.md#q02), S. 19).

Die Aktionsliste bildet den **kompletten derzeit gültigen Bestand** an Aktionsaufträgen für den ausführenden Kundenvertragspartner ab ([Q02](../../QUELLEN.md#q02), S. 19).

Hier unterscheiden sich die Versionen: In (((etiCORE erhält jeder beim Produktverantwortlichen anfordernde ausführende Kundenvertragspartner **dieselbe** Aktionsliste. In **KA 1.X** kann der ausführende Kundenvertragspartner die Liste über die Konfiguration von Terminalgruppen und Produkten für sich aufbereiten, sodass eine **spezifische Aktionsliste je ausführendem Kundenvertragspartner** entsteht ([Q02](../../QUELLEN.md#q02), S. 19).

Übertragen wird die Liste als Nachricht `TXAML`; die Spezifikation dazu ist die nicht öffentliche KA AktM-SPEC ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, 4.3.1).

Im eTicket RheinMain werden Sperr- und Aktionslisten **nur einmal täglich** erstellt und bereitgestellt; entsprechend ist das Abfrageintervall für die Manifest-Datei auf einmal täglich festgelegt ([Q06](../../QUELLEN.md#q06), Kap. 3.2) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Die Aktionsliste ist eine Merkliste für Terminals. Auf ihr steht, grob gesagt: „Wenn eine dieser Karten auftaucht, tu das Folgende.“

Beim Bären-Verkehrsbund, dem Produktverantwortlichen, laufen alle offenen Aufträge zusammen. Für Pias ABO Azubi steht dort ein Eintrag, für andere Fahrgäste stehen andere darin: eine Rücknahme hier, eine Entsperrung dort. Die Bärstädter Verkehrsbetriebe holen diese Liste ab und verteilen sie an ihre Geräte — an den Automaten und das Lesegerät am Hauptbahnhof und an die Geräte in den Fahrzeugen der Linie 4.

Entscheidend ist, dass die Liste immer den **vollständigen** aktuellen Bestand zeigt und nicht nur das Neue. Ein Terminal muss also nichts mitrechnen und nichts aus früheren Listen erinnern. Es hat die Wahrheit des Tages in der Hand.

„Des Tages“ ist dabei wörtlich zu nehmen. Im eTicket RheinMain wird die Liste einmal am Tag erstellt. Übertragen auf Bärstadt heißt das: Genehmigt Bodo Bärlauch Pias Abo am Dienstagnachmittag, steht ihr Auftrag erst in der Liste von Mittwoch. Und weil die Liste nur wirkt, wenn Pia auch ein Gerät berührt, kommt die Zeit bis zu ihrem nächsten Terminalkontakt noch hinzu.

Daher die Antwort auf die häufigste Kundenfrage „Warum ist mein Abo noch nicht drauf?“: Es fehlt entweder der Listenzyklus oder der Kartenkontakt — nicht die Genehmigung.

Ein Detail für später: In der VDV-KA 1.x darf sich jedes Verkehrsunternehmen seine Liste zuschneiden, etwa nach Terminalgruppen oder Produkten. In der neueren Generation bekommen alle dieselbe Liste. Das klingt nach einer Kleinigkeit, ändert aber, wie viel ein Unternehmen selbst konfigurieren muss.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19 („Aktionsliste“: Definition, Bereitstellung durch den PV, Abruf durch die ausführenden KVP, vollständiger Bestand, Unterschied KA 1.X zu (((etiCORE)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (TXAML, Verweis auf KA_SPEC_AktM), Kap. 3.2 (einmal täglich erstellt und bereitgestellt), Kap. 3.4 (Aktionsliste herunterladen), Kap. 4.3.1 · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
