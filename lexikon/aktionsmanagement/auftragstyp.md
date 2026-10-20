---
titel: Auftragstyp
englisch: order type
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktion.md, lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md]
quellen: [Q02, Q11, Q25, Q50, Q52, Q55]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 11
    codeliste: AuftragsTyp_CODE
    bedeutung: Aktionsliste
    quelle: Q52
    fundstelle: Tab. 6-43 (S. 69)
    status: belegt
    verbundspezifisch: false
  - wert: 12
    codeliste: AuftragsTyp_CODE
    bedeutung: Aktionsdifferenzliste
    quelle: Q52
    fundstelle: Tab. 6-43 (S. 69)
    status: belegt
    verbundspezifisch: false
  - wert: 13
    codeliste: AuftragsTyp_CODE
    bedeutung: Aktionsauftrag Ausgabe
    quelle: Q55
    fundstelle: Kap. 6.2 (S. 67)
    status: belegt
    verbundspezifisch: false
  - wert: 14
    codeliste: AuftragsTyp_CODE
    bedeutung: Aktionsauftrag Rücknahme
    quelle: Q55
    fundstelle: Kap. 6.2 (S. 67)
    status: belegt
    verbundspezifisch: false
  - wert: 15
    codeliste: AuftragsTyp_CODE
    bedeutung: Aktionsauftrag Entsperrung
    quelle: Q55
    fundstelle: Kap. 6.2 (S. 67)
    status: belegt
    verbundspezifisch: false
  - wert: 16
    codeliste: AuftragsTyp_CODE
    bedeutung: Löschauftrag Aktion
    quelle: Q52
    fundstelle: Tab. 6-43 (S. 69)
    status: belegt
    verbundspezifisch: false
  - wert: 22
    codeliste: AuftragsTyp_CODE
    bedeutung: Aktionsliste_zip
    quelle: Q52
    fundstelle: Tab. 6-43 (S. 69)
    status: belegt
    verbundspezifisch: false
  - wert: 23
    codeliste: AuftragsTyp_CODE
    bedeutung: Aktionsdifferenzliste_zip
    quelle: Q52
    fundstelle: Tab. 6-43 (S. 69)
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Auftragstyp
<!-- /GEN:breadcrumb -->

# Auftragstyp

Das Feld `amAuftragsTyp` kennzeichnet in einem Aktionslisteneintrag die Art des Aktionsauftrags. Es hat den Typ **`AuftragsTyp_CODE`** und gibt an, „um welchen Typ Datensatz es sich innerhalb einer Liste des AktM handelt“ ([Q55](../../QUELLEN.md#q55), Kap. 6.4.2, S. 88).

Die KA AktM-SPEC ergänzt diese Codeliste um drei Werte für das Aktionsmanagement ([Q55](../../QUELLEN.md#q55), Kap. 6.2, S. 67):

| Wert | Bedeutung |
|---:|---|
| **13** | Aktionsauftrag Ausgabe |
| **14** | Aktionsauftrag Rücknahme |
| **15** | Aktionsauftrag Entsperrung |

Dazu tragen **16** den Löschauftrag Aktion, **11** die Aktionsliste und **12** die Aktionsdifferenzliste, komprimiert **22** und **23** ([Q52](../../QUELLEN.md#q52), Tab. 6-43, S. 69).

Damit ist der Wert **13** der ausgewerteten `txalisber`-Nachricht ([Q11](../../QUELLEN.md#q11)) als Ausgabe einer Berechtigung **belegt**. Die frühere Indizienkette aus `logTransaktionsTyp` 37 und `berSynchronNummer` 1 führte zum richtigen Ergebnis.

**Zum Verhältnis der Begriffsebenen:** Im Aktionsmanagement wird „zwischen Ausgabe, Rücknahme von EFS und Entsperrung von Berechtigungen unterschieden sowie der Löschung einer“ Aktion ([Q55](../../QUELLEN.md#q55), S. 88). Auftragstyp und Aktionstyp sind keine zwei Ebenen — der Auftragstyp benennt die beauftragte Aktion.

**Eine Prüfregel aus dem Standard:** Die Aktionslistenprüfung im KVP-Terminal durchsucht den Bestand valider Aktionsaufträge; ein Treffer liegt vor, wenn die `appInstanz_ID` zusammen mit dem Auftragstyp 13, 14 oder 15 vorliegt **und** der Auftrag noch gültig ist ([Q55](../../QUELLEN.md#q55), Kap. 7.4.1.1, S. 132).

**Achtung bei Querverweisen:** Die KA AktM-SPEC verweist für `AuftragsTyp_CODE` auf „Tabelle 6-42“ und an anderer Stelle auf „Tabelle 6-59“ der KA BOM-SPEC. In 1.12.0 ist es **Tabelle 6-43**; 6-59 ist der `IONTransaktionsTyp_CODE`. Die Tabellennummern dieser Querverweise sind veraltet.

## Einfach erklärt – Beispiel aus Bärstadt

Im Auftrag für Pias ABO Azubi steht an einer Stelle eine 13. Lange wusste niemand hier, was sie bedeutet. Jetzt steht es fest: **Aktionsauftrag Ausgabe.**

Die Stelle sagt, was mit der Berechtigung geschehen soll. Drei Dinge kommen in Frage, und sie haben benachbarte Nummern:

**13 — ausgeben.** Eine neue Berechtigung soll auf die Karte.
**14 — zurücknehmen.** Sie soll wieder verschwinden.
**15 — entsperren.** Eine gesperrte soll wieder gelten.

Dazu kommt die 16 für „Auftrag löschen“ — nicht die Berechtigung, sondern der Auftrag selbst. Und weil dieselbe Liste auch beschreibt, was man anfordern kann, stehen dort noch 11 für die Aktionsliste und 12 für die Aktionsdifferenzliste.

Es lohnt, kurz zu erzählen, wie diese 13 geklärt wurde — nicht weil das Ergebnis spannend ist, sondern weil der Weg etwas über die Arbeit mit solchen Nachrichten sagt.

Vorher ließ sich nur ermitteln wie bei einem Indizienprozess. An anderer Stelle derselben Nachricht stand eine 37, und die bedeutet belegt „Ausgabe eines Fahrscheins über die Aktionsliste“. Der Versionszähler stand auf 1, es war der erste Stand. Beide Indizien zeigten in dieselbe Richtung. Daraus folgte: 13 heißt wahrscheinlich „Ausgabe“ — aber eben nur wahrscheinlich.

Dieser Artikel trug deshalb den Status „zu prüfen“, und im Werkzeug hätte die 13 bis auf Weiteres mit Vorbehalt angezeigt werden müssen. Das war unbefriedigend, aber richtig: Hätte man die Vermutung als Tatsache eingetragen und falsch gelegen, dann zeigte das Werkzeug ab sofort überzeugend formatierte, falsche Auskünfte — und niemand käme auf die Idee, sie zu hinterfragen.

Nun liegt die Spezifikation vor, und sie sagt es in einem Satz: dem Auftragstyp werden drei Codes hinzugefügt, 13 für Ausgabe, 14 für Rücknahme, 15 für Entsperrung. Die Vermutung war richtig.

Daraus zwei Lehren. Die erste: Eine gut gebaute Indizienkette trägt oft weit. Die zweite, wichtigere: Man weiß vorher nicht, welche sie ist. Deshalb bleibt der Unterschied zwischen „belegt“ und „abgeleitet“ in jedem Satz dieses Lexikons sichtbar — damit später jemand nachsehen kann, worauf er sich eigentlich verlässt.

Ein praktischer Nachsatz für den Werkzeugbau: Die Spezifikation beschreibt auch, wie ein Terminal seine Aktionsliste durchsucht. Es sucht nach der Kennung der Applikationsinstanz zusammen mit einem der drei Auftragstypen — und prüft zusätzlich, ob der Auftrag überhaupt noch gültig ist. Ein abgelaufener Auftrag ist kein Treffer.

## Quellen

- [Q55](../../QUELLEN.md#q55) – KA AktM-SPEC 1.12.0, Kap. 6.2 (S. 67): dem Aufzählungstyp `AuftragsTyp_CODE` werden drei Codes für das Aktionsmanagement hinzugefügt — Aktionsauftrag Ausgabe (13), Rücknahme (14), Entsperrung (15); Kap. 6.4.2 (S. 88): `amAuftragsTyp` vom Typ `AuftragsTyp_CODE`, Kardinalität 1..1, mit der Unterscheidung von Ausgabe, Rücknahme, Entsperrung und Löschung; Kap. 7.4.1.1 (S. 132): Aktionslistenprüfung im KVP-Terminal. Exzerpt: [exzerpte/Q55.md](../../exzerpte/Q55.md) · *nicht öffentlich*
- [Q52](../../QUELLEN.md#q52) – KA HD_BOM-SPEC 1.12.0, Tab. 6-43 (S. 69): Codeliste `AuftragsTyp_CODE`, Format `INT1`; S. 68: „Der AuftragsTyp_CODE gibt an, welcher Auftrag auf Seiten des Empfängers der Auftragstransaktion ausgelöst werden soll.“ Exzerpt: [exzerpte/Q52.md](../../exzerpte/Q52.md) · *nicht öffentlich*
- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht, Feld `amAuftragsTyp` mit dem Wert 13. **Nicht öffentliche Unterlage**; übernommen sind nur Feldname und Wert, keine weiteren Inhalte.
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19 (die vier möglichen Aktionen einer Aktionsliste)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 239): Anwendungsfälle „Aktionsauftrag …“
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management_xsd`: `amAuftragsTyp` entfällt in den Listeneinträgen mit der Begründung „clear from context“ · *Release-Kandidat*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Aktion](aktion.md)
- [Ausgabe EFS über Aktionsliste](ausgabe-efs-ueber-aktionsliste.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
