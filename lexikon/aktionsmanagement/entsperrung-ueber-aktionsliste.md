---
titel: Entsperrung über Aktionsliste
englisch: unblocking via action list
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/entsperrnachweis.md, lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: [O1]
stand: 2026-10-19
codes:
  - wert: 38
    bedeutung: TXSNAWB – Entsperrtransaktion EFS über Aktionsliste
    quelle: Q06
    fundstelle: Kap. 2.1.5, Fußnote 1 (PDF-S. 13)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Entsperrung über Aktionsliste
<!-- /GEN:breadcrumb -->

# Entsperrung über Aktionsliste

Das Entsperren einer Berechtigung ist einer der vier Aktionstypen, die über eine Aktionsliste beauftragt werden können ([Q02](../../QUELLEN.md#q02), S. 19), und zählt zu den KVP-Aktionen des Aktionsmanagements ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5).

Fachlich ist eine Entsperrung ein **Statuswechsel**: Nutzermedium-Applikationen und Berechtigungen können entsperrt werden und sind danach wieder nutzbar; das Entsperren erfolgt aufgrund einer Statusänderung bei der Applikation oder Berechtigung auf dem Nutzermedium. Ein Entsperren ist **nur an autorisierten Terminals des Kundenvertragspartners möglich** ([Q02](../../QUELLEN.md#q02), S. 38 f.).

Im Feld `logTransaktionsTyp` gilt der Wert **38** für die Entsperrtransaktion EFS über Aktionsliste, dort dem Nachweis `TXSNAWB` zugeordnet ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1). Diese Zuordnung ist eine Festlegung im eTicket RheinMain; ob sie KA-weit gilt, ist nicht belegt (zu prüfen, O1) · *verbundspezifisch*.

Das eTicket-Regelwerk benennt den vollständigen Ablauf über drei Anwendungsfälle des Kundenvertragspartner-Systems: „Aktionsauftrag Berechtigung entsperren“, „Entsperrnachweis bearbeiten nach Aktionsauftrag“ und „Entsperrnachweis an PV melden“ ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38).

Damit ist die Entsperrung über die Aktionsliste vom bloßen Zustand „entsperrt“ zu unterscheiden: Dieser Artikel beschreibt den beauftragten Vorgang, nicht den Status.

## Einfach erklärt – Beispiel aus Bärstadt

Eine gesperrte Karte ist nicht kaputt. Sie ist stillgelegt — und lässt sich wieder in Betrieb nehmen.

Angenommen, Pia Brummbär meldet ihre BärenKarte als verloren. Bodo Bärlauch sperrt daraufhin ihre Berechtigung, damit niemand mit dem gefundenen Stück fährt. Zwei Tage später findet Pia die Karte in der Jackentasche wieder.

Jetzt muss die Sperre weg. Und hier stellt sich dasselbe Problem wie bei der Ausgabe: Bodo kann die Karte nicht aus der Ferne ändern. Die Sperrmarkierung sitzt auf dem Chip, und auf den Chip kommt nur ein Gerät, das die Karte tatsächlich in der Hand hat.

Also geht die Entsperrung denselben Weg: Sie wird als Auftrag in die Aktionsliste eingetragen. Beim nächsten Mal, wenn Pia ihre Karte an ein Gerät hält, wird die Markierung entfernt. Danach gilt die Berechtigung wieder.

Eine Einschränkung gibt es: Entsperren darf nicht jedes Gerät, sondern nur ein autorisiertes Terminal des Kundenvertragspartners — in Bärstadt also der BVB. Das ist einleuchtend: Sperren schützt vor Missbrauch, und eine Schutzmaßnahme, die jedes beliebige Gerät aufheben könnte, wäre keine.

Wie bei der Ausgabe entsteht auch hier eine Rückmeldung, der **Entsperrnachweis**. Er trägt die Kennzahl 38 und sagt: „Diese Berechtigung wurde über die Aktionsliste wieder freigegeben.“ Er geht an die BVB und zusätzlich an den Bären-Verkehrsbund als Produktverantwortlichen — der muss wissen, dass sein Produkt wieder im Umlauf ist.

Zwei Begriffe lohnen die Unterscheidung: Dieser Artikel beschreibt den **Vorgang** des Entsperrens. Dass eine Berechtigung danach *den Zustand* „entsperrt“ hat, ist etwas anderes — das ist ihr Status.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19 („Entsperren einer Berechtigung“ als Aktion der Aktionsliste), S. 38 f. („Entsperrung“: Statusänderung auf dem Nutzermedium, nur an autorisierten KVP-Terminals), S. 39 („Entsperrnachweis“)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (Berechtigung-Entsperrung als KVP-Aktion; Fußnote 1, PDF-S. 13: TXSNAWB – Entsperrtransaktion EFS über Aktionsliste = 38) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 238)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
