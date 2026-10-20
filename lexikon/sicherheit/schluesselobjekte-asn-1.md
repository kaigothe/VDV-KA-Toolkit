---
titel: Schlüsselobjekte (ASN.1)
englisch: key objects in ASN.1
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/datenformate/asn-1-typen-in-eticore.md, lexikon/sicherheit/schluesselarten.md, lexikon/sicherheit/cv-zertifikat.md, lexikon/sicherheit/sam.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Schlüsselobjekte (ASN.1)
<!-- /GEN:breadcrumb -->

# Schlüsselobjekte (ASN.1)

Schlüssel und Signaturen in `common` ([Q51](../../QUELLEN.md#q51)):

- `KeyReference` (`0x53`) kennzeichnet einen Schlüssel. In `SymmetricKeyInfo` zeigt sie die Schlüsselgeneration an; der Wert `0x00` darf nicht verwendet werden. Dazu kommt die OID des Verfahrens, etwa AES128 oder AES256.
- `SymmetricKey` verbindet diese Angaben mit dem Schlüsselmaterial: im SAM der Masterschlüssel, im Medium ein Paar aus Verschlüsselungs- und MAC-Schlüssel. `SymmetricKeys` und `SymmetricKeyDirectory` sind die Listen dazu.
- `PuKInfo` (`0x76`) ist ein Auszug aus einem Zertifikat: Subject, Berechtigungen, Gültigkeit und Parameter des öffentlichen Schlüssels. Daraus bestehen `RootCaKeychain` und `SupplementaryCaKeychain` für Stamm- und Unter-CAs.
- `SupportedCurves` und `SupportedSignatureAlgorithms` listen als OIDs auf, welche Kurven und Signaturverfahren ein Teilnehmer unterstützt.
- `AttestationSignature` (`0x9E`) ist ein Signaturwert, den ein SAM, ein Medium oder eine MOTICS-App berechnet hat.
- `PrivateKeyParameters` und `PrivateKeyWithReference` kommen nur beim GlobalPlatform-Befehl `STORE_DATA` mit gesichertem Nachrichtenaustausch vor, um private Schlüssel bei der Individualisierung einzuspielen.

Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Man stelle sich einen Schlüsselbund vor, an dem jeder Schlüssel ein Schild mit Nummer trägt. Die Nummer ist die Schlüsselreferenz, und sie sagt, welche Generation des Schlüssels gemeint ist. Die Nummer 0 ist ausdrücklich nicht erlaubt.

Im SAM der BVB liegt der Masterschlüssel. Auf Pias BärenKarte liegt dagegen ein Paar aus zwei Schlüsseln, einer zum Verschlüsseln und einer zum Beglaubigen. Zusätzlich führen beide Seiten ein Verzeichnis: Welche Schlüssel habe ich, und für welches Verfahren sind sie gedacht?

Außerdem gibt es das Beglaubigungsschreiben, das Zertifikat. Wer nicht das ganze Schreiben mitführen will, nimmt einen Auszug: Wer ist der Inhaber, was darf er, von wann bis wann gilt es, und welcher öffentliche Schlüssel gehört dazu? Das ist die `PuKInfo`. Eine Liste davon bildet die Kette der Stellen, denen das Gerät vertraut.

Die Signatur am Ende einer Bescheinigung ist der Stempel darunter. Sie stammt vom SAM, vom Medium oder von einer MOTICS-App.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `common`: `KeyReference`, `SymmetricKey`, `SymmetricKeyInfo`, `SymmetricKeys`, `SymmetricKeyDirectory`, `PuKInfo`, `RootCaKeychain`, `SupplementaryCaKeychain`, `SupportedCurves`, `SupportedSignatureAlgorithms`, `SignatureAlgorithmId`, `AttestationSignature`, `PrivateKeyParameters`, `PrivateKeyWithReference` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick
- [Schlüsselarten](schluesselarten.md) – die Schlüssel in der KA 1.x
- [CV-Zertifikat](cv-zertifikat.md) – das Zertifikat
- [SAM](sam.md) – das Sicherheitsmodul

<!-- GEN:siehe_auch -->
## Siehe auch

- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
- [Schlüsselarten](schluesselarten.md)
- [CV-Zertifikat](cv-zertifikat.md) (CVC)
- [Secure Application Module](sam.md) (SAM)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
