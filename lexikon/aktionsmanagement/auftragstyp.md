---
titel: Auftragstyp
englisch: order type
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktion.md, lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md]
quellen: [Q02, Q11, Q25, Q50]
status: zu prüfen
offene_fragen: [O2, O9]
stand: 2026-10-20
codes:
  - wert: 13
    codeliste: amAuftragsTyp
    bedeutung: vermutlich Ausgabe einer Berechtigung über die Aktionsliste
    quelle: Q11
    fundstelle: Feld amAuftragsTyp im ausgewerteten Datensatz
    status: zu prüfen
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Auftragstyp
<!-- /GEN:breadcrumb -->

# Auftragstyp

Das Feld `amAuftragsTyp` kennzeichnet in einem Aktionslisteneintrag die Art des Aktionsauftrags. In der ausgewerteten `txalisber`-Nachricht trägt es den Wert **13** ([Q11](../../QUELLEN.md#q11)).

**Die Bedeutung des Werts 13 ist nicht belegt** (zu prüfen, O2). Die zugehörige Codeliste steht in der nicht öffentlichen KA AktM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 41).

Für „Ausgabe einer Berechtigung“ spricht eine Indizienkette aus derselben Nachricht (abgeleitet): Der `logTransaktionsTyp` ist 37, also Ausgabe EFS über Aktionsliste; die `berSynchronNummer` ist 1, es ist der erste Stand. Dazu kommt ein Hinweis aus etiCORE: Dort entfällt `amAuftragsTyp` in den Listeneinträgen für Ausgabe, Entsperrung und Rücknahme mit der Begründung „clear from context“; der Typ des Eintrags trägt die Information ([Q50](../../QUELLEN.md#q50), `po-oa-management_xsd`). Das Feld unterscheidet demnach die Auftragsarten (abgeleitet).

Offen ist zudem das **Verhältnis der Begriffsebenen** (zu prüfen, O9). [Q02](../../QUELLEN.md#q02), S. 19, zählt vier *Aktionen* auf: Ausgabe eines elektronischen Fahrscheins, Entsperren einer Berechtigung, Rücknahme einer Berechtigung sowie — nur für (((etiCORE — Sperren einer Berechtigung. Das eTicket-Regelwerk benennt für das Kundenvertragspartner-System die *Anwendungsfälle* „Aktionsauftrag EFS_Berechtigung ausgeben“, „Aktionsauftrag EFS_Berechtigung zurücknehmen“ und „Aktionsauftrag Berechtigung entsperren“ ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38).

Die Wortwahl „Aktionsauftrag“ stützt die Lesart, dass der Auftragstyp die beauftragte Aktion bezeichnet und damit nahe an den Aktionstypen liegt (abgeleitet). Ob die Codewerte eins zu eins den vier Aktionen entsprechen, ist damit nicht gezeigt.

## Einfach erklärt – Beispiel aus Bärstadt

Im Auftrag für Pias ABO Azubi steht an einer Stelle eine 13. Niemand kann derzeit mit Sicherheit sagen, was diese 13 bedeutet — und das ist ein gutes Beispiel dafür, wie man mit so einer Lücke sauber umgeht.

Was man weiß: An der Stelle steht die **Art des Auftrags**. Ob also eine Berechtigung ausgegeben, zurückgenommen oder entsperrt werden soll. Was fehlt, ist die Übersetzungstabelle von Zahlen in Bedeutungen. Diese Tabelle steht in einer Spezifikation, die nicht öffentlich ist.

Man kann sich der Antwort trotzdem nähern, und zwar so, wie ein Ermittler es täte: über Indizien, die sich gegenseitig stützen.

Erstens steht an anderer Stelle derselben Nachricht die Zahl 37, und die bedeutet belegt „Ausgabe eines Fahrscheins über die Aktionsliste“. Zweitens steht der Versionszähler auf 1, es ist der allererste Stand. Beide Indizien zeigen in dieselbe Richtung: Hier wird etwas Neues ausgegeben, nichts entsperrt. Drittens haben die etiCORE-Unterlagen das Feld ersatzlos gestrichen, weil sich der Typ dort aus der Art des Eintrags ergibt. Das bestätigt, dass es die Art des Auftrags meint, nicht aber, welche Zahl welche Art ist.

Daraus folgt mit guter Wahrscheinlichkeit: 13 heißt „Ausgabe“. Was eben nicht folgt: dass das sicher ist.

Dieser Unterschied ist keine Spitzfindigkeit. Würde man die 13 als gesicherte Tatsache in ein Auswertungswerkzeug schreiben und läge man falsch, dann zeigte das Werkzeug ab sofort überzeugend formatierte, falsche Auskünfte — und niemand käme auf die Idee, sie zu hinterfragen. Eine ehrliche Lücke ist nützlicher als eine selbstsichere Vermutung.

Deshalb trägt dieser Artikel den Status „zu prüfen“, und die Frage steht als offener Punkt im Plan.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management_xsd`: Typen `EntitlementIssuanceActionListEntry`, `…UnblockingActionListEntry`, `…TerminationActionListEntry` mit `meta:deleted` = `amAuftragsTyp` („clear from context“) · *Release-Kandidat*
- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht, Feld `amAuftragsTyp` mit dem Wert 13. **Nicht öffentliche Unterlage**; übernommen sind nur Feldname und Wert, keine weiteren Inhalte.
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19 (die vier möglichen Aktionen einer Aktionsliste)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA AktM-SPEC, Inventarnummer 41, als Normquelle der Codeliste); Anlage 2, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 239): Anwendungsfälle „Aktionsauftrag …“

<!-- GEN:siehe_auch -->
## Siehe auch

- [Aktion](aktion.md)
- [Ausgabe EFS über Aktionsliste](ausgabe-efs-ueber-aktionsliste.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
