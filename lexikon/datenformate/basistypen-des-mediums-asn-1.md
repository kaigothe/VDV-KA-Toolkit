---
titel: Basistypen des Mediums (ASN.1)
englisch: basic types of the user medium in ASN.1
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/zaehler-zeit-und-versionen-asn-1.md, lexikon/berechtigungen/gueltigkeit.md, lexikon/medien/verzeichnisse-auf-dem-medium-asn-1.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › Basistypen des Mediums (ASN.1)
<!-- /GEN:breadcrumb -->

# Basistypen des Mediums (ASN.1)

Viele Typen im Modul `user-medium` ([Q51](../../QUELLEN.md#q51)) sind einfache Hüllen um Grundtypen.

- Zeitangaben: `EffectiveTime` (`0x51`) und `ExpirationTime` (`0x55`) sind Unix-Zeiten für Beginn und Ende der Gültigkeit einer Sache. `EntitlementEffectiveTime`, `EntitlementExpirationTime`, `DiscountEffectiveTime` und `DiscountExpirationTime` setzen sie fort. `ApplicationEffectiveTime` und `ApplicationExpirationTime` hängen dagegen am Zertifikat-Typ und tragen dessen Tags `0x5F25` und `0x5F24`.
- Zahlen: `NonNegativeInteger` und `PositiveInteger` (beide Tag `0x02`) schränken `INTEGER` auf Werte ab null beziehungsweise ab eins ein. `OrderNumber` (`0x5A`) ist die Auftragsnummer, die der CCP beim Kauf vergibt, wenn die Berechtigung über eine Aktionsliste ausgegeben wird.
- Zustand: `Status` (`0x57`) ist der Grundtyp der Statusangaben, `EntitlementStatusCode` und `AppStatusCode` setzen ihn fort. `TransitionCounter` (`0x58`) zählt Statuswechsel.
- Text und Verweise: `Infotext` (`0x43`) ist ein `UTF8String`. `EntryId` (`0x93`) ist die Kennung der Datengruppe im Verzeichnis. `LastSAMActionData` (`0x7B`) trägt das `SamActionData` der letzten erfolgreichen Aktion.

Dieselbe Tag-Nummer bezeichnet je nach Umgebung Verschiedenes. Das gilt hier etwa für `0x02`, das alle Aufzählungs-Markierungen und Zahlentypen verwenden. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Ein Formular besteht nicht nur aus großen Kästchen. Es hat auch die kleinen Kästchen: ein Datumsfeld, ein Feld „nur Zahlen ab null“, ein Feld für einen Freitext.

Bei Pias ABO Azubi stehen Beginn und Ende der Gültigkeit in solchen Datumsfeldern, und zwar als Sekundenzähler seit 1970, den jeder Rechner leicht vergleichen kann. Der Hinweistext „ABO Azubi“ steht im Textfeld. Die Auftragsnummer, die die BVB beim Auftrag vergeben hat, steht im Zahlenfeld.

Zu den Eigenheiten gehört, dass die Gültigkeit der Applikation (also der ganzen Karte) und die Gültigkeit eines Zertifikats dasselbe Etikett tragen: Beide sind „Beginn“ und „Ende“, nur gehören sie zu verschiedenen Dingen. Das Gerät erkennt sie an der Stelle, an der sie stehen.

Das ist, in klein, das Prinzip der ganzen Beschreibung: Die Bausteine sind schlicht, und ihre Bedeutung entsteht erst aus dem Zusammenhang.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `Status`, `EffectiveTime`, `ExpirationTime`, `EntitlementEffectiveTime`, `EntitlementExpirationTime`, `DiscountEffectiveTime`, `DiscountExpirationTime`, `ApplicationEffectiveTime`, `ApplicationExpirationTime`, `NonNegativeInteger`, `PositiveInteger`, `OrderNumber`, `Infotext`, `EntryId`, `TransitionCounter`, `LastSAMActionData` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Zähler, Zeit und Versionen (ASN.1)](zaehler-zeit-und-versionen-asn-1.md) – `UnixTime` und die Zähler
- [Gültigkeit](../berechtigungen/gueltigkeit.md) – der Begriff
- [Verzeichnisse auf dem Medium (ASN.1)](../medien/verzeichnisse-auf-dem-medium-asn-1.md) – wo `EntryId` vorkommt
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Zähler, Zeit und Versionen (ASN.1)](zaehler-zeit-und-versionen-asn-1.md)
- [Gültigkeit](../berechtigungen/gueltigkeit.md)
- [Verzeichnisse auf dem Medium (ASN.1)](../medien/verzeichnisse-auf-dem-medium-asn-1.md)
- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
