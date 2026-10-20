---
titel: SAM-Datenobjekte (ASN.1)
englisch: SAM data objects in ASN.1
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/sam.md, lexikon/sicherheit/cv-zertifikat-in-eticore.md, lexikon/berechtigungen/statische-berechtigung-in-eticore.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › SAM-Datenobjekte (ASN.1)
<!-- /GEN:breadcrumb -->

# SAM-Datenobjekte (ASN.1)

Das Modul `sam` ([Q51](../../QUELLEN.md#q51)) beschreibt, was im SAM abgelegt ist.

- `SamFci` (`0x6F`) ist die Dateisteuerinformation: die Applikationskennung `aid` und in `SamProprietaryData` die `AppVersion`.
- `ProductIssuanceRights` (`0x7F29`) enthält die **Product Owner Tokens** des SAM. Ein `ProductOwnerToken` (`0x70`) zeigt, dass das SAM für diese Organisation Produkte ausgeben darf, und führt einen Zähler (`ProductIssuanceCounter`, `0x46`) der bereits autorisierten Ausgaben. Die Typbeschreibung nennt ihn teils je Organisation, teils je Produkt.
- `SamActivationRights` (`0x7F28`) und `ConfigurationAuthorisation` (`0x7F27`) listen die `SubjectAuthorisation`, die das SAM für Aktivierung beziehungsweise Konfiguration annimmt.
- `SigningPublicKey` (`0x7F22`) und `SigningPrivateKey` (`0x7F6D`) sind das **eine** Schlüsselpaar, mit dem das SAM über den Befehl `AUTHORISE_STATIC_ENTITLEMENT` statische Berechtigungen signiert. `KeyEstablishmentPublicKeys` (`0x7F32`) enthält öffentliche Schlüssel für den Schlüsselaufbau mit `COMPUTE_SESSIONKEYS`.
- `CertificateRepository` (`0x7F23`) legt Zertifikate ab, die andere im Gespräch mit dem SAM brauchen, damit das SAM leichter übertragbar ist.
- `IdentityData` (`0xA5`) bindet beim Autorisieren eine statische Berechtigung an eine Identität, etwa eine SCE-ID.

Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Ein SAM der BVB ist wie ein Tresor mit Beschriftung. Außen steht, was darin läuft: die Kennung seiner Anwendung und deren Version.

Im Tresor liegen Berechtigungen. Die wichtigste ist die Erlaubnis, für bestimmte Organisationen Produkte auszugeben. Für den Bären-Verkehrsbund (9020) steht darin zum Beispiel, dass dieses SAM seine Produkte ausgeben darf, und wie viele Ausgaben es schon autorisiert hat. Eine zweite Liste sagt, wer das SAM aktivieren oder neu einrichten darf.

Dazu kommt ein einziges Unterschriftenpaar. Wenn das SAM für Olli Tapsigs Einzelfahrschein eine statische Berechtigung signiert, benutzt es genau diesen Schlüssel. Soll das Ticket an eine Identität gebunden werden, kommt sie in diesem Moment mit hinein.

Und schließlich liegt im Tresor ein Mäppchen mit Zertifikaten, die das SAM selbst nicht braucht, aber seine Gesprächspartner. Wer das SAM weitergibt, gibt das Mäppchen mit.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `sam`: `SamFci`, `SamProprietaryData`, `ProductIssuanceRights`, `ProductOwnerToken`, `ProductIssuanceCounter`, `SamActivationRights`, `ConfigurationAuthorisation`, `SigningPublicKey`, `SigningPrivateKey`, `KeyEstablishmentPublicKeys`, `PublicKeyWithReference`, `CertificateRepository`, `IdentityData` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [SAM](sam.md) – das Sicherheitsmodul
- [CV-Zertifikat in etiCORE](cv-zertifikat-in-eticore.md) – die `SubjectAuthorisation`
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md) – was das Signaturpaar unterschreibt
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Secure Application Module](sam.md) (SAM)
- [CV-Zertifikat in etiCORE](cv-zertifikat-in-eticore.md)
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
