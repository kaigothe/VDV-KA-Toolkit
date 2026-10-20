---
titel: Aktionsmanagement in etiCORE
englisch: action management in etiCORE
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktionsliste.md, lexikon/aktionsmanagement/aktionsdifferenzliste.md, lexikon/transaktionen/nachrichten-in-ka-1-x-und-eticore.md, lexikon/rollen/rollennamen-in-eticore.md]
quellen: [Q02, Q49, Q50]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktionsmanagement in etiCORE
<!-- /GEN:breadcrumb -->

# Aktionsmanagement in etiCORE

In [etiCORE](../grundlagen/eticore.md) verteilt sich das Aktionsmanagement auf drei Schnittstellen: `po-oa-management` im Product-Owner-System, `ccp-oa-ordering` für den bestellenden und `ccp-oa-execution` für den ausführenden CCP ([Q50](../../QUELLEN.md#q50), WSDL `po-oa-management`, Operationsliste). Eine *ordered action* ist eine Aktion auf einem User Medium, die im PO-System bestellt und über Aktionslisten an ausführende CCP verteilt wird; diese legen sie in ihren Terminals ab ([Q49](../../QUELLEN.md#q49), Glossar).

**Bestellen.** Der bestellende CCP ruft `orderEntitlementIssuance`, `…Blocking`, `…Unblocking` und `…Termination` auf und storniert mit `cancelOrder`. `orderGroup` bestellt mehrere Aufträge „in an atomic fashion“ und gilt seit 3.0.0 ([Q50](../../QUELLEN.md#q50), WSDL `po-oa-management`).

**Abrufen.** Der ausführende CCP holt die vollständige Liste (`getActionList`) oder die inkrementelle (`getIncrementalActionList`, mit der Nummer der zuletzt empfangenen Liste); beide sind „now always compressed“. Mit `verifyActionListUpdatedViaIncrements` (seit 3.0.0) prüft er per Hash, ob sein Bestand zur Gesamtliste passt ([Q50](../../QUELLEN.md#q50), `po-oa-management-messaging_xsd`).

**Melden.** Nach der Ausführung meldet der ausführende CCP das Ergebnis an das PO-System (`notifyOrderedEntitlement…`). Bricht eine Ausgabe vor dem dauerhaften Schreiben ab, geht eine Meldung nur „for monitoring purposes“ ein (`…IssuingAborted`). Das PO-System leitet die Meldungen an den bestellenden CCP weiter (`forwardOrderedEntitlement…`) ([Q50](../../QUELLEN.md#q50)).

In etiCORE erhalten alle ausführenden CCP **dieselbe** Liste; die KA 1.x erlaubte eine Liste je KVP ([Q02](../../QUELLEN.md#q02), S. 19). Quelle ist ein Release-Kandidat, 3.0.0-rc.6.

## Einfach erklärt – Beispiel aus Bärstadt

Stellen wir uns vor, der Bären-Verkehrsbund arbeitet nach etiCORE. Dann ist der BVV das Product-Owner-System, die Bärstädter Verkehrsbetriebe sind ein CCP, und weil sie auch Aktionen am Terminal ausführen, ein eCCP.

Pia soll ihr ABO Azubi bekommen. Bodo Bärlauch im Kundencenter am Honigmarkt gibt den Auftrag auf: Das ist `orderEntitlementIssuance`. Er liegt jetzt beim BVV.

Damit das Lesegerät T-4712 am Hauptbahnhof ihn kennt, holt das Hintergrundsystem der BVB die Aktionsliste beim BVV ab. Nach dem ersten Mal fragt es nur noch, was seit der zuletzt erhaltenen Liste dazugekommen ist. Das spart Daten, birgt aber ein Risiko: Geht dabei etwas verloren, fehlt später ein Auftrag. Deshalb fragt die BVB mit einem Prüfwert nach, ob ihr Bestand mit der Gesamtliste übereinstimmt. Es ist wie das Nachzählen der Kasse am Abend.

Pia hält ihre BärenKarte ans Gerät. Es findet den Auftrag auf seiner Liste und schreibt die Berechtigung auf die Karte. Danach meldet die BVB dem BVV: ausgeführt. Der BVV gibt die Meldung an den weiter, der bestellt hat.

Zieht Pia die Karte zu früh ab, bevor die Berechtigung dauerhaft geschrieben ist, geht beim BVV nur eine Abbruchmeldung ein, damit er das im Blick behält.

Hätte Bodo sich beim Bestellen vertan, würde er den Auftrag mit `cancelOrder` stornieren.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: WSDL `po-oa-management` (Operationen, Beschreibungen), `po-oa-management-messaging_xsd` (Elemente `orderGroup`, `verifyActionListUpdatedViaIncrements`, `listVerificationInformation`)
- [Q49](../../QUELLEN.md#q49) – etiCORE Specification, Glossar, Eintrag *Ordered action*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 19

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Aktionsliste](aktionsliste.md) – die Liste in der KA 1.x
- [Aktionsdifferenzliste](aktionsdifferenzliste.md) – die inkrementelle Liste
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md) – die Namen der KA 1.x
- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md) – CCP, PO und eCCP

<!-- GEN:siehe_auch -->
## Siehe auch

- [Aktionsliste](aktionsliste.md) (TXAML)
- [Aktionsdifferenzliste](aktionsdifferenzliste.md)
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md)
- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
