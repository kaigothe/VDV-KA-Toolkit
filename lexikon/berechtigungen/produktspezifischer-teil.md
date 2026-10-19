---
titel: Produktspezifischer Teil
englisch: product specific part
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/berechtigung.md, lexikon/berechtigungen/produkt.md, lexikon/datenformate/nullwerte.md]
quellen: [Q02, Q05, Q11, Q12, Q35]
status: belegt
offene_fragen: [O6]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Produktspezifischer Teil
<!-- /GEN:breadcrumb -->

# Produktspezifischer Teil

Der produktspezifische Teil nimmt die Tarifparameter auf, die **nur das jeweilige Produkt** betreffen. Das EFM-Produkt legt als Produkt-Template fest, wie sie als spezifizierte Datenelemente innerhalb einer Berechtigung abgelegt werden; sie sind Bestandteil der Berechtigung und liegen im **erweiterten Datenteil** in der Regel in Form eines **TLV-EFS** ([Q02](../../QUELLEN.md#q02), S. 36).

Der TLV-EFS ist ein elektronischer Fahrschein „mit in einer Anlage zur KA BOM-Spec definierten TLV-Datenelementen in der Datenstruktur Statischer Produktspezifischer Teil und Transaktion Produktspezifischer Teil“. **In KA Release 1.x wird der Transaktion Produktspezifische Teil für den TLV-EFS nicht verwendet** ([Q02](../../QUELLEN.md#q02), S. 96).

Im RMV-EFS liegt der statische produktspezifische Teil unter **Tag 0x85** innerhalb der separaten Daten (Tag 0xEA) und hat dort die Länge **0x44**, also 68 Byte ([Q05](../../QUELLEN.md#q05), Kap. 2.1) · *verbundspezifisch*. Die Länge ist produktabhängig; in der ausgewerteten Nachricht steht an derselben Stelle 0x57 ([Q11](../../QUELLEN.md#q11)).

**Bekannte TLV-Tags** innerhalb dieses Teils:

| Tag | Inhalt | Quelle |
|---|---|---|
| **0xDA** | Grundlegende Daten, u. a. Verkaufsproduktnummer | [Q35](../../QUELLEN.md#q35) · NRW |
| **0xDB** | Fahrgast: `efsFahrgastName`, `efsFahrgastGeburtsdatum`, `efsFahrgastGeschlecht` | [Q12](../../QUELLEN.md#q12) |

Hier liegen auch die personenbezogenen Daten eines personengebundenen EFS ([Q12](../../QUELLEN.md#q12)).

**Offen** (zu prüfen, O6): In der ausgewerteten Nachricht gibt die Länge 0x57 = 87 Byte an, es folgen aber 90 Byte. Füllbytes, Übertragungsfehler oder eine falsche TLV-Annahme sind nicht zu unterscheiden; die Normquelle ist die nicht öffentliche Anlage TLV EFS.

## Einfach erklärt – Beispiel aus Bärstadt

Jede Berechtigung hat einen Teil, den nur ihr Produkt versteht.

Der Rest ist standardisiert: Berechtigungsnummer, Produktnummer, Gültigkeit, Status — diese Felder sehen bei jeder KA-Berechtigung gleich aus, und jedes Kontrollgerät kann sie lesen. Dann kommt ein Block, bei dem das aufhört.

Bei Pias ABO Azubi stehen dort ihr Name und ihr Geburtsdatum. Bei Olli Tapsigs Einzelfahrschein stünde dort etwas anderes — vielleicht ein Tarifgebiet, vielleicht nichts Vergleichbares. Beides sind Berechtigungen, beide haben denselben äußeren Aufbau, und beide haben an dieser Stelle verschiedene Inhalte.

Der Aufbau folgt einem einfachen Muster, das in der Technik überall begegnet: **Typ, Länge, Wert**. Erst ein Byte, das sagt, was kommt. Dann die Länge. Dann die Daten. Ein Lesegerät kann so auch über Felder hinweglesen, die es nicht kennt — es weiß ja, wie lang sie sind.

Zwei dieser Typen sind öffentlich bekannt. Unter dem Kennzeichen 0xDA liegen grundlegende Daten wie die Verkaufsproduktnummer, unter 0xDB die Fahrgastdaten: Name, Geburtsdatum, Geschlecht.

Damit ist auch klar, wo im System die personenbezogenen Daten sitzen — nämlich genau hier, in diesem einen Block. Das ist für Datenschutzfragen die entscheidende Stelle.

Und es erklärt die Grenze jeder Auswertung. Ohne das Produktschema sieht man Hexadezimalzahlen. Man kann die Struktur zerlegen, Längen prüfen, Tags erkennen — aber man kann nicht sagen, was eine Zahl bedeutet, wenn das Produkt sie definiert.

Eine Auffälligkeit aus der Praxis: In einer echten Nachricht gab die Länge 87 Byte an, es folgten aber 90. Solche Abweichungen muss ein Werkzeug melden können, statt sie stillschweigend zu überlesen.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 36 (Produkt-Template, Ablage der Tarifparameter im erweiterten Datenteil als TLV-EFS), S. 96 („TLV-EFS“: TLV-Datenelemente in der Anlage zur KA BOM-Spec, Statischer und Transaktion Produktspezifischer Teil, Nichtverwendung des Transaktionsteils in KA 1.x)
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (PDF-S. 9): Tag 0x85 „Separate Daten – Berechtigung RMV EFS – Statischer produktspezifischer Teil“ mit Länge 0x44, eingebettet in Tag 0xEA · *verbundspezifisch*
- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings (Tag 0xDB „Fahrgast“ mit `efsFahrgastName`, `efsFahrgastGeburtsdatum`, `efsFahrgastGeschlecht`; Verweis auf die Anlage TLV EFS) · *Herstellerquelle*
- [Q35](../../QUELLEN.md#q35) – KCD NRW, Produktparameter (Tag 0xDA mit der Verkaufsproduktnummer) · *verbundspezifisch: NRW*
- [Q11](../../QUELLEN.md#q11) – ausgewertete Nachricht (Längenangabe 0x57 bei 90 folgenden Byte). **Nicht öffentliche Unterlage.**

<!-- GEN:siehe_auch -->
## Siehe auch

- [Berechtigung](berechtigung.md)
- [Produkt](produkt.md)
- [Nullwerte](../datenformate/nullwerte.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
