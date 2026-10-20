---
titel: Zahlungsmittel (ASN.1)
englisch: payment means in ASN.1
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/fahrtdaten-asn-1.md, lexikon/datenformate/organisation-und-produkt-asn-1.md, lexikon/datenformate/asn-1-typen-in-eticore.md, lexikon/transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 0
    codeliste: PaymentMeansEnum
    bedeutung: notSpecified — Not specified
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: PaymentMeansEnum
    bedeutung: cash
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 3
    codeliste: PaymentMeansEnum
    bedeutung: creditcard — Credit card
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 5
    codeliste: PaymentMeansEnum
    bedeutung: accountBasedAuthorisation — Account-based authorisation
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 6
    codeliste: PaymentMeansEnum
    bedeutung: sepaDirectDebit — SEPA Direct Debit offline
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 7
    codeliste: PaymentMeansEnum
    bedeutung: invoice
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 8
    codeliste: PaymentMeansEnum
    bedeutung: storedValues — Stored Values
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 9
    codeliste: PaymentMeansEnum
    bedeutung: loyaltyRedemption — Loyalty-Redemption
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 10
    codeliste: PaymentMeansEnum
    bedeutung: token — Token (e.g. ID-Based-Ticketing)
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 11
    codeliste: PaymentMeansEnum
    bedeutung: membershipBenefit — Membership-Benefit
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 12
    codeliste: PaymentMeansEnum
    bedeutung: prepaidAutoload — Prepaid Autoload
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 14
    codeliste: PaymentMeansEnum
    bedeutung: voucher
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 17
    codeliste: PaymentMeansEnum
    bedeutung: directDebitOnline — Direct-Debit Online
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 24
    codeliste: PaymentMeansEnum
    bedeutung: electronicPurse — Electronic Purse
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 25
    codeliste: PaymentMeansEnum
    bedeutung: mastercard
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 26
    codeliste: PaymentMeansEnum
    bedeutung: visacard — Visa
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 27
    codeliste: PaymentMeansEnum
    bedeutung: handyTicketAccount — HandyTicket Account
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 28
    codeliste: PaymentMeansEnum
    bedeutung: viaMobilPhoneContractInvoice — Via Mobil Phone Contract Invoice
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 29
    codeliste: PaymentMeansEnum
    bedeutung: cashless
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 30
    codeliste: PaymentMeansEnum
    bedeutung: mixedPayment — Mixed Payment
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 100
    codeliste: PaymentMeansEnum
    bedeutung: amazonPay — Amazon Pay
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 101
    codeliste: PaymentMeansEnum
    bedeutung: amex
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 102
    codeliste: PaymentMeansEnum
    bedeutung: googlePay — Google Pay
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 103
    codeliste: PaymentMeansEnum
    bedeutung: applePay — Apple Pay
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 104
    codeliste: PaymentMeansEnum
    bedeutung: anyAppBasedPayment — Any App Based Payment
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 105
    codeliste: PaymentMeansEnum
    bedeutung: girocardContactless — Girocard Contactless
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 106
    codeliste: PaymentMeansEnum
    bedeutung: girogo
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 107
    codeliste: PaymentMeansEnum
    bedeutung: giropay
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 108
    codeliste: PaymentMeansEnum
    bedeutung: maestro
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 109
    codeliste: PaymentMeansEnum
    bedeutung: paypassContactlessMaestroMastercard — Paypass, contactless Maestro/Mastercard
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 110
    codeliste: PaymentMeansEnum
    bedeutung: paydirect
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 111
    codeliste: PaymentMeansEnum
    bedeutung: payPal
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 112
    codeliste: PaymentMeansEnum
    bedeutung: printTicketAccount — PrintTicket Account
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 113
    codeliste: PaymentMeansEnum
    bedeutung: sofortDirectDebitOnline — SOFORT (Direct Debit Online)
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 114
    codeliste: PaymentMeansEnum
    bedeutung: vPay — V-Pay
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 115
    codeliste: PaymentMeansEnum
    bedeutung: payWaveContactlessVisa — payWave (contactless NFC VISA)
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
  - wert: 116
    codeliste: PaymentMeansEnum
    bedeutung: furtherWebBasedPaymentMethods — Further web-based payment methods
    quelle: Q51
    fundstelle: Modul payment, Typ PaymentMeansEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Zahlungsmittel (ASN.1)
<!-- /GEN:breadcrumb -->

# Zahlungsmittel (ASN.1)

Das Modul `payment` ([Q51](../../QUELLEN.md#q51)) beschreibt Zahlungsmittel und die Parameter, mit denen sie belastet oder aufgeladen werden.

- `PaymentMeansCode` (`0x9A`) und `PaymentMeansEnum` mit **37 Werten** klassifizieren das Zahlungsmittel nach EN 1545-1:2015, von „nicht angegeben“ und Bargeld über Kreditkarte und SEPA-Lastschrift bis zur kontobasierten Autorisierung. Alle Werte stehen im Frontmatter.
- `SvpmChargingPaymentParameters` gilt für das Aufladen oder Erstatten eines Guthaben-Zahlungsmittels. Bei einer manuellen Aufladung steht dort das tatsächlich genutzte Zahlungsmittel, bei der automatischen Aufladung (Autoload) der Wert 12, bei einer Erstattung das Mittel, auf das erstattet wird.
- `CreditDebitPaymentParameters` gilt für Gutschrift und Belastung kontobasierter und Guthaben-Zahlungsmittel. Es ist eine Auswahl: entweder `EtiCoreTicketInformation` mit Berechtigungs-ID und Produkt-ID des Fahrscheins, der die Abbuchung (Verkauf) oder Gutschrift (Erstattung) auslöst, oder ein Bytewert für einen Fahrschein eines fremden Systems.

Diese drei Strukturen tragen alle den Tag `0x7F39`; erst die Verwendung im umgebenden Typ unterscheidet sie. Das gilt auch für `CicoPaymentParameters` ([Fahrtdaten](fahrtdaten-asn-1.md)). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Olli Tapsig lädt sein Guthaben in der BVB-App auf. Das Hintergrundsystem muss festhalten, womit er bezahlt hat. Dafür gibt es die Liste der Zahlungsmittel, eine Art Wörterbuch aus 37 Einträgen: Bargeld, Kreditkarte, Lastschrift und weitere. Eingetragen wird die Nummer des passenden Eintrags.

Bei der automatischen Aufladung, wenn das Guthaben unter einen Schwellenwert fällt und sich von selbst füllt, steht immer die 12. Es gibt dann kein Zahlungsmittel, das gerade benutzt wurde, sondern eine vorher getroffene Vereinbarung.

Kauft Olli später mit dem Guthaben einen Einzelfahrschein, wird das Guthaben belastet. Die Belastung trägt zwei Angaben: die Kennung der Berechtigung und die Kennung des Produkts. So lässt sich später sagen, wofür das Geld abgebucht wurde. Stammt der Fahrschein von einem fremden System, steht stattdessen nur ein Byte-Wert.

Alle drei Strukturen haben dieselbe Nummer, 0x7F39. Das ist unproblematisch, solange man weiß, in welcher Umgebung man liest. Es ist wie eine Postfachnummer: Dieselbe Nummer in zwei Postämtern meint zwei Fächer.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `payment`: `PaymentMeansCode`, `PaymentMeansEnum`, `SvpmChargingPaymentParameters`, `CreditDebitPaymentParameters`, `EtiCoreTicketInformation` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Fahrtdaten (ASN.1)](fahrtdaten-asn-1.md) – die Parameter für Check-in und Check-out
- [Organisation und Produkt (ASN.1)](organisation-und-produkt-asn-1.md) – Berechtigungs-ID und Produkt-ID
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md) – die zugehörigen Nachweise
- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Fahrtdaten (ASN.1)](fahrtdaten-asn-1.md)
- [Organisation und Produkt (ASN.1)](organisation-und-produkt-asn-1.md)
- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md)
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](../transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
