---
titel: Kontroll- und Sperrlistenservice
abkuerzung: KOSE
englisch: Hotlist Service
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/rollencodes.md, lexikon/rollen/kvp.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Kontroll- und Sperrlistenservice
<!-- /GEN:breadcrumb -->

# Kontroll- und Sperrlistenservice

Der Kontroll- und Sperrlistenservice (KOSE) bietet Listen mit Sperreinträgen von **Berechtigungen, Applikationen, SAMs, Schlüsseln und Organisationen** ([Q02](../../QUELLEN.md#q02), S. 54).

In der KA geben die Einträge in den dedizierten Listen einen Hinweis darauf, dass die referenzierte Instanz gestohlen, kompromittiert oder ungültig ist ([Q02](../../QUELLEN.md#q02), S. 54).

Wer Einträge **hinzufügen** darf, ist nach Gegenstand geregelt ([Q02](../../QUELLEN.md#q02), S. 54):

- der Scheme Manager für Organisationen, SAMs und Schlüssel,
- die Kundenvertragspartner für Applikationen und Berechtigungen,
- in (((etiCORE zusätzlich der Dienstleister für eigene SAMs.

**Entfernen** können der Scheme Manager (Organisationen, SAMs, Schlüssel) und die Kundenvertragspartner (Applikationen, Berechtigungen) ([Q02](../../QUELLEN.md#q02), S. 54).

In der KA werden darüber hinaus im Rahmen von Collecting and Forwarding nach ISO 24014-1 **Sperrnachweise** bearbeitet, die sich auf eine Berechtigung oder eine Applikation beziehen; sie werden von den Dienstleistern gesammelt und weitergeleitet ([Q02](../../QUELLEN.md#q02), S. 54).

**Wichtiger Versionsunterschied:** In (((etiCORE wird diese Information **nicht länger im KOSE gespeichert**, sondern liegt nur noch im System des Primär-Kundenvertragspartners vor; Sperrnachweise gehen dann direkt vom Dienstleister an den Produktverantwortlichen ([Q02](../../QUELLEN.md#q02), S. 54).

Im `TX_BASE` trägt der KOSE den [Rollencode](rollencodes.md) **5** ([Q06](../../QUELLEN.md#q06), Kap. 4.10) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Der Kontrollservice Bärenland führt die Listen dessen, was nicht mehr gelten soll.

Als Pia ihre BärenKarte als verloren meldete, musste diese Information an jedes Kontrollgerät im Land. Das geht nicht per Zuruf. Also landet ein Eintrag auf einer Sperrliste, und die Geräte laden diese Liste regelmäßig.

Bemerkenswert ist, wie viele verschiedene Dinge gesperrt werden können. Nicht nur Berechtigungen und Karten, sondern auch **Sicherheitsbausteine**, **Schlüssel** und sogar ganze **Organisationen**. Letzteres ist der schwerste Fall: Würde ein Verkehrsunternehmen aus dem System ausgeschlossen, verlieren alle seine Ausgaben die Gültigkeit.

Entsprechend ist genau geregelt, wer was sperren darf. Die Verkehrsbetriebe dürfen Karten und Berechtigungen ihrer eigenen Kunden sperren — Bodo Bärlauch kann Pias Abo stilllegen. Schlüssel oder Organisationen kann er nicht sperren; das darf nur die übergeordnete Stelle. Jeder darf das sperren, was in seiner Verantwortung liegt, und nichts darüber hinaus.

Der Kontrollservice ist außerdem eine Sammelstelle in die andere Richtung. Wenn Petra Pranke bei einer Kontrolle eine gesperrte Karte findet und das Gerät die Sperre auf der Karte vermerkt, entsteht ein Sperrnachweis. Diese Nachweise werden gesammelt und weitergeleitet, damit alle Beteiligten wissen, dass die Sperre wirklich angekommen ist.

Ein Blick in die Zukunft lohnt hier: In der neuen Generation wird es diesen zentralen Dienst in dieser Form nicht mehr geben. Die Information liegt dann beim Kundenvertragspartner, und die Nachweise gehen direkt an den Produktverantwortlichen. Wer heute eine Architektur entwirft, sollte wissen, dass diese Rolle auf dem Weg nach draußen ist.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 53 f. („Kontroll- und Sperrlistenservice / Hotlist Service“: die fünf Arten von Sperreinträgen, Bedeutung der Einträge, Berechtigungen zum Hinzufügen und Entfernen, Bearbeitung von Sperrnachweisen im Rahmen von Collecting and Forwarding nach ISO 24014-1, Wegfall der Funktion in (((etiCORE)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.10 (Rollencode KOSE = 5), Kap. 3.3 (Sperrlisten herunterladen) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Rollencodes](rollencodes.md)
- [Kundenvertragspartner](kvp.md) (KVP)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
