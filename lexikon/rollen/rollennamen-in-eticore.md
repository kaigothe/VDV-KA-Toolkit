---
titel: Rollennamen in etiCORE
englisch: role names in etiCORE
parent: lexikon/rollen.md
siehe_auch: [lexikon/grundlagen/eticore.md, lexikon/rollen/rollencodes.md]
quellen: [Q02, Q43, Q45]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Rollennamen in etiCORE
<!-- /GEN:breadcrumb -->

# Rollennamen in etiCORE

Mit [etiCORE](../grundlagen/eticore.md) werden die Rollen und zentralen Dienste **umbenannt und englisch benannt**. Die Zuordnung ist über die Migrationsdokumente des Releases belegt, die jeweils „die Gegenüberstellung der Anwendungsfälle“ beider Welten enthalten ([Q43](../../QUELLEN.md#q43), Kap. 7.1, PDF-S. 35):

| KA 1.x | etiCORE | Gegenstand |
|---|---|---|
| [KVP](kvp.md) Kundenvertragspartner | **CCP** Customer Contract Partner | Hintergrundsystem und Terminal |
| [PV](pv.md) Produktverantwortlicher | **PO** Product Owner | Hintergrundsystem |
| [DL](dl.md) Dienstleister | **SO** Service Operator | Hintergrundsystem und Terminal |
| [KOSE](kose.md) Kontroll- und Sperrlistenservice | **Hotlist Service** | zentraler Dienst |
| ZVM Zentrale Vermittlungsstelle | **CRE** Central Routing Engine | zentraler Dienst |
| ASM Applikations- und Sicherheitsmanagement | **ESH** e-Ticket Security Hub | zentraler Dienst |
| PE Personalisierungseinheit | **Execution Unit**, Schnittstelle EUI | Terminalanteil |
| Fremdsystem | **External System**, Schnittstelle ESI | Terminalanteil |
| [Nutzermedium](../medien/nutzermedium.md) | **UM** User Medium | Medium |

Die Abkürzungen ZVM, ASM und PE der linken Spalte sind über [Q45](../../QUELLEN.md#q45), S. 7 f., belegt.

**Zwei Rollen haben kein unmittelbares Gegenstück.** Neu ist der **eCCP**, der Executing Customer Contract Partner: ein CCP, „welches zusätzlich zur Grundfunktionalität im Rahmen des [Aktionsmanagements](../aktionsmanagement.md) ausgeführte Aktionen verarbeitet“ beziehungsweise „Aktionen mit dem Nutzermedium ausführt und meldet“. Daneben steht der **CCP-STE** für Systeme und Terminals, die „ausschließlich mit [statischen Berechtigungen](../berechtigungen/statische-berechtigung.md) arbeiten“ ([Q43](../../QUELLEN.md#q43), Kap. 2.1, PDF-S. 24).

Die Aufgabe des [ALISE](alise.md) findet sich in den Schnittstellen wieder: „Product Owner Action Management“ auf der bestellenden, „Customer Contract Partner Action Ordering“ und „Customer Contract Partner Ordered Action Execution“ auf der ausführenden Seite ([Q43](../../QUELLEN.md#q43), Kap. 5.2.2, PDF-S. 33) — eine Gleichsetzung mit ALISE ist damit naheliegend, aber nicht ausgesprochen (abgeleitet).

Der [AH](ah.md) erscheint als Teil des **Scheme Manager** ([Q02](../../QUELLEN.md#q02), S. 23).

## Einfach erklärt – Beispiel aus Bärstadt

Dieselben Beteiligten, andere Namen. Mehr ist es im Kern nicht — aber es reicht, um beim Lesen zweier Dokumente durcheinanderzukommen.

Bärstadt unter etiCORE:

- Die **Bärstädter Verkehrsbetriebe** sind nicht mehr KVP, sondern **CCP**. Sie haben den Vertrag mit Pia, sie geben die Karte aus.
- Der **Bären-Verkehrsbund** ist nicht mehr PV, sondern **PO** — Product Owner. Ihm gehört das Produkt 2001, das ABO Azubi.
- Im Fahrbetrieb ist die BVB nicht mehr DL, sondern **SO**, Service Operator.
- Der **Kontrollservice Bärenland** heißt nicht mehr KOSE, sondern **Hotlist Service**. Die Sperrliste wird zur Hotlist.
- Pias **BärenKarte** ist kein NM mehr, sondern ein **UM**, User Medium.

Zwei Dinge sind mehr als eine Umbenennung.

**Der eCCP.** Bisher war die Ausführung einer Aktionsliste eine Fähigkeit, die ein KVP eben hatte oder nicht. Jetzt gibt es dafür einen eigenen Namen: ein CCP, der Aktionen ausführt und meldet, ist ein eCCP. Für die BVB heißt das, dass sie sich entscheiden muss — und dass im Vertrag und im Lastenheft steht, was sie dann können muss.

**Der CCP-STE.** Wer nur mit statischen Berechtigungen arbeitet, also mit Barcodes, braucht nicht den ganzen Apparat. Für dieses Haus gibt es jetzt eine eigene, kleinere Spezifikation. Ein Luchsstädter Busunternehmen, das nur Handy-Tickets verkauft, muss nicht mehr dasselbe umsetzen wie die BVB mit ihren Chipkarten.

**Ein praktischer Rat für die Lektüre.** Wer in einem etiCORE-Dokument „CCP“ liest und in einem Pflichtenheft von 2019 „KVP“, liest über dieselbe Rolle. Wer dagegen „eCCP“ liest, liest über eine Rolle, die es unter diesem Namen vorher nicht gab. Der Unterschied zwischen einer Umbenennung und einer Neuerung ist genau die Stelle, an der man beim Vergleich zweier Versionen stolpert.

## Quellen

- [Q43](../../QUELLEN.md#q43) – etiCORE Release Letter 3.0.0-rc.6: Kap. 2.1, PDF-S. 24 (eCCP als CCP, der im Rahmen des Aktionsmanagements ausgeführte Aktionen verarbeitet bzw. Aktionen mit dem Nutzermedium ausführt und meldet; CCP-STE für ausschließlich statische Berechtigungen; Referenzspezifikationen für CCP, SO, PO), Kap. 5.2.2, PDF-S. 33 (Schnittstellen Product Owner Action Management, Customer Contract Partner Action Ordering, Customer Contract Partner Ordered Action Execution; ESH als vormaliges ASM), Kap. 7.1, PDF-S. 35 (Migrationsdokumente mit der Gegenüberstellung KVP/CCP, PV/PO, DL/SO, KOSE/Hotlist Service, ZVM/CRE, ASM/ESH, PE/Execution Unit, Fremdsystem/External System)
- [Q45](../../QUELLEN.md#q45) – ASM-Tool Glossar, S. 7 f. (Abkürzungen ASM als Applikations- und Sicherheitsmanagement-System, ZVM als Zentrale Vermittlungsstelle im ION, NM als Nutzermedium)
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 23 (Applikationsherausgeber als Teil des Scheme Manager)

<!-- GEN:siehe_auch -->
## Siehe auch

- [etiCORE](../grundlagen/eticore.md)
- [Rollencodes](rollencodes.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
