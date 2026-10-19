---
titel: TXAML
abkuerzung: TXAML
englisch: action list transaction
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/aktionsmanagement/aktionsliste.md, lexikon/transaktionen/tx-base.md]
quellen: [Q06, Q25, Q39]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › TXAML
<!-- /GEN:breadcrumb -->

# TXAML

`TXAML` ist die Nachricht, mit der eine [Aktionsliste](../aktionsmanagement/aktionsliste.md) übertragen wird. Die Struktur ist der nicht öffentlichen KA AktM-SPEC zu entnehmen ([Q06](../../QUELLEN.md#q06), Kap. 4.3.1; [Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 41). `TXAML` ist damit die einzige der hier behandelten Nachrichten, deren Struktur **nicht** aus der KA SST-SPEC stammt.

Angefordert wird sie mit der Nachricht `TXAS`; `TXAML` ist die Antwort darauf, und der Austausch läuft **synchron** ([Q39](../../QUELLEN.md#q39), Kap. 3.2.5) · *verbundspezifisch*.

Sie wird nicht zugestellt, sondern **abgeholt**. Der Ablauf ([Q06](../../QUELLEN.md#q06), Kap. 3.1) · *verbundspezifisch*:

1. Der Aufrufer lädt die Manifest-Datei herunter.
2. Er prüft anhand der Nachrichtentypen und der Nachricht-ID gegen lokal gespeicherte Informationen, ob eine neue Nachricht vorliegt.
3. Nur wenn eine neue Nachricht existiert, lädt er sie herunter — also die aktuelle Version der Aktionsliste.

Der Download erfolgt über eine eigene Schnittstelle, die die angeforderte Aktionsliste für den Aufrufer zurückliefert; die Nachricht-ID der Aktionsliste steht in der Manifest-Datei ([Q06](../../QUELLEN.md#q06), Kap. 3.4, 3.2).

Das Abfrageintervall ist auf **einmal täglich** festgelegt, weil Sperr- und Aktionslisten auch nur einmal täglich erstellt und bereitgestellt werden. Ruft ein Terminalmanagementsystem die Listen permanent ab, wertet das System dies als Fehlfunktion und lehnt den Aufruf ab ([Q06](../../QUELLEN.md#q06), Kap. 3.2) · *verbundspezifisch*.

Im Anwendungsfall „Aktionsliste herunterladen“ trägt der Empfänger im [`TX_BASE`](tx-base.md) die Rolle **PV (3)** ([Q06](../../QUELLEN.md#q06), Kap. 4.10).

## Einfach erklärt – Beispiel aus Bärstadt

Die Aktionsliste wird nicht geschickt, sie wird geholt. Dieser Unterschied prägt den ganzen Ablauf.

Das Terminalmanagementsystem der Bärstädter Verkehrsbetriebe fragt nicht einfach jeden Morgen die komplette Liste ab. Es schaut zuerst in ein Inhaltsverzeichnis, das Manifest. Dort steht, welche Nachrichten gerade bereitliegen und welche Nummer sie tragen.

Dann vergleicht es: Kenne ich diese Nummer schon? Wenn ja, ist nichts Neues passiert, und es wird nichts geladen. Wenn nein, holt es die Liste.

Das ist derselbe Mechanismus, den ein Browser für Bilder nutzt, und er spart viel: Die Liste kann groß sein, und sie ändert sich nur einmal am Tag.

Apropos einmal am Tag — darin steckt eine Regel mit Zähnen. Weil die Listen ohnehin nur täglich neu entstehen, ist auch der Abruf auf einmal täglich festgelegt. Und wenn ein Terminalmanagementsystem trotzdem dauernd nachfragt, wird das nicht achselzuckend hingenommen: Das Hintergrundsystem betrachtet das als Fehlfunktion und weist den Aufruf ab.

Das ist ungewöhnlich deutlich für ein Pflichtenheft und verrät etwas über den Betrieb. Ein defektes Gerät, das im Sekundentakt anfragt, kann ein Hintergrundsystem lahmlegen, an dem viele Verkehrsunternehmen hängen. Also wird nicht auf Vernunft gehofft, sondern abgeriegelt.

Ein Detail für das Lesen von Nachrichten: Wenn die BVB die Aktionsliste anfordert, steht im Briefkopf als Empfänger die Rolle „Produktverantwortlicher“ — also der Bären-Verkehrsbund, nicht ALISE. Das passt zum Standard, denn der Aktionslistenservice ist ein Dienst des PV-Systems.

Und noch eine Besonderheit: `TXAML` ist die einzige Nachricht dieser Kategorie, deren Aufbau nicht in der allgemeinen Schnittstellenspezifikation steht, sondern in der eigenen Spezifikation für das Aktionsmanagement.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.3.1 (`TXAML` aus `[KA_SPEC_AktM]`), Kap. 3.1 (Ablauf des Nachrichtenabrufs über das Manifest), Kap. 3.2 (Manifest, Intervall einmal täglich, Ablehnung bei permanentem Abruf), Kap. 3.4 (Aktionsliste herunterladen, Nachricht-ID), Kap. 4.10 (Rolle PV = 3 als Empfänger im Anwendungsfall „Aktionsliste herunterladen“) · *verbundspezifisch: eTicket RheinMain*
- [Q39](../../QUELLEN.md#q39) – RMV vHGS-Vertrag, Kap. 3.2.5 (`TXAS` als Anforderung, `TXAML` als synchrone Antwort) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA AktM-SPEC, Inventarnummer 41)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
