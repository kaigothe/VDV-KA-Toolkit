---
titel: Fehlercodes der Terminalanteile
englisch: error codes of the terminal components
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/fehlercodes-eticore.md, lexikon/rollen/rollennamen-in-eticore.md, lexikon/rollen/akzeptanzterminal.md, lexikon/sicherheit/sam-datenobjekte-asn-1.md]
quellen: [Q50]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: "E_ESI_EU_ERROR_UM_UNCHANGED"
    codeliste: EsiErrorEnum
    bedeutung: Fehler bei der Zusammenarbeit mit der Ausführungseinheit, bevor das Medium verändert wurde.
    quelle: Q50
    fundstelle: esi-event-enums_xsd, Aufzählung EsiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ESI_EXECUTION_INCOMPLETE"
    codeliste: EsiErrorEnum
    bedeutung: Die Ausführung der Ausgabe oder Beendigung ist unvollständig.
    quelle: Q50
    fundstelle: esi-event-enums_xsd, Aufzählung EsiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ESI_ILLEGAL_ISSUANCE_INFORMATION"
    codeliste: EsiErrorEnum
    bedeutung: Das aktuelle Nutzermedium gehört nicht zur angegebenen Referenznummer.
    quelle: Q50
    fundstelle: esi-event-enums_xsd, Aufzählung EsiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ESI_UNKNOWN_PRODUCT_CONFIGURATION"
    codeliste: EsiErrorEnum
    bedeutung: Die referenzierte Produktkonfiguration ist unbekannt.
    quelle: Q50
    fundstelle: esi-event-enums_xsd, Aufzählung EsiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ESI_UNKNOWN_READER_ID"
    codeliste: EsiErrorEnum
    bedeutung: Die referenzierte Leser-ID ist unbekannt.
    quelle: Q50
    fundstelle: esi-event-enums_xsd, Aufzählung EsiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ESI_UNKNOWN_REFERENCE_NUMBER"
    codeliste: EsiErrorEnum
    bedeutung: Die Referenznummer ist unbekannt.
    quelle: Q50
    fundstelle: esi-event-enums_xsd, Aufzählung EsiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_ESI_WRONG_UM_FOR_REFERENCE_NUMBER"
    codeliste: EsiErrorEnum
    bedeutung: Das aktuelle Nutzermedium gehört nicht zur angegebenen Referenznummer.
    quelle: Q50
    fundstelle: esi-event-enums_xsd, Aufzählung EsiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_ACTION_AMOUNT_DISALLOWED"
    codeliste: EuiErrorEnum
    bedeutung: Ein Aktionsbetrag ist gesetzt, für diesen Produkttyp aber nicht zulässig.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_ACTION_AMOUNT_MISSING"
    codeliste: EuiErrorEnum
    bedeutung: Der Aktionsbetrag fehlt, obwohl er für diesen Produkttyp verlangt ist.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_ACTIVATION_FAILED"
    codeliste: EuiErrorEnum
    bedeutung: Die Signaturprüfung und damit die Aktivierung des SAM ist fehlgeschlagen.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_ALL_SUITABLE_SAMS_BUSY"
    codeliste: EuiErrorEnum
    bedeutung: Alle SAMs, die den Auswahlkriterien entsprechen, sind gerade belegt; ein späterer Versuch kann gelingen.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_APPLICATION_STATUS_PREVENTS_OPERATION_EXECUTION"
    codeliste: EuiErrorEnum
    bedeutung: Der Status der Applikation verhindert die Operation, etwa kann an eine gesperrte Applikation keine Berechtigung ausgegeben werden.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_BALANCE_CONSTRAINTS_VIOLATED"
    codeliste: EuiErrorEnum
    bedeutung: Der angegebene Aktionsbetrag würde die Grenzen des Guthabens verletzen.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_CANNOT_SELECT_UM_APPLICATION"
    codeliste: EuiErrorEnum
    bedeutung: Die etiCORE-Applikation des Mediums lässt sich nicht auswählen.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_CERTIFICATE_VALIDATION_FAILED"
    codeliste: EuiErrorEnum
    bedeutung: Das Zertifikat ließ sich nicht prüfen.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_CONFIGURATION_EXECUTION_FAILED"
    codeliste: EuiErrorEnum
    bedeutung: Die Ausführung des Konfigurationsskripts für die Applikation des Mediums ist fehlgeschlagen.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_CONFIGURATION_RETRIEVAL_FAILED"
    codeliste: EuiErrorEnum
    bedeutung: Das Konfigurationsskript ließ sich nicht abrufen, etwa weil der ESH mit einem Fehler antwortet oder nicht erreichbar ist.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_DATA_OBJECT_NOT_FOUND"
    codeliste: EuiErrorEnum
    bedeutung: Das zu lesende oder zu löschende Datenobjekt wurde nicht gefunden.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_ENTITLEMENT_NOT_FOUND"
    codeliste: EuiErrorEnum
    bedeutung: Im Medium gibt es keine Berechtigung mit der angegebenen Eintrags-ID.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_ENTITLEMENT_STATUS_PREVENTS_OPERATION_EXECUTION"
    codeliste: EuiErrorEnum
    bedeutung: Der Status der Berechtigung verhindert die Operation, etwa kann eine beendete Berechtigung nicht gesperrt werden.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_ERROR_WHILE_PRINTING"
    codeliste: EuiErrorEnum
    bedeutung: Fehler beim Drucken.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_ILLEGAL_PRODUCT_ID"
    codeliste: EuiErrorEnum
    bedeutung: Die Produkt-ID darf nur bei Check-in/Check-out mit interoperablen Produkten gesetzt sein und muss denselben Produkttyp wie die ursprüngliche Produkt-ID tragen.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_INVALID_ENTRY_ID"
    codeliste: EuiErrorEnum
    bedeutung: Die angegebene Eintrags-ID ist ungültig.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_MISSING_OR_INVALID_SESSION"
    codeliste: EuiErrorEnum
    bedeutung: "Eine gültige Sitzung ist nötig: Es wurde keine Sitzungs-ID angegeben, oder sie ist ungültig."
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_NO_CHECKIN_FOUND"
    codeliste: EuiErrorEnum
    bedeutung: Die letzte Mobilitäts-Bescheinigung müsste eine Check-in-Bescheinigung enthalten, tut es aber nicht oder ist nicht auffindbar.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_NO_ENTRY_ID_AVAILABLE"
    codeliste: EuiErrorEnum
    bedeutung: Es ist keine Eintrags-ID mehr frei, auf der die Berechtigung ausgegeben werden könnte.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_NO_PRINTER_AVAILABLE"
    codeliste: EuiErrorEnum
    bedeutung: Es ist kein Drucker verfügbar.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_NO_SIGNATURE_ALGORITHM_MATCHES"
    codeliste: EuiErrorEnum
    bedeutung: Es gibt kein Signaturverfahren, das SAM und Kontrolleinheit unterstützen und die Subject-Authorisation erlaubt.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_NO_SUITABLE_SAM_AVAILABLE"
    codeliste: EuiErrorEnum
    bedeutung: Es ist kein SAM verfügbar, das den Auswahlkriterien entspricht.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_NO_UM_FOUND"
    codeliste: EuiErrorEnum
    bedeutung: Es wurde kein Nutzermedium gefunden, obwohl die Einheit die eingestellte Zeit gewartet hat.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_PASSWORD_BLOCKED_OR_NOT_CONFIGURED"
    codeliste: EuiErrorEnum
    bedeutung: Die Authentisierungsdaten sind nicht gesetzt, oder der Kennwortzustand ist gesperrt.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_PRINTER_TIMED_OUT"
    codeliste: EuiErrorEnum
    bedeutung: Zeitüberschreitung beim Drucker.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_SAM_NOT_ACTIVATED"
    codeliste: EuiErrorEnum
    bedeutung: Das SAM ist nicht aktiviert.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_SECURITY_ERROR"
    codeliste: EuiErrorEnum
    bedeutung: Ein sicherheitsrelevanter Fehler ist aufgetreten, etwa antwortet SAM oder Medium auf einen Befehl mit „SM data objects incorrect“ (SW = 0x6988) und die gesicherte Sitzung wurde zurückgesetzt. Der Fehler tritt auch auf, wenn zwischen SAM und Medium keine gesicherte Sitzung zustande kommt.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_UNIT_BUSY"
    codeliste: EuiErrorEnum
    bedeutung: Die Ausführungseinheit ist mit anderen Sitzungen beschäftigt.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_WRONG_OPERATION_ORDER"
    codeliste: EuiErrorEnum
    bedeutung: Die Reihenfolge der Operationen ist falsch; Voraussetzungen sind womöglich nicht erfüllt.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_WRONG_PASSWORD"
    codeliste: EuiErrorEnum
    bedeutung: Die Autorisierung mit dem angegebenen Kennwort war nicht erfolgreich.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_WRONG_PRODUCT_TYPE_FOR_ACTION"
    codeliste: EuiErrorEnum
    bedeutung: Der Produkttyp der referenzierten Berechtigung verhindert die Operation, etwa kann ein Guthaben-Zahlungsmittel nicht entwertet werden.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_EUI_WRONG_SAM_ACTIVATION_RIGHTS"
    codeliste: EuiErrorEnum
    bedeutung: Das SAM lässt sich mit der angegebenen Subject-Authorisation nicht aktivieren.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_COMMUNICATION_HEADERS_MISSING"
    codeliste: PersonalisationErrorEnum
    bedeutung: Kommunikationsköpfe fehlen.
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_DATA_CONVERSION_ERROR"
    codeliste: PersonalisationErrorEnum
    bedeutung: Fehler bei der Umwandlung von Daten.
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_INVALID_NEW_PASSWORD"
    codeliste: PersonalisationErrorEnum
    bedeutung: Das neue Kennwort verletzt die Vorgaben der Kennwortparameter (zu kurz oder zu lang).
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_INVALID_PARAMETERS"
    codeliste: PersonalisationErrorEnum
    bedeutung: Die Parameter für Medium oder SAM sind falsch und lassen sich für die Operation nicht verwenden.
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_INVALID_PASSWORD_CONFIGURATION"
    codeliste: PersonalisationErrorEnum
    bedeutung: Die Authentisierungsdaten verletzen technische Bedingungen, etwa eine größte Kennwortlänge unter der kleinsten.
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_MESSAGE_UNRECOVERABLE"
    codeliste: PersonalisationErrorEnum
    bedeutung: Die referenzierte Nachricht ist per ID bekannt, aber nicht wiederherstellbar.
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_MISSING_PRODUCT_ISSUANCE_RIGHTS"
    codeliste: PersonalisationErrorEnum
    bedeutung: Dem SAM fehlen die für diese Operation nötigen Rechte zur Produktausgabe.
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_MISSING_REQUIRED_FILE"
    codeliste: PersonalisationErrorEnum
    bedeutung: Eine benötigte Datei fehlt, etwa eine referenzierte Layoutvorlage.
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "E_PE_OPERATION_NOT_SUPPORTED"
    codeliste: PersonalisationErrorEnum
    bedeutung: Operation nicht unterstützt.
    quelle: Q50
    fundstelle: personalisation-event-enums_xsd, Aufzählung PersonalisationErrorEnum
    status: belegt
    verbundspezifisch: false
  - wert: "W_EUI_ENTITLEMENT_TERMINATED_BUT_NOT_DELETED"
    codeliste: EuiWarningEnum
    bedeutung: Zum Löschen einer Berechtigung muss das SAM aktiviert sein; ist es das nicht, kann die Ausführungseinheit den Löschteil der Beendigung nicht ausführen.
    quelle: Q50
    fundstelle: eui-event-enums_xsd, Aufzählung EuiWarningEnum
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Fehlercodes der Terminalanteile
<!-- /GEN:breadcrumb -->

# Fehlercodes der Terminalanteile

Die Terminalanteile melden 49 Codes ([Q50](../../QUELLEN.md#q50)). Die Kürzel stehen für die Ausführungseinheit (EUI, `EuiErrorEnum`, `EuiWarningEnum`), die Personalisierung (PE, `PersonalisationErrorEnum`) und die Schnittstelle zu Fremdsystemen (ESI, `EsiErrorEnum`); das ist aus den Namen und aus [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md) erschlossen (abgeleitet).

Die 32 `E_EUI_`-Fehler lassen sich ordnen:
- **SAM:** nicht aktiviert, Aktivierung gescheitert, falsche Aktivierungsrechte, kein passendes oder nur belegte SAMs, kein gemeinsames Signaturverfahren.
- **Medium und Berechtigung:** kein Medium gefunden, Applikation nicht auswählbar, Berechtigung oder Eintrag nicht gefunden, keine freie Eintrags-ID.
- **Status und Produkt:** Status von Applikation oder Berechtigung verhindert die Operation, falscher Produkttyp, fehlender oder unzulässiger Aktionsbetrag, verletzte Guthabengrenzen.
- **Sicherheit:** Sicherheitsfehler (etwa „SM data objects incorrect“, SW = `0x6988`), Zertifikat nicht prüfbar, falsches oder gesperrtes Kennwort.
- **Betrieb:** keine oder abgelaufene Sitzung, Einheit belegt, falsche Reihenfolge, Konfiguration nicht abrufbar oder nicht ausführbar, Druckerfehler.

`E_PE_…` betrifft ungültige Parameter, Kennwortvorgaben, fehlende Ausgaberechte des SAM und fehlende Dateien; `E_ESI_…` unbekannte Leser, Referenznummern und Produktkonfigurationen. Zwei ESI-Codes tragen in der Quelle denselben Text. `W_EUI_…` warnt, dass eine beendete Berechtigung nicht gelöscht werden kann, wenn das SAM nicht aktiviert ist. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Pia hält ihre BärenKarte an das Lesegerät T-4712 am Hauptbahnhof, das eine Berechtigung ausführen soll. Zwischen Karte und Gerät arbeitet eine Ausführungseinheit, die vieles prüft und bei jedem Hindernis einen eigenen Code liefert.

Ist Pias Applikation gesperrt, kommt `E_EUI_APPLICATION_STATUS_PREVENTS_OPERATION_EXECUTION`: Auf eine gesperrte Applikation lässt sich nichts ausgeben. Ist das SAM des Geräts nicht aktiviert, meldet die Einheit `E_EUI_SAM_NOT_ACTIVATED`. Wird innerhalb der eingestellten Wartezeit keine Karte aufgelegt, heißt es `E_EUI_NO_UM_FOUND`.

Hat jemand ein Kennwort auf der Karte eingerichtet und wird es mehrfach falsch eingegeben, ist es irgendwann gesperrt: `E_EUI_PASSWORD_BLOCKED_OR_NOT_CONFIGURED`.

Am Automaten gibt es dazu noch Fehler, die jeder kennt: `E_EUI_NO_PRINTER_AVAILABLE`, wenn das Papier alle ist, oder `E_EUI_PRINTER_TIMED_OUT`, wenn der Drucker nicht antwortet.

Alle diese Codes sagen nicht, wer schuld ist, sondern wo es hakt. Das ist für die Fehlersuche der halbe Weg.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `eui-event-enums_xsd`, `personalisation-event-enums_xsd`, `esi-event-enums_xsd`: Aufzählungen `EuiErrorEnum`, `EuiWarningEnum`, `PersonalisationErrorEnum`, `EsiErrorEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Fehlercodes (etiCORE)](fehlercodes-eticore.md) – die Codes der Aktionsverwaltung
- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md) – Execution Unit, EUI, ESI
- [Akzeptanzterminal](../rollen/akzeptanzterminal.md) – das Gerät
- [SAM-Datenobjekte (ASN.1)](../sicherheit/sam-datenobjekte-asn-1.md) – Rechte und Schlüssel des SAM

<!-- GEN:siehe_auch -->
## Siehe auch

- [Fehlercodes (etiCORE)](fehlercodes-eticore.md)
- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md)
- [Akzeptanzterminal](../rollen/akzeptanzterminal.md) (AKT)
- [SAM-Datenobjekte (ASN.1)](../sicherheit/sam-datenobjekte-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
