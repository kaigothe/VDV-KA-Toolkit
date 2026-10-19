---
titel: Tag 0xDB Fahrgast
englisch: tag 0xDB passenger
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/kuerzungsregel-fuer-namen.md, lexikon/medien/personengebunden.md]
quellen: [Q12, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes:
  - wert: 0
    bedeutung: efsFahrgastGeschlecht — unspecified
    quelle: Q12
    fundstelle: Feldliste und FAQ
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Tag 0xDB Fahrgast
<!-- /GEN:breadcrumb -->

# Tag 0xDB Fahrgast

Unter dem TLV-Tag **`0xDB` „Fahrgast“** liegen im statischen produktspezifischen Teil einer Berechtigung die personenbezogenen Daten. Normquelle ist die nicht öffentliche **Anlage TLV EFS**, Abschnitt 2.2, dort S. 9 der Fassung V190 ([Q12](../../QUELLEN.md#q12); [Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 2).

Drei Felder sind belegt ([Q12](../../QUELLEN.md#q12)):

| Feld | Belegung in der Praxis |
|---|---|
| `efsFahrgastGeschlecht` | beim Deutschlandticket fest `0x00` = unspecified, „gemäß Vorgabe VDV-ETS“ |
| `efsFahrgastGeburtsdatum` | das Geburtsdatum, falls vorhanden — andernfalls **1970-01-01** |
| `efsFahrgastName` | der nach Typ 1 [maskierte und gekürzte Name](kuerzungsregel-fuer-namen.md), andernfalls leer |

Zwei Beobachtungen sind für die Auswertung wichtig (abgeleitet):

**Ein Standardwert ist kein Wert.** Das Geburtsdatum 1970-01-01 ist in dieser Praxis der Platzhalter für „nicht angegeben“. Wer es als echtes Datum verarbeitet, erzeugt einen Jahrgang 1970, den es nie gab. Dasselbe gilt für `0x00` beim Geschlecht.

**Das Tag entscheidet nicht über Personenbezug.** Ein `0xDB` kann vorhanden und inhaltlich leer sein — bei einem übertragbaren Ticket ist der Name leer. Die Anwesenheit des Tags belegt also nicht, dass die Berechtigung [personengebunden](../medien/personengebunden.md) ist.

Dass diese Daten **auf dem Medium** liegen, ist der Grund, weshalb die Kontrolle die Berechtigungsprüfung ohne Rückfrage beim Hintergrundsystem durchführen kann ([Q12](../../QUELLEN.md#q12)) (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Unter dem Kennzeichen `0xDB` steht auf Pias BärenKarte, wer sie ist.

Genauer: drei Angaben — Name, Geburtsdatum, Geschlecht. Mehr nicht. Keine Adresse, keine Bankverbindung, keine Vertragsnummer. Das ist bemerkenswert sparsam und hat einen Zweck: Petra Pranke braucht bei der Kontrolle genau diese drei Dinge und nichts weiter.

Nun zu zwei Fallen, die beim Auswerten solcher Daten regelmäßig zuschlagen.

**Die erste Falle ist das Datum 1. Januar 1970.** Wer Software kennt, erkennt es sofort: Das ist der Nullpunkt der Unix-Zeitrechnung, der klassische Platzhalter für „kein Wert". In der Praxis wird genau dieser Wert eingetragen, wenn kein Geburtsdatum vorliegt.

Für eine Auswertung ist das heikel. Zählt man naiv die Jahrgänge aus, entsteht ein Riesenberg bei 1970. Fragt man „ist der Fahrgast über 18?", antwortet das System bei jedem Platzhalter mit „ja". Dieselbe Falle gilt für das Geschlecht, das in der Praxis durchgehend auf „unspecified" steht.

**Die zweite Falle ist die Anwesenheit des Tags selbst.** Man könnte denken: Wenn `0xDB` da ist, ist das Ticket personengebunden. Stimmt nicht. Das Feld kann vorhanden und der Name darin leer sein — so sieht ein übertragbares Ticket aus. Die Übertragbarkeit steht im Produkt, nicht im Vorhandensein eines Tags.

Und ein Satz zum praktischen Nutzen: Weil diese drei Angaben **auf der Karte** liegen und nicht im Rechenzentrum, kann Petra auch in der Waldsiedlung kontrollieren, wo ihr Gerät keinen Empfang hat. Sie liest den Namen vom Chip und vergleicht ihn mit Pias Ausweis — ganz ohne Netz.

## Quellen

- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings: Tag 0xDB „Fahrgast“ nach Anlage TLV EFS V190, S. 9, Abschn. 2.2; `efsFahrgastGeschlecht` fest 0x00 „unspecified“ gemäß Vorgabe VDV-ETS; `efsFahrgastGeburtsdatum` mit Geburtsdatum, sonst 1970-01-01; `efsFahrgastName` als Typ-1-anonymisierter Name, sonst leer; Verweis auf KA HD_BOM-Spec_V190 Abschn. 6.7.2 · *Herstellerquelle, belegt Marktpraxis*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (Anlage TLV EFS, Inventarnummer 2, als Normquelle der Tags)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
