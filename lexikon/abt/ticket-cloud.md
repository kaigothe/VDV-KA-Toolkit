---
titel: Ticket Cloud
englisch: ticket cloud
parent: lexikon/abt.md
siehe_auch: [lexikon/abt/account.md, lexikon/berechtigungen/berechtigung.md]
quellen: [Q01, Q02, Q30]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Account Based Ticketing](../abt.md) › Ticket Cloud
<!-- /GEN:breadcrumb -->

# Ticket Cloud

„Ticket Cloud“ bezeichnet den zentralen Ablageort der Berechtigungen beim ABT. Das Glossar nennt als eine der Ablageformen einer Berechtigung „das Hinterlegen der Berechtigung **in einer Cloud**, auf die dann mit Hilfe einer eindeutigen ID zugegriffen werden kann“ ([Q02](../../QUELLEN.md#q02), S. 30), und beschreibt beim ABT die Verknüpfung „direkt mit dem Kundenkonto im Hintergrundsystem **oder in der Cloud**“ ([Q02](../../QUELLEN.md#q02), S. 16).

[Q01](../../QUELLEN.md#q01) begründet den Wechsel: „Mit zunehmender Online-Verfügbarkeit ist es möglich, die Daten **nicht mehr dezentral zu verteilen**, sondern“ zentral zu halten.

Die Vorteile folgen aus dem Wegfall des Speicherorts auf dem Medium (abgeleitet aus [Q01](../../QUELLEN.md#q01), [Q30](../../QUELLEN.md#q30), Kap. 5.1):

- **Kein Speicherengpass.** Auf einer KA-Applikation ist nur Platz für wenige Berechtigungen; zentral entfällt diese Grenze.
- **Keine Schreibvorgänge am Medium.** Ein Ticket ist sofort gültig, der Umweg über Aktionslisten und Terminalkontakt entfällt.
- **Zentrale Statusverwaltung.** Entwertung, Sperrung, Storno und Erstattung laufen über alle Kanäle konsistent.
- **Zentrale Tarifpflege.** Tarife müssen nicht auf jedem Endgerät nachgezogen werden.
- **Einfache Medien.** Es genügt ein [ID-Token](id-token.md) ohne Secure Element und ohne SAM-Schreibvorgang.

Dem steht die Abhängigkeit von Konnektivität gegenüber ([Q01](../../QUELLEN.md#q01)) — siehe [Online- und Offline-Kontrolle](online-und-offline-kontrolle.md).

Das Weißbuch leitet daraus eine Basisanforderung ab: ein **zentrales System und eine zentrale Organisation** ([Q30](../../QUELLEN.md#q30), Kap. 5.2.7), für das Deutschlandticket ausdrücklich „den Aufbau eines zentralen ABT-Systems“ ([Q30](../../QUELLEN.md#q30), Kap. 5.2.10).

## Einfach erklärt – Beispiel aus Bärstadt

Die Ticket Cloud ist kein Produkt, sondern eine Ortsangabe: Das Ticket liegt in der Mitte, nicht am Rand.

Für Olli Tapsig hat das einen unmittelbar spürbaren Vorteil. Er kauft seinen Einzelfahrschein in der App, während die Straßenbahn einfährt — und steigt ein. Kein Terminalbesuch, kein Warten auf eine Liste.

Pia kennt das anders. Zwischen Bodos Genehmigung und dem Abo auf ihrer Karte lagen ein Listenzyklus und ein Besuch am Hauptbahnhof.

Der zweite Vorteil ist der Platz. Auf Pias Chip ist Raum für einige Berechtigungen — nicht für hunderte. Würde Bärstadt jeden Einzelfahrschein auf Chipkarten ablegen, wäre der Speicher schnell voll. Zentral spielt das keine Rolle.

Der dritte ist der leiseste und vielleicht wichtigste: **alles an einer Stelle.** Wenn Olli sein Ticket storniert, ist es sofort überall storniert — in der App, am Automaten, im Kontrollgerät. Bei Pias Karte muss eine Sperrung erst zu jedem Gerät reisen.

Dasselbe gilt für Tarife. Ändert der Bären-Verkehrsbund einen Preis, muss er es zentral tun und nicht auf jedem Gerät im Land.

Und schließlich wird das Medium billig. Olli braucht keinen Sicherheitschip, kein SAM, keine Zulassung — eine Nummer genügt.

Die Rechnung hat eine Gegenseite, und sie ist nicht klein: **Ohne Verbindung keine Auskunft.** Wo Pias Karte selbst Bescheid weiß, muss Ollis Gerät fragen. Was passiert, wenn es nicht fragen kann, ist das zentrale Thema beim ABT — und hat eigene Antworten, von Zwischenspeichern bis zur nachgelagerten Prüfung.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 30 (Cloud als Ablageform einer Berechtigung mit Zugriff über eine eindeutige ID), S. 16 (Verknüpfung mit dem Kundenkonto im Hintergrundsystem oder in der Cloud)
- [Q01](../../QUELLEN.md#q01) – VDV eTS, Einordnung von Account Based Ticketing, V1.0 (zunehmende Online-Verfügbarkeit erlaubt zentrale statt dezentrale Datenhaltung; Konnektivität als entscheidende Anforderung; Vorteile und Synchronisation beim MBT)
- [Q30](../../QUELLEN.md#q30) – VDV eTS, Weißbuch ABT V1.0.1, Kap. 5.1 (Erwartungen im Vergleich zum MBT, vertriebliche und fachliche Vorteile), Kap. 5.2.7 (zentrales System und zentrale Organisation als Basisanforderung), Kap. 5.2.10 (Aufbau eines zentralen ABT-Systems für das Deutschlandticket)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Account Based Ticketing](../abt.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
