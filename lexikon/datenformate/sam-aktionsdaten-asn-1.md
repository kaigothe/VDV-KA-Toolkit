---
titel: SAM-Aktionsdaten (ASN.1)
englisch: SAM action data in ASN.1
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/asn-1-typen-in-eticore.md, lexikon/sicherheit/sam.md, lexikon/datenformate/zaehler-zeit-und-versionen-asn-1.md]
quellen: [Q51]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › SAM-Aktionsdaten (ASN.1)
<!-- /GEN:breadcrumb -->

# SAM-Aktionsdaten (ASN.1)

Für Aktionen am Medium liefert ein SAM kleine Datenpakete ([Q51](../../QUELLEN.md#q51), Modul `common`):

- `SamActionData` (`0x7F6A`) besteht aus der `samId` des SAM und dem `samActionCounter`, dem Aktionszähler beim Autorisieren.
- `Script` (`0x30`) ist „a sequence of CommandAPDUs“, mit der ein SAM oder ein Medium entweder konfiguriert oder zurückgesetzt wird.
- `CommandApdu` (`0x52`) enthält einen einzelnen Befehl im Format einer Chipkarten-APDU.
- `Aid` (`0x40`) ist die „registered application identifier“, ein Byte-String von fünf bis sechzehn Bytes.

Wie die Skripte im Einzelnen ablaufen, steht nicht in diesem Modul. Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Ein Skript ist eine Anweisungsliste für ein Chipbauteil, wie ein Rezept: Schritt eins, Schritt zwei, Schritt drei, jeder Schritt ein kleiner Befehl, den die Karte versteht.

Wenn die BVB eine neue BärenKarte für Pia vorbereitet, schickt das System ein Skript, das die Karte einrichtet. Löst Pia die Karte später auf, genügt ein anderes Skript, das sie zurücksetzt. Jeder einzelne Schritt ist ein `CommandApdu`.

Das SAM im Kontrollgerät hält zu jeder Aktion fest, wer es war und die wievielte Aktion es ist: seine eigene Kennung und den Aktionszähler. So lässt sich später nachvollziehen, von welchem Gerät eine Aktion ausging.

Die Applikationskennung schließlich ist die Adresse der Anwendung auf der Karte. Sie sagt dem Lesegerät, welche der Anwendungen auf dem Chip angesprochen wird.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `common`: `SamActionData`, `Script`, `CommandApdu`, `Aid` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md) – Überblick
- [SAM](../sicherheit/sam.md) – das Sicherheitsmodul
- [Zähler, Zeit und Versionen](zaehler-zeit-und-versionen-asn-1.md) – der Aktionszähler

<!-- GEN:siehe_auch -->
## Siehe auch

- [ASN.1-Typen in etiCORE](asn-1-typen-in-eticore.md)
- [Secure Application Module](../sicherheit/sam.md) (SAM)
- [Zähler, Zeit und Versionen (ASN.1)](zaehler-zeit-und-versionen-asn-1.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
