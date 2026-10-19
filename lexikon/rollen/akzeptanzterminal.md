---
titel: Akzeptanzterminal
abkuerzung: AKT
englisch: Medium Access Device
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/hintergrundsystem.md, lexikon/aktionsmanagement/aktionsliste.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Akzeptanzterminal
<!-- /GEN:breadcrumb -->

# Akzeptanzterminal

Ein Akzeptanzterminal ist die **Gesamtheit der Gerätetechnik — Hardware und Software —, die den Datenaustausch mit einem Nutzermedium ermöglicht**; das Glossar verweist dabei auf die ISO/IEC 14443 ([Q02](../../QUELLEN.md#q02), S. 21 f.).

Der Begriff ist bewusst weit und umfasst sieben Gerätearten ([Q02](../../QUELLEN.md#q02), S. 22):

- Geräte für die Erstellung kompletter Tickets, auf Chip und/oder Papier
- Geräte für das Anlegen und/oder Komplettieren von Tickets
- Geräte für den Abruf von Informationen und den Druck von Tickets und Belegen
- Geräte für das Laden von ÖPV-Werteinheiten
- mobile Geräte für die Kontrolle und/oder Entwertung von Tickets
- Geräte für das Freischalten und die Personalisierung der Applikation
- Geräte für die Erfassung von IN-OUT-Vorgängen in IN-OUT-Systemen

Das Akzeptanzterminal ist der **Oberbegriff**; konkrete Terminals sind Spezialisierungen davon. So beschreibt das Glossar die Aktionsliste als Liste auszuführender Aktionen „am Kundenvertragspartner-Terminal als Spezialisierung eines Akzeptanzterminals“ ([Q02](../../QUELLEN.md#q02), S. 19). Eigene Einträge bestehen für das Dienstleister-Terminal (S. 35), das Kundenvertragspartner-Terminal (S. 61) und das Vertriebsterminal (S. 97).

Das Akzeptanzterminal markiert die Grenze zum [Hintergrundsystem](hintergrundsystem.md), das die Daten „ab der Hierarchie der Akzeptanzterminals“ übernimmt ([Q02](../../QUELLEN.md#q02), S. 46).

Es ist zugleich der **einzige Ort**, an dem eine Transaktion im strengen Sinn stattfindet: ausschließlich zwischen Nutzermedium und Akzeptanzterminal unter Mithilfe eines SAM ([Q02](../../QUELLEN.md#q02), S. 96).

## Einfach erklärt – Beispiel aus Bärstadt

Der Begriff klingt nach Fahrkartenautomat, meint aber sehr viel mehr.

In Bärstadt sind Akzeptanzterminals: der Automat am Hauptbahnhof, das Lesegerät T-4712 daneben, das Gerät T-4711 im Kundencenter am Honigmarkt, das mobile Prüfgerät T-4713 von Petra Pranke und das Gerät T-4714 ohne Sicherheitsbaustein. Fünf sehr verschiedene Kisten, ein Oberbegriff.

Was sie gemeinsam haben, ist das Einzige, worauf es ankommt: Sie können mit einer Karte sprechen.

Die Liste im Glossar zeigt, wie unterschiedlich die Aufgaben sein können. Manche Geräte erzeugen komplette Tickets. Manche vervollständigen vorbereitete. Manche lesen nur und drucken einen Belegt aus. Manche laden Guthaben. Manche kontrollieren. Manche schalten eine neue Karte überhaupt erst frei. Und manche erfassen Ein- und Ausstiege für Check-in/Check-out-Systeme.

Dass all das denselben Namen trägt, hat einen praktischen Grund: Für den Rest des Systems ist nur wichtig, **dass** irgendwo ein Gerät Kontakt zur Karte hatte. Was das Gerät sonst kann, interessiert die Aktionsliste nicht. Pias Abo kann am Automaten, am Lesegerät oder im Kundencenter auf die Karte kommen — Hauptsache, sie hält die Karte irgendwo hin.

Und hier liegt die eigentliche Bedeutung dieses Begriffs. Das Akzeptanzterminal ist der einzige Ort im ganzen System, an dem wirklich etwas mit der Karte passiert. Alles andere — Verträge, Produkte, Aufträge, Abrechnungen — ist Vorbereitung oder Nachbereitung.

Deshalb verläuft hier auch die Grenze zum Hintergrundsystem: Davor stehen die Geräte, dahinter die Rechenzentren. Und deshalb ist der Satz „das Hintergrundsystem kann die Karte nicht beschreiben“ keine technische Schwäche, sondern eine Aussage über diese Grenze.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 21 f. („Akzeptanztechnik, Akzeptanzstellen, Akzeptanzterminal / Medium Access Device“: Definition als Gesamtheit der Gerätetechnik mit Verweis auf ISO/IEC 14443, Aufzählung der sieben Gerätearten; Abkürzungen AKT und MAD), S. 19 (KVP-Terminal als Spezialisierung eines Akzeptanzterminals), S. 35 (Dienstleister-Terminal), S. 46 (Abgrenzung zum Hintergrundsystem), S. 61 (KVP-Terminal), S. 96 (Transaktion findet ausschließlich zwischen Nutzermedium und Akzeptanzterminal unter Mithilfe eines SAM statt), S. 97 (Vertriebsterminal)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.5 (Verteilung der Aktionsliste auf die Akzeptanzterminals) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Hintergrundsystem](hintergrundsystem.md) (HGS)
- [Aktionsliste](../aktionsmanagement/aktionsliste.md) (TXAML)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
