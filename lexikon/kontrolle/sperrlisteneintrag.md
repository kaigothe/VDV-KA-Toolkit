---
titel: Sperrlisteneintrag
englisch: Hotlist Entry
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/sperrliste.md, lexikon/kontrolle/sperrgrund.md]
quellen: [Q02]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Sperrlisteneintrag
<!-- /GEN:breadcrumb -->

# Sperrlisteneintrag

„Ein Sperrlisteneintrag führt zur Aufnahme eines Objekts — Applikation, Berechtigung, Organisation, SAM oder Schlüssel — in die Sperrliste.“ ([Q02](../../QUELLEN.md#q02), S. 89)

Der Eintrag ist damit die **kleinste Einheit** des Sperrmanagements: Eine [Sperrliste](sperrliste.md) ist nichts anderes als eine Menge solcher Einträge ([Q02](../../QUELLEN.md#q02), S. 89).

Das in einen Eintrag aufgenommene Objekt heißt **Sperrobjekt**. Sperrobjekte werden von derjenigen Instanz verwaltet, die die Sperrung veranlasst ([Q02](../../QUELLEN.md#q02), S. 90).

Ein Eintrag sagt aus, „dass die referenzierte Instanz gestohlen, kompromittiert, ungültig usw. ist“ ([Q02](../../QUELLEN.md#q02), S. 54). Die genaue Begründung trägt der [Sperrgrund](sperrgrund.md) ([Q02](../../QUELLEN.md#q02), S. 88).

**Wer Einträge hinzufügen und entfernen darf, ist nach Objektart geregelt** ([Q02](../../QUELLEN.md#q02), S. 54):

| | Hinzufügen | Entfernen |
|---|---|---|
| Organisationen, SAMs, Schlüssel | Scheme Manager | Scheme Manager |
| Applikationen, Berechtigungen | Kundenvertragspartner | Kundenvertragspartner |
| eigene SAMs | in etiCORE auch der Dienstleister | — |

Für die Auswertung folgt daraus ein wichtiger Punkt (abgeleitet): Ein Eintrag für eine **Applikation** setzt die ganze Karte still, ein Eintrag für eine **Berechtigung** nur ein einzelnes Ticket darauf. Beide Fälle sehen in der Sperrliste ähnlich aus, haben aber sehr unterschiedliche Wirkung.

Wird bei der Kontrolle ein relevanter Eintrag gefunden, folgt die physische Sperrung und darüber ein [Sperrnachweis](sperrnachweis.md) ([Q02](../../QUELLEN.md#q02), S. 90).

## Einfach erklärt – Beispiel aus Bärstadt

Ein Sperrlisteneintrag ist eine Zeile mit großer Wirkung.

Als Bodo Bärlauch Pias verlorene Karte sperrte, entstand genau so ein Eintrag: ein Verweis auf die Applikationsinstanz 90000042, versehen mit einem Grund. Diese eine Zeile wanderte in die Sperrliste und von dort auf jedes Kontrollgerät im Bärenland.

Nun ein Unterschied, der im Kundencenter täglich eine Rolle spielt und den man an der Liste kaum erkennt.

Man kann die **Karte** sperren — dann ist alles darauf still. Pias Abo, ein eventuelles Guthaben, jede weitere Berechtigung. Das ist der Verlustfall: Die Karte ist weg, also soll nichts davon nutzbar sein.

Oder man sperrt nur **eine Berechtigung**. Dann bleibt die Karte benutzbar, und nur ein Ticket darauf gilt nicht mehr. Das wäre der Fall, wenn Pias Abo gekündigt wird, sie die Karte aber behält und weiter Einzelfahrscheine darauf lädt.

Beide Einträge sehen in der Liste ähnlich aus — eine Kennung und ein Grund. Die Wirkung ist völlig verschieden. Wer eine Sperrliste auswertet, muss also auf die Objektart schauen, nicht nur auf die Nummer.

Ebenso klar geregelt ist die Zuständigkeit, und sie folgt dem Besitz. Die Bärstädter Verkehrsbetriebe dürfen Karten und Berechtigungen ihrer eigenen Kunden sperren und wieder freigeben. Schlüssel, Sicherheitsbausteine und ganze Organisationen kann nur die übergeordnete Stelle sperren.

Man merkt an dieser Aufteilung, dass hier ein Mehrparteiensystem organisiert wird. Könnte jedes Verkehrsunternehmen beliebige Objekte sperren, wäre das ein Einfallstor — ein einziger fehlerhafter Eintrag könnte einen anderen Teilnehmer lahmlegen.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 89 („Sperrlisteneintrag / Hotlist Entry“: Aufnahme eines Objekts der fünf Arten in die Sperrliste; Sperrliste als Menge von Einträgen), S. 90 („Sperrobjekt / Hotlisted Object“: Verwaltung durch die veranlassende Instanz), S. 54 (Bedeutung der Einträge; Berechtigungen zum Hinzufügen und Entfernen je Objektart, einschließlich der Erweiterung für Dienstleister in etiCORE), S. 88 (Sperrgrund)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
