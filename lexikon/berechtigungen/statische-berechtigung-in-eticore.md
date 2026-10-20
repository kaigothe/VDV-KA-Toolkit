---
titel: Statische Berechtigung in etiCORE
englisch: static entitlement in etiCORE
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/statische-berechtigung.md, lexikon/berechtigungen/berstatus.md, lexikon/berechtigungen/bersynchronnummer.md, lexikon/datenformate/vdv-barcode.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes:
  - wert: 5
    codeliste: EntitlementStatusEnum
    bedeutung: Beendet (terminated; in EN 1545-1:2015 „cancelled“)
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementStatusEnum
    status: belegt
    verbundspezifisch: false
  - wert: 7
    codeliste: EntitlementStatusEnum
    bedeutung: In Ordnung (ok)
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementStatusEnum
    status: belegt
    verbundspezifisch: false
  - wert: 19
    codeliste: EntitlementStatusEnum
    bedeutung: Gesperrt (blocked)
    quelle: Q51
    fundstelle: Modul user-medium, Typ EntitlementStatusEnum
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F3B"
    codeliste: ASN.1-Tag (Modul ste)
    bedeutung: StaticEntitlements — Liste signierter Berechtigungen samt Zertifikat des signierenden SAM
    quelle: Q51
    fundstelle: Modul ste
    status: belegt
    verbundspezifisch: false
  - wert: "0x7F3C"
    codeliste: ASN.1-Tag (Modul ste)
    bedeutung: StaticEntitlementData — eine Berechtigung mit Signatur
    quelle: Q51
    fundstelle: Modul ste
    status: belegt
    verbundspezifisch: false
  - wert: "0xA6"
    codeliste: ASN.1-Tag (Modul ste)
    bedeutung: StaticElectronicTicketParameters — Parameter zur Vorbereitung der Ausgabe mit einem SAM
    quelle: Q51
    fundstelle: Modul ste
    status: belegt
    verbundspezifisch: false
  - wert: "0x30"
    codeliste: ASN.1-Tag (Modul ste)
    bedeutung: StaticEntitlementsData — Liste der Einträge
    quelle: Q51
    fundstelle: Modul ste
    status: belegt
    verbundspezifisch: false
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Statische Berechtigung in etiCORE
<!-- /GEN:breadcrumb -->

# Statische Berechtigung in etiCORE

Das Modul `ste` der ASN.1-Beschreibung definiert die [statische Berechtigung](statische-berechtigung.md) von etiCORE als signierten Datensatz ([Q51](../../QUELLEN.md#q51), Modul `ste`). Von außen nach innen:

- `StaticEntitlements` (Tag `0x7F3B`) enthält mindestens einen Eintrag und das Zertifikat des signierenden SAM, `samCertificate`.
- `StaticEntitlementData` (`0x7F3C`) trägt `specVersion`, optional eine `sceId`, mit der die Berechtigung an eine App-Instanz gebunden wird, die `entitlement`, die Kennung des Signaturalgorithmus und die `signature`. Sie wird über alle Angaben davor „including tags and lengths“ gebildet.
- Die `Entitlement`-Struktur (`0x69`) stammt aus dem Modul `user-medium`: Produkt-ID, Berechtigungs-ID, Ausgabezähler, optionale Auftragsnummer, Gültigkeitsbeginn und -ende, Status und zwei Zähler ([Q51](../../QUELLEN.md#q51), Modul `user-medium`).

`StaticElectronicTicketParameters` (`0xA6`) bereitet die Ausgabe im Zusammenspiel mit einem SAM vor. Die Auftragsnummer ist darin nur gesetzt, wenn die Berechtigung über eine Aktionsliste ausgegeben wird.

Der Status kennt drei Werte: **5** terminated, **7** ok und **19** blocked, mit Verweis auf EN 1545-1:2015 ([Q51](../../QUELLEN.md#q51), Typ `EntitlementStatusEnum`). Der `entitlementTransitionCounter` zählt Statuswechsel, der `entitlementActionCounter` ausgeführte Aktionen.

Ein Vergleich mit dem VDV-Barcode der KA 1.x steht hier nicht an; die Quelle beschreibt nur etiCORE (Release-Kandidat 3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Olli Tapsig kauft einen Einzelfahrschein Bärstadt per App. Stellen wir uns vor, er bekommt ihn als statische Berechtigung nach etiCORE.

Man kann sich den Datensatz wie einen Brief mit Siegel vorstellen. Im Brief steht, was Olli darf: das Produkt 2002 des Bären-Verkehrsbunds, ab wann und bis wann es gilt, dass es in Ordnung ist. Das Siegel ist die Signatur. Wer den Brief liest, kann prüfen, dass er unterwegs nicht verändert wurde. Weil die Signatur auch die Längenangaben mit abdeckt, würde schon ein verschobenes Byte auffallen.

Beigelegt ist ein Ausweis des Absenders: das Zertifikat des SAM, das unterschrieben hat. Damit kann Petra Pranke mit ihrem Kontrollgerät nachvollziehen, wer unterschrieben hat, ohne beim Bären-Verkehrsbund anrufen zu müssen.

Ein Feld, die `sceId`, kann die Berechtigung an eine bestimmte App-Instanz binden, hier an Ollis App. Es ist optional, und wie diese Bindung geprüft wird, nennt die Quelle nicht.

Und noch ein Hinweis zum Status: Er kennt in diesem Modul nur „beendet“, „in Ordnung“ und „gesperrt“. Wer aus der KA 1.x den Wert 8, „neu, aber noch nicht aktiv“, kennt, findet ihn hier nicht.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6: Modul `ste` (Typen `StaticEntitlements`, `StaticEntitlementData`, `StaticEntitlementsData`, `StaticElectronicTicketParameters`), Modul `user-medium` (Typen `Entitlement`, `EntitlementStatusEnum`, `TransitionCounter`) · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Statische Berechtigung](statische-berechtigung.md) – der Begriff in der KA
- [berStatus](berstatus.md) – die Statuswerte der KA 1.x
- [berSynchronNummer](bersynchronnummer.md) – Vorläufer des Übergangszählers
- [VDV-Barcode](../datenformate/vdv-barcode.md) – ein Datenformat statischer Berechtigungen

<!-- GEN:siehe_auch -->
## Siehe auch

- [Statische Berechtigung](statische-berechtigung.md) (StatBer)
- [berStatus](berstatus.md)
- [berSynchronNummer](bersynchronnummer.md)
- [VDV-Barcode](../datenformate/vdv-barcode.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
