---
titel: Applikation
abkuerzung: App
englisch: Application
parent: lexikon/medien.md
siehe_auch: [lexikon/medien/applikationsinstanz-id.md, lexikon/medien/lebenszyklus-der-applikation.md]
quellen: [Q02, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Medien](../medien.md) › Applikation
<!-- /GEN:breadcrumb -->

# Applikation

„Eine Applikation gemäß ISO 24014-1:2020 besteht aus **Daten, Kommandos, Abläufen, Zuständen, Mechanismen, Algorithmen und Programmcode** — z. B. innerhalb einer Chipkarte oder als Emulation in einem Smartphone —, um diese im Rahmen eines bestimmten Systems zu betreiben.“ ([Q02](../../QUELLEN.md#q02), S. 22)

Zu den Mechanismen zählen die Einbindung in die **Sicherheitsarchitektur** des jeweiligen Gesamtsystems sowie die Chipkarten-Übertragungsprotokolle ([Q02](../../QUELLEN.md#q02), S. 22).

Die Definition ist weiter als „Datenstruktur“: Eine Applikation bringt auch **Abläufe und Programmcode** mit. Deshalb kann ein Terminal mit ihr Transaktionen durchführen, statt nur Bytes zu lesen (abgeleitet).

**Anonymität ist im Hintergrundsystem definiert, nicht auf dem Medium.** Zusammen mit der [Applikationsinstanz-ID](applikationsinstanz-id.md) können Personendaten im Hintergrundsystem hinterlegt sein; „eine Applikation ist **anonym**, wenn dazu im Hintergrundsystem keine Personendaten hinterlegt sind“ ([Q02](../../QUELLEN.md#q02), S. 22). Ob eine Karte anonym ist, entscheidet also nicht ihr Inhalt, sondern was das Backend über sie weiß.

Da auf einem Nutzermedium mehrere Applikationen existieren können, dient die **Applikations-Kennung (AID)** dazu, die richtige — hier die KA- bzw. etiCORE-Applikation — auszuwählen ([Q02](../../QUELLEN.md#q02), S. 24).

Normquelle ist die nicht öffentliche KA NM-SPEC, Inventarnummer 7 ([Q25](../../QUELLEN.md#q25), Kap. 3). Zum Weg von der Initialisierung bis zur Nutzbarkeit siehe [Lebenszyklus der Applikation](lebenszyklus-der-applikation.md).

Abkürzung: **App**.

## Einfach erklärt – Beispiel aus Bärstadt

„Applikation" klingt nach einer App auf dem Handy, und das ist kein schlechter Vergleich — nur sitzt sie hier auf einem Chip.

Auf Pias BärenKarte liegt nicht einfach eine Tabelle mit Daten. Es liegt dort etwas, das **antworten** kann. Wenn das Lesegerät am Hauptbahnhof mit der Karte spricht, stellt es Fragen und bekommt Antworten; dabei rechnet der Chip mit, prüft Schlüssel und führt eine Transaktion durch, die entweder vollständig gelingt oder gar nicht.

Deshalb spricht die Definition von Kommandos, Abläufen und Programmcode. Eine reine Datenstruktur könnte das nicht.

Eine Karte kann mehrere solche Applikationen tragen — eine für den Nahverkehr, eine fürs Bezahlen, eine für den Werksausweis. Damit das Gerät weiß, mit welcher es reden will, gibt es eine Kennung. Das ist wie die Durchwahl in einem Unternehmen: Dieselbe Nummer, verschiedene Ansprechpartner.

Der interessanteste Satz der Definition betrifft aber die **Anonymität**, und er steht an einer überraschenden Stelle.

Man würde vermuten: Eine Karte ist anonym, wenn kein Name darauf steht. Das Glossar sagt etwas anderes. Eine Applikation ist anonym, wenn **im Hintergrundsystem** keine Personendaten zu ihr hinterlegt sind.

Das verschiebt die Frage grundlegend. Olli Tapsig könnte eine Karte ohne jeden Namenseintrag haben — wenn die Verkehrsbetriebe zu dieser Kartennummer seinen Namen, seine Adresse und seine Bankverbindung gespeichert haben, ist sie nicht anonym. Umgekehrt stünde Pias Name auf ihrer Karte, und trotzdem entscheidet über die Anonymität, was das Rechenzentrum weiß.

Für Datenschutzdiskussionen ist das der entscheidende Punkt: Es nützt wenig, auf das Medium zu schauen. Man muss ins Backend schauen.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 22 („Applikation / Application“: Definition nach ISO 24014-1:2020 mit Daten, Kommandos, Abläufen, Zuständen, Mechanismen, Algorithmen und Programmcode; Einbindung in die Sicherheitsarchitektur und die Chipkarten-Übertragungsprotokolle; Hinterlegung von Personendaten im Hintergrundsystem gemeinsam mit der Applikationsinstanz-ID; Definition der Anonymität über das Hintergrundsystem; Abkürzung App), S. 24 („Applikations-Kennung / Application Identifier, AID“: Auswahl der richtigen Applikation auf einem Medium mit mehreren Applikationen)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA NM-SPEC, Inventarnummer 7)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Applikationsinstanz-ID](applikationsinstanz-id.md)
- [Lebenszyklus der Applikation](lebenszyklus-der-applikation.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Medien](../medien.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
