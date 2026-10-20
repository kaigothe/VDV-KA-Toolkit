---
titel: TXSNAWB
abkuerzung: TXSNAWB
englisch: unblock attestation transaction
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/aktionsmanagement/entsperrnachweis.md, lexikon/aktionsmanagement/entsperrung-ueber-aktionsliste.md]
quellen: [Q02, Q06, Q25, Q52, Q55]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › TXSNAWB
<!-- /GEN:breadcrumb -->

# TXSNAWB

`TXSNAWB` ist der Nachweis über die **Entsperrung** einer Berechtigung. [Q06](../../QUELLEN.md#q06), Kap. 2.1.5, führt die Nachricht ausdrücklich als „`TXSNAWB` Entsperrung“ auf. Die Struktur ist der nicht öffentlichen KA SST-SPEC zu entnehmen; zusätzlich ist die KA AktM-SPEC zu beachten ([Q06](../../QUELLEN.md#q06), Kap. 4.3.2; [Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummern 4 und 41).

Im [`logTransaktionsTyp`](logtransaktionstyp.md) ist die Zuordnung ausdrücklich belegt: „`TXSNAWB` – Entsperrtransaktion EFS über Aktionsliste = **38**“ ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1). Anders als beim [`TXRBER`](txrber.md) ist der Nachrichtenname hier direkt genannt. Der **Codewert 38** gilt KA-weit ([Q52](../../QUELLEN.md#q52), Tab. 6-65, S. 87); der Standard ordnet ihn dem Listeneintrag `TXELISBER` zu ([Q55](../../QUELLEN.md#q55), Kap. 6.2.3.1, S. 67). Die Zuordnung zum Nachweis `TXSNAWB` bleibt eine Festlegung des eTicket RheinMain · *verbundspezifisch*.

`TXSNAWB` ist damit die technische Entsprechung des fachlichen [Entsperrnachweises](../aktionsmanagement/entsperrnachweis.md). Dessen Empfängerregel ist im Glossar festgelegt: Bei einer Nutzermedium-Applikation geht der Nachweis an das Hintergrundsystem des Kundenvertragspartners, bei einer Berechtigung zusätzlich an den Produktverantwortlichen ([Q02](../../QUELLEN.md#q02), S. 39).

Gemeinsam mit [`TXABER`](txaber.md) und [`TXRBER`](txrber.md) bildet `TXSNAWB` die drei Transaktionsnachweise, die ein Terminalmanagementsystem aus der Ausführung von Aktionslisteneinträgen zurückliefert ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, 4.3.2).

Der Name legt „Sperrnachweis Berechtigung“ nahe, obwohl die Nachricht eine **Ent**sperrung meldet; das ist aus den öffentlichen Quellen nicht aufzulösen (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

`TXSNAWB` ist der Beleg: „Diese Berechtigung ist wieder freigegeben.“

Pia Brummbär hatte ihre BärenKarte als verloren gemeldet, Bodo Bärlauch hatte die Berechtigung gesperrt. Dann fand sie die Karte wieder, die Entsperrung wurde in die Aktionsliste eingetragen, und beim nächsten Kartenkontakt hat ein Terminal die Sperrmarkierung entfernt. `TXSNAWB` meldet genau diesen Moment zurück, mit der Kennzahl 38.

Diese Rückmeldung hat zwei Adressaten, und das ist bei der Entsperrung anders als bei der Ausgabe. War eine einzelne Berechtigung betroffen, geht der Beleg an die Bärstädter Verkehrsbetriebe **und** an den Bären-Verkehrsbund. Der Verkehrsbund muss wissen, dass sein Produkt wieder im Umlauf ist — und er muss den Entsperrauftrag von seiner Aktionsliste nehmen können.

Eine Eigenheit, die beim Lesen von Spezifikationen irritiert: Der Name sieht aus wie „Sperrnachweis Berechtigung“. Gemeldet wird aber eine Entsperrung. Das Pflichtenheft ist an dieser Stelle unmissverständlich — es schreibt hinter die Nachricht ausdrücklich das Wort „Entsperrung“ — und die Kennzahl 38 ist ebenfalls klar der Entsperrtransaktion zugeordnet.

Warum der Name trotzdem so lautet, lässt sich aus den öffentlichen Unterlagen nicht sagen. Vermutlich stammt er aus einer Zeit, in der Sperren und Entsperren als ein gemeinsamer Vorgang mit zwei Richtungen gedacht wurden.

Für die Praxis heißt das: Dem Namen nicht trauen, der Dokumentation trauen. Wer `TXSNAWB` nach Gefühl als Sperrnachweis einordnet, verbucht eine Freigabe als Sperrung — und das ist genau der Fehler, der im Kundencenter später schwer zu erklären ist.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 („Transaktionsnachweise TXABER, TXRBER, TXSNAWB Entsperrung“; Fußnote 1, PDF-S. 14: `TXSNAWB` – Entsperrtransaktion EFS über Aktionsliste = 38), Kap. 4.3.2 (Struktur aus `[KA_SPEC_SST]`, zusätzlich `[KA_SPEC_AktM]`) · *verbundspezifisch: eTicket RheinMain*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 39 („Entsperrnachweis“: Empfängerregel)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SST-SPEC, Inventarnummer 4; KA AktM-SPEC, Inventarnummer 41)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Entsperrnachweis](../aktionsmanagement/entsperrnachweis.md)
- [Entsperrung über Aktionsliste](../aktionsmanagement/entsperrung-ueber-aktionsliste.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
