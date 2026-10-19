---
titel: VDV-Barcode
englisch: VDV barcode
parent: lexikon/datenformate.md
siehe_auch: [lexikon/berechtigungen/statische-berechtigung.md, lexikon/datenformate/tlv.md]
quellen: [Q02, Q07, Q10, Q12, Q25, Q34, Q37]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › VDV-Barcode
<!-- /GEN:breadcrumb -->

# VDV-Barcode

Der VDV-Barcode ist die Ausgabeform einer [statischen Berechtigung](../berechtigungen/statische-berechtigung.md) als 2D-Barcode ([Q02](../../QUELLEN.md#q02), S. 92). Normquelle ist die nicht öffentliche **KA STB-Spec**, „Spezifikation statischer Berechtigungen für 2D-Barcode-Tickets“, Inventarnummer 42 ([Q25](../../QUELLEN.md#q25), Kap. 3); für den Kopierschutz tritt die **KA STB-SPEC mobile plus** hinzu, „Kryptographischer Kopierschutz für statische Berechtigungen VDV-Barcode mobile+“ ([Q37](../../QUELLEN.md#q37)).

Der Aufbau ist über eine Herstellerdokumentation im Detail belegt ([Q12](../../QUELLEN.md#q12)) · *Herstellerquelle*:

- Der Datensatz beginnt mit der **Kennung „VDV“** als OctetString und einer **Version** — im belegten Fall `0x19 0x00` für die Fassung 1.9.0.0 der KA-STB-Spec (Tabelle 3-1, S. 12).
- Er enthält dieselben Datenelemente wie eine Berechtigung auf der Chipkarte: `berBerechtigung_ID`, `prodProdukt_ID`, `berGueltigkeitsbeginn`, `berGueltigkeitsende`, den [statischen produktspezifischen Teil](../berechtigungen/produktspezifischer-teil.md) mit [Tag 0xDB](tag-0xdb-fahrgast.md), dazu Angaben zu Terminal, Ort und SAM.
- Am Ende stehen **Füllbytes** `0x00`, damit das Ticket mindestens **111 Byte** lang ist.
- Der **Transaktion produktspezifische Teil** bleibt leer (`0x8A 0x00`), weil er beim TLV-EFS nicht benutzt wird.

Daran ist die Verwandtschaft ablesbar: Der Barcode ist **kein eigenes Format**, sondern dieselbe TLV-Struktur in einem anderen Träger, ergänzt um Kennung, Version, Signatur und Auffüllung (abgeleitet).

Als Beispiel der Anwendung sind die Produktnummern des Deutschlandtickets belegt: **9999** für das reguläre Ticket, **9998** für das Jobticket, **9995** für Schüler ([Q12](../../QUELLEN.md#q12), gestützt auf die Technische Anforderung Deutschlandticket; vgl. [Q10](../../QUELLEN.md#q10)). Zur Abgrenzung gegenüber dem UIC-Barcode siehe [Q34](../../QUELLEN.md#q34).

## Einfach erklärt – Beispiel aus Bärstadt

Der VDV-Barcode ist Pias Berechtigung — nur gedruckt statt auf einem Chip.

Das ist wörtlich zu nehmen. Es ist kein eigenes Format, das man neu lernen müsste. Es sind dieselben Datenelemente in derselben TLV-Verpackung: Berechtigungsnummer, Produktnummer, Gültigkeit von und bis, Fahrgastdaten. Wer die Chipkarte versteht, versteht den Barcode.

Drei Dinge kommen hinzu.

**Eine Kennung am Anfang.** Der Datensatz beginnt mit den Buchstaben „VDV" und einer Versionsangabe. Ein Lesegerät weiß also beim ersten Byte, womit es zu tun hat — nützlich in einer Welt, in der auf Handys auch UIC-Barcodes der Bahn und Hausformate von Anbietern liegen.

**Eine Signatur.** Weil ein Barcode nichts kann und sich nicht wehrt, muss die Echtheit im Datensatz selbst stecken.

**Füllbytes am Ende.** Der Datensatz wird mit Nullen auf mindestens 111 Byte aufgefüllt. Das ist zunächst verwunderlich — warum Platz verschwenden?

Der Grund dürfte in der Signatur liegen: Kryptografische Verfahren arbeiten mit festen Blockgrößen, und eine Mindestlänge vereinfacht das. Für eine Auswertung heißt es jedenfalls: Eine Kette von Nullbytes am Ende ist normal und kein Datenschrott.

Ein Beispiel aus der Praxis, das man sich merken kann: Beim Deutschlandticket hat das reguläre Produkt die Nummer **9999**, das Jobticket **9998**, das Schülerticket **9995**. Wer solche Nummern in einem Barcode sieht, weiß sofort, um welches Produkt es geht.

Und ein letzter Punkt, der Olli Tapsig betrifft: Weil der Barcode nicht veränderbar ist, kann man ihn nicht sperren. Deshalb gibt es inzwischen eine eigene Spezifikation für den Kopierschutz — ein Datensatz, der sich beliebig vervielfältigen lässt, wäre sonst eine offene Flanke.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 92 (statische Berechtigung als 2D-Barcode auf Papier oder mobilem Endgerät), S. 66 (Smartphone und Sicherheits-Papier als Träger)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA STB-Spec, Inventarnummer 42)
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht (2024), S. 4 (KA STB-SPEC und KA STB-SPEC mobile plus für den kryptographischen Kopierschutz des VDV-Barcode mobile+, Version 1.12.0)
- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings: Kennung „VDV“ als OctetString und Version `0x19 0x00` nach KA STB-SPEC_V190 Tabelle 3-1, S. 12; Füllbytes auf mindestens 111 Byte; leerer Transaktion produktspezifischer Teil `0x8A 0x00`; vollständige Feldliste; Produktnummern 9999, 9998 und 9995 des Deutschlandtickets · *Herstellerquelle, belegt Marktpraxis*
- [Q10](../../QUELLEN.md#q10) – KCD NRW, Technische Anforderung Deutschlandticket (Produktnummern und Kontrollvorgaben) · *verbundspezifisch*
- [Q34](../../QUELLEN.md#q34) – KCD NRW, Ergebnisdokument Deutschlandticket / UIC (Abgrenzung zum UIC-Barcode) · *Auswertung offen*
- [Q07](../../QUELLEN.md#q07) – RMV, Statische Berechtigung RMV-EFS, Datenlayout · *verbundspezifisch, Auswertung offen*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Statische Berechtigung](../berechtigungen/statische-berechtigung.md) (StatBer)
- [TLV-Kodierung](tlv.md) (TLV)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
