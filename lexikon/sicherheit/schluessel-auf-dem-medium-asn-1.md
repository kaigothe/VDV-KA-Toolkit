---
titel: Schlüssel auf dem Medium (ASN.1)
englisch: keys on the user medium in ASN.1
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/schluesselobjekte-asn-1.md, lexikon/sicherheit/cv-zertifikat-in-eticore.md, lexikon/medien/verzeichnisse-auf-dem-medium-asn-1.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Schlüssel auf dem Medium (ASN.1)
<!-- /GEN:breadcrumb -->

# Schlüssel auf dem Medium (ASN.1)

Das Medium trägt Schlüssel und Zertifikate ([Q51](../../QUELLEN.md#q51), Modul `user-medium`):

- `PublicKeyUM` (`0x7F33`) ist der öffentliche Schlüssel des Mediums. Er dient dem Schlüsselaufbau im Befehl `COMPUTE_SESSIONKEYS` und den Signaturen in `INTERNAL_AUTHENTICATE` und `EXECUTE_ACTION`; dazu gehört die Kennung des Signaturverfahrens. `PrivateKeyUM` (`0x7F4A`) enthält den zugehörigen privaten Schlüssel.
- `AlternatePublicKeyUM` (`0x7F34`) ist ein zweiter Schlüssel, nur für `COMPUTE_SESSIONKEYS`. Er soll den Wechsel auf neue Schlüsselparameter erleichtern: Der Schlüssel mit den neuen Parametern wird `PublicKeyUM`, der mit den bisherigen `AlternatePublicKeyUM`. `AlternatePrivateKeyUM` (`0x7F4B`) ist der private Gegenpart.
- `CertificateChain` (`0x7F2F`) und `AlternateCertificateChain` (`0x7F35`) enthalten die Zertifikatsketten dazu, als Liste von [CV-Zertifikaten](../sicherheit/cv-zertifikat-in-eticore.md).
- `KeyReferenceList` (`0x7F7C`) listet Schlüsselreferenzen.
- `PkiDirectory` fasst zusammen: die Subjects der Stamm- und Unter-CAs (`RootCaSubjects`, `SupplementaryCaSubjects`, aus den `PuKInfo` des Schlüsselbunds) sowie die elliptischen Kurven von `PublicKeyUM` und `AlternatePublicKeyUM` (`PublicKeyUMEllipticCurveID`, `AlternatePublicKeyUMEllipticCurveID`).

Private Schlüssel erscheinen in der Beschreibung nur als Datenobjekte der Individualisierung ([Schlüsselobjekte](schluesselobjekte-asn-1.md)). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Pias BärenKarte hat ein eigenes Schlüsselpaar. Der öffentliche Teil darf jeder sehen, der private bleibt in der Karte. Der öffentliche Schlüssel dient dazu, mit einem Gerät einen gemeinsamen Sitzungsschlüssel zu vereinbaren und Aktionen zu unterschreiben.

Zum Schlüssel gehört eine Zertifikatskette, eine Reihe von Beglaubigungen, die von der Stelle, die Pias Schlüssel beglaubigt hat, bis zu einer Stelle reicht, der das Lesegerät von sich aus vertraut. Ohne die Kette wäre der Schlüssel einfach nur eine Zahl.

Jetzt kommt der Teil für Zeiten des Wechsels. Angenommen, die Parameter der Kartenschlüssel werden erneuert. Dann muss nicht über Nacht jede Karte ausgetauscht werden. Die Karte bekommt den neuen Schlüssel als ihren Hauptschlüssel und behält den alten als Zweitschlüssel. Denkbar ist, dass Geräte, die nur den alten Weg kennen, beim Aufbau der Sitzung weiter den Zweitschlüssel verwenden. Dazu ist der alternative Schlüssel gedacht: Er soll den Wechsel auf neue Parameter erleichtern.

Das PKI-Verzeichnis ist die Kurzfassung: wem die Karte vertraut und mit welchen Kurven sie rechnet.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `PublicKeyUM`, `PrivateKeyUM`, `AlternatePublicKeyUM`, `AlternatePrivateKeyUM`, `CertificateChain`, `AlternateCertificateChain`, `KeyReferenceList`, `PkiDirectory`, `RootCaSubjects`, `SupplementaryCaSubjects`, `PublicKeyUMEllipticCurveID`, `AlternatePublicKeyUMEllipticCurveID` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Schlüsselobjekte (ASN.1)](schluesselobjekte-asn-1.md) – die gemeinsamen Schlüsseltypen
- [CV-Zertifikat in etiCORE](cv-zertifikat-in-eticore.md) – das Zertifikat
- [Verzeichnisse auf dem Medium (ASN.1)](../medien/verzeichnisse-auf-dem-medium-asn-1.md) – das PKI-Verzeichnis im Überblick
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Schlüsselobjekte (ASN.1)](schluesselobjekte-asn-1.md)
- [CV-Zertifikat in etiCORE](cv-zertifikat-in-eticore.md)
- [Verzeichnisse auf dem Medium (ASN.1)](../medien/verzeichnisse-auf-dem-medium-asn-1.md)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
