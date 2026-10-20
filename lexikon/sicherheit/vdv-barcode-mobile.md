---
titel: VDV-Barcode mobile+
englisch: VDV barcode mobile plus
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/datenformate/vdv-barcode.md, lexikon/sicherheit/motics.md]
quellen: [Q02, Q37, Q46]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › VDV-Barcode mobile+
<!-- /GEN:breadcrumb -->

# VDV-Barcode mobile+

Der VDV-Barcode mobile+ ist der **[VDV-Barcode](../datenformate/vdv-barcode.md) mit kryptographischem Kopierschutz** für statische Berechtigungen auf Smartphones. Normquelle ist die „KA STB-SPEC mobile+“, Anlage 1 zur KA STB-Spec ([Q46](../../QUELLEN.md#q46), Kap. 4, PDF-S. 7; [Q37](../../QUELLEN.md#q37)).

**Das Problem:** Ein gewöhnlicher Barcode lässt sich vervielfältigen, weshalb bei der Kontrolle ein Identifikationsmerkmal zu prüfen ist. Weil das Zeit kostet, wird dieser Teil der Fahrausweisprüfung nicht durchgehend geleistet; es ist davon auszugehen, „dass es zu Einnahmeverlusten aufgrund nicht erkannter Kopien kommt“ ([Q46](../../QUELLEN.md#q46), Kap. 4.2, PDF-S. 11).

**Die Lösung** bindet die statische Berechtigung **eindeutig an ein bestimmtes Mobilgerät**, „so dass jeder Versuch, die Berechtigung auf ein anderes Mobilgerät zu übertragen und dort zu nutzen oder auszudrucken, bei der Kontrolle erkannt wird“ ([Q46](../../QUELLEN.md#q46), Kap. 4.2, PDF-S. 11).

Dazu treten vier Bausteine zusammen ([Q46](../../QUELLEN.md#q46), Kap. 4.2, PDF-S. 11):

- Eine **[Secure Crypto Environment](schluesselarten.md)** als softwarebasierter Sicherheitskern. Sie bindet die App an das Smartphone und nimmt das Zertifikat mit dem kryptographischen Schlüssel auf.
- Der **[MOTICS](motics.md)**-Dienst, der den Sicherheitskern mit dem Sicherheitsmanagement von eTicket Deutschland verbindet.
- **Kurzzeitzertifikate** mit begrenzten Laufzeiten von jeweils drei Monaten.
- Ein **dynamisches Element**: Der signierte Barcode wird dynamisiert, etwa über ein in Abständen aktualisiertes Zeitmerkmal. „Dadurch tragen Kopien zum Zeitpunkt einer Kontrolle immer ein bereits veraltetes Merkmal“ und werden erkannt ([Q46](../../QUELLEN.md#q46), Kap. 2, PDF-S. 5).

**Für die Kontrollseite** bedeutet das ein Softwareupdate: Das Gerät muss auch das dynamische Element verarbeiten können. Der VDV-Barcode mobile+ ist **abwärtskompatibel** — aktualisierte Geräte lesen weiterhin herkömmliche VDV-Barcodes ([Q46](../../QUELLEN.md#q46), Kap. 4.2, PDF-S. 11).

## Einfach erklärt – Beispiel aus Bärstadt

Olli Tapsig kauft seine Einzelfahrscheine per App. Der Fahrschein erscheint als Barcode auf dem Bildschirm.

Nun ist ein Bildschirmfoto schnell gemacht. Olli könnte es seinem Nachbarn schicken, der damit ebenso einsteigt. Keine besondere Fertigkeit nötig, kein Werkzeug außer dem Handy.

**Wie man das bisher auffängt.** Petra Pranke prüft nicht nur den Barcode, sondern zusätzlich einen Ausweis. Nur so lässt sich sagen, ob der Fahrschein zu der Person gehört, die ihn vorzeigt. Das Verfahren funktioniert — nur dauert es. In einer vollen Straßenbahn auf der Linie 4 prüft man nicht dreißig Ausweise. Also wird es nicht durchgehend gemacht, und nicht erkannte Kopien kosten Geld.

**Was mobile+ anders macht.** Der Fahrschein wird an Ollis Telefon gefesselt. Drei Dinge greifen dabei ineinander.

Erstens hat Ollis App einen kleinen Tresor — einen Sicherheitskern, den er nie zu sehen bekommt. Darin liegt ein Schlüssel, der das Telefon kennt. Kopiert jemand die App samt Fahrscheinen auf ein anderes Telefon, bleibt der Tresor zurück.

Zweitens ist das Zertifikat kurzlebig: drei Monate. Wer etwas an sich bringt, hat es nicht lange.

Drittens — und das ist der schönste Teil — ändert sich der Barcode selbst. In das signierte Ticket wird ein Zeitmerkmal eingerechnet, das regelmäßig neu gebildet wird. Das Bildschirmfoto, das Olli seinem Nachbarn geschickt hat, trägt deshalb ein Merkmal von gestern. Petras Gerät sieht einen gültig signierten Fahrschein — mit einem Zeitstempel, der nicht mehr passt. Kopie erkannt, ohne einen Ausweis zu verlangen.

**Was das für Petras Gerät heißt.** Es braucht ein Update: Ohne Kenntnis des dynamischen Elements hält es den veralteten Code für einen Fehler statt für eine Kopie. Umgekehrt verliert es nichts — nach dem Update liest es weiterhin die gewöhnlichen Barcodes.

**Und was es für ein Prüfwerkzeug heißt.** Ein mobile+-Barcode, zweimal kurz hintereinander eingelesen, ist nicht zweimal derselbe Datensatz. Wer darauf prüft, ob zwei Lesungen identisch sind, hält genau den funktionierenden Kopierschutz für einen Fehler.

## Quellen

- [Q46](../../QUELLEN.md#q46) – Whitepaper Barcodes im ÖPNV (2021): Kap. 2, PDF-S. 5 (Dynamisierung des signierten Barcodes über ein in Abständen aktualisiertes Zeitmerkmal; Kopien tragen zum Kontrollzeitpunkt ein veraltetes Merkmal), Kap. 4, PDF-S. 7 (KA STB-SPEC mobile+ als Anlage 1 zur KA STB-Spec), Kap. 4.1, PDF-S. 8 (Identifikationsmerkmal bei der Kontrolle), Kap. 4.2, PDF-S. 11 (Zeitaufwand der Prüfung des Identifikationsmerkmals und Einnahmeverluste; eindeutige Bindung an ein Mobilgerät; Secure Crypto Environment als softwarebasierter Sicherheitskern mit zwei Funktionen; Mobile Ticketing Crypto Service zur Installation; Kurzzeitzertifikate mit drei Monaten Laufzeit; Softwareupdate der Kontrollgeräte für Zertifikat und dynamisches Element; Abwärtskompatibilität)
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht (2024), S. 4 (KA STB-SPEC mobile plus, „Kryptographischer Kopierschutz für statische Berechtigungen VDV-Barcode mobile+“, Version 1.12.0)
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 81 (Secure Crypto Environment: Schlüssel unveränderlich an mobiles Gerät und Ticketing-App gebunden, resistent gegen Auslesen und Kopieren)

<!-- GEN:siehe_auch -->
## Siehe auch

- [VDV-Barcode](../datenformate/vdv-barcode.md)
- [MOTICS](motics.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
