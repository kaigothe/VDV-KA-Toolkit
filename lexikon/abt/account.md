---
titel: Account
englisch: account
parent: lexikon/abt.md
siehe_auch: [lexikon/abt/id-token.md, lexikon/abt/ticket-cloud.md]
quellen: [Q02, Q30]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Account Based Ticketing](../abt.md) › Account
<!-- /GEN:breadcrumb -->

# Account

„Beim Account Based Ticketing wird allen Fahrgästen eine **eindeutige ID** zugeordnet, die sie mit einem **Account im Hintergrundsystem** verbindet. Dort sind alle Kunden-, Ticket- und Tarifdaten gespeichert, die für Module wie beispielsweise die Fahrpreisberechnung notwendig sind.“ ([Q30](../../QUELLEN.md#q30), Kap. 5.2.1)

„Ein Account stellt ein **Konto** dar, das es Nutzern ermöglicht, ÖPNV-Dienstleistungen in Anspruch zu nehmen. **Einem Account können mehrere [ID-Medien](id-token.md) zugeordnet werden.**“ ([Q30](../../QUELLEN.md#q30), Kap. 5.2.1)

Der letzte Satz ist der folgenreichste: Die Beziehung zwischen Account und Medium ist **1:n**. Ein Account ist damit keine Eigenschaft eines Mediums, sondern die übergeordnete Einheit — Medien sind Zugänge dazu (abgeleitet).

**Account heißt nicht personenbezogen.** Das Glossar beschreibt den Zugang über „ein persönliches Identifikationsmittel, wie Kreditkarten, Chipkarten oder Apps“ ([Q02](../../QUELLEN.md#q02), S. 16); ob dabei Personendaten hinterlegt sind, ist eine Gestaltungsfrage. Nach dem Maßstab der Kernapplikation ist eine Applikation anonym, „wenn dazu im Hintergrundsystem keine Personendaten hinterlegt sind“ ([Q02](../../QUELLEN.md#q02), S. 22) — dasselbe Kriterium lässt sich auf einen Account anwenden (abgeleitet).

Das Weißbuch führt den Account als **erste** von siebzehn Basisanforderungen an ein ABT-Verfahren; weitere betreffen ID-Medium, Mobilitätsanbieter, Kosten, offene Spezifikationen, Datenschutz und Datensicherheit, zentrales System und zentrale Organisation, Open-Source-Komponenten, den Verzicht auf Sperrlisten, zentrale Gültigkeitsprüfung, vereinfachte Ticketerzeugung, Einnahmeaufteilung, alle Tarifprodukte, grenzüberschreitendes ABT und Monitoring ([Q30](../../QUELLEN.md#q30), Kap. 5.2).

## Einfach erklärt – Beispiel aus Bärstadt

Der Account ist der Ort, an dem beim ABT alles zusammenläuft — und er ist nicht das, was man zuerst vermutet.

Man denkt bei „Account" an ein Login mit E-Mail und Passwort. Technisch ist er etwas Schlichteres: ein **Konto**, in dem Tickets, Tarifdaten und Kundendaten liegen, und auf das eine Kennung zeigt.

Der wichtigste Satz dazu steht im Weißbuch: **Einem Account können mehrere ID-Medien zugeordnet werden.**

Was das bedeutet, zeigt Olli Tapsig. Er fährt meist mit dem Handy. Manchmal nimmt er seine Bankkarte, weil der Akku leer ist. Im Winter hat er eine Smartwatch. Drei Medien — ein Konto.

Für Olli heißt das: Es ist gleichgültig, was er hinhält. Das Ticket ist nicht an ein Stück Hardware gebunden, sondern an sein Konto. Verliert er die Bankkarte, verliert er kein Ticket.

Das ist der Punkt, an dem ABT für den Fahrgast spürbar bequemer wird als Pias Karte. Verliert Pia die BärenKarte, ist ihr Abo zunächst nicht nutzbar — es liegt auf dem verlorenen Chip. Es braucht eine Sperrung, eine Ersatzkarte und eine neue Ausgabe.

Und nun eine Klarstellung, die in Diskussionen regelmäßig fehlt: **Ein Account muss keine Person kennen.** „Account" klingt nach Registrierung, aber technisch ist es ein Datensatz mit einer Nummer. Ob daneben ein Name liegt, entscheidet der Betreiber.

Die Kernapplikation bietet für diese Frage sogar einen brauchbaren Maßstab: Anonym ist, wozu im Hintergrundsystem keine Personendaten hinterlegt sind. Nach diesem Kriterium kann ein Account durchaus anonym sein — und ein Kundenkonto mit Namen und Bankverbindung ist es nicht.

## Quellen

- [Q30](../../QUELLEN.md#q30) – VDV eTS, Weißbuch ABT V1.0.1, Kap. 5.2.1 „Account“ (Zuordnung einer eindeutigen ID zu jedem Fahrgast, Verbindung mit einem Account im Hintergrundsystem, dort Kunden-, Ticket- und Tarifdaten für Module wie die Fahrpreisberechnung; Account als Konto; mehrere ID-Medien je Account), Kap. 5.2 (die Basisanforderungen 5.2.1 bis 5.2.17)
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 16 (Authentifizierung über ein persönliches Identifikationsmittel), S. 22 (Anonymität als Eigenschaft des Hintergrundsystems)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Account Based Ticketing](../abt.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
