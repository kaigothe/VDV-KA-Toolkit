---
titel: Entwertung
englisch: validation
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/berechtigungen/efs.md, lexikon/transaktionen/logtransaktionstyp.md, lexikon/transaktionen/bescheinigungen-zu-berechtigungen-asn-1.md, lexikon/kontrolle/sichtkontrolle.md]
quellen: [Q02, Q05, Q50, Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Entwertung
<!-- /GEN:breadcrumb -->

# Entwertung

**Entwertung** im Sinne des ÖPV „bedeutet das Verwenden eines Tickets, welches für eine einmalige Nutzung zu einem beliebigem, dem Tarifprodukt des Tickets entsprechenden Zeitpunkt vorgesehen war“ ([Q02](../../QUELLEN.md#q02), S. 39 f.). Das Verwenden bescheinigt ein Stempel auf dem Papierticket oder ein elektronischer Nachweis im [Elektronischen Fahrschein](../berechtigungen/efs.md). Dadurch kann das Ticket nicht noch einmal verwendet werden; andererseits wird es erst durch diesen Vorgang für die aktuelle Fahrt gültig ([Q02](../../QUELLEN.md#q02), S. 39 f.).

Im RMV-Pflichtenheft ist die Entwertung der Transaktionstyp 2, „als Option für Fahrkarten, die eine Entwertung vor bzw. während der Fahrt benötigen“ ([Q05](../../QUELLEN.md#q05), Kap. 4.4.4) · *verbundspezifisch*; siehe [logTransaktionsTyp](../transaktionen/logtransaktionstyp.md).

In etiCORE heißt der Nachweis `EntitlementValidatedAttestation` (Tag `0x7F5B`); sie kann Parameter für Check-in, Check-out oder Entwertung tragen ([Q51](../../QUELLEN.md#q51), Modul `user-medium`; [Bescheinigungen zu Berechtigungen](../transaktionen/bescheinigungen-zu-berechtigungen-asn-1.md)). Nicht jedes Produkt lässt sich entwerten: Ein Guthaben-Zahlungsmittel nicht (`E_EUI_WRONG_PRODUCT_TYPE_FOR_ACTION`), und eine Aktion außerhalb der Gültigkeit warnt `W_CO_ACTION_NOT_IN_VALIDITY_PERIOD_OF_OBJECT` ([Q50](../../QUELLEN.md#q50)). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Man kennt die Entwertung vom Papierticket: Man steckt es in den Stempelautomaten, und es ist benutzt.

Olli Tapsig hat sich einen Einzelfahrschein Bärstadt auf sein Handy geladen. Solange er ihn nicht benutzt hat, ist er nur ein Anspruch: Er kann ihn irgendwann einlösen. Beim Einsteigen in die Linie 4 entwertet er. Dann gilt der Fahrschein für diese Fahrt, und er verfällt zugleich, denn ein zweites Mal geht es nicht. Beides passiert in einem Schritt.

Auf dem Handy ist der „Stempel“ ein elektronischer Nachweis im Fahrschein selbst.

Nicht alles lässt sich entwerten. Ollis Guthaben ist kein Fahrschein, der einmal benutzt wird, sondern ein Geldbeutel. Wollte ein Gerät das Guthaben „entwerten“, bekäme es einen Fehler: Das Produkt passt nicht zur Aktion.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 39 f. (*Entwertung / Validation*) (wörtliche Definition)
- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 4.4.4 (Transaktionstyp 2 = Entwertung) · *verbundspezifisch: eTicket RheinMain*
- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `EntitlementValidatedAttestation`, `EntitlementValidationParameters` · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: `eui-event-enums_xsd`, `common-event-enums_xsd` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Elektronischer Fahrschein](../berechtigungen/efs.md) – was entwertet wird
- [logTransaktionsTyp](../transaktionen/logtransaktionstyp.md) – der Transaktionstyp 2
- [Bescheinigungen zu Berechtigungen (ASN.1)](../transaktionen/bescheinigungen-zu-berechtigungen-asn-1.md) – der Nachweis in etiCORE
- [Sichtkontrolle](sichtkontrolle.md) – wie man ihn prüft

<!-- GEN:siehe_auch -->
## Siehe auch

- [Elektronischer Fahrschein](../berechtigungen/efs.md) (EFS)
- [logTransaktionsTyp](../transaktionen/logtransaktionstyp.md)
- [Bescheinigungen zu Berechtigungen (ASN.1)](../transaktionen/bescheinigungen-zu-berechtigungen-asn-1.md)
- [Sichtkontrolle](sichtkontrolle.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
