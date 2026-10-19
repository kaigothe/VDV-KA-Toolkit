---
titel: Nullwerte
englisch: encoding of null values
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/tlv.md, lexikon/datenformate/tag-0xdb-fahrgast.md]
quellen: [Q06, Q12]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes:
  - wert: 32
    codeliste: Nullwert-Bytewert
    bedeutung: Leerzeichen 0x20 als Nullwert in PrintableStrings
    quelle: Q06
    fundstelle: Kap. 5.2 (PDF-S. 41)
    status: belegt
    verbundspezifisch: true
  - wert: 255
    codeliste: Nullwert-Bytewert
    bedeutung: 0xFF als "keine Angabe" bei OrtsTyp-Codes
    quelle: Q06
    fundstelle: Kap. 5.2 (PDF-S. 41)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Nullwerte
<!-- /GEN:breadcrumb -->

# Nullwerte

„Bei der Codierung der Bytestrings in den KA-Transaktionsdaten ist zu berücksichtigen, dass die ‚Nullwerte‘ bzw. ‚keine Angabe‘-Werte **nicht immer durch den Wert 0 des einzelnen Bytes** dargestellt werden.“ ([Q06](../../QUELLEN.md#q06), Kap. 5.2)

Zwei Beispiele nennt die Quelle ([Q06](../../QUELLEN.md#q06), Kap. 5.2) · *verbundspezifisch*:

- Der Nullwert für den `PrintableString5` des Attributs `berTarifversion` ist ein **String mit fünf Leerzeichen**; das Leerzeichen wird im Bytestring mit dem Wert **`0x20`** dargestellt.
- Für die **OrtsTyp-Codes**, etwa in `efsStartort_ID` und `efsZielort_ID`, ist in der KA der dezimale Wert **255**, hexadezimal **`0xFF`**, als „keine Angabe“ spezifiziert.

Die Regel gilt also **typabhängig**: Textfelder werden mit Leerzeichen aufgefüllt, Codefelder tragen einen reservierten Höchstwert (abgeleitet).

Ein dritter Fall kommt aus der Praxis hinzu: Beim Tag [0xDB „Fahrgast“](tag-0xdb-fahrgast.md) steht für ein fehlendes Geburtsdatum der **Platzhalter 1970-01-01** und für das Geschlecht fest `0x00` ([Q12](../../QUELLEN.md#q12)) · *Herstellerquelle*. Hier ist der Nullwert also ein scheinbar gültiger Inhalt.

**Für die Auswertung folgt daraus** (abgeleitet): Ein Feld ist nicht leer, weil es Nullbytes enthält, und nicht gefüllt, weil es etwas enthält. Jedes Feld braucht die Prüfung gegen seinen **typspezifischen** Nullwert. Nachlaufende Leerzeichen in einem Namensfeld sind reguläre Auffüllung und kein Fehler.

## Einfach erklärt – Beispiel aus Bärstadt

Ein leeres Feld sieht in der VDV-KA nicht leer aus. Das ist eine der ergiebigsten Fehlerquellen beim Lesen solcher Daten.

Naiv erwartet man: keine Angabe heißt Nullbytes. Hier ist es anders, und zwar je nach Feldtyp verschieden.

**Textfelder werden mit Leerzeichen aufgefüllt.** Ein Feld für fünf Zeichen, in dem nichts steht, enthält fünfmal den Wert `0x20`. Und ein Namensfeld mit Platz für vierzig Zeichen, in dem ein kurzer Name steht, hat hinten lauter Leerzeichen.

Das ist der Grund, warum man in echten Datensätzen immer Ketten von `20 20 20 20` findet. Beim ersten Mal hält man das für Datenschrott. Es ist reguläre Auffüllung.

**Codefelder tragen einen reservierten Höchstwert.** Bei Ortsangaben bedeutet `0xFF` — die 255 — nicht „Ort Nummer 255", sondern „keine Angabe". Wer das übersieht, erfindet einen Ort.

**Und manchmal ist der Nullwert ein echt aussehender Wert.** Fehlt ein Geburtsdatum, steht in der Praxis der 1. Januar 1970 dort. Eine Auswertung, die das für ein Datum nimmt, berechnet ein Alter von über fünfzig Jahren — für eine Auszubildende.

Für Bärstadt heißt das konkret: Als die Bärstädter Verkehrsbetriebe ihre Nachrichten zum ersten Mal auswerteten, waren drei Felder verdächtig. Die Leerzeichen am Ende des Namens, eine 255 bei der Zielhaltestelle, und Pias Mitschüler, die alle 1970 geboren schienen.

Keines davon war ein Fehler. Alle drei waren korrekt kodierte Nullwerte.

Die Lehre für ein Auswertungswerkzeug: Zu jedem Feld gehört nicht nur sein Datentyp, sondern auch sein Nullwert. Ohne diese zweite Angabe lässt sich „nicht angegeben" nicht von „angegeben" unterscheiden.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 5.2 „Kodierung von Nullwerten in Bytestrings in KA-Transaktionsdaten“ (PDF-S. 41): Nullwerte werden nicht immer durch den Wert 0 dargestellt; `berTarifversion` als `PrintableString5` mit fünf Leerzeichen, Leerzeichen als `0x20`; OrtsTyp-Codes in `efsStartort_ID` und `efsZielort_ID` mit dezimal 255 bzw. `0xFF` als „keine Angabe“ · *verbundspezifisch: eTicket RheinMain*
- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings (Platzhalter 1970-01-01 für ein fehlendes Geburtsdatum, `0x00` für das Geschlecht) · *Herstellerquelle*

<!-- GEN:siehe_auch -->
## Siehe auch

- [TLV-Kodierung](tlv.md) (TLV)
- [Tag 0xDB Fahrgast](tag-0xdb-fahrgast.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
