---
titel: TXABER
abkuerzung: TXABER
englisch: issue attestation
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md, lexikon/transaktionen/logtransaktionstyp.md]
quellen: [Q05, Q06, Q25, Q52]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › TXABER
<!-- /GEN:breadcrumb -->

# TXABER

`TXABER` ist der **Ausgabenachweis** einer Berechtigung. Die Struktur ist der nicht öffentlichen KA SST-SPEC zu entnehmen ([Q06](../../QUELLEN.md#q06), Kap. 4.3.2, 4.4.1; [Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 4).

Bemerkenswert ist, dass `TXABER` in **zwei verschiedenen Zusammenhängen** auftritt ([Q06](../../QUELLEN.md#q06)):

- als Transaktionsnachweis aus einer **Aktionsausführung** (Kap. 4.3.2) — hier ist zusätzlich die KA AktM-SPEC zu beachten,
- als Ausgabenachweis aus dem **Verkauf** (Kap. 4.4.1), dort gemeinsam mit `TXAA`.

Unterschieden werden die beiden Fälle über den [`logTransaktionsTyp`](logtransaktionstyp.md): Der Wert 37 kennzeichnet die Ausgabe EFS **über Aktionsliste** ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1). Der Wert stammt aus der Standardcodeliste und gilt KA-weit ([Q52](../../QUELLEN.md#q52), Tab. 6-65, S. 87). Eine Ausgabe im Verkauf trägt ihn folglich nicht (abgeleitet).

Für den **fachlichen Teil** verweist [Q06](../../QUELLEN.md#q06) auf das Schwesterdokument PH 05-A1 „RMV-EFS“ ([Q05](../../QUELLEN.md#q05)). Insbesondere ist zu beachten, dass das `TXABER` **immer** die Datenstruktur `berechtigungTarifbereichZusatz` gemäß den Vorgaben des PH 05-A1 enthält ([Q06](../../QUELLEN.md#q06), Kap. 4.3.2) · *verbundspezifisch*.

Zum Datenschutz: Fahrtnummer und Linienvariante dürfen in einem `TXABER` **nicht** überschrieben werden — die entsprechende Vorgabe gilt ausschließlich für Kontrollnachweise ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2).

Ab KA 1.3.0 kommt für Multiberechtigungen `TXAMBER` hinzu ([Q06](../../QUELLEN.md#q06), Kap. 4.3.2, 4.4.1).

## Einfach erklärt – Beispiel aus Bärstadt

`TXABER` ist der Beleg „Berechtigung ausgegeben“. In Pias Fall: Das Lesegerät am Hauptbahnhof hat das ABO Azubi geschrieben, und `TXABER` meldet das zurück.

Interessant ist, dass derselbe Belegtyp für zwei verschiedene Wege verwendet wird.

**Weg eins** ist Pias Weg: Der Auftrag stand auf der Aktionsliste, ein Terminal hat ihn beim Kartenkontakt abgearbeitet.

**Weg zwei** ist der Verkauf: Olli Tapsig steht am Automaten, kauft ein Ticket und bekommt es sofort auf die Karte geschrieben. Keine Aktionsliste, kein Warten — die Ausgabe passiert direkt beim Kauf.

Beide Male entsteht ein `TXABER`. Für die Abrechnung sind es aber ganz verschiedene Vorgänge: Beim einen hat die BVB vorher einen Auftrag erteilt, der irgendwo verbucht ist. Beim anderen hat ein Kunde gerade Geld bezahlt.

Unterscheiden kann man sie an der Kennzahl im Inneren der Nachricht. Die **37** sagt: Das kam über die Aktionsliste. Fehlt sie, war es ein Verkauf.

Wer eine solche Nachricht auswertet, sollte diese Zahl also nicht als Nebensache behandeln. Sie entscheidet darüber, in welchen Prozess der Beleg gehört.

Ein zweites praktisches Detail: Im eTicket RheinMain muss jedes `TXABER` eine bestimmte Zusatzangabe zum Tarifbereich mitbringen — immer, ohne Ausnahme. Das ist eine Festlegung dieses Verbunds und keine Regel des Standards. Eine Auswertung, die solche Pflichtfelder prüfen will, braucht also die Regeln des jeweiligen Verbunds und nicht nur die allgemeine Spezifikation.

Und eine Besonderheit beim Datenschutz: In Kontrollnachweisen werden Fahrt- und Liniennummer geleert, damit keine Bewegungsprofile entstehen. Im `TXABER` darf das ausdrücklich **nicht** passieren.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.3.2 (`TXABER` als Transaktionsnachweis aus Aktionsausführung, Struktur aus `[KA_SPEC_SST]`, zusätzlich `[KA_SPEC_AktM]`, Pflicht zur Datenstruktur `berechtigungTarifbereichZusatz`, Verweis auf PH05-A1, Ergänzung `TXAMBER` ab KA 1.3.0), Kap. 4.4.1 (`TXABER` und `TXAA` als Ausgabenachweise aus Verkauf), Kap. 2.1.5 Fußnote 1 (`logTransaktionsTyp` 37), Kap. 5.1.2 (Fahrtnummer und Linienvariante dürfen im `TXABER` nicht überschrieben werden) · *verbundspezifisch: eTicket RheinMain*
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1 „RMV-EFS“ als Quelle des fachlichen Teils
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SST-SPEC, Inventarnummer 4)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Ausgabe EFS über Aktionsliste](../aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md)
- [logTransaktionsTyp](logtransaktionstyp.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
