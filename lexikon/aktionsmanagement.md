---
titel: Aktionsmanagement
abkuerzung: AktM
englisch: action management
parent: README.md
siehe_auch: [lexikon/grundlagen/elementarprozess.md]
quellen: [Q02, Q06, Q25, Q39]
status: belegt
offene_fragen: [O9]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../README.md) › Aktionsmanagement
<!-- /GEN:breadcrumb -->

# Aktionsmanagement

Das Aktionsmanagement ist eine Verwaltungseinheit in den Systemen von beauftragendem Kundenvertragspartner, ausführendem Kundenvertragspartner und Produktverantwortlichem ([Q02](../QUELLEN.md#q02), S. 20).

Es löst ein grundlegendes Problem: Ein Hintergrundsystem kann eine Berechtigung nicht selbst auf ein Nutzermedium schreiben, dafür ist der Kontakt zu einem Terminal nötig. Eine **Aktion** ist deshalb ein vorbereiteter Auftrag, der beim nächsten Kontakt ausgeführt wird. Aktionen unterliegen einem Lebenszyklus und müssen verwaltet werden ([Q02](../QUELLEN.md#q02), S. 20).

**Lebenszyklus** ([Q02](../QUELLEN.md#q02), S. 20 f.): Die Aktion beginnt als „bestellt“, sobald der beauftragende KVP sie an den Produktverantwortlichen sendet. Dieser nimmt sie als „aktiv“ in seine Aktionsliste. Aktiv bleibt sie, bis ein ausführender KVP sie mit dem Nutzermedium durchgeführt und gemeldet hat. Der Produktverantwortliche setzt sie dann auf „ausgeführt“, wodurch sie von der Aktionsliste entfernt wird, und meldet dies dem beauftragenden KVP.

Vier Aktionen sind vorgesehen ([Q02](../QUELLEN.md#q02), S. 19): Ausgabe eines elektronischen Fahrscheins, Entsperren einer Berechtigung, Rücknahme einer Berechtigung sowie — nur für (((etiCORE — Sperren einer Berechtigung anhand der ID des Aktionsauftrags.

Das Aktionsmanagement ist eine **optionale Ergänzung** und nur zu den Ausbauvarianten 2, 2a, 2b-1 und 2b-2 zulässig ([Q25](../QUELLEN.md#q25), Anlage 2, PDF-S. 159). Normquelle ist die nicht öffentliche KA AktM-SPEC, Inventarnummer 41 ([Q25](../QUELLEN.md#q25), Kap. 3).

Im Nachrichtenfluss stehen eigene **Auftragsnachrichten** neben den Nachweisen: `TXAAUFBER` (Ausgabe), `TXRAUFBER` (Rücknahme), `TXEAUFBER` (Entsperrung) sowie `TXAFREIBER` und `TXAFREIMITBER` für die [Aktionsfreigabe](aktionsmanagement/aktionsfreigabe.md) ([Q39](../QUELLEN.md#q39), Kap. 3.2.5) · *verbundspezifisch*.

Wie sich „Aktionstyp“ und das Nachrichtenfeld `amAuftragsTyp` zueinander verhalten, ist nicht belegt (zu prüfen, O9).

## Einfach erklärt – Beispiel aus Bärstadt

Pia Brummbär beginnt ihre Ausbildung und möchte das ABO Azubi auf ihre BärenKarte bekommen. Sie geht ins Kundencenter am Honigmarkt, legt ihren Ausbildungsvertrag vor und füllt den Antrag aus. Bodo Bärlauch prüft den Nachweis und genehmigt das Abo.

Jetzt kommt das eigentliche Problem. Die Berechtigung muss auf den Chip ihrer BärenKarte geschrieben werden — aber die Karte liegt in Pias Tasche. Kein Rechenzentrum der Welt kann sie dort beschreiben. Schreiben kann nur ein Gerät, an das Pia ihre Karte tatsächlich hält.

Deshalb arbeiten die Bärstädter Verkehrsbetriebe mit **Aufträgen auf Vorrat**. Die BVB bestellt beim Bären-Verkehrsbund, dem Produktverantwortlichen für das ABO Azubi, die Aktion „Ausgabe eines Fahrscheins für die Karte 90000042“. Dieser Auftrag gilt zunächst als *bestellt*.

Der Bären-Verkehrsbund nimmt den Auftrag in seine **Aktionsliste** auf. Er ist damit *aktiv*. Die Aktionsliste ist nichts anderes als eine Merkliste: „Wenn eines dieser Nutzermedien auftaucht, tu Folgendes.“ Die BVB holt diese Liste ab und verteilt sie an ihre Terminals — an den Automaten und das Lesegerät am Hauptbahnhof, an die Geräte in den Fahrzeugen der Linie 4.

Zwei Tage später hält Pia ihre Karte an das Lesegerät am Hauptbahnhof. Das Gerät erkennt die Kartennummer, findet den passenden Auftrag in seiner Liste und schreibt das ABO Azubi auf den Chip. Erst jetzt ist das Abo wirklich auf der Karte.

Damit ist die Sache aber noch nicht abgeschlossen. Das Terminal meldet die Ausführung zurück: über die BVB an den Bären-Verkehrsbund. Der streicht den Auftrag von seiner Aktionsliste — er ist *ausgeführt* — und bestätigt der BVB, dass ihr Auftrag erledigt ist.

Diese Rückmeldung ist der Grund, warum es überhaupt ein Aktionsmanagement gibt und nicht bloß eine Liste. Jemand muss wissen, welche Aufträge noch offen sind, welche erledigt wurden und wer dafür zahlt. Die drei Zustände bestellt, aktiv und ausgeführt sind genau diese Buchführung.

Für Pia bedeutet das vor allem eines: Zwischen Bodos Genehmigung und dem fertigen Abo auf der Karte liegen ein Tag für die Listenerstellung und der nächste Besuch an einem Terminal.

## Quellen

- [Q02](../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 18 („Aktion“, „Aktionsclearing“), S. 19 („Aktionsliste“, Aufzählung der vier Aktionen), S. 20 f. („Aktionsmanagement“, Lebenszyklus, Abkürzung AktM), S. 21 („Aktionslistenservice“)
- [Q06](../QUELLEN.md#q06) – RMV PH 06-02, Kap. 1.2.2 (Datenfluss, dauerhafte Speicherung beim beauftragenden KVP), Kap. 2.1.5 (Aktionsausführung) · *verbundspezifisch: eTicket RheinMain*
- [Q39](../QUELLEN.md#q39) – RMV vHGS-Vertrag, Anlage 6, Kap. 3.2.5 (Auftragsnachrichten `TXAAUFBER`, `TXRAUFBER`, `TXEAUFBER`, Freigabenachrichten `TXAFREIBER` und `TXAFREIMITBER`, Anforderung `TXAS` mit Antwort `TXAML`, Nachweise und ihre Weiterleitung an den beauftragenden KVP) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA AktM-SPEC als Inventarnummer 41), Anlage 2 Migrationsszenarien, PDF-S. 159 (AktM als optionale Ergänzung zu den Ausbauvarianten 2, 2a, 2b-1, 2b-2), Kap. 5 (Elementarprozesse je Rolle)

<!-- GEN:unterartikel -->
## Unterartikel

- [Aktion](aktionsmanagement/aktion.md)
- [Aktionsclearing](aktionsmanagement/aktionsclearing.md)
- [Aktionsdifferenzliste](aktionsmanagement/aktionsdifferenzliste.md)
- [Aktionsfreigabe](aktionsmanagement/aktionsfreigabe.md)
- [Aktionsliste](aktionsmanagement/aktionsliste.md)
- [Änderungsreferenz](aktionsmanagement/aenderungsreferenz.md)
- [Auftragstyp](aktionsmanagement/auftragstyp.md)
- [Ausgabe EFS über Aktionsliste](aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md)
- [Entsperrnachweis](aktionsmanagement/entsperrnachweis.md)
- [Entsperrung über Aktionsliste](aktionsmanagement/entsperrung-ueber-aktionsliste.md)
- [Rücknahme EFS über Aktionsliste](aktionsmanagement/ruecknahme-efs-ueber-aktionsliste.md)
- [Terminalaktionsliste](aktionsmanagement/terminalaktionsliste.md)
<!-- /GEN:unterartikel -->

<!-- GEN:siehe_auch -->
## Siehe auch

- [Elementarprozess](grundlagen/elementarprozess.md) (EP)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../README.md) · [Register](../REGISTER.md)
<!-- /GEN:navigation -->
