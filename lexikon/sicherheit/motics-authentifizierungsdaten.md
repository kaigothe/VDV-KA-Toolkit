---
titel: MOTICS-Authentifizierungsdaten
englisch: MOTICS authentication data
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/motics.md, lexikon/sicherheit/vdv-barcode-mobile.md, lexikon/sicherheit/cv-zertifikat-in-eticore.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q02, Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › MOTICS-Authentifizierungsdaten
<!-- /GEN:breadcrumb -->

# MOTICS-Authentifizierungsdaten

Das Modul `motics` ([Q51](../../QUELLEN.md#q51)) hat fünf Typen. Kern ist `AuthenticationData` (`0x7F70`), der Datensatz im [MOTICS](motics.md)-Kopierschutzcontainer:

- `specVersion`: die Version der SCE, mit der der Container erzeugt wurde, etwa „MoticsX.Y.Z“;
- optional `contentType` und `applicationData`: Anwendungsdaten und die Angabe, wie sie aufgebaut sind (`contentType` nur zusammen mit `applicationData`);
- optional `randomData`: Zufallsdaten einer fremden Stelle in einem Challenge-Response-Ablauf;
- optional `timeStamp`: Erzeugungszeit;
- `sceSignatureAlgorithmId` und `sceSignature`: die Signatur über alles davor, einschließlich Tags und Längen;
- `sceCertificate`: das [CV-Zertifikat](cv-zertifikat-in-eticore.md) der SCE.

Die SCE (Secure Crypto Environment) ist eine logische Komponente auf dem Smartphone, die Schlüssel unveränderlich an das Gerät und die Ticket-App bindet; sie soll das Auslesen und Kopieren der Schlüssel verhindern ([Q02](../../QUELLEN.md#q02), S. 81).

Der Container belegt demnach, dass die Daten von einer bestimmten SCE stammen und zu einem Zeitpunkt entstanden, optional als Antwort auf eine Aufforderung (abgeleitet). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Stellen wir uns vor, Olli Tapsig hält sein Handy ans Kontrollgerät von Petra Pranke. Sein Ticket ist ein Barcode mit Kopierschutz. Petra will wissen, ob er wirklich auf Ollis Handy erzeugt wurde und nicht ein Foto davon ist.

Dazu kann ihr Gerät eine Zufallszahl mitsenden: „Unterschreibe mir diese Zahl.“ Ollis App lässt die SCE unterschreiben. Das ist das Sicherheitsfach im Handy, das seine Schlüssel nicht herausgibt. Die Antwort enthält die Zufallszahl, die Uhrzeit, die Version der SCE, die Unterschrift und das Zertifikat der SCE.

Petras Gerät prüft das Zertifikat und dann die Unterschrift. So ist ein Challenge-Response gedacht: Die Zufallszahl zeigt, dass die Antwort zu dieser Aufforderung gehört. Ein Foto vom Ticket hätte sie nicht.

Die Anwendungsdaten sind optional. Wenn welche dabei sind, sagt der Inhaltstyp, wie sie zu lesen sind. Ohne Anwendungsdaten gibt es keinen Inhaltstyp, denn die beiden gehören immer zusammen.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `motics`: `AuthenticationData`, `ContentType`, `ApplicationData`, `RandomData`, `TimeStamp` · *Release-Kandidat*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 81 (Eintrag *Secure Crypto Environment*)

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [MOTICS](motics.md) – der Dienst und der Container
- [VDV-Barcode mobile+](vdv-barcode-mobile.md) – der Kopierschutz
- [CV-Zertifikat in etiCORE](cv-zertifikat-in-eticore.md) – das mitgesendete Zertifikat
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [MOTICS](motics.md)
- [VDV-Barcode mobile+](vdv-barcode-mobile.md)
- [CV-Zertifikat in etiCORE](cv-zertifikat-in-eticore.md)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
