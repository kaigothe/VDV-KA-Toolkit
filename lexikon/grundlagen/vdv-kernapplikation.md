---
titel: VDV-Kernapplikation
abkuerzung: KA
englisch: core application
parent: lexikon/grundlagen.md
siehe_auch: [lexikon/grundlagen/versionen.md, lexikon/grundlagen/efm.md, lexikon/grundlagen/eticket-deutschland.md]
quellen: [Q02, Q25, Q37]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Grundlagen](../grundlagen.md) › VDV-Kernapplikation
<!-- /GEN:breadcrumb -->

# VDV-Kernapplikation

„Der Name Kernapplikation (KA) steht für den deutschlandweiten Standard für elektronische Fahrgeldmanagementsysteme bei unterschiedlichen ÖPV- oder Systembetreibern **in der Version 1 und 2**. Der neue Name etiCORE bezieht sich auf **Version 3**.“ ([Q02](../../QUELLEN.md#q02), S. 51)

Beide Standards umfassen **Sicherheit, Zertifizierung, Organisationskonzept und relevante Systemschnittstellen** im E-Ticketing, die die interoperable Nutzung einer ÖPV-Applikation auf einem Nutzermedium gestatten ([Q02](../../QUELLEN.md#q02), S. 51).

Definiert werden vier Gegenstände ([Q02](../../QUELLEN.md#q02), S. 51):

1. die Realisierung der Spezifikation in einer Applikation auf einem Nutzermedium und dessen Interface zu den notwendigen Akzeptanzterminals,
2. die Schnittstellen zwischen Akzeptanzterminals und Hintergrundsystemen,
3. die Schnittstellen zwischen den Hintergrundsystemen unterschiedlich ausgeprägter Fahrgeldmanagementsysteme und relevanter Instanzen,
4. den Nachweis der Standardkonformität und Sicherheit durch ein Zertifizierungsverfahren.

Der Standard ist **kein einzelnes Dokument**, sondern ein Paket. Das eTicket-Regelwerk verzeichnet die Einzeldokumente mit Inventarnummern von 0 bis 59 ([Q25](../../QUELLEN.md#q25), Kap. 3) — siehe [KA-Spezifikationen](ka-spezifikationen.md). Ein Zulassungs-Prüfbericht von 2024 führt zwölf dieser Dokumente in **Version 1.12.0** auf ([Q37](../../QUELLEN.md#q37)).

Die Zertifizierung aus Punkt 4 ist damit nicht abstrakt: Sie geschieht als Prüfung gegen eine benannte Dokumentenliste mit Versionsstand, hier bei der Zulassungsstelle des VDV eTS ([Q37](../../QUELLEN.md#q37)).

## Einfach erklärt – Beispiel aus Bärstadt

Was die Kernapplikation festlegt, lässt sich an Pias Weg nachvollziehen — und zwar genau an den vier Stellen, an denen etwas zusammenpassen muss.

**Erste Stelle: Karte und Gerät.** Auf Pias BärenKarte liegt eine Datenstruktur. Als sie die Karte an das Lesegerät am Hauptbahnhof hält, müssen beide dieselbe Sprache sprechen: gleiche Datenfelder, gleiche Reihenfolge, gleiche Sicherungsverfahren. Das legt die Kernapplikation fest.

**Zweite Stelle: Gerät und Rechenzentrum.** Das Lesegerät muss melden, was es getan hat. Dafür braucht es ein verabredetes Nachrichtenformat — sonst versteht das Rechenzentrum der Bärstädter Verkehrsbetriebe die Meldung nicht.

**Dritte Stelle: Rechenzentrum und Rechenzentrum.** Die BVB müssen dem Bären-Verkehrsbund mitteilen, dass sein Produkt ausgegeben wurde. Zwei verschiedene Organisationen, zwei verschiedene Softwarehersteller, möglicherweise zwei verschiedene Jahrzehnte der Anschaffung.

**Vierte Stelle: der Nachweis.** Und hier kommt der Punkt, der aus Papier Wirklichkeit macht. Bevor ein Gerätehersteller sein Lesegerät in Bärstadt verkaufen darf, muss er zeigen, dass es sich an die Regeln hält. Dafür gibt es eine Zulassungsstelle und Prüfberichte, in denen Dokument für Dokument steht, gegen welche Fassung geprüft wurde.

Dieser vierte Punkt ist der Grund, warum das Ganze funktioniert. Pia kann ihre Karte an ein Gerät halten, das sie nie gesehen hat, von einem Hersteller, von dem sie nie gehört hat — und es klappt, weil jemand das vorher geprüft hat.

Bemerkenswert ist noch, was die Kernapplikation **nicht** festlegt: Tarife, Preise, Produkte. Das ABO Azubi ist eine Entscheidung des Bären-Verkehrsbunds. Der Standard sagt nur, wie es auf die Karte kommt.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 51 („Kernapplikation / etiCORE“: wörtliche Definition, Version 1 und 2 als KA, Version 3 als etiCORE, Umfang Sicherheit/Zertifizierung/Organisationskonzept/Systemschnittstellen, die vier Definitionsgegenstände; Abkürzung KA)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (Verzeichnis der KA-Dokumentation mit Inventarnummern 0–59)
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht Akzeptanzterminal (2024), S. 4 (zwölf KA-Spezifikationen in Version 1.12.0; Zulassung bei der Zulassungsstelle des VDV eTS) · *Herstellerquelle, belegt den Prüfgegenstand, nicht den Standard*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Versionen](versionen.md)
- [Elektronisches Fahrgeldmanagement](efm.md) (EFM)
- [eTicket Deutschland](eticket-deutschland.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Grundlagen](../grundlagen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
