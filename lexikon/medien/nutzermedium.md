---
titel: Nutzermedium
abkuerzung: NM
englisch: User Medium
parent: lexikon/medien.md
siehe_auch: [lexikon/medien/applikation.md, lexikon/berechtigungen/statische-berechtigung.md]
quellen: [Q02, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Medien](../medien.md) › Nutzermedium
<!-- /GEN:breadcrumb -->

# Nutzermedium

„Das Nutzermedium kann als **Träger für eine Berechtigung** angesehen werden. Je nach Ausprägung des Nutzermediums sind verschiedene Berechtigungen möglich“ ([Q02](../../QUELLEN.md#q02), S. 66):

| Ausprägung | Mögliche Berechtigungen |
|---|---|
| **Smartcard bzw. chipbasiert** | elektronischer Fahrschein, eBezahlberechtigung |
| **Smartphone** | statische Berechtigung als 2D-Barcode; statische Berechtigung mit Motics als dynamischer 2D-Barcode oder Binärstruktur |
| **Sicherheits-Papier** | statische Berechtigung als 2D-Barcode |

Daran ist die entscheidende Regel ablesbar: **Nur ein chipbasiertes Medium kann einen EFS oder eine eBezahlberechtigung tragen.** Smartphone und Papier tragen ausschließlich [statische Berechtigungen](../berechtigungen/statische-berechtigung.md) ([Q02](../../QUELLEN.md#q02), S. 66). Der Grund liegt in der Veränderbarkeit: Ein EFS wird über ein SAM beschrieben, eine statische Berechtigung ist ein signierter, nicht veränderbarer Datensatz ([Q02](../../QUELLEN.md#q02), S. 92) (abgeleitet).

Aus Sicht des elektronischen Fahrgeldmanagements wird das Nutzermedium **eindeutig durch die [Applikationsinstanz-ID](applikationsinstanz-id.md) identifiziert** ([Q02](../../QUELLEN.md#q02), S. 24) — nicht durch eine Seriennummer des Chips.

Der Nutzer ist im Besitz des Nutzermediums und im Sinne der ISO 24014-1 der Reisende ([Q02](../../QUELLEN.md#q02), S. 66).

Normquellen sind die nicht öffentliche KA NM-SPEC (Inventarnummer 7) und mehrere Anlagen zum Systemlastenheft Nutzermedium, darunter die Zulassung von Nutzermedien als KA-Medium ([Q25](../../QUELLEN.md#q25), Kap. 3, Inv. 7 und 21–28).

Abkürzungen: **NM** (deutsch), **UM** (englisch).

## Einfach erklärt – Beispiel aus Bärstadt

Das Nutzermedium ist das, was der Fahrgast in der Hand hält — und es ist bemerkenswert, wie unterschiedlich das aussehen darf.

Pia hat eine **Chipkarte**, die BärenKarte. Olli Tapsig hat ein **Smartphone** mit einem Barcode darin. Und es gäbe noch eine dritte Möglichkeit: **Sicherheits-Papier**, also ein gedrucktes Ticket mit Barcode.

Alle drei sind Nutzermedien. Was sie können, ist aber nicht dasselbe, und der Unterschied ist grundlegend.

Nur die Chipkarte kann einen **veränderbaren** Fahrschein tragen. Pias Abo kann geschrieben, gesperrt, entsperrt und zurückgenommen werden, weil der Chip mitarbeitet und das Terminal mit seinem Sicherheitsbaustein darauf schreiben kann.

Smartphone und Papier können das nicht. Dort liegt nur ein **signierter Datensatz**, der sich nicht mehr ändert. Olli kann sein Ticket nicht sperren lassen — es gibt nichts zu sperren, der Barcode ist einfach da.

Daraus folgt die Arbeitsteilung, die man im Alltag beobachtet: Abos und Zeitkarten laufen über Chipkarten, Einzelfahrscheine und Handytickets über Barcodes. Das ist keine Vorliebe, sondern eine Eigenschaft des Mediums.

Ein Detail, das beim Auswerten von Nachrichten wichtig ist: Das System erkennt Pias Karte nicht an einer Nummer des Chips, sondern an der **Applikationsinstanz-ID**. Das ist zunächst überraschend — der Chip hat doch eine Seriennummer. Aber maßgeblich ist die Nummer der Applikation darauf, denn die wurde vom Kundenvertragspartner ausgegeben und ist im System bekannt.

Deshalb heißt es auch nie „Karte 90000042 wurde gesperrt", sondern „Applikationsinstanz 90000042". Das ist genauer, als es klingt.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 66 („Nutzermedium / User Medium“: Träger für eine Berechtigung, die drei Ausprägungen Smartcard bzw. chipbasiert, Smartphone und Sicherheits-Papier mit den jeweils möglichen Berechtigungen; Abkürzungen NM und UM; „Nutzer“ als Besitzer und Reisender nach ISO 24014-1), S. 24 (eindeutige Identifikation des Nutzermediums durch die Applikationsinstanz-ID), S. 92 („Statische Berechtigung“ als signierter, nicht veränderbarer Datensatz)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA NM-SPEC als Inventarnummer 7; Anlagen zum Systemlastenheft Nutzermedium, Inventarnummern 21 bis 28, u. a. Zulassung von Nutzermedien als KA-Medium)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Medien](../medien.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
