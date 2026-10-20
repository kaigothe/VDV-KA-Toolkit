---
titel: CV-Zertifikat in etiCORE
englisch: CV certificate in etiCORE
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/cv-zertifikat.md, lexikon/sicherheit/schluesselobjekte-asn-1.md, lexikon/sicherheit/pki.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › CV-Zertifikat in etiCORE
<!-- /GEN:breadcrumb -->

# CV-Zertifikat in etiCORE

Das **CV-Zertifikat** („card verifiable“) ist in etiCORE ein zweiteiliger Datensatz ([Q51](../../QUELLEN.md#q51), Modul `cv-certificates`): `CvCertificate` (Tag `0x7F21`) enthält den `certificateBody` und eine `signature`, die über den Rumpf „including tag and length“ gebildet wird.

Der `CertificateBody` (`0x7F4E`) enthält:
- `subject`: den Namen der Stelle, der der öffentliche Schlüssel gehört,
- `subjectAuthorisation`: die erlaubte Verwendung und die Rechte des Schlüssels,
- Beginn und Ende der Gültigkeit als Unix-Zeit,
- `certificateAuthorityReference`: das Subject des Schlüssels, mit dem unterschrieben wurde,
- `publicKeyParameters`: Algorithmenkennung (OID), öffentlicher Schlüssel und gegebenenfalls Domänenparameter,
- die Kennung des Signaturalgorithmus.

Die `SubjectAuthorisation` (`0x7F4C`) nennt die verantwortliche Organisation (`ownerId`) und optional die erlaubten Algorithmen, die zulässigen Befehlsköpfe (`CLA | INS | P1 | P2`) einer Chipkarten-APDU, eine relative Sicherheitsstufe des Hosts und ein Zugriffs-Token.

Ein Feld `keytype` wie bei den Zertifikaten der KA 1.x ([CV-Zertifikat](cv-zertifikat.md)) enthält die Struktur nicht; die Verwendung des Schlüssels ergibt sich aus der `SubjectAuthorisation` (abgeleitet). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Das Kontrollgerät T-4713 der BVB wird von den Stellen, denen es begegnet, nicht einfach geglaubt. Es hat eine Art beglaubigten Ausweis, das CV-Zertifikat.

Auf dem Ausweis steht erstens, wem er gehört: das Subject, also die Stelle, die den Schlüssel führt. Zweitens, was sie damit darf, die `SubjectAuthorisation`: Der Schlüssel gehört der BVB (9010). Er kann außerdem auf bestimmte Verfahren und bestimmte Befehle an die Karte beschränkt sein. Drittens steht darauf, von wann bis wann der Ausweis gilt, und viertens, wer ihn ausgestellt hat. Dann folgt der öffentliche Schlüssel selbst.

Unter dem Ganzen steht die Unterschrift der ausstellenden Stelle. Sie deckt auch die Längenangaben mit ab, nicht nur die Inhalte.

Der Unterschied zur KA 1.x ist, dass es dort ein Feld gibt, das die Art des Schlüssels als Zahl benennt, eine 1 für diesen, eine 7 für das Zertifikat einer CA. In etiCORE steht dieselbe Information nicht als Zahl da, sondern ergibt sich vermutlich aus den Rechten, die der Ausweis vergibt.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `cv-certificates`: `CvCertificate`, `CertificateBody`, `SubjectAuthorisation`, `PublicKeyParameters`, `AlgorithmIds`, `CommandHeaders`, `CertificateAuthorityReference`, `Signature`, `CertificateEffectiveTime`, `CertificateExpirationTime` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [CV-Zertifikat](cv-zertifikat.md) – das Zertifikat der KA 1.x
- [Schlüsselobjekte (ASN.1)](schluesselobjekte-asn-1.md) – Auszug aus dem Zertifikat (`PuKInfo`)
- [PKI](pki.md) – die Infrastruktur
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [CV-Zertifikat](cv-zertifikat.md) (CVC)
- [Schlüsselobjekte (ASN.1)](schluesselobjekte-asn-1.md)
- [Public Key Infrastructure](pki.md) (PKI)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
