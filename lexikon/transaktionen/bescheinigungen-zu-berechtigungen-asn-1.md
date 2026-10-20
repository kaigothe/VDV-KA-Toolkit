---
titel: Bescheinigungen zu Berechtigungen (ASN.1)
englisch: entitlement attestations in ASN.1
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/nachweis.md, lexikon/berechtigungen/statische-berechtigung-in-eticore.md, lexikon/transaktionen/bescheinigungen-zu-applikationen-asn-1.md, lexikon/datenformate/zaehler-zeit-und-versionen-asn-1.md]
quellen: [Q50, Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: "0x7F50"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: EntitlementIssuedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementIssuedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F59"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: EntitlementBlockedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementBlockedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F52"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: EntitlementUnblockedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementUnblockedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F58"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: EntitlementTerminatedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementTerminatedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F5A"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: EntitlementInspectedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementInspectedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F5B"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: EntitlementValidatedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementValidatedAttestation
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Bescheinigungen zu Berechtigungen (ASN.1)
<!-- /GEN:breadcrumb -->

# Bescheinigungen zu Berechtigungen (ASN.1)

Eine **Bescheinigung** (`Attestation`) hält fest, dass eine Aktion mit einer Berechtigung ausgeführt wurde. Das Medium signiert sie ([Q50](../../QUELLEN.md#q50), Fehlercode `E_CO_DUPLICATE_UM_ATTESTATION`). Das Modul `user-medium` ([Q51](../../QUELLEN.md#q51)) kennt sechs davon:

| Bescheinigung | Tag |
|---|---|
| Ausgabe (`EntitlementIssuedAttestation`) | `0x7F50` |
| Sperrung (`…Blocked…`) | `0x7F59` |
| Entsperrung (`…Unblocked…`) | `0x7F52` |
| Beendigung (`…Terminated…`) | `0x7F58` |
| Prüfung (`…Inspected…`) | `0x7F5A` |
| Entwertung (`…Validated…`) | `0x7F5B` |

Alle nennen Produkt-ID, Berechtigungs-ID, den Status **nach** der Aktion und die Werte von Übergangs- und Aktionszähler nach der Aktion. Hinzu kommen optional der Kontostand bei Guthaben-Zahlungsmitteln, tarifliche Parameter, `TerminalActionData` (Betreiber, Terminal, Zeitpunkt, Ort), `SamActionData` und die Daten der letzten SAM-Aktion. Die Ausgabe nennt zusätzlich Ausgabezähler, Auftragsnummer, Gültigkeit, Produktparameter und Infotext; die Entwertung kann Check-in-Parameter tragen.

Zu jeder Aktion gehört eine Parameterstruktur, die die Autorisierung anstößt (`…Parameters`). Beim Zusammenspiel mit dem SAM wird nur deren Wertteil verwendet. Der Aufbau erinnert an die Nachweise der KA 1.x ([Nachweis](nachweis.md)); eine Zuordnung nennt die Quelle nicht (abgeleitet). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Wenn Pias ABO Azubi ausgegeben wird, entsteht ein Beleg, wie der Kassenzettel nach dem Einkauf. Das ist die Ausgabe-Bescheinigung. Auf ihr steht, was ausgegeben wurde: Produkt, Berechtigungs-ID, Beginn und Ende der Gültigkeit, die Auftragsnummer des Auftrags, dem die Ausgabe folgte, und der Status, vermutlich „in Ordnung“.

Wird die Karte später gesperrt, entsteht eine Sperr-Bescheinigung. Sie ist kürzer: Dieselbe Berechtigung, jetzt mit dem Status „gesperrt“, und die beiden Zähler, die sich verändert haben. Der Übergangszähler ist eins höher, weil der Status gewechselt hat. Der Aktionszähler ist ebenfalls höher, weil eine Aktion ausgeführt wurde.

Jede Bescheinigung trägt auch auf, wer sie wo und wann ausgestellt hat: der Betreiber, das Terminal, der Zeitpunkt, der Ort. Hätte Petra Pranke Pias Karte mit T-4713 geprüft, stünde das Terminal und die Uhrzeit auf der Prüf-Bescheinigung.

So ist jede Bescheinigung für sich lesbar, auch weit weg von dem Ort, an dem sie entstand.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `EntitlementIssuedAttestation`, `…BlockedAttestation`, `…UnblockedAttestation`, `…TerminatedAttestation`, `…InspectedAttestation`, `…ValidatedAttestation` und die zugehörigen `…Parameters`, `TerminalActionData`, `LastSAMActionData` · *Release-Kandidat*
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6, `common-event-enums_xsd`: Fehlercode `E_CO_DUPLICATE_UM_ATTESTATION`

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Nachweis](nachweis.md) – die Nachweise der KA 1.x
- [Bescheinigungen zu Applikationen (ASN.1)](bescheinigungen-zu-applikationen-asn-1.md) – dieselbe Idee für die Applikation
- [Zähler, Zeit und Versionen (ASN.1)](../datenformate/zaehler-zeit-und-versionen-asn-1.md) – Übergangs- und Aktionszähler
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Nachweis](nachweis.md)
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md)
- [Bescheinigungen zu Applikationen (ASN.1)](bescheinigungen-zu-applikationen-asn-1.md)
- [Zähler, Zeit und Versionen (ASN.1)](../datenformate/zaehler-zeit-und-versionen-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
