---
titel: Online- und Offline-Kontrolle
englisch: online and offline inspection
parent: lexikon/abt.md
siehe_auch: [lexikon/abt/hybridsystem.md, lexikon/kontrolle/sichtkontrolle.md]
quellen: [Q01, Q18, Q30]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Account Based Ticketing](../abt.md) › Online- und Offline-Kontrolle
<!-- /GEN:breadcrumb -->

# Online- und Offline-Kontrolle

Beim ABT verlagert sich die Prüfung ins Zentrum. „Die Kontrollgeräte müssen **in Echtzeit** mit dem zentralen System, in dem die ID-Token abgelegt sind, oder dem **Bordrechner** kommunizieren können.“ ([Q30](../../QUELLEN.md#q30), Kap. 5.2.10)

Daraus wird die bekannte Einwendung: Ohne Verbindung keine Kontrolle. [Q01](../../QUELLEN.md#q01) benennt die Abhängigkeit ausdrücklich — „da der Großteil der Verarbeitung zentral erfolgt, ist die Konnektivität von entscheidender Bedeutung“.

Das Weißbuch beschreibt die Folgen konkret: Niedrige Übertragungsraten und „Funklöcher“ können dazu führen, dass die bei der Validierung erzeugten Datensätze **nicht vor der Kontrolle** im zentralen Speicher abgelegt oder nicht abgerufen werden können ([Q30](../../QUELLEN.md#q30), Kap. 5.2.10).

Als Erfordernis nennt es daraufhin einen bemerkenswert handfesten Mechanismus ([Q30](../../QUELLEN.md#q30), Kap. 5.2.10):

> **Zwischenspeicher im Fahrzeug** und Kommunikation zwischen Kontrollgerät und Fahrzeug. Kontrolleure sperren InOut-Terminals; die InOut-Terminals erzeugen einen **Barcode**, durch dessen Abscannen die Kontrolleure alle im Bus vorhandenen ID-Token übermittelt bekommen.

Die Prüfung findet also nicht zwingend gegen das Rechenzentrum statt, sondern kann gegen das **Fahrzeug** erfolgen (abgeleitet). Das ist eine dritte Möglichkeit neben online und offline.

Als weitere Basisanforderung fordert das Weißbuch „zentrale Gültigkeitsprüfung“ mit **„einfachen“ Kontrollgeräten** ([Q30](../../QUELLEN.md#q30), Kap. 5.2.10) — die Geräte werden schlichter, weil die Prüflogik zentral liegt (abgeleitet).

Zu Validierungs- und Kontrollkonzepten im ABT siehe auch [Q18](../../QUELLEN.md#q18) · *Herstellerquelle*.

## Einfach erklärt – Beispiel aus Bärstadt

„Ohne Netz keine Kontrolle" ist der häufigste Einwand gegen ABT — und er ist zu einfach.

Richtig ist der Kern: Ollis Ticket liegt im Rechenzentrum. Kann Petra Pranke nicht nachfragen, weiß sie nicht, ob er eines hat. Bei Pias Karte wäre das kein Problem, da steht alles auf dem Chip.

Interessant wird es bei der Frage, **wen** man eigentlich fragen muss.

Das Weißbuch beschreibt einen Weg, der bei Funklöchern erstaunlich gut funktioniert und mit dem Rechenzentrum nichts zu tun hat. Der Bus weiß nämlich selbst, wer eingestiegen ist — die Terminals an der Tür haben die Kennungen gelesen und im Fahrzeug zwischengespeichert.

Petra muss also nicht das Rechenzentrum fragen. Sie fragt den Bus.

Und zwar so: Sie sperrt die Einstiegsterminals, damit niemand nachträglich eincheckt. Das Terminal erzeugt daraufhin einen **Barcode**. Petra scannt ihn mit ihrem Gerät — und hat damit alle Kennungen, die in diesem Fahrzeug unterwegs sind.

Das ist elegant, weil es ohne jede Funkverbindung auskommt und weil es die Lücke schließt, die sonst am meisten weh tut: Tickets, die Sekunden vor der Kontrolle gekauft wurden.

Daneben gibt es die weiteren Bausteine: zwischengespeicherte Listen auf dem Gerät, signierte Nachweise, nachgelagerte Prüfung.

Eine Folge dieser Verlagerung wird gern übersehen und ist für Beschaffungen bedeutsam: Die Geräte werden **einfacher**. Pias Kontrolle braucht ein Gerät mit Sicherheitsbaustein, das schreiben kann. Ollis Kontrolle braucht ein Gerät, das lesen und fragen kann — und das ist deutlich weniger.

## Quellen

- [Q30](../../QUELLEN.md#q30) – VDV eTS, Weißbuch ABT V1.0.1, Kap. 5.2.10 „Zentrale Gültigkeitsprüfung — ‚einfache‘ Kontrollgeräte“ (Echtzeitkommunikation der Kontrollgeräte mit dem zentralen System oder dem Bordrechner; Folgen niedriger Übertragungsraten und von Funklöchern; Erfordernis eines Zwischenspeichers im Fahrzeug; Sperren der InOut-Terminals durch Kontrolleure und Übermittlung aller im Fahrzeug vorhandenen ID-Token über einen vom Terminal erzeugten Barcode; Aufbau eines zentralen ABT-Systems für das Deutschlandticket), Kap. 4.1.2 und 4.2.2 (Kontrollprozesse der ABT-Varianten)
- [Q01](../../QUELLEN.md#q01) – VDV eTS, Einordnung von Account Based Ticketing, V1.0 (Konnektivität als entscheidende Anforderung; Hybridsysteme zur Minimierung von Datenverlust)
- [Q18](../../QUELLEN.md#q18) – Kentkart, „To validate, or not to validate“ (Validierungs- und Kontrollkonzepte im ABT) · *Herstellerquelle, belegt Marktpraxis*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Hybridsystem](hybridsystem.md)
- [Sichtkontrolle](../kontrolle/sichtkontrolle.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Account Based Ticketing](../abt.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
