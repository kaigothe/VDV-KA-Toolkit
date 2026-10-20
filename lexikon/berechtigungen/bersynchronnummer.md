---
titel: berSynchronNummer
englisch: entitlement synchronisation number
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/berstatus.md, lexikon/aktionsmanagement/aenderungsreferenz.md]
quellen: [Q02, Q05, Q11, Q50, Q51, Q52, Q55]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › berSynchronNummer
<!-- /GEN:breadcrumb -->

# berSynchronNummer

`berSynchronNummer` steht gemeinsam mit [`berStatus`](berstatus.md) im **dynamischen Teil** der Berechtigung, hat den Datentyp **`SequenceNumberOne`** mit einem Byte und den Wertebereich **0 bis 255** ([Q52](../../QUELLEN.md#q52), S. 135).

Die Normquelle beschreibt Zweck und Verhalten: „Die Synchronnummer wird bei Statusänderungen der Berechtigung inkrementiert. Dazu zählen insbesondere auch Sperr- und Entsperrvorgänge.“ Über sie kann ein offline arbeitendes Terminal erkennen, ob die letzte Statusänderung auf dem präsentierten Nutzermedium älter oder jünger ist als die Information, die es vom Hintergrundsystem hat ([Q52](../../QUELLEN.md#q52), S. 135).

**Zum Überlauf:** „Nach Erreichen von 0xff wird sie auf 0x00 inkrementiert.“ Die Hintergrundsysteme müssen diesen Überlauf verarbeiten können ([Q52](../../QUELLEN.md#q52), S. 135). Der Zähler läuft also um und endet nicht.

Welche Transaktionen zählen, nennt die KA AktM-SPEC: Ausgabe EFS, Sperrung EFS, Entsperrung EFS/AFB und Rücknahme EFS. Die Nummer bringt „alle entsprechenden Anwendungsfälle, die die Statusänderung ein und derselben Berechtigung betreffen, in eine chronologische Abfolge … unabhängig davon, ob sie innerhalb oder außerhalb des Aktionsmanagements stattfinden“ ([Q55](../../QUELLEN.md#q55), Kap. 4.1.2.2, S. 28).

**Zwei Zeitpunkte der Erhöhung:** Im Aktionsmanagement wird bereits **mit der Beauftragung** im KVP-System erhöht, damit der Wert unverändert über die Aktionsliste in den Transaktionsnachweis gelangt. Bei direkter Ausführung am Terminal erhöht **das Terminal** um eins.

Die Werte im Aktionsauftrag ([Q55](../../QUELLEN.md#q55), Kap. 4.1.2.2, S. 28):

| Aktion | Wert |
|---|---|
| Ausgabe | 1 |
| Entsperrung | letzte Statusänderung + 1 |
| Rücknahme, Nachweis liegt vor | dessen Nummer + 1 |
| Rücknahme, Entsperrnachweis fehlt | beauftragte Nummer + 1 |
| Rücknahme, Sperrnachweis fehlt | beauftragte Nummer + **2** |

In der ausgewerteten Nachricht trägt das Feld den Wert 1 bei leerer Änderungsreferenz und Status 7 — eine Neuausgabe ([Q11](../../QUELLEN.md#q11)).

**Prüfregel:** Stimmt die Nummer im Sperrlisteneintrag nicht mit dem Applikationsverzeichniseintrag überein, **erfolgt keine Statusänderung** auf dem Nutzermedium ([Q55](../../QUELLEN.md#q55), Kap. 4.1.2.2, Fußnote 27, S. 28).

## Einfach erklärt – Beispiel aus Bärstadt

Die Synchronnummer ist ein Zähler, und ihr Zweck ist, veraltete Informationen zu erkennen.

Das Problem, das sie löst, entsteht aus der Verzögerung im System. Pias Berechtigung liegt auf ihrer Karte. Gleichzeitig weiß das Hintergrundsystem der Bärstädter Verkehrsbetriebe etwas über diese Berechtigung. Und auf jedem Kontrollgerät liegt eine Liste, die irgendwann einmal aktuell war.

Vier Stellen, vier Stände, die auseinanderlaufen können.

Der Zähler schafft Ordnung: Jede Fassung einer Berechtigung trägt eine Nummer. Pias Abo wurde neu ausgegeben, also steht dort die 1. Wird es gesperrt, steht 2 darauf. Wird es wieder entsperrt, 3. Trifft das Kontrollgerät T-4712 mit einem Stand 2 auf eine Karte mit Stand 3, weiß es: Meine Information ist überholt.

Gezählt werden dabei nur die **Statusänderungen** — Ausgabe, Sperrung, Entsperrung, Rücknahme. Nicht jede Fahrt, nicht jede Kontrolle.

Jetzt kommt die Stelle, an der es interessant wird: **Der Zähler wird schon beim Auftrag erhöht, nicht erst bei der Ausführung.** Bodo Bärlauch beauftragt die Entsperrung, und in dem Moment steht im System bereits die neue Nummer. Sie reist mit der Aktionsliste zum Automaten und wird dort unverändert in den Nachweis geschrieben.

Das hat einen Grund und eine Folge. Der Grund: Alle Beteiligten sollen dieselbe Nummer für denselben Vorgang verwenden. Die Folge: Wenn ein Auftrag übersprungen wird, entsteht eine Lücke — eine Nummer, die vergeben wurde, zu der aber nie eine Ausführung kam. Genau daran erkennen die BVB, dass etwas schiefgelaufen ist, und schicken eine [Aktionsfreigabe](../aktionsmanagement/aktionsfreigabe.md).

Deshalb gibt es auch den merkwürdigen Fall „plus zwei“. Wird eine Rücknahme beauftragt, während eine Sperre noch unbestätigt in der Luft hängt, muss die Rücknahme zwei Schritte weiterzählen — denn die Sperre wird bei ihrer Ausführung ja selbst noch einen Schritt verbrauchen. Wer hier um eins zu niedrig zählt, bekommt eine Berechtigung, deren Nummern nicht mehr zusammenpassen.

Und das ist nicht harmlos. Ein Sperrlisteneintrag besteht aus der Kennung der Berechtigung **und** dieser Nummer. Stimmt die Nummer nicht mit der auf der Karte überein, dann wird die Karte **nicht** gesperrt. Die Sperre greift einfach nicht. Für ein Prüfwerkzeug ist das eine der wichtigsten Regeln überhaupt: Eine Sperre mit falscher Synchronnummer sieht aus wie eine Sperre, wirkt aber nicht.

Bemerkenswert ist noch die Größe: **ein Byte**. Nach 255 geht es bei 0 weiter — der Zähler läuft um. Das steht ausdrücklich so im Standard, zusammen mit der Auflage an die Hintergrundsysteme, damit umgehen zu können. Wer stattdessen annimmt, nach 255 sei Schluss, baut einen Fehler ein, der erst nach Jahren auffällt.

## Quellen

- [Q52](../../QUELLEN.md#q52) – KA HD_BOM-SPEC 1.12.0, S. 135: `berSynchronNummer`, Kardinalität 1..1, Wertebereich 0..255, Datentyp `SequenceNumberOne`; „Die Synchronnummer wird bei Statusänderungen der Berechtigung inkrementiert. Dazu zählen insbesondere auch Sperr- und Entsperrvorgänge.“; Erkennung älterer oder jüngerer Stände durch ein offline arbeitendes Terminal; „Nach Erreichen von 0xff wird sie auf 0x00 inkrementiert.“ sowie die Auflage, den Überlauf in den Hintergrundsystemen zu verarbeiten. Datentyp in Tab. 6-33 (S. 56). Exzerpt: [exzerpte/Q52.md](../../exzerpte/Q52.md) · *nicht öffentlich*
- [Q55](../../QUELLEN.md#q55) – KA AktM-SPEC 1.12.0, Kap. 4.1.2.2 (S. 28): die vier inkrementierenden Transaktionen, Zweck der chronologischen Abfolge, Erhöhung bereits mit der Beauftragung, Erhöhung durch das Terminal bei direkter Ausführung, die Rechenregeln für Ausgabe, Entsperrung und die drei Rücknahmefälle; Fußnote 27: Vergleich des Sperrlisteneintrags mit dem Applikationsverzeichniseintrag, bei Abweichung keine Statusänderung. Exzerpt: [exzerpte/Q55.md](../../exzerpte/Q55.md) · *nicht öffentlich*
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (PDF-S. 9): `berSynchronNummer` im dynamischen Teil, Datentyp `SequenceNumberOne` mit einem Byte · *verbundspezifisch: eTicket RheinMain*
- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht: Wert 1 bei leerer Änderungsreferenz und Status 7. **Nicht öffentliche Unterlage**; übernommen sind nur Feldname und Wert.
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`, Typ `TransitionCounter`: Nachfolgerin `entitlementTransitionCounter`, „increasing sequence number which indicates if an entitlement's state has been changed“ · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management_xsd`, Typ `EntitlementUnblockingActionListEntry`: Zuordnung des Altnamens · *Release-Kandidat*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE: **kein** Eintrag „Synchronnummer“ (geprüft am Inhaltsverzeichnis, S. 2–13)

<!-- GEN:siehe_auch -->
## Siehe auch

- [berStatus](berstatus.md)
- [Änderungsreferenz](../aktionsmanagement/aenderungsreferenz.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
