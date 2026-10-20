---
titel: Hotlist Service
englisch: hotlist service
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/rollen/kose.md, lexikon/kontrolle/sperrliste.md, lexikon/rollen/rollennamen-in-eticore.md, lexikon/transaktionen/nachrichten-in-ka-1-x-und-eticore.md]
quellen: [Q06, Q49, Q50]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Hotlist Service
<!-- /GEN:breadcrumb -->

# Hotlist Service

Der Hotlist Service ist in [etiCORE](../grundlagen/eticore.md) der zentrale Dienst, der die Aufgaben des [KOSE](../rollen/kose.md) übernimmt: Er führt die Hotlist und stellt sie bereit ([Q49](../../QUELLEN.md#q49), Glossar). Dafür sprechen die Altbezeichner seiner Operationen im Namensraum `http://vdv/ka/kose/2` und derselbe Rollencode 5 ([Q50](../../QUELLEN.md#q50), `hotlist-messaging_xsd`, WSDL `hotlist`; für den KOSE [Q06](../../QUELLEN.md#q06), Kap. 4.10).

**Gegenstände.** Die Hotlist führt Einträge für Applikationsinstanzen, auch von MOTICS-Apps, für Berechtigungen auf dem Medium und statische, für SAMs, symmetrische Authentifizierungsschlüssel und Organisationen ([Q50](../../QUELLEN.md#q50)).

**Wer darf was.** Kundenvertragspartner tragen Applikationen und Berechtigungen ein und nehmen sie wieder heraus (`addApplicationToHotlist`, `addEntitlementToHotlist`, `remove…`). Schlüssel und Organisationen sind „only provided for the scheme manager“, also dem ESH vorbehalten. SAMs tragen Dienstleister, ESH und CCP ein; entfernen kann sie nur der ESH ([Q50](../../QUELLEN.md#q50), WSDL `hotlist`).

**Abruf.** Es gibt vollständige und inkrementelle Listen (`getApplicationHotlist`, `getIncrementalEntitlementHotlist` u. a.). Berechtigungslisten enthalten nur „the products accepted by the caller“; wer welche Produkte akzeptiert, richtet der Product Owner am Hotlist Service ein (`addProductAcceptanceConfiguration`). `getEntitlementWithProductHotlist` liefert zusätzlich Produktangaben, sortiert nach Product Owner ([Q50](../../QUELLEN.md#q50)).

Die Angaben stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Pia hat ihre BärenKarte verloren. Bodo Bärlauch im Kundencenter am Honigmarkt sperrt die Applikationsinstanz 90000042. Stellen wir uns vor, der Bären-Verkehrsbund arbeitet nach etiCORE: Dann ruft die BVB als CCP beim Hotlist Service `addApplicationToHotlist` auf. Der Eintrag ist jetzt für alle sichtbar, die die Hotlist abrufen.

Petra Pranke prüft in der Linie 4 mit dem Kontrollgerät T-4713. Es muss nicht jedes Mal die ganze Liste laden, sondern fragt nach dem, was seit dem letzten Mal neu ist: die inkrementelle Liste. So erfährt es von Pias gesperrter Karte, ohne jeden Eintrag erneut zu holen.

Etwas Besonderes ist die Rolle der Produkte. Die Liste der Berechtigungen enthält nur Produkte, die der Abrufende akzeptiert. Nehmen wir an, der Luchs-Verkehrsverbund erlaubt der BVB, seine Luchs-Monatskarte zu akzeptieren. Dann richtet er das beim Hotlist Service ein, und die BVB bekommt auch Sperren zu diesem Produkt. Ohne diese Einrichtung blieben sie ihr verborgen. Ein Kontrollgerät sieht also nicht automatisch alles Gesperrte, sondern das, wofür sein Betreiber freigeschaltet ist.

Schlüssel und ganze Organisationen kann Bodo nicht sperren. Dafür ist nur die übergeordnete Stelle zuständig, in etiCORE der ESH.

## Quellen

- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: WSDL `hotlist` (Operationen, Aufrufer, Rolle 5), `hotlist-messaging_xsd` (Beschreibungen, `meta:old`) · *Release-Kandidat*
- [Q49](../../QUELLEN.md#q49) – etiCORE Specification, Glossar, Einträge *Hotlist* und *Hotlist Service*
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.10 (Rollencode 5 für den KOSE) · *verbundspezifisch*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Kontroll- und Sperrlistenservice](../rollen/kose.md) – die Rolle in der KA 1.x
- [Sperrliste](sperrliste.md) – die Liste selbst
- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md) – KOSE heißt jetzt Hotlist Service
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md) – Altnamen der Hotlist-Aufträge

<!-- GEN:siehe_auch -->
## Siehe auch

- [Kontroll- und Sperrlistenservice](../rollen/kose.md) (KOSE)
- [Sperrliste](sperrliste.md)
- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md)
- [Nachrichten in KA 1.x und etiCORE](../transaktionen/nachrichten-in-ka-1-x-und-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
