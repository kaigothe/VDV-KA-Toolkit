---
titel: TLV-Kodierung
abkuerzung: TLV
englisch: TLV encoding
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/bom.md, lexikon/berechtigungen/produktspezifischer-teil.md]
quellen: [Q02, Q05, Q11, Q12, Q25, Q35]
status: belegt
offene_fragen: [O6]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › TLV-Kodierung
<!-- /GEN:breadcrumb -->

# TLV-Kodierung

TLV steht für **Tag, Length, Value**: Jedes Element beginnt mit einer Kennung, dann folgt die Länge, dann der Wert. Strukturen lassen sich schachteln, indem der Wert selbst wieder TLV-Elemente enthält.

Der **TLV-EFS** ist ein elektronischer Fahrschein „mit in einer Anlage zur KA BOM-Spec definierten TLV-Datenelementen in der Datenstruktur Statischer Produktspezifischer Teil und Transaktion Produktspezifischer Teil“. **In KA Release 1.x wird der Transaktion Produktspezifische Teil nicht verwendet** ([Q02](../../QUELLEN.md#q02), S. 96) — bestätigt durch die Praxis, die ihn als leeres TLV `0x8A 0x00` mit Länge 0 schreibt ([Q12](../../QUELLEN.md#q12)).

**Belegte Tags:**

| Tag | Bedeutung | Quelle |
|---|---|---|
| `0xE8` | Berechtigung | [Q05](../../QUELLEN.md#q05) |
| `0xE9` | Verzeichniseintrag Berechtigung | [Q05](../../QUELLEN.md#q05) |
| `0xC0` | Systemspezifischer Verzeichnisteil | [Q05](../../QUELLEN.md#q05) |
| `0x83` | Verzeichniseintrag, statischer Teil | [Q05](../../QUELLEN.md#q05) |
| `0x84` | Verzeichniseintrag, dynamischer Teil | [Q05](../../QUELLEN.md#q05) |
| `0xEA` | Separate Daten Berechtigung | [Q05](../../QUELLEN.md#q05) |
| `0x85` | Statischer produktspezifischer Teil | [Q05](../../QUELLEN.md#q05) |
| `0x8A` | Transaktion produktspezifischer Teil — in KA 1.x leer | [Q12](../../QUELLEN.md#q12) |
| `0xDA` | Grundlegende Daten | [Q35](../../QUELLEN.md#q35) |
| `0xDB` | [Fahrgast](tag-0xdb-fahrgast.md) | [Q12](../../QUELLEN.md#q12) |

**Längenkodierung:** Längen bis 127 stehen in einem Byte (`0x44` = 68). Größere Längen werden mehrbytig kodiert — in [Q05](../../QUELLEN.md#q05) erscheint `0x81 0xE1` für 225 und `0x81 0x95` für 149 Byte, also ein Präfixbyte `0x81` plus Längenbyte (abgeleitet; entspricht der BER-TLV-Konvention).

Normquelle ist die nicht öffentliche **Anlage TLV EFS**, Inventarnummer 2 ([Q25](../../QUELLEN.md#q25), Kap. 3); [Q12](../../QUELLEN.md#q12) verweist auf die Fassung V190, S. 9 für Tag 0xDB und S. 18 Tabelle 2-8 für Variante D.

**Offen** (zu prüfen, O6): In der ausgewerteten Nachricht gibt Tag `0x85` die Länge `0x57` = 87 Byte an, es folgen aber 90 Byte ([Q11](../../QUELLEN.md#q11)).

## Einfach erklärt – Beispiel aus Bärstadt

TLV ist ein Verfahren, Daten so zu verpacken, dass man sie auch ohne Kenntnis des Inhalts zerlegen kann.

Drei Teile hat jedes Element. Zuerst ein **Tag** — eine Zahl, die sagt, was folgt. Dann die **Länge** in Byte. Dann der **Wert**.

Der Nutzen zeigt sich beim Lesen. Ein Kontrollgerät liest auf Pias BärenKarte das Tag `0x85` und erfährt: Hier kommt der produktspezifische Teil. Es liest die Länge, 68 Byte. Und jetzt kommt das Entscheidende: Falls das Gerät mit diesem Produkt nichts anfangen kann, **überspringt es einfach 68 Byte** und liest weiter.

Das ist der eigentliche Trick. Ein Format ohne Längenangaben müsste jedes Feld verstehen, um zum nächsten zu kommen. Mit TLV kann ein altes Gerät neue Felder überlesen, ohne daran zu scheitern.

Geschachtelt wird, indem ein Wert selbst wieder TLV-Elemente enthält. Pias Berechtigung ist genau so gebaut: ganz außen das Tag für „Berechtigung", darin ein Verzeichniseintrag, darin wiederum ein statischer und ein dynamischer Teil.

Bei den Längen gibt es eine Feinheit, über die man leicht stolpert. Kurze Längen stehen in einem Byte. Für größere Werte steht erst ein Byte `0x81` und dann die eigentliche Länge — denn ein einzelnes Byte reicht nur bis 127. Wer das übersieht, liest bei langen Strukturen an der falschen Stelle weiter.

Und ein Detail, das zeigt, warum man diese Dinge nachrechnen sollte: In einer echten Nachricht gab die Länge 87 Byte an, und es folgten 90. Entweder sind drei Byte Füllung, oder es ist ein Fehler, oder die Annahme über das Tag war falsch.

Genau solche Abweichungen soll ein Analysewerkzeug anzeigen statt stillschweigend darüber hinweglesen.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 96 („TLV-EFS“: TLV-Datenelemente nach einer Anlage zur KA BOM-Spec, Statischer und Transaktion Produktspezifischer Teil, Nichtverwendung des Transaktionsteils in KA 1.x)
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (PDF-S. 8 f.): Tags 0xE8, 0xE9, 0xC0, 0x83, 0x84, 0xEA, 0x85 mit Längen, darunter die mehrbytigen Angaben 0x81 0xE1 und 0x81 0x95 · *verbundspezifisch*
- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings (Tag 0xDB nach Anlage TLV EFS V190, S. 9; Variante D nach S. 18 Tab. 2-8; Transaktion Produktspezifischer Teil als leeres TLV 0x8A 0x00) · *Herstellerquelle*
- [Q35](../../QUELLEN.md#q35) – KCD NRW, Produktparameter (Tag 0xDA „Grundlegende Daten“ mit der Verkaufsproduktnummer) · *verbundspezifisch*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (Anlage TLV EFS, Inventarnummer 2)
- [Q11](../../QUELLEN.md#q11) – ausgewertete Nachricht (Längenangabe 0x57 bei 90 folgenden Byte). **Nicht öffentliche Unterlage.**

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
