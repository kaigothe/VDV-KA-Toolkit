---
titel: etiCORE
englisch: etiCORE
parent: lexikon/grundlagen.md
siehe_auch: [lexikon/grundlagen/spezifikationsmodell.md, lexikon/rollen/rollennamen-in-eticore.md]
quellen: [Q02, Q43, Q44]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Grundlagen](../grundlagen.md) › etiCORE
<!-- /GEN:breadcrumb -->

# etiCORE

**etiCORE ist der Name der Version 3 der VDV-Kernapplikation** ([Q02](../../QUELLEN.md#q02), S. 51) — siehe [Versionen](versionen.md).

**Stand:** Die jüngste belegte Fassung ist **3.0.0-rc.6 vom 24. November 2025**, ein Release-Kandidat, der „für Ausschreibungen und Systementwicklung verwendet werden kann“; empfohlen wird, „immer den aktuellsten Release-Kandidaten zu verwenden“ ([Q43](../../QUELLEN.md#q43), Vorwort, PDF-S. 4). Eine freigegebene Version 3.0.0 lag zu diesem Zeitpunkt also noch nicht vor (abgeleitet).

**Der Formunterschied zu KA 1.x ist grundlegend.** Nicht die Dokumente sind die Quelle, sondern ein **[Spezifikationsmodell](spezifikationsmodell.md)**: Es „beinhaltet alle Informationen, die in den nachfolgenden Spezifikationen enthalten sind. Die nachfolgenden Spezifikationen stellen einen speziellen Export aus dem Spezifikationsmodell dar“ ([Q43](../../QUELLEN.md#q43), Kap. 2.1, PDF-S. 23).

**Zuschnitt der Pflichten:** Release-Kandidat 6 teilt die Basispakete für Terminals und Hintergrundsysteme neu auf. Dadurch entfallen Anwendungsfälle, „die für das Umsetzen nicht notwendig sind, vorher aber im umsetzungspflichtigen Basispaket enthalten waren“; zusätzlich werden **optionale Pakete und Anwendungsfälle** definiert und im Modell gekennzeichnet ([Q43](../../QUELLEN.md#q43), Kap. 1.1.1, PDF-S. 4).

**Aufbau der Spezifikation:** querschnittlich SPEC-MAIN mit Rollenmodell und Prozessbeschreibungen in BPMN sowie SPEC-ION für den sicheren Nachrichtenaustausch zwischen Hintergrundsystemen; dazu je Rolle eine Referenzspezifikation für System und Terminal ([Q43](../../QUELLEN.md#q43), Kap. 2.1, PDF-S. 23 ff.) — siehe [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md).

**Nicht alles wird neu.** Sieben Dokumente aus KA 1.x gelten in **Version 1.12.1** weiter: die fünf PKM-Spezifikationen, die Rahmenrichtlinie „Anlage Datenschutz“ und die **„Anlage TLV EFS“** mit dem Basisobjektmodell ([Q43](../../QUELLEN.md#q43), Kap. 3, PDF-S. 27). Der [TLV-EFS](../berechtigungen/efs.md) bleibt damit auch unter etiCORE die Grundlage (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Für Bärstadt ist etiCORE der Umzug in ein neues Haus — bei dem das halbe Mobiliar mitkommt.

**Was sich ändert: die Namen.** Die Bärstädter Verkehrsbetriebe sind heute KVP. Unter etiCORE heißen sie CCP, Customer Contract Partner. Der Bären-Verkehrsbund ist heute PV und wird PO, Product Owner. Wer alte und neue Unterlagen nebeneinanderlegt, muss diese Übersetzung ständig im Kopf haben.

**Was sich ändert: die Form der Spezifikation.** Bisher war die VDV-KA ein Stapel PDF-Dokumente. Unter etiCORE ist sie ein Modell — eine verlinkte Darstellung von Prozessen, Datentypen und Schnittstellen, aus der die Dokumente erzeugt werden. Für Bodo Bärlauch im Kundencenter ändert das nichts. Für den Hersteller, der das System der BVB baut, ändert es alles: Er liest nicht mehr ein Kapitel, er folgt einem Prozess durch das Modell.

**Was sich ändert: der Umfang der Pflicht.** Bisher war ein Basispaket ein Basispaket, und wer es umsetzte, setzte alles darin um. Jetzt sind Teile davon ausdrücklich optional gekennzeichnet. Die BVB kann also kleiner anfangen als früher.

**Was bleibt.** Pias BärenKarte. Die Tarifmodule. Und vor allem: der TLV-EFS, also die Art, wie eine Berechtigung auf dem Chip kodiert ist. Das steckt in der „Anlage TLV EFS“, und die gilt in Version 1.12.1 weiter. Wer heute lernt, eine Berechtigung zu lesen, lernt nichts Verlorenes.

**Was man beim Datum beachten sollte.** Die jüngste Fassung, die hier belegt ist, trägt den Zusatz „rc.6“ — Release-Kandidat sechs, November 2025. Das ist noch keine freigegebene Version. Der VDV empfiehlt ausdrücklich, immer den neuesten Kandidaten zu nehmen. Für ein Werkzeug heißt das: Was man heute gegen etiCORE baut, kann sich morgen noch ändern. Gegen KA 1.x gebaut, ist man auf festerem Boden.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 51 (Kernapplikation als Name für Version 1 und 2, etiCORE für Version 3)
- [Q43](../../QUELLEN.md#q43) – etiCORE Release Letter 3.0.0-rc.6 (24.11.2025): Vorwort, PDF-S. 4 (Release-Kandidat für Ausschreibungen und Systementwicklung, Empfehlung zum jeweils aktuellsten Kandidaten), Kap. 1.1.1, PDF-S. 4 (Aufteilung der Basispakete, optionale Pakete und Anwendungsfälle), Kap. 1.1.2, PDF-S. 4 (neue Spezifikationen für CCP-STE und eCCP), Kap. 2.1, PDF-S. 23 ff. (Spezifikationsmodell als Quelle, Dokumente als Export; SPEC-MAIN, SPEC-ION, Referenzspezifikationen je Rolle), Kap. 2.2, PDF-S. 25 (CipherSuite-Spezifikation für etiCORE/2GSI), Kap. 3, PDF-S. 27 (aus KA 1.x übernommene Dokumente in Version 1.12.1)
- [Q44](../../QUELLEN.md#q44) – etiCORE Release Letter 3.0.0-rc.1 (ältere Fassung zum Vergleich) · *Auswertung offen*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Spezifikationsmodell](spezifikationsmodell.md)
- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Grundlagen](../grundlagen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
