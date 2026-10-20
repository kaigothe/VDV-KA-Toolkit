---
titel: Aktionsfreigabe
englisch: action release
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/kontrolle/sperranforderung.md, lexikon/aktionsmanagement/aktion.md, lexikon/aktionsmanagement/aktionsliste.md, lexikon/rollen/alise.md, lexikon/transaktionen/nachrichten-in-ka-1-x-und-eticore.md]
quellen: [Q02, Q25, Q39, Q40, Q49, Q50, Q55]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 141
    codeliste: IONTransaktionsTyp_CODE
    bedeutung: TXAFREIBER — Aktionsfreigabeauftrag
    quelle: Q55
    fundstelle: Kap. 6.2.5 (S. 75)
    status: belegt
    verbundspezifisch: false
  - wert: 142
    codeliste: IONTransaktionsTyp_CODE
    bedeutung: TXAFREIMITBER — Aktionsfreigabemitteilung
    quelle: Q55
    fundstelle: Kap. 6.2.6 (S. 75)
    status: belegt
    verbundspezifisch: false
  - wert: 9
    codeliste: AblehnungsTyp_CODE
    bedeutung: Referenz nicht vorhanden — Ablehnung, wenn der freizugebende Auftrag nicht mehr im Bestand des ALISE ist
    quelle: Q55
    fundstelle: Kap. 4.2.2.3, Fußnote 66 (S. 48)
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktionsfreigabe
<!-- /GEN:breadcrumb -->

# Aktionsfreigabe

Mit dem Aktionsfreigabeauftrag `TXAFREIBER` erhält der beauftragende Kundenvertragspartner „ein Steuerungsinstrument zur Veranlassung der Entfernung eines von ihm beauftragten Aktionsauftrages vor Ablauf dessen Gültigkeit“ beim ALISES des Produktverantwortlichen, der ihn aus dem Aktionslistenbestand entfernt oder einen Löschauftrag für betroffene Aktionsdifferenzlisten erstellt ([Q55](../../QUELLEN.md#q55), Kap. 4.2.2.3, S. 48).

Die Freigabe bezieht sich damit auf den **Auftrag**, nicht auf die Berechtigung. Sie löst beim Produktverantwortlichen denselben Prozess aus wie eine Aktion, die durch Gültigkeitsende zu entfernen ist.

**Sie ist nur für Entsperrungen zugelassen:** „Er wird nur für die Freigabe einer Entsperrung zugelassen.“ Für Ausgabe und Rücknahme ist sie ausdrücklich ausgeschlossen — wegen der rechtlichen Folgen gegenüber dem Kunden, wegen des Risikos, dass eine freigegebene Ausgabe zwischen Freigabe und Listenaktualisierung doch noch ausgeführt wird, und weil nach der Freigabe einer Ausgabe zusätzlich ein Sperrfreigabeauftrag nötig wäre ([Q55](../../QUELLEN.md#q55), Kap. 4.2.2.3, S. 48 f.).

**Der Anwendungsfall:** Eine Rücknahme wurde ausgeführt, ohne dass der vorher beauftragte Entsperrauftrag zur gleichen Berechtigung ausgeführt wurde — er trägt eine um eins kleinere [berSynchronNummer](../berechtigungen/bersynchronnummer.md). Da die übersprungene Entsperrung keinen Transaktionsnachweis erzeugt, bliebe sie bis zum Gültigkeitsende im Bestand.

**Bestätigt wird mit `TXB`**, nicht mit der Aktionsfreigabemitteilung. Existiert der freizugebende Auftrag nicht mehr, folgt eine Ablehnung `TXA` mit `AblehnungsTyp_CODE` 9.

**`TXAFREIMITBER` gehört zum Aktionsclearing.** Damit meldet der Produktverantwortliche, dass er einen Auftrag entfernt hat, dessen Ausführung über einen Kontrollnachweis `TXEBER` oder Sperrnachweis `TXSNAWB` statt über einen Transaktionsnachweis belegt war ([Q55](../../QUELLEN.md#q55), Kap. 4.2.4, S. 49; Kap. 6.4.5.1, S. 96). Die aus [Q39](../../QUELLEN.md#q39) gewonnene Lesart, sie sei die Antwort auf `TXAFREIBER`, gilt für den Standard **nicht**.

## Einfach erklärt – Beispiel aus Bärstadt

Pia hat ihre BärenKarte verloren gemeldet, das Abo wurde gesperrt. Zwei Tage später findet sie die Karte in der Jackentasche. Bodo Bärlauch im Kundencenter beauftragt die Entsperrung — der Auftrag geht an den Aktionslistenservice und wartet dort, bis Pia das nächste Mal an ein Terminal kommt.

Sie kommt nicht. Stattdessen entscheidet sie sich für ein anderes Produkt, und die Bärstädter Verkehrsbetriebe nehmen das alte Abo zurück. Diese Rücknahme wird am Automaten ausgeführt — und überspringt dabei die noch offene Entsperrung.

Jetzt liegt im Auftragsbestand eine Entsperrung, die niemand mehr ausführen wird. Sie wird auch nicht von selbst verschwinden: Aufträge werden aus dem Bestand entfernt, wenn ein Ausführungsnachweis eintrifft oder wenn ihre Gültigkeit abläuft. Beides passiert hier nicht zeitnah. Bis dahin schleppt jede Aktionsliste einen toten Eintrag mit.

**Dafür ist die Aktionsfreigabe da.** Die BVB merken die Lücke, wenn der Nachweis der Rücknahme eintrifft: Sein Zähler ist um eins höher als der der Entsperrung, die nie bestätigt wurde. Also schicken sie eine Nachricht an den Aktionslistenservice: Dieser Auftrag ist freizugeben. Der Service nimmt ihn aus dem Bestand, und der Verkehrsbund bestätigt das.

**Warum „Freigabe“ und nicht „Stornierung“?** Weil die KA das Wort anders benutzt, als man zunächst denkt. Freigeben heißt hier: etwas aus einer Bindung lösen. Bei einer Sperre ist das offensichtlich — ein Sperrfreigabeauftrag hebt die Sperre auf. Bei einem Auftrag ist es dasselbe Muster: Die Berechtigung wird von dem Auftrag freigegeben, der auf ihr liegt.

Wer das Wort im Alltagssinn liest, kommt auf die umgekehrte Bedeutung — „der Auftrag wird zur Ausführung freigegeben“ — und damit auf das Gegenteil. Das ist eine der Stellen, an denen die KA-Begriffe eine Falle stellen.

**Und jetzt der Teil, der überrascht.** Man würde erwarten, dass sich jeder Auftrag so zurückziehen lässt. Das ist nicht so: Die Freigabe gilt **nur für Entsperrungen**. Eine beauftragte Ausgabe lässt sich nicht freigeben, eine Rücknahme auch nicht.

Die Spezifikation begründet das, und die Begründung ist einleuchtend. Eine Ausgabe hängt an einer Zahlung; wer sie zurückzieht, muss das dem Kunden gegenüber vertreten. Vor allem aber: Zwischen der Freigabe und dem Zeitpunkt, an dem die Terminals ihre neue Liste haben, liegt Zeit. In dieser Zeit könnte die Ausgabe doch noch ausgeführt werden — und dann bräuchte man zusätzlich eine Rücknahme. Man hätte also nichts gewonnen, sondern einen Zustand, über den niemand mehr sicher Auskunft geben kann.

Bei einer Entsperrung ist der Schaden im Zweifel klein: Wird sie doch noch ausgeführt, ist eine Berechtigung entsperrt, die gleich danach ohnehin zurückgenommen wird.

Für ein Prüfwerkzeug ist das eine klare Regel: Ein Aktionsfreigabeauftrag, der sich auf eine Ausgabe oder eine Rücknahme bezieht, ist nach dem Standard unzulässig — und einer, dessen Auftrag gar nicht mehr im Bestand liegt, bekommt eine Ablehnung.

## Quellen

- [Q55](../../QUELLEN.md#q55) – KA AktM-SPEC 1.12.0, Kap. 4.2.2.3 (S. 48 f.): Definition des Aktionsfreigabeauftrags `TXAFREIBER` als Steuerungsinstrument des BKVP zur Entfernung eines eigenen Aktionsauftrags vor Ablauf der Gültigkeit; Bestätigung mit `TXB`; Ablehnung `TXA` mit `AblehnungsTyp_CODE` 9; Beschränkung „Er wird nur für die Freigabe einer Entsperrung zugelassen“ samt drei Begründungen; Anwendungsfall der übersprungenen Entsperrung. Kap. 4.2.4 (S. 49) und Kap. 6.4.5.1 (S. 96): `TXAFREIMITBER` als Nachricht des Aktionsclearings. Kap. 6.2.5 und 6.2.6 (S. 75): neue `IONTransaktionsTyp_CODE` 141 und 142. Exzerpt: [exzerpte/Q55.md](../../exzerpte/Q55.md) · *nicht öffentlich*
- [Q39](../../QUELLEN.md#q39) – RMV vHGS-Vertrag, Anlage 6 „Konzept Externer Mandant“, Kap. 3.2.5 (PDF-S. 52 f.): `TXAFREIBER` und `TXAFREIMITBER` mit Richtung, beide asynchron · *verbundspezifisch: eTicket RheinMain*; Kap. 3.2.1 f. (PDF-S. 50 f.): `TXSAUFB` und `TXSFREIB`, `TXSAUFA` und `TXSFREIA`
- [Q40](../../QUELLEN.md#q40) – KCD NRW, Rahmenlastenheft DL-System v2.4, PDF-S. 16 und PDF-S. 20: Sperrfreigabeauftrag und Sperraufhebungsanforderung als Paar · *verbundspezifisch: NRW*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 87 f.: Sperrfreigabeauftrag als Auftrag, „ein Objekt von der jeweiligen Sperrliste zu nehmen“; **kein** Eintrag „Aktionsfreigabe“
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2, Kap. 5.1.2, Tabelle 38 (Anlagenseite 95, PDF-S. 239): Anwendungsfälle „Aktionsfreigabe senden“ und „Aktionsfreigabemitteilung entgegennehmen“
- [Q49](../../QUELLEN.md#q49) – etiCORE-Spezifikationsmodell, *Ordered action management › Ordering › Cancel order*: Markierung als storniert und Entfernen aus der nächsten Aktionsliste
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management-messaging_xsd`, Element `cancelOrder` mit `meta:old` = `TXAFREIBER` · *Release-Kandidat*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Sperranforderung](../kontrolle/sperranforderung.md)
- [Aktion](aktion.md)
- [Aktionsliste](aktionsliste.md) (TXAML)
- [Aktionslistenservice](../rollen/alise.md) (ALISE)
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
