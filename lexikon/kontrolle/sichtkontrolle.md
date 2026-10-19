---
titel: Sichtkontrolle
englisch: visual inspection
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/kontrollgeraet.md, lexikon/kontrolle/sperrliste.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Sichtkontrolle
<!-- /GEN:breadcrumb -->

# Sichtkontrolle

Eine Sichtkontrolle prüft ohne kryptografische Mittel. [Q06](../../QUELLEN.md#q06), Kap. 6.1, beschreibt einen konkreten Fall · *verbundspezifisch*:

Für Geräte, bei denen „der Einsatz eines vollwertigen mobilen Kontrollterminals wirtschaftlich nicht sinnvoll ist“, werden Smartphones mit NFC-Schnittstelle und einer App zum Einlesen und Anzeigen von KA-Berechtigungen eingesetzt. „Die Kontrolle erfolgt als **reine Sichtkontrolle mit automatischer Auswertung ausgewählter EFS-Attribute**, z. B. zeitliche Gültigkeit.“

Die Einschränkung ist präzise benannt: „Da das Smartphone **nicht über ein SAM verfügt**, erfolgen **keine kryptographischen Prüfungen** des KA-Nutzermediums und der KA-Berechtigungen und es können **keine Transaktionen mit dem Nutzermedium** durchgeführt werden.“ ([Q06](../../QUELLEN.md#q06), Kap. 6.1)

Daraus folgt, was eine Sichtkontrolle leisten kann und was nicht (abgeleitet):

| Möglich | Nicht möglich |
|---|---|
| Berechtigung lesen und anzeigen | Echtheit der Berechtigung prüfen |
| Gültigkeitszeitraum auswerten | Berechtigung oder Karte sperren |
| Personenbezug mit einem Ausweis vergleichen | einen Kontrollnachweis erzeugen |
| gegen die Sperrliste prüfen | — |

Die Sperrlistenprüfung bleibt also erhalten: Die Geräte „sollen die nutzermediumbezogene Sperrliste `TXSLNM` vom vHGS beziehen und auswerten“; ihr Datenaustausch beschränkt sich auf Manifest und Sperrlistendownload ([Q06](../../QUELLEN.md#q06), Kap. 6.1 f.).

**Perspektive:** Ab 2GSI / etiCORE wird der Kontrollnachweis nur noch an den Produktverantwortlichen gesendet, „damit ist ab 2GSI / etiCORE die Kontrolle ohne SAM möglich“ ([Q02](../../QUELLEN.md#q02), S. 53). Die heutige Beschränkung der Sichtkontrolle entfällt damit weitgehend (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Nicht jedes Kontrollgerät kann alles — und manchmal ist das eine bewusste Rechnung.

Ein vollwertiges Prüfgerät ist teuer. Es braucht einen Sicherheitsbaustein, Schlüssel, eine Zulassung. Für die Hauptlinien lohnt sich das. Für eine Nebenlinie mit drei Fahrten am Tag vielleicht nicht.

Für solche Fälle gibt es eine Sparvariante: ein gewöhnliches Smartphone mit NFC und einer App. Es liest Pias Karte, zeigt das ABO Azubi an, rechnet die Gültigkeit aus und meldet „gültig bis 31.08.2029".

Was es **nicht** kann, benennt das Pflichtenheft erfreulich offen. Ohne Sicherheitsbaustein gibt es keine kryptografischen Prüfungen und keine Transaktionen mit der Karte. Konkret heißt das:

Das Gerät kann nicht feststellen, ob die Berechtigung **echt** ist. Es liest, was auf der Karte steht, und glaubt es. Eine geschickt gefälschte Karte würde es nicht entlarven.

Es kann auch nichts **schreiben**. Findet es eine gesperrte Karte, kann es die Sperre nicht auf dem Chip vermerken — und es kann keinen Kontrollnachweis hinterlassen.

Ein Punkt bleibt aber erhalten, und das ist der wichtigste: **Die Sperrliste wird geprüft.** Das Gerät lädt sie herunter und vergleicht. Pias verlorene Karte würde also auffallen.

Damit ist die Sichtkontrolle überraschend brauchbar. Sie erkennt abgelaufene Tickets, falsche Personen und gesperrte Karten — also die Fälle, die im Alltag vorkommen. Sie erkennt keine Fälschungen, und sie hinterlässt keine Spur.

Und sie ist ein Vorgriff auf die Zukunft: In der nächsten Generation braucht auch die richtige Kontrolle keinen Sicherheitsbaustein mehr.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 6.1 „SCG Ticketinfo Mobil Kontrollgeräte“ (PDF-S. 43): Smartphones mit NFC-Schnittstelle und App zum Einlesen und Anzeigen von KA-Berechtigungen; Einsatz dort, wo ein vollwertiges mobiles Kontrollterminal wirtschaftlich nicht sinnvoll ist; reine Sichtkontrolle mit automatischer Auswertung ausgewählter EFS-Attribute; kein SAM, daher keine kryptographischen Prüfungen und keine Transaktionen mit dem Nutzermedium; Bezug und Auswertung der nutzermediumbezogenen Sperrliste `TXSLNM`; Kap. 6.2 (Beschränkung des Datenaustauschs auf Manifest und Sperrlistendownload) · *verbundspezifisch: eTicket RheinMain*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 53 (Kontrolle ohne SAM ab 2GSI / etiCORE, weil der Kontrollnachweis nicht mehr auf das Nutzermedium geschrieben wird), S. 52 (Sperren auf dem Nutzermedium ohne SAM ab 2GSI)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
