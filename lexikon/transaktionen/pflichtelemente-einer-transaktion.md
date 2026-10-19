---
titel: Pflichtelemente einer Transaktion
englisch: mandatory transaction elements
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/grundlagen/datenschutz.md, lexikon/datenformate/nullwerte.md]
quellen: [Q48]
status: belegt
offene_fragen: [O15]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Pflichtelemente einer Transaktion
<!-- /GEN:breadcrumb -->

# Pflichtelemente einer Transaktion

Die Inhalte der Transaktionen sind in der **KA NM-SPEC** spezifiziert und „notwendig als Element des Sicherheitskonzepts“. Die Datenschutzvorgabe zur [Datensparsamkeit](../grundlagen/datenschutz.md) legt sie wie folgt fest ([Q48](../../QUELLEN.md#q48), S. 7):

| Datenelement | Vorgabe |
|---|---|
| Zeitpunkt | genannt, ohne Einschränkung |
| Ort-ID, Fahrt-ID, Linien-ID | „könnten evtl. gestrichen werden“; nicht benutzte Datenelemente mit `0x00` füllen |
| Typ des Terminals | kann `0x00` sein, ist Bestandteil der Terminal-ID |
| Terminal-ID | **Muss-Element** |
| SAM-ID | **Muss-Element** |
| Produkt-ID | **Muss-Element** |
| Berechtigungs-Nr. | **Muss-Element** |
| Daten der MAC-Sicherung | **Muss-Elemente** |

Dazu der Grundsatz: „Alle weiteren Informationen werden nur dann gefüllt (ungleich `0x00`), wenn sie im Geschäftsprozess zwingend erforderlich sind“ ([Q48](../../QUELLEN.md#q48), S. 7).

Das ist für eine Auswertung die wichtigste Aussage des Artikels: **Ein leeres Feld ist der Normalfall, kein Fehler.** Fehlt dagegen eines der fünf Muss-Elemente, ist die Transaktion unvollständig (abgeleitet).

Zwei weitere Festlegungen derselben Fundstelle: Im Medium werden **höchstens zehn Transaktionen** gespeichert, damit der Kunde seine letzten Nutzungen auslesen kann; gebrauchsbezogene Daten im Nutzermedium werden **beim nächsten Gebrauch überschrieben**. Die Transaktionen werden an das für die genutzte Fahrtberechtigung zuständige [Hintergrundsystem](../rollen/hintergrundsystem.md) weitergeleitet ([Q48](../../QUELLEN.md#q48), S. 7).

Offen ist das Verhältnis des hier genannten Füllwerts `0x00` zu den [Nullwerten](../datenformate/nullwerte.md) der Datenformate, die für andere Typen andere Füllwerte vorsehen (zu prüfen, O15).

## Einfach erklärt – Beispiel aus Bärstadt

Wer zum ersten Mal eine echte Transaktion sieht, erlebt meist eine Enttäuschung: Das halbe Ding ist leer. Ort — leer. Fahrt — leer. Linie — leer. Der erste Gedanke ist: Da ist etwas kaputt.

Nichts ist kaputt. Es ist Absicht, und zwar eine ausdrücklich mit den Datenschutzbehörden abgestimmte.

**Was immer drinstehen muss.** Fünf Angaben sind Pflicht, und alle fünf dienen demselben Zweck — nachzuweisen, dass die Transaktion echt ist und zu wem sie gehört:

- **Terminal-ID:** Welches Gerät war es? Bei Pias Abo-Ausgabe das T-4712 am Hauptbahnhof.
- **SAM-ID:** Welcher Sicherheitsbaustein hat gesichert? SAM-9010-7.
- **Produkt-ID:** Welches Produkt? Die 2001, das ABO Azubi.
- **Berechtigungs-Nr.:** Welches Exemplar? Die 400815 im Nummernraum der BVB.
- **MAC-Daten:** Die Sicherung selbst, ohne die alles andere wertlos wäre.

**Was fehlen darf.** Ort, Fahrt und Linie. Und das ist der eigentliche Punkt. Würde jede Fahrt mit Haltestelle und Linie gemeldet, entstünde in den Rechnern der BVB genau das, was nicht entstehen darf: ein Bewegungsprofil von Pia. Linie 4, morgens, Waldsiedlung bis Berufsschule Tannenweg, jeden Werktag. Niemand müsste es böse meinen; es wäre einfach da.

Deshalb bleiben diese Felder leer, solange der Geschäftsprozess sie nicht zwingend braucht. Die Vorgabe sagt sogar, man könnte sie ganz streichen.

**Die zehn Plätze auf der Karte.** Auf Pias BärenKarte liegen höchstens zehn Transaktionen. Die elfte überschreibt die erste. Das ist kein Speichermangel, sondern Datensparsamkeit mit einem Nebennutzen: Pia kann ihre letzten Nutzungen selbst auslesen.

**Für ein Prüfwerkzeug** folgt daraus eine klare Regel. Ein leeres Ortsfeld ist kein Befund. Eine fehlende SAM-ID dagegen schon — ohne sie lässt sich nicht nachvollziehen, wer die Transaktion gesichert hat.

## Quellen

- [Q48](../../QUELLEN.md#q48) – Teilnehmerbrief Datenschutz (22.12.2014), S. 7 (Anforderung 4 „Datensparsamkeit“: in KA NM-SPEC spezifizierte Transaktionsinhalte als Element des Sicherheitskonzepts; Muss-Elemente Terminal-ID, SAM-ID, Produkt-ID, Berechtigungs-Nr. und MAC-Sicherung; Ort-ID, Fahrt-ID und Linien-ID mit `0x00` zu füllen; Terminaltyp als Bestandteil der Terminal-ID; weitere Informationen nur bei zwingendem Bedarf; höchstens zehn Transaktionen im Medium; Überschreiben beim nächsten Gebrauch; Weiterleitung an das zuständige Hintergrundsystem)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Datenschutz](../grundlagen/datenschutz.md)
- [Nullwerte](../datenformate/nullwerte.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
