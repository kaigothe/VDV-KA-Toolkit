---
titel: ABT in der Kernapplikation
englisch: ABT within the core application
parent: lexikon/abt.md
siehe_auch: [lexikon/grundlagen/ausbauvarianten.md, lexikon/grundlagen/versionen.md]
quellen: [Q01, Q25, Q30, Q33]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Account Based Ticketing](../abt.md) › ABT in der Kernapplikation
<!-- /GEN:breadcrumb -->

# ABT in der Kernapplikation

ABT ist in der VDV-KA **kein Fremdkörper, sondern eine vorgesehene Erweiterung**. [Q01](../../QUELLEN.md#q01) formuliert es ausdrücklich: „Im konkreten Fall der VDV-Kernapplikation und ihrer technischen Weiterentwicklung etiCORE handelt es sich bei ABT um eine **Erweiterung der sogenannten Ausbaustufen**.“

Die Begründung dafür ist bemerkenswert: Die VDV-KA ist „mit ihren MBT-Prozessen, der Werteinheiten-Berechtigung, PrePaid-Karten, eTicket und eKontrolle sowie CICO und BIBO **voll ausspezifiziert**. Damit stehen **alle benötigten Prozesse für ein interoperables ABT bereits heute im Kern zur Verfügung**. Diese müssen im Rahmen einer Erweiterung um die spezifischen Anwendungsfälle einer reinen Online-Kommunikation modifiziert werden.“ ([Q01](../../QUELLEN.md#q01))

Konkret benannt werden **zwei neue Ausbaustufen** ([Q01](../../QUELLEN.md#q01)):

| Stufe | Inhalt |
|---|---|
| **Ausbaustufe 4** | Online eTicket und Online eKontrolle |
| **Ausbaustufe 5** | Online CICO |

Sie würden „nach einem notwendigen **Beschluss der Teilnehmerversammlung**“ erarbeitet. Auf dieser Basis wären „lokale interoperable ABT-Systeme für den deutschen ÖPV schnell realisierbar“; für ein **nationales** ABT seien dagegen „weitreichende verbindliche Branchenbeschlüsse notwendig und ein Paradigmenwechsel in der gesamten Vertriebsinfrastruktur“ ([Q01](../../QUELLEN.md#q01)).

Das ordnet sich in die bestehenden [Ausbauvarianten](../grundlagen/ausbauvarianten.md) 1 bis 3 ein ([Q25](../../QUELLEN.md#q25), Anlage 2) — ABT wäre die Fortsetzung derselben Zählung (abgeleitet).

Die Arbeitsgruppe Kontrolle führt ABT entsprechend unter „Ausblick“ ([Q33](../../QUELLEN.md#q33), Kap. 6.2), gemeinsam mit einem **deutschlandweiten ALISE** (Kap. 6.3). Das Weißbuch [Q30](../../QUELLEN.md#q30) liefert dazu die Basisanforderungen.

## Einfach erklärt – Beispiel aus Bärstadt

Die Frage „KA oder ABT?" ist falsch gestellt. Nach Auffassung der VDV eTS ist ABT eine Erweiterung der KA, nicht ihr Nachfolger.

Das Argument dafür ist stärker, als man zunächst denkt. Die Kernapplikation beschreibt bereits alles, was ein Ticketsystem braucht: Produkte, Berechtigungen, Rollen, Kontrolle, Abrechnung, Check-in/Check-out. Das ist viele Jahre Arbeit, und es ist fertig.

Was fehlt, ist nicht die Fachlichkeit, sondern eine Annahme. Die KA geht davon aus, dass die Berechtigung auf dem Medium liegt und ein Terminal gelegentlich Kontakt hat. ABT dreht genau diese eine Annahme um.

Deshalb lautet der Plan nicht „neu anfangen", sondern **zwei neue Ausbaustufen ergänzen**:

**Stufe 4** wäre Online eTicket und Online eKontrolle — Pias Abo läge im Rechenzentrum statt auf der Karte, und die Kontrolle fragte dort nach.

**Stufe 5** wäre Online CICO — Check-in und Check-out mit Preisbildung im Nachhinein.

Für Bärstadt wäre das eine Fortsetzung des Wegs, den es schon gegangen ist: Variante 1 war elektronisches Bezahlen, Variante 2 der elektronische Fahrschein, Variante 3 Check-in/Check-out. Die Stufen 4 und 5 wären dieselben Dinge, nur online.

Zwei Sätze aus dem Dokument sind allerdings ernst zu nehmen.

Erstens braucht es einen **Beschluss der Teilnehmerversammlung**. Diese Stufen existieren noch nicht; sie müssten erst erarbeitet werden.

Zweitens die Unterscheidung zwischen lokal und national: Lokale ABT-Systeme wären „schnell realisierbar". Ein nationales ABT verlangt „weitreichende verbindliche Branchenbeschlüsse und einen Paradigmenwechsel in der gesamten Vertriebsinfrastruktur".

Das ist keine technische Aussage mehr, sondern eine über Organisation und Willen.

## Quellen

- [Q01](../../QUELLEN.md#q01) – VDV eTS, Einordnung von Account Based Ticketing, V1.0 (25.03.2024), S. 11: ABT als Erweiterung der Ausbaustufen; die VDV-KA ist mit ihren MBT-Prozessen voll ausspezifiziert und stellt alle für ein interoperables ABT benötigten Prozesse im Kern bereit; Erweiterung um die Anwendungsfälle reiner Online-Kommunikation; Ausbaustufe 4 „Online eTicket und Online eKontrolle“ und Ausbaustufe 5 „Online CICO“ nach einem notwendigen Beschluss der Teilnehmerversammlung; lokale interoperable ABT-Systeme schnell realisierbar, nationales ABT nur mit weitreichenden verbindlichen Branchenbeschlüssen und einem Paradigmenwechsel in der Vertriebsinfrastruktur
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2 (bestehende Ausbauvarianten 1 bis 3)
- [Q30](../../QUELLEN.md#q30) – VDV eTS, Weißbuch ABT V1.0.1 (Verfahren und Basisanforderungen)
- [Q33](../../QUELLEN.md#q33) – KCD NRW, Ergebnisdokument der Arbeitsgruppe Kontrolle, V1.3, Kap. 6.2 (Account-Based-Ticketing im Ausblick), Kap. 6.3 (Diskussion eines deutschlandweiten ALISE) · *produktbezogen*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Account Based Ticketing](../abt.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
