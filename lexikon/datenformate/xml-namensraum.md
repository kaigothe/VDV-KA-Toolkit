---
titel: XML-Namensraum
englisch: XML namespace
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/xsd.md, lexikon/transaktionen/txalisber.md]
quellen: [Q11, Q25]
status: belegt
offene_fragen: [O4]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › XML-Namensraum
<!-- /GEN:breadcrumb -->

# XML-Namensraum

Auch die Namensräume der KA-Schnittstellen folgen einer festgelegten Konvention. Sie ist in EBNF beschrieben ([Q25](../../QUELLEN.md#q25), Kap. 4.3.3):

```text
Namensraum        = … NamensraumBereich, ["types"], "/", Version
NamensraumBereich = "ah" | "kose" | "dl" | "kvp" | "pv" | "kvp-dl-pv"
                  | "pv-alise" | "kvp-alise" | "dl-statber"
                  | "kvp-statber" | "pv-statber" | "ion" | "common"
```

Zwei Festlegungen sind daran wichtig:

**Die letzte Pfadstelle ist eine Version, nicht ein Release.** Dazu passt Kap. 4.3.1.4: „Innerhalb einer Version sind die Releases hinsichtlich des gemeinsamen Namensraumes kompatibel.“ Gleichzeitig werden nur zwei Versionen unterstützt (Kap. 4.3.1.3).

**Service-Packs ändern den Namensraum nicht.** Bei Einführung eines Service-Packs oder einer Korrektur „bleibt der Namensraum bestehen“; erweitert wird nur das Namensraumkürzel um `-ext-` plus Releasenummer ([Q25](../../QUELLEN.md#q25), Kap. 4.3.3).

Daraus folgt für die Praxis: **Aus dem Namensraum lässt sich die Version ablesen, nicht aber das Release** (abgeleitet). Zwei Systeme mit demselben Namensraum können unterschiedliche Releases fahren.

Angewandt auf den beobachteten Namensraum `http://vdv/ka/alise/2` ([Q11](../../QUELLEN.md#q11)): Die `2` ist nach dieser Konvention die **Version** (abgeleitet). Das passt dazu, dass die Kernapplikation laut Glossar die Versionen 1 und 2 umfasst.

**Offen** (zu prüfen, O4): Die extrahierte Bereichsliste führt `pv-alise` und `kvp-alise`, nicht ein einfaches `alise`. Ob der beobachtete Namensraum einer anderen Fassung der Konvention folgt oder die Extraktion unvollständig ist, lässt sich nicht entscheiden — die EBNF in [Q25](../../QUELLEN.md#q25) weist Kodierungslücken auf.

## Einfach erklärt – Beispiel aus Bärstadt

Ein Namensraum sieht aus wie eine Internetadresse, ist aber keine. Man kann ihn nicht aufrufen.

Bei Pias Aktionslisteneintrag steht in der ersten Zeile:

```text
http://vdv/ka/alise/2
```

Niemand erwartet, dort eine Webseite zu finden. Der Zweck ist ein anderer: Er sagt eindeutig, **in welchem Vokabular** die folgenden Elementnamen zu verstehen sind. Ein `berStatus` aus diesem Namensraum ist etwas anderes als ein `berStatus`, das irgendein anderes System gleich benennt.

Interessant wird die letzte Zahl, die **2**.

Naheliegend wäre, sie für eine Versionsnummer der VDV-KA zu halten — und damit wäre man auf dem Holzweg, denn die Releases heißen 1.1.07, 1.3.0 oder 1.12.0. Eine 2 passt da nicht.

Die Konvention im eTicket-Regelwerk löst das auf. Dort endet ein Namensraum ausdrücklich auf eine **Version**, und Version ist etwas anderes als Release: Die Kernapplikation umfasst die Versionen 1 und 2, etiCORE ist Version 3. Die Releases 1.1.07 und 1.3.0 liegen *innerhalb* einer Version und teilen deshalb denselben Namensraum.

Das ist ein kluger Entwurf, und man sieht den Grund sofort. Würde jedes Release einen neuen Namensraum bekommen, müsste jedes System bei jedem Update alle Partner nachziehen. So bleibt der Namensraum stabil, und nur Fehlerkorrekturen bekommen ein Anhängsel.

Für Bärstadt bedeutet das: Aus der 2 kann man **nicht** schließen, welches Release die Verkehrsbetriebe fahren. Dafür muss man sie fragen.

Ehrlich bleibt eine Unschärfe. Die Bereichsliste der Konvention nennt `pv-alise` und `kvp-alise` — ein einfaches `alise` steht dort nicht.

## Quellen

- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 4.3.3 (PDF-S. 115): EBNF der Namensraumkonvention mit der Liste der Bereiche, Endung auf eine Version, Erhalt des Namensraums bei Service-Packs und Korrekturen, Erweiterung des Namensraumkürzels um `-ext-` plus Releasenummer; Kap. 4.3.1.3 (nur zwei Versionen gleichzeitig), Kap. 4.3.1.4 (Kompatibilität der Releases innerhalb einer Version über den gemeinsamen Namensraum)
- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht mit dem Namensraum `http://vdv/ka/alise/2`. **Nicht öffentliche Unterlage**; übernommen ist nur der Namensraum.

**Hinweis zur Extraktion:** Die EBNF in [Q25](../../QUELLEN.md#q25) enthält im extrahierten Text Lücken durch fehlende Sonderzeichen; insbesondere das Präfix der Namensraum-Produktion ist nicht vollständig lesbar. Zitate vor verbindlicher Verwendung am PDF prüfen.

<!-- GEN:siehe_auch -->
## Siehe auch

- [XSD und WSDL](xsd.md) (XSD)
- [txalisber](../transaktionen/txalisber.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
