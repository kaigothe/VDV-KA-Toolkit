---
titel: txalisber
englisch: alise entitlement transaction
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/txaml.md, lexikon/aktionsmanagement/auftragstyp.md]
quellen: [Q06, Q11, Q25]
status: zu prüfen
offene_fragen: [O4, O14]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › txalisber
<!-- /GEN:breadcrumb -->

# txalisber

`txalisber` ist der Name eines XML-Elements, das in einer ausgewerteten ALISE-Nachricht auftritt. Es trägt den Namespace `http://vdv/ka/alise/2` und enthält einen Aktionslisteneintrag für eine Berechtigung ([Q11](../../QUELLEN.md#q11)).

**Die Nachricht ist in den öffentlichen Quellen nicht dokumentiert** (zu prüfen). [Q06](../../QUELLEN.md#q06) nennt sie nicht; dort heißt die Aktionsliste [`TXAML`](txaml.md) ([Q06](../../QUELLEN.md#q06), Kap. 4.3.1).

Aus dem Namen liegt die Lesart „ALISE-Eintrag Berechtigung“ nahe (abgeleitet). Wie sich `txalisber` zu `TXAML` verhält, ist offen: ob es ein Element **innerhalb** einer `TXAML` ist, eine eigene Nachricht der ALISE-Schnittstelle oder eine verbund- bzw. herstellerspezifische Variante (zu prüfen, O14).

Zur **Versionszuordnung** gibt es eine belegte Konvention: [Q25](../../QUELLEN.md#q25), Kap. 4.3.3, definiert den Namensraum in EBNF, endend auf `NamensraumBereich, ["types"], "/", Version`. Die letzte Pfadstelle ist also eine **Version**, nicht ein Release. Dazu Kap. 4.3.1.4: „Innerhalb einer Version sind die Releases hinsichtlich des gemeinsamen Namensraumes kompatibel“; unterstützt werden nur zwei Versionen (Kap. 4.3.1.3).

Die `2` in `http://vdv/ka/alise/2` ist damit sehr wahrscheinlich die **Namensraum-Version** (abgeleitet). Auf das KA-Release — 1.1.07, 1.3.0 oder neuer — lässt sich daraus weiterhin **nicht** schließen, weil mehrere Releases denselben Namensraum teilen (zu prüfen, O4).

Die Bereichsliste derselben Konvention nennt `pv-alise` und `kvp-alise`, die WSDL-Bereiche entsprechend `PV_ALISE` und `KVP_ALISE` ([Q25](../../QUELLEN.md#q25), Kap. 4.3.2 f.). Es gibt also **zwei** ALISE-Schnittstellen, was die Frage nach der Zuordnung von `txalisber` verschärft (zu prüfen, O14).

Das Präfix `am…` mehrerer Felder (`amAuftragsTyp`, `amAenderungsreferenz_ID`, `amTerminalGruppe_ID`) liest sich als Aktionsmanagement-Merkmal (abgeleitet).

**Dieser Artikel ist der Ausgangspunkt des geplanten Analysewerkzeugs** und gleichzeitig seine größte Lücke.

## Einfach erklärt – Beispiel aus Bärstadt

`txalisber` ist der Name, mit dem die Nachricht beginnt, die dieses ganze Projekt angestoßen hat. Und ausgerechnet über ihn ist am wenigsten bekannt.

Was man sieht, ist die erste Zeile:

```xml
<ns:txalisber xmlns:ns="http://vdv/ka/alise/2">
```

Zwei Dinge stehen darin. Der Elementname `txalisber` und ein Namensraum, der auf ALISE verweist — den Dienst, der Aktionslisten bereitstellt.

Den Namen kann man zerlegen: `tx` für Transaktion, `alis` für ALISE, `ber` für Berechtigung. Das ergibt „ALISE-Eintrag für eine Berechtigung“, und zum Inhalt passt es gut: Die Nachricht beschreibt genau einen Auftrag für genau eine Karte.

Nur steht das so in keiner öffentlichen Unterlage. Das Pflichtenheft des eTicket RheinMain, sonst die ergiebigste Quelle, kennt `txalisber` nicht. Dort heißt die Aktionsliste `TXAML`.

Daraus folgt eine ehrliche offene Frage: Ist `txalisber` ein einzelner Eintrag **innerhalb** einer `TXAML`? Eine eigene Nachricht der ALISE-Schnittstelle? Oder etwas, das ein Hersteller für sein System gebaut hat? Alle drei Möglichkeiten passen zu dem, was man sieht.

Und noch eine Falle: Die `2` am Ende des Namensraums sieht wie eine Versionsnummer aus. Sie ist aber einfach Teil des Namens. Daraus auf „VDV-KA Version 2“ zu schließen, wäre falsch — die hier relevanten Releases heißen 1.1.07, 1.3.0 und 1.5.0.

Für das geplante Werkzeug ist das die wichtigste Erkenntnis dieses Lexikons. Man kann eine solche Nachricht öffnen, ihre Struktur anzeigen und viele Felder erklären. Aber man kann sie nicht gegen ein Schema prüfen, das man nicht hat. Deshalb muss das Werkzeug von Anfang an sagen können: Das weiß ich, das schließe ich, und das weiß ich nicht.

## Quellen

- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht: Elementname, Namespace `http://vdv/ka/alise/2`, Felder mit dem Präfix `am…`. **Nicht öffentliche Unterlage**; übernommen sind nur Elementname, Namespace und Feldnamen.
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.3.1 (die Aktionsliste heißt dort `TXAML`; `txalisber` wird nicht genannt) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 4.3.1.3 f. (nur zwei Versionen gleichzeitig; Releases innerhalb einer Version über den gemeinsamen Namensraum kompatibel), Kap. 4.3.2 f., PDF-S. 114 f. (EBNF der Dateinamen- und Namensraumkonvention; `NamensraumBereich` mit `pv-alise` und `kvp-alise`, WSDL-Bereiche `PV_ALISE` und `KVP_ALISE`; Namensraum endet auf eine Version)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
