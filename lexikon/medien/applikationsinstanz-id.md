---
titel: Applikationsinstanz-ID
englisch: Application Instance ID
parent: lexikon/medien.md
siehe_auch: [lexikon/medien/nutzermedium.md, lexikon/rollen/ah.md]
quellen: [Q02, Q11]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Medien](../medien.md) › Applikationsinstanz-ID
<!-- /GEN:breadcrumb -->

# Applikationsinstanz-ID

„Die Applikationsinstanz befindet sich auf dem Nutzermedium, in der Regel innerhalb eines Chips. Diese Instanz wird mit Hilfe einer ID identifiziert. Sowohl **Schlüssel und Zertifikate** als auch die **Verwaltung von Nutzermedien** innerhalb der Systemkomponenten setzen auf diese Applikationsinstanz-ID auf. Aus Sicht des elektronischen Fahrgeldmanagements **identifiziert die Applikationsinstanz-ID das Nutzermedium eindeutig**.“ ([Q02](../../QUELLEN.md#q02), S. 24)

Drei Folgerungen ergeben sich daraus:

- Das Nutzermedium wird **nicht** über eine Chip-Seriennummer identifiziert, sondern über die ID der Applikation darauf (abgeleitet).
- Sperren und Entsperren beziehen sich auf die Applikationsinstanz, nicht auf „die Karte“ — der [Sperrlistenservice](../rollen/kose.md) führt Sperreinträge für Applikationen ([Q02](../../QUELLEN.md#q02), S. 54).
- Gemeinsam mit der Applikationsinstanz-ID können im Hintergrundsystem **Personendaten** hinterlegt sein; fehlen sie, ist die Applikation anonym ([Q02](../../QUELLEN.md#q02), S. 22).

Der [Applikationsherausgeber](../rollen/ah.md) ist verantwortlich für die Bereitstellung von Informationen über die Applikationsinstanz-ID bei Anfragen zu **defekten Nutzermedien** und implementiert ein Zertifikatsmanagement für alle Applikationsinstanzen ([Q02](../../QUELLEN.md#q02), S. 23). Bei einer unlesbaren Karte ist die ID damit die letzte verbleibende Spur (abgeleitet).

In Aktionslisteneinträgen steht die ID im Feld `appInstanz_ID` als **Zielmedium** der Aktion, zusammen mit der Organisations-ID des ausgebenden Kundenvertragspartners ([Q11](../../QUELLEN.md#q11)).

## Einfach erklärt – Beispiel aus Bärstadt

Wenn in Bärstadt von „Pias Karte" die Rede ist, meint das System etwas Genaueres: die Applikationsinstanz 90000042.

Der Unterschied wird im Verlustfall praktisch. Pia meldet ihre BärenKarte als verloren. Bodo Bärlauch sperrt daraufhin nicht ein Stück Plastik, sondern diese Nummer. Sie wandert auf die Sperrliste, und jedes Kontrollgerät im Bärenland weiß von da an: 90000042 gilt nicht mehr.

Pia bekommt eine Ersatzkarte, und die trägt die Instanz 90000043. Für das System ist das ein völlig anderes Medium — auch wenn Pia dieselbe Person mit demselben Abo ist.

Zwei Dinge hängen an dieser Nummer, und beide sind wichtig.

**Erstens die Schlüssel.** Die kryptografischen Schlüssel und Zertifikate einer Karte sind an die Applikationsinstanz gebunden. Das ist der Grund, warum eine Ersatzkarte nicht einfach eine Kopie sein kann: Sie hat eigene Schlüssel, weil sie eine eigene Instanz ist.

**Zweitens die Personendaten.** Was die Verkehrsbetriebe über Pia wissen, hängt im Hintergrundsystem an dieser Nummer. Sie ist das Bindeglied zwischen der Karte in ihrer Tasche und ihrem Vertrag im Rechenzentrum.

Besonders aufschlussreich ist eine Aufgabe des Applikationsherausgebers: Er muss Auskunft über die Applikationsinstanz-ID geben können, wenn jemand mit einem **defekten** Nutzermedium ankommt.

Man stelle sich das vor: Pias Karte ist durch die Waschmaschine gegangen, der Chip antwortet nicht mehr. Niemand kann mehr auslesen, was darauf war. Was bleibt, ist die Nummer — und über sie findet man den Vertrag, die Berechtigung und den Weg zu einer Ersatzkarte.

Deshalb steht diese ID auch gedruckt auf der Karte.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 24 („Applikationsinstanz-ID / Application Instance ID“: Lage auf dem Nutzermedium, Identifikation der Instanz, Aufsetzen von Schlüsseln, Zertifikaten und Medienverwaltung auf dieser ID, eindeutige Identifikation des Nutzermediums aus Sicht des EFM), S. 22 (Hinterlegung von Personendaten im Hintergrundsystem gemeinsam mit der ID, Anonymität), S. 23 (Verantwortung des Applikationsherausgebers für Informationen zur Applikationsinstanz-ID bei defekten Nutzermedien, Zertifikatsmanagement), S. 54 (Sperreinträge für Applikationen beim Sperrlistenservice)
- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht, Feld `appInstanz_ID` als Zielmedium der Aktion samt Org-ID des KVP. **Nicht öffentliche Unterlage**; übernommen ist nur der Feldname.

<!-- GEN:siehe_auch -->
## Siehe auch

- [Nutzermedium](nutzermedium.md) (NM)
- [Applikationsherausgeber](../rollen/ah.md) (AH)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Medien](../medien.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
