---
titel: Kontrollnachweise
englisch: inspection attestations
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/transaktionen/txeber.md, lexikon/kontrolle/sperrnachweis.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Kontrollnachweise
<!-- /GEN:breadcrumb -->

# Kontrollnachweise

Kontrollnachweise dokumentieren eine durchgeführte Kontrolle. [Q06](../../QUELLEN.md#q06), Kap. 4.2.3, nennt **fünf** Strukturen, alle aus der nicht öffentlichen KA SST-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 4) · *verbundspezifisch*:

| Nachricht | Zusammenhang |
|---|---|
| [`TXEBER`](../transaktionen/txeber.md) | Kontrolle einer Berechtigung |
| `TXEMBER` | Kontrolle einer Multiberechtigung, ab KA 1.3.0 |
| `TXKNAWA` | Kontrollnachweis, Variante A |
| `TXKNAWB` | Kontrollnachweis, Variante B |
| `TXKNAWDM` | Kontrollnachweis, Variante DM |

`TXEBER` und `TXEMBER` sind dabei die Nachweise aus der **Kontrolltransaktion** ([Q06](../../QUELLEN.md#q06), Kap. 5.1). Wofür die drei `TXKNAW*`-Varianten im Einzelnen stehen, ist aus den öffentlichen Quellen nicht zu belegen (zu prüfen).

**Versionsunterschied mit Folgen:** In 1GSI / KA 1.X wird ein Kontrollnachweis **zusätzlich zum Senden an den Produktverantwortlichen auf das Nutzermedium geschrieben**; ab 2GSI / etiCORE geht er **nur noch an den Produktverantwortlichen** und kann nicht mehr aus dem Nutzermedium ausgelesen werden. „Damit ist ab 2GSI / etiCORE die Kontrolle ohne SAM möglich.“ ([Q02](../../QUELLEN.md#q02), S. 53)

Der Nachweis auf dem Medium ist also der Grund, warum heutige Kontrollgeräte ein SAM brauchen (abgeleitet).

**Datenschutz:** Für `TXEBER` aus Kontrolle sind drei Attribute zu leeren — Fahrtnummer und Linienvariante —, weil Kontrollnachweise ohne Fahrt- und Linieninformation gespeichert werden sollen. Weil diese Attribute Teil der MAC-Daten sind, werden die betroffenen Transaktionen von der MAC-Validierung ausgenommen ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Jede Kontrolle hinterlässt eine Spur — und das aus einem handfesten wirtschaftlichen Grund.

Die Bärstädter Verkehrsbetriebe befördern Pia. Bezahlt hat sie an ihren Kundenvertragspartner, und das Produkt gehört dem Bären-Verkehrsbund. Damit die BVB ihr Geld bekommen, müssen sie belegen können, dass sie die Leistung erbracht haben. Kontrollnachweise sind ein Teil dieses Belegs.

Deshalb entsteht bei jeder Prüfung eine Meldung. Petra Pranke liest Pias Karte, und ihr Gerät schreibt: Diese Berechtigung wurde zu diesem Zeitpunkt kontrolliert und war in Ordnung.

Jetzt kommt ein Detail, das die ganze Gerätelandschaft erklärt.

**Heute schreibt das Gerät diesen Nachweis auch auf die Karte.** Nicht nur ans Rechenzentrum — auch auf den Chip. Und dafür braucht es einen Sicherheitsbaustein, denn der Nachweis muss kryptografisch gesichert sein.

Das ist der Grund, warum ein vollwertiges Kontrollgerät teuer ist. Es muss nicht nur lesen, sondern schreiben können, mit Schlüsseln arbeiten und einen Sicherheitsbaustein mitführen.

**In der nächsten Generation entfällt das.** Der Nachweis geht nur noch ans Backend. Damit ist, wie das Glossar nüchtern festhält, „die Kontrolle ohne SAM möglich" — ein gewöhnliches Smartphone genügt.

Wer heute eine Investitionsentscheidung trifft, sollte das wissen. Geräte, die ihren Wert aus dem Sicherheitsbaustein ziehen, verlieren einen Teil ihrer Begründung.

Und ein Datenschutzdetail, das man nicht vermuten würde: In Kontrollnachweisen werden Fahrt- und Liniennummer absichtlich geleert, damit keine Bewegungsprofile entstehen. Das macht den Nachweis allerdings kryptografisch unprüfbar — eine bewusst in Kauf genommene Einschränkung.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.2.3 (die Strukturen `TXEBER`, `TXEMBER`, `TXKNAWDM`, `TXKNAWA` und `TXKNAWB` aus `[KA_SPEC_SST]`), Kap. 5.1 (Durchführung der Kontrolltransaktion `TXEBER`, `TXEMBER`), Kap. 5.1.2 (Datenschutzvorgabe zum Leeren von Fahrtnummer und Linienvariante, Ausnahme von der MAC-Validierung) · *verbundspezifisch: eTicket RheinMain*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 53 (Kontrollnachweis in 1GSI zusätzlich auf dem Nutzermedium, ab 2GSI nur noch an den Produktverantwortlichen, dadurch Kontrolle ohne SAM möglich), S. 53 (Abrechnung des Dienstleisters über Leistungsnachweise)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SST-SPEC, Inventarnummer 4)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
