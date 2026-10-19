---
titel: Personengebunden
englisch: Person-Related
parent: lexikon/medien.md
siehe_auch: [lexikon/berechtigungen/efs.md, lexikon/berechtigungen/produktspezifischer-teil.md]
quellen: [Q02, Q11, Q12]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Medien](../medien.md) › Personengebunden
<!-- /GEN:breadcrumb -->

# Personengebunden

„Der Begriff ‚personengebunden‘ wird üblicherweise im Zusammenhang mit Berechtigungen verwendet und bedeutet, dass eine **Berechtigung nur für eine bestimmte Person gültig und nicht übertragbar** ist.“ ([Q02](../../QUELLEN.md#q02), S. 71)

Das Gegenstück beschreibt der Eintrag zum elektronischen Fahrschein: *übertragbar* bedeutet, dass der Besitz des EFS ausreicht und jeder ihn verwenden darf; *personengebunden* bedeutet, dass nur eine bestimmte Person ihn verwenden darf — und dafür werden bei der Kontrolle **zusätzliche Identifikationsmittel** herangezogen ([Q02](../../QUELLEN.md#q02), S. 38).

Technisch liegen die dafür nötigen Daten im [produktspezifischen Teil](../berechtigungen/produktspezifischer-teil.md) der Berechtigung, unter dem TLV-Tag **0xDB „Fahrgast“** mit den Feldern `efsFahrgastName`, `efsFahrgastGeburtsdatum` und `efsFahrgastGeschlecht` ([Q12](../../QUELLEN.md#q12)). Für den Namen gilt eine Kürzungsregel, für fehlende Geburtsdaten ein Standardwert ([Q12](../../QUELLEN.md#q12)) · *Herstellerquelle*.

**Personengebunden ist nicht dasselbe wie personalisiert** (abgeleitet):

| Begriff | Bezugspunkt |
|---|---|
| **personengebunden** | Eigenschaft der **Berechtigung** — nicht übertragbar |
| **personalisiert** | Zustand der **Applikation** — es sind personengebundene Daten aufgebracht ([Q02](../../QUELLEN.md#q02), S. 70) |
| **anonym** | Eigenschaft im **Hintergrundsystem** — dort sind keine Personendaten hinterlegt ([Q02](../../QUELLEN.md#q02), S. 22) |

Dass die Daten auf dem Medium liegen, ist der Grund, weshalb die Kontrolle ohne Rückfrage beim Hintergrundsystem prüfen kann, ob die vorzeigende Person die berechtigte ist (abgeleitet). In der ausgewerteten Nachricht enthält der produktspezifische Teil eines Azubi-Abos entsprechend Name und Geburtsdatum ([Q11](../../QUELLEN.md#q11)).

## Einfach erklärt – Beispiel aus Bärstadt

„Personengebunden" heißt: Dieses Ticket gehört Pia, und niemandem sonst.

Praktisch bedeutet das, dass Petra Pranke bei der Kontrolle zwei Dinge tut. Erst liest sie die Karte und sieht das ABO Azubi. Dann fragt sie nach einem Ausweis — denn auf der Karte stehen Name und Geburtsdatum, und sie darf prüfen, ob die Person vor ihr dazu passt.

Das Gegenteil ist der übertragbare Fahrschein. Olli Tapsigs Einzelfahrschein gehört dem, der ihn hat. Er könnte ihn weitergeben, und der Nächste dürfte damit fahren. Entsprechend fragt niemand nach einem Ausweis.

Warum macht man Tickets überhaupt personengebunden? Weil manche Preise an eine Person geknüpft sind. Pias Abo ist günstig, weil sie Auszubildende ist. Wäre es übertragbar, könnte die ganze Familie mit dem Azubi-Rabatt fahren.

Nun zu drei Begriffen, die ständig verwechselt werden — und der Unterschied ist bei Datenschutzfragen entscheidend:

**Personengebunden** ist eine Eigenschaft des **Tickets**: nicht übertragbar.

**Personalisiert** ist ein Zustand der **Karte**: Es sind Personendaten darauf aufgebracht.

**Anonym** ist eine Eigenschaft im **Rechenzentrum**: Dort ist zu dieser Karte nichts über eine Person gespeichert.

Diese drei können in überraschenden Kombinationen auftreten. Eine Karte kann personalisiert sein und ein übertragbares Ticket tragen. Und eine Karte ohne jeden Namenseintrag kann im Rechenzentrum sehr wohl einem Kunden zugeordnet sein — dann ist sie nicht anonym, obwohl auf ihr nichts steht.

Ein letzter Punkt mit praktischem Wert: Weil Name und Geburtsdatum **auf der Karte** liegen, kann Petra auch dort kontrollieren, wo ihr Gerät keinen Empfang hat.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 71 („Personengebunden / Person-Related“: wörtliche Definition, nur für eine bestimmte Person gültig und nicht übertragbar), S. 38 (übertragbar gegenüber personengebunden beim EFS, zusätzliche Identifikationsmittel bei der Kontrolle), S. 70 („Personalisierung der Applikation“), S. 22 (Anonymität als Eigenschaft im Hintergrundsystem)
- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings (Tag 0xDB „Fahrgast“ mit `efsFahrgastName`, `efsFahrgastGeburtsdatum` und `efsFahrgastGeschlecht`; Kürzungsregel für Namen, Standardwert für fehlende Geburtsdaten) · *Herstellerquelle, belegt Marktpraxis, nicht den Standard*
- [Q11](../../QUELLEN.md#q11) – ausgewertete Nachricht (Name und Geburtsdatum im produktspezifischen Teil eines Azubi-Abos). **Nicht öffentliche Unterlage.**

<!-- GEN:siehe_auch -->
## Siehe auch

- [Elektronischer Fahrschein](../berechtigungen/efs.md) (EFS)
- [Produktspezifischer Teil](../berechtigungen/produktspezifischer-teil.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Medien](../medien.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
