---
titel: Zähler, Zeit und Versionen (ASN.1)
englisch: counters, time and versions in ASN.1
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/asn-1-typen-in-eticore.md, lexikon/berechtigungen/bersynchronnummer.md, lexikon/berechtigungen/statische-berechtigung-in-eticore.md]
quellen: [Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Zähler, Zeit und Versionen (ASN.1)
<!-- /GEN:breadcrumb -->

# Zähler, Zeit und Versionen (ASN.1)

Folgenummern, Zeitangaben und Versionen in `common` ([Q51](../../QUELLEN.md#q51)):

- `ActionCounter` (`0x4A`) ist eine Folgenummer, die um eins steigt, sooft ein SAM eine Aktion mit einem Nutzermedium autorisiert. `EntitlementIssuanceCounter` (`0x4B`) steigt bei jeder autorisierten Ausgabe einer (statischen) Berechtigung. Der `TransitionCounter` (Modul `user-medium`, `0x58`) zählt Statuswechsel einer Applikation oder Berechtigung.
- `UnixTime` (`0x02`) ist ein `INTEGER` und gilt als „Unix timestamp“. `IndividualisationTime` (`0x5F2D`) ist der Zeitpunkt, zu dem die Individualisierungsdaten geschrieben wurden.
- `ConfigurationVersion` (`0x5F2E`) ist die Version der Konfiguration, die die Applikation verwendet. `SpecVersion` (`0x82`) ist ein Text mit der Version der zugrunde liegenden Spezifikation. `AppVersion` (`0x61`) fasst zusammen: Anbieter der Applikation, Anbieterversion, `specVersion` und Version des Fähigkeitsprofils.
- `EnumMarker` (`0x02`) ist der gemeinsame Grundtyp aller ganzzahligen Aufzählungen.

Die drei Zähler zählen Verschiedenes und dürfen nicht verwechselt werden (abgeleitet). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Ein Kilometerzähler zählt, wie weit ein Auto gefahren ist. In etiCORE gibt es drei Zähler, die alle nur nach oben zählen und Verschiedenes festhalten.

Das SAM im Kontrollgerät der BVB zählt mit, wie oft es eine Aktion mit einer Karte autorisiert hat, den Aktionszähler. Dasselbe SAM zählt auch, wie oft es eine Berechtigung ausgegeben hat, den Ausgabezähler. Auf Pias Berechtigung selbst steht, wie oft sich ihr Status geändert hat, der Übergangszähler. Das ABO Azubi ist einmal ausgegeben, und wenn es gesperrt und wieder entsperrt würde, stünde dort zwei Wechsel mehr.

Zeitangaben sind schlichte Zahlen: Sekunden seit dem 1. Januar 1970. Die Individualisierungszeit sagt, wann die Daten auf Pias BärenKarte geschrieben wurden.

Versionen sind Text: Welche Fassung der Spezifikation verwendet der Anbieter der Karten-Applikation, und welche Konfiguration läuft darauf? Das hilft, wenn ein Gerät fragt, ob es eine Karte überhaupt lesen kann.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `common`: `ActionCounter`, `EntitlementIssuanceCounter`, `UnixTime`, `IndividualisationTime`, `ConfigurationVersion`, `SpecVersion`, `AppVersion`, `EnumMarker` · *Release-Kandidat*; Modul `user-medium`: `TransitionCounter`

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md) – Überblick
- [berSynchronNummer](../berechtigungen/bersynchronnummer.md) – der Vorgänger des Übergangszählers
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md)

<!-- GEN:siehe_auch -->
## Siehe auch

- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md)
- [berSynchronNummer](../berechtigungen/bersynchronnummer.md)
- [Statische Berechtigung in etiCORE](../berechtigungen/statische-berechtigung-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
