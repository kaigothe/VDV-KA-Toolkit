---
titel: Fehlercodes im ION
englisch: error codes in the ION
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/fehlercodes-eticore.md, lexikon/transaktionen/duplikaterkennung.md, lexikon/sicherheit/esh.md, lexikon/transaktionen/nachrichten-in-ka-1-x-und-eticore.md]
quellen: [Q50]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: "E_CRE_SERVICE_NOT_CONFIGURED"
    codeliste: CreErrorEnum
    bedeutung: "Der Dienst ist nicht eingerichtet: Der Aufrufer hat einen Dienstnamen gesendet, der im CRE nicht konfiguriert ist."
    quelle: Q50
    fundstelle: cre-event-enums_xsd, Aufzählung CreErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ESH_UNKNOWN_MEDIUM_ID"
    codeliste: EshErrorEnum
    bedeutung: Die Medium-ID lässt sich keiner App-Instanz-ID zuordnen.
    quelle: Q50
    fundstelle: esh-event-enums_xsd, Aufzählung EshErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_CRE_COULD_NOT_STORE_MESSAGE"
    codeliste: IonCommunicationErrorEnum
    bedeutung: Die Nachricht ließ sich nicht für die spätere Weiterleitung einreihen.
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_HEADER_TO_TLS_CERTIFICATE_MISMATCH"
    codeliste: IonCommunicationErrorEnum
    bedeutung: Die Absender-ID im SOAP-Header stimmt nicht mit der Absender-ID im TLS-Zertifikat überein.
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_INVALID_SOAP_HEADER"
    codeliste: IonCommunicationErrorEnum
    bedeutung: "Ungültige Nachricht: Absender-ID oder Routing-Angaben ließen sich dem SOAP-Header nicht entnehmen."
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_NO_TARGET_ADDRESS_FOUND_FOR_ROUTING_PARAMETERS"
    codeliste: IonCommunicationErrorEnum
    bedeutung: Zu den Routing-Angaben wurde keine Zieladresse gefunden.
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_RECEIVER_NOT_REACHABLE"
    codeliste: IonCommunicationErrorEnum
    bedeutung: Eine Verbindung zum Empfänger kam nicht zustande.
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_RECEIVER_RESPONSE_TIMEOUT"
    codeliste: IonCommunicationErrorEnum
    bedeutung: Der Empfänger antwortet nicht innerhalb der vorgegebenen Zeit.
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_UNKNOWN_OPERATION"
    codeliste: IonCommunicationErrorEnum
    bedeutung: Der Operationsname im ION-Nachrichtenkopf ist dem CRE unbekannt.
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_UNKNOWN_OR_UNAUTHORISED_RECEIVER"
    codeliste: IonCommunicationErrorEnum
    bedeutung: Die Organisations-ID des Empfängers ist deaktiviert oder unbekannt.
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_IONC_UNKNOWN_OR_UNAUTHORISED_SENDER"
    codeliste: IonCommunicationErrorEnum
    bedeutung: Die Organisations-ID des Absenders ist deaktiviert oder unbekannt.
    quelle: Q50
    fundstelle: ion-communication-event-enums_xsd, Aufzählung IonCommunicationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_DATA_OF_SOAP_HEADER_DOES_NOT_MATCH_MESSAGE_DATA"
    codeliste: IonErrorEnum
    bedeutung: Der SOAP-Header passt nicht zu den Daten der Nachricht.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_DUPLICATE_ION_MESSAGE_ID"
    codeliste: IonErrorEnum
    bedeutung: Eine Nachricht mit derselben ION-Nachrichten-ID ist bereits eingegangen.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_DUPLICATE_RESPONSE"
    codeliste: IonErrorEnum
    bedeutung: Die ursprüngliche Anfrage hat bereits eine zugeordnete Antwort.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_OPERATION_NOT_IMPLEMENTED"
    codeliste: IonErrorEnum
    bedeutung: Die vom Absender genannte Operation ist beim Empfänger nicht umgesetzt.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_ORIGINAL_REQUEST_NOT_FOUND"
    codeliste: IonErrorEnum
    bedeutung: Die Antwort verweist auf eine ursprüngliche Anfrage, die es nicht gibt.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_RECEIVER_ORGANISATION_MISMATCH"
    codeliste: IonErrorEnum
    bedeutung: Die Organisations-ID des Empfängers in der Anfrage stimmt nicht mit der des tatsächlichen Empfängers überein.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_RECEIVER_ROLE_MISMATCH"
    codeliste: IonErrorEnum
    bedeutung: Die Rollen-ID des Empfängers in der Anfrage stimmt nicht mit der des tatsächlichen Empfängers überein.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_RECEIVER_SERVICE_MISMATCH"
    codeliste: IonErrorEnum
    bedeutung: Der Dienstname des Empfängers in der Anfrage stimmt nicht mit dem des tatsächlichen Empfängers überein.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_SAME_MESSAGE_IN_PROGRESS"
    codeliste: IonErrorEnum
    bedeutung: Eine identische Nachricht wird gerade verarbeitet, zum Beispiel wenn mehrere gleiche Nachrichten im CRE gespeichert waren und nun fast gleichzeitig zugestellt werden.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_UNKNOWN_SENDER"
    codeliste: IonErrorEnum
    bedeutung: Zu prüfen ist, ob die Organisations-ID in der Organisationsliste des Scheme Managers steht.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_UNKNOWN_TECHNICAL_PROBLEM"
    codeliste: IonErrorEnum
    bedeutung: Unbekanntes technisches Problem.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_WRONG_SENDER_ROLE"
    codeliste: IonErrorEnum
    bedeutung: Falsche Rolle des Absenders.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ION_WRONG_SENDER_SERVICE"
    codeliste: IonErrorEnum
    bedeutung: Falscher Dienst des Absenders.
    quelle: Q50
    fundstelle: ion-event-enums_xsd, Aufzählung IonErrorEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Fehlercodes im ION
<!-- /GEN:breadcrumb -->

# Fehlercodes im ION

Beim Übermitteln einer Nachricht im ION melden 24 Codes Fehler ([Q50](../../QUELLEN.md#q50), `ion-event-enums_xsd`, `ion-communication-event-enums_xsd`, `cre-event-enums_xsd`, `esh-event-enums_xsd`). Die Kürzel stehen für das Netz (`E_ION_`), die Kommunikation mit der CRE (`E_IONC_`), die CRE selbst (`E_CRE_`) und den ESH (`E_ESH_`); das ist aus den Namen erschlossen (abgeleitet).

- **Adressierung:** Organisation, Rolle oder Dienst des Empfängers stimmen nicht mit dem tatsächlichen Empfänger überein; falsche Rolle oder falscher Dienst des Absenders; unbekannter Absender; der SOAP-Header passt nicht zu den Daten.
- **Routing in der CRE:** keine Zieladresse, Empfänger nicht erreichbar, Zeitüberschreitung bei der Antwort, unbekannte Operation, unbekannter oder nicht berechtigter Absender oder Empfänger, nicht eingerichteter Dienst, Nachricht nicht einreihbar. `E_IONC_HEADER_TO_TLS_CERTIFICATE_MISMATCH` meldet, dass die Absender-ID im Header nicht zu der im TLS-Zertifikat passt.
- **Duplikate und Zuordnung:** doppelte ION-Nachrichten-ID, identische Nachricht in Bearbeitung, doppelte Antwort, Antwort auf eine unbekannte Anfrage.
- **ESH:** `E_ESH_UNKNOWN_MEDIUM_ID`, wenn sich eine Medium-ID keiner App-Instanz zuordnen lässt.

Die Prüfung auf doppelte ION-Nachrichten-IDs erinnert an die [Duplikaterkennung](duplikaterkennung.md) der KA 1.x; ob beide gleich arbeiten, nennt die Quelle nicht. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Die BVB schickt dem Bären-Verkehrsbund eine Bestellung. Der Weg führt über die zentrale Vermittlungsstelle, die CRE. Sie liest vorn auf dem Umschlag, an wen die Nachricht gehen soll, und stellt zu.

Hat sich beim Adressieren ein Fehler eingeschlichen, etwa ein falscher Dienstname, merkt es der Empfänger: `E_ION_RECEIVER_SERVICE_MISMATCH`. Dann stimmt der Umschlag nicht mit dem Haus überein, in dem er ankam.

Ist der BVV für den Moment nicht zu erreichen, meldet die CRE `E_IONC_RECEIVER_NOT_REACHABLE`. Antwortet er, aber zu spät, ist es `E_IONC_RECEIVER_RESPONSE_TIMEOUT`.

Manchmal liegt dieselbe Nachricht zweimal im Briefkasten der CRE und wird fast gleichzeitig zugestellt. Dann sagt der BVV beim zweiten Exemplar `E_ION_SAME_MESSAGE_IN_PROGRESS`: Das habe ich schon in Arbeit. Kommt sie später noch einmal, wäre es `E_ION_DUPLICATE_ION_MESSAGE_ID`.

Und für das Vertrauen sorgt das TLS-Zertifikat: Behauptet der Umschlag, von der BVB zu kommen, das Zertifikat aber, von jemand anderem, wird die Nachricht mit `E_IONC_HEADER_TO_TLS_CERTIFICATE_MISMATCH` abgewiesen.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `ion-event-enums_xsd`, `ion-communication-event-enums_xsd`, `cre-event-enums_xsd`, `esh-event-enums_xsd`: Aufzählungen `IonErrorEnum`, `IonCommunicationErrorEnum`, `CreErrorEnum`, `EshErrorEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Fehlercodes (etiCORE)](fehlercodes-eticore.md) – die Codes der Aktionsverwaltung
- [Duplikaterkennung](duplikaterkennung.md) – die Duplikatprüfung der KA 1.x
- [ESH](../sicherheit/esh.md) – der Hub, dessen Fehler hier auftaucht
- [Nachrichten in KA 1.x und etiCORE](nachrichten-in-ka-1-x-und-eticore.md) – Altnamen

<!-- GEN:siehe_auch -->
## Siehe auch

- [Fehlercodes (etiCORE)](fehlercodes-eticore.md)
- [Duplikaterkennung](duplikaterkennung.md)
- [ESH](../sicherheit/esh.md)
- [Nachrichten in KA 1.x und etiCORE](nachrichten-in-ka-1-x-und-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
