---
titel: Bescheinigungen zu Applikationen (ASN.1)
englisch: application attestations in ASN.1
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/bescheinigungen-zu-berechtigungen-asn-1.md, lexikon/berechtigungen/berstatus.md, lexikon/kontrolle/sperrung.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 5
    codeliste: AppStatusEnum
    bedeutung: "terminated — Terminated (cancelled in EN 1545-1:2015)"
    quelle: Q51
    fundstelle: Modul user-medium, Typ AppStatusEnum
    status: belegt
    verbundspezifisch: false
  - wert: 7
    codeliste: AppStatusEnum
    bedeutung: ok
    quelle: Q51
    fundstelle: Modul user-medium, Typ AppStatusEnum
    status: belegt
    verbundspezifisch: false
  - wert: 19
    codeliste: AppStatusEnum
    bedeutung: blocked — Blocked (but could be unblocked)
    quelle: Q51
    fundstelle: Modul user-medium, Typ AppStatusEnum
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F62"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: ApplicationBlockedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ ApplicationBlockedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F51"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: ApplicationUnblockedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ ApplicationUnblockedAttestation
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F61"
    codeliste: ASN.1-Tag (Bescheinigungen im Modul user-medium)
    bedeutung: ApplicationTerminatedAttestation
    quelle: Q51
    fundstelle: Modul user-medium, Typ ApplicationTerminatedAttestation
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Bescheinigungen zu Applikationen (ASN.1)
<!-- /GEN:breadcrumb -->

# Bescheinigungen zu Applikationen (ASN.1)

Auch für die **Applikation** auf dem Medium gibt es Bescheinigungen ([Q51](../../QUELLEN.md#q51), Modul `user-medium`): Sperrung (`ApplicationBlockedAttestation`, Tag `0x7F62`), Entsperrung (`…Unblocked…`, `0x7F51`) und Beendigung (`…Terminated…`, `0x7F61`).

Sie nennen die `appInstanceId` der Applikation, den Status **nach** der Aktion (`AppStatusCode`), den Wert des Übergangszählers nach der Aktion, `TerminalActionData`, `SamActionData` und optional die Daten der letzten SAM-Aktion der Applikation.

`AppStatusEnum` kennt drei Werte nach EN 1545-1:2015: **5** terminated, **7** ok und **19** blocked, hier erläutert als „blocked (but could be unblocked)“. Das sind dieselben Zahlen wie beim Status der Berechtigung ([Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md)).

Die zugehörigen Parameterstrukturen verwenden eine **Pseudo-Produkt-ID**: Als Organisation gilt die des Medien-Inhabers, Produkttyp und Produktnummer sind 0 ([Q51](../../QUELLEN.md#q51), `ApplicationBlockingParameters`). So lassen sich Aktionen an der Applikation wie Aktionen an einem Produkt autorisieren (abgeleitet). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Pias BärenKarte trägt eine Applikation, in der ihre Berechtigungen liegen. Verliert sie die Karte, sperrt Bodo Bärlauch nicht ein einzelnes Abo, sondern die ganze Applikation mit der Instanz 90000042.

Darüber entsteht eine eigene Bescheinigung. Sie nennt, welche Applikation gesperrt wurde, den neuen Status und den Zähler der Statuswechsel. Der Status ist 19: gesperrt, aber so, dass er sich wieder aufheben ließe. Fände Pia die Karte wieder, käme eine Entsperr-Bescheinigung mit Status 7. Gibt sie die Karte ab, wird die Applikation beendet, Status 5.

Warum hat die Sperre einer Applikation eine Produkt-Kennung, wo sie doch kein Produkt ist? Vermutlich, damit das System für Berechtigungen und Applikationen mit derselben Mechanik arbeiten kann. Die Kennung ist eine Platzhalterin: Als Organisation steht die des Karteninhabers, hier die BVB (9010), und als Produkt eine Null.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `ApplicationBlockedAttestation`, `ApplicationUnblockedAttestation`, `ApplicationTerminatedAttestation`, `ApplicationBlockingParameters` u. a., `AppStatusCode`, `AppStatusEnum` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Bescheinigungen zu Berechtigungen (ASN.1)](bescheinigungen-zu-berechtigungen-asn-1.md) – dieselbe Idee für Berechtigungen
- [berStatus](../berechtigungen/berstatus.md) – der Status in der KA 1.x
- [Sperrung](../kontrolle/sperrung.md) – der Vorgang
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Bescheinigungen zu Berechtigungen (ASN.1)](bescheinigungen-zu-berechtigungen-asn-1.md)
- [berStatus](../berechtigungen/berstatus.md)
- [Sperrung](../kontrolle/sperrung.md)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
