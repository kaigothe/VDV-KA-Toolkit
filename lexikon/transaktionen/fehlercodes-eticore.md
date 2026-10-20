---
titel: Fehlercodes (etiCORE)
englisch: error codes in etiCORE
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/aktionsmanagement/aktionsmanagement-in-eticore.md, lexikon/aktionsmanagement/aktionsfreigabe.md, lexikon/transaktionen/nachrichten-in-ka-1-x-und-eticore.md]
quellen: [Q50]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: E_POOAM_ACTION_ORDER_EXPIRED
    codeliste: PoOaManagementErrorEnum
    bedeutung: Der Aktionsauftrag ist abgelaufen.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_APP_INSTANCE_ID_NOT_IDENTICAL_OVER_GROUP
    codeliste: PoOaManagementErrorEnum
    bedeutung: In einer Auftragsgruppe muss die App-Instanz-ID des Mediums für alle Aufträge gleich sein.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_CONFLICTING_ACTION_ORDER_EXISTS
    codeliste: PoOaManagementErrorEnum
    bedeutung: Für die zu löschende oder zu entsperrende Berechtigung ist bereits ein anderer Aktionsauftrag aktiv.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_DUPLICATE_ORDER_ID
    codeliste: PoOaManagementErrorEnum
    bedeutung: Die Auftrags-ID ist bereits vergeben.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_ENTITLEMENT_ALREADY_REPLACED
    codeliste: PoOaManagementErrorEnum
    bedeutung: Die angegebene ersetzte Berechtigung wurde bereits durch einen anderen Auftrag oder eine andere Ausgabemeldung ersetzt.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_GROUP_ID_NOT_IDENTICAL_OVER_GROUP
    codeliste: PoOaManagementErrorEnum
    bedeutung: In einer Auftragsgruppe muss die Gruppen-ID gesetzt und für alle Aufträge gleich sein.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_INVALID_ISSUANCE_PARAMETERS
    codeliste: PoOaManagementErrorEnum
    bedeutung: Die Ausgabeparameter sind ungültig und würden vom Medium abgelehnt.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_INVALID_MAXIMUM_BALANCE
    codeliste: PoOaManagementErrorEnum
    bedeutung: Der Höchstbetrag des Guthabens im Ausgabeauftrag entspricht nicht der Festlegung des Product Owners.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_INVALID_METADATA
    codeliste: PoOaManagementErrorEnum
    bedeutung: Die Metadaten der Ausgabe im Ausgabeauftrag entsprechen nicht der Festlegung des Product Owners.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_INVALID_PRODUCT_PARAMETERS
    codeliste: PoOaManagementErrorEnum
    bedeutung: Die Produktparameter verstoßen gegen die Tarifregeln.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_ORDER_ALREADY_CANCELLED
    codeliste: PoOaManagementErrorEnum
    bedeutung: Der Auftrag kann nicht storniert werden, weil er bereits storniert wurde.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_ORDER_ALREADY_EXECUTED
    codeliste: PoOaManagementErrorEnum
    bedeutung: Der Auftrag kann nicht storniert werden, weil er bereits ausgeführt wurde.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_REFERENCED_ACTION_ORDER_UNKNOWN
    codeliste: PoOaManagementErrorEnum
    bedeutung: Die Auftrags-ID lässt sich keinem bekannten Aktionsauftrag zuordnen.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_RETRIEVAL_PERMISSION_MISSING
    codeliste: PoOaManagementErrorEnum
    bedeutung: Die Aktionsliste darf nur abrufen, wem der Product Owner dies über die Konfiguration erlaubt hat.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_SENDER_NOT_ENTITLEMENT_OWNER
    codeliste: PoOaManagementErrorEnum
    bedeutung: Der Absender des Aktionsauftrags ist nicht Inhaber der Berechtigung.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_SENDER_TO_ORDER_ID_MISMATCH
    codeliste: PoOaManagementErrorEnum
    bedeutung: Die Organisations-ID in der Auftrags-ID ist nicht die des Absenders.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_POOAM_STILL_GENERATING_ACTION_LIST
    codeliste: PoOaManagementErrorEnum
    bedeutung: Der Zyklus der Aktionsliste wird gerade erzeugt; ein Abruf ist im Moment nicht möglich.
    quelle: Q50
    fundstelle: po-oa-management-event-enums_xsd, Aufzählung PoOaManagementErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_APP_INSTANCE_ID_UNKNOWN
    codeliste: CommonErrorEnum
    bedeutung: Die übermittelte App-Instanz-ID ist dem Empfänger nicht bekannt.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_BINARY_STRUCTURE_CANNOT_BE_PROCESSED
    codeliste: CommonErrorEnum
    bedeutung: Die binäre Struktur in der Anfrage lässt sich nicht verarbeiten.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_CANNOT_DECOMPRESS_DATA
    codeliste: CommonErrorEnum
    bedeutung: Die eingebetteten komprimierten Daten lassen sich nicht entpacken (kein gültiger Base64-Wert oder kein gültiges ZIP-Archiv).
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_CYCLE_NUMBER_UNKNOWN_OR_TOO_OLD
    codeliste: CommonErrorEnum
    bedeutung: Inkrementelle Liste: Der Zyklus ist dem liefernden System unbekannt oder zu alt; die vollständige Liste ist anzufordern.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_DUPLICATE_HOTLISTING_DEMAND_REVOCATION
    codeliste: CommonErrorEnum
    bedeutung: Die Sperranforderung wurde bereits widerrufen.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_DUPLICATE_UM_ATTESTATION
    codeliste: CommonErrorEnum
    bedeutung: Die vom Medium signierte Bescheinigung wurde bereits verarbeitet.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_INCORRECT_CHECKSUM
    codeliste: CommonErrorEnum
    bedeutung: Inkrementelle Liste: Die Prüfsumme zum Zyklus stimmt nicht mit der des liefernden Systems überein; als Ausweg kann die vollständige Liste angefordert werden.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_MEDIA_COMMUNICATION_FAILURE
    codeliste: CommonErrorEnum
    bedeutung: Die Kommunikation mit einem Medium ist fehlgeschlagen.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_NO_MATCHING_HOTLISTING_DEMAND_TO_REVOKE
    codeliste: CommonErrorEnum
    bedeutung: Die zu widerrufende Sperranforderung wurde nicht gefunden.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_SAM_LOSS
    codeliste: CommonErrorEnum
    bedeutung: Der Kommunikationskanal zum SAM ist abgebrochen.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_THIRD_PARTY_SYSTEM_ERROR
    codeliste: CommonErrorEnum
    bedeutung: Beim Zugriff auf ein Drittsystem trat eine Zeitüberschreitung oder ein anderer Fehler auf; die Anfrage lässt sich nicht verarbeiten.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_UM_LOSS
    codeliste: CommonErrorEnum
    bedeutung: Der Kommunikationskanal zum Medium ist abgebrochen.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_UNKNOWN_BLOCKING_MODE
    codeliste: CommonErrorEnum
    bedeutung: Die verwendete Sperrart ist unbekannt.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_UNKNOWN_BLOCKING_REASON
    codeliste: CommonErrorEnum
    bedeutung: Der verwendete Sperrgrund ist unbekannt.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_WRONG_ATTESTATION_IN_NOTIFICATION
    codeliste: CommonErrorEnum
    bedeutung: Eine vom Medium signierte Bescheinigung steckt in der falschen Meldung.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_WRONG_ELEMENT_IN_COMPRESSED_DATA
    codeliste: CommonErrorEnum
    bedeutung: Die komprimierten Daten enthalten nicht das erwartete Element.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_WRONG_SECURITY_LEVEL
    codeliste: CommonErrorEnum
    bedeutung: Ein referenziertes Objekt (SAM-ID, Berechtigungs-ID, App-Instanz-ID u. a.) gehört zur falschen Sicherheitsstufe.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CO_WRONG_SUBJECT_ROLE
    codeliste: CommonErrorEnum
    bedeutung: Die Subjektrolle in der App-Instanz-ID ist in diesem Zusammenhang nicht erlaubt.
    quelle: Q50
    fundstelle: common-event-enums_xsd, Aufzählung CommonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_PO_GIVEN_VALIDITY_TIME_TOO_FAR
    codeliste: PoErrorEnum
    bedeutung: Der angegebene Zeitpunkt für die Abfrage gültiger Berechtigungen liegt zu weit entfernt.
    quelle: Q50
    fundstelle: po-event-enums_xsd, Aufzählung PoErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_PO_RECEIVER_IS_NOT_PRODUCT_OWNER_OF_OBJECT
    codeliste: PoErrorEnum
    bedeutung: Der Empfänger ist nicht der Product Owner des Objekts.
    quelle: Q50
    fundstelle: po-event-enums_xsd, Aufzählung PoErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: E_CCPOAO_REFERENCED_ACTION_ORDER_UNKNOWN
    codeliste: CcpOaOrderingErrorEnum
    bedeutung: Die Meldung lässt sich keinem bekannten Aktionsauftrag zuordnen.
    quelle: Q50
    fundstelle: ccp-oa-ordering-event-enums_xsd, Aufzählung CcpOaOrderingErrorEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Fehlercodes (etiCORE)
<!-- /GEN:breadcrumb -->

# Fehlercodes (etiCORE)

etiCORE meldet Fehler und Warnungen der Schnittstellen mit festen Textcodes. Fehler beginnen mit `E_`, Warnungen mit `W_`; dann folgt das Kürzel des Bereichs ([Q50](../../QUELLEN.md#q50), `*-event-enums_xsd`). `E_POOAM_` stammt aus der Aktionsverwaltung des Product Owners, `E_CO_` ist allgemein, `E_PO_` gehört zum PO-System und `E_CCPOAO_` zur Bestellseite des CCP; die Bedeutung der Kürzel ist aus den Namen erschlossen (abgeleitet). Die Kopie führt rund 200 verschiedene Fehler- und Warncodes.

Jede Operation nennt in der WSDL die für sie „relevanten Fehler“ und liefert sie als `…Exception` oder `deliveryRejection` zurück ([Q50](../../QUELLEN.md#q50), WSDL `po-oa-management`).

**Absender und Inhaber.** `E_POOAM_SENDER_NOT_ENTITLEMENT_OWNER` und `E_POOAM_SENDER_TO_ORDER_ID_MISMATCH` prüfen, dass nur der Inhaber bestellt und die Auftrags-ID zu ihm passt.

**Aufträge.** Doppelte Auftrags-ID, kollidierender Auftrag, abgelaufener Auftrag und unzulässige Parameter haben je einen eigenen Code. Für Auftragsgruppen müssen App-Instanz und Gruppen-ID für alle Aufträge gleich sein.

**Stornierung.** `E_POOAM_ORDER_ALREADY_EXECUTED` lehnt die Stornierung eines bereits ausgeführten Auftrags ab. `cancelOrder` wirkt also nur vor der Ausführung; das stützt die Lesart der [Aktionsfreigabe](../aktionsmanagement/aktionsfreigabe.md) als Rücknahme (abgeleitet).

**Listen.** Bei `E_CO_CYCLE_NUMBER_UNKNOWN_OR_TOO_OLD` und `E_CO_INCORRECT_CHECKSUM` soll der Abrufende die vollständige Liste anfordern.

Alle 38 betrachteten Codes stehen im Frontmatter. Die Warncodes `W_…` und die Bereiche EUI, HL, ION und andere sind nicht erfasst. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Stellen wir uns vor, der Bären-Verkehrsbund arbeitet nach etiCORE. Die Fehlercodes sind dann wie die Gründe auf einem Rückschein: kurz, immer gleich und für Menschen lesbar.

Bodo Bärlauch gibt für Pias ABO Azubi einen Auftrag auf. Aus Versehen schickt die BVB denselben Auftrag mit derselben Nummer ein zweites Mal. Der BVV antwortet nicht einfach „Fehler“, sondern mit `E_POOAM_DUPLICATE_ORDER_ID`: Die Nummer ist schon vergeben.

Später will Bodo den Auftrag stornieren, doch Pia hat ihre BärenKarte am Lesegerät im Hauptbahnhof schon aufgelegt, und der Auftrag ist ausgeführt. Jetzt kommt `E_POOAM_ORDER_ALREADY_EXECUTED`. Eine Stornierung hilft nicht mehr; es bliebe, die Berechtigung selbst zurückzunehmen.

Und das Hintergrundsystem der BVB holt regelmäßig nur die Änderungen der Aktionsliste. Passt dabei ein Prüfwert nicht, meldet der BVV `E_CO_INCORRECT_CHECKSUM`. Der Ausweg steht gleich dabei: einmal die vollständige Liste holen und von dort aus neu beginnen.

Der Vorteil für ein Werkzeug liegt auf der Hand: Es braucht keine Fehlertexte zu raten, es schlägt den Code nach.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: Aufzählungen `PoOaManagementErrorEnum` (`po-oa-management-event-enums_xsd`), `CommonErrorEnum` (`common-event-enums_xsd`), `PoErrorEnum` (`po-event-enums_xsd`), `CcpOaOrderingErrorEnum` (`ccp-oa-ordering-event-enums_xsd`); WSDL `po-oa-management` (Abschnitt „Relevant errors“) · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Aktionsmanagement in etiCORE](../aktionsmanagement/aktionsmanagement-in-eticore.md) – die Operationen, die diese Fehler liefern
- [Aktionsfreigabe](../aktionsmanagement/aktionsfreigabe.md) – Stornierung als Rücknahme
- [Nachrichten in KA 1.x und etiCORE](nachrichten-in-ka-1-x-und-eticore.md) – Altnamen

<!-- GEN:siehe_auch -->
## Siehe auch

- [Aktionsmanagement in etiCORE](../aktionsmanagement/aktionsmanagement-in-eticore.md)
- [Aktionsfreigabe](../aktionsmanagement/aktionsfreigabe.md)
- [Nachrichten in KA 1.x und etiCORE](nachrichten-in-ka-1-x-und-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
