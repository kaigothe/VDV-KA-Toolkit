---
titel: Hintergrundsystem
abkuerzung: HGS
englisch: Backoffice System
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/akzeptanzterminal.md, lexikon/rollen/dl.md]
quellen: [Q02, Q06, Q13]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Hintergrundsystem
<!-- /GEN:breadcrumb -->

# Hintergrundsystem

Ein Hintergrundsystem umfasst **alle Computersysteme eines elektronischen Fahrgeldmanagements, welche die Verarbeitung und Verwaltung von Daten ab der Hierarchie der [Akzeptanzterminals](akzeptanzterminal.md) übernehmen** ([Q02](../../QUELLEN.md#q02), S. 46).

Die Definition zieht die Grenze also **nach oben**: Alles oberhalb der Terminals ist Hintergrundsystem. Der Begriff bezeichnet keine einzelne Anwendung, sondern eine Schicht.

Je Rolle gibt es ein eigenes System. Das **Dienstleister-System** etwa gehört zu den Hintergrundsystemen und dient als Verbindung zwischen den Dienstleister-Terminals und den anderen beteiligten Systemen im EFM; neben dem Sammeln und Weiterleiten von Daten nimmt es Aufgaben des Monitorings wahr und verwaltet die SAMs ([Q02](../../QUELLEN.md#q02), S. 34). Entsprechende Einträge bestehen für das Kundenvertragspartner-System (S. 60) und das Produktverantwortlichen-System.

Eine Sonderform ist die **Gemeinsame Servicestelle (GSS)**: ein spezielles Hintergrund-Teilnehmersystem, das einen gemeinsamen Zugang in das Interoperabilitätsnetzwerk bietet. Angeschlossene Systeme können über die GSS Nachrichten senden und empfangen, ohne selbst direkt angeschlossen zu sein; die GSS übernimmt die Nachrichtenvermittlung ([Q02](../../QUELLEN.md#q02), S. 46).

Die Arbeitsteilung mit den Terminals ist grundlegend: Ein Hintergrundsystem kann ein Nutzermedium **nicht selbst beschreiben** — dafür braucht es ein Terminal mit physischem Kontakt. Das ist der Grund für das Aktionsmanagement ([Q02](../../QUELLEN.md#q02), S. 19 f.).

Hersteller bieten KA-Hintergrundsysteme als Produkt an ([Q13](../../QUELLEN.md#q13)).

## Einfach erklärt – Beispiel aus Bärstadt

„Hintergrundsystem“ ist kein Produktname, sondern eine Ortsangabe: alles, was hinter den Geräten liegt.

In Bärstadt heißt das konkret: Das Lesegerät T-4712 am Hauptbahnhof ist ein Terminal. Alles, was dessen Daten entgegennimmt, verarbeitet, speichert und weiterleitet, ist Hintergrundsystem. Die Grenze verläuft genau dort, wo die Geräte enden.

Jede Rolle hat ihr eigenes. Die Bärstädter Verkehrsbetriebe haben eines als Kundenvertragspartner — dort liegen Pias Vertrag und ihre Berechtigung. Sie haben eines als Dienstleister — dort laufen die Daten der Fahrzeuggeräte zusammen. Der Bären-Verkehrsbund hat eines, in dem die Produkte und die Aktionsliste liegen.

Die Aufgaben sind erstaunlich bodenständig: Daten sammeln, weiterleiten, den Betrieb überwachen und die Sicherheitsbausteine in den Geräten verwalten. Letzteres wird gern übersehen, ist aber kritisch — ohne gültige Schlüssel in den Geräten kann niemand mehr kontrollieren oder schreiben.

Der wichtigste Satz über Hintergrundsysteme ist aber ein negativer: **Sie können eine Karte nicht beschreiben.** So viel Rechenleistung sie auch haben, sie kommen an Pias Chip nicht heran. Nur ein Gerät, an das Pia ihre Karte hält, kann das. Diese eine Einschränkung erklärt, warum es Aktionslisten gibt, warum ein Abo nicht sofort nach der Genehmigung gilt und warum Sperren verzögert wirken.

Eine Spezialität am Rand: Nicht jedes Unternehmen muss direkt am landesweiten Netz hängen. Es gibt Sammelstellen, über die mehrere Teilnehmer ihre Nachrichten schicken — wie ein Postfachdienst für Unternehmen, die kein eigenes Postfach unterhalten wollen. Für kleine Verkehrsunternehmen senkt das die Hürde erheblich.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 46 („Hintergrundsystem / Backoffice System“: Abgrenzung ab der Hierarchie der Akzeptanzterminals; „Gemeinsame Servicestelle“: gemeinsamer Zugang in das Interoperabilitätsnetzwerk, Nachrichtenvermittlung), S. 34 („Dienstleister-System“: Zugehörigkeit zu den Hintergrundsystemen, Verbindung zu den Terminals, Monitoring, SAM-Verwaltung), S. 60 („Kundenvertragspartner-System“), S. 19 f. (Arbeitsteilung mit den Terminals im Aktionsmanagement)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 1.2 (Datenflüsse zwischen Hintergrundsystem und Terminalmanagementsystemen) · *verbundspezifisch: eTicket RheinMain*
- [Q13](../../QUELLEN.md#q13) – Krauth Technology, KA Background System · *Herstellerquelle, belegt Marktpraxis, nicht den Standard*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
