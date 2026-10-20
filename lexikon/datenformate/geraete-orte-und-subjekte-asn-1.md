---
titel: Geräte, Orte und Subjekte (ASN.1)
englisch: devices, locations and subjects in ASN.1
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/asn-1-typen-in-eticore.md, lexikon/rollen/akzeptanzterminal.md, lexikon/sicherheit/cv-zertifikat.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 0
    codeliste: DeviceTypeEnum
    bedeutung: otherwise-specified — Otherwise specified
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: DeviceTypeEnum
    bedeutung: registrationTerminal — Registration terminal (used for cico/bibo etc.)
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: DeviceTypeEnum
    bedeutung: ticketVendingMachine — Ticket vending machine
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 3
    codeliste: DeviceTypeEnum
    bedeutung: inspectionTerminal — Inspection terminal (mobile, operated by staff)
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 4
    codeliste: DeviceTypeEnum
    bedeutung: customerMediaIssuingTerminal — Customer media issuing terminal
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 5
    codeliste: DeviceTypeEnum
    bedeutung: customerMediaReturnTerminal — Customer media return terminal
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 6
    codeliste: DeviceTypeEnum
    bedeutung: validator — Validator / ticket stamper / puncher
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 7
    codeliste: DeviceTypeEnum
    bedeutung: multiFunctionTerminal — Multi function terminal (operated by customer)
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 8
    codeliste: DeviceTypeEnum
    bedeutung: informationTerminal — Information terminal
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 9
    codeliste: DeviceTypeEnum
    bedeutung: loadingTerminal — Loading terminal
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 13
    codeliste: DeviceTypeEnum
    bedeutung: massPersonaliser — Terminal at mass personaliser
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 14
    codeliste: DeviceTypeEnum
    bedeutung: serviceTerminal — Terminal in sales or service center (operated by staff)
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 15
    codeliste: DeviceTypeEnum
    bedeutung: driverTerminal — Driver terminal (sales and inspection)
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 16
    codeliste: DeviceTypeEnum
    bedeutung: mobileTicketServer — Mobile ticket server
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 17
    codeliste: DeviceTypeEnum
    bedeutung: onlineTicketServer — Online ticket server
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 18
    codeliste: DeviceTypeEnum
    bedeutung: mobileSalesTerminal — Mobile sales terminal (operated by customer)
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 19
    codeliste: DeviceTypeEnum
    bedeutung: mobileSalesAndInspectionTerminal — Mobile sales and inspection terminal (operated by staff)
    quelle: Q51
    fundstelle: Modul common, Typ DeviceTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: LocationSchemaTypeEnum
    bedeutung: "eticore — Indicates that locationIdString consists of the location type, the location number and the responsible organisation ID, in this order, coded as decimals without leading zeroes, separated by colons (':'). Example: locatio"
    quelle: Q51
    fundstelle: Modul common, Typ LocationSchemaTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: LocationSchemaTypeEnum
    bedeutung: ifopt — Indicates that locationIdString comprises a IFOPT compatible location identifier, e.g., a DHID.
    quelle: Q51
    fundstelle: Modul common, Typ LocationSchemaTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 0
    codeliste: LocationTypeEnum
    bedeutung: busStopStation — Bus stop station
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 1
    codeliste: LocationTypeEnum
    bedeutung: metroStation — Metro station
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 2
    codeliste: LocationTypeEnum
    bedeutung: railwayStation — Railway station
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 3
    codeliste: LocationTypeEnum
    bedeutung: tramStopStation — Tram stop station
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 11
    codeliste: LocationTypeEnum
    bedeutung: retailAgent — Retail agent
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 16
    codeliste: LocationTypeEnum
    bedeutung: areaId — Area ID
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 17
    codeliste: LocationTypeEnum
    bedeutung: corridor
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 200
    codeliste: LocationTypeEnum
    bedeutung: generalStop — General stop, independent of mode of transport
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 201
    codeliste: LocationTypeEnum
    bedeutung: massPersonaliser — Mass personaliser
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 202
    codeliste: LocationTypeEnum
    bedeutung: areaListId — Spatial area
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 203
    codeliste: LocationTypeEnum
    bedeutung: inVehicle — In vehicle / train
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 204
    codeliste: LocationTypeEnum
    bedeutung: touchPoint — Touch point
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 205
    codeliste: LocationTypeEnum
    bedeutung: inVehicleOfLine — In vehicle of line
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 206
    codeliste: LocationTypeEnum
    bedeutung: inVehicleOfNumber — In vehicle of number
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 207
    codeliste: LocationTypeEnum
    bedeutung: partialZone — Partial zone
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 208
    codeliste: LocationTypeEnum
    bedeutung: neutralZone — Neutral zone
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 209
    codeliste: LocationTypeEnum
    bedeutung: fareZone — Fare zone
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 210
    codeliste: LocationTypeEnum
    bedeutung: largeFareZone — Large fare zone
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 211
    codeliste: LocationTypeEnum
    bedeutung: tariffPoint — Tariff point
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 212
    codeliste: LocationTypeEnum
    bedeutung: backOffice — Back office
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 213
    codeliste: LocationTypeEnum
    bedeutung: inVehicleAtStop — In vehicle at stop
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 214
    codeliste: LocationTypeEnum
    bedeutung: eventLocation — Event location
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 215
    codeliste: LocationTypeEnum
    bedeutung: ticketServer — Ticket server
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 216
    codeliste: LocationTypeEnum
    bedeutung: postalCode — Postal code
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 217
    codeliste: LocationTypeEnum
    bedeutung: globalIdInDE — Global ID in DE = DHID
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 218
    codeliste: LocationTypeEnum
    bedeutung: globalIdInNL — Global ID in NL
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 219
    codeliste: LocationTypeEnum
    bedeutung: globalIdInBE — Global ID in BE
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 220
    codeliste: LocationTypeEnum
    bedeutung: globalIdInLU — Global ID in LU
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 221
    codeliste: LocationTypeEnum
    bedeutung: globalIdInFR — Global ID in FR
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 222
    codeliste: LocationTypeEnum
    bedeutung: globalIdInCH — Global ID in CH
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 223
    codeliste: LocationTypeEnum
    bedeutung: globalIdInAT — Global ID in AT
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 224
    codeliste: LocationTypeEnum
    bedeutung: globalIdInCZ — Global ID in CZ
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 225
    codeliste: LocationTypeEnum
    bedeutung: globalIdInPL — Global ID in PL
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 226
    codeliste: LocationTypeEnum
    bedeutung: globalIdInDK — Global ID in DK
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 251
    codeliste: LocationTypeEnum
    bedeutung: suburb — Suburb / local quarter
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 252
    codeliste: LocationTypeEnum
    bedeutung: municipality
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 253
    codeliste: LocationTypeEnum
    bedeutung: county — County / rural district
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 254
    codeliste: LocationTypeEnum
    bedeutung: state — State. may be used to identify a country or a state.
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
  - wert: 255
    codeliste: LocationTypeEnum
    bedeutung: unspecified
    quelle: Q51
    fundstelle: Modul common, Typ LocationTypeEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Geräte, Orte und Subjekte (ASN.1)
<!-- /GEN:breadcrumb -->

# Geräte, Orte und Subjekte (ASN.1)

Mehrere Kennungen in `common` ([Q51](../../QUELLEN.md#q51)) benennen Beteiligte und Orte.

- `Subject` (`0x7F20`) ist der „name for an entity“, dem der öffentliche Schlüssel eines Zertifikats gehört. Es besteht aus der Organisation der Registrierungsstelle (`registrationAuthorityId`), einer Rolle (`subjectRole`) und optional Name und Nummer.
- `AppInstanceId` (`0x64`) ist ähnlich aufgebaut, aber ohne Name: Registrierungsstelle, Rolle und Nummer, jeweils von der Registrierungsstelle vergeben.
- `TerminalId` (`0x7F1F`) umfasst die Organisation des Terminalbetreibers, den Gerätetyp und die Terminalnummer. Nummer und Betreiber bilden zusammen ein eindeutiges Paar.
- `LocationId` (`0x7F69`) hat ein Ortsschema und eine Kennung nach diesem Schema. Als Schema sind `eticore` (1) und `ifopt` (2) vorgesehen.

Zwei Aufzählungen verweisen auf EN 1545-1:2015. `DeviceTypeEnum` hat 17 Werte, darunter Anmeldeterminal, Fahrkartenautomat und mobiles Kontrollterminal. `LocationTypeEnum` hat 39 Werte, vom Bushalt über Bahnhof und Straßenbahnhaltestelle bis zur Verkaufsstelle. Alle Werte stehen im Frontmatter. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Petra Pranke prüft in der Linie 4 mit dem Kontrollgerät T-4713. In etiCORE hat dieses Gerät eine Terminal-ID aus drei Teilen: der Organisation, die es betreibt, der BVB mit 9010, dem Gerätetyp und der Nummer des Geräts. Der Gerätetyp „Inspection terminal (mobile, operated by staff)“ passt zu ihm. Beim Lesegerät T-4712 am Hauptbahnhof wäre es ein anderer Typ.

Orte tragen ebenfalls eine Kennung samt Art. Die Berufsschule Tannenweg ist eine Haltestelle an der Linie 4, also eine Straßenbahnhaltestelle. Der Hauptbahnhof ist ein Bahnhof. Welche Kennung eine Haltestelle trägt, hängt vom Ortsschema ab: `eticore` oder `ifopt`.

Bei Pias BärenKarte steht die App-Instanz 90000042 der BVB. Sie ist ähnlich aufgebaut wie das Subject in einem Zertifikat: eine Registrierungsstelle, eine Rolle und eine Nummer.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `common`: `Subject`, `AppInstanceId`, `TerminalId`, `TerminalNumber`, `LocationId`, `DeviceTypeEnum`, `LocationTypeEnum`, `LocationSchemaTypeEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md) – Überblick
- [Akzeptanzterminal](../rollen/akzeptanzterminal.md) – das Gerät
- [CV-Zertifikat](../sicherheit/cv-zertifikat.md) – das Zertifikat, in dem das Subject steht

<!-- GEN:siehe_auch -->
## Siehe auch

- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md)
- [Akzeptanzterminal](../rollen/akzeptanzterminal.md) (AKT)
- [CV-Zertifikat](../sicherheit/cv-zertifikat.md) (CVC)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
