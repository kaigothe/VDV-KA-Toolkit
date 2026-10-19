---
titel: logTransaktionsTyp
englisch: logical transaction type
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/tx-base.md, lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md]
quellen: [Q05, Q06, Q25]
status: belegt
offene_fragen: [O1]
stand: 2026-10-19
codes:
  - wert: 1
    bedeutung: Ausgabetransaktion
    quelle: Q05
    fundstelle: Kap. 4.4.4 (PDF-S. 22)
    status: belegt
    verbundspezifisch: true
  - wert: 2
    bedeutung: Entwertung
    quelle: Q05
    fundstelle: Kap. 4.4.4 (PDF-S. 22)
    status: belegt
    verbundspezifisch: true
  - wert: 20
    bedeutung: Sperrtransaktion
    quelle: Q05
    fundstelle: Kap. 4.4.4 (PDF-S. 22)
    status: belegt
    verbundspezifisch: true
  - wert: 21
    bedeutung: Entsperrtransaktion
    quelle: Q05
    fundstelle: Kap. 4.4.4 (PDF-S. 22)
    status: belegt
    verbundspezifisch: true
  - wert: 25
    bedeutung: Rückgabetransaktion
    quelle: Q05
    fundstelle: Kap. 4.4.4 (PDF-S. 23)
    status: belegt
    verbundspezifisch: true
  - wert: 27
    bedeutung: Kontrolle — TXEBER aus Kontrolle
    quelle: Q05
    fundstelle: Kap. 4.4.4 (PDF-S. 23); bestätigt in Q06 Kap. 5.1.2
    status: belegt
    verbundspezifisch: true
  - wert: 37
    bedeutung: TXABER – Ausgabe EFS über Aktionsliste
    quelle: Q06
    fundstelle: Kap. 2.1.5, Fußnote 1 (PDF-S. 13)
    status: belegt
    verbundspezifisch: true
  - wert: 38
    bedeutung: TXSNAWB – Entsperrtransaktion EFS über Aktionsliste
    quelle: Q06
    fundstelle: Kap. 2.1.5, Fußnote 1 (PDF-S. 13)
    status: belegt
    verbundspezifisch: true
  - wert: 39
    bedeutung: Rückgabetransaktion EFS über Aktionsliste
    quelle: Q06
    fundstelle: Kap. 2.1.5, Fußnote 1 (PDF-S. 13)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › logTransaktionsTyp
<!-- /GEN:breadcrumb -->

# logTransaktionsTyp

Das Feld `logTransaktionsTyp` kennzeichnet den Transaktionstyp auf Nutzermedium-Ebene. Es nutzt die Codeliste `NmTransaktionsTyp_CODE` ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1).

**Es ist nicht dasselbe wie `transTransaktionsTyp` im [`TX_BASE`](tx-base.md)**, das die Codeliste `IONTransaktionsTyp_CODE` nutzt. Beide Felder können in derselben Nachricht stehen und unterschiedliche Werte tragen: Ein `TXEBER` aus Kontrolle hat `IONTransaktionsTyp_CODE` = 059 **und** `logTransaktionsTyp.code` = 27 ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2). Diese Verwechslung ist beim Auswerten einer Nachricht eine naheliegende Fehlerquelle.

[Q05](../../QUELLEN.md#q05), Kap. 4.4.4, nennt die „relevanten Transaktionstypcodes“ vollständig; [Q06](../../QUELLEN.md#q06) bestätigt 27 und 37 bis 39:

| Wert | Bedeutung | | Wert | Bedeutung |
|---:|---|---|---:|---|
| **1** | Ausgabetransaktion | | **25** | Rückgabetransaktion |
| **2** | Entwertung | | **27** | Kontrolle |
| **20** | Sperrtransaktion | | **37** | Ausgabe EFS über Aktionsliste |
| **21** | Entsperrtransaktion | | **38** | Entsperrtransaktion EFS über Aktionsliste |
| | | | **39** | Rückgabetransaktion EFS über Aktionsliste |

**Die Systematik ist aufschlussreich:** Drei Vorgänge treten paarweise auf — Ausgabe als 1 und 37, Entsperrung als 21 und 38, Rückgabe als 25 und 39. Der niedrige Wert bezeichnet den direkten Vorgang, der hohe denselben Vorgang **über die Aktionsliste** (abgeleitet). Entwertung (2), Sperrung (20) und Kontrolle (27) haben keine Aktionslisten-Entsprechung.

Alle Werte stammen aus Verbunddokumenten. Ob sie KA-weit gelten, ist nicht belegt (zu prüfen, O1) · *verbundspezifisch*.

Die vollständige Codeliste steht in der nicht öffentlichen KA BOM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 1).

## Einfach erklärt – Beispiel aus Bärstadt

In einer KA-Nachricht gibt es nicht einen Typ, sondern zwei — und sie bedeuten verschiedene Dinge.

Man kann sich das wie bei einem Paket vorstellen. Außen auf dem Versandetikett steht eine Sendungsart: Brief, Paket, Einschreiben. Innen im Paket liegt eine Ware, und die hat ihre eigene Artikelnummer. Beide Angaben beschreiben dasselbe Paket, aber aus verschiedener Perspektive.

Bei der VDV-KA ist es genauso. Auf dem Briefkopf steht, um welche **Art von Nachricht** es sich handelt — das ist `transTransaktionsTyp`. Weiter innen, bei den Daten, die von der Karte stammen, steht, welche **Art von Vorgang auf der Karte** stattgefunden hat — das ist `logTransaktionsTyp`.

Dass das zwei Paar Schuhe sind, zeigt ein belegtes Beispiel aus dem eTicket RheinMain: Bei einem Kontrollnachweis steht außen die 59 und innen die 27. Wer nur eine der beiden Zahlen liest und sie in der falschen Tabelle nachschlägt, kommt zu einem Ergebnis, das überzeugend aussieht und falsch ist.

Für Bärstadt sind vier Zahlen interessant. Die **37** heißt: Hier wurde ein Fahrschein über die Aktionsliste ausgegeben — das ist Pias Fall. Die **38** steht für eine Entsperrung, die **39** für eine Rücknahme, und die **27** für eine Kontrolle, also für den Moment, in dem Petra Pranke in der Linie 4 eine Karte prüft.

Und die immer gleiche Warnung: Diese Zahlen stammen aus dem Pflichtenheft eines einzelnen Verbunds. Die vollständige Liste steht in einer Spezifikation, die nicht öffentlich ist. Wer eine Nachricht aus einem anderen System auswertet, muss die dort gültige Liste heranziehen. Eine Zahl, die man aus einem fremden Verbund kennt, ist ein Anhaltspunkt — kein Beleg.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5, Fußnote 1 (PDF-S. 13): `logTransaktionsTyp` vom Typ `NmTransaktionsTyp_CODE` mit den Werten 37, 38 und 39; Kap. 5.1.2 (PDF-S. 40): `TXEBER` aus Kontrolle mit `IONTransaktionsTyp_CODE` = 059 und `logTransaktionsTyp.code` = 27 · *verbundspezifisch: eTicket RheinMain*
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 4.4.4 (PDF-S. 22 f.): vollständige Liste der „relevanten Transaktionstypcodes“ 1, 2, 20, 21, 25, 27, 37, 38 und 39 · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA BOM-SPEC, Inventarnummer 1, als Normquelle der Codelisten)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
