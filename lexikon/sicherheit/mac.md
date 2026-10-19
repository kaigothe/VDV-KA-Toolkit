---
titel: MAC
abkuerzung: MAC
englisch: Message Authentication Code
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/schluesselreferenz.md, lexikon/transaktionen/txa-txb.md]
quellen: [Q05, Q06, Q11]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › MAC
<!-- /GEN:breadcrumb -->

# MAC

Ein MAC sichert Integrität und Herkunft von Daten mit einem **symmetrischen** Schlüssel. In der VDV-KA bildet das [SAM](sam.md) des Terminals die MACs beim Schreiben auf das Nutzermedium ([Q11](../../QUELLEN.md#q11)).

**Wo MACs geprüft werden:** Ein Hintergrundsystem lehnt Transaktionen mit „negativem Ergebnis der MAC-Prüfung“ ab und stellt dafür einen Ablehnungsdatensatz [`TXA`](../transaktionen/txa-txb.md) aus ([Q06](../../QUELLEN.md#q06), Kap. 3.1) · *verbundspezifisch*.

**Mehrere MACs je Berechtigung.** [Q05](../../QUELLEN.md#q05), Kap. 2.1, nennt für die Felder einer Berechtigung getrennte Schlüsselreferenzen: `berBerechtigung_ID` ist „Referenz-ID für K_KVP-NM-MAC“, `prodProdukt_ID` für „K_PV-NM-MAC“, `prodKeyOrganisation_ID` für „K_ERF-NM-MAC“ und „MK/K_TR-MAC“. Integrität und Herkunft sind damit **getrennt für Kundenvertragspartner, Produktverantwortlichen und Schlüsselorganisation** gesichert (abgeleitet) — siehe [Schlüsselreferenz](schluesselreferenz.md).

**Grenze des MAC.** Die Felder einer Nachricht enthalten nur Schlüssel­referenzen, nicht die Schlüssel und keinen MAC über die Nachricht selbst. Eine in sich stimmige Manipulation im Hintergrundsystem lässt sich damit nicht erkennen; kryptografisch gesichert sind die **Transaktionsnachweise der Terminals** (abgeleitet aus [Q11](../../QUELLEN.md#q11), [Q06](../../QUELLEN.md#q06), Kap. 3.1).

**Ein belegter Konflikt mit dem Datenschutz:** In `TXEBER`-Kontrollnachweisen sind drei Attribute zu leeren. Weil diese „Teil der Daten sind, über die die MACs gebildet wurden“, kennzeichnet das Hintergrundsystem die betroffenen Transaktionen, „die dann von einer späteren MAC-Validierung **ausgenommen** werden“ ([Q06](../../QUELLEN.md#q06), Kap. 5.1.2) · *verbundspezifisch*. Datensparsamkeit kostet hier Beweiskraft.

## Einfach erklärt – Beispiel aus Bärstadt

Ein MAC ist ein Prüfsiegel, und er beantwortet zwei Fragen auf einmal: Sind die Daten unverändert, und kommen sie von jemandem, der den Schlüssel hat?

Als das Lesegerät am Hauptbahnhof Pias ABO Azubi schrieb, hat sein Sicherheitsbaustein über die Daten gerechnet und das Ergebnis mit auf die Karte geschrieben. Wer später etwas am Gültigkeitsdatum ändert, erzeugt eine Abweichung — das Siegel passt nicht mehr.

Interessant ist, dass es **nicht ein** Siegel gibt, sondern mehrere. Pias Berechtigung trägt getrennte Sicherungen für die Bärstädter Verkehrsbetriebe, für den Bären-Verkehrsbund und für die Schlüsselstelle.

Der Grund liegt in den Zuständigkeiten. Die Berechtigungsnummer gehört den Verkehrsbetrieben, das Produkt dem Verkehrsbund. Jeder soll das sichern können, was ihm gehört — und keiner soll die Angaben eines anderen unbemerkt ändern können.

Nun eine Grenze, die beim Auswerten von Nachrichten oft überschätzt wird. In der Nachricht über Pias Abo stehen nur **Verweise** auf Schlüssel — Nummer, Version, Inhaber. Kein Schlüssel und kein Siegel über die Nachricht selbst.

Das heißt: Hätte jemand mit Systemzugang in dieser Nachricht das Gültigkeitsende von 2029 auf 2035 geändert, wäre das daran nicht erkennbar. Die Siegel entstehen erst, wenn ein Terminal die Daten auf die Karte schreibt.

Und schließlich ein Fall, in dem zwei gute Prinzipien kollidieren. Aus Datenschutzgründen werden in Kontrollnachweisen Fahrt- und Liniennummer geleert. Genau diese Felder waren Teil des Siegels. Also passt es danach nicht mehr — und das System nimmt diese Nachweise von der Prüfung aus.

Ein bewusster Tausch: weniger Beweiskraft für weniger Bewegungsdaten.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 3.1 (Ablehnung bei negativem Ergebnis der MAC-Prüfung und Ausstellung eines `TXA`), Kap. 5.1.2 (die zu leerenden Attribute sind Teil der MAC-Daten; Kennzeichnung und Ausnahme von der späteren MAC-Validierung) · *verbundspezifisch: eTicket RheinMain*
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (Schlüsselreferenzen `K_KVP-NM-MAC`, `K_PV-NM-MAC`, `K_ERF-NM-MAC`, `MK/K_TR-MAC` zu den jeweiligen Feldern der Berechtigung) · *verbundspezifisch*
- [Q11](../../QUELLEN.md#q11) – ausgewertete Nachricht (Schlüsselreferenzfelder mit Nummer, Version und Inhaber; MAC-Bildung durch das SAM beim Schreiben). **Nicht öffentliche Unterlage**; übernommen sind nur Feldnamen und Struktur.

<!-- GEN:siehe_auch -->
## Siehe auch

- [Schlüsselreferenz](schluesselreferenz.md)
- [TXA/TXB](../transaktionen/txa-txb.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
