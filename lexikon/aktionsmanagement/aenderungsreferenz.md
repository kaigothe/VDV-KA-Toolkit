---
titel: Änderungsreferenz
englisch: change reference
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/auftragstyp.md]
quellen: [Q02, Q11, Q25]
status: zu prüfen
offene_fragen: [O13]
stand: 2026-10-19
codes:
  - wert: 0
    bedeutung: vermutlich keine Vorgänger-Berechtigung, also Neuausgabe
    quelle: Q11
    fundstelle: Feld amAenderungsreferenz_ID im ausgewerteten Datensatz
    status: abgeleitet
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Änderungsreferenz
<!-- /GEN:breadcrumb -->

# Änderungsreferenz

Das Feld `amAenderungsreferenz_ID` in einem Aktionslisteneintrag verweist auf eine Berechtigung, die durch die beauftragte Aktion ersetzt oder geändert wird. In der ausgewerteten `txalisber`-Nachricht trägt es den Wert **0** in beiden Teilen, also Nummer und Organisation ([Q11](../../QUELLEN.md#q11)).

**Die Bedeutung ist nicht belegt** (zu prüfen, O13). Die Codeliste und die Feldsemantik stehen in der nicht öffentlichen KA AktM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 41). Das Glossar [Q02](../../QUELLEN.md#q02) enthält keinen entsprechenden Eintrag; geprüft am Inhaltsverzeichnis, S. 2–13.

Aus Feldname und Wert liegt folgende Lesart nahe (abgeleitet): Eine Änderungsreferenz von 0 bedeutet, dass es keine Vorgänger-Berechtigung gibt. Die Aktion ist dann eine **Neuausgabe** und keine Änderung einer bestehenden Berechtigung.

Diese Lesart wird von zwei weiteren Feldern derselben Nachricht gestützt: Die `berSynchronNummer` ist 1, also der erste Stand der Berechtigung, und der `logTransaktionsTyp` ist 37, also Ausgabe EFS über Aktionsliste. Drei Felder, die unabhängig voneinander auf eine Neuausgabe deuten, bilden eine belastbare Indizienkette — aber keinen Beleg.

Ungeklärt bleibt, welchen Wert das Feld bei einer **tatsächlichen** Änderung trägt und ob es dann die Berechtigungsnummer samt Organisation des Vorgängers aufnimmt (zu prüfen, O13).

## Einfach erklärt – Beispiel aus Bärstadt

In Pias Auftrag steht an einer Stelle eine Null — genauer gesagt zwei Nullen, eine für eine Nummer und eine für eine Organisation. Das Feld heißt Änderungsreferenz.

Der Name legt die Bedeutung nahe: Es ist ein Verweis auf etwas Früheres. Wenn eine Berechtigung eine andere ersetzt, kann man hier eintragen, welche das war. Eine Null heißt dann: Es gibt nichts Früheres. Pias ABO Azubi wird neu ausgegeben und tritt nicht an die Stelle eines anderen Abos.

Warum ist das überhaupt nützlich? Weil Berechtigungen im Lauf der Zeit ersetzt werden. Pia verliert ihre Karte und bekommt eine Ersatzkarte — die neue Berechtigung darauf ist dann die Nachfolgerin der alten. Ohne einen Verweis wüsste niemand, dass die beiden zusammengehören. Mit ihm kann man die Kette nachvollziehen: Diese Berechtigung ist aus jener entstanden.

Nun das Wichtige: Diese Erklärung ist eine **Deutung**, keine belegte Tatsache. Sie stammt aus dem Feldnamen und daraus, dass zwei andere Felder in dieselbe Richtung zeigen — der Versionszähler steht auf 1, und die Transaktion ist als Ausgabe gekennzeichnet. Drei Hinweise, die zusammenpassen, machen eine Deutung wahrscheinlich. Sie machen sie nicht wahr.

Besonders offen ist die Gegenprobe. Niemand hier hat eine Nachricht gesehen, in der das Feld **nicht** null ist. Wie eine echte Änderungsreferenz aussieht — ob dort die Berechtigungsnummer der Vorgängerin steht, ob zusätzlich deren Organisation, in welchem Format —, lässt sich aus dem einen vorliegenden Beispiel nicht sagen.

Deshalb steht dieser Artikel auf „zu prüfen“. Für ein Auswertungswerkzeug heißt das: Eine Null darf als „Neuausgabe“ angezeigt werden, aber mit dem Hinweis, dass diese Deutung erschlossen ist.

## Quellen

- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht, Feld `amAenderungsreferenz_ID` mit dem Wert 0/0, dazu `berSynchronNummer` 1 und `logTransaktionsTyp` 37. **Nicht öffentliche Unterlage**; übernommen sind nur Feldnamen und Werte.
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA AktM-SPEC, Inventarnummer 41, als Normquelle der Feldsemantik)
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE: **kein** Eintrag zur Änderungsreferenz (geprüft am Inhaltsverzeichnis, S. 2–13)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
