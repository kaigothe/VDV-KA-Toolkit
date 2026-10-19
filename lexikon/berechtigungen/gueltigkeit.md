---
titel: Gültigkeit
englisch: validity
parent: lexikon/berechtigungen.md
siehe_auch: [lexikon/berechtigungen/berechtigung.md, lexikon/berechtigungen/berstatus.md]
quellen: [Q02, Q05, Q11, Q35]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Berechtigungen](../berechtigungen.md) › Gültigkeit
<!-- /GEN:breadcrumb -->

# Gültigkeit

Eine Berechtigung besteht unter anderem aus einer eindeutigen ID und einem **Gültigkeitszeitraum** ([Q02](../../QUELLEN.md#q02), S. 30). Abgebildet wird er durch zwei Felder im **statischen Teil** der Berechtigung: `berGueltigkeitsbeginn` und `berGueltigkeitsende`, jeweils mit dem Datentyp **`DateTimeCompact`** und **4 Byte** ([Q05](../../QUELLEN.md#q05), Kap. 2.1) · *verbundspezifisch*.

Dass die Gültigkeit im **statischen** Teil liegt, ist die entscheidende Eigenschaft: Sie wird mit der Ausgabe festgeschrieben und nicht mehr verändert. Für den elektronischen Fahrschein sagt das Glossar es ausdrücklich — EFM-Produkt und Tarifparameter zur räumlichen und zeitlichen Gültigkeit stehen mit Nutzungsbeginn fest und werden im Nachhinein nicht mehr verändert ([Q02](../../QUELLEN.md#q02), S. 38).

**Gültigkeit und [Status](berstatus.md) sind unabhängig voneinander.** Eine Berechtigung kann den Status „aktiv“ tragen und zeitlich längst abgelaufen sein; umgekehrt kann sie im Gültigkeitszeitraum liegen und gesperrt sein. Bei der Kontrolle sind daher **beide** zu prüfen (abgeleitet).

Über den Zeitraum der Berechtigung hinaus kennt die Produktebene weitere Zeitangaben. Die NRW-Produktparameter führen unter anderem einen **Vorverkaufsbeginn** sowie Vertriebs- und Gültigkeitsdaten je Produkt ([Q35](../../QUELLEN.md#q35)) · *verbundspezifisch*. Zu trennen sind also drei Ebenen: ab wann ein Produkt verkauft werden darf, ab wann eine konkrete Berechtigung gilt, und wann eine Fahrt stattfindet.

In der ausgewerteten Nachricht tragen die Felder Zeitstempel mit Sekundenversatz gegenüber Mitternacht ([Q11](../../QUELLEN.md#q11)) — vermutlich, um Grenzfälle am Tageswechsel zu vermeiden (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Pias ABO Azubi gilt vom 1. September 2026 bis zum 31. August 2029. Diese zwei Daten stehen in acht Byte auf ihrer Karte, vier für den Anfang und vier für das Ende.

Entscheidend ist, **wo** sie stehen: im statischen Teil. Dort liegt alles, was sich nie ändert. Die Gültigkeit ist mit der Ausgabe besiegelt.

Verlängert der Verkehrsbund Pias Abo um ein Jahr, wird also nicht das Enddatum überschrieben. Die alte Berechtigung wird zurückgenommen und eine neue ausgegeben. Das klingt aufwendig, hat aber denselben Grund wie bei Papierfahrkarten: Ein Ticket, dessen Gültigkeit man nachträglich ändern kann, taugt nicht als Nachweis.

Nun der Punkt, an dem im Kundencenter die meisten Missverständnisse entstehen: **Gültigkeit und Status sind zwei verschiedene Dinge.**

Eine Berechtigung kann den Status „aktiv“ tragen und trotzdem abgelaufen sein. Genau das wäre bei einem Abo mit Ende 2025 heute der Fall: Status 7, aktiv — und seit Monaten nutzlos. Das ist kein Fehler im System. Niemand läuft herum und setzt abgelaufene Berechtigungen auf einen anderen Status; das Datum sagt bereits alles.

Umgekehrt genauso: Pias Abo ist mitten im Gültigkeitszeitraum, aber nach ihrer Verlustmeldung gesperrt. Gültig und doch nicht nutzbar.

Deshalb prüft Petra Pranke bei der Kontrolle immer beides. Nur das Datum zu lesen reicht nicht, nur den Status zu lesen auch nicht.

Eine kleine Eigenheit noch: In echten Datensätzen beginnen Gültigkeiten gern ein paar Sekunden nach Mitternacht und enden ein paar Sekunden davor. Das ist Vorsicht beim Tageswechsel — Mitternacht genau auf der Grenze erzeugt Streitfälle.

## Quellen

- [Q05](../../QUELLEN.md#q05) – RMV PH 05-A1, Kap. 2.1 (PDF-S. 9): `berGueltigkeitsbeginn` und `berGueltigkeitsende` im statischen Teil der Berechtigung, Datentyp `DateTimeCompact` mit je 4 Byte · *verbundspezifisch: eTicket RheinMain*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 30 (Gültigkeitszeitraum als Bestandteil einer Berechtigung), S. 38 (Festschreibung von Produkt und Tarifparametern mit Nutzungsbeginn)
- [Q35](../../QUELLEN.md#q35) – KCD NRW, Produktparameter der Tarife in NRW (Vorverkaufsbeginn sowie Vertriebs- und Gültigkeitsdaten je Produkt) · *verbundspezifisch: NRW*
- [Q11](../../QUELLEN.md#q11) – ausgewertete `txalisber`-Nachricht (Zeitstempel mit Sekundenversatz gegenüber Mitternacht). **Nicht öffentliche Unterlage.**

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Berechtigungen](../berechtigungen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
