---
titel: Ausgabe EFS über Aktionsliste
englisch: issue of an electronic ticket via action list
parent: lexikon/aktionsmanagement.md
siehe_auch: []
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: [O1, O2]
stand: 2026-10-19
codes:
  - wert: 37
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: TXABER – Ausgabe EFS über Aktionsliste
    quelle: Q06
    fundstelle: Kap. 2.1.5, Fußnote 1 (PDF-S. 13)
    status: belegt
    verbundspezifisch: true
  - wert: 38
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: TXSNAWB – Entsperrtransaktion EFS über Aktionsliste
    quelle: Q06
    fundstelle: Kap. 2.1.5, Fußnote 1 (PDF-S. 13)
    status: belegt
    verbundspezifisch: true
  - wert: 39
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Rückgabetransaktion EFS über Aktionsliste
    quelle: Q06
    fundstelle: Kap. 2.1.5, Fußnote 1 (PDF-S. 13)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Ausgabe EFS über Aktionsliste
<!-- /GEN:breadcrumb -->

# Ausgabe EFS über Aktionsliste

Die Ausgabe eines elektronischen Fahrscheins ist einer der vier Aktionstypen, die über eine Aktionsliste beauftragt werden können ([Q02](../../QUELLEN.md#q02), S. 19). Gegenstand des Aktionsmanagements sind die KVP-Aktionen Berechtigung-Ausgabe, Berechtigung-Rücknahme und Berechtigung-Entsperrung ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5).

Das Terminalmanagementsystem erhält die Aktionsliste als `TXAML` und liefert die Transaktionsnachweise `TXABER`, `TXRBER` und `TXSNAWB` zurück. Diese Nachweise sind über **spezifische KA-Transaktionstyp-Codes** als Ergebnis der Ausführung eines Aktionslisteneintrags gekennzeichnet ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5).

Im Feld `logTransaktionsTyp` vom Typ `NmTransaktionsTyp_CODE` gilt ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1):

| Wert | Bedeutung |
|---:|---|
| **37** | `TXABER` – Ausgabe EFS über Aktionsliste |
| **38** | `TXSNAWB` – Entsperrtransaktion EFS über Aktionsliste |
| **39** | Rückgabetransaktion EFS über Aktionsliste |

Diese Zuordnung ist eine Festlegung im eTicket RheinMain. Ob sie KA-weit gilt, ist nicht belegt (zu prüfen, O1).

Zum **Rollencode** im Transaktionskopf: In der Schnittstellenversion KA 1.1.07 wurde für solche Transaktionen alternativ auch der Rollencode 31 (ALISE) akzeptiert. Ab KA 1.3.0 ist 31 für einen aus dem PV-System ausgelagerten, eigenständigen zentralen ALISE-Server reserviert; ist ALISE in das PV-System integriert, ist stattdessen die Rolle 3 zu verwenden. In der TMS-Schnittstellenversion KA 1.3.0 ist für Transaktionen aus Aktionsausführungen zwingend der Rollencode 3 zu verwenden ([Q06](../../QUELLEN.md#q06), Fußnote 7, PDF-S. 39).

Normquelle ist die nicht öffentliche KA AktM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 41). Welchen Wert das Feld `amAuftragsTyp` für diesen Fall trägt, ist nicht belegt (zu prüfen, O2).

## Einfach erklärt – Beispiel aus Bärstadt

Pias ABO Azubi ist genehmigt. Jetzt soll es auf die Karte. Der Weg dorthin besteht aus zwei Schritten, die man gut auseinanderhalten sollte: dem **Auftrag** und dem **Nachweis**.

**Der Auftrag.** Die Bärstädter Verkehrsbetriebe tragen beim Bären-Verkehrsbund eine Aktion ein: „Schreibe das Produkt 2001 auf die Applikationsinstanz 90000042.“ Dieser Eintrag landet in der Aktionsliste. Dort steht er zusammen mit allen anderen offenen Aufträgen und wird einmal täglich neu zusammengestellt. Die BVB holt die Liste ab und verteilt sie an ihre Terminals.

**Die Ausführung.** Pia hält ihre BärenKarte an das Lesegerät T-4712 am Hauptbahnhof. Das Gerät vergleicht die Kartennummer mit seiner Liste, findet den Auftrag und schreibt die Berechtigung 400815 auf den Chip. Dabei bildet das SAM im Gerät die Sicherungscodes, mit denen sich später nachweisen lässt, dass die Berechtigung echt ist.

**Der Nachweis.** Nun entsteht etwas Neues, das es vorher nicht gab: eine Meldung darüber, dass der Auftrag tatsächlich ausgeführt wurde. Diese Meldung heißt `TXABER` und trägt die Kennzahl **37**. Die 37 sagt genau das: „Hier wurde ein Fahrschein über die Aktionsliste ausgegeben.“

Das ist der Grund für die eigenen Kennzahlen. Ein Fahrschein kann auch anders auf eine Karte kommen — am Automaten, im Kundencenter, direkt beim Verkauf. Für die Abrechnung und für Rückfragen muss man unterscheiden können, auf welchem Weg er dort gelandet ist. Die 37 markiert den Weg über die Aktionsliste.

Ihre Geschwister sind die **38** für eine Entsperrung und die **39** für eine Rücknahme. Wenn Pia später ihre Ausbildung abbricht und das Abo von der Karte genommen wird, entsteht beim nächsten Terminalkontakt eine Meldung mit der 39.

Ein Wort der Vorsicht: Diese drei Zahlen sind so im Pflichtenheft des eTicket RheinMain festgelegt. Ob im Bärenland — oder in einem anderen echten Verbund — dieselben Zahlen gelten, muss man in der dort gültigen Spezifikation nachsehen. Eine Zahl aus einem fremden Verbund ungeprüft zu übernehmen, ist einer der häufigsten Fehler beim Lesen solcher Nachrichten.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19 („Aktionsliste“, Aufzählung „Ausgabe eines elektronischen Fahrscheins“)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (KVP-Aktionen über Aktionsliste; TXAML hinein, TXABER/TXRBER/TXSNAWB heraus; Kennzeichnung über spezifische KA-Transaktionstyp-Codes), Kap. 2.1.5 Fußnote 1, PDF-S. 13 (Codes 37/38/39), Fußnote 7, PDF-S. 39 (Rollencode 31 bzw. 3) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA AktM-SPEC, Inventarnummer 41 „Aktionsmanagement für die Berechtigungsart EFS“)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
