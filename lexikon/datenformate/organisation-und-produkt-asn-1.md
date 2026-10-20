---
titel: Organisation und Produkt (ASN.1)
englisch: organisation and product in ASN.1
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/asn-1-typen-in-eticore.md, lexikon/rollen/organisations-id.md, lexikon/berechtigungen/produktnummer.md, lexikon/berechtigungen/statische-berechtigung-in-eticore.md]
quellen: [Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 1
    codeliste: ProductTypeEnum
    bedeutung: electronicTicket — Electronic ticket
    quelle: Q51
    fundstelle: Modul common, Typ ProductTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: ProductTypeEnum
    bedeutung: interoperableAccountBasedPaymentMethod — Interoperable account-based ePaymentMethod
    quelle: Q51
    fundstelle: Modul common, Typ ProductTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 3
    codeliste: ProductTypeEnum
    bedeutung: nonInteroperableAccountBasedPaymentMethod — Non-interoperable account-based ePaymentMethod for local use
    quelle: Q51
    fundstelle: Modul common, Typ ProductTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 4
    codeliste: ProductTypeEnum
    bedeutung: interoperableStoredValuePaymentMethod — Interoperable stored value ePaymentMethod
    quelle: Q51
    fundstelle: Modul common, Typ ProductTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 5
    codeliste: ProductTypeEnum
    bedeutung: nonInteroperableStoredValuePaymentMethod — Non-interoperable stored value ePaymentMethod for local use
    quelle: Q51
    fundstelle: Modul common, Typ ProductTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 17
    codeliste: ProductTypeEnum
    bedeutung: staticElectronicTicket — Static electronic ticket
    quelle: Q51
    fundstelle: Modul common, Typ ProductTypeEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Organisation und Produkt (ASN.1)
<!-- /GEN:breadcrumb -->

# Organisation und Produkt (ASN.1)

Die Kennungen im Modul `common` ([Q51](../../QUELLEN.md#q51)) bauen aufeinander auf.

- `OrganisationId` (Tag `0x4D`, `INTEGER`) ist der „unique identifier of an organisation“. `OwnerId` ist dieselbe Zahl in der Rolle der Organisation, die derzeit für SAM oder Medium verantwortlich ist.
- `ProductId` (`0x6C`) besteht aus `orgId` des Product Owners, `productType` und `productNumber`. Erst alle Teile zusammen machen das Produkt im ganzen Fahrgeldmanagement eindeutig; die Produktnummer ist nur zusammen mit der Organisation eindeutig.
- `ProductTypeEnum` kennt sechs Werte: Fahrschein (1), interoperables und nicht interoperables kontobasiertes Zahlungsmittel (2, 3), ebensolche Guthaben-Zahlungsmittel (4, 5) und statischer Fahrschein (17). Bei der Ausführung von Aktionen kann der Produkttyp auch 0 für „Applikation“ sein.
- `EntitlementId` (`0x6E`) setzt sich zusammen aus `ccpOrgId`, der `samId` des ausgebenden SAM und dem `entitlementIssuanceCounter`. Dieser Zähler (`0x4B`) steigt um eins, sooft ein SAM die Ausgabe einer (statischen) Berechtigung autorisiert.

Eine Berechtigung ist danach über SAM und Zählerstand eindeutig, nicht über eine vom CCP vergebene Nummer (abgeleitet). Wie die Kennung der KA 1.x damit zusammenhängt, zeigt die Quelle nicht. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Der Bären-Verkehrsbund hat die Organisations-ID 9020. Sein ABO Azubi trägt die Produktnummer 2001. Die Produkt-ID besteht also aus drei Angaben: der Organisation 9020, der Produktnummer 2001 und dem Typ „Fahrschein“. Die Luchs-Monatskarte des Nachbarverbunds hat die Nummer 2101 bei der Organisation 9070. Hätte sie zufällig die Nummer 2001, wäre sie trotzdem ein anderes Produkt, weil die Organisation eine andere ist.

Pias Berechtigung bekommt ihre Kennung nach einem anderen Muster. Sie setzt sich zusammen aus der ausgebenden Organisation, hier der BVB (9010), dem SAM, das die Ausgabe autorisiert hat, und einer laufenden Nummer, die dieses SAM bei jeder Ausgabe um eins erhöht. Das ist wie ein Notar, der jede Beglaubigung fortlaufend nummeriert: Wer die Nummer und den Notar kennt, kann die Urkunde eindeutig benennen.

Olli Tapsigs Einzelfahrschein als Barcode ist ein statischer Fahrschein, Typ 17. Das Produkt 2002 ist damit zugleich Fahrschein und statisch. Der Typ sagt, in welche Schublade das Produkt gehört, die Nummer, welches es innerhalb dieser Schublade ist.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `common`: `OrganisationId`, `OwnerId`, `ProductId`, `ProductNumber`, `ProductTypeEnum`, `EntitlementId`, `EntitlementIssuanceCounter` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md) – Überblick
- [Organisations-ID](../rollen/organisations-id.md) – die Kennung in der KA 1.x
- [Produktnummer](../berechtigungen/produktnummer.md) – die Produktnummer in der KA 1.x
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md)

<!-- GEN:siehe_auch -->
## Siehe auch

- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md)
- [Organisations-ID](../rollen/organisations-id.md) (Org-ID)
- [Produktnummer](../berechtigungen/produktnummer.md)
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
