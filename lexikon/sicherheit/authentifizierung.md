---
titel: Authentifizierung
englisch: authentication
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/schluesselarten.md, lexikon/sicherheit/schluessel-auf-dem-medium-asn-1.md, lexikon/sicherheit/cv-zertifikat-in-eticore.md, lexikon/transaktionen/fehlercodes-der-terminalanteile.md]
quellen: [Q02, Q50, Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Authentifizierung
<!-- /GEN:breadcrumb -->

# Authentifizierung

Bei einer **Authentifizierung** zwischen zwei Instanzen „authentisiert sich die Eine, während die Andere die Erstere authentifiziert“: Die erste legt Informationen zur Echtheitsprüfung vor, die zweite verifiziert sie. Die Authentifizierung prüft also die Behauptung der Echtheit und wird auch im Sinne einer Identitätsfeststellung verwendet ([Q02](../../QUELLEN.md#q02), S. 29).

Im Glossar steht das Beispiel eines Programms: Der Benutzer behauptet seine Zugangsberechtigung mit dem Benutzernamen und authentisiert sich mit dem Kennwort; das Programm identifiziert ihn und authentifiziert ihn dann ([Q02](../../QUELLEN.md#q02), S. 29).

In der KA 1.x werden symmetrische Schlüssel für die gegenseitige Authentisierung der Komponenten benutzt, daneben für authentische Nachweise von Berechtigungsausgaben und Bezahlvorgängen. In etiCORE entfallen die symmetrischen Schlüssel der Product Owner und CCP; die für die gegenseitige Authentisierung bleiben. Statt Regulär- und Notfallversion gibt es ein Schlüsselregister mit Schlüsselgenerationen ([Q02](../../QUELLEN.md#q02), S. 93).

Beispiele aus den etiCORE-Typen und -Codes ([Q50](../../QUELLEN.md#q50), [Q51](../../QUELLEN.md#q51)): ein optionales Kennwort auf dem Medium (`UserAuthenticationData`, Fehler `E_EUI_WRONG_PASSWORD`), die Signaturen von Medium und SAM (`INTERNAL_AUTHENTICATE`, [Schlüssel auf dem Medium](schluessel-auf-dem-medium-asn-1.md)) und die Prüfung des Absenders gegen das TLS-Zertifikat (`E_IONC_HEADER_TO_TLS_CERTIFICATE_MISMATCH`). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Das Wort klingt nach Amtsdeutsch, die Sache kennt jeder. Am Eingang des Kundencenters am Honigmarkt muss Bodo Bärlauch beweisen, dass er dort arbeitet.

Er sagt seinen Namen: Das ist die Behauptung. Er hält seinen Mitarbeiterausweis ans Lesegerät: Das ist das Authentisieren, er legt etwas vor, das nur er haben sollte. Das System prüft den Ausweis: Das ist das Authentifizieren, es stellt fest, dass die Behauptung stimmt. Der Ausweis ist ein Beleg. Das System glaubt ihm nur, weil es der ausstellenden Stelle vertraut.

Genauso unterhalten sich Pias BärenKarte und das Lesegerät T-4712. Beide beweisen einander, dass sie echt sind, bevor die Karte etwas herausgibt. Dazu dienen Schlüssel.

Die Karte kann auch Pia fragen, ob sie es wirklich ist, wenn ein Kennwort eingerichtet wurde. Dann ist Pia selbst die authentisierende Seite. Wer das Kennwort zu oft falsch eingibt, dessen Kennwort wird gesperrt. Ein falsches Kennwort hat einen eigenen Fehlercode.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 29 (*Authentifizierung / Authentication*), S. 93 (symmetrische Schlüssel) (wörtliche Definition und Versionsunterschied)
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `UserAuthenticationData`, `PublicKeyUM` · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: `E_EUI_WRONG_PASSWORD`, `E_IONC_HEADER_TO_TLS_CERTIFICATE_MISMATCH` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Schlüsselarten](schluesselarten.md) – die Schlüssel der KA
- [Schlüssel auf dem Medium (ASN.1)](schluessel-auf-dem-medium-asn-1.md) – Schlüssel im Medium
- [CV-Zertifikat in etiCORE](cv-zertifikat-in-eticore.md) – der Beleg
- [Fehlercodes der Terminalanteile](../transaktionen/fehlercodes-der-terminalanteile.md) – falsches Kennwort

<!-- GEN:siehe_auch -->
## Siehe auch

- [Schlüsselarten](schluesselarten.md)
- [Schlüssel auf dem Medium (ASN.1)](schluessel-auf-dem-medium-asn-1.md)
- [CV-Zertifikat in etiCORE](cv-zertifikat-in-eticore.md)
- [Fehlercodes der Terminalanteile](../transaktionen/fehlercodes-der-terminalanteile.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
