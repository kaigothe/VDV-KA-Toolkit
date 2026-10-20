---
titel: Verzeichnisse auf dem Medium (ASN.1)
englisch: directories on the user medium in ASN.1
parent: lexikon/medien.md
siehe_auch: [lexikon/medien/nutzermedium.md, lexikon/sicherheit/schluessel-auf-dem-medium-asn-1.md, lexikon/sicherheit/sam-datenobjekte-asn-1.md, lexikon/datenformate/asn-1-typen-in-eticore.md]
quellen: [Q51]
status: abgeleitet
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Medien](../medien.md) › Verzeichnisse auf dem Medium (ASN.1)
<!-- /GEN:breadcrumb -->

# Verzeichnisse auf dem Medium (ASN.1)

Auf dem Nutzermedium gibt es Verzeichnisse, die einen schnellen Überblick geben ([Q51](../../QUELLEN.md#q51), Modul `user-medium`):

- `UmFci` (`0x6F`) ist die Dateisteuerinformation des Mediums: die Applikationskennung `aid` und in `UmProprietaryData` das `ApplicationDirectory`.
- `ApplicationDirectory` (`0x7F7D`) enthält „the most commonly relevant information about the application“: Version, App-Instanz-ID, Status, Übergangszähler und optional Beginn und Ende der Gültigkeit, die Organisation des Inhabers (`ownerId`), eine Liste der Schlüsselreferenzen und die Daten der letzten SAM-Aktion.
- `EntitlementDirectory` (`0x7F7E`) nennt die Gesamtkapazität für Berechtigungen als Anzahl; der Platz je Berechtigung steht im Fähigkeitsprofil. Dazu kommen die Einträge (`EntitlementDirectoryEntry`, `0xA1`): Datengruppen-Kennung `entryId`, Produkt-ID, Berechtigungs-ID, optional Auftragsnummer, Gültigkeitszeitraum, Status und Übergangszähler.
- `PkiDirectory` (`0x7F7F`) fasst Angaben zu den Zertifikaten zusammen ([Schlüssel auf dem Medium](../sicherheit/schluessel-auf-dem-medium-asn-1.md)).
- `ScopeOfApplication` (`0xA2`) ist eine Liste von Organisations-IDs.

Das Verzeichnis ist demnach ein Inhaltsverzeichnis: Es wiederholt Angaben der einzelnen Berechtigungen in Kurzform (abgeleitet). Dasselbe Tag `0x6F` trägt auch die Dateisteuerinformation des SAM ([SAM-Datenobjekte](../sicherheit/sam-datenobjekte-asn-1.md)). Quelle ist ein Release-Kandidat (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Wie ein Buch hat das Medium vorne ein Inhaltsverzeichnis. Wer Pias BärenKarte ans Lesegerät hält, bekommt nicht gleich alles, sondern zuerst diese Übersicht.

Die erste Seite zeigt die Applikation: in welcher Version sie läuft, ihre Instanz 90000042 der BVB, ihr Status und wie oft er gewechselt hat. Die Organisation, die für die Karte verantwortlich ist, steht dort auch.

Die zweite Seite ist das Verzeichnis der Berechtigungen. Zuerst steht, wie viele Berechtigungen überhaupt auf die Karte passen. Dann folgt je Berechtigung eine Zeile: das Produkt, etwa das ABO Azubi (2001 des BVV), die Kennung der Berechtigung, von wann bis wann sie gilt und ihr Status. Das Lesegerät kann daran schon erkennen, was auf der Karte ist, ohne jede Berechtigung im Ganzen zu lesen.

Die letzte Seite verzeichnet die Zertifikate: bei welchen Stellen die Karte welchen Unterschriften vertraut.

## Quellen

- [Q51](../../QUELLEN.md#q51) – etiCORE ASN.1 Data Type Description 3.0.0-rc.6, Modul `user-medium`: `UmFci`, `UmProprietaryData`, `ApplicationDirectory`, `EntitlementDirectory`, `EntitlementDirectoryEntries`, `EntitlementDirectoryEntry`, `PkiDirectory`, `ScopeOfApplication`, `EntryId` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Nutzermedium](nutzermedium.md) – das Medium
- [Schlüssel auf dem Medium (ASN.1)](../sicherheit/schluessel-auf-dem-medium-asn-1.md) – das PKI-Verzeichnis
- [SAM-Datenobjekte (ASN.1)](../sicherheit/sam-datenobjekte-asn-1.md) – die Dateisteuerinformation des SAM
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md) – Überblick

<!-- GEN:siehe_auch -->
## Siehe auch

- [Nutzermedium](nutzermedium.md) (NM)
- [Schlüssel auf dem Medium (ASN.1)](../sicherheit/schluessel-auf-dem-medium-asn-1.md)
- [SAM-Datenobjekte (ASN.1)](../sicherheit/sam-datenobjekte-asn-1.md)
- [ASN.1-Typen in etiCORE](../datenformate/asn-1-typen-in-eticore.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Medien](../medien.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
