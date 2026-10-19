---
titel: Entsperrnachweis
englisch: unblock attestation
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/entsperrung-ueber-aktionsliste.md, lexikon/aktionsmanagement/aktionsclearing.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Entsperrnachweis
<!-- /GEN:breadcrumb -->

# Entsperrnachweis

Ein Entsperrnachweis belegt die Ausführung einer Entsperrung. Allgemein protokolliert ein Nachweis authentisch eine zuvor ausgeführte Transaktion auf Nutzermedium-Ebene und wird zur weiteren Verarbeitung an die Hintergrundsysteme weitergeleitet ([Q02](../../QUELLEN.md#q02), S. 65).

Wohin er geht, hängt davon ab, **was** entsperrt wurde ([Q02](../../QUELLEN.md#q02), S. 39):

- Wird die Sperrmarkierung in einer **Nutzermedium-Applikation** entfernt, geht der Entsperrnachweis an das Hintergrundsystem des Kundenvertragspartners.
- Wird sie in einer **Berechtigung** entfernt, geht er an das Hintergrundsystem des Kundenvertragspartners **und zusätzlich an den Produktverantwortlichen**.

Diese Asymmetrie folgt den Zuständigkeiten: Die Applikation verantwortet der Kundenvertragspartner, das Produkt hinter der Berechtigung der Produktverantwortliche — und nur der Produktverantwortliche führt die Aktionsliste, aus der die Entsperrung stammt (abgeleitet).

Das eTicket-Regelwerk nennt dazu zwei getrennte Anwendungsfälle des Kundenvertragspartner-Systems: „Entsperrnachweis bearbeiten nach Aktionsauftrag“ und „Entsperrnachweis an PV melden“ ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38). Verarbeitung und Weitermeldung sind also zwei Schritte.

Im eTicket RheinMain wird der Nachweis zur Entsperrung über die Aktionsliste als `TXSNAWB` übertragen und über den `logTransaktionsTyp` 38 gekennzeichnet ([Q06](../../QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Pia hat ihre wiedergefundene BärenKarte an das Lesegerät am Hauptbahnhof gehalten, die Sperre ist weg. Nun muss die Welt davon erfahren — und zwar nicht nur eine Stelle, sondern je nach Fall zwei.

Der Nachweis ist dabei mehr als eine Benachrichtigung. Er ist ein **Protokoll mit Beweiskraft**: Er hält fest, dass auf dieser Karte tatsächlich etwas geschehen ist, und er ist dabei kryptografisch gesichert, sodass man ihm trauen kann.

Wer ihn bekommt, hängt davon ab, was entsperrt wurde.

War die **ganze Karte** stillgelegt, also die Applikation darauf, dann ist das eine Angelegenheit der Bärstädter Verkehrsbetriebe. Sie haben die Karte ausgegeben, sie verwalten sie, sie bekommen die Meldung.

War dagegen eine **einzelne Berechtigung** gesperrt — etwa nur Pias ABO Azubi, während die Karte selbst nutzbar blieb —, dann geht die Meldung an die BVB *und* an den Bären-Verkehrsbund. Der Grund ist einfach: Das ABO Azubi ist ein Produkt des Verkehrsbunds. Er muss wissen, dass sein Produkt wieder im Umlauf ist, und er führt außerdem die Aktionsliste, auf der der Entsperrauftrag stand — er muss ihn dort streichen können.

Dass es zwei getrennte Arbeitsschritte sind, steht ausdrücklich im Regelwerk: den Nachweis *bearbeiten* und ihn *an den Produktverantwortlichen melden*. Das System der BVB tut also zweierlei — es verbucht die Entsperrung bei sich und gibt sie weiter.

Diese Weitergabe hat eine praktische Folge, die man im Alltag unterschätzt: Geht sie verloren, bleibt beim Verkehrsbund ein Auftrag stehen, der längst erledigt ist. Für solche Fälle gibt es das Aktionsclearing.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 39 („Entsperrnachweis / Unblock Attestation“: Empfänger je nach Applikation oder Berechtigung), S. 65 („Nachweis / Attestation“: authentisches Protokoll einer ausgeführten Transaktion auf Nutzermedium-Ebene)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 238): „Entsperrnachweis bearbeiten nach Aktionsauftrag“, „Entsperrnachweis an PV melden“
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 und Fußnote 1, PDF-S. 13 (TXSNAWB, `logTransaktionsTyp` 38) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Entsperrung über Aktionsliste](entsperrung-ueber-aktionsliste.md)
- [Aktionsclearing](aktionsclearing.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
