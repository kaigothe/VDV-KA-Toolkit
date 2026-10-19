---
titel: TXRBER
abkuerzung: TXRBER
englisch: termination attestation
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/aktionsmanagement/ruecknahme-efs-ueber-aktionsliste.md]
quellen: [Q06, Q25]
status: belegt
offene_fragen: [O1]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › TXRBER
<!-- /GEN:breadcrumb -->

# TXRBER

`TXRBER` ist der Nachweis über die **Rücknahme** einer Berechtigung. Die Struktur ist der nicht öffentlichen KA SST-SPEC zu entnehmen; zusätzlich ist die KA AktM-SPEC zu beachten ([Q06](../../QUELLEN.md#q06), Kap. 4.3.2; [Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummern 4 und 41).

`TXRBER` gehört zu den drei Transaktionsnachweisen, die ein Terminalmanagementsystem aus der Ausführung von Aktionslisteneinträgen zurückliefert — neben [`TXABER`](txaber.md) und [`TXSNAWB`](txsnawb.md). Alle drei sind über spezifische KA-Transaktionstyp-Codes als Ergebnis der Ausführung eines Aktionslisteneintrags gekennzeichnet ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5).

Für die [Rücknahme über Aktionsliste](../aktionsmanagement/ruecknahme-efs-ueber-aktionsliste.md) nennt [Q06](../../QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1, den `logTransaktionsTyp`-Wert **39** („Rückgabetransaktion EFS über Aktionsliste“). Anders als bei den Werten 37 und 38 ist dort **kein Nachrichtenname** angegeben; die Zuordnung zu `TXRBER` ergibt sich aus der Aufzählung der zurückgelieferten Nachweise in derselben Kapitelstelle (abgeleitet). Ob die Codezuordnung KA-weit gilt, ist nicht belegt (zu prüfen, O1) · *verbundspezifisch*.

Ab KA 1.3.0 kommt für Multiberechtigungen `TXRMBER` hinzu ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, 4.3.2).

Anders als beim `TXABER` nennen die öffentlichen Quellen für den fachlichen Teil des `TXRBER` keine gesonderten Pflichtfelder.

## Einfach erklärt – Beispiel aus Bärstadt

Wenn Pia Brummbär ihre Ausbildung abbricht und das ABO Azubi von der Karte genommen wird, entsteht dafür ein eigener Beleg: `TXRBER`.

Man könnte fragen, warum es dafür eine separate Nachrichtenart braucht. Könnte man nicht einfach einen Ausgabenachweis mit umgekehrtem Vorzeichen schicken?

Die Antwort liegt in der Abrechnung. Eine Ausgabe und eine Rücknahme sind nicht einfach Plus und Minus. Bei der Rücknahme stellen sich eigene Fragen: Wie lange war die Berechtigung in Gebrauch? Steht dem Kunden Geld zurück? Wird das Produkt dem Produktverantwortlichen wieder zugeschrieben? Ein eigener Belegtyp erlaubt es, dafür eigene Felder vorzusehen und eigene Prüfungen zu machen.

Der Weg ist derselbe wie bei der Ausgabe. Die Bärstädter Verkehrsbetriebe beauftragen die Rücknahme, der Auftrag landet in der Aktionsliste, ein Terminal arbeitet ihn beim nächsten Kartenkontakt ab — und meldet mit `TXRBER` zurück, dass es geschehen ist.

Dieser letzte Schritt ist der entscheidende. Solange Pia ihre Karte nicht an ein Gerät hält, ist die Berechtigung noch auf dem Chip, auch wenn im Hintergrundsystem längst alles vorbereitet ist. Für die Kontrolle in der Linie 4 ist der Auftrag unsichtbar. Erst der Nachweis belegt, dass die Karte wirklich bereinigt wurde.

Bei der Zuordnung der Kennzahl 39 zu `TXRBER` ist dieses Lexikon vorsichtig. Das Pflichtenheft nennt die 39 für die Rückgabetransaktion, setzt aber — anders als bei der 37 und der 38 — keinen Nachrichtennamen dazu. Dass es `TXRBER` sein muss, ergibt sich aus dem Zusammenhang und ist damit erschlossen, nicht abgelesen. Für ein Lexikon ist das ein Unterschied, den man kenntlich macht.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (`TXRBER` als einer der drei Transaktionsnachweise aus Aktionsausführung, Kennzeichnung über spezifische KA-Transaktionstyp-Codes; Fußnote 1: Rückgabetransaktion EFS über Aktionsliste = 39; `TXRMBER` ab KA 1.3.0), Kap. 4.3.2 (Struktur aus `[KA_SPEC_SST]`, zusätzlich `[KA_SPEC_AktM]`) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SST-SPEC, Inventarnummer 4; KA AktM-SPEC, Inventarnummer 41)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
