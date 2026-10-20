---
titel: Bescheinigungen zu Zahlungsmitteln (ASN.1)
englisch: payment attestations in ASN.1
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/bescheinigungen-zu-berechtigungen-asn-1.md, lexikon/datenformate/zahlungsmittel-asn-1.md, lexikon/datenformate/fahrtdaten-asn-1.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: "0x7F53"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: StoredValuePaymentMethodRechargedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ StoredValuePaymentMethodRechargedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F54"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: StoredValuePaymentMethodReimbursedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ StoredValuePaymentMethodReimbursedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F55"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: StoredValuePaymentMethodCreditedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ StoredValuePaymentMethodCreditedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F5F"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: StoredValuePaymentMethodDebitedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ StoredValuePaymentMethodDebitedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F56"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: AccountBasedPaymentMethodCreditedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ AccountBasedPaymentMethodCreditedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F60"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: AccountBasedPaymentMethodDebitedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ AccountBasedPaymentMethodDebitedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x68"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: PaymentAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ PaymentAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x67"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: MobilityAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ MobilityAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F5C"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: CheckinAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ CheckinAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F5D"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: CheckoutAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ CheckoutAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F5E"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: UserTariffParametersChangedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ UserTariffParametersChangedAttestation
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Bescheinigungen zu Zahlungsmitteln (ASN.1)
<!-- /GEN:breadcrumb -->

# Bescheinigungen zu Zahlungsmitteln (ASN.1)

Guthaben- und kontobasierte Zahlungsmittel haben eigene Bescheinigungen ([Q51](../../QUELLEN.md#q51), Modul `user-medium`). Sie führen zusätzlich den Betrag der Aktion (`actionAmount`, in kleinster Währungseinheit, negativ beim Abbuchen) und, bei Guthaben, den Kontostand danach:

- **Guthaben:** aufgeladen (`0x7F53`), erstattet (`0x7F54`), gutgeschrieben (`0x7F55`), belastet (`0x7F5F`);
- **kontobasiert:** gutgeschrieben (`0x7F56`), belastet (`0x7F60`).

Die Auswahl `PaymentAttestation` (`0x68`) fasst diese sechs zusammen. Die Auswahl `MobilityAttestation` (`0x67`) umfasst Entwertung, Check-in (`0x7F5C`), Check-out (`0x7F5D`) und die Änderung der Nutzertarifparameter (`0x7F5E`).

Die Parameterstrukturen legen die Vorzeichen fest: Aufladen muss einen nicht negativen, Abbuchen und Check-in einen nicht positiven Betrag haben. `StoredValueParameters` führt Kontostand (nicht negativ) und Höchstbetrag (positiv); das Medium führt keine Aktion aus, die den Höchstbetrag überschritte. `StoredValueAutoloadParameters` hat Schwelle und festen Betrag: Würde eine Bescheinigung den Stand unter die Schwelle senken, muss die ausführende Stelle zuerst aufladen.

Die Zahlungsparameter stehen im Artikel [Zahlungsmittel](../datenformate/zahlungsmittel-asn-1.md), die Fahrtdaten in [Fahrtdaten](../datenformate/fahrtdaten-asn-1.md). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Olli Tapsig hat Guthaben auf seinem Medium. Das ist ein Guthaben-Zahlungsmittel mit Kontostand und einem Höchstbetrag, den der Bären-Verkehrsbund festlegt.

Lädt er in der App 20 Euro auf, entsteht eine Aufladungs-Bescheinigung. Der Betrag ist positiv, und der neue Kontostand steht darauf. Würde die Aufladung den Höchstbetrag überschreiten, lehnt das Medium sie ab, und es gibt gar keine Bescheinigung.

Kauft er davon einen Einzelfahrschein, entsteht eine Belastungs-Bescheinigung mit negativem Betrag. Auf ihr steht auch, welcher Fahrschein die Abbuchung ausgelöst hat.

Der Kontostand kann nie unter null fallen. Damit Olli nicht an der Haltestelle ohne Geld dasteht, kann er eine Schwelle einstellen: Fällt der Stand darunter, lädt die Stelle, die gerade abbucht, zuerst einen festen Betrag nach. Das ist die automatische Aufladung.

Beim Fahren mit Check-in und Check-out entstehen die Mobilitäts-Bescheinigungen. Der Betrag beim Check-in darf nur null oder negativ sein.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `StoredValuePaymentMethod…Attestation` (vier), `AccountBasedPaymentMethod…Attestation` (zwei), `PaymentAttestation`, `MobilityAttestation`, `CheckinAttestation`, `CheckoutAttestation`, `UserTariffParametersChangedAttestation`, zugehörige `…Parameters`, `StoredValueParameters`, `StoredValueAutoloadParameters` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Bescheinigungen zu Berechtigungen (ASN.1)](bescheinigungen-zu-berechtigungen-asn-1.md) – die gemeinsamen Felder
- [Zahlungsmittel (ASN.1)](../datenformate/zahlungsmittel-asn-1.md) – die Zahlungsparameter
- [Fahrtdaten (ASN.1)](../datenformate/fahrtdaten-asn-1.md) – die Parameter für Check-in und Check-out
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Bescheinigungen zu Berechtigungen (ASN.1)](bescheinigungen-zu-berechtigungen-asn-1.md)
- [Zahlungsmittel (ASN.1)](../datenformate/zahlungsmittel-asn-1.md)
- [Fahrtdaten (ASN.1)](../datenformate/fahrtdaten-asn-1.md)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
