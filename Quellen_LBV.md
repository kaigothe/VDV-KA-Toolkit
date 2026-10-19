# Bewerberaufgabe – Spezialist Vertriebssoftware EFM (m/w/d)

**Leipziger Verkehrsbetriebe (LVB) GmbH**

**Stand:** 19.10.2026

> **Hinweis zur bereinigten Fassung (19.10.2026):** Dieses Dokument ist die Auswertung einer echten KA-Transaktion aus einer Bewerbungsaufgabe. Für die Veröffentlichung sind alle Werte des Originaldatensatzes durch die **fiktiven Entsprechungen aus [welt/baerstadt.md](welt/baerstadt.md)** ersetzt: Organisations-IDs, Berechtigungs- und Applikationsnummern, Produktnummer, Schlüsselnummern sowie Name und Geburtsdatum im produktspezifischen Teil. Die **fachliche Argumentation ist unverändert** — nur die Zahlen sind andere. Wer die Originalwerte braucht, muss die Quelle [Q11](QUELLEN.md#q11) heranziehen; sie ist nicht Teil dieses Repositorys. Zitate aus den Verbunddokumenten sind kurze Exzerpte mit Fundstelle; die Dokumente selbst liegen nicht im Repository (siehe [QUELLEN.md](QUELLEN.md)).

> **Vorbemerkung zur Herangehensweise:** Ich unterscheide durchgängig zwischen (a) direkt ablesbaren Werten, (b) fachlichen Schlussfolgerungen und (c) Punkten, die gegen die für das LVB-/MDV-System gültige VDV-KA-Spezifikation bzw. Codelisten zu prüfen sind. Codewerte, die ich nur aus Vergleichsquellen anderer Verbünde kenne, sind entsprechend gekennzeichnet.

---

## Aufgabe 1: Account Based Ticketing

### 1.0 Begriffsklärung: Account heißt nicht Person

Die Frage wirkt auf den ersten Blick widersprüchlich: Wenn man für ABT einen Account braucht, ist dann nicht jedes Ticket automatisch personalisiert? Das ist nicht der Fall.

Beim ABT ist der Account technisch ein Datensatz im Hintergrundsystem, auf den ein Identifikationsmerkmal (Token) verweist, zum Beispiel:

- die ID einer Chipkarte oder eines einfachen NFC-Mediums,
- eine tokenisierte Bankkarte,
- eine App-Instanz oder ein Gastkonto ohne Login.

Die Berechtigung ist damit an das **Medium bzw. Token** gebunden und nicht an einen Menschen. Wer das Medium besitzt, darf fahren, und das Ticket bleibt durch Weitergabe des Mediums übertragbar. Die VDV eTS verweist für London auf diesen Effekt: Mit tokenisierten Bankkarten ist aus Sicht des Verkehrsunternehmens ein „quasi-anonymes“ Fahren möglich [2].

Zu unterscheiden sind zwei Bedeutungen von „personalisiert“:

| Begriff | Bedeutung | Beispiel |
|---|---|---|
| Tariflich personalisiert | Das Ticket ist nicht übertragbar. Name bzw. Geburtsdatum sind hinterlegt, bei der Kontrolle kann ein Ausweis verlangt werden. | Azubi-Abo (siehe Aufgabe 2), Deutschlandticket |
| Registriertes Kundenkonto | Der Kunde ist mit Namen und Zahlungsdaten registriert. Das Ticket muss deshalb nicht personalisiert sein. | Einzelfahrschein im Konto, der übertragbar bleibt |

**Einschränkung:** Verlangt eine Ticket Cloud für Kauf, Erstattung oder Ersatz ein Login, entsteht eine *faktische* Zuordnung zu einer Person. Das ist eine Gestaltungsfrage. Gegensteuern lässt sich mit Gastkauf, Datenminimierung und einer Trennung von Ticket-Account und Kundenkonto.

### 1.1 Vorteile der Speicherung nicht personalisierter Tickets in der Cloud

Der Kern des ABT ist die Trennung von **Fahrberechtigung** und **Trägermedium**. Die VDV eTS fasst das so zusammen: „Das Account-Based-Ticketing dreht die Logik des Speicherortes um.“ In einem reinen ABT-System werden „überhaupt keine Berechtigungs-Daten auf ein Medium geschrieben“ [2].

| Vorteil | Begründung |
|---|---|
| **Ein Prozess für alle Produkte** | Einzelfahrschein, Tageskarte und Abo laufen über dieselbe Kette: Verkauf, Kontrolle, Clearing, Einnahmenaufteilung. Die Parallelwelt aus Papier, Barcode und Chip entfällt. Das senkt Komplexität und Betriebskosten. |
| **Kein Speicherengpass auf dem Chip** | Auf einer KA-Applikation ist nur Platz für wenige Berechtigungen. Viele kurzlebige Einzelfahrscheine würden diesen Platz belegen. In der Cloud gibt es diese Grenze nicht. |
| **Keine Schreibvorgänge am Medium** | Ein Ticket kann jederzeit und über jeden Kanal gekauft werden und ist sofort gültig [2]. Der Umweg über Aktionslisten und den nächsten Terminalkontakt entfällt. |
| **Einfache, günstige Medien** | Es genügt ein ID-Medium ohne Secure Element und ohne SAM-Schreibvorgang: ein einfacher NFC-Chip, eine Bankkarte oder ein Smartphone. |
| **Zentrale Statusverwaltung und Missbrauchsschutz** | Entwertung, Sperrung, Storno und Erstattung laufen zentral und konsistent über alle Kanäle. Mehrfachnutzung bzw. kopierte Token werden erkennbar, und auf dem Medium gibt es nichts zu manipulieren. |
| **Unabhängigkeit vom Medium** | Bei Verlust oder Gerätewechsel kann die Berechtigung einem neuen Medium zugeordnet werden, sofern eine Wiederherstellungskennung existiert, etwa ein Kaufbeleg oder ein Konto-Token. Bei vollständig anonymen Tickets ohne eine solche Kennung ist ein Ersatz nicht möglich. |
| **Zentrale Tarifpflege** | Tarife und Produkte werden zentral geändert und müssen nicht auf jedem Endgerät nachgezogen werden [2]. Im Gegenzug steigen die Anforderungen an die Verfügbarkeit des Backends, an die IT-Sicherheit und an den Betrieb. |
| **Grundlage für neue Tarifmodelle** | Bestpreis, Fare Capping, Check-in/Check-out und Upgrades wie ein Anschlussfahrschein werden möglich. Voraussetzung ist eine wiedererkennbare Token-Kennung. Ein isoliertes anonymes Einzelticket bringt diesen Vorteil allein nicht. |
| **Datenbasis** | Aggregierte, pseudonyme Echtzeitdaten unterstützen Einnahmenaufteilung, Angebotsplanung und Fraud-Erkennung. Bei nicht personalisierten Tickets bleibt der DSGVO-Aufwand geringer. |
| **Interoperabilität** | Weil viele Prozesse zentral laufen, lassen sich lokale und regionale Systeme leichter verknüpfen [2]. Dafür braucht es weiterhin abgestimmte Standards, Verträge und Clearing. |

**Fazit 1.1:** Ein Einzelfahrschein in der Cloud ist kein Selbstzweck. Er ist der Schritt zu **einer einheitlichen Prozesswelt** für alle Produkte und die Voraussetzung für spätere Tarifmodelle wie Bestpreis oder Check-in/Check-out.

### 1.2 Einwand: „Ohne Online-Verbindung ist keine Kontrolle möglich“

Der Einwand trifft auf eine **reine Echtzeitprüfung gegen das Backend** zu. Auch die VDV eTS nennt die hohe Abhängigkeit von der Konnektivität [2]. Für eine gut gestaltete ABT-Architektur gilt er aber nicht. Folgende Argumente lassen sich entgegenhalten:

1. **Lokaler Cache bzw. Whitelist auf dem Kontrollgerät.** Das Gerät synchronisiert regelmäßig die gültigen Berechtigungen je Medien-ID (als Hash bzw. pseudonymisiert) und dazu die Sperrlisten. Das Datenvolumen ist gering: Auch einige hunderttausend aktive Tickets ergeben nur wenige Megabyte, danach werden nur noch Deltas übertragen. Bei Zeitkarten und Abos ist das unkritisch.
2. **Signierter Offline-Nachweis (hybrides Modell).** Das Smartphone zeigt zusätzlich einen zeitlich begrenzten, digital signierten Barcode, wie es beim Deutschlandticket bereits üblich ist. Das Gerät prüft die Signatur offline mit dem öffentlichen Schlüssel. Damit ist die kritische Lücke geschlossen: Tickets, die Sekunden vor der Kontrolle gekauft wurden. Einschränkung: Die Signatur belegt Echtheit und Integrität, aber nicht zwingend den aktuellen Sperrstatus. Replay-Angriffe begrenzt man über kurze Gültigkeitsfenster.
3. **Nachgelagerte Prüfung (Post-Validation).** Ist das Gerät offline und der Fall unklar, speichert es Medien-ID, Zeit und Ort. Weil der **Kaufzeitpunkt zentral protokolliert** ist, lässt sich später eindeutig feststellen, ob zum Kontrollzeitpunkt eine gültige Berechtigung bestand. Ein erhöhtes Beförderungsentgelt kann dann nachträglich erhoben werden. Die Abschreckung bleibt also erhalten, es fehlt nur die Sofortreaktion. Organisatorisch kennen wir das schon vom Nachreichen eines vergessenen Abos.
4. **Auch die Chipkarte ist nicht wirklich offline.** Bei der heutigen mediumbasierten KA-Kontrolle werden Sperrlisten und Transaktionen ebenfalls synchronisiert, laut VDV eTS typischerweise innerhalb von 24 Stunden [2]. Im eTicket RheinMain etwa werden Sperr- und Aktionslisten „nur einmal täglich erstellt und bereitgestellt“ [8, Kap. 3.2]. Eine Sperrung wirkt dort also bis zu einen Tag verzögert. Der Unterschied zu ABT ist graduell und nicht grundsätzlich.
5. **Internationale Praxis.** ABT-Systeme wie TfL Contactless in London, OMNY in New York und OVpay in den Niederlanden laufen produktiv mit Sperrlisten (Deny Lists) und nachgelagerter Prüfung [5][6].
6. **Wirtschaftliche Abwägung.** Im städtischen LVB-Netz sind Funklöcher kurz und lokal begrenzt. Das Restrisiko aus den wenigen Offline-Fällen ist gering im Vergleich zu den Einsparungen bei Medien, Automaten, Papier und Prozessen.

**Empfehlung für die LVB:** Offline-Fähigkeit sollte von Anfang an Teil des Systemdesigns bzw. der Ausschreibung sein. Dazu gehören:

- ein hybrides Kontrollkonzept aus Online-Abfrage, Cache, signiertem Nachweis und Post-Validation,
- definierte Offline-Gültigkeitsfenster und Synchronisationsintervalle,
- klare Betriebsregeln für das Prüfpersonal,
- eine Kennzahl „Offline-Quote“ zur laufenden Überwachung.

**In einem Satz:** Kontrolle ohne Online-Verbindung ist im ABT möglich, wenn die Architektur lokal prüfbare Nachweise und zwischengespeicherte Statusdaten vorsieht. Das verbleibende Risiko ist begrenzt, messbar und wirtschaftlich vertretbar.

---

## Aufgabe 2: Interpretation der VDV-KA-Nachricht (Transaktion)

### 2.1 Was bedeutet „Aktion“?

Das Hintergrundsystem kann ein Nutzermedium (Chipkarte) nicht direkt beschreiben. Das geht nur, wenn das Medium physisch an ein Terminal gehalten wird. Eine **Aktion** ist daher ein im Hintergrund vorbereiteter **Auftrag**, den ein Terminal beim nächsten Kontakt mit einem bestimmten Nutzermedium ausführt.

Das VDV-Glossar definiert: „Eine Aktionsliste ist eine Liste von auszuführenden Aktionen am Akzeptanzterminal.“ Sie wird beim nächsten Kontakt mit dem Nutzermedium abgearbeitet [3]. Als Aktionstypen nennt das Glossar:

- die **Ausgabe eines EFS** (elektronischer Fahrschein),
- das **Entsperren einer Berechtigung**,
- die **Rücknahme eines EFS**.

Aktionen haben einen Lebenszyklus und werden im **Aktionsmanagement** verwaltet [3]. Das RMV-Schnittstellen-Pflichtenheft bestätigt diese drei Aktionen als „KVP-Aktionen über eine Aktionsliste: Berechtigung-Ausgabe, Berechtigung-Rücknahme, Berechtigung-Entsperrung“ [8, Kap. 2.1.5]. Es beschreibt auch den Datenfluss [8, Kap. 1.2.2]:

1. Der KVP ruft die Aktionsliste beim **ALISE** ab. ALISE ist eine eigene KA-Rolle mit dem Rollen-Code 31 [8, Kap. 4.10]; das System dazu heißt ALISES und ist häufig in das PV-System integriert.
2. Die Terminals führen die Einträge aus.
3. Die Ausführungsnachweise laufen über den KVP zurück an PV bzw. ALISE.
4. Dauerhaft gespeichert werden sie beim **„beauftragenden KVP“**, der die wirtschaftliche Verantwortung trägt. Wichtig ist dabei die Unterscheidung zwischen dem **Auftrag**, also dem Eintrag in der Aktionsliste, und der **nachgewiesenen Ausführung**, also der Rückmeldung des Terminals per Transaktion.

Die Nachricht passt zu diesem Bild:

- Der Namespace `http://vdv/ka/alise/2` verweist auf die KA-Rolle **ALISE** [8, Kap. 4.10], also das System, das die Aktionslisten bereitstellt.
- `txalisber` lese ich als Transaktion „ALISE-Eintrag **Ber**echtigung“, also einen Aktionslisteneintrag für eine Berechtigung. Die Aktionsliste wird insgesamt als TXAML übertragen [8, Kap. 2.1.5, 4.3.1].
- Das Präfix `am…` lese ich als Aktionsmanagement-Merkmale.

Die Zuordnung zur Rolle ALISE ist belegt. Die Lesart von `txalisber` als Eintrag in der TXAML und die Deutung von `am…` sind aus der Benennung abgeleitet.

### 2.2 Auswertung der Meldesequenz

**Hinweis zur Struktur:** Vor dem öffnenden Tag `<ns:txalisber …>` steht bereits `</ns:txalisber>`. Das ist sehr wahrscheinlich das Ende der **vorherigen** Transaktion. Der Ausschnitt stammt also aus einer **Folge mehrerer Meldungen**, eben einer Meldesequenz. Für eine maschinelle Prüfung würde ich den vollständigen Originaldatensatz anfordern, weil der Ausschnitt für sich allein nicht wohlgeformt ist.

#### Feldauswertung

| Feld | Wert | Interpretation |
|---|---|---|
| `amAuftragsTyp` | 13 | Art des Aktionsauftrags. Sehr wahrscheinlich **Ausgabe einer Berechtigung** (siehe Indizienkette unten). Gegen die Codeliste prüfen. |
| `logTransaktionsTyp` | 37 | **Belegt:** „TXABER – Ausgabe EFS über Aktionsliste = 37“. Zum Vergleich: 38 = Entsperrtransaktion, 39 = Rückgabetransaktion, jeweils über Aktionsliste [8, Kap. 2.1.5, Fußnote 1]. Der Code kennzeichnet, welcher Transaktionsnachweis bei der Ausführung entsteht. |
| `berInfoText` | ABO Azubi | Klartext des Produkts: ein **Azubi-Abonnement** (Zeitkarte, personalisiert). |
| `prodProdukt_ID` | 2001 / 9020 | Produktnummer 2001 des **Produktverantwortlichen (PV)** 9020. Eindeutig ist sie nur in Kombination mit der Organisation. |
| `berBerechtigung_ID` | 400815 / 9010 | Eindeutige Kennung der Berechtigung im Nummernraum des **Kundenvertragspartners (KVP)** 9010. |
| `appInstanz_ID` | 90000042 / 9010 | **Zielmedium der Aktion:** die KA-Applikationsinstanz auf der Kundenkarte, ausgegeben vom KVP 9010. |
| `logTransaktionsOperator_ID` | 9010 | Erzeuger der Transaktion ist der KVP. |
| `prodKeyOrganisation_ID` | 9060 | Organisation, deren Schlüssel für das Produkt verwendet werden. |
| `berGueltigkeitsbeginn` | 01.03.2021 00:00:02 | Beginn der Gültigkeit. |
| `berGueltigkeitsende` | 31.12.2025 23:59:58 | Ende der Gültigkeit. Der Zeitraum von knapp fünf Jahren passt zur Dauer einer Ausbildung. Die Sekunden-Offsets deuten auf eine Konvention, um Grenzfälle am Tageswechsel zu vermeiden. |
| `berStatus` | 7 | Laut RMV-Codeliste **aktiv / entsperrt** [4]. Dort gilt außerdem: 5 = zurückgenommen, 8 = neu/nicht aktiv, 19 = gesperrt. |
| `berSynchronNummer` | 1 | Versionszähler der Berechtigung. Der Wert 1 steht für den **ersten Stand**; bei Änderungen steigt der Zähler, sodass Terminals veraltete Stände erkennen. |
| `amAenderungsreferenz_ID` | 0 / 0 | **Keine Vorgänger-Berechtigung.** Es handelt sich also um eine Neuausgabe und keine Änderung. |
| `amTerminalGruppe_ID`, `amTerminal_ID` | alle 0 | Die Aktion ist **an kein bestimmtes Terminal gebunden** und kann an jedem berechtigten Terminal ausgeführt werden. Dafür spricht der Standard: Er sieht zwar „spezifische Aktionslisten für einzelne Terminals bzw. Terminalgruppen“ vor, im eTicket RheinMain werden diese aber zunächst nicht eingesetzt [8, Kap. 2.1.5]. Die Nullwerte passen zu einer allgemeinen Aktionsliste. |
| `prodAbrechnungsVerfahren`, `berBezahlArt` | 0 | Nicht angegeben bzw. Standardwert. Das ist plausibel bei einem Abo, dessen Bezahlung im Vertragssystem läuft, etwa per SEPA. Gegen die Codeliste prüfen. |
| `berBezahlMittel` | (codierter Wert, hier nicht wiedergegeben) | Codierter Wert, ohne Codeliste nicht sicher zu deuten. |

#### Beteiligte Organisationen (technische Rollen)

- **9010**: Kundenvertragspartner (KVP), Transaktionsoperator und Schlüsselinhaber. Im Original das Verkehrsunternehmen selbst.
- **9020**: Produktverantwortlicher (PV) und Schlüsselinhaber. Im Original die Verbund- bzw. Tarifebene.
- **9060**: Produktschlüsselorganisation und Schlüsselinhaber.

Die Namen hinter den IDs lassen sich nur über das Organisationsverzeichnis der VDV eTS belastbar zuordnen. Die hier genannten IDs sind fiktiv (Bereich 9000–9099) und in keinem solchen Verzeichnis enthalten.

#### Schlüsselreferenzen und Sicherheit

| Referenz | Schlüsselnr. | Version | Inhaber |
|---|---:|---:|---:|
| `amMKPV-NM-MAC_ID` | 110 | 1 | 9020 (PV) |
| `amMKKVP-NM-MAC_ID` | 120 | 1 | 9010 (KVP) |
| `amMKERF-NM-MAC_ID` | 130 | 1 | 9060 |

Die Felder enthalten **Referenzen** auf Schlüssel, nicht die geheimen Schlüssel selbst. Mit diesen Schlüsseln bildet das SAM des Terminals beim Schreiben der Berechtigung die MACs (Message Authentication Codes) auf dem Nutzermedium. So sind Integrität und Herkunft getrennt für PV, KVP und Schlüsselorganisation abgesichert. Ob eine Prüfung erfolgreich war, geht aus dem Datensatz selbst nicht hervor.

#### Produktspezifischer Teil (hexadezimal, dekodiert)

```
85 57              → vermutlich TLV-Tag 0x85, Länge 0x57 (87 Byte)
00 00
42 72 75 … 20 20   → Namensfeld, 40 Zeichen, mit Leerzeichen aufgefüllt:
                     "Brummbaer, Pia"             (fiktiv, siehe Welt-Bibel)
00 19 xx 01 01     → Geburtsdatum (BCD): 01.01.19xx  (maskiert)
… 02 11 00 34 E5 17 A7 …
                   → weitere produktspezifische Daten (z. B. Tarifgebiet,
                     Kunden-/Vertragsnummer), Bedeutung nur mit Produktschema
00 …               → Auffüllung
```

**Ergebnis:** Name und Geburtsdatum stehen auf dem Medium. Das belegt die **tarifliche Personalisierung** des Azubi-Abos; der Kontrolleur kann sie mit einem Ausweis abgleichen. Name und Geburtsdatum sind hier ersetzt bzw. maskiert. Im Originaldatensatz stand an dieser Stelle ein Geburtsdatum vom Typ 01.01., also ein runder Wert, der ein Platzhalter sein kann. Andere Systeme verwenden für fehlende Werte ebenfalls feste Standarddaten, etwa 01.01.1970 [7].

#### Indizienkette: Neuausgabe einer Berechtigung

Mehrere Felder bestätigen sich gegenseitig:

1. Transaktionstyp 37 steht für „Ausgabe EFS über Aktionsliste“ (belegt in [8]).
2. Die Änderungsreferenz ist 0, es gibt also keinen Vorgänger.
3. Die SynchronNummer ist 1, es ist also der erste Stand.
4. Das Glossar nennt „Ausgabe EFS“ als einen der Aktionstypen [3].

Daraus folgt mit hoher Wahrscheinlichkeit: **Auftragstyp 13 = Ausgabe einer Berechtigung über die Aktionsliste.**

Zur Kodierung: In KA-Bytestrings ist ein „Nullwert“ nicht immer das Byte 0. Bei PrintableStrings steht er zum Beispiel als Leerzeichen (0x20), bei Orts-Typ-Codes als 0xFF [8, Kap. 5.2]. Die Leerzeichen am Ende des Namensfelds sind deshalb normale Auffüllung und kein Fehler.

### 2.3 Status 7 bei Version 1: Wo bleibt die Prüfung des Azubi-Abos?

Ein Azubi-Abo muss vor der Ausgabe von einem Sachbearbeiter geprüft werden, zum Beispiel anhand des Ausbildungsnachweises. Da liegt die Frage nahe, warum die Berechtigung schon in der ersten Version (`berSynchronNummer` = 1) den Status 7 (aktiv) hat und keinen Zwischenstatus. Die Antwort ergibt sich, wenn man zwei Dinge auseinanderhält.

**1. Status und Version sind verschiedene Größen.**

- `berSynchronNummer` = 1 ist der **Versionszähler** der Berechtigung.
- `berStatus` = 7 ist ein **Code für einen Zustand** und kein Zähler von Prozessschritten.

Die Codes sind nicht fortlaufend vergeben. In der Vergleichscodeliste [4] stehen 5 für zurückgenommen, **7 für aktiv/entsperrt**, 8 für neu/nicht aktiv und 19 für gesperrt. „Neu“ hat also einen *höheren* Code als „aktiv“.

**2. Die fachliche Prüfung findet vor der Berechtigung statt, in einem anderen System.**

Der Prüfprozess des Azubi-Abos (Antrag, Nachweisprüfung, Genehmigung) läuft in der vorgelagerten **Abo- bzw. Vertragsverwaltung**. Die KA-Berechtigung wird erst nach der Genehmigung erzeugt und ist deshalb von Anfang an aktiv:

```
Vertragssystem (Abo-Verwaltung)            VDV-KA-Hintergrundsystem
───────────────────────────────            ────────────────────────
Antrag eingegangen
   ↓
in Prüfung (Sachbearbeiter)
   ↓
genehmigt  ───────────────────────────→  Berechtigung wird erzeugt
                                           Status 7 (aktiv), SynchronNr. 1
                                             ↓
                                           Aktion „Ausgabe EFS“ in der Aktionsliste [3]
                                             ↓
                                           Terminal schreibt die Berechtigung auf die Karte
```

Die vermissten Zwischenstatus gibt es also. Sie sind nur nicht Teil der KA-Transaktion.

Diesen Weg über das Hintergrundsystem schreibt das RMV-Pflichtenheft für Abos ausdrücklich vor: An „Offline“-Verkaufsgeräten ist „die Ausgabe von Fahrtberechtigungen aufgrund von Abonnements und anderen Vertragsprodukten […] ausgeschlossen“ [8, Kap. 1.1]. Ein Vertragsprodukt wie das Azubi-Abo gelangt also über das Hintergrundsystem bzw. die Aktionsliste auf die Karte. Weil die Aktionslisten nur einmal täglich erzeugt werden [8, Kap. 3.2], liegt zwischen Genehmigung und Schreiben auf die Karte mindestens ein Listenzyklus. Hinzu kommt die Zeit bis zum nächsten Terminalkontakt des Kunden.

**3. Alternative: Zwischenstatus innerhalb der KA.**

Möglich ist auch ein anderer Ablauf: Die Berechtigung wird zunächst mit Status 8 (neu/nicht aktiv) [4] auf die Karte geschrieben und nach der Prüfung über die Aktion **„Entsperren einer Berechtigung“** aktiviert. Das VDV-Glossar führt diese Aktion ausdrücklich als eigenen Aktionstyp [3]. In diesem Fall wäre eine zweite Transaktion zu erwarten, und zwar mit dem eigenen Transaktionstyp **38 (Entsperrtransaktion EFS über Aktionsliste)** [8, Kap. 2.1.5, Fußnote 1] und höherer SynchronNummer. Die vorliegende Meldung hat aber den Typ 37 (Ausgabe). Ob ein reiner Statuswechsel die SynchronNummer erhöht, ist gegen die Spezifikation zu prüfen.

**Bewertung:** SynchronNummer 1, Status 7 und Änderungsreferenz 0 sprechen für den **ersten Ablauf**. Die fachliche Prüfung war bereits abgeschlossen, als die Berechtigung erzeugt wurde.

### 2.4 Plausibilitäts- und Manipulationsprüfung

**Grenze der Nachricht:** Die Felder `amMK…-NM-MAC_ID` enthalten nur **Schlüsselreferenzen** (Nummer, Version, Inhaber) und keinen MAC über die Nachricht selbst. Mit diesen Schlüsseln bildet das SAM erst beim Schreiben auf die Karte die MACs. Eine Manipulation, die in sich stimmig ist, lässt sich mit den IDs deshalb nicht erkennen. Ein Beispiel wäre ein Gültigkeitsende, das von 2025 auf 2030 geändert wurde. Kryptografisch gesichert sind die **Transaktionsnachweise der Terminals**, die nach der Ausführung entstehen. Das RMV-Pflichtenheft belegt das an mehreren Stellen:

- Das Hintergrundsystem lehnt Transaktionen mit „negative[m] Ergebnis der MAC-Prüfung“ oder „inkonsistente[n] Daten“ ab und schickt einen Ablehnungsdatensatz (TXA) zurück [8, Kap. 3.1].
- Die MACs werden über die Transaktionsdaten gebildet. Werden einzelne Felder nachträglich verändert, etwa aus Datenschutzgründen, muss die Transaktion gekennzeichnet und von der späteren MAC-Validierung ausgenommen werden [8, Kap. 5.1.2].
- Der Transaktionskopf (TX_BASE) sieht zusätzlich optionale Signaturfelder vor (`transSignatur…`) [8, Kap. 5.4].

**a) Konsistenz innerhalb der Nachricht:**

| Prüfung | Ergebnis |
|---|---|
| KVP der App-Instanz = KVP der Berechtigung = Transaktionsoperator = Inhaber des KVP-MAC-Schlüssels | 9010 = 9010 = 9010 = 9010 ✓ |
| Produktorganisation = Inhaber des PV-MAC-Schlüssels | 9020 = 9020 ✓ |
| Produktschlüssel-Organisation = Inhaber des ERF-MAC-Schlüssels | 9060 = 9060 ✓ |
| Gültigkeitsbeginn liegt vor dem Gültigkeitsende | ✓ |
| Neuausgabe: Änderungsreferenz 0, SynchronNummer 1, Status 7 passen zusammen | ✓ |
| TLV-Länge im produktspezifischen Teil | **auffällig:** 0x57 = 87 Byte angegeben, es folgen aber 90 Byte. Mögliche Ursachen sind Füllbytes, ein Übertragungsfehler oder eine falsche TLV-Annahme. Zu klären. |
| Schema-Prüfung gegen die XSD `vdv/ka/alise/2` | nur mit der XSD möglich; der Ausschnitt ist für sich nicht wohlgeformt |

**b) Abgleich mit Verzeichnissen und Stammdaten:**

- **Schlüsselverwaltung:** Existiert der Schlüssel, ist die Version gültig und für das Produkt zugelassen?
- **Produktverzeichnis:** Existiert Produkt 17/9020 als „ABO Azubi“, und liegt die Gültigkeit im zulässigen Rahmen?
- **Organisationsverzeichnis:** Haben die IDs 9010, 9020 und 9060 die passenden Rollen?
- **Medienverwaltung:** Existiert die App-Instanz 90000042, und ist sie nicht gesperrt?

**c) Abgleich mit dem Quellsystem.** Nur so lassen sich stimmige Manipulationen aufdecken:

- Gibt es einen Azubi-Abo-Vertrag mit genau diesem Zeitraum?
- Passen Name und Geburtsdatum zu den Kundenstammdaten?
- Ist die Berechtigungsnummer eindeutig?

**d) Prüfung der Melde-Sequenz:**

- Die Sequenznummern sind lückenlos, und es gibt keine Duplikate. Im RMV-System gilt eine Transaktion als Duplikat, wenn die Transaktions-ID (Org-ID + Rollen-Code + Sequenznummer) samt Wiederholungszähler oder die ID der enthaltenen Nutzermedium-Transaktion schon vorhanden ist. Duplikate werden abgelehnt [8, Kap. 5.3].
- Zu jeder Aktion gibt es genau eine Ausführungsmeldung mit gültigem SAM-MAC.
- Auffällige Muster werden erkannt, etwa ungewöhnliche Zeiten oder Operatoren.

**Fazit:** Mit den IDs erkennt man Fehler und plumpe Manipulationen. Im Beispiel ist alles in sich konsistent, nur die TLV-Länge sollte man klären. Gegen eine stimmige Manipulation durch jemanden mit Systemzugang helfen nur der Abgleich mit dem Vertragssystem und die kryptografisch gesicherten Ausführungsmeldungen.

### 2.5 Zusammenfassende Interpretation

Der **KVP 9010** erteilt über das Aktionsmanagement den Auftrag, auf die **Kundenkarte mit der KA-Applikationsinstanz 90000042** eine **neue, personalisierte Berechtigung „ABO Azubi“** zu laden. Es handelt sich um Produkt 2001 des PV 9020 mit der Berechtigungsnummer 400815. Die Aktion ist an kein bestimmtes Terminal gebunden. Die Berechtigung wird mit den MAC-Schlüsseln von PV, KVP und Schlüsselorganisation abgesichert.

Die Gültigkeit reicht vom **01.03.2021 bis 31.12.2025**. Der Status ist **7 (aktiv/entsperrt)**. Status und Gültigkeit sind aber getrennt zu betrachten: Der Status ist zwar aktiv, **zeitlich ist die Berechtigung heute (Oktober 2026) abgelaufen**.

**Offene Punkte**, die mit den LVB-Unterlagen zu klären sind:

- die verbindliche Bedeutung von Auftragstyp 13 und Transaktionstyp 37 im verwendeten KA-Release,
- die Bezahl- und Abrechnungscodes,
- das vollständige Produktschema des produktspezifischen Teils,
- die Organisationsnamen hinter den IDs.

---

## Fazit zur Vorgehensweise

Bei einer solchen Analyse gehe ich in vier Schritten vor:

1. **Struktur prüfen:** Ist die Nachricht vollständig und wohlgeformt, und in welchem Kontext steht sie (Einzelmeldung oder Sequenz)?
2. **Felder gruppieren:** nach Identifikation, Produkt, Gültigkeit, Status, Organisationen und Sicherheit.
3. **Ableiten und plausibilisieren:** Felder, die sich gegenseitig bestätigen, zu einer Indizienkette verbinden und Rohdaten wie den Hex-Teil dekodieren.
4. **Verifizieren:** alle Codewerte gegen die **für das LVB-System gültigen** VDV-KA-Codelisten abgleichen und dabei klar trennen, was belegt ist, was geschlossen wurde und was offen bleibt.

---

## Quellen

**[1]** Leipziger Verkehrsbetriebe (LVB) GmbH: *Bewerberaufgabe – Spezialist Vertriebssoftware EFM*, 13.10.2026, S. 1–2. Primärquelle für die Aufgabenstellung und die XML-Werte.

**[2]** VDV eTicket Service: *Einordnung von Account Based Ticketing*, Arbeitsdokument V1.0, 25.03.2024. https://www.kcd-nrw.de/fileadmin/user_upload/VDV-ETSEinordungvonAccountBasedTicketingV1_6602929704990.pdf. Hauptquelle zu ABT: Speicherortlogik, Vorteile, Konnektivität, Synchronisation bei mediumbasierten Systemen und das London-Beispiel.

**[3]** VDV eTicket Service: *Glossar VDV-KA / etiCORE*. https://www.eticket-deutschland.de/media/glossary_vdv_ka_eticore.pdf. Definition von Aktionsmanagement und Aktionsliste sowie die Aktionstypen Ausgabe EFS, Entsperren und Rücknahme.

**[4]** Cubic Transportation Systems / eTicket RheinMain: *vHGS Pflichtenheft PH 05 Systemspezifikation, Anhang 1: RMV-EFS*, v1.6, 15.04.2019. https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_24_EFM_Anh_1a_vHGS_PH05-A1_RMV-EFS_v1.6_190415_MVU_200122.pdf. Vergleichsquelle für die Codewerte berStatus (Abschnitt 2.1 dort; hier genutzt in 2.2 und 2.3) und Transaktionstyp. *Hinweis:* Es handelt sich um die Spezifikation eines anderen Verbunds; die Codes können bei LVB/MDV abweichen. Das Dokument ist öffentlich auffindbar, die zitierten berStatus-Codes habe ich aber nicht selbst im Dokument geprüft. Den Transaktionstyp 37 bestätigt das Schwesterdokument [8].

**[5]** Kentkart: *To validate, or not to validate*. https://www.kentkart.com/?p=15641. Kontrollkonzepte im ABT.

**[6]** Ticketer: *PAR Deny Lists*. https://ticketer.com/en/did-you-know/par-deny-lists. Sperrlisten bei bankkartenbasiertem ABT.

**[7]** TapConnect: *VDV Barcode Field Mappings*. https://documentation.tapconnect.io/public/specs/vdv-barcode-field-mappings.html. Fahrgastdaten in VDV-Strukturen, Namens-Anonymisierung und Standard-Geburtsdatum.

**[8]** Cubic Transportation Systems / eTicket RheinMain: *vHGS Pflichtenheft – Schnittstellenspezifikation PH 06-02 Terminalmanagementsysteme (TMS)*, Version 2.3, 09.11.2018 (Anlage 24, Anhang 2). Belegt den Transaktionstyp 37/38/39 (Kap. 2.1.5, Fußnote 1), die Aktionen und den Datenfluss im Aktionsmanagement (Kap. 1.2.2, 2.1.5), die Rolle ALISE (Kap. 4.10), den Ausschluss von Abo-Ausgaben an Offline-Verkaufsgeräten (Kap. 1.1), den täglichen Listenzyklus (Kap. 3.2), die MAC-Prüfung und Duplikaterkennung (Kap. 3.1, 5.1.2, 5.3) sowie die Kodierung von Nullwerten (Kap. 5.2). *Hinweis:* Vergleichsdokument eines anderen Verbunds; die berStatus-Codes stehen nicht in diesem Dokument, sondern im PH 05-A1 [4].

**Weiterführend:** VDV: *Der Weg zur einheitlichen Fahrkarte – eTicket*, https://www.vdv.de/der-weg-zur-einheitlichen-fahrkarte-eticket.aspx; UITP: *Demystifying Ticketing and Payment in Public Transport*, https://www.uitp.org/publications/demystifying-ticketing-and-payment-in-public-transport/

**Quellenkritik:** Die VDV-KA-Spezifikation und ihre Codelisten sind nicht öffentlich. Releaseabhängige Codezuordnungen sind vor einer verbindlichen Verwendung gegen die für das LVB-System maßgebliche Spezifikation zu prüfen.