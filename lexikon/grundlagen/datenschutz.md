---
titel: Datenschutz
englisch: data protection
parent: lexikon/grundlagen.md
siehe_auch: [lexikon/transaktionen/pflichtelemente-einer-transaktion.md, lexikon/kontrolle/kontrollnachweise.md]
quellen: [Q06, Q43, Q48]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Grundlagen](../grundlagen.md) › Datenschutz
<!-- /GEN:breadcrumb -->

# Datenschutz

Die datenschutzrechtlichen Grundanforderungen für das [elektronische Fahrgeldmanagement](efm.md) in Deutschland sind **mit den Datenschutzbeauftragten des Bundes und der Länder entwickelt und abgestimmt**. Es sind **elf Anforderungen**, denen jeweils die Maßnahmen zu ihrer Erfüllung gegenübergestellt sind ([Q48](../../QUELLEN.md#q48), S. 3).

Der Weg dorthin ist belegt: Die 64. Konferenz der Datenschutzbeauftragten des Bundes und der Länder nahm am 24./25. Oktober 2002 in Trier ein vom Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen vorgelegtes Papier einstimmig zustimmend zur Kenntnis; mit Schreiben vom 30. Oktober 2012 erklärte dieselbe Stelle die Abstimmung unter den Aufsichtsbehörden für abgeschlossen ([Q48](../../QUELLEN.md#q48), S. 4, S. 16).

**Die elf Anforderungen** ([Q48](../../QUELLEN.md#q48), S. 2): Transparenz · Widerspruchsrecht · Wahlmöglichkeit · Datensparsamkeit · Getrennte Verarbeitung · Zweckbindung der Ticketdaten · Vorabkontrolle · Zugriffsberechtigung · Datenschutzgerechte Gestaltung der Systemkomponenten · Schutz gegen Missbrauch · Löschung.

Verbindlich werden sie über das Regelwerk: Dessen **Kapitel 6 „Datenschutz-Grundsätze“** verpflichtet die Teilnehmer auf zehn Ziffern und eine Vorabkontrolle ([Q48](../../QUELLEN.md#q48), S. 13 ff., Auszug). In KA 1.x lebt die Vorgabe als **Rahmenrichtlinie „Anlage Datenschutz“** fort, Version **1.12.1** ([Q43](../../QUELLEN.md#q43), Kap. 3, PDF-S. 27).

Drei Festlegungen sind technisch unmittelbar greifbar:

- Auf personenbezogene Daten im [Nutzermedium](../medien/nutzermedium.md) darf ein autorisiertes Terminal **nur nach PIN-Eingabe oder asymmetrischer Authentisierung** zugreifen ([Q48](../../QUELLEN.md#q48), S. 12, S. 13).
- **Fehlermeldungen an der Kundenschnittstelle dürfen den Grund** der Fehlermeldung oder [Sperre](../kontrolle/sperrung.md) — Säumnis, Vertragsbeendigung, Diebstahl — **nicht offenbaren** ([Q48](../../QUELLEN.md#q48), S. 13).
- **ORG-IDs sind vertraulich**, Nummercodes für Orte, Haltestellen und Bahnhöfe werden nicht veröffentlicht ([Q48](../../QUELLEN.md#q48), S. 10).

Was das für die Inhalte einer Transaktion bedeutet, steht in [Pflichtelemente einer Transaktion](../transaktionen/pflichtelemente-einer-transaktion.md).

## Einfach erklärt – Beispiel aus Bärstadt

Pias ABO Azubi trägt ihren Namen und ihr Geburtsdatum — das muss so sein, weil ein Ausbildungstarif personenbezogen kontrolliert wird. Genau dieser Umstand macht die Regeln nötig.

**Was Petra Pranke sieht.** Beim Kontrollgang in der Linie 4 liest Petra mit dem Gerät T-4713 die Berechtigung aus. Sie sieht, ob das Ticket räumlich und zeitlich gilt, und bei Pia zusätzlich Name und Geburtsdatum, weil sie den Ausbildungstarif gegen den Ausweis prüfen muss. Was sie nicht darf: diese Daten elektronisch sammeln. Sie werden angesehen, nicht eingesammelt.

**Was das Gerät verschweigt.** Nehmen wir an, Olli Tapsigs Berechtigung ist gesperrt, weil er seine Lastschrift nicht gedeckt hat. Am Lesegerät T-4712 am Hauptbahnhof erscheint deshalb eine Abweisung — aber ohne Grund. Kein „Zahlung offen“, kein „gestohlen“. Der Grund steht nur im Hintergrundsystem der BVB.

Das ist keine Schlamperei in der Fehlerbehandlung, sondern Absicht. Ein Gerät in einer vollen Straßenbahn soll niemanden vor anderen Fahrgästen bloßstellen. Wer ein Prüfwerkzeug baut und sich über nichtssagende Fehlermeldungen wundert: Hier ist der Grund.

**Was getrennt bleibt.** Die BVB führt zwei Welten. Im Kundencenter am Honigmarkt verwaltet Bodo Bärlauch die Stammdaten — Pias Name, ihre Anschrift, ihr Abo. In einem anderen System liegen die Fahrtdaten. Zusammengeführt werden beide nur zur Abrechnung oder wenn Pia reklamiert. Ein Bewegungsprofil darf nicht entstehen.

**Was Olli wählen darf.** Olli kauft Einzelfahrscheine, meist per App. Er muss sich nicht registrieren: Mindestens eine anonym nutzbare Form der Fahrberechtigung muss es geben — sie darf sogar der gewöhnliche Papierfahrschein sein.

**Und warum dieses Lexikon mit erfundenen Nummern arbeitet.** Die Org-IDs sind laut dieser Vorgabe vertraulich, und Ortscodes werden nicht veröffentlicht. Deshalb heißt die BVB hier 9010 und nicht so, wie ein echtes Verkehrsunternehmen heißt. Die Regel steht nicht nur im Lexikon, sie steht in der Quelle.

## Quellen

- [Q48](../../QUELLEN.md#q48) – Teilnehmerbrief Datenschutz (22.12.2014): S. 2 (die elf Anforderungen), S. 3 (Abstimmung mit den Datenschutzbeauftragten des Bundes und der Länder), S. 4 (64. Konferenz, Trier, 24./25.10.2002), S. 6 f. (Wahlmöglichkeit, Datensparsamkeit), S. 8 (getrennte Verarbeitung, Zweckbindung, Vorabkontrolle), S. 9 f. (Zugriffsberechtigung, Gestaltung, Missbrauch, Löschung), S. 10 (ORG-IDs vertraulich, Ortscodes nicht veröffentlicht), S. 12 f. (PIN oder asymmetrische Authentisierung; Regelwerk Kap. 6), S. 13 (Fehlermeldungen ohne Grund), S. 16 (Schreiben des LDI NRW vom 30.10.2012)
- [Q43](../../QUELLEN.md#q43) – etiCORE Release Letter 3.0.0-rc.6, Kap. 3, PDF-S. 27 („Anlage Datenschutz_v1121.pdf“, Rahmenrichtlinie, Version 1.12.1, aus KA 1.x übernommen)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 5.1.2 (Datenschutz: Leeren von Fahrt- und Linienangaben in Kontrollnachweisen) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Pflichtelemente einer Transaktion](../transaktionen/pflichtelemente-einer-transaktion.md)
- [Kontrollnachweise](../kontrolle/kontrollnachweise.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Grundlagen](../grundlagen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
