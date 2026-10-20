---
titel: Änderungsreferenz
englisch: change reference
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/auftragstyp.md, lexikon/aktionsmanagement/aktionsmanagement-in-eticore.md]
quellen: [Q02, Q11, Q25, Q50]
status: zu prüfen
offene_fragen: [O13]
stand: 2026-10-20
codes:
  - wert: 0
    codeliste: amAenderungsreferenz_ID
    bedeutung: vermutlich keine Gruppe (in etiCORE ist das Nachfolgefeld groupId optional)
    quelle: Q50
    fundstelle: po-oa-management_xsd, Typ ActionListEntryBaseInformation, Element groupId
    status: abgeleitet
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Änderungsreferenz
<!-- /GEN:breadcrumb -->

# Änderungsreferenz

Das Feld `amAenderungsreferenz_ID` steht in einem Aktionslisteneintrag. In der ausgewerteten `txalisber`-Nachricht trägt es den Wert **0** in beiden Teilen, Nummer und Organisation ([Q11](../../QUELLEN.md#q11)).

**Die Bedeutung ist in den Quellen zur KA 1.x nicht belegt** (zu prüfen, O13). Die Feldsemantik steht in der nicht öffentlichen KA AktM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 41). Das Glossar [Q02](../../QUELLEN.md#q02) enthält keinen Eintrag; geprüft am Inhaltsverzeichnis, S. 2–13.

Einen Hinweis geben die etiCORE-Schnittstellen. Dort ist `amAenderungsreferenz_ID` der Altname von `groupId`. Das Feld besteht aus der Organisations-ID des bestellenden CCP und einer Gruppennummer. Es gruppiert Einträge „logically“, damit sie „in a single transaction“ ausgeführt werden, und ist optional ([Q50](../../QUELLEN.md#q50), `po-oa-management_xsd`, Typ `ActionListEntryBaseInformation`).

Danach wäre die Änderungsreferenz eine **Gruppenzugehörigkeit** und kein Verweis auf eine Vorgänger-Berechtigung (abgeleitet, O13). Den Verweis auf eine ersetzte Berechtigung führt etiCORE als eigenes Feld `replacedEntitlementId`, neu seit 3.0.0 und ohne Altnamen ([Q50](../../QUELLEN.md#q50), `po-oa-management_xsd`). Das passt zu den zwei Teilen des Werts; 0/0 hieße „keine Gruppe“ (abgeleitet).

Ungeklärt bleibt, ob die KA 1.x das Feld ebenso verwendet und welchen Wert es bei einer tatsächlichen Gruppierung trägt (zu prüfen, O13). Die etiCORE-Angaben stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

In Pias Auftrag steht an einer Stelle eine Null — genauer: zwei Nullen, eine für eine Nummer und eine für eine Organisation. Das Feld heißt Änderungsreferenz.

Der Name legt eine Deutung nahe: ein Verweis auf etwas Früheres, die Berechtigung, die ersetzt wird. Diese Deutung tragen die etiCORE-Unterlagen nicht. Dort heißt das Feld **Gruppe**. Es besteht aus der Organisation des Bestellers und einer Nummer, die bei diesem Besteller eindeutig ist. Einträge mit derselben Gruppe sollen zusammen in einer Transaktion ausgeführt werden.

Denkbar ist das so: Pia wechselt von ihrem ABO Azubi auf eine Monatskarte Bärstadt. Die BVB bestellt die Rücknahme des alten Produkts und die Ausgabe des neuen. Beides soll gemeinsam geschehen, sonst stünde Pia kurz mit zwei Produkten oder mit keinem da. Tragen beide Einträge dieselbe Gruppe, kann das Terminal sie in einem Zug abarbeiten. Das ist eine Veranschaulichung, keine Beschreibung der Nachricht.

Pias Auftrag trägt zweimal die Null. Wenn die Null „keine Gruppe“ heißt, steht der Eintrag für sich allein: Er ist eine einzelne Ausgabe ohne Partner. Dazu passt, dass die beiden anderen Felder derselben Nachricht auf eine einfache Neuausgabe zeigen.

Wichtig bleibt die Grenze: Auch diese Lesart ist erschlossen, aus den Angaben eines Release-Kandidaten und nicht aus einer KA-1.x-Quelle. Niemand hier hat eine Nachricht gesehen, in der das Feld nicht null ist. Deshalb steht der Artikel weiter auf „zu prüfen“. Ein Auswertungswerkzeug darf die Null als „keine Gruppe“ anzeigen, aber mit dem Hinweis, dass diese Deutung erschlossen ist.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management_xsd`: Typ `ActionListEntryBaseInformation`, Element `groupId` mit `meta:old` = `amAenderungsreferenz_ID`; Typ `GroupId` · *Release-Kandidat*
- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht, Feld `amAenderungsreferenz_ID` mit dem Wert 0/0, dazu `berSynchronNummer` 1 und `logTransaktionsTyp` 37. **Nicht öffentliche Unterlage**; übernommen sind nur Feldnamen und Werte.
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA AktM-SPEC, Inventarnummer 41, als Normquelle der Feldsemantik)
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE: **kein** Eintrag zur Änderungsreferenz (geprüft am Inhaltsverzeichnis, S. 2–13)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Auftragstyp](auftragstyp.md)
- [Aktionsmanagement in etiCORE](aktionsmanagement-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
