---
titel: Warnungen in etiCORE
englisch: warnings in etiCORE
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/fehlercodes-eticore.md, lexikon/transaktionen/fehlercodes-und-warnungen-des-ccp.md, lexikon/transaktionen/bescheinigungen-zu-berechtigungen-asn-1.md, lexikon/datenformate/zaehler-zeit-und-versionen-asn-1.md]
quellen: [Q50]
status: zu prüfen
offene_fragen: [O22]
stand: 2026-10-20
codes:
  - wert: "W_CO_ACTION_NOT_IN_VALIDITY_PERIOD_OF_OBJECT"
    codeliste: CommonWarningEnum
    bedeutung: Das referenzierte Objekt wurde außerhalb seiner Gültigkeit verwendet.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ACTION_NOT_VALID_FOR_PRODUCT_TYPE"
    codeliste: CommonWarningEnum
    bedeutung: Manche Aktionen gelten nur für bestimmte Produkttypen, etwa darf nur ein Guthaben-Zahlungsmittel aufgeladen werden.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_DUPLICATE_ENTITLEMENT_ACTION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Der Wert des Aktionszählers der Berechtigung wurde schon für eine andere Aktion verwendet.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_DUPLICATE_ENTITLEMENT_ID"
    codeliste: CommonWarningEnum
    bedeutung: Die Berechtigungs-ID ist bereits registriert; vermutlich wurde eine Berechtigung mit dieser ID mehrfach ausgegeben.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_DUPLICATE_ENTITLEMENT_TRANSITION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Der Wert des Übergangszählers der Berechtigung wurde schon für eine andere Aktion verwendet.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_DUPLICATE_PRODUCT_ISSUANCE_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Der Wert des Produktausgabezählers wurde schon für die Ausgabe einer anderen Berechtigung verwendet.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_DUPLICATE_SAM_ACTION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Der Wert des SAM-Aktionszählers wurde schon für eine andere Aktion verwendet.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ENTITLEMENT_ALREADY_REPLACED"
    codeliste: CommonWarningEnum
    bedeutung: Die angegebene ersetzte Berechtigung wurde bereits nach einem Aktionsauftrag oder einer anderen Ausgabemeldung ersetzt.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ENTITLEMENT_ISSUED_WITH_INVALID_ACTION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Der Anfangsstatus der Berechtigung ist ungültig (Beschreibung der Quelle; der Name nennt den Aktionszähler).
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ENTITLEMENT_ISSUED_WITH_INVALID_EFFECTIVE_TIME"
    codeliste: CommonWarningEnum
    bedeutung: Der Beginn der Berechtigung liegt nach ihrem Ende.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ENTITLEMENT_ISSUED_WITH_INVALID_EXPIRATION_TIME"
    codeliste: CommonWarningEnum
    bedeutung: Das Ende der Berechtigung liegt nach dem Ende der Applikation.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ENTITLEMENT_ISSUED_WITH_INVALID_STATUS"
    codeliste: CommonWarningEnum
    bedeutung: Der Anfangsstatus der Berechtigung war nicht auf gültig gesetzt.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ENTITLEMENT_ISSUED_WITH_INVALID_TRANSITION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Der anfängliche Übergangszähler der Berechtigung ist ungültig.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ENTITLEMENT_STATE_NOT_VALID_FOR_ACTION"
    codeliste: CommonWarningEnum
    bedeutung: Der Statuscode der Berechtigung erlaubt die ausgeführte Aktion nicht.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ENTITY_SHOULD_HAVE_BEEN_BLOCKED_OR_REJECTED"
    codeliste: CommonWarningEnum
    bedeutung: Das referenzierte Objekt hätte gesperrt oder abgewiesen werden müssen, statt dass eine Aktion damit ausgeführt wurde.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_FALSE_ISSUING_ABORTED_NOTIFICATION"
    codeliste: CommonWarningEnum
    bedeutung: Eine Berechtigung, deren Ausgabe angeblich abgebrochen wurde, wurde im Betrieb gesehen.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_INVALID_USER_MEDIUM_SIGNATURE"
    codeliste: CommonWarningEnum
    bedeutung: Die Signatur des Mediums unter einer Bescheinigung ist ungültig.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_ISSUANCE_OUTSIDE_SAM_VALIDITY_PERIOD"
    codeliste: CommonWarningEnum
    bedeutung: Die (statische) Berechtigung wurde außerhalb der Gültigkeit des ausgebenden SAM ausgegeben.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_MISSING_ENTITLEMENT_ACTION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Ein oder mehrere Werte des Aktionszählers der Berechtigung scheinen verwendet, aber nicht gemeldet worden zu sein.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_MISSING_ENTITLEMENT_ISSUED_NOTIFICATION"
    codeliste: CommonWarningEnum
    bedeutung: Die Ausgabemeldung zu einer Berechtigung fehlt, obwohl die Berechtigung schon benutzt wird. Dem Empfänger bekannte Nutzungsmeldungen sind über die Nachrichtenreferenz im Ereignis angegeben, die Berechtigungs-ID in der Ereignisbeschreibung.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_MISSING_ENTITLEMENT_TRANSITION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Ein oder mehrere Werte des Übergangszählers der Berechtigung scheinen verwendet, aber nicht gemeldet worden zu sein.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_MISSING_LAST_SAM_ACTION_DATA"
    codeliste: CommonWarningEnum
    bedeutung: Alle Meldungen je Applikation oder Berechtigung außer der ersten (Aktionszähler 1) müssen das Objekt lastSamActionData enthalten.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_MISSING_PRODUCT_ISSUANCE_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Ein oder mehrere Werte des Produktausgabezählers scheinen verwendet, aber in keiner Ausgabemeldung gemeldet worden zu sein.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_MISSING_SAM_ACTION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Ein oder mehrere Werte des SAM-Aktionszählers scheinen verwendet, aber nicht gemeldet worden zu sein.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_PRODUCT_ID_DEVIATES_ILLEGALLY"
    codeliste: CommonWarningEnum
    bedeutung: Die Produkt-ID in der Meldung weicht unzulässig von der in der Ausgabemeldung ab.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_SAM_USAGE_OUTSIDE_ITS_VALIDITY_PERIOD"
    codeliste: CommonWarningEnum
    bedeutung: Das SAM wurde für eine Aktion außerhalb seiner Gültigkeit benutzt.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STATUS_NOT_BLOCKED_AFTER_BLOCKING"
    codeliste: CommonWarningEnum
    bedeutung: Der Status des Objekts ist nach einer Sperrung nicht „gesperrt“.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STATUS_NOT_OK_AFTER_UNBLOCKING"
    codeliste: CommonWarningEnum
    bedeutung: Der Status des Objekts ist nach einer Entsperrung nicht „in Ordnung“.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STATUS_NOT_TERMINATED_AFTER_TERMINATION"
    codeliste: CommonWarningEnum
    bedeutung: Der Status des Objekts ist nach einer Beendigung nicht „beendet“.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STORED_VALUE_AUTOLOAD_PARAMETERS_DISALLOWED_FOR_PRODUCT"
    codeliste: CommonWarningEnum
    bedeutung: Autoload-Parameter sind vorhanden, obwohl sie für diesen Produkttyp verboten sind.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STORED_VALUE_AUTOLOAD_PARAMETERS_INCONSISTENT"
    codeliste: CommonWarningEnum
    bedeutung: Die Autoload-Parameter widersprechen einander oder dem Höchstbetrag.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STORED_VALUE_AUTOLOAD_PARAMETERS_INVALID_AMOUNT"
    codeliste: CommonWarningEnum
    bedeutung: Der Autoload-Betrag ist ungültig.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STORED_VALUE_AUTOLOAD_PARAMETERS_INVALID_THRESHOLD"
    codeliste: CommonWarningEnum
    bedeutung: Die Autoload-Schwelle ist ungültig.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STORED_VALUE_PARAMETERS_DISALLOWED_FOR_PRODUCT"
    codeliste: CommonWarningEnum
    bedeutung: Guthaben-Parameter sind vorhanden, obwohl sie für diesen Produkttyp verboten sind.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STORED_VALUE_PARAMETERS_INVALID_INITIAL_CURRENT_BALANCE"
    codeliste: CommonWarningEnum
    bedeutung: Der anfängliche Kontostand des Guthabens ist ungültig.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STORED_VALUE_PARAMETERS_INVALID_MAXIMUM_BALANCE"
    codeliste: CommonWarningEnum
    bedeutung: Der Höchstbetrag des Guthabens ist ungültig.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_STORED_VALUE_PARAMETERS_MISSING_FOR_PRODUCT"
    codeliste: CommonWarningEnum
    bedeutung: Guthaben-Parameter fehlen, obwohl sie für diesen Produkttyp verlangt sind.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_TERMINAL_DOES_NOT_BELONG_TO_SAM_OWNER"
    codeliste: CommonWarningEnum
    bedeutung: "Empfehlung: Terminalbetreiber und SAM-Inhaber sollten immer identisch sein."
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_TRANSACTION_TIMED_OUT"
    codeliste: CommonWarningEnum
    bedeutung: Das Medium hat auf den Befehl zum Abschluss der Transaktion nicht geantwortet; es kam zu einer Zeitüberschreitung.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_UM_APP_INSTANCE_ID_DEVIATES"
    codeliste: CommonWarningEnum
    bedeutung: Die App-Instanz-ID des Mediums in der Meldung weicht von der in der Ausgabemeldung ab.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_CO_UM_SKIPPED_ENTITLEMENT_ACTION_COUNTER"
    codeliste: CommonWarningEnum
    bedeutung: Die App-Instanz des Mediums hat einen oder mehrere Werte des Aktionszählers der Berechtigung übersprungen.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_POSTE_IMPLAUSIBLE_INSPECTIONS"
    codeliste: PoSteWarningEnum
    bedeutung: Die statische Berechtigung wurde mehrfach geprüft, und die Abstände in Zeit und Raum zwischen den Prüfungen wirken unplausibel.
    quelle: Q50
    fundstelle: po-ste-event-enums_xsd, Aufzählung PoSteWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_PO_ENTITLEMENT_HOTLISTED_OUTSIDE_VALIDITY_PERIOD"
    codeliste: PoWarningEnum
    bedeutung: Die gesperrte Berechtigung liegt nicht mehr in ihrer Gültigkeit; der Hotlist-Eintrag ist zu entfernen.
    quelle: Q50
    fundstelle: po-event-enums_xsd, Aufzählung PoWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_PO_ENTITLEMENT_HOTLISTING_STATUS_OBSOLETE"
    codeliste: PoWarningEnum
    bedeutung: Die gesperrte Berechtigung ist bereits gesperrt oder beendet; der Hotlist-Eintrag ist zu entfernen.
    quelle: Q50
    fundstelle: po-event-enums_xsd, Aufzählung PoWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_PO_ENTITLEMENT_ISSUED_WITH_UNKNOWN_PRODUCT"
    codeliste: PoWarningEnum
    bedeutung: Das Produkt der ausgegebenen Berechtigung ist unbekannt.
    quelle: Q50
    fundstelle: po-event-enums_xsd, Aufzählung PoWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_PO_ENTITLEMENT_ISSUED_WITH_WRONG_PRODUCT_TYPE"
    codeliste: PoWarningEnum
    bedeutung: Das Produkt der ausgegebenen Berechtigung hat einen falschen Produkttyp.
    quelle: Q50
    fundstelle: po-event-enums_xsd, Aufzählung PoWarningEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_PO_ORDER_NUMBER_ALSO_USED_FOR_ACTION_ORDERING"
    codeliste: PoWarningEnum
    bedeutung: Die Auftragsnummer der ausgegebenen Berechtigung wurde auch für einen Aktionsauftrag verwendet. Entweder hat die ausgebende Stelle die falsche Operation aufgerufen (notifyEntitlementIssued statt notifyOrderedEntitlementIssued), oder der primäre CCP verwendet Auftragsnummern unzulässig mehrfach. Im ersten Fall ist der Aktionsauftrag zu stornieren. Der zweite Fall ist verboten, weil Terminals sonst den Aktionsauftrag fälschlich als ausgeführt ansehen könnten und Sperraufträge zu dieser Nummer eine falsche Berechtigung sperren könnten.
    quelle: Q50
    fundstelle: po-event-enums_xsd, Aufzählung PoWarningEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Warnungen in etiCORE
<!-- /GEN:breadcrumb -->

# Warnungen in etiCORE

Die Warncodes `W_CO_…` (41 Codes, `CommonWarningEnum`) und `W_PO_…` (6, `PoWarningEnum`) sowie `W_POSTE_…` (1) beschreiben **Plausibilitätsprüfungen**: Sie unterbrechen keine Verarbeitung, zeigen aber, dass Meldungen nicht zusammenpassen ([Q50](../../QUELLEN.md#q50), `common-event-enums_xsd`, `po-event-enums_xsd`, `po-ste-event-enums_xsd`). Die Gruppen:

- **Zähler:** Werte von SAM-Aktionszähler, Aktionszähler und Übergangszähler der Berechtigung und Produktausgabezähler doppelt (`W_CO_DUPLICATE_…`), fehlend (`…_MISSING_…`) oder vom Medium übersprungen (`…_UM_SKIPPED_…`).
- **Anfangswerte bei der Ausgabe:** Beginn nach Ende, Ende nach dem Ende der Applikation, ungültiger Anfangsstatus oder -zähler.
- **Status nach Aktion:** nach Sperrung nicht „gesperrt“, nach Entsperrung nicht „in Ordnung“, nach Beendigung nicht „beendet“, Aktion im falschen Status.
- **Guthaben:** Parameter fehlen, sind unzulässig oder widersprüchlich (Höchstbetrag, Anfangsstand, Autoload).
- **Gültigkeit und Meldungen:** Nutzung außerhalb der Gültigkeit von Objekt oder SAM, fehlende Ausgabemeldung bei benutztem Ticket, fehlendes `lastSamActionData`, ungültige Mediumsignatur, abweichende Produkt- oder App-Instanz-ID.
- **Produkte und Hotlist (`W_PO_`):** unbekanntes Produkt, falscher Produkttyp, Hotlist-Eintrag außerhalb der Gültigkeit oder überholt, Auftragsnummer für Ausgabe und Aktionsauftrag doppelt verwendet. `W_POSTE_IMPLAUSIBLE_INSPECTIONS` meldet unplausible Abstände mehrerer Prüfungen einer statischen Berechtigung.

Für ein Analysewerkzeug sind sie eine fertige Prüfliste (abgeleitet). Bei `W_CO_ENTITLEMENT_ISSUED_WITH_INVALID_ACTION_COUNTER` passt der Text der Quelle nicht zum Namen (zu prüfen, O22). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Ein Prüfer im Büro, der jeden Tag Kassenzettel nachzählt, merkt Unstimmigkeiten, ohne dass etwas Schlimmes passiert sein muss. Das sind die Warnungen.

Die laufenden Nummern sind seine Lieblingsprüfung. Auf Pias ABO Azubi hat jede Ausgabe und jede Aktion eine Nummer, die nur hochzählt. Fehlt eine, dann kann das ein Fehler in der Übermittlung sein oder ein Gerät, das nicht gemeldet hat. Taucht eine Nummer zweimal auf, wurde etwas doppelt geschickt oder doppelt vergeben. Beides ist unschön, aber nicht unbedingt ein Betrug.

Auch der Status wird nachgeprüft. Sperrt Bodo Bärlauch Pias Berechtigung und die Bescheinigung danach zeigt „in Ordnung“, stimmt etwas nicht, und `W_CO_STATUS_NOT_BLOCKED_AFTER_BLOCKING` sagt es.

Und bei Olli Tapsigs Guthaben wird geprüft, ob die Zahlen zusammenpassen: Ein Anfangsstand, der nicht zu den Vorgaben passt, ist nicht plausibel (`…_INVALID_INITIAL_CURRENT_BALANCE`).

Nicht jede Warnung ist ein Fehler. Aber eine Warnung, die immer wieder bei demselben Gerät auftaucht, verdient einen Blick.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `common-event-enums_xsd`, `po-event-enums_xsd`, `po-ste-event-enums_xsd`: Aufzählungen `CommonWarningEnum`, `PoWarningEnum`, `PoSteWarningEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Fehlercodes (etiCORE)](fehlercodes-eticore.md) – die Fehlercodes der Aktionsverwaltung
- [Fehlercodes und Warnungen des CCP](fehlercodes-und-warnungen-des-ccp.md) – die Warnungen der CCP-Systeme
- [Bescheinigungen zu Berechtigungen (ASN.1)](bescheinigungen-zu-berechtigungen-asn-1.md) – was geprüft wird
- [Zähler, Zeit und Versionen (ASN.1)](../datenformate/zaehler-zeit-und-versionen-asn-1.md) – die Zähler

<!-- GEN:siehe_auch -->
## Siehe auch

- [Fehlercodes (etiCORE)](fehlercodes-eticore.md)
- [Fehlercodes und Warnungen des CCP](fehlercodes-und-warnungen-des-ccp.md)
- [Bescheinigungen zu Berechtigungen (ASN.1)](bescheinigungen-zu-berechtigungen-asn-1.md)
- [Zähler, Zeit und Versionen (ASN.1)](../datenformate/zaehler-zeit-und-versionen-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
