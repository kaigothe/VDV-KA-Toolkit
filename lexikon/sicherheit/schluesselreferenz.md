---
titel: Schlüsselreferenz
englisch: key reference
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/mac.md, lexikon/sicherheit/keymanagement.md]
quellen: [Q05, Q11]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Schlüsselreferenz
<!-- /GEN:breadcrumb -->

# Schlüsselreferenz

Eine Schlüsselreferenz benennt einen Schlüssel, **ohne ihn zu enthalten**. In Nachrichten des Aktionsmanagements erscheinen drei solche Felder, jeweils mit **Nummer, Version und Inhaber** ([Q11](../../QUELLEN.md#q11)):

| Feld | Inhaber im Beispiel |
|---|---|
| `amMKPV-NM-MAC_ID` | Produktverantwortlicher |
| `amMKKVP-NM-MAC_ID` | Kundenvertragspartner |
| `amMKERF-NM-MAC_ID` | Schlüsselorganisation |

[Q05](../../QUELLEN.md#q05), Kap. 2.1, zeigt die Entsprechung auf dem Medium: Felder der Berechtigung dienen zugleich als Referenz-ID für einen Schlüssel — `berBerechtigung_ID` für `K_KVP-NM-MAC`, `prodProdukt_ID` für `K_PV-NM-MAC`, `prodKeyOrganisation_ID` für `K_ERF-NM-MAC` und `MK/K_TR-MAC` · *verbundspezifisch*.

Bemerkenswert daran: **Dieselben Felder tragen zwei Aufgaben.** Die Produkt-ID sagt, welches Produkt vorliegt — und gleichzeitig, mit welchem Schlüssel der Eintrag gesichert ist (abgeleitet).

**Die Namensbildung ist systematisch** (abgeleitet): `MK` für Masterkey, `K` für den abgeleiteten Schlüssel, danach die Rolle (`PV`, `KVP`, `ERF`), dann der Gegenstand (`NM` für Nutzermedium, `TR` für Transaktion) und der Zweck (`MAC`).

**Warum nur Referenzen?** Ein Schlüssel darf ein Hintergrundsystem nie verlassen; die Referenz genügt, weil das [SAM](sam.md) des Terminals den passenden Schlüssel selbst besitzt oder ableiten kann (abgeleitet). Die Angabe der **Version** erlaubt zudem den Schlüsselwechsel: Alte und neue Generation lassen sich unterscheiden ([Q05](../../QUELLEN.md#q05), Kap. 2.1).

**Grenze für die Auswertung:** Aus einer Schlüsselreferenz folgt **nicht**, dass eine Prüfung erfolgreich war. Sie sagt nur, welcher Schlüssel zuständig ist (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Eine Schlüsselreferenz ist ein Zettel, auf dem steht, welcher Schlüssel gemeint ist — nicht der Schlüssel selbst.

In der Nachricht über Pias Abo stehen drei solche Zettel. Einer verweist auf einen Schlüssel des Bären-Verkehrsbunds, einer auf einen der Bärstädter Verkehrsbetriebe, einer auf einen der Schlüsselstelle. Jeder trägt drei Angaben: welche Nummer, welche Version, wessen Schlüssel.

Der Grund für diese Zurückhaltung ist offensichtlich: Ein geheimer Schlüssel hat in einer Nachricht nichts zu suchen. Er steckt im Sicherheitsbaustein des Terminals und verlässt ihn nie. Die Nachricht muss nur sagen, **welcher** gemeint ist.

Elegant ist, wo diese Verweise stehen. Sie haben nämlich keine eigenen Felder, sondern sind in den Fachdaten versteckt: Die Produktnummer sagt gleichzeitig „das ist Produkt 2001 des Verbunds" **und** „gesichert mit dem Schlüssel des Verbunds". Zwei Aussagen in denselben vier Byte.

Die Versionsangabe ist die unscheinbarste und praktisch wichtigste. Schlüssel werden irgendwann ausgetauscht — nach Jahren, oder wenn einer kompromittiert wurde. Ohne Versionsangabe würde jede Karte mit altem Schlüssel unprüfbar. Mit ihr weiß das Terminal: Diese Berechtigung wurde mit Version 1 gesichert, also prüfe ich mit Version 1.

Ein Hinweis zum Schluss, der beim Lesen von Nachrichten wichtig ist: Dass eine Schlüsselreferenz dasteht, sagt **nichts** darüber, ob eine Prüfung geklappt hat. Sie nennt nur den zuständigen Schlüssel. Ob das Siegel passte, steht an dieser Stelle nicht — und ein Werkzeug sollte das nicht behaupten.

## Quellen

- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht: die Felder `amMKPV-NM-MAC_ID`, `amMKKVP-NM-MAC_ID` und `amMKERF-NM-MAC_ID` mit jeweils Nummer, Version und Inhaber. **Nicht öffentliche Unterlage**; übernommen sind nur Feldnamen und Struktur.
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (Doppelfunktion der Felder als Fachdaten und Referenz-ID: `berBerechtigung_ID` für `K_KVP-NM-MAC`, `prodProdukt_ID` für `K_PV-NM-MAC`, `prodKeyOrganisation_ID` für `K_ERF-NM-MAC` und `MK/K_TR-MAC`) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [MAC](mac.md)
- [Keymanagement](keymanagement.md) (KM)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
