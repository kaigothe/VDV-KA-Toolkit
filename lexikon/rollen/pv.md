---
titel: Produktverantwortlicher
abkuerzung: PV
englisch: Product Owner
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/alise.md, lexikon/aktionsmanagement/aktionsliste.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Produktverantwortlicher
<!-- /GEN:breadcrumb -->

# Produktverantwortlicher

Der Produktverantwortliche (PV) entwickelt **aus seinen Tarifen EFM-Produkte** für Transportdienstleistungen in einem oder mehreren geografischen Gebieten, in denen verschiedene Dienstleister Transportdienstleistungen anbieten ([Q02](../../QUELLEN.md#q02), S. 74).

Der Teilnahmevertrag regelt die nötigen Modalitäten zwischen dem Produktverantwortlichen, den Kundenvertragspartnern und den Dienstleistern. Der PV erwirbt vom Scheme Manager vertraglich geregelt das Recht zur Teilnahme an den EFM-Systemen und **registriert dort seine Produkte**; vom Scheme Manager erhält er die nötigen Kennungen und Informationen zur Verwaltung seiner Token, Rechte und Sicherheitsmodule ([Q02](../../QUELLEN.md#q02), S. 74).

Für das Aktionsmanagement ist der PV die zentrale Stelle: Die Aktionsliste wird **vom System des Produktverantwortlichen zur Verfügung gestellt** und von den ausführenden Kundenvertragspartnern abgerufen ([Q02](../../QUELLEN.md#q02), S. 19). Er nimmt bestellte Aktionen als „aktiv“ in seine Liste auf, setzt sie nach der Ausführung auf „ausgeführt“ und meldet dies dem beauftragenden KVP ([Q02](../../QUELLEN.md#q02), S. 20 f.). Der [Aktionslistenservice](alise.md) ist ein Dienst seines Systems ([Q02](../../QUELLEN.md#q02), S. 21).

Auch die Kontrollnachweise laufen bei ihm zusammen ([Q02](../../QUELLEN.md#q02), S. 53).

Im `TX_BASE` trägt der PV den [Rollencode](rollencodes.md) **3** ([Q06](../../QUELLEN.md#q06), Kap. 4.10) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Der Bären-Verkehrsbund besitzt keine Straßenbahn. Er beschäftigt keine Fahrer, besitzt keine Haltestellen und verkauft keine Tickets am Schalter. Trotzdem hängt alles an ihm.

Seine Aufgabe ist das **Produkt**. Er entscheidet, dass es ein ABO Azubi gibt, was es kostet, für wen es gilt, in welchem Gebiet und wie lange. Daraus entsteht Produkt 2001, und diese Nummer gilt nur in Verbindung mit seiner Organisations-ID 9020.

Der Zuschnitt ist bewusst so gewählt. In einem Verbundgebiet fahren mehrere Unternehmen. Würde jedes seine eigenen Produkte definieren, bräuchte Pia für den Weg zur Berufsschule drei Tickets, sobald sie zweimal umsteigt. Weil die Produkte beim Verbund liegen, genügt eines.

Daraus folgt eine Arbeitsteilung, die man sich einprägen kann: Der Verbund **macht** das Produkt, die Verkehrsbetriebe **verkaufen** es, und sie befördern Pia damit. Drei Aufgaben, zwei Organisationen.

Für das Aktionsmanagement ist der Verkehrsbund außerdem der Ort, an dem die Aktionsliste liegt. Das ist zunächst überraschend — die Karte gehört den Verkehrsbetrieben, der Kunde auch, warum führt dann der Verbund die Liste?

Weil es um sein Produkt geht. Wenn das ABO Azubi auf eine Karte geschrieben wird, verändert sich sein Bestand, nicht der der Verkehrsbetriebe. Er muss wissen, wie viele seiner Abos im Umlauf sind, welche zurückgenommen wurden und für welche abgerechnet wird. Die Liste ist deshalb bei dem, dem die Produkte gehören.

Und genau deshalb geht Pias Ausgabenachweis am Ende nicht nur an die Verkehrsbetriebe, sondern auch an ihn.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 74 („Produktverantwortlicher / Product Owner“: Entwicklung von EFM-Produkten aus den Tarifen, Teilnahmevertrag, Registrierung der Produkte beim Scheme Manager), S. 19 (die Aktionsliste wird vom System des PV bereitgestellt), S. 20 f. (Rolle des PV im Lebenszyklus der Aktion), S. 21 (Aktionslistenservice als Dienst des PV-Systems), S. 53 (Kontrollnachweise an den PV)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.10 (Rollencode PV = 3) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
