---
titel: Basisobjektmodell
abkuerzung: BOM
englisch: Basic Object Model
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/tlv.md, lexikon/grundlagen/ka-spezifikationen.md]
quellen: [Q05, Q06, Q12, Q25, Q37]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Basisobjektmodell
<!-- /GEN:breadcrumb -->

# Basisobjektmodell

Das Basisobjektmodell (BOM) ist die **gemeinsame Grundlage aller KA-Datenformate**. Es steht im Hauptdokument der Spezifikation, verzeichnet als „Hauptdokument mit Basisobjektmodell (BOM)“ mit der **Inventarnummer 1** ([Q25](../../QUELLEN.md#q25), Kap. 3); in Prüfberichten erscheint es als **KA HD_BOM-SPEC** ([Q37](../../QUELLEN.md#q37)).

Das Dokument ist nicht öffentlich. Aus den Verweisen anderer Quellen lässt sich sein Zuschnitt aber genau ablesen — es definiert:

- **Datentypen** wie `INT1`, `OctetString`, `PrintableString`, `DateTimeCompact`, `SequenceNumberOne`, `ReferenceNumberTwo` ([Q05](../../QUELLEN.md#q05), Kap. 2.1),
- **Strukturen** wie `Berechtigung_ID`, `EFM Produkt_ID`, `Ort_ID`, `Terminal_ID`, `IONTransaktion_ID` ([Q05](../../QUELLEN.md#q05); [Q06](../../QUELLEN.md#q06), Kap. 5.3),
- **Codelisten** wie `WertobjektStatus_CODE`, `NmTransaktionsTyp_CODE`, `IONTransaktionsTyp_CODE`, `AblehnungsTyp_CODE`, `OrtsTyp_Codes` ([Q05](../../QUELLEN.md#q05); [Q06](../../QUELLEN.md#q06), Kap. 5.2, 5.3),
- **Regeln** wie die Kürzungsregel für Namen in Abschnitt **6.7.2** ([Q12](../../QUELLEN.md#q12)).

[Q12](../../QUELLEN.md#q12) verweist seitengenau in die Fassung **V190**, etwa auf S. 50 Tabelle 6-10 für `dateTimeCompact`, S. 104 Tabelle 6-103 für die Produkt-ID-Struktur und S. 110 Tabelle 6-123 für `Ort_ID`. Das belegt den Aufbau als durchnummeriertes Tabellenwerk und nennt mit **1.9.0** eine weitere Version neben der 1.12.0 aus [Q37](../../QUELLEN.md#q37).

**Für die Praxis heißt das:** Ohne BOM lässt sich kein Codewert verbindlich deuten. Fast jede offene Frage dieses Lexikons endet hier — weshalb das Dokument in [BESCHAFFUNG.md](../../BESCHAFFUNG.md) zu den drei wichtigsten gehört.

## Einfach erklärt – Beispiel aus Bärstadt

Das Basisobjektmodell ist das Wörterbuch, auf das alles andere verweist.

Man merkt es daran, wie andere Dokumente sprechen. Das RMV-Pflichtenheft sagt nicht „hier stehen zwei Byte mit einer Zahl darin", sondern: `prodKeyOrganisation_ID`, Typ `ReferenceNumberTwo`. Es benennt den Typ und setzt voraus, dass jemand anderswo festgelegt hat, was das bedeutet.

Dieses „anderswo" ist das BOM. Dort steht, wie ein `DateTimeCompact` aus vier Byte ein Datum macht, wie eine `Berechtigung_ID` aus Nummer und Organisation zusammengesetzt ist, und welche Zahl in `WertobjektStatus_CODE` für „gesperrt" steht.

Deshalb ist es die Antwort auf die meisten offenen Fragen in diesem Lexikon. Immer wenn hier steht „die Codeliste ist nicht öffentlich", ist das BOM gemeint.

Wie es aufgebaut ist, lässt sich erstaunlich genau rekonstruieren, ohne es zu haben. Ein Hersteller dokumentiert nämlich öffentlich, wie er einen VDV-Barcode erzeugt — und zitiert dabei seitengenau: Seite 50, Tabelle 6-10 für das Datumsformat. Seite 110, Tabelle 6-123 für die Ortsangabe. Abschnitt 6.7.2 für die Namenskürzung.

Aus solchen Verweisen entsteht ein Bild: ein mehrere hundert Seiten starkes Tabellenwerk, in dem jeder Datentyp, jede Struktur und jede Codeliste ihre Nummer hat.

Nebenbei verrät dieser Hersteller eine Version, die sonst nirgends auftaucht: **1.9.0**. Ein Prüfbericht von 2024 nennt dagegen 1.12.0, die Verbunddokumente arbeiten mit 1.1.07 und 1.3.0.

Vier Versionsangaben aus vier Quellen — ein guter Grund, bei jedem Zitat die Fassung mitzuschreiben.

## Quellen

- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (Inventarnummer 1: „Hauptdokument mit Basisobjektmodell BOM“, Kurzzeichen KA BOM-SPEC)
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht (2024), S. 4 (KA HD_BOM-SPEC in Version 1.12.0)
- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings: seitengenaue Verweise in KA HD_BOM-Spec_V190, u. a. S. 50 Tab. 6-10 (`dateTimeCompact`), S. 84 Tab. 6-69 (OrtTyp), S. 92 Tab. 6-85 (TerminalTyp), S. 104 Tab. 6-103 (Produkt-ID-Struktur), S. 110 Tab. 6-123 (`Ort_ID`), S. 112 Tab. 6-127 (`Terminal_ID`), Abschn. 6.7.2 (Kürzungsregel für Namen) · *Herstellerquelle*
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (Datentypen und Strukturen in der Berechtigung) · *verbundspezifisch*
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 5.2 (OrtsTyp-Codes), Kap. 5.3 (`IONTransaktion_ID`, `AblehnungsTyp_CODE`, Verweis auf KA_SPEC_BOM) · *verbundspezifisch*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
