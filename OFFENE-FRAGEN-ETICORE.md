# Offene Fragen zur Abbildung KA 1.x ↔ etiCORE

**Stand:** 2026-10-20 · **Zweck:** Abstimmung mit einem zweiten Bearbeiter oder Agenten, der Zugriff auf weitere Unterlagen hat. Jede Frage ist für sich lesbar. Die Nummern O1 bis O20 sind die aus [PLAN.md](PLAN.md), Abschnitt 5; F-Nummern sind neu.

**Anlass:** Die Schnittstellendokumentation der etiCORE-Spezifikation 3.0.0-rc.6 ([Q50](QUELLEN.md#q50)) nennt an rund 850 Elementen den Namen in der KA 1.x (`meta:old`). Die Namenstabelle steht in [exzerpte/Q50.md](exzerpte/Q50.md). Sie belegt, **welcher etiCORE-Name an die Stelle des alten tritt**, nicht, dass die Bedeutung gleich ist. Daraus entstehen die folgenden Fragen.

**Bitte so antworten:** Antwort, dann Beleg mit Dokument, Kapitel oder Seite und der Version. Verbundspezifisches bitte als solches kennzeichnen ([CLAUDE.md](CLAUDE.md), Regel 4). Ist etwas nur vermutet, bitte als Vermutung schreiben.

---

## F1 — Was ist die „Aktionsfreigabe“? (O20, berührt O12)

**Frage:** Ist `TXAFREIBER` in der KA 1.x die **Stornierung** eines Auftrags, oder gibt sie einen vorbereiteten Auftrag erst **frei**? *(Unsere Antwort nach eigener Prüfung: Stornierung — Begründung unten. Wir suchen die Bestätigung.)*

**Was wir wissen:**
- Eine **RMV**-Quelle ([Q39](QUELLEN.md#q39), Kap. 3.2.5, PDF-S. 52) nennt `TXAFREIBER` „Aktionsfreigabeauftrag“ des beauftragenden KVP an PV bzw. ALISE und `TXAFREIMITBER` „Aktionsfreigabemitteilung“ des ALISE zurück, beide asynchron. Die Kapitelüberschrift lautet „Aktionsmanagement RMV-EFS“. *(Eine frühere Fassung dieses Dokuments nannte Q39 eine NRW-Quelle — das war falsch.)* Das Glossar ([Q02](QUELLEN.md#q02)) kennt den Begriff nicht.
- In etiCORE trägt `cancelOrder` den Altbezeichner `TXAFREIBER` (Namensraum `http://vdv/ka/alise/2`). Es hat ein einziges Feld, `orderId` („Cancel an order“).
- `TXAFREIMITBER` ist der Altbezeichner von `notifyOrderSeemsToBeObsolete`: Meldung des PO-Systems an den bestellenden CCP, dass ein Entsperrauftrag auf anderer Grundlage (einer Inspektionsbescheinigung) erledigt scheint.
- Beide Richtungen passen zur Tabelle in [Q39](QUELLEN.md#q39).
- **Neu, und aus unserer Sicht entscheidend: Das Benennungsmuster der KA spricht für die Stornierung.** Im Sperrmanagement steht dem Sperrauftrag `TXSAUFB` der Sperrfreigabeauftrag `TXSFREIB` gegenüber, der NmApplikation entsprechend `TXSAUFA` und `TXSFREIA` ([Q39](QUELLEN.md#q39), Kap. 3.2.1 f., PDF-S. 50 f.). Eine „Freigabe“ nimmt dort zurück, was der Auftrag bewirkt hat. Ein **NRW**-Rahmenlastenheft bestätigt die Paarung ausdrücklich: Es nennt „Sperraufhebungsanforderungen“ und „die zugehörigen … Sperrfreigabemitteilungen“ in einem Satz ([Q40](QUELLEN.md#q40), PDF-S. 20) und führt Elementarprozesse `EP_Sperrfreigabeauftrag_*` neben `EP_Sperraufhebungsanforderung_*` ([Q40](QUELLEN.md#q40), PDF-S. 16). „Freigabe“ heißt in dieser Begriffswelt also **Aufhebung**, nicht Erlaubnis.
- **Vierter Beleg aus etiCORE:** Dieselbe Spezifikation bildet `TXSAUFB` auf `addEntitlementToHotlist` und `TXSFREIB` auf `removeEntitlementFromHotlist` ab („Removes the entry … from the hotlist“, [Q50](QUELLEN.md#q50), `hotlist-messaging_xsd`). Die Sperrfreigabe ist dort also das Entfernen eines Eintrags.
- Unser Artikel [aktionsfreigabe.md](lexikon/aktionsmanagement/aktionsfreigabe.md) führt die Freigabe deshalb jetzt als **Rücknahme eines noch nicht ausgeführten Auftrags** (abgeleitet). Die frühere Lesart — ein Schritt, der einen Auftrag „wirksam werden“ lässt — ist aufgegeben: Sie stützte sich allein auf den Alltagssinn des Wortes.

**Was wir brauchen:** die Beschreibung der Nachricht in der KA AktM-SPEC (oder SST-SPEC), mit Feldliste, und wenn möglich ein Beispiel. Die Frage ist damit **nicht mehr offen in beide Richtungen** — gesucht ist die Bestätigung, dass `TXAFREIBER` einen Auftrag zurücknimmt, und die Auskunft, worauf sich die Freigabe bezieht: auf den Auftrag selbst oder auf die Berechtigung, die er betrifft.

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

## Antworten (vorläufig, aus der etiCORE-Kopie)

**Wichtig beim Lesen:** Die Antworten beruhen auf der **etiCORE-Spezifikation 3.0.0-rc.6** ([Q49](QUELLEN.md#q49), [Q50](QUELLEN.md#q50)). Sie belegen, was etiCORE festlegt und welche Altnamen es nennt. Ob die KA 1.x dasselbe meint, ist jeweils eigens vermerkt. Die Spalte „Gilt für KA 1.x“ trennt das.

| Frage | Antwort | Beleg | Gilt für KA 1.x |
|---|---|---|---|
| **F1** | **Teilweise.** Der etiCORE-Nachfolger von `TXAFREIBER` storniert einen Auftrag: Er wird „im Auftragsbestand als storniert markiert und aus der nächsten Aktionsliste entfernt“. Der Nachfolger von `TXAFREIMITBER` meldet dem bestellenden CCP, dass ein Entsperrauftrag auf anderer Grundlage erledigt scheint; das Modell kennt dafür die Aktion „Mark order as obsolete“. „Freigabe“ meint danach vermutlich, einen Auftrag **aus der Aktionsliste herauszunehmen**, nicht ihn wirksam zu machen. Dazu passt, dass dieselbe Spezifikation `TXSFREIB` als `removeEntitlementFromHotlist` abbildet. | Q49, Modell: Layer 3, *Ordered action management › Ordering › Cancel order › Handle order cancellation* (Artifact-Text). Q50, `po-oa-management-messaging_xsd` (`cancelOrder`, `meta:old` = `TXAFREIBER`); `ccp-oa-ordering-messaging_xsd` (`notifyOrderSeemsToBeObsolete`, `meta:old` = `TXAFREIMITBER`) | **Nicht bestätigt.** Der Name der Altnachricht ist belegt, ihre Beschreibung in der KA 1.x nicht (abgeleitet). |
| **F2** | **Teilweise.** `amAuftragsTyp` unterscheidet die Auftragsarten. In etiCORE entfällt das Feld in den Listeneinträgen für Ausgabe, Entsperrung und Rücknahme mit der Begründung „clear from context“: Der Typ des Eintrags trägt die Information. Ein vierter Eintragstyp, *Blocking*, hat keinen Altnamen. **Der Wert 13 ist damit nicht aufgelöst.** In `EntitlementIssuanceActionListEntry` entfällt zugleich `logTransaktionsTyp`, das in unserer Beispielnachricht 37 (Ausgabe) ist. Das stützt, dass 13 zur Ausgabe gehört (abgeleitet). | Q50, `po-oa-management_xsd`, Typen `EntitlementIssuanceActionListEntry`, `…UnblockingActionListEntry`, `…TerminationActionListEntry`, `meta:deleted` | Wert: **offen**. Funktion: abgeleitet. |
| **F3** | **Teilweise.** `TXALISBER_Type`, `TXELISBER_Type` und `TXRLISBER_Type` sind Altnamen der Typen der **Listeneinträge** für Ausgabe, Entsperrung und Rücknahme. Danach ist `txalisber` ein Eintrag einer Aktionsliste. Ob die `TXAML` ihn enthält, steht dort nicht. | Q50, `po-oa-management_xsd` | Abgeleitet. |
| **F4** | **Nicht beantwortet.** Die Endungen `_1_3_0` und `_1_7_1` erscheinen als Altnamen (`TXASAMDL_1_3_0`, `TXAML_1_7_1` u. a.); die Spezifikation erklärt sie nicht. | Q50, Altnamen im Namensraum `http://vdv/ka/alise/2` | — |
| **F5** | **Ja, in den Listeneinträgen.** Die XSDs ordnen auch Felder zu, siehe die Tabelle unten. Außerhalb der Aktionsliste haben wir sie nicht vollständig ausgewertet. Die Migrationsdokumente (Q43, Kap. 7.1) liegen uns nicht vor. | Q50, `po-oa-management_xsd` | Zuordnung der Namen belegt; Bedeutung in der KA 1.x abgeleitet. |
| **F6** | **Nicht beantwortet.** `logTransaktionsTyp` entfällt in Listeneinträgen („clear from context“) und in mehreren Aktionen („Action parameter obsolete“). Eine Codeliste mit Werten steht in der Kopie nicht. | Q50 | — |
| **F7** | **Ja, etiCORE übernimmt die Rollencodes.** Die WSDLs nennen als Rolle (dezimal): CCP **1**, SO **2**, PO **3**, ESH **4**, Hotlist Service **5**, CRE **254**. Das entspricht den Codes der KA 1.x für KVP 1, DL 2, PV 3, AH 4 und KOSE 5. Eine Rolle 31 für ALISE kommt **nicht** vor; die Aktionsmanagement-Schnittstelle hat die **3**. | Q50, WSDL-Köpfe aller Schnittstellen (*Role (decimal representation)*) | Stützt K1 in PLAN.md (Rolle 3 statt 31). Die Zuordnung ESH ↔ 4 (in der KA 1.x der AH) ist offen. |
| **F8** | **Nicht beantwortet.** Stand der Kopie ist rc.6; ob es eine Endfassung gibt, haben wir nicht geprüft. | Q49 | — |

### Feldzuordnung in den Listeneinträgen (zu F5)

| Name in der KA 1.x | etiCORE | Beschreibung in etiCORE |
|---|---|---|
| `tx_identam` (Typ `TX_IDENTAM_Type`) | `actionListEntryBaseInformation` | Basisinformation aller Listeneinträge |
| `appInstanz_ID` | `umAppInstanceId` | App-Instanz des Mediums, für das der Eintrag gilt |
| **`amAenderungsreferenz_ID`** | **`groupId`** (Organisations-ID des bestellenden CCP und Gruppennummer) | „Logically groups action list entries to be executed in a single transaction“; optional |
| `berBerechtigung_ID` und `berSynchronNummer` | `orderId` (bestellender CCP und Auftragsnummer) | „Uniquely identifies the underlying order“ |
| `logTransaktionsOperator_ID` | `actionOperator` | „Action operator to be used for action execution within terminal action data“ |
| `prodProdukt_ID` | `productId` | Produkt (im Eintrag für die Ausgabe) |
| `berGueltigkeitsbeginn` und `berGueltigkeitsende` | `entitlementEffectiveTime` und `entitlementExpirationTime` | Beginn und Ende der Gültigkeit |
| `berProduktspezTeil` | `productParameters` (daneben `storedValueParameters`, `storedValueAutoloadParameters`) | produktspezifischer Teil |
| `berInfoText` | `infotext` | Klartext |
| `berBerechtigung_ID` (Entsperrung, Rücknahme) | `entitlementId` | Berechtigung |
| `berSynchronNummer` (Entsperrung) | `entitlementTransitionCounter` | „Increasing sequence number which indicates if an entitlement's state has been changed. Each state transition causes an increasing of the counter.“ (ASN.1, Modul `user-medium`) |

**Entfallene Felder** (`meta:deleted`): `amAuftragsTyp` und `logTransaktionsTyp` („clear from context“), `amTerminalGruppe_ID` und `amTerminal_ID` („CR353“, vermutlich eine Änderungsanforderung), `berStatus` („determined by UM, not by terminal“), `prodKeyOrganisation_ID` („Erfassungsschlüssel obsolete“), die Schlüsselkennungen `amMK…-NM-MAC_ID` („Schlüssel obsolete“).

### Funde, die Sie gegenprüfen sollten

- **G1 — Änderungsreferenz (O13).** Unser Artikel liest `amAenderungsreferenz_ID` als Verweis auf die **Vorgänger-Berechtigung**. etiCORE führt das Feld auf eine **Gruppe** zurück (`groupId`: bestellender CCP plus Gruppennummer). Das passt zu den zwei Teilen des Werts „0 / 0“ in unserer Beispielnachricht und würde „keine Gruppe“ bedeuten. Bitte prüfen: Bezeichnet die Änderungsreferenz in der KA 1.x eine Gruppe von Aktionen, die gemeinsam ausgeführt werden (etwa Austausch einer Karte als Rücknahme plus Ausgabe)?
- **G2 — Synchronnummer (O5).** `berSynchronNummer` entspricht in etiCORE dem `entitlementTransitionCounter`: Jeder Zustandswechsel erhöht ihn. Bitte prüfen, ob das für die KA 1.x ebenso gilt.
- **G3 — Terminalgruppen (K3 in PLAN.md).** Die Felder `amTerminalGruppe_ID` und `amTerminal_ID` entfallen, passend zu „in etiCORE erhält jeder ausführende CCP dieselbe Liste“ ([Q02](QUELLEN.md#q02), S. 19).

*Die vollständige Zuordnung (rund 850 Paare) liegt nur lokal; die Namen zu Aktionsmanagement und Hotlist stehen in [exzerpte/Q50.md](exzerpte/Q50.md).*
