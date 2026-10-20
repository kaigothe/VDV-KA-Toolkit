---
titel: Scheme Manager
englisch: scheme manager
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/ah.md, lexikon/sicherheit/asm.md, lexikon/sicherheit/esh.md, lexikon/kontrolle/hotlist-service.md]
quellen: [Q02, Q50]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Scheme Manager
<!-- /GEN:breadcrumb -->

# Scheme Manager

Der **Scheme Manager** ist „die oberste Instanz“ von eTicket Deutschland; diese Aufgabe übernimmt VDV-ETS ([Q02](../../QUELLEN.md#q02), S. 78). Er verbindet die Rollen Applikationsherausgeber, Registrierung und Sicherheitsmanager aus ISO 24014-1, erstellt die Vorschriften und überwacht sie. Er existiert einmal im System und identifiziert sich eindeutig. Die meisten seiner Services setzt das [ASM](../sicherheit/asm.md) um; dazu kommt ein Kundenservice für Verkehrsunternehmen und Hersteller ([Q02](../../QUELLEN.md#q02), S. 78).

Der [Applikationsherausgeber](ah.md) ist Teil des Scheme Managers ([Q02](../../QUELLEN.md#q02), S. 23); auch die Zertifizierung ist eine Rolle des Scheme Managers: Sie legt die Zertifizierungsverfahren fest, zertifiziert die Systemkomponenten und stellt Zertifikate aus ([Q02](../../QUELLEN.md#q02), S. 100).

Die etiCORE-Schnittstellen zeigen, wo der Scheme Manager im Betrieb auftritt ([Q50](../../QUELLEN.md#q50)):
- Im [Hotlist Service](../kontrolle/hotlist-service.md) sind Einträge für Schlüssel und Organisationen „only provided for the scheme manager“; er darf sich nicht selbst eintragen (`E_HL_SCHEME_MANAGER_MAY_NOT_HOTLIST_HIMSELF`).
- Beendet ein CCP die Applikation eines Mediums, unterrichtet er den Scheme Manager (`terminateUmApplication` am [ESH](../sicherheit/esh.md)).
- „In the role of the ESH“ kann der Scheme Manager Informationen zu nicht abgeholten Listen abfragen.

Eine eigene Rollennummer für den Scheme Manager nennt die Quelle nicht; die Nummer 4 trägt der ESH. Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Stellen wir uns vor, im Bärenland erfüllt der Bärenland eTicket Service (9030) die Aufgabe des Scheme Managers. Er ist der Hausherr des Systems: Er schreibt die Regeln auf und achtet darauf, dass alle sie einhalten.

Wenn die BVB und der Bären-Verkehrsbund am System teilnehmen wollen, brauchen sie seine Erlaubnis. Er vergibt ihnen ihre Kennungen und gibt ihnen das Recht, bestimmte Schlüssel zu nutzen. Er prüft, dass die Geräte zertifiziert sind, und sperrt notfalls einen Teilnehmer. So eine Sperre kann nur er veranlassen, die BVB darf Karten und Berechtigungen sperren, aber keine Organisationen.

Gibt Pia ihre BärenKarte zurück und die BVB beendet die Applikation darauf, erfährt auch der Hausherr davon. Und wenn ein Hersteller ein neues Terminal bauen will, ist er für Fragen der Ansprechpartner.

Einen Scheme Manager gibt es nur einmal. Die meisten seiner Dienste laufen in einem eigenen System, dem ASM, das in etiCORE ESH heißt.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 78 (Eintrag *Scheme Manager*), S. 23 (Applikationsherausgeber), S. 100 (Zertifizierung)
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: WSDL `hotlist` (Operationen für Schlüssel und Organisationen, `getUnclaimedListInformation`), WSDL `esh` (`terminateUmApplication`), `hotlist-event-enums_xsd` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Applikationsherausgeber](ah.md) – die Rolle als Teil des Scheme Managers
- [ASM](../sicherheit/asm.md) – das System, in dem die meisten Services laufen
- [ESH](../sicherheit/esh.md) – der Nachfolger des ASM
- [Hotlist Service](../kontrolle/hotlist-service.md) – was nur der Scheme Manager darf

<!-- GEN:siehe_auch -->
## Siehe auch

- [Applikationsherausgeber](ah.md) (AH)
- [ASM](../sicherheit/asm.md)
- [ESH](../sicherheit/esh.md)
- [Hotlist Service](../kontrolle/hotlist-service.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
