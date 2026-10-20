---
titel: Kundendaten und Parameter (ASN.1)
englisch: customer data and parameters in ASN.1
parent: lexikon/datenformate.md
siehe_auch: [lexikon/berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md, lexikon/berechtigungen/produktspezifischer-teil.md, lexikon/grundlagen/datenschutz.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 0
    codeliste: DiscountTypeEnum
    bedeutung: no-reduction — No reduction
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: DiscountTypeEnum
    bedeutung: percentage-discount-level-1
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: DiscountTypeEnum
    bedeutung: percentage-discount-level-2
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 3
    codeliste: DiscountTypeEnum
    bedeutung: percentage-discount-level-3
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 4
    codeliste: DiscountTypeEnum
    bedeutung: percentage-discount-level-4
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 5
    codeliste: DiscountTypeEnum
    bedeutung: percentage-discount-level-5
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 6
    codeliste: DiscountTypeEnum
    bedeutung: reduction-on-basis-of-a-kilometre-calculation
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 7
    codeliste: DiscountTypeEnum
    bedeutung: reduction-dependant-on-the-used-mode-of-transport
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 8
    codeliste: DiscountTypeEnum
    bedeutung: reduction-dependant-on-the-vehicle-class
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 9
    codeliste: DiscountTypeEnum
    bedeutung: for-short-distance-bus-and-train-travel-up-to-50-km — for-short-distance-bus-and-train-travel-up-to-50 km
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 10
    codeliste: DiscountTypeEnum
    bedeutung: for-long-distance-train-travel
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 11
    codeliste: DiscountTypeEnum
    bedeutung: for-long-distance-bus-travel
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 46
    codeliste: DiscountTypeEnum
    bedeutung: "purchaseUsingEPaymentMethodDiscountedBy25Percent — Purchase using ePaymentMethod discounted by 25%"
    quelle: Q51
    fundstelle: Modul user-medium, Typ DiscountTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 0
    codeliste: GenderEnum
    bedeutung: notKnown — not known
    quelle: Q51
    fundstelle: Modul user-medium, Typ GenderEnum
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: GenderEnum
    bedeutung: male
    quelle: Q51
    fundstelle: Modul user-medium, Typ GenderEnum
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: GenderEnum
    bedeutung: female
    quelle: Q51
    fundstelle: Modul user-medium, Typ GenderEnum
    status: belegt
    verbundspezifisch: false
  - wert: 3
    codeliste: GenderEnum
    bedeutung: unspecified
    quelle: Q51
    fundstelle: Modul user-medium, Typ GenderEnum
    status: belegt
    verbundspezifisch: false
  - wert: 0
    codeliste: ProductParametersContentTypeEnum
    bedeutung: unspecified — Unspecified content.
    quelle: Q51
    fundstelle: Modul user-medium, Typ ProductParametersContentTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: ProductParametersContentTypeEnum
    bedeutung: tlvEfs — Indicates that the product parameter content consists of the tag 0x85, which in turn contains data objects corresponding to 1.X TLV EFS.
    quelle: Q51
    fundstelle: Modul user-medium, Typ ProductParametersContentTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: ProductParametersContentTypeEnum
    bedeutung: referenzEfs — Indicates that the product parameter content consists of the tag 0x85, which in turn contains data objects corresponding to 1.X Referenz EFS.
    quelle: Q51
    fundstelle: Modul user-medium, Typ ProductParametersContentTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 3
    codeliste: ProductParametersContentTypeEnum
    bedeutung: referenzPobPeb — Indicates that the product parameter content consists of the tag 0x85, which in turn contains data objects corresponding to 1.X Referenz POB/PEB.
    quelle: Q51
    fundstelle: Modul user-medium, Typ ProductParametersContentTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 4
    codeliste: ProductParametersContentTypeEnum
    bedeutung: referenzPlatzreservierung — Indicates that the product parameter content consists of the tag 0x85, which in turn contains data objects corresponding to 1.X Referenz Platzreservierung.
    quelle: Q51
    fundstelle: Modul user-medium, Typ ProductParametersContentTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 5
    codeliste: ProductParametersContentTypeEnum
    bedeutung: referenzPlatzgruppenreservierung — Indicates that the product parameter content consists of the tag 0x85, which in turn contains data objects corresponding to 1.X Referenz Platzgruppenreservierung.
    quelle: Q51
    fundstelle: Modul user-medium, Typ ProductParametersContentTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 6
    codeliste: ProductParametersContentTypeEnum
    bedeutung: referenzEfsStb — Indicates that the product parameter content consists of the tag 0x85, which in turn contains data objects corresponding to 1.X Referenz EFS in the STB variant.
    quelle: Q51
    fundstelle: Modul user-medium, Typ ProductParametersContentTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 7
    codeliste: ProductParametersContentTypeEnum
    bedeutung: etiCoreEt — Indicates that the product parameter content is structured according to etiCORE ET guidelines.
    quelle: Q51
    fundstelle: Modul user-medium, Typ ProductParametersContentTypeEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Kundendaten und Parameter (ASN.1)
<!-- /GEN:breadcrumb -->

# Kundendaten und Parameter (ASN.1)

Kundendaten, Ermäßigungen und Parameter im Modul `user-medium` ([Q51](../../QUELLEN.md#q51)):

- `Customer` (`0x7F4F`): Vorname, Nachname und Geburtsdatum sind **Pflicht**, das Geschlecht ist optional. Anders als `Passenger` im Modul `et` ([Fahrgast, Linie und Identifikationsmedium](../berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md)). Es sind personenbezogene Daten ([Datenschutz](../grundlagen/datenschutz.md)).
- `Discount` (`0x7F7B`): Product Owner, Ermäßigungsart (`DiscountTypeEnum`, 13 Werte, nach EN 1545-2:2015), betroffene Organisationen und Gültigkeit. `Favourite` (`0x7F67`): ein Produkt mit Parametern und Infotext.
- `UserAuthenticationData` (`0x7F36`): Mindest- und Höchstlänge des Kennworts, erlaubte und verbleibende Fehlversuche und der Zustand „PWD Not Initialized“, „PWD Initialized“ oder „PWD Blocked“. `PasswordParameters` dient dem Einrichten.
- `ProductParameters` (`0x65`): Inhaltsart (`ProductParametersContentTypeEnum`, 8 Werte) und der Inhalt. Sechs Werte (1 bis 6) bedeuten, dass der Inhalt Datenobjekten der **KA 1.x** entspricht: TLV-EFS, Referenz-EFS, POB/PEB, Platz- und Platzgruppenreservierung, Referenz-EFS (STB). Der Wert 7 steht für die etiCORE-ET-Vorgaben.
- `ActionTariffParameters` (`0x7F3A`) kann „für die Migration“ den produktspezifischen Teil der Transaktion (Tag `0x8A`) tragen ([Produktspezifischer Teil](../berechtigungen/produktspezifischer-teil.md)).

Die Werte stehen im Frontmatter. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Pia hat auf ihrer BärenKarte ein ABO Azubi. Für produktspezifische Angaben gibt es ein Fach für Produktparameter. Sein Etikett nennt die Art des Inhalts. Und hier zeigt sich, wie etiCORE auf die Vergangenheit baut: Mehrere Etiketten heißen „wie in der KA 1.x“, zum Beispiel „TLV-EFS“. Wer vom alten System kommt, kann seine Produktdaten im Aufbau der KA 1.x in das neue Fach legen.

Dazu kommt das Kundenkästchen mit Name und Geburtsdatum. Bei Pias personalisiertem Abo ist es gefüllt, und es ist, anders als im Fahrscheinformular, Pflicht, sobald es vorhanden ist.

Familie Tatze würde eine Ermäßigung eintragen lassen, falls es sie gäbe: von welchem Verbund, welche Art (etwa „Prozentrabatt Stufe 2“), für welche Betreiber, von wann bis wann.

Ein Kennwort kann die Karte schützen. Wie lang es sein darf, wie oft man sich vertippen darf und ob es schon eingerichtet oder bereits gesperrt ist, steht im Kennwortkästchen.

Und Olli Tapsig kann Favoriten ablegen: Der Einzelfahrschein Bärstadt, den er am häufigsten kauft, läge dann als Produkt mit Parametern und einem Hinweistext bereit.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `Customer`, `GenderEnum`, `Discount`, `Discounts`, `DiscountTypeEnum`, `Favourite`, `Favourites`, `UserAuthenticationData`, `PasswordParameters`, `ProductParameters`, `ProductParametersContentTypeEnum`, `ActionTariffParameters` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Fahrgast, Linie und Identifikationsmedium (ASN.1)](../berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md) – `Passenger` im Vergleich
- [Produktspezifischer Teil](../berechtigungen/produktspezifischer-teil.md) – der Teil in der KA 1.x
- [Datenschutz](../grundlagen/datenschutz.md) – Grundsätze zu personenbezogenen Daten
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Fahrgast, Linie und Identifikationsmedium (ASN.1)](../berechtigungen/fahrgast-linie-und-identifikationsmedium-asn-1.md)
- [Produktspezifischer Teil](../berechtigungen/produktspezifischer-teil.md)
- [Datenschutz](../grundlagen/datenschutz.md)
- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
