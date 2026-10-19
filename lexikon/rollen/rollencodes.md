---
titel: Rollencodes
englisch: role codes
parent: lexikon/rollen.md
siehe_auch: [lexikon/transaktionen/tx-base.md, lexikon/rollen/organisations-id.md]
quellen: [Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes:
  - wert: 1
    bedeutung: KVP — Kundenvertragspartner
    quelle: Q06
    fundstelle: Kap. 4.10 (PDF-S. 37 ff.)
    status: belegt
    verbundspezifisch: true
  - wert: 2
    bedeutung: DL — Dienstleister
    quelle: Q06
    fundstelle: Kap. 4.10 (PDF-S. 37 ff.)
    status: belegt
    verbundspezifisch: true
  - wert: 3
    bedeutung: PV — Produktverantwortlicher
    quelle: Q06
    fundstelle: Kap. 4.10 (PDF-S. 37 ff.)
    status: belegt
    verbundspezifisch: true
  - wert: 4
    bedeutung: AH — Applikationsherausgeber (laut Versionshistorie von 5 auf 4 korrigiert)
    quelle: Q06
    fundstelle: Kap. 4.10, Versionshistorie v2.2
    status: belegt
    verbundspezifisch: true
  - wert: 5
    bedeutung: KOSE — Kontroll- und Sperrlistenservice
    quelle: Q06
    fundstelle: Kap. 4.10 (PDF-S. 37 ff.)
    status: belegt
    verbundspezifisch: true
  - wert: 31
    bedeutung: ALISE — ab KA 1.3.0 nur für einen ausgelagerten zentralen ALISE-Server
    quelle: Q06
    fundstelle: Fußnote 7 (PDF-S. 39)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Rollencodes
<!-- /GEN:breadcrumb -->

# Rollencodes

Jede Nachricht trägt im [`TX_BASE`](../transaktionen/tx-base.md) neben der [Organisations-ID](organisations-id.md) einen Rollencode. Erst beide zusammen sagen, **wer** in **welcher Funktion** sendet oder empfängt ([Q06](../../QUELLEN.md#q06), Kap. 4.10).

| Code | Rolle |
|---:|---|
| **1** | [KVP](kvp.md) — Kundenvertragspartner |
| **2** | [DL](dl.md) — Dienstleister |
| **3** | [PV](pv.md) — Produktverantwortlicher |
| **4** | [AH](ah.md) — Applikationsherausgeber |
| **5** | [KOSE](kose.md) — Kontroll- und Sperrlistenservice |
| **31** | [ALISE](alise.md) — eingeschränkt, siehe unten |

Zwei Besonderheiten:

Der Code **4** für den AH ist eine Korrektur. Die Versionshistorie von [Q06](../../QUELLEN.md#q06) vermerkt zum 16.03.2018: „In Kap. 4.10 Rollencode für den AH von 5 auf 4 korrigiert“. In älteren Unterlagen kann also eine 5 stehen.

Der Code **31** für ALISE ist ab KA 1.3.0 nur noch für einen aus dem PV-System ausgelagerten, eigenständigen zentralen ALISE-Server reserviert; sonst ist die Rolle 3 zu verwenden ([Q06](../../QUELLEN.md#q06), Fußnote 7, PDF-S. 39).

[Q06](../../QUELLEN.md#q06), Kap. 4.10, stellt die Codes **je Anwendungsfall** dar und unterscheidet nach der Rolle des Verkehrsunternehmens: ist es DL, aber nicht KVP, gilt DL = 2; ist es KVP, aber nicht DL, gilt KVP = 1; ist es **beides**, gilt KVP = 1 · *verbundspezifisch*.

Die Codeliste selbst steht in der nicht öffentlichen KA BOM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 1).

## Einfach erklärt – Beispiel aus Bärstadt

Eine Organisations-ID allein genügt nicht, um zu sagen, wer gerade spricht.

Die Bärstädter Verkehrsbetriebe haben die ID 9010. Aber sie sind Kundenvertragspartner **und** Dienstleister. Wenn eine Nachricht von 9010 kommt — handelt es sich dann um den Vertriebsarm, der Pias Abo verwaltet, oder um den Fahrbetrieb, der sie befördert?

Deshalb steht neben der Nummer immer eine zweite Angabe, der Rollencode. Erst `9010 / 1` sagt: die BVB als Kundenvertragspartner. `9010 / 2` wäre dieselbe Organisation als Dienstleister.

Die sechs Codes sind schnell gelernt: 1 für den Kundenvertragspartner, 2 für den Dienstleister, 3 für den Produktverantwortlichen, 4 für den Applikationsherausgeber, 5 für den Sperrlistenservice. Für Pias Abo-Ausgabe heißt das: Absender ist 9010 in Rolle 1, Empfänger der Bären-Verkehrsbund 9020 in Rolle 3.

Zwei Stolpersteine lohnen die Aufmerksamkeit.

Der erste: Der Code für den Applikationsherausgeber war im RMV-Pflichtenheft zunächst falsch und wurde 2018 von 5 auf 4 korrigiert. Wer eine Implementierung gegen eine alte Fassung gebaut hat, verwechselte den Applikationsherausgeber mit dem Sperrlistenservice. Das ist der Grund, warum eine Korrektur in einer Versionshistorie manchmal wichtiger ist als der Haupttext.

Der zweite: Ist ein Unternehmen gleichzeitig Dienstleister und Kundenvertragspartner — wie in Bärstadt —, dann gilt in den betreffenden Fällen die 1, nicht die 2. Es gibt also eine Vorrangregel. Sie steht nicht im Standard, sondern im Pflichtenheft eines Verbunds, und ob sie überall so gilt, ist offen.

Deshalb hier derselbe Hinweis wie bei allen Codelisten: Für ein anderes System die dort gültige Festlegung heranziehen.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.10 „Übersicht über die in `TX_BASE` verwendeten KA-Rollencodes und Org-IDs“ (PDF-S. 37 ff.): Darstellung je Anwendungsfall, Codes KVP = 1, DL = 2, PV = 3, KOSE = 5, Vorrangregel bei Doppelrolle; Versionshistorie zu v2.2 (Korrektur des AH-Codes von 5 auf 4); Fußnote 7, PDF-S. 39 (Einschränkung des Codes 31 für ALISE); Kap. 2.1.2 (die Mandantenzuordnung erfolgt im Hintergrundsystem über die Device-ID, nicht über die Sender- und Empfängerattribute des `TX_BASE`) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA BOM-SPEC, Inventarnummer 1, als Normquelle der Codelisten)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
