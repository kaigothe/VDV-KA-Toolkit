---
titel: Rücknahme EFS über Aktionsliste
englisch: termination of an electronic ticket via action list
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md]
quellen: [Q02, Q05, Q06, Q25, Q52, Q55]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes:
  - wert: 39
    codeliste: NmTransaktionsTyp_CODE
    bedeutung: Rückgabe/Rücknahme EFS über Aktionsliste
    quelle: Q52
    fundstelle: Tab. 6-65 (S. 87); ergänzt durch Q55 Kap. 6.2 (S. 67)
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Rücknahme EFS über Aktionsliste
<!-- /GEN:breadcrumb -->

# Rücknahme EFS über Aktionsliste

Die Rücknahme einer Berechtigung ist einer der vier Aktionstypen der Aktionsliste. [Q02](../../QUELLEN.md#q02), S. 19, fasst sie weiter als die beiden anderen: „Rücknahme einer Berechtigung elektronischer Fahrschein **oder eBezahlberechtigung**“. Als KVP-Aktion des Aktionsmanagements heißt sie Berechtigung-Rücknahme ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5).

Im Feld `logTransaktionsTyp` gilt der Wert **39** für die Rückgabetransaktion EFS über Aktionsliste ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1). Anders als bei 37 und 38 nennt die Fußnote dort keinen Nachrichtennamen; aus der Aufzählung der zurückgelieferten Nachweise in derselben Kapitelstelle liegt `TXRBER` nahe (abgeleitet). Der **Wert 39** stammt aus der Standardcodeliste, dort als „Rückgabe/Rücknahme EFS über Aktionsliste“, und gilt KA-weit; die KA AktM-SPEC ergänzt ihn für den Listeneintrag `TXRLISBER` ([Q52](../../QUELLEN.md#q52), Tab. 6-65, S. 87; [Q55](../../QUELLEN.md#q55), Kap. 6.2.3.1, S. 67). Die Zuordnung zu `TXRBER` bleibt abgeleitet.

Das eTicket-Regelwerk unterscheidet zwei Anwendungsfälle: „Aktionsauftrag EFS_Berechtigung zurücknehmen“ für die Beauftragung und „EFS_Berechtigung zurücknehmen nach Aktionsauftrag“ für die Ausführung ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38).

Zum resultierenden Status: Der Wert **5** steht für „zurückgenommen“ und stammt aus der Standardcodeliste `WertobjektStatus_CODE`, dort mit der Entsprechung EN 1545-1 „canceled“ ([Q52](../../QUELLEN.md#q52), Tab. 6-91, S. 102). Er gilt damit KA-weit; die Nennung in [Q05](../../QUELLEN.md#q05), Abschnitt 2.1, war eine Auswahl aus dieser Liste. Siehe [berStatus](../berechtigungen/berstatus.md).

## Einfach erklärt – Beispiel aus Bärstadt

Pia Brummbär bricht ihre Ausbildung ab. Damit entfällt die Grundlage für das ABO Azubi, und die Berechtigung muss von der Karte verschwinden.

„Verschwinden“ ist dabei das falsche Bild. Die Daten werden nicht einfach gelöscht, sondern die Berechtigung wird **zurückgenommen** — sie erhält einen Zustand, der sagt: Diese Berechtigung ist nicht mehr gültig. Für die Kontrolle ist das dasselbe Ergebnis, für die Nachvollziehbarkeit nicht: Man kann hinterher noch erkennen, dass hier etwas war und was damit geschah.

Der Weg ist der gewohnte. Die Bärstädter Verkehrsbetriebe beauftragen die Rücknahme, der Auftrag landet in der Aktionsliste, und beim nächsten Kartenkontakt führt ein Terminal ihn aus. Die Rückmeldung trägt die Kennzahl 39.

Interessant ist, was diese Aktion gegenüber den anderen zwei umfasst. Ausgeben und Entsperren betreffen Fahrscheine. Zurücknehmen geht weiter: Es gilt auch für eine Bezahlberechtigung, also für die Funktion, mit der Fahrgeld hinterlegt wird. Rücknahme ist damit der allgemeinste der drei Vorgänge.

Zwei Dinge lohnen beim Lesen einer solchen Nachricht die Aufmerksamkeit.

Das eine ist die Unterscheidung zwischen **Auftrag** und **Ausführung**. Dass eine Rücknahme beauftragt wurde, heißt nicht, dass sie geschehen ist. Solange Pia ihre Karte in der Schublade liegen lässt, steht der Auftrag und nichts passiert. Erst der Nachweis vom Terminal belegt die Ausführung.

Das andere ist der Zustandswert. Im RMV steht die 5 für „zurückgenommen“. Diese Zahl stammt aber aus der Festlegung eines einzelnen Verbunds. Sie ungeprüft auf ein anderes System zu übertragen, wäre genau der Fehler, vor dem dieses Lexikon an mehreren Stellen warnt.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19 („Rücknahme einer Berechtigung elektronischer Fahrschein oder eBezahlberechtigung“)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (Berechtigung-Rücknahme als KVP-Aktion; Nachweise TXABER, TXRBER, TXSNAWB; Fußnote 1, PDF-S. 14: Rückgabetransaktion EFS über Aktionsliste = 39) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 239)
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Abschnitt 2.1 (berStatus 5 = zurückgenommen) · *verbundspezifisch, Fundstelle noch nicht am Dokument geprüft*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Ausgabe EFS über Aktionsliste](ausgabe-efs-ueber-aktionsliste.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
