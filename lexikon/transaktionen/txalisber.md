---
titel: txalisber
englisch: alise entitlement transaction
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/txaml.md, lexikon/aktionsmanagement/auftragstyp.md]
quellen: [Q06, Q11, Q25, Q50, Q55]
status: zu prüfen
offene_fragen: [O4]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › txalisber
<!-- /GEN:breadcrumb -->

# txalisber

`txalisber` ist der Name eines XML-Elements, das in einer ausgewerteten ALISE-Nachricht auftritt. Es trägt den Namespace `http://vdv/ka/alise/2` und enthält einen Aktionslisteneintrag für eine Berechtigung ([Q11](../../QUELLEN.md#q11)).

**Was es ist, ist belegt.** Die KA AktM-SPEC führt `TXALISBER`, `TXRLISBER` und `TXELISBER` als „Datensatzbeschreibung zur Ausgabe, Rücknahme und Entsperrung einer Berechtigung in allen Aktionslisten über das Aktionsmanagement“ und ergänzt für sie die `NmTransaktionsTyp_CODE` 37, 38 und 39 ([Q55](../../QUELLEN.md#q55), Kap. 6.2.3.1, S. 67). `txalisber` ist damit ein **Eintrag** in einer Aktionsliste, keine eigene Nachricht. Die Liste selbst ist die [`TXAML`](txaml.md) mit `IONTransaktionsTyp_CODE` 137, komprimiert 183; sie wird vom KVP-System beim PV-System abgefordert.

Das deckt sich mit etiCORE: Dort führt `TXALISBER_Type` auf den Typ `EntitlementIssuanceActionListEntry`, also ebenfalls einen Listeneintrag ([Q50](../../QUELLEN.md#q50), `po-oa-management_xsd`). [Q06](../../QUELLEN.md#q06) kennt den Namen nicht und nennt nur die [`TXAML`](txaml.md) (Kap. 4.3.1).

Zur **Versionszuordnung** gilt eine belegte Konvention: [Q25](../../QUELLEN.md#q25), Kap. 4.3.3, lässt den Namensraum auf eine **Version** enden, nicht auf ein Release; innerhalb einer Version sind die Releases hinsichtlich des Namensraums kompatibel (Kap. 4.3.1.4). Die `2` in `http://vdv/ka/alise/2` ist damit die Namensraum-Version (abgeleitet). Auf das KA-Release lässt sich daraus **nicht** schließen (zu prüfen, O4).

Die Bereichsliste nennt `pv-alise` und `kvp-alise`, die WSDL-Bereiche `PV_ALISE` und `KVP_ALISE` ([Q25](../../QUELLEN.md#q25), Kap. 4.3.2 f.) — es gibt also **zwei** ALISE-Schnittstellen.

Das Präfix `am…` mehrerer Felder (`amAuftragsTyp`, `amAenderungsreferenz_ID`, `amTerminalGruppe_ID`) liest sich als Aktionsmanagement-Merkmal (abgeleitet).


## Einfach erklärt – Beispiel aus Bärstadt

`txalisber` ist der Name, mit dem die Nachricht beginnt, die dieses ganze Projekt angestoßen hat. Und ausgerechnet über ihn ist am wenigsten bekannt.

Was man sieht, ist die erste Zeile:

```xml
<ns:txalisber xmlns:ns="http://vdv/ka/alise/2">
```

Zwei Dinge stehen darin. Der Elementname `txalisber` und ein Namensraum, der auf ALISE verweist — den Dienst, der Aktionslisten bereitstellt.

Den Namen kann man zerlegen: `tx` für Transaktion, `alis` für ALISE, `ber` für Berechtigung. Das ergibt „ALISE-Eintrag für eine Berechtigung“, und zum Inhalt passt es gut: Die Nachricht beschreibt genau einen Auftrag für genau eine Karte.

Nur steht das so in keiner öffentlichen Unterlage. Das Pflichtenheft des eTicket RheinMain, sonst die ergiebigste Quelle, kennt `txalisber` nicht. Dort heißt die Aktionsliste `TXAML`.

Einen Hinweis liefern die etiCORE-Schnittstellen: Dort heißt der Typ `EntitlementIssuanceActionListEntry` und trägt `TXALISBER_Type` als Altnamen. Das klingt nach einem einzelnen Eintrag in einer Liste.

Daraus bleibt für die KA 1.x eine ehrliche offene Frage: Ist `txalisber` ein einzelner Eintrag **innerhalb** einer `TXAML`? Eine eigene Nachricht der ALISE-Schnittstelle? Oder etwas, das ein Hersteller für sein System gebaut hat? Alle drei Möglichkeiten passen zu dem, was man sieht.

Und noch eine Falle: Die `2` am Ende des Namensraums sieht wie eine Versionsnummer aus. Sie ist aber einfach Teil des Namens. Daraus auf „VDV-KA Version 2“ zu schließen, wäre falsch — die hier relevanten Releases heißen 1.1.07, 1.3.0 und 1.5.0.

Für das geplante Werkzeug ist das die wichtigste Erkenntnis dieses Lexikons. Man kann eine solche Nachricht öffnen, ihre Struktur anzeigen und viele Felder erklären. Aber man kann sie nicht gegen ein Schema prüfen, das man nicht hat. Deshalb muss das Werkzeug von Anfang an sagen können: Das weiß ich, das schließe ich, und das weiß ich nicht.

## Quellen

- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht: Elementname, Namespace `http://vdv/ka/alise/2`, Felder mit dem Präfix `am…`. **Nicht öffentliche Unterlage**; übernommen sind nur Elementname, Namespace und Feldnamen.
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.3.1 (die Aktionsliste heißt dort `TXAML`; `txalisber` wird nicht genannt) · *verbundspezifisch: eTicket RheinMain*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management_xsd`: Typen `EntitlementIssuanceActionListEntry`, `EntitlementUnblockingActionListEntry`, `EntitlementTerminationActionListEntry` mit `meta:old` · *Release-Kandidat*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 4.3.1.3 f. (nur zwei Versionen gleichzeitig; Releases innerhalb einer Version über den gemeinsamen Namensraum kompatibel), Kap. 4.3.2 f., PDF-S. 114 f. (EBNF der Dateinamen- und Namensraumkonvention; `NamensraumBereich` mit `pv-alise` und `kvp-alise`, WSDL-Bereiche `PV_ALISE` und `KVP_ALISE`; Namensraum endet auf eine Version)

<!-- GEN:siehe_auch -->
## Siehe auch

- [TXAML](txaml.md)
- [Auftragstyp](../aktionsmanagement/auftragstyp.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
