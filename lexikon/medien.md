---
titel: Medien
englisch: media and applications
parent: README.md
siehe_auch: [lexikon/berechtigungen.md, lexikon/rollen/akzeptanzterminal.md]
quellen: [Q02]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../README.md) › Medien
<!-- /GEN:breadcrumb -->

# Medien

Diese Kategorie behandelt den **Träger** einer Berechtigung und das Stück Software darauf.

Das **[Nutzermedium](medien/nutzermedium.md)** „kann als Träger für eine Berechtigung angesehen werden“; je nach Ausprägung sind verschiedene Berechtigungen möglich ([Q02](../QUELLEN.md#q02), S. 66).

Darauf liegt die **[Applikation](medien/applikation.md)** — nach ISO 24014-1:2020 bestehend aus Daten, Kommandos, Abläufen, Zuständen, Mechanismen, Algorithmen und Programmcode, etwa in einer Chipkarte oder als Emulation auf einem Smartphone ([Q02](../QUELLEN.md#q02), S. 22).

Drei Begriffe sind streng zu unterscheiden (abgeleitet aus [Q02](../QUELLEN.md#q02), S. 22, S. 24):

| Begriff | Was es bezeichnet |
|---|---|
| **Applikation** | die Software- und Datenstruktur selbst, als Typ |
| **Applikations-Kennung (AID)** | wählt auf einem Medium mit mehreren Applikationen die richtige aus |
| **[Applikationsinstanz-ID](medien/applikationsinstanz-id.md)** | identifiziert **diese eine** ausgegebene Applikation — und damit aus Sicht des EFM das Nutzermedium eindeutig |

Eine Applikation wird nicht fertig ausgeliefert, sondern durchläuft einen [Lebenszyklus](medien/lebenszyklus-der-applikation.md) von der Initialisierung über die Ausgabe bis zur Aktivierung ([Q02](../QUELLEN.md#q02), S. 17, S. 27, S. 46 f.).

Ob eine Berechtigung auf dem Medium nur vom Berechtigten genutzt werden darf, entscheidet die Eigenschaft [personengebunden](medien/personengebunden.md) ([Q02](../QUELLEN.md#q02), S. 71).

## Einfach erklärt – Beispiel aus Bärstadt

Auf Pias BärenKarte steckt mehr, als man von außen sieht.

Die Karte selbst ist das **Nutzermedium** — das Stück Plastik mit einem Chip darin. Sie ist nur der Träger, ähnlich wie ein Schlüsselbund nur der Träger für Schlüssel ist.

Auf dem Chip liegt die **Applikation**. Das ist die Datenstruktur samt Regeln, die aus einem beliebigen Chip ein KA-Medium macht. Ohne sie wäre die Karte für jedes Lesegerät in Bärstadt bedeutungslos.

Und in dieser Applikation liegt schließlich Pias **Berechtigung**, das ABO Azubi. Drei Ebenen, von außen nach innen.

Warum diese Unterscheidung mehr ist als Begriffsklauberei, zeigt der Verlustfall. Als Pia ihre Karte verloren meldet, wird nicht „die Karte" gesperrt, sondern die **Applikationsinstanz 90000042** — die eine bestimmte Applikation auf dieser einen bestimmten Karte. Die Ersatzkarte bekommt eine neue Instanz, 90000043, und dieselbe Berechtigung wird dort neu ausgegeben.

Eine Chipkarte kann übrigens mehrere Applikationen tragen. Deshalb gibt es eine Kennung, mit der ein Lesegerät sagt: Ich möchte die KA-Applikation sprechen, nicht die andere. Das ist der gleiche Mechanismus, mit dem eine Bankkarte Zahlfunktion und Geldkarte auseinanderhält.

Was man beim Lesen von Spezifikationen leicht verwechselt: Die **Applikations-Kennung** sagt, *welche Art* von Applikation gemeint ist — bei allen BärenKarten dieselbe. Die **Applikationsinstanz-ID** sagt, *welche konkrete* Applikation gemeint ist — bei Pias Karte eine andere als bei der ihrer Mitschülerin.

Und schließlich: Eine Karte ist nicht einfach da und benutzbar. Sie wird angelegt, ausgegeben und freigeschaltet, in dieser Reihenfolge.

## Quellen

- [Q02](../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 66 („Nutzermedium“ als Träger für eine Berechtigung samt Ausprägungen), S. 22 („Applikation“ nach ISO 24014-1:2020), S. 24 („Applikationsinstanz-ID“ und „Applikations-Kennung / AID“), S. 17 („Aktivieren der Applikation“), S. 27 („Ausgabe der Applikation“), S. 46 f. („Initialisierung der NM-Applikation“), S. 70 („Personalisierung der Applikation“), S. 71 („Personengebunden“)

<!-- GEN:unterartikel -->
## Unterartikel

- [Applikation](medien/applikation.md)
- [Applikationsinstanz-ID](medien/applikationsinstanz-id.md)
- [Lebenszyklus der Applikation](medien/lebenszyklus-der-applikation.md)
- [Nutzermedium](medien/nutzermedium.md)
- [Personengebunden](medien/personengebunden.md)
<!-- /GEN:unterartikel -->

<!-- GEN:siehe_auch -->
## Siehe auch

- [Berechtigungen](berechtigungen.md)
- [Akzeptanzterminal](rollen/akzeptanzterminal.md) (AKT)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../README.md) · [Register](../REGISTER.md)
<!-- /GEN:navigation -->
