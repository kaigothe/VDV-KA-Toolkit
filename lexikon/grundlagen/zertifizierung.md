---
titel: Zertifizierung
englisch: certification
parent: lexikon/grundlagen.md
siehe_auch: [lexikon/rollen/scheme-manager.md, lexikon/rollen/akzeptanzterminal.md, lexikon/grundlagen/teilnahmevertrag.md, lexikon/grundlagen/ka-spezifikationen.md]
quellen: [Q02, Q14, Q15, Q37]
status: zu prüfen
offene_fragen: [O23]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Grundlagen](../grundlagen.md) › Zertifizierung
<!-- /GEN:breadcrumb -->

# Zertifizierung

Die **Zertifizierung** ist eine Rolle des Scheme Managers. Sie ist „verantwortlich für die einheitliche Vorgabe der für die Kernapplikation notwendigen Zertifizierungsverfahren, für die Durchführung der Zertifizierung aller Systemkomponenten und für die Erteilung von Zertifikaten für die relevanten Systemkomponenten“ ([Q02](../../QUELLEN.md#q02), S. 100; [Scheme Manager](../rollen/scheme-manager.md)).

Wie das in der Praxis aussieht, zeigen Herstellerangaben (Marktpraxis, keine Norm): Die VDV eTicket Service GmbH zertifiziert Systeme und Geräte nach einem Testprogramm mit praxisnahen Anwendungsfällen, darunter die Verarbeitung von Sperrlisten, das Aktivieren von Notfallschlüsseln und der Umgang mit ungültigen SAMs ([Q14](../../QUELLEN.md#q14); [Q15](../../QUELLEN.md#q15)). Zertifizierte Systeme sollen ohne weitere Anpassung zusammenarbeiten.

Ein Prüfbericht von 2024 zu einem Akzeptanzterminal listet die Testszenarien für Dienstleister- und KVP-Terminal, etwa Applikation und Berechtigung sperren, Sperrlisten aktualisieren, Kryptogramme laden, Notfallschlüssel aktivieren und statische Berechtigungen mit und ohne MOTICS kontrollieren, und schließt mit der Empfehlung, das Produkt „ohne Einschränkungen“ zu zertifizieren ([Q37](../../QUELLEN.md#q37), S. 7 f.). Zugrunde liegen die Spezifikationen in Version 1.12.0.

Wer die Zulassung erteilt, ist im Prüfbericht als „Zulassungsstelle des VDV-ETS“ benannt ([Q37](../../QUELLEN.md#q37), S. 2). Ein Zertifizierungsverfahren für etiCORE nennen die ausgewerteten Quellen nicht (zu prüfen, O23).

## Einfach erklärt – Beispiel aus Bärstadt

Bevor ein neues Terminal bei der BVB in die Linie 4 darf, muss es durch eine Prüfung. Das ist wie die Hauptuntersuchung beim Auto.

Der Hersteller lässt das Gerät von einem Prüflabor testen. Der Prüfer spielt Szenarien durch, wie sie im Betrieb vorkommen: eine Applikation sperren und sehen, ob das Gerät sie danach ablehnt. Die Sperrliste aktualisieren. Eine statische Berechtigung kontrollieren, mit und ohne Kopierschutz. Den Notfallschlüssel aktivieren, wenn ein Schlüssel kompromittiert ist. Besteht das Gerät alles, schreibt das Labor in den Bericht, dass eine Zertifizierung ohne Einschränkungen empfohlen wird.

Die Entscheidung trifft nicht das Labor, sondern die Zulassungsstelle des Scheme Managers, in Bärstadt der Bärenland eTicket Service. Erst nach der Zulassung gilt das Gerät als zertifiziert.

Der Sinn ist praktisch: Die BVB muss nicht jedes Gerät einzeln ausprobieren. Ein zertifiziertes Terminal spricht mit den Systemen des Bären-Verkehrsbunds und des Luchs-Verkehrsverbunds, ohne dass jemand erst nachbessern muss.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 100 (*Zertifizierung / Certification*) (wörtliche Definition)
- [Q37](../../QUELLEN.md#q37) – cetecom advanced, Prüfbericht Akzeptanzterminal, S. 2, 7 f. (Testszenarien, Empfehlung) · *Hersteller / Zulassungsprüfung*
- [Q14](../../QUELLEN.md#q14) – eos.uptrade, *eos.ticketingsuite VDV-KA zertifiziert* (Webarchiv) · *Hersteller*
- [Q15](../../QUELLEN.md#q15) – IVU, *VDV-KA-Zertifizierung für Hard- und Software* (Webarchiv) · *Hersteller*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Scheme Manager](../rollen/scheme-manager.md) – die Instanz, bei der die Rolle liegt
- [Akzeptanzterminal](../rollen/akzeptanzterminal.md) – das typische Prüfobjekt
- [Teilnahmevertrag](teilnahmevertrag.md) – die vertragliche Seite
- [KA-Spezifikationen](ka-spezifikationen.md) – wonach geprüft wird

<!-- GEN:siehe_auch -->
## Siehe auch

- [Scheme Manager](../rollen/scheme-manager.md)
- [Akzeptanzterminal](../rollen/akzeptanzterminal.md) (AKT)
- [Teilnahmevertrag](teilnahmevertrag.md)
- [KA-Spezifikationen](ka-spezifikationen.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Grundlagen](../grundlagen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
