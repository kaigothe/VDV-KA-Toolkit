---
titel: Interoperabilitätsnetzwerk
abkuerzung: ION
englisch: interoperability network
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/rollen/zentrale-vermittlungsstelle.md, lexikon/transaktionen/fehlercodes-im-ion.md, lexikon/grundlagen/interoperabilitaet.md, lexikon/grundlagen/eticore.md]
quellen: [Q02, Q43, Q49, Q50]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Interoperabilitätsnetzwerk
<!-- /GEN:breadcrumb -->

# Interoperabilitätsnetzwerk

Das **Interoperabilitätsnetzwerk** (ION) „erlaubt einen interoperablen und sicheren Nachrichtenaustausch zwischen Teilnehmersystemen“ bei verteilten oder übergreifenden Prozessen ([Q02](../../QUELLEN.md#q02), S. 49). Es legt fest:
- das **Nachrichtenformat** und die **Adressierung**,
- einheitliche **Sicherheitsmechanismen** für Transport und Nachrichten,
- einheitliche **Sende- und Empfangsprozesse** samt Fehlerszenarien.

Teil des ION ist die [Zentrale Vermittlungsstelle](../rollen/zentrale-vermittlungsstelle.md), die die logische in die physische Adressierung übersetzt. Dadurch brauchen die Hintergrundsysteme von Applikationsherausgeber, Hotlist Service, Product Owner, Customer Contract Partner und Service Operator nur Organisations-ID, Rolle und Dienstname des Partners ([Q02](../../QUELLEN.md#q02), S. 49). Die Anbindung folgt der ION-Spezifikation, die im Spezifikationsmodell ein eigenes Paket bildet ([Q49](../../QUELLEN.md#q49); [Q43](../../QUELLEN.md#q43), Kap. 2.1, PDF-S. 23 ff.).

Die etiCORE-Schnittstellen sind SOAP-Dienste im Stil `document/literal`; jede Anfrage trägt einen `ionRoutingHeader` ([Q50](../../QUELLEN.md#q50), WSDL `po-oa-management`). Der Absender muss zum TLS-Zertifikat passen (`E_IONC_HEADER_TO_TLS_CERTIFICATE_MISMATCH`), und ION-Nachrichten-IDs verhindern Doppelzustellung (`E_ION_DUPLICATE_ION_MESSAGE_ID`). Alle Fehler stehen in [Fehlercodes im ION](fehlercodes-im-ion.md). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Stellen wir uns eine Stadt vor, in der alle Geschäfte miteinander Geschäfte machen, aber niemand die Straßen kennt. Das ION ist das Postsystem dieser Stadt.

Es legt drei Dinge fest. Erstens, wie ein Brief aussieht: Welche Angaben vorn auf den Umschlag gehören. Zweitens, wie er unterwegs geschützt wird: Der Briefträger kann ihn nicht lesen, und der Empfänger erkennt, von wem er kommt. Drittens, wie sich Absender und Empfänger verhalten: Wer bestätigt wann, was geschieht bei einer Doppelzustellung, und was bei einem Fehler.

Die Bärstädter Verkehrsbetriebe, der Bären-Verkehrsbund, der Kontrollservice Bärenland und der Bärenland eTicket Service nutzen dasselbe Postsystem. Als die BVB Pias Auftrag aufgibt, schreibt sie auf den Umschlag: Organisation 9020, Rolle Produktverantwortlicher, Dienst Aktionsmanagement. Die Vermittlungsstelle erledigt den Rest.

Das System lohnt sich, weil es allen die gleiche Sprache gibt. Ein neuer Teilnehmer, etwa der Luchs-Verkehrsverbund, muss nicht mit jedem Partner einzeln verhandeln. Er hält sich an die ION-Spezifikation und kann mit allen sprechen.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 48 f. (Eintrag *Interoperabilitätsnetzwerk / Interoperability Network*)
- [Q43](../../QUELLEN.md#q43) – etiCORE Release Letter 3.0.0-rc.6, Kap. 2.1, PDF-S. 23 ff. (Aufbau der Spezifikation mit SPEC-ION)
- [Q49](../../QUELLEN.md#q49) – etiCORE Specification, Glossar, Eintrag *Central Routing Engine*; oberste Paketebene *ION Specification*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: WSDL `po-oa-management` (SOAP-Stil, `ionRoutingHeader`), `ion-communication-event-enums_xsd` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Zentrale Vermittlungsstelle](../rollen/zentrale-vermittlungsstelle.md) – der Vermittler im ION
- [Fehlercodes im ION](fehlercodes-im-ion.md) – die Fehlerszenarien
- [Interoperabilität](../grundlagen/interoperabilitaet.md) – der übergeordnete Begriff
- [etiCORE](../grundlagen/eticore.md) – die Version, in der das ION neu beschrieben ist

<!-- GEN:siehe_auch -->
## Siehe auch

- [Zentrale Vermittlungsstelle](../rollen/zentrale-vermittlungsstelle.md) (ZVM)
- [Fehlercodes im ION](fehlercodes-im-ion.md)
- [Interoperabilität](../grundlagen/interoperabilitaet.md)
- [etiCORE](../grundlagen/eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
