---
titel: MOTICS
abkuerzung: MOTICS
englisch: Mobile Ticketing Crypto Service
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/vdv-barcode-mobile.md, lexikon/grundlagen/spezifikationsmodell.md]
quellen: [Q43, Q46]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › MOTICS
<!-- /GEN:breadcrumb -->

# MOTICS

**MOTICS steht für Mobile Ticketing Crypto Service** ([Q43](../../QUELLEN.md#q43), Kap. 5.2.1, PDF-S. 31 f., ASN.1-Modul `motics.asn`).

**Die Aufgabe im Betrieb:** Um das Zertifikat und den Sicherheitskern für den [VDV-Barcode mobile+](vdv-barcode-mobile.md) auf einem Smartphone zu installieren, wird der Mobile Ticketing Crypto Service genutzt. Er „stellt die Verbindung zwischen dem Sicherheitsmanagement [von] eTicket Deutschland und dem Sicherheitskern auf dem Smartphone des Fahrgastes her“ und wird von einem Chipkartenhersteller bereitgestellt ([Q46](../../QUELLEN.md#q46), Kap. 4.2, PDF-S. 11).

**In etiCORE wird daraus ein Datenformat.** Die „Motics Specification“ (`etiCORE SPEC-MOTICS`) „spezifiziert Aufbau und Einsatz des **MOTICS Kopierschutzcontainers** im Zusammenspiel mit Ticketerwerb und Ticketkontrolle“. Sie ist in der Fassung 3.0.0-rc.6 **noch nicht im Release enthalten** ([Q43](../../QUELLEN.md#q43), Kap. 2.2, PDF-S. 26).

Drei Spuren im selben Release zeigen, wie weit MOTICS dort hineinreicht:

- Die CipherSuite-Spezifikation legt die kryptographischen Algorithmen fest, „wie sie im Nutzermedium, [SAM](sam.md) und bei der Signatur von Barcodes oder im MOTICS zum Einsatz kommen“ ([Q43](../../QUELLEN.md#q43), Kap. 2.2, PDF-S. 25).
- Zu den Beispieldaten gehören „Signaturen für [statische Berechtigungen](../berechtigungen/statische-berechtigung.md) **mit und ohne Motics**“ ([Q43](../../QUELLEN.md#q43), Kap. 7.2, PDF-S. 36).
- Die Änderungshistorie nennt einen Anwendungsfall „Check MOTICS requirements“ auf der Terminalseite ([Q43](../../QUELLEN.md#q43), Kap. 1.1.4, PDF-S. 6).

Daraus folgt für eine Auswertung: Eine statische Berechtigung kann **mit oder ohne MOTICS-Container** vorliegen, und beide Formen sind vorgesehen (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

MOTICS ist der Dienst, der Ollis Telefon zu einem Ort macht, an dem ein Geheimnis liegen darf.

**Das Problem dahinter.** Der Kopierschutz des VDV-Barcode mobile+ beruht darauf, dass in Ollis App ein Sicherheitskern mit einem Zertifikat steckt. Nur: Wie kommt dieses Zertifikat dorthin? Es darf nicht in der App mitgeliefert werden, denn dann hätte jeder, der die App herunterlädt, dasselbe Geheimnis. Es muss einzeln und sicher auf genau dieses Telefon gebracht werden.

Das erledigt MOTICS. Der Dienst reicht die Verbindung durch — von der Sicherheitsstelle des Bärenland eTicket Service bis in den Tresor in Ollis App. Betrieben wird so ein Dienst von einem Chipkartenhersteller, also von jemandem, der genau diese Aufgabe aus der Chipkartenwelt kennt: Schlüssel in ein Stück Hardware bringen, das man nie in der Hand hält.

**Der Begriff wandert.** Unter etiCORE bezeichnet MOTICS nicht mehr nur den Dienst, sondern auch einen **Container** — einen definierten Datenbereich, der den Kopierschutz in das Ticket hineinbringt. Es gibt eine eigene Spezifikation dafür, die allerdings zum belegten Stand noch nicht Teil des Pakets war.

**Was das praktisch bedeutet.** Es gibt Barcodes mit MOTICS-Container und Barcodes ohne. Olli hat eines mit — sein Ticket ist an sein Telefon gebunden. Ein Papierfahrschein auf Sicherheitspapier, den Bodo Bärlauch im Kundencenter ausdruckt, hat keinen: Da gibt es kein Telefon, an das man binden könnte.

**Für ein Prüfwerkzeug** ist das die Kernaussage dieses Artikels. Das Fehlen eines MOTICS-Anteils ist kein Mangel. Es sagt nur, dass dieses Ticket seinen Kopierschutz nicht auf diesem Weg erhält. Dass es beide Formen gibt, ist in den Beispieldaten des Standards ausdrücklich vorgesehen — dort liegen Signaturen mit und ohne Motics nebeneinander.

## Quellen

- [Q43](../../QUELLEN.md#q43) – etiCORE Release Letter 3.0.0-rc.6: Kap. 1.1.4, PDF-S. 6 (Anwendungsfälle „Check MOTICS requirements“), Kap. 2.2, PDF-S. 25 (CipherSuite-Spezifikation: Algorithmen im Nutzermedium, SAM, bei der Signatur von Barcodes und im MOTICS), Kap. 2.2, PDF-S. 26 („Motics Specification“, SPEC-MOTICS, Aufbau und Einsatz des MOTICS-Kopierschutzcontainers im Zusammenspiel mit Ticketerwerb und Ticketkontrolle; im Release nicht enthalten), Kap. 5.2.1, PDF-S. 31 f. („Mobile Ticketing Crypto Service ASN.1 Data Type Description“, `motics.asn`), Kap. 7.2, PDF-S. 36 (Beispieldaten mit Signaturen für statische Berechtigungen mit und ohne Motics)
- [Q46](../../QUELLEN.md#q46) – Whitepaper Barcodes im ÖPNV (2021), Kap. 4.2, PDF-S. 11 (Installation von Zertifikat und Sicherheitskern über den Mobile Ticketing Crypto Service; Verbindung zwischen dem Sicherheitsmanagement von eTicket Deutschland und dem Sicherheitskern auf dem Smartphone; Bereitstellung durch einen Chipkartenhersteller)

<!-- GEN:siehe_auch -->
## Siehe auch

- [VDV-Barcode mobile+](vdv-barcode-mobile.md)
- [Spezifikationsmodell](../grundlagen/spezifikationsmodell.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
