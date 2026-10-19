---
titel: Aktionsdifferenzliste
englisch: action difference list
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktionsliste.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktionsdifferenzliste
<!-- /GEN:breadcrumb -->

# Aktionsdifferenzliste

Neben der vollständigen Aktionsliste kennt die VDV-KA eine Aktionsdifferenzliste. Das eTicket-Regelwerk führt für das Kundenvertragspartner-System die Anwendungsfälle „Aktionsdifferenzliste anfordern und empfangen“ sowie „Terminalaktionsdifferenzlisten bereitstellen“ als Teil des Pakets Aktionsmanagement ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38).

Die Mechanismen sind in der KA AktM-SPEC beschrieben. [Q06](../../QUELLEN.md#q06), Kap. 2.1.5, nennt sie ausdrücklich als Paar: „die in der Spezifikation […] beschriebenen Mechanismen a) Differenzlisten und b) spezifische Aktionslisten für einzelne Terminals bzw. Terminalgruppen“.

Beide Mechanismen werden **zum Systemstart des eTicket RheinMain nicht eingesetzt**; es ist geplant, sie in einer nachfolgenden Ausbaustufe des Systems zu ergänzen ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5) · *verbundspezifisch*.

Der Zweck ergibt sich aus der Gegenüberstellung: Weil die [Aktionsliste](aktionsliste.md) stets den kompletten derzeit gültigen Bestand an Aktionsaufträgen abbildet ([Q02](../../QUELLEN.md#q02), S. 19), wächst ihr Umfang mit der Zahl offener Aufträge. Eine Differenzliste überträgt nur die Änderungen gegenüber einem bekannten Stand und spart damit Datenvolumen und Übertragungszeit (abgeleitet).

Welche Felder eine Differenzliste trägt und wie ein Terminal den Bezugsstand bestimmt, ist aus den öffentlichen Quellen nicht zu belegen (zu prüfen).

## Einfach erklärt – Beispiel aus Bärstadt

Eine Aktionsliste ist vollständig: Jeden Tag steht alles darauf, was offen ist. Das ist bequem, aber mit der Zeit unnötig schwer.

Man stelle sich den Fahrplanaushang an der Haltestelle Tannenweg vor. Wenn sich eine einzige Abfahrtszeit ändert, könnte man den ganzen Aushang neu drucken und austauschen. Das ist sicher und einfach — jeder sieht sofort den gültigen Stand. Oder man hängt einen kleinen Zettel daneben: „Achtung, die 7:42 fährt jetzt um 7:45.“ Das ist die Differenzliste.

Für die Bärstädter Verkehrsbetriebe mit einigen tausend offenen Aufträgen ist der vollständige Aushang kein Problem. Hätte das Bärenland aber eine Million Kundinnen und Kunden und müsste jedes Fahrzeuggerät die Liste über Mobilfunk laden, sähe das anders aus: Dann lohnt es sich, nur noch die Änderungen zu schicken.

Der Preis dafür ist Buchführung. Beim vollständigen Aushang genügt ein Blick. Beim Zettel daneben muss man wissen, zu welchem Aushang er gehört — sonst klebt die Korrektur am falschen Fahrplan. Ein Gerät, das Differenzlisten verarbeitet, muss also seinen letzten Stand kennen und merken, welche Änderungen es schon eingearbeitet hat.

Genau deshalb ist es nachvollziehbar, dass das eTicket RheinMain diesen Mechanismus zum Start **nicht** genutzt hat, obwohl der Standard ihn vorsieht. Man hat mit dem einfachen, robusten Verfahren angefangen und sich die Sparvariante für später vorbehalten. Das ist bei der VDV-KA ein wiederkehrendes Muster: Der Standard kann mehr, als ein einzelner Verbund zum Start einschaltet.

## Quellen

- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2 „KA Migrationsszenarien“ V1.6.0, Kap. 5.1.2, Tabelle 38 „Aktionsmanagement für das Kundenvertragspartner-System“ (Anlagenseite 95, PDF-S. 238): Anwendungsfälle „Aktionsdifferenzliste anfordern und empfangen“, „Terminalaktionsdifferenzlisten bereitstellen“
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19 (die Aktionsliste bildet den kompletten derzeit gültigen Bestand ab)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (Differenzlisten als Mechanismus der KA AktM-SPEC; zum Systemstart nicht eingesetzt, Ergänzung in einer nachfolgenden Ausbaustufe geplant) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
