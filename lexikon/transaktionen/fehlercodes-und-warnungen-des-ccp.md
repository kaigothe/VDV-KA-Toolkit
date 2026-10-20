---
titel: Fehlercodes und Warnungen des CCP
englisch: error codes and warnings of the CCP
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/fehlercodes-eticore.md, lexikon/transaktionen/warnungen-in-eticore.md, lexikon/kontrolle/sperrung.md, lexikon/transaktionen/bescheinigungen-zu-zahlungsmitteln-asn-1.md]
quellen: [Q50]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: "E_CCP_APP_INSTANCE_ID_NOT_MATCHING_DATABASE"
    codeliste: CcpErrorEnum
    bedeutung: Die App-Instanz-ID in der Sperranforderung stimmt nicht mit der Datenbank des CCP-Systems überein; die Berechtigung muss zur richtigen App-Instanz gehören.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_CCP_ENTITY_ALREADY_TERMINATED"
    codeliste: CcpErrorEnum
    bedeutung: Das Objekt ist bereits beendet; eine Sperranforderung ist nicht zulässig.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_CCP_PRODUCTID_OF_REFERENCED_CICO_NOT_ABPM"
    codeliste: CcpErrorEnum
    bedeutung: Die Produkt-ID der referenzierten Check-in-/Check-out-Meldungen gehört nicht zu einem kontobasierten Zahlungsmittel.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_CCP_PRODUCT_ID_NOT_MATCHING_DATABASE"
    codeliste: CcpErrorEnum
    bedeutung: Die Produkt-ID in der Sperranforderung stimmt nicht mit der Datenbank des CCP-Systems überein; die Berechtigung muss dem richtigen Produkt zugeordnet sein.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_CCP_RECEIVER_IS_NOT_ENTITY_OWNER"
    codeliste: CcpErrorEnum
    bedeutung: Der Empfänger ist nicht Inhaber des betroffenen Objekts; bei Sperranforderungen gehört das Objekt zu einer Berechtigung oder Applikation.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_CCP_REFERENCED_CICO_NOTIFICATION_NOT_FOUND_IN_DATABASE"
    codeliste: CcpErrorEnum
    bedeutung: Die referenzierte Check-in- oder Check-out-Meldung steht nicht in der Datenbank.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_CCP_REFERENCED_CICO_NOT_HAVE_SAME_ENTITLMENTID"
    codeliste: CcpErrorEnum
    bedeutung: Die referenzierten Meldungen einer Reise tragen nicht dieselbe Berechtigungs-ID.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_CCP_REFERENCED_CICO_NOT_HAVE_SAME_PRODUCTID"
    codeliste: CcpErrorEnum
    bedeutung: Die referenzierten Meldungen einer Reise tragen nicht dieselbe Produkt-ID.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCPSTE_STATIC_ENTITLEMENT_DELIVERY_UNCLEAR"
    codeliste: CcpSteWarningEnum
    bedeutung: Es ließ sich nicht bestätigen, dass die ausgegebene statische Berechtigung ihr Ziel erreicht hat; ähnlich einer Zeitüberschreitung bei einer Transaktion.
    quelle: Q50
    fundstelle: ccp-ste-event-enums_xsd, Aufzählung CcpSteWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_ABPM_DEBITING_SALES_ITEM_VOID"
    codeliste: CcpWarningEnum
    bedeutung: Die Abbuchung beruht auf einer ungültigen Verkaufsposition; das Konto des kontobasierten Zahlungsmittels darf NICHT belastet werden.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_APPLICATION_SHOULD_STILL_BE_BLOCKED"
    codeliste: CcpWarningEnum
    bedeutung: "Die Applikation müsste noch gesperrt sein. Überwachung: Es gibt Meldungen, obwohl die Applikation als gesperrt gilt."
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_APPLICATION_STATE_NOT_VALID_FOR_ACTION"
    codeliste: CcpWarningEnum
    bedeutung: Der Statuscode der Applikation erlaubt die ausgeführte Aktion nicht.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_DUPLICATE_APPLICATION_TRANSITION_COUNTER"
    codeliste: CcpWarningEnum
    bedeutung: Der Wert des Übergangszählers der Applikation wurde schon für eine andere Aktion verwendet.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_DUPLICATE_ENTITLEMENT_ISSUANCE_COUNTER"
    codeliste: CcpWarningEnum
    bedeutung: Der Wert des Ausgabezählers wurde schon für die Ausgabe einer anderen Berechtigung verwendet.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_ENTITLEMENT_SHOULD_STILL_BE_BLOCKED"
    codeliste: CcpWarningEnum
    bedeutung: "Die Berechtigung müsste noch gesperrt sein. Überwachung: Es gibt Meldungen, obwohl die Berechtigung als gesperrt gilt."
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_ILLEGAL_BLOCKING_OF_APPLICATION"
    codeliste: CcpWarningEnum
    bedeutung: Die Sperrung der Applikation war nicht autorisiert.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_ILLEGAL_BLOCKING_OF_ENTITLEMENT"
    codeliste: CcpWarningEnum
    bedeutung: Die Sperrung der Berechtigung war nicht autorisiert.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_ILLEGAL_UNBLOCKING_OF_APPLICATION"
    codeliste: CcpWarningEnum
    bedeutung: Die Entsperrung der Applikation war nicht autorisiert.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_ILLEGAL_UNBLOCKING_OF_ENTITLEMENT"
    codeliste: CcpWarningEnum
    bedeutung: Die Entsperrung der Berechtigung war nicht autorisiert.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_INVALID_STORED_VALUE_BALANCE_CHANGE"
    codeliste: CcpWarningEnum
    bedeutung: Der Kontostand des Guthabens wurde unzulässig verändert.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_MISSING_APPLICATION_TRANSITION_COUNTER"
    codeliste: CcpWarningEnum
    bedeutung: Ein oder mehrere Werte des Übergangszählers der Applikation scheinen verwendet, aber nicht gemeldet worden zu sein.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_MISSING_ENTITLEMENT_ISSUANCE_COUNTER"
    codeliste: CcpWarningEnum
    bedeutung: Ein oder mehrere Werte des Ausgabezählers scheinen verwendet, aber in keiner Ausgabemeldung gemeldet worden zu sein.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_REFERENCED_CICO_OPEN_EVENTS"
    codeliste: CcpWarningEnum
    bedeutung: Die referenzierten Check-in-/Check-out-Meldungen haben Warn- oder Fehlerereignisse, die noch in Bearbeitung sind.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_SVPM_DEBITING_SALES_ITEM_VOID"
    codeliste: CcpWarningEnum
    bedeutung: Die Abbuchung beruht auf einer ungültigen Verkaufsposition, das Guthaben-Zahlungsmittel wurde aber bereits belastet; der Betrag ist dem Kunden zu erstatten oder dem Zahlungsmittel gutzuschreiben.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CCP_UM_SKIPPED_APPLICATION_TRANSITION_COUNTER"
    codeliste: CcpWarningEnum
    bedeutung: Die App-Instanz des Mediums hat einen oder mehrere Werte des Übergangszählers übersprungen.
    quelle: Q50
    fundstelle: ccp-event-enums_xsd, Aufzählung CcpWarningEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Fehlercodes und Warnungen des CCP
<!-- /GEN:breadcrumb -->

# Fehlercodes und Warnungen des CCP

Die CCP-Systeme melden 8 Fehler (`CcpErrorEnum`), 16 Warnungen (`CcpWarningEnum`) und eine Warnung zur statischen Berechtigung (`CcpSteWarningEnum`) ([Q50](../../QUELLEN.md#q50), `ccp-event-enums_xsd`, `ccp-ste-event-enums_xsd`).

**Fehler** betreffen zwei Fälle. Bei einer Sperranforderung: App-Instanz oder Produkt stimmen nicht mit der Datenbank überein, das Objekt ist schon beendet, oder der Empfänger ist nicht dessen Inhaber. Beim Check-in/Check-out: die referenzierte Meldung fehlt in der Datenbank, die Meldungen einer Reise tragen nicht dieselbe Berechtigungs- oder Produkt-ID, oder das Produkt ist kein kontobasiertes Zahlungsmittel.

**Warnungen** sind Plausibilitätsprüfungen, zum Teil ausdrücklich „used for monitoring“:
- Zähler: Werte des Übergangszählers der Applikation oder des Ausgabezählers doppelt, fehlend oder vom Medium übersprungen;
- Sperrungen: unberechtigte Sperrung oder Entsperrung von Applikation und Berechtigung, Meldungen trotz angenommener Sperre;
- Guthaben: unzulässige Änderung des Kontostands; Belastung aufgrund einer ungültigen Verkaufsposition, die beim kontobasierten Zahlungsmittel nicht belasten darf und beim Guthaben zu erstatten ist;
- `W_CCPSTE_STATIC_ENTITLEMENT_DELIVERY_UNCLEAR`: Es ist unklar, ob eine ausgegebene statische Berechtigung ihr Ziel erreichte, ähnlich einer Zeitüberschreitung.

Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Bei der BVB geht eine Sperranforderung für Pias Berechtigung ein, die aber die Applikation der Ersatzkarte nennt, 90000043. Das CCP-System der BVB gleicht mit seiner Datenbank ab und antwortet `E_CCP_APP_INSTANCE_ID_NOT_MATCHING_DATABASE`: Die Berechtigung gehört zur anderen Applikation.

Die Warnungen sind leiser, sie unterbrechen nichts. Das Hintergrundsystem der BVB sieht in den Meldungen des SAM die Ausgabezähler 41 und 43, die 42 fehlt. Es setzt `W_CCP_MISSING_ENTITLEMENT_ISSUANCE_COUNTER`. Vielleicht ist die Meldung unterwegs. Vielleicht wurde eine Ausgabe nicht gemeldet. Die Warnung sagt nur: Hier fehlt etwas, schaut nach.

Olli Tapsig hat Guthaben, und beim Kauf eines Einzelfahrscheins wird abgebucht. Stellt sich später heraus, dass die Verkaufsposition ungültig war, steht das Geld schon abgebucht: `W_CCP_SVPM_DEBITING_SALES_ITEM_VOID`. Olli bekommt es erstattet oder gutgeschrieben. Wäre es ein Konto gewesen, hätte es gar nicht belastet werden dürfen, das ist `W_CCP_ABPM_DEBITING_SALES_ITEM_VOID`.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `ccp-event-enums_xsd`, `ccp-ste-event-enums_xsd`: Aufzählungen `CcpErrorEnum`, `CcpWarningEnum`, `CcpSteWarningEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Fehlercodes (etiCORE)](fehlercodes-eticore.md) – die Codes der Aktionsverwaltung
- [Warnungen in etiCORE](warnungen-in-eticore.md) – die allgemeinen Plausibilitätsprüfungen
- [Sperrung](../kontrolle/sperrung.md) – der Vorgang
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](bescheinigungen-zu-zahlungsmitteln-asn-1.md) – Guthaben und Zähler

<!-- GEN:siehe_auch -->
## Siehe auch

- [Fehlercodes (etiCORE)](fehlercodes-eticore.md)
- [Warnungen in etiCORE](warnungen-in-eticore.md)
- [Sperrung](../kontrolle/sperrung.md)
- [Bescheinigungen zu Zahlungsmitteln (ASN.1)](bescheinigungen-zu-zahlungsmitteln-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
