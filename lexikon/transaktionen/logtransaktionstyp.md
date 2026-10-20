---
titel: logTransaktionsTyp
englisch: logical transaction type
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/tx-base.md, lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md]
quellen: [Q05, Q06, Q25, Q52, Q55]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 0
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: unspezifiziert/andere
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 86)
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Ausgabetransaktion Applikation/Berechtigung
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 86)
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Entwertung — Ci für Fahrt
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 86)
    status: belegt
    verbundspezifisch: false
  - wert: 20
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Sperrtransaktion Applikation/Berechtigung
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 86)
    status: belegt
    verbundspezifisch: false
  - wert: 21
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Entsperrtransaktion Applikation/Berechtigung
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 86)
    status: belegt
    verbundspezifisch: false
  - wert: 25
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Rückgabetransaktion Applikation/Berechtigung
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 86)
    status: belegt
    verbundspezifisch: false
  - wert: 27
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Kontrolle — ohne Motics
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 86)
    status: belegt
    verbundspezifisch: false
  - wert: 37
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Ausgabe EFS über Aktionsliste
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 87); ergänzt durch Q55 Kap. 6.2 (S. 67)
    status: belegt
    verbundspezifisch: false
  - wert: 38
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Entsperrtransaktion BER über Aktionsliste
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 87); ergänzt durch Q55 Kap. 6.2 (S. 67)
    status: belegt
    verbundspezifisch: false
  - wert: 39
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Rückgabe/Rücknahme EFS über Aktionsliste
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 87); ergänzt durch Q55 Kap. 6.2 (S. 67)
    status: belegt
    verbundspezifisch: false
  - wert: 40
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Rücknahme BER ohne Prioritätenlisteneintrag — in der KA 1.x wird stattdessen 0 verwendet, 40 erst ab Version 3.0.0
    quelle: Q52
    fundstelle: Tab. 6-65, Fußnote 10 (S. 87)
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › logTransaktionsTyp
<!-- /GEN:breadcrumb -->

# logTransaktionsTyp

Das Feld `logTransaktionsTyp` kennzeichnet den Transaktionstyp auf Nutzermedium-Ebene und nutzt die Codeliste `NmTransaktionsTyp_CODE`. Diese „klassifiziert Arten von Transaktionen, die mit Wertobjekten auf dem Nutzermedium auftreten“; die Normquelle nennt als Entsprechung `EN 1545: EventTypeCode` ([Q52](../../QUELLEN.md#q52), Tab. 6-65, S. 85 ff.).

**Es ist nicht dasselbe wie `transTransaktionsTyp` im [`TX_BASE`](tx-base.md)**, das die Codeliste `IONTransaktionsTyp_CODE` nutzt. Beide Felder können in derselben Nachricht stehen und unterschiedliche Werte tragen: Ein `TXEBER` aus Kontrolle hat `IONTransaktionsTyp_CODE` = 059 **und** `logTransaktionsTyp.code` = 27 ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2). Diese Verwechslung ist beim Auswerten einer Nachricht eine naheliegende Fehlerquelle.

Die im Lexikon behandelten Werte, alle aus der Standardcodeliste:

| Wert | Bedeutung | | Wert | Bedeutung |
|---:|---|---|---:|---|
| **0** | unspezifiziert/andere | | **25** | Rückgabetransaktion Applikation/Berechtigung |
| **1** | Ausgabetransaktion Applikation/Berechtigung | | **27** | Kontrolle, ohne Motics |
| **2** | Entwertung, Ci für Fahrt | | **37** | Ausgabe EFS über Aktionsliste |
| **20** | Sperrtransaktion Applikation/Berechtigung | | **38** | Entsperrtransaktion BER über Aktionsliste |
| **21** | Entsperrtransaktion Applikation/Berechtigung | | **39** | Rückgabe/Rücknahme EFS über Aktionsliste |

**Die Systematik:** Drei Vorgänge treten paarweise auf — Ausgabe als 1 und 37, Entsperrung als 21 und 38, Rückgabe als 25 und 39. Der niedrige Wert bezeichnet den direkten Vorgang, der hohe denselben Vorgang **über die Aktionsliste**. Die drei hohen Werte sind von der KA AktM-SPEC ergänzt worden ([Q55](../../QUELLEN.md#q55), Kap. 6.2, S. 67). Entwertung, Sperrung und Kontrolle haben keine Aktionslisten-Entsprechung.

**Die Werte gelten KA-weit.** [Q05](../../QUELLEN.md#q05) und [Q06](../../QUELLEN.md#q06) nennen sie als „relevante Transaktionstypcodes“ des eTicket RheinMain — eine **Auswahl aus der Standardliste**, keine eigene Festlegung.

**Zwei Versionsvorbehalte:** Für „Rücknahme BER ohne Prioritätenlisteneintrag“ ist 40 festgelegt, „zur Zeit“ wird aber **0** verwendet; 40 gilt erst ab 3.0.0. Und **41 und 42 sind doppelt belegt** — als Kontrolle mit Motics und, ab 3.0.0, als rekonstruierte IN- bzw. OUT-Transaktion ([Q52](../../QUELLEN.md#q52), Fußnoten 9 und 10, S. 86 f.).

## Einfach erklärt – Beispiel aus Bärstadt

In einer KA-Nachricht gibt es nicht einen Typ, sondern zwei — und sie bedeuten verschiedene Dinge.

Man kann sich das wie bei einem Paket vorstellen. Außen auf dem Versandetikett steht eine Sendungsart: Brief, Paket, Einschreiben. Innen im Paket liegt eine Ware, und die hat ihre eigene Artikelnummer. Beide Angaben beschreiben dasselbe Paket, aber aus verschiedener Perspektive.

Bei der VDV-KA ist es genauso. Auf dem Briefkopf steht, um welche **Art von Nachricht** es sich handelt — das ist `transTransaktionsTyp`. Weiter innen, bei den Daten, die von der Karte stammen, steht, welche **Art von Vorgang auf der Karte** stattgefunden hat — das ist `logTransaktionsTyp`.

Dass das zwei Paar Schuhe sind, zeigt ein belegtes Beispiel: Bei einem Kontrollnachweis steht außen die 59 und innen die 27. Wer nur eine der beiden Zahlen liest und sie in der falschen Tabelle nachschlägt, kommt zu einem Ergebnis, das überzeugend aussieht und falsch ist.

Für Bärstadt sind vier Zahlen interessant. Die **37** heißt: Hier wurde ein Fahrschein über die Aktionsliste ausgegeben — das ist Pias Fall. Die **38** steht für eine Entsperrung, die **39** für eine Rücknahme, und die **27** für eine Kontrolle, also für den Moment, in dem Petra Pranke in der Linie 4 eine Karte prüft.

Hübsch ist das Muster dahinter. Dieselbe Sache gibt es zweimal: einmal am Automaten, einmal über die Aktionsliste. Ausgabe ist 1 oder 37, Entsperrung 21 oder 38, Rücknahme 25 oder 39. Wer die niedrige Zahl sieht, weiß: Das lief direkt am Gerät. Wer die hohe sieht: Das kam aus einer Liste. Für eine Entwertung gibt es kein Gegenstück — eine Fahrt kann man nicht per Liste beauftragen.

**Und jetzt der Teil, der an dieser Stelle einmal anders klang.** Dieser Artikel trug lange die Warnung, alle diese Zahlen stammten aus dem Pflichtenheft eines einzelnen Verbunds und man wisse nicht, ob sie überall gelten. Seit die Spezifikation vorliegt, ist das geklärt: Sie gelten überall. Das Pflichtenheft hatte aus der Standardliste nur ausgewählt, was es brauchte.

Zwei neue Vorsichten sind dafür hinzugekommen, und beide sind unangenehmer als die alte.

Die erste: Für einen bestimmten Fall — eine Rücknahme ohne Eintrag in der Prioritätenliste — ist eigentlich die 40 vorgesehen. Benutzt wird aber die **0**, und die 40 erst ab der nächsten Hauptversion. Wer streng nach Tabelle prüft, erklärt also korrekte Nachrichten für falsch.

Die zweite ist kurioser: Die Zahlen **41 und 42 stehen zweimal in derselben Tabelle**, mit verschiedenen Bedeutungen. Welche gilt, entscheidet die Version. Ein Prüfwerkzeug muss hier wissen, aus welcher Welt die Nachricht kommt — die Zahl allein genügt nicht.

Das ist die Art von Stelle, an der Software still falsch wird. Nicht weil jemand schlecht gearbeitet hätte, sondern weil eine Tabelle über zwanzig Jahre gewachsen ist und zwei Versionen gleichzeitig bedienen muss.

## Quellen

- [Q52](../../QUELLEN.md#q52) – KA HD_BOM-SPEC 1.12.0, Tab. 6-65 (S. 85 bis 87): Codeliste `NmTransaktionsTyp_CODE`, Format `INT1`, Entsprechung `EN 1545: EventTypeCode`; Beschreibung „klassifiziert Arten von Transaktionen, die mit Wertobjekten auf dem Nutzermedium auftreten“; die Werte 0, 1, 2, 20, 21, 25, 27 sowie 37, 38, 39; Fußnote 10 (S. 87) zur Verwendung von 0 statt 40 und Fußnote 9 (S. 86) zur Doppelbelegung von 41 und 42. Exzerpt: [exzerpte/Q52.md](../../exzerpte/Q52.md) · *nicht öffentlich*
- [Q55](../../QUELLEN.md#q55) – KA AktM-SPEC 1.12.0, Kap. 6.2 (S. 67): dem `NmTransaktionsTyp_CODE` werden die Werte für Ausgabe EFS über Aktionsliste (37), Entsperrtransaktion EFS über Aktionsliste (38) und Rückgabetransaktion EFS über Aktionsliste (39) hinzugefügt. Exzerpt: [exzerpte/Q55.md](../../exzerpte/Q55.md) · *nicht öffentlich*
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5, Fußnote 1 (PDF-S. 14): `logTransaktionsTyp` vom Typ `NmTransaktionsTyp_CODE` mit den Werten 37, 38 und 39; Kap. 5.1.2 (PDF-S. 41): `TXEBER` aus Kontrolle mit `IONTransaktionsTyp_CODE` = 059 und `logTransaktionsTyp.code` = 27 · *verbundspezifisch: eTicket RheinMain — Auswahl aus der Standardliste*
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 4.4.4 (PDF-S. 22 f.): „relevante Transaktionstypcodes“ 1, 2, 20, 21, 25, 27, 37, 38 und 39 · *verbundspezifisch: eTicket RheinMain — Auswahl aus der Standardliste*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3: Nennung der KA BOM-SPEC, Inventarnummer 1

<!-- GEN:siehe_auch -->
## Siehe auch

- [TX_BASE](tx-base.md)
- [Ausgabe EFS über Aktionsliste](../aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
