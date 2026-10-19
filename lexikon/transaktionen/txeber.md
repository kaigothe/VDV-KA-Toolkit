---
titel: TXEBER
abkuerzung: TXEBER
englisch: inspection attestation
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/logtransaktionstyp.md, lexikon/transaktionen/nachweis.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes:
  - wert: 59
    bedeutung: IONTransaktionsTyp_CODE für TXEBER aus Kontrolle
    quelle: Q06
    fundstelle: Kap. 5.1.2 (PDF-S. 40)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › TXEBER
<!-- /GEN:breadcrumb -->

# TXEBER

`TXEBER` ist der **Kontrollnachweis** einer Berechtigung. Die Struktur ist der nicht öffentlichen KA SST-SPEC zu entnehmen, gemeinsam mit `TXEMBER`, `TXKNAWDM`, `TXKNAWA` und `TXKNAWB` ([Q06](../../QUELLEN.md#q06), Kap. 4.2.3; [Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 4).

Für `TXEBER` aus Kontrolle sind **beide Typfelder belegt**: `IONTransaktionsTyp_CODE` = 059 und `logTransaktionsTyp.code` = 27 ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2) · *verbundspezifisch*.

**Datenschutzvorgabe.** Aus der Begutachtung des Hintergrundsystems durch den Datenschutz des Landes Hessen im November 2016 resultierte die Vorgabe, Kontrollnachweise **ohne Fahrtnummer und Linieninformation** zu speichern. Konkret sind in `TXEBER` aus Kontrolle drei Attribute zu leeren: `berLogFahrt_ID.fahrtNummer`, `berLogLinieVarianteID.linie_ID.linienNummer` und `berLogLinieVarianteID.variantenNummer`. Dies soll vorzugsweise bereits durch das Terminal geschehen ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2).

Daraus folgt ein technischer Konflikt: Die Attribute sind Teil der Daten, über die die MACs gebildet wurden. Überschreibt das Hintergrundsystem sie, kennzeichnet es die betroffenen Transaktionen, die dann **von einer späteren MAC-Validierung ausgenommen** werden ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2).

Die Vorgabe gilt **ausschließlich** für `TXEBER`-Kontrollnachweise, nicht generell für die Attribute Fahrtnummer und Linienvariante — im [`TXABER`](txaber.md) dürfen sie nicht überschrieben werden ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2).

Ab KA 1.3.0 kommt `TXEMBER` für Multiberechtigungen hinzu ([Q06](../../QUELLEN.md#q06), Kap. 5.1).

## Einfach erklärt – Beispiel aus Bärstadt

Wenn Petra Pranke in der Linie 4 eine Karte prüft, entsteht ein Beleg darüber: `TXEBER`. Er hält fest, dass diese Berechtigung zu diesem Zeitpunkt kontrolliert wurde.

Dieser Beleg ist der heikelste in der ganzen Kategorie, und zwar nicht aus technischen Gründen.

Ein Kontrollnachweis enthält nämlich von Natur aus Fahrt- und Liniennummer. Sammelt man viele davon, entsteht etwas, das niemand haben wollte: ein Bewegungsprofil. Man könnte nachlesen, wann Pia welche Linie benutzt hat.

Genau das hat der hessische Datenschutz 2016 bei der Prüfung des Hintergrundsystems beanstandet. Die Vorgabe lautete: Kontrollnachweise werden ohne Fahrt- und Linieninformation gespeichert. Drei Felder werden geleert, und zwar möglichst schon im Kontrollgerät, bevor die Daten überhaupt losgeschickt werden.

Nun kommt das technisch Spannende. Diese Felder sind Teil der Daten, über die der Prüfcode gebildet wurde — der Code also, der beweist, dass der Beleg echt ist. Leert man die Felder, passt der Prüfcode nicht mehr. Der Beleg wird durch die Datensparsamkeit unprüfbar.

Hier musste man sich entscheiden, und die Entscheidung fiel für den Datenschutz: Das Hintergrundsystem leert die Felder, **markiert** den Beleg aber und nimmt ihn von späteren Prüfungen der Echtheit aus.

Das ist ein ehrlicher Kompromiss, und man sollte ihn kennen. Es bedeutet, dass für Kontrollnachweise ein Stück Beweiskraft bewusst aufgegeben wurde.

Besonders aufschlussreich ist die Abgrenzung: Für Pias Ausgabenachweis gilt das nicht. Dort dürfen dieselben Felder ausdrücklich **nicht** geleert werden — weil eine Ausgabe kein Bewegungsdatum ist und der Beleg seine volle Beweiskraft behalten soll.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.2.3 (Kontrollnachweise `TXEBER`, `TXEMBER`, `TXKNAWDM`, `TXKNAWA`, `TXKNAWB` aus `[KA_SPEC_SST]`), Kap. 5.1 (Durchführung der Kontrolltransaktion `TXEBER`, `TXEMBER`), Kap. 5.1.2 „Datenschutz“ (PDF-S. 40): Begutachtung durch den Datenschutz des Landes Hessen im November 2016, `IONTransaktionsTyp_CODE` = 059 und `logTransaktionsTyp.code` = 27, die drei zu leerenden Attribute, Ausnahme von der MAC-Validierung, Abgrenzung zum `TXABER` · *verbundspezifisch: eTicket RheinMain*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 65 („Nachweis“, Kontrolle als Anlass)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SST-SPEC, Inventarnummer 4)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
