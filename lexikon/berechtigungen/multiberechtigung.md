---
titel: Multiberechtigung
abkuerzung: MultiBER
englisch: multi entitlement
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/berechtigung.md, lexikon/grundlagen/ausbauvarianten.md]
quellen: [Q06, Q25, Q37, Q39]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Multiberechtigung
<!-- /GEN:breadcrumb -->

# Multiberechtigung

Die Multiberechtigung ist eine **optionale Ergänzung** der VDV-KA. Sie ist nur in Verbindung mit den Ausbauvarianten 2, 2a, 2b-1 und 2b-2 zulässig ([Q25](../../QUELLEN.md#q25), Anlage 2, PDF-S. 159) — also dort, wo es überhaupt elektronische Fahrscheine gibt.

Normquelle ist die nicht öffentliche **KA MultiBER-SPEC**, Inventarnummer 40 ([Q25](../../QUELLEN.md#q25), Kap. 3). Der vollständige Titel lautet nach [Q37](../../QUELLEN.md#q37): „Performanceverbesserung bei der EFS-Ausgabe in der Kernapplikation — Spezifikation zur Multi-Berechtigungsausgabe“. Der Zweck ist damit benannt: **Performanceverbesserung bei der Ausgabe**, also das Schreiben mehrerer Berechtigungen in einem Vorgang (abgeleitet).

**Nachrichten.** Mit der Umstellung auf **KA 1.3.0** können neben den bisherigen Transaktionen auch die Transaktionen zu Multiberechtigungen übermittelt werden ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, 4.3.2, 4.4.1) · *verbundspezifisch*:

| Nachricht | Zusammenhang |
|---|---|
| `TXAMBER` | Ausgabe, aus Aktionsausführung und aus Verkauf |
| `TXEMBER` | Kontrolle — genannt bei der Kontrolltransaktion neben `TXEBER` ([Q06](../../QUELLEN.md#q06), Kap. 4.2.3, 5.1) |
| `TXRMBER` | Rücknahme |

Die Namen folgen dem Muster der Einzelberechtigungs-Nachrichten mit eingeschobenem `M`: `TXABER` zu `TXAMBER`, `TXEBER` zu `TXEMBER`, `TXRBER` zu `TXRMBER` (abgeleitet).

Das eTicket-Regelwerk führt für das Kundenvertragspartner-System ein eigenes Paket „Multiberechtigung“ mit den Anwendungsfällen „Multiberechtigung ausgeben“, „Multi-Berechtigung_Kontrollnachweis bearbeiten“, „Multi-Berechtigung zurücknehmen“ und „Multi-Berechtigungsrücknahme entgegennehmen“ ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.1, Tabelle 37).

Im eTicket RheinMain war die Multiberechtigung zum Systemstart noch nicht im Einsatz und kam erst mit KA 1.3.0 hinzu ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5).

## Einfach erklärt – Beispiel aus Bärstadt

Eine Multiberechtigung ist mehreres auf einmal — und sie existiert aus einem sehr praktischen Grund: Zeit.

Jeder Schreibvorgang auf einer Chipkarte dauert. Nicht lange, aber messbar. Und er findet in einer Situation statt, in der niemand Zeit hat: Pia hält ihre Karte an ein Gerät, während hinter ihr die Straßenbahn einfährt.

Nun stelle man sich Familie Tatze vor. Mutter und zwei Kinder, und für den Ausflug braucht es eine Tageskarte Familie. Technisch könnten das drei einzelne Berechtigungen sein — drei Schreibvorgänge, drei Nachweise, dreimal warten.

Die Multiberechtigung erlaubt, das in einem Zug zu erledigen. Der vollständige Titel der Spezifikation sagt es unverblümt: „Performanceverbesserung bei der EFS-Ausgabe“. Es geht nicht um neue Tarifmöglichkeiten, sondern darum, dass es schneller geht.

An den Nachrichtennamen erkennt man die Systematik sofort. Aus `TXABER` für den Ausgabenachweis wird `TXAMBER`, aus `TXEBER` für die Kontrolle `TXEMBER`, aus `TXRBER` für die Rücknahme `TXRMBER`. Immer dasselbe Wort mit einem **M** in der Mitte. Wer diese Regel kennt, kann eine unbekannte Nachricht oft schon am Namen einordnen.

Zwei Einschränkungen sind wichtig.

Die Multiberechtigung ist eine **Zusatzoption**, nicht Grundbestand. Ein Verbund kann sie weglassen — Bärstadt hat sie, das eTicket RheinMain hatte sie zum Start nicht und bekam sie erst später.

Und sie setzt voraus, dass es überhaupt elektronische Fahrscheine gibt. Zu einer reinen Bezahlkarte passt sie nicht, denn es gibt nichts, wovon man mehrere ausgeben könnte.

## Quellen

- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA MultiBER-SPEC, Inventarnummer 40); Anlage 2, PDF-S. 159 (MultiBER als optionale Ergänzung nur zu den Ausbauvarianten 2, 2a, 2b-1, 2b-2); Anlage 2, Kap. 5.1.1, Tabelle 37 (Paket „Multiberechtigung“ für das Kundenvertragspartner-System mit vier Anwendungsfällen)
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht (2024), S. 4 (vollständiger Titel „Performanceverbesserung bei der EFS-Ausgabe in der Kernapplikation — Spezifikation zur Multi-Berechtigungsausgabe“, Version 1.12.0)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (`TXAMBER`, `TXRMBER` ab KA 1.3.0; zum Systemstart nicht im Einsatz), Kap. 4.2.3 und 5.1 (`TXEMBER` bei der Kontrolltransaktion), Kap. 4.3.2 und 4.4.1 (`TXAMBER` aus Aktionsausführung und aus Verkauf) · *verbundspezifisch: eTicket RheinMain*
- [Q39](../../QUELLEN.md#q39) – RMV vHGS-Vertrag (weitere Nachrichtennamen im Umfeld) · *verbundspezifisch*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Berechtigung](berechtigung.md)
- [Ausbauvarianten](../grundlagen/ausbauvarianten.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
