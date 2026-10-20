---
titel: VDV-Barcode
englisch: VDV barcode
parent: lexikon/datenformate.md
siehe_auch: [lexikon/berechtigungen/statische-berechtigung.md, lexikon/datenformate/tlv.md, lexikon/datenformate/uic-barcode.md, lexikon/sicherheit/vdv-barcode-mobile.md]
quellen: [Q02, Q07, Q10, Q12, Q25, Q34, Q37, Q45, Q46]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › VDV-Barcode
<!-- /GEN:breadcrumb -->

# VDV-Barcode

Der VDV-Barcode ist die Ausgabeform einer [statischen Berechtigung](../berechtigungen/statische-berechtigung.md) als 2D-Barcode ([Q02](../../QUELLEN.md#q02), S. 92). Normquelle ist die nicht öffentliche **KA STB-Spec**, „Spezifikation statischer Berechtigungen für 2D-Barcode-Tickets“, Inventarnummer 42 ([Q25](../../QUELLEN.md#q25), Kap. 3); für den Kopierschutz tritt die **KA STB-SPEC mobile+** hinzu ([Q37](../../QUELLEN.md#q37)).

Der Aufbau ist über eine Herstellerdokumentation im Detail belegt ([Q12](../../QUELLEN.md#q12)) · *Herstellerquelle*:

- Der Datensatz beginnt mit der **Kennung „VDV“** als OctetString und einer **Version**, im belegten Fall `0x19 0x00` für die KA-STB-Spec 1.9.0.0 (Tabelle 3-1, S. 12).
- Er enthält dieselben Datenelemente wie eine Berechtigung auf der Chipkarte: `berBerechtigung_ID`, `prodProdukt_ID`, `berGueltigkeitsbeginn`, `berGueltigkeitsende`, den [statischen produktspezifischen Teil](../berechtigungen/produktspezifischer-teil.md) mit [Tag 0xDB](tag-0xdb-fahrgast.md), dazu Angaben zu Terminal, Ort und SAM.
- Am Ende stehen **Füllbytes** `0x00`, damit das Ticket mindestens **111 Byte** lang ist.
- Der **Transaktion produktspezifische Teil** bleibt leer (`0x8A 0x00`).

**Sicherung:** Bei der Ausgabe wird eine digitale Signatur über die Ticketdaten gebildet, wofür ein [SAM](../sicherheit/sam.md) mit geheimem Signaturschlüssel nötig ist; geprüft wird sie über Signaturzertifikate, die eTicket Deutschland bereitstellt. Gegen Vervielfältigung schützt der Barcode nicht — deshalb ist zusätzlich ein **Identifikationsmerkmal** zu prüfen ([Q46](../../QUELLEN.md#q46), Kap. 4.1, PDF-S. 8), siehe [VDV-Barcode mobile+](../sicherheit/vdv-barcode-mobile.md). **Sperren ist dagegen möglich:** Ein gesperrtes Barcodeticket wird bei der Kontrolle erkannt und muss abgewiesen werden (PDF-S. 9). Als Nachweis der Fahrtanmeldung in IN/OUT-Systemen dient die Anlage **CIBO-STB** (PDF-S. 7).

Belegt sind die Produktnummern des Deutschlandtickets: **9999** regulär, **9998** Jobticket, **9995** Schüler ([Q12](../../QUELLEN.md#q12); vgl. [Q10](../../QUELLEN.md#q10)). Zur Abgrenzung siehe [UIC-Barcode](uic-barcode.md).

## Einfach erklärt – Beispiel aus Bärstadt

Der VDV-Barcode ist Pias Berechtigung — nur gedruckt statt auf einem Chip.

Das ist wörtlich zu nehmen. Es ist kein eigenes Format, das man neu lernen müsste. Es sind dieselben Datenelemente in derselben TLV-Verpackung: Berechtigungsnummer, Produktnummer, Gültigkeit von und bis, Fahrgastdaten. Wer die Chipkarte versteht, versteht den Barcode.

Drei Dinge kommen hinzu.

**Eine Kennung am Anfang.** Der Datensatz beginnt mit den Buchstaben „VDV" und einer Versionsangabe. Ein Lesegerät weiß also beim ersten Byte, womit es zu tun hat — nützlich in einer Welt, in der auf Handys auch UIC-Barcodes der Bahn und Hausformate von Anbietern liegen.

**Eine Signatur.** Weil ein Barcode nichts kann und sich nicht wehrt, muss die Echtheit im Datensatz selbst stecken.

**Füllbytes am Ende.** Der Datensatz wird mit Nullen auf mindestens 111 Byte aufgefüllt. Das ist zunächst verwunderlich — warum Platz verschwenden?

Der Grund dürfte in der Signatur liegen: Kryptografische Verfahren arbeiten mit festen Blockgrößen, und eine Mindestlänge vereinfacht das. Für eine Auswertung heißt es jedenfalls: Eine Kette von Nullbytes am Ende ist normal und kein Datenschrott.

Ein Beispiel aus der Praxis, das man sich merken kann: Beim Deutschlandticket hat das reguläre Produkt die Nummer **9999**, das Jobticket **9998**, das Schülerticket **9995**. Wer solche Nummern in einem Barcode sieht, weiß sofort, um welches Produkt es geht.

Und ein letzter Punkt, der Olli Tapsig betrifft. Der Inhalt eines Barcodes kann nach der Erzeugung nicht mehr verändert werden — eine Entwertung, eine Sperrung oder eine Stornierung hinterlässt dort keine Spur. Gesperrt werden kann das Ticket trotzdem, nur eben nicht auf dem Papier: Es kommt auf die Sperrliste, und das Kontrollgerät erkennt es dort und weist es ab. Was der Barcode von sich aus nicht verhindern kann, ist das Kopieren. Deshalb gibt es für Tickets auf dem Handy eine eigene Spezifikation für den Kopierschutz, und deshalb verlangt die Kontrolle eines gewöhnlichen Barcodes zusätzlich ein Identifikationsmerkmal.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 92 (statische Berechtigung als 2D-Barcode auf Papier oder mobilem Endgerät), S. 66 (Smartphone und Sicherheits-Papier als Träger)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA STB-Spec, Inventarnummer 42)
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht (2024), S. 4 (KA STB-SPEC und KA STB-SPEC mobile plus für den kryptographischen Kopierschutz des VDV-Barcode mobile+, Version 1.12.0)
- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings: Kennung „VDV“ als OctetString und Version `0x19 0x00` nach KA STB-SPEC_V190 Tabelle 3-1, S. 12; Füllbytes auf mindestens 111 Byte; leerer Transaktion produktspezifischer Teil `0x8A 0x00`; vollständige Feldliste; Produktnummern 9999, 9998 und 9995 des Deutschlandtickets · *Herstellerquelle, belegt Marktpraxis*
- [Q10](../../QUELLEN.md#q10) – KCD NRW, Technische Anforderung Deutschlandticket (Produktnummern und Kontrollvorgaben) · *verbundspezifisch*
- [Q34](../../QUELLEN.md#q34) – KCD NRW, Ergebnisdokument Deutschlandticket / UIC (Abgrenzung zum UIC-Barcode) · *Auswertung offen*
- [Q07](../../QUELLEN.md#q07) – RMV, Statische Berechtigung RMV-EFS, Datenlayout · *verbundspezifisch, Auswertung offen*

- [Q46](../../QUELLEN.md#q46) – Whitepaper Barcodes im ÖPNV (2021), Kap. 4, PDF-S. 7 (KA STB-Spec und ihre Anlagen; CIBO-STB für IN/OUT-Systeme), Kap. 4.1, PDF-S. 8 (digitale Signatur über die Ticketdaten bei der Ausgabe, SAM mit geheimem Signaturschlüssel, Prüfung über Signaturzertifikate von eTicket Deutschland, Vervielfältigung nicht verhinderbar, Identifikationsmerkmal bei der Kontrolle zu prüfen), Kap. 4.1, PDF-S. 9 (Sperrung von Barcodetickets, Erkennung und Abweisung bei der Kontrolle)
- [Q45](../../QUELLEN.md#q45) – ASM-Tool Glossar, S. 10 („2D-Barcode“: Ticketdaten und Sicherheitselemente im Barcode; generell ein statisches Element, dessen Inhalt nach der Generierung nicht mehr verändert werden kann, auch nicht durch Entwertung, Sperrung oder Stornierung)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Statische Berechtigung](../berechtigungen/statische-berechtigung.md) (StatBer)
- [TLV-Kodierung](tlv.md) (TLV)
- [UIC-Barcode](uic-barcode.md)
- [VDV-Barcode mobile+](../sicherheit/vdv-barcode-mobile.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
