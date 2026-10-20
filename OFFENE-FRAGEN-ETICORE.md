# Offene Fragen zur Abbildung KA 1.x ↔ etiCORE

**Stand:** 2026-10-20 · **Zweck:** Abstimmung mit einem zweiten Bearbeiter oder Agenten, der Zugriff auf weitere Unterlagen hat. Jede Frage ist für sich lesbar. Die Nummern O1 bis O20 sind die aus [PLAN.md](PLAN.md), Abschnitt 5; F-Nummern sind neu.

**Anlass:** Die Schnittstellendokumentation der etiCORE-Spezifikation 3.0.0-rc.6 ([Q50](QUELLEN.md#q50)) nennt an rund 850 Elementen den Namen in der KA 1.x (`meta:old`). Die Namenstabelle steht in [exzerpte/Q50.md](exzerpte/Q50.md). Sie belegt, **welcher etiCORE-Name an die Stelle des alten tritt**, nicht, dass die Bedeutung gleich ist. Daraus entstehen die folgenden Fragen.

**Bitte so antworten:** Antwort, dann Beleg mit Dokument, Kapitel oder Seite und der Version. Verbundspezifisches bitte als solches kennzeichnen ([CLAUDE.md](CLAUDE.md), Regel 4). Ist etwas nur vermutet, bitte als Vermutung schreiben.

---

## F1 — Was ist die „Aktionsfreigabe“? (O20, berührt O12)

**Frage:** Ist `TXAFREIBER` in der KA 1.x die **Stornierung** eines Auftrags, oder gibt sie einen vorbereiteten Auftrag erst **frei**?

**Was wir wissen:**
- Eine NRW-Quelle ([Q39](QUELLEN.md#q39), Kap. 3.2.5) nennt `TXAFREIBER` „Aktionsfreigabeauftrag“ des beauftragenden KVP an PV bzw. ALISE und `TXAFREIMITBER` „Aktionsfreigabemitteilung“ des ALISE zurück, beide asynchron. Das Glossar ([Q02](QUELLEN.md#q02)) kennt den Begriff nicht.
- In etiCORE trägt `cancelOrder` den Altbezeichner `TXAFREIBER` (Namensraum `http://vdv/ka/alise/2`). Es hat ein einziges Feld, `orderId` („Cancel an order“).
- `TXAFREIMITBER` ist der Altbezeichner von `notifyOrderSeemsToBeObsolete`: Meldung des PO-Systems an den bestellenden CCP, dass ein Entsperrauftrag auf anderer Grundlage (einer Inspektionsbescheinigung) erledigt scheint.
- Beide Richtungen passen zur NRW-Tabelle. Unser Artikel [aktionsfreigabe.md](lexikon/aktionsmanagement/aktionsfreigabe.md) führt die Freigabe bisher als Schritt, der einen Auftrag „wirksam werden“ lässt. Das ist eine Lesart aus dem Namen, nicht belegt.

**Was wir brauchen:** die Beschreibung der Nachricht in der KA AktM-SPEC (oder SST-SPEC), mit Feldliste, und wenn möglich ein Beispiel.

## F2 — Was bedeutet `amAuftragsTyp`? (O2, O9)

**Frage:** Welche Werte hat die Codeliste zu `amAuftragsTyp`, und steht 13 für „Ausgabe“?

**Was wir wissen:** In der ausgewerteten Beispielnachricht steht `amAuftragsTyp` = 13 neben `logTransaktionsTyp` = 37 (Ausgabe EFS über Aktionsliste, verbundspezifisch). Die Indizien sprechen für Ausgabe, belegt ist es nicht.

etiCORE modelliert die Aufträge als **eigene Operationen** (`orderEntitlementIssuance`, `…Unblocking`, `…Termination`, `…Blocking`), nicht als Wert eines Feldes. In den XSDs steht `amAuftragsTyp` unter `meta:deleted` der drei Listeneintrags-Typen, mit der Begründung „clear from context“. Der Auftragstyp ergibt sich dort also aus dem Typ des Eintrags.

**Was wir brauchen:** die Codeliste mit Werten und Bedeutung (KA BOM-SPEC oder AktM-SPEC), und die Klärung, ob „Aktion“, „Aktionstyp“ und „Auftragstyp“ Synonyme oder zwei Ebenen sind.

## F3 — Was ist `txalisber` in der KA 1.x? (O14)

**Frage:** Ist `txalisber` ein Eintrag **innerhalb** einer `TXAML`, oder eine eigene Nachricht?

**Was wir wissen:** In etiCORE heißen die Typen der Listeneinträge `EntitlementIssuanceActionListEntry`, `EntitlementUnblockingActionListEntry` und `EntitlementTerminationActionListEntry`. Ihre Altbezeichner sind `TXALISBER_Type`, `TXELISBER_Type` und `TXRLISBER_Type`. Das spricht für Listeneinträge. Für die KA 1.x ist es nicht belegt, [Q06](QUELLEN.md#q06) kennt `txalisber` nicht.

**Was wir brauchen:** das XSD zu `http://vdv/ka/alise/2` oder die AktM-SPEC, Abschnitt zur Aktionsliste.

## F4 — Welche KA-Release stehen hinter `_1_3_0` und `_1_7_1`? (O4)

**Frage:** Die Altbezeichner tragen Versionsendungen: `TXAML_1_7_1`, `TXAMDL_1_7_1`, `TXASAML_1_7_1`, `TXASAMDL_1_3_0`, `TXAMK_1_3_0`. Bezeichnen sie KA-Release (1.3.0, 1.7.1) oder Schnittstellenversionen?

**Was wir wissen:** Alle teilen den Namensraum `…/alise/2`. Nach [Q25](QUELLEN.md#q25), Kap. 4.3.3, ist die letzte Pfadstelle eine Version, und mehrere Releases teilen sie. Was die Endungen genau bedeuten, nennt die Quelle nicht.

**Was wir brauchen:** die Versionshistorie der Schnittstelle (Änderungsvermerke der AktM-SPEC oder der XSD).

## F5 — Gibt es eine Abbildung auf Feldebene? (neu)

**Frage:** Die XSDs ordnen Felder der KA 1.x über `meta:old` (umbenannt) und `meta:deleted` (entfallen, mit Grund) zu. Gibt es zusätzlich eine vollständige Feldzuordnung, etwa in den Migrationsdokumenten des Releases? Und gilt die Zuordnung auch für die KA 1.x selbst?

**Was wir wissen:** [Q43](QUELLEN.md#q43), Kap. 7.1, verweist auf Migrationsdokumente mit der „Gegenüberstellung der Anwendungsfälle“. In den Listeneinträgen fanden wir unter anderem `amAenderungsreferenz_ID` → `groupId`, `berBerechtigung_ID` und `berSynchronNummer` → `orderId` beziehungsweise `entitlementId` und `entitlementTransitionCounter`, `appInstanz_ID` → `umAppInstanceId`, `logTransaktionsOperator_ID` → `actionOperator`.

**Was wir brauchen:** diese Dokumente, oder die Auskunft, dass sie nicht öffentlich sind, und die Bestätigung, dass die Zuordnung die Bedeutung in der KA 1.x trifft.

## F6 — Gelten Transaktionstypen 37/38/39 KA-weit? (O1)

**Frage:** Sind 37 (Ausgabe), 38 (Entsperren) und 39 (Rücknahme) Werte des Standards oder des eTicket RheinMain?

**Was wir wissen:** Sie stammen aus einem Projektdokument ([Q06](QUELLEN.md#q06), Kap. 2.1.5, Fußnote 1). In den etiCORE-Schnittstellen entfällt `logTransaktionsTyp` in den Listeneinträgen („clear from context“) und in mehreren Aktionen („Action parameter obsolete“); eine Codeliste mit Werten fanden wir dort nicht.

**Was wir brauchen:** `NmTransaktionsTyp_CODE` aus der KA SST-SPEC oder BOM-SPEC.

## F7 — Rolle 3 und die Rollencodes (zu K1 in PLAN.md)

**Frage:** Das WSDL `po-oa-management` nennt als Rolle (dezimal) die **3**. Ist das derselbe Code wie der Rollencode 3 (PV) der KA 1.x?

**Was wir wissen:** [PLAN.md](PLAN.md), K1, belegt: In der TMS-Schnittstelle ab KA 1.3.0 ist für Transaktionen aus Aktionsausführungen zwingend der Rollencode 3 zu verwenden; 31 (ALISE) fällt weg. Die Rolle 3 im WSDL würde dazu passen.

**Was wir brauchen:** die Rollencodeliste der etiCORE-Spezifikation (Role Model) und ihren Bezug zur KA-1.x-Liste.

## F8 — Endfassung von etiCORE

**Frage:** Liegt inzwischen eine freigegebene Version 3.0.0 vor, und was hat sich gegenüber rc.6 geändert?

**Was wir wissen:** Alle Aussagen beruhen auf 3.0.0-rc.6 vom 24.11.2025, einem Release-Kandidaten ([Q43](QUELLEN.md#q43)). Der Start von etiCORE ist für den 1. Dezember 2026 angekündigt ([Q42](QUELLEN.md#q42), Sekundärquelle).

**Was wir brauchen:** den aktuellen Stand unter `modell.eticket-deutschland.de/LATEST/` und die Änderungsliste.

---

## Antworten

Hier tragen Sie die Antworten ein, je Frage in drei Zeilen: **Antwort · Beleg · Verbundspezifisch ja/nein**.

| Frage | Antwort | Beleg | Verbundspezifisch |
|---|---|---|---|
| F1 | | | |
| F2 | | | |
| F3 | | | |
| F4 | | | |
| F5 | | | |
| F6 | | | |
| F7 | | | |
| F8 | | | |
