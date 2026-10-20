---
titel: berSynchronNummer
englisch: entitlement synchronisation number
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/berstatus.md, lexikon/aktionsmanagement/aenderungsreferenz.md]
quellen: [Q02, Q05, Q11, Q50, Q51]
status: abgeleitet
offene_fragen: [O5]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › berSynchronNummer
<!-- /GEN:breadcrumb -->

# berSynchronNummer

`berSynchronNummer` steht gemeinsam mit [`berStatus`](berstatus.md) im **dynamischen Teil** der Berechtigung und hat den Datentyp **`SequenceNumberOne`** mit **einem Byte** ([Q05](../../QUELLEN.md#q05), Kap. 2.1) · *verbundspezifisch*.

Ein Byte bedeutet einen Wertebereich von 0 bis 255 (abgeleitet). Die Zahl der Änderungen an einer Berechtigung ist damit begrenzt; was bei Überlauf geschieht, ist nicht belegt (zu prüfen).

**Das Glossar enthält keinen Eintrag „Synchronnummer“** (geprüft am Inhaltsverzeichnis, [Q02](../../QUELLEN.md#q02), S. 2–13). Die Deutung stützt sich daher auf Feldname, Datentyp und Beobachtung.

Aus Name und Typ ergibt sich: Es ist ein **Versionszähler** der Berechtigung (abgeleitet). Der Wert 1 steht für den ersten Stand; bei Änderungen steigt der Zähler, sodass Systeme veraltete Stände erkennen können. In der ausgewerteten Nachricht trägt das Feld den Wert 1 bei gleichzeitig leerer Änderungsreferenz und Status 7 — eine Neuausgabe ([Q11](../../QUELLEN.md#q11)).

Dass Status und Synchronnummer **gemeinsam** im dynamischen Teil liegen und zusammen genau zwei Byte belegen, stützt diese Lesart: Es sind die beiden einzigen Angaben einer Berechtigung, die sich im Laufe ihres Lebens ändern (abgeleitet).

**Hinweis aus etiCORE:** Die Nachfolgerin heißt `entitlementTransitionCounter` und ist eine „increasing sequence number which indicates if an entitlement's state has been changed“; der Typ zählt „the number of times the status of an application or entitlement has changed“ ([Q51](../../QUELLEN.md#q51), Modul `user-medium`, Typ `TransitionCounter`; Zuordnung über [Q50](../../QUELLEN.md#q50), `po-oa-management_xsd`, Typ `EntitlementUnblockingActionListEntry`). Der Zähler zählt danach **Statuswechsel** (abgeleitet für die KA 1.x, O5).

**Offen** (zu prüfen, O5): Gilt das in der KA 1.x ebenso, und zählen auch inhaltliche Änderungen ohne Statuswechsel?

## Einfach erklärt – Beispiel aus Bärstadt

Die Synchronnummer ist ein Zähler, und ihr Zweck ist, veraltete Informationen zu erkennen.

Das Problem, das sie löst, entsteht aus der Verzögerung im System. Pias Berechtigung liegt auf ihrer Karte. Gleichzeitig weiß das Hintergrundsystem der Bärstädter Verkehrsbetriebe etwas über diese Berechtigung. Und auf jedem Kontrollgerät liegt eine Liste, die irgendwann einmal aktuell war.

Vier Stellen, vier Stände, die auseinanderlaufen können.

Der Zähler schafft Ordnung: Jede Fassung einer Berechtigung trägt eine Nummer. Pias Abo wurde neu ausgegeben, also steht dort die 1. Würde sein Status später wechseln, etwa durch eine Sperrung, stünde 2 darauf. So zählt es jedenfalls die Nachfolgerin in etiCORE. Trifft ein Gerät mit einem Stand 1 auf eine Karte mit Stand 2, weiß es: Meine Information ist überholt.

Das ist dasselbe Prinzip, das jede Textverarbeitung mit Versionsnummern verwendet — und dasselbe, das verhindert, dass eine ältere Datei eine neuere überschreibt.

Bemerkenswert ist die Größe: **ein Byte**. Es passen also 255 Änderungen in eine Berechtigung, dann ist der Zähler am Ende. Für ein Abo über drei Jahre ist das reichlich. Es zeigt aber, wie sparsam auf einer Chipkarte gerechnet wird — man hat für den Zähler kein zweites Byte vorgesehen.

Zwei Dinge sollte man nicht verwechseln, weil sie direkt nebeneinander stehen.

Der **Status** sagt, in welchem Zustand die Berechtigung ist: aktiv, gesperrt, zurückgenommen. Die **Synchronnummer** sagt, wie oft sie sich geändert hat. Eine Berechtigung mit Status 7 und Nummer 5 ist aktiv und war schon viermal anders.

Was offen bleibt: Ob eine Sperrung den Zähler erhöht, lässt sich aus den vorliegenden Unterlagen nicht sagen.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: Typ `TransitionCounter` (Tag `0x58`), Feld `entitlementTransitionCounter` · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `po-oa-management_xsd`: `berSynchronNummer` als `meta:old` von `entitlementTransitionCounter` · *Release-Kandidat*
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (PDF-S. 9): `berSynchronNummer` im dynamischen Teil der Berechtigung, Datentyp `SequenceNumberOne` mit einem Byte, gemeinsam mit `berStatus` genau zwei Byte · *verbundspezifisch: eTicket RheinMain*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE: **kein** Eintrag „Synchronnummer“ (geprüft am Inhaltsverzeichnis, S. 2–13)
- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht, Feld `berSynchronNummer` mit dem Wert 1 bei leerer Änderungsreferenz und Status 7. **Nicht öffentliche Unterlage**; übernommen sind nur Feldname und Wert.

<!-- GEN:siehe_auch -->
## Siehe auch

- [berStatus](berstatus.md)
- [Änderungsreferenz](../aktionsmanagement/aenderungsreferenz.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
