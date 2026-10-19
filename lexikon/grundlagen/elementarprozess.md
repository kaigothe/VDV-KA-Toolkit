---
titel: Elementarprozess
abkuerzung: EP
englisch: Basic Process
parent: lexikon/grundlagen.md
siehe_auch: [lexikon/transaktionen/transaktion.md, lexikon/aktionsmanagement/aktion.md]
quellen: [Q02, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Grundlagen](../grundlagen.md) › Elementarprozess
<!-- /GEN:breadcrumb -->

# Elementarprozess

„Ein Elementarprozess bezeichnet eine fachlich zusammenhängende Menge von **Transaktionen, Aktionen, Nachrichten und/oder Prüfungen**, die auf unterschiedliche Systeme verteilt sein können und jeweils einzelnen Anwendungsfällen zugeordnet werden. Ein Elementarprozess enthält somit in der Regel mehrere Anwendungsfälle.“ ([Q02](../../QUELLEN.md#q02), S. 38)

Der Begriff ist die **Brücke zwischen Fachlichkeit und Technik**: Er bündelt, was zusammengehört, auch wenn es über mehrere Systeme und mehrere Nachrichten verteilt ist (abgeleitet).

Wie das in der Praxis aussieht, zeigt das eTicket-Regelwerk. Es listet die Anwendungsfälle **je Rolle und je Paket** auf. Für das Kundenvertragspartner-System im Paket Aktionsmanagement sind das 21 Anwendungsfälle ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38), darunter:

- „Aktionsauftrag EFS_Berechtigung ausgeben“, „… zurücknehmen“, „Aktionsauftrag Berechtigung entsperren“
- „EFS_Berechtigung ausgeben nach Aktionsauftrag“, „… zurücknehmen nach Aktionsauftrag“
- „Entsperrnachweis bearbeiten nach Aktionsauftrag“, „Entsperrnachweis an PV melden“
- „Aktionsfreigabe senden“, „Aktionsfreigabemitteilung entgegennehmen“
- „Aktionslisten anfordern und empfangen“, „Aktionsdifferenzliste anfordern und empfangen“
- „Terminalaktionslisten bereitstellen“, „Terminalaktionsdifferenzlisten bereitstellen“
- „Applikationsinformation anfordern und empfangen“
- „TG_Terminal anlegen / entfernen / ändern“, „TG_Status aktivieren / deaktivieren“

Diese Listen sind der Grund, warum sich der Funktionsumfang einer [Ausbauvariante](ausbauvarianten.md) überhaupt vertraglich fassen lässt: Sie werden „in funktionsorientierten Paketen zusammengefasst, die gemeinsam ein funktionsfähiges System oder eine Systemkomponente beschreiben“ ([Q25](../../QUELLEN.md#q25), Anlage 2, PDF-S. 158).

Zur Abgrenzung: Eine [Transaktion](../transaktionen/transaktion.md) findet zwischen Nutzermedium und Terminal statt, eine [Aktion](../aktionsmanagement/aktion.md) ist ein vorbereiteter Auftrag — ein Elementarprozess fasst beides mit Nachrichten und Prüfungen zu einem fachlichen Ganzen zusammen.

## Einfach erklärt – Beispiel aus Bärstadt

Der Begriff ist sperrig, die Idee dahinter einfach: Was fachlich eine Sache ist, besteht technisch meist aus vielen Teilen.

„Pia bekommt ihr ABO Azubi“ ist für sie ein Vorgang. Technisch ist es eine ganze Kette: Die Bärstädter Verkehrsbetriebe schicken einen Auftrag. Der Bären-Verkehrsbund nimmt ihn in die Aktionsliste. Die Verkehrsbetriebe holen die Liste ab. Ein Terminal arbeitet den Eintrag ab. Ein Nachweis geht zurück. Der Auftrag wird gestrichen. Die Verkehrsbetriebe erfahren davon.

Sieben Schritte, drei Systeme, mindestens vier Nachrichten — und ein Vorgang. Genau dieses Bündel nennt der Standard einen Elementarprozess.

Warum ist das mehr als eine Bezeichnung? Weil es die Einheit ist, in der man über solche Systeme **verhandelt**.

Das zeigt die Liste im Regelwerk sehr schön. Dort steht nicht „das Verkehrsunternehmen muss das Aktionsmanagement unterstützen“ — das wäre zu unbestimmt für einen Vertrag. Stattdessen stehen 21 einzelne Anwendungsfälle: Aktionsauftrag ausgeben. Aktionsliste anfordern. Entsperrnachweis an den Produktverantwortlichen melden. Terminal einer Gruppe hinzufügen.

Jeder einzelne ist prüfbar. Ein Hersteller kann zeigen, dass sein System genau diese Fälle beherrscht, und die Zulassungsstelle kann es nachprüfen.

Daraus ergibt sich auch, was eine Ausbauvariante eigentlich ist: ein benanntes Bündel solcher Fälle. „Wir machen Variante 2a mit Aktionsmanagement“ heißt übersetzt: Diese Liste von Anwendungsfällen setzen wir um, die anderen nicht.

Für das Lesen von Spezifikationen lohnt sich darum die Frage: Welcher Elementarprozess ist hier eigentlich gemeint? Eine einzelne Nachricht ergibt oft erst in seinem Zusammenhang Sinn.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 38 („Elementarprozess / Basic Process“: wörtliche Definition, Verteilung über Systeme, Zuordnung zu Anwendungsfällen; Abkürzungen EP und BP)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2 „KA Migrationsszenarien“ V1.6.0, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 238): die 21 Anwendungsfälle des Pakets Aktionsmanagement für das Kundenvertragspartner-System; PDF-S. 158 (Zusammenfassung der Anwendungsfälle in funktionsorientierten Paketen je Ausbauvariante); Kap. 5.1 ff. (weitere Pakete je Rolle)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Transaktion](../transaktionen/transaktion.md)
- [Aktion](../aktionsmanagement/aktion.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Grundlagen](../grundlagen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
