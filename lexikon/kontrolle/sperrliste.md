---
titel: Sperrliste
englisch: Hotlist
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/sperrlisteneintrag.md, lexikon/rollen/kose.md]
quellen: [Q02, Q06, Q33]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Sperrliste
<!-- /GEN:breadcrumb -->

# Sperrliste

Eine Sperrliste — der Name ist aus der EN 15xxx übernommen — „besteht aus einer Menge von Sperrlisteneinträgen für ein bestimmtes Objekt (Berechtigung, Applikation, SAM, Schlüssel, Organisation)“. Sie dient nach entsprechender Verteilung in den Systemen und Terminals „dem Auffinden einer unzulässigen Verwendung“ ([Q02](../../QUELLEN.md#q02), S. 89).

Es gibt also **nicht eine** Sperrliste, sondern eine **je Objektart**. Entsprechend sind die Nachrichten aufgeteilt ([Q06](../../QUELLEN.md#q06), Kap. 4.1, 4.2.1) · *verbundspezifisch*:

| Bis KA 1.1.07 | Ab KA 1.3.0 | Gegenstand |
|---|---|---|
| `TXSLNM` | `TXSLNMRESP` | nutzermediumbezogen — Applikationen und Berechtigungen |
| `TXSLOS` | `TXSLORGRESP`, `TXSLSAMRESP` | Organisationen und SAMs |
| `TXSLK` | `TXSLKASYMRESP`, `TXSLKSYMRESP` | Schlüssel, getrennt nach asymmetrisch und symmetrisch |

Die älteren Strukturen stammen aus der KA SST-SPEC 1.1.07, die `*RESP`-Varianten aus der Fassung 1.3.0 ([Q06](../../QUELLEN.md#q06), Kap. 4.2.1). Die Aufteilung von `TXSLOS` und `TXSLK` in je zwei Antworten ab 1.3.0 ist belegt; die Auflösung der Kürzel `NM`, `OS` und `K` ergibt sich aus den Gegenständen (abgeleitet).

**Verteilung:** Im eTicket RheinMain werden Sperr- und Aktionslisten **nur einmal täglich** erstellt und bereitgestellt; entsprechend ist der Abruf auf einmal täglich festgelegt ([Q06](../../QUELLEN.md#q06), Kap. 3.2) · *verbundspezifisch*. Eine Sperrung wirkt dort also mit bis zu einem Tag Verzögerung (abgeleitet).

Für das Deutschlandticket gilt inzwischen Strengeres: „Die Verwendung einer gemeinsamen bundesweiten, für alle Marktteilnehmer zugänglichen Sperrliste ist **verpflichtend**“, und das VDV-Präsidium empfiehlt den Aufbau einer **neartime- bzw. Online-Sperrliste** ([Q33](../../QUELLEN.md#q33)).

## Einfach erklärt – Beispiel aus Bärstadt

„Die Sperrliste" gibt es nicht. Es sind mehrere, und das hat einen einleuchtenden Grund.

Gesperrt werden können fünf sehr verschiedene Dinge: Berechtigungen, Karten, Sicherheitsbausteine, Schlüssel und ganze Organisationen. Diese Listen haben völlig unterschiedliche Größen und Änderungsraten. Die Liste gesperrter Karten ist lang und ändert sich täglich; die Liste gesperrter Organisationen ist kurz und ändert sich fast nie.

Beides in eine Datei zu packen wäre Verschwendung. Also gibt es getrennte Nachrichten — und man erkennt an den Namen, worum es geht: `TXSLNM` für Nutzermedien, `TXSLK` für Schlüssel, `TXSLOS` für Organisationen und Sicherheitsbausteine.

Interessant ist die Entwicklung. Ab Version 1.3.0 wurden zwei dieser Listen aufgespalten: Organisationen und SAMs bekamen je eine eigene, und bei den Schlüsseln wurde zwischen symmetrisch und asymmetrisch getrennt. Aus drei Listen wurden fünf. Das ist ein typisches Muster — mit der Zeit wird feiner unterteilt, weil feiner verteilt werden kann.

Nun der Punkt, an dem die Praxis wehtut. Im eTicket RheinMain werden die Listen **einmal am Tag** erstellt. Sperrt Bodo Bärlauch Pias Karte am Dienstagnachmittag, kennen die Kontrollgeräte diese Sperre am Mittwoch. Dazwischen könnte jemand mit der gefundenen Karte fahren.

Genau darüber ist man inzwischen hinaus. Beim Deutschlandticket ist eine **bundesweite** Sperrliste Pflicht, und es gibt eine Empfehlung, sie auf nahezu Echtzeit umzustellen.

Das ist der eigentliche Grund: Ein Deutschlandticket ist eine Dauerberechtigung. Wird es gekündigt oder platzt die Abbuchung, darf die Sperre nicht einen Tag warten.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 89 („Sperrliste / Hotlist“: Name aus der EN übernommen, Menge von Sperrlisteneinträgen je Objektart, Verteilung in Systeme und Terminals, physische gegenüber logischer Sperre)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 3.2 (Sperr- und Aktionslisten nur einmal täglich erstellt und bereitgestellt), Kap. 3.3 (Sperrlisten herunterladen), Kap. 4.1 (Nachrichtentypen im Manifest: `TXSLNM`/`TXSLNMRESP`, `TXSLOS`/`TXSLORGRESP`/`TXSLSAMRESP`, `TXSLK`/`TXSLKASYMRESP`/`TXSLKSYMRESP`), Kap. 4.2.1 (ältere Strukturen aus KA_SPEC_SST_1107, `*RESP`-Varianten aus KA_SPEC_SST_1300) · *verbundspezifisch: eTicket RheinMain*
- [Q33](../../QUELLEN.md#q33) – KCD NRW, Ergebnisdokument der Arbeitsgruppe Kontrolle, V1.3 (Pflicht zur gemeinsamen bundesweiten Sperrliste; Beschlussvorschlag zum Aufbau einer neartime- bzw. Online-Sperrliste für das Deutschlandticket; Kap. 7.2 zum Sperrmanagement) · *produktbezogen auf das Deutschlandticket*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
