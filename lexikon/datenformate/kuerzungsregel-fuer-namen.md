---
titel: Kürzungsregel für Namen
englisch: name truncation rule
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/tag-0xdb-fahrgast.md, lexikon/datenformate/bom.md]
quellen: [Q12, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Kürzungsregel für Namen
<!-- /GEN:breadcrumb -->

# Kürzungsregel für Namen

Der Name eines Fahrgasts wird nicht im Klartext auf das Medium geschrieben, sondern **maskiert und gekürzt**. Die Regel steht im Basisobjektmodell, Abschnitt **6.7.2 „Kürzungsregel für Namen und Vornamen“** ([Q12](../../QUELLEN.md#q12); nicht öffentlich, [Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 1).

Es gibt **zwei Typen** der Anonymisierung. [Q12](../../QUELLEN.md#q12) nennt **Typ 1 „Maskierter und gekürzter Name“** und erwähnt einen **Typ 2**, der dort nicht unterstützt wird; wie Typ 2 arbeitet, ist nicht belegt.

Beispiel für Typ 1 ([Q12](../../QUELLEN.md#q12)) · *Herstellerquelle*:

| | |
|---|---|
| Vorname | `Eva-Maria Alexandra Tanja Manuela` |
| Nachname | `Gräfin von Konstantinopolus` |
| Ergebnis | `E1a*@*K0s` |
| Anzeige je nach Scanner | `E_a K_________s` |

Daran ist ablesbar (abgeleitet): Erhalten bleiben jeweils **erster und letzter Buchstabe**, das Dazwischenliegende wird maskiert; Vor- und Nachname werden durch ein Trennmuster verbunden. Die genaue Kodierung der Füllzeichen ist ohne Abschnitt 6.7.2 nicht zu rekonstruieren.

**Der Zweck ist eine Abwägung** (abgeleitet): Der Name muss bei der Kontrolle mit einem Ausweis **vergleichbar** bleiben, soll aber bei einem verlorenen Medium oder einem abgefangenen Barcode möglichst wenig verraten. Eine Maskierung, die Anfang und Ende erhält, leistet beides — ein Prüfer erkennt die Übereinstimmung, ein Finder nicht die Person.

Im Feld `efsFahrgastName` steht entsprechend der Typ-1-Name, bei übertragbaren Berechtigungen bleibt es leer ([Q12](../../QUELLEN.md#q12)).

## Einfach erklärt – Beispiel aus Bärstadt

Auf Pias BärenKarte steht ihr Name — aber nicht so, wie sie ihn schreibt.

Das Verfahren lässt sich am veröffentlichten Beispiel eines Herstellers nachvollziehen. Aus dem Vornamen „Eva-Maria Alexandra Tanja Manuela" und dem Nachnamen „Gräfin von Konstantinopolus" wird:

`E1a*@*K0s`

Oder, wie es ein Kontrollgerät anzeigt: `E_a K_________s`

Man erkennt das Prinzip. Der erste und der letzte Buchstabe bleiben stehen, alles dazwischen verschwindet hinter Platzhaltern. Aus Eva-Maria wird E…a, aus Konstantinopolus wird K…s.

Warum dieser Aufwand? Weil hier zwei Interessen gegeneinander stehen.

**Petra Pranke braucht den Namen.** Pias Abo ist personengebunden; ohne einen Vergleich mit dem Ausweis wäre die Bindung wertlos. Ein völlig anonymes Feld würde die Kontrolle unmöglich machen.

**Pia braucht Schutz.** Verliert sie die Karte, soll der Finder nicht ihren vollen Namen erfahren. Und ein Barcode auf Papier kann von jedem gescannt werden, der ihn in die Hand bekommt.

Die Maskierung löst das elegant. Petra sieht `E_a K_________s`, schaut auf den Ausweis mit „Eva-Maria … Konstantinopolus" und kann die Übereinstimmung bestätigen. Ein Finder sieht zwei Buchstabenpaare und eine Länge — daraus eine Person zu bestimmen, ist praktisch unmöglich.

Was man sich merken sollte: Das Feld ist **kein Name**, sondern eine Prüfhilfe. Es taugt nicht dazu, einen Kunden zu identifizieren, eine Datenbank zu durchsuchen oder einen Brief zu adressieren. Wer es dafür verwendet, hat die Regel missverstanden.

Dass es zwei Typen der Maskierung gibt und der zweite hier unbekannt bleibt, ist ehrlich gesagt eine Lücke.

## Quellen

- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings, FAQ „Why is the efsFahrgastname encoded“: Verweis auf KA HD_BOM-Spec_V190, Abschn. 6.7.2 „Kürzungsregel für Namen und Vornamen“; zwei Typen der Anonymisierung, Typ 1 „Maskierter und gekürzter Name“ verwendet, Typ 2 nicht unterstützt; das wörtlich wiedergegebene Beispiel samt Anzeigeform · *Herstellerquelle, belegt Marktpraxis*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA BOM-SPEC, Inventarnummer 1, als Normquelle des Abschnitts 6.7.2)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
