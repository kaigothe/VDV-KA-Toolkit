---
titel: Fehlercodes des Hotlist Service
englisch: error codes of the hotlist service
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/hotlist-service.md, lexikon/transaktionen/fehlercodes-eticore.md, lexikon/kontrolle/sperrliste.md]
quellen: [Q50]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: "E_HL_CCP_NOT_ACCEPTING_PRODUCT"
    codeliste: HotlistErrorEnum
    bedeutung: Das Produkt der zu sperrenden Berechtigung steht nicht in der Akzeptanzliste der Organisation, oder es ist kein interoperables Produkt.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_HOTLIST_ENTRY_ALREADY_EXISTS"
    codeliste: HotlistErrorEnum
    bedeutung: Der Hotlist-Eintrag besteht im Hotlist Service bereits.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_HOTLIST_ENTRY_ALREADY_REMOVED"
    codeliste: HotlistErrorEnum
    bedeutung: Der Hotlist-Eintrag wurde bereits entfernt. Relevant für Aufträge zum Entfernen.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_HOTLIST_ENTRY_EFFECTIVE_TIME_AFTER_EXPIRATION_TIME"
    codeliste: HotlistErrorEnum
    bedeutung: Der Beginn des Hotlist-Eintrags liegt nach seinem Ende.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_HOTLIST_ENTRY_EFFECTIVE_TIME_TOO_FAR"
    codeliste: HotlistErrorEnum
    bedeutung: Der Beginn des Hotlist-Eintrags liegt zu weit in der Vergangenheit (höchstens 5 Jahre).
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_HOTLIST_ENTRY_EXPIRATION_TIME_IN_THE_PAST"
    codeliste: HotlistErrorEnum
    bedeutung: Das Ende des Hotlist-Eintrags liegt in der Vergangenheit.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_HOTLIST_ENTRY_EXPIRATION_TIME_TOO_FAR"
    codeliste: HotlistErrorEnum
    bedeutung: Das Ende des Hotlist-Eintrags liegt zu weit in der Zukunft.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_HOTLIST_ENTRY_NOT_FOUND"
    codeliste: HotlistErrorEnum
    bedeutung: Der referenzierte Hotlist-Eintrag wurde nicht gefunden. Relevant für Aufträge zum Entfernen.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_INTEROPERABLE_PRODUCT_NOT_ALLOWED_IN_PRODUCT_ACCEPTANCE"
    codeliste: HotlistErrorEnum
    bedeutung: Interoperable Produkte dürfen nicht Teil der Liste der Produktakzeptanz sein.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_INVALID_BLOCKING_MODE"
    codeliste: HotlistErrorEnum
    bedeutung: Die Sperrart ist für den angegebenen Produkttyp ungültig.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_INVALID_TRANSITION_COUNTER"
    codeliste: HotlistErrorEnum
    bedeutung: Der Übergangszähler ist für den Produkttyp oder die Sperrart ungültig.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_PRODUCT_ACCEPTANCE_ALREADY_EXISTS"
    codeliste: HotlistErrorEnum
    bedeutung: Das Produkt steht bereits in der Akzeptanzliste der Organisation. Relevant beim Hinzufügen.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_PRODUCT_EXPIRY_DATE_TOO_FAR"
    codeliste: HotlistErrorEnum
    bedeutung: Das Ablaufdatum des Produkts liegt zu weit in der Zukunft. Gilt, wenn ein Produkt bei allen Akzeptanzpartnern entfernt wird.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_SCHEME_MANAGER_MAY_NOT_HOTLIST_HIMSELF"
    codeliste: HotlistErrorEnum
    bedeutung: Eine Organisation darf sich nicht selbst in die Hotlist eintragen.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_STILL_GENERATING_HOTLIST"
    codeliste: HotlistErrorEnum
    bedeutung: Der Zyklus der Hotlist wird gerade erzeugt; ein Abruf ist im Moment nicht möglich.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_UNAUTHORISED_TO_ADD_TO_OR_REMOVE_FROM_HOTLIST"
    codeliste: HotlistErrorEnum
    bedeutung: Der Absender darf den Eintrag nicht setzen oder entfernen, weil er nicht der Inhaber ist.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_UNKNOWN_ORGANISATION_FOR_HOTLISTING"
    codeliste: HotlistErrorEnum
    bedeutung: Die in die Hotlist einzutragende Organisation ist unbekannt.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_UNKNOWN_ORGANISATION_FOR_PRODUCT_ACCEPTANCE"
    codeliste: HotlistErrorEnum
    bedeutung: Die Anfrage nennt ein Produkt für einen Akzeptanzpartner, der unbekannt oder inaktiv ist.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_UNKNOWN_PRODUCT_ACCEPTANCE"
    codeliste: HotlistErrorEnum
    bedeutung: Das zu entfernende Produkt stand nicht in der Akzeptanzliste der Organisation.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_HL_UNKNOWN_PRODUCT_OWNER"
    codeliste: HotlistErrorEnum
    bedeutung: Die Organisations-ID des Product Owners ist unbekannt.
    quelle: Q50
    fundstelle: hotlist-event-enums_xsd, Aufzählung HotlistErrorEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Fehlercodes des Hotlist Service
<!-- /GEN:breadcrumb -->

# Fehlercodes des Hotlist Service

Der [Hotlist Service](hotlist-service.md) meldet Fehler mit Codes der Form `E_HL_…`; es sind 20 Codes der Aufzählung `HotlistErrorEnum` ([Q50](../../QUELLEN.md#q50), `hotlist-event-enums_xsd`). Sie lassen sich in fünf Gruppen ordnen:

- **Einträge:** `…_HOTLIST_ENTRY_ALREADY_EXISTS`, `…_ALREADY_REMOVED` und `…_NOT_FOUND`. Die beiden letzten gelten für Aufträge zum Entfernen.
- **Zeiträume:** Beginn nach dem Ende, Beginn mehr als fünf Jahre zurück, Ende in der Vergangenheit oder zu weit in der Zukunft.
- **Berechtigung zum Eintragen:** `E_HL_UNAUTHORISED_TO_ADD_TO_OR_REMOVE_FROM_HOTLIST` (der Absender ist nicht Inhaber), `E_HL_SCHEME_MANAGER_MAY_NOT_HOTLIST_HIMSELF` und die Codes zu unbekannten Organisationen und Product Ownern.
- **Produktakzeptanz:** In der Akzeptanzliste einer Organisation darf kein interoperables Produkt stehen. Doppeltes Hinzufügen, Entfernen eines unbekannten Produkts und ein zu fernes Ablaufdatum haben eigene Codes. `E_HL_CCP_NOT_ACCEPTING_PRODUCT` meldet, das Produkt stehe nicht in der Akzeptanzliste oder sei nicht interoperabel.
- **Sperrdaten und Listen:** ungültige Sperrart oder ungültiger Übergangszähler für den Produkttyp, und `E_HL_STILL_GENERATING_HOTLIST`, solange die Liste erzeugt wird.

Die Operationen, die diese Fehler liefern, stehen im Artikel zum Hotlist Service. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Pia findet ihre BärenKarte wieder. Bodo Bärlauch nimmt die Sperre der Applikation 90000042 aus der Hotlist. Versehentlich geht derselbe Auftrag noch einmal hinaus. Der Hotlist Service antwortet mit `E_HL_HOTLIST_ENTRY_ALREADY_REMOVED`: Der Eintrag ist schon weg.

Anderes Beispiel: Bodo will einen Eintrag setzen, dessen Ende gestern war. Das lehnt der Dienst ab, `E_HL_HOTLIST_ENTRY_EXPIRATION_TIME_IN_THE_PAST`, denn eine Sperre, die schon abgelaufen ist, hat keinen Zweck.

Und ein Fall für die Produktakzeptanz: Stellen wir uns vor, die BVB will eine Berechtigung des Nachbarverbunds sperren, deren Produkt, die Luchs-Monatskarte, bei ihr gar nicht in der Akzeptanzliste steht. Dann kommt `E_HL_CCP_NOT_ACCEPTING_PRODUCT`.

Und wenn Petra Pranke gerade die Hotlist abrufen will, während sie neu erzeugt wird? Dann bekommt sie `E_HL_STILL_GENERATING_HOTLIST` und fragt später wieder.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `hotlist-event-enums_xsd`: Aufzählung `HotlistErrorEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Hotlist Service](hotlist-service.md) – die Operationen
- [Fehlercodes (etiCORE)](../transaktionen/fehlercodes-eticore.md) – die Codes der Aktionsverwaltung
- [Sperrliste](sperrliste.md) – die Liste der KA

<!-- GEN:siehe_auch -->
## Siehe auch

- [Hotlist Service](hotlist-service.md)
- [Fehlercodes (etiCORE)](../transaktionen/fehlercodes-eticore.md)
- [Sperrliste](sperrliste.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
