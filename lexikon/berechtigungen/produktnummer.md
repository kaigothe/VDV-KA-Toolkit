---
titel: Produktnummer
englisch: product number
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/produkt.md, lexikon/rollen/organisations-id.md]
quellen: [Q02, Q05, Q25, Q35]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Produktnummer
<!-- /GEN:breadcrumb -->

# Produktnummer

Die Produktnummer identifiziert ein EFM-Produkt **innerhalb** eines Produktverantwortlichen. Eindeutig im gesamten EFM-System ist erst das Paar aus Produktnummer und [Organisations-ID](../rollen/organisations-id.md) des Produktverantwortlichen ([Q02](../../QUELLEN.md#q02), S. 36).

**Wertebereich:** Die EFM-Produktnummer ist numerisch mit dem Bereich **0 bis 65535** und wird „in der Fahrtberechtigung im Feld `produktNummer`“ genutzt ([Q35](../../QUELLEN.md#q35)) · *verbundspezifisch*. Das entspricht zwei Byte (abgeleitet).

**Ablage:** Im RMV-EFS steht das Feld `prodProdukt_ID` als Struktur „EFM Produkt_ID“ mit **4 Byte** im statischen Teil der Berechtigung und enthält „neben der Produktnummer die Org-ID“ des Produktverantwortlichen. Es dient zugleich als Referenz-ID für den Schlüssel `K_PV-NM-MAC`. „Produktnummern werden vom RMV festgelegt.“ ([Q05](../../QUELLEN.md#q05), Kap. 2.1) · *verbundspezifisch*

Vier Byte für Produktnummer und Org-ID zusammen bei einem Wertebereich bis 65535 für die Nummer bedeutet: je zwei Byte (abgeleitet).

**Vergabe:** Für die Vergabe von Produkt-IDs in VDV-KA-EFM-Systemen existiert eine eigene Verfahrensanweisung, die KA PROD_ID-ANW mit der Inventarnummer 35 ([Q25](../../QUELLEN.md#q25), Kap. 3). Sie ist nicht öffentlich.

Daneben führt die NRW-Praxis eine **Tarifproduktnummer** je Produktverantwortlichem, die im VRS und AVV „im TLV-EFS im Tag 0xDA im Feld Verkaufsproduktnummer“ genutzt wird ([Q35](../../QUELLEN.md#q35)) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Die Produktnummer ist ein gutes Beispiel dafür, wie in der VDV-KA fast nichts für sich allein eindeutig ist.

Pias ABO Azubi ist Produkt **2001**. Diese Zahl gilt beim Bären-Verkehrsbund. Beim Luchs-Verkehrsverbund könnte 2001 eine Tageskarte für Hunde sein — ohne dass irgendwo ein Konflikt entsteht. Erst die Angabe `2001 / 9020` ist eindeutig.

Das ist kein Schönheitsfehler, sondern Absicht. Würde eine zentrale Stelle alle Produktnummern aller Verbünde vergeben, müsste jeder neue Tarif dort beantragt werden. So vergibt jeder Verbund seine Nummern selbst und muss sich mit niemandem abstimmen.

Der Wertebereich verrät, wie das technisch gedacht ist: 0 bis 65535. Das sind genau zwei Byte. Ein Verbund kann also gut 65 000 Produkte definieren — mehr als jeder braucht, und wenig genug, dass es auf eine Chipkarte passt.

Im RMV-Format belegt das Feld vier Byte: zwei für die Nummer, zwei für die Organisation. Daran sieht man, dass die Paarung nicht nur eine Konvention ist, sondern in der Datenstruktur verankert.

Ein Detail mit praktischem Wert: Dasselbe Feld dient gleichzeitig als **Verweis auf einen Schlüssel** — nämlich den des Produktverantwortlichen. Es sagt also nicht nur „das ist Produkt 2001 des Verbunds“, sondern auch „mit dessen Schlüssel ist dieser Eintrag gesichert“. Zwei Aufgaben in vier Byte.

Für die Vergabe gibt es übrigens eine eigene Verfahrensanweisung des Standards. Man darf Nummern also nicht völlig frei wählen — es gibt Regeln dafür, die allerdings nicht öffentlich sind.

Und eine Verwechslungsgefahr zum Schluss: Die **Tarif**produktnummer ist etwas anderes als die **EFM**-Produktnummer. In NRW stehen beide in derselben Tabelle, in verschiedenen Spalten.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 36 (Eindeutigkeit der Nummer je PV und gemeinsam mit der Org-ID im gesamten EFM-System)
- [Q35](../../QUELLEN.md#q35) – KCD NRW, Produktparameter der Tarife in NRW, V1.0 (EFM-Produktnummer numerisch mit Wertebereich 0 bis 65535, Nutzung im Feld `produktNummer` der Fahrtberechtigung; Tarifproduktnummer bzw. Verkaufsproduktnummer im TLV-EFS unter Tag 0xDA) · *verbundspezifisch: NRW*
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (`prodProdukt_ID` als Struktur „EFM Produkt_ID“ mit 4 Byte im statischen Teil, enthält Produktnummer und Org-ID, dient als Referenz-ID für `K_PV-NM-MAC`; Produktnummern werden vom RMV festgelegt) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA PROD_ID-ANW, Inventarnummer 35: Verfahrensanweisung zur Vergabe von Produkt_IDs)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Produkt](produkt.md)
- [Organisations-ID](../rollen/organisations-id.md) (Org-ID)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
