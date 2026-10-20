---
titel: Bärstadt in Bärenland
stand: 2026-10-19
hinweis: Referenzseite, kein Lexikonartikel — Navigation wird hier von Hand gepflegt
---

[Home](../README.md) › Bärstadt in Bärenland

# Bärstadt in Bärenland – Welt-Bibel

> **Alles auf dieser Seite ist frei erfunden.** Organisationen, Personen, Org-IDs, Produktnummern und Transaktionswerte sind Phantasie und haben keinen Bezug zu realen Verkehrsunternehmen, Verbünden oder Personen. Die **Struktur** der Beispieltransaktion in Abschnitt 6 ist dem Aufbau einer echten KA-Nachricht nachempfunden ([Q11](../QUELLEN.md#q11)), **alle Werte darin sind ersetzt**.

Diese Seite ist die **verbindliche Referenz** für alle Beispiele im Lexikon. Sie sorgt dafür, dass Namen, Nummern und Zusammenhänge über alle Artikel hinweg gleich bleiben.

**Regel:** Kein Artikel erfindet eigene Namen, IDs, Produkte oder Figuren. Fehlt etwas, wird **zuerst diese Seite ergänzt**, dann der Artikel geschrieben.

---

## 1. Das Land und die Stadt

**Bärenland** ist ein Land mit einem interoperablen elektronischen Fahrgeldmanagement nach dem Vorbild der VDV-Kernapplikation. Der landesweite Verbundrahmen heißt **Bärenland-eTicket**.

**Bärstadt** ist eine Stadt mit etwa 300 000 Einwohnern im Bärenland. Nachbarstadt ist **Luchsstadt** mit einem eigenen Verbund — sie dient den Beispielen zur Interoperabilität.

---

## 2. Organisationen und Rollen

Fiktive Org-IDs liegen im Bereich **9000–9099**. Dieser Bereich ist bewusst gewählt: Er überschneidet sich nicht mit den realen IDs aus [Q11](../QUELLEN.md#q11) und ist als künstlich erkennbar.

| Org-ID | Organisation | Kürzel | KA-Rollen | Rolle im Lexikon |
|---:|---|---|---|---|
| **9010** | Bärstädter Verkehrsbetriebe | **BVB** | KVP, DL | Verkehrsunternehmen: Kundenverträge, Fahrbetrieb, Terminals |
| **9020** | Bären-Verkehrsbund | **BVV** | PV, ALISE | Verbund und Tarifgeber; betreibt den Aktionslistenservice |
| **9030** | Bärenland eTicket Service | **BeTS** | AH | Applikationsherausgeber, Standardgeber im Bärenland |
| **9040** | Kontrollservice Bärenland | **KSB** | KOSE | Sperr- und Kontrolllisten |
| **9060** | Schlüsselstelle Bärenland | **SSB** | Produktschlüsselorganisation | hält die Schlüssel für die Produkte des BVV |
| **9070** | Luchs-Verkehrsverbund | **LVV** | PV, KVP | Nachbarverbund für Beispiele zur Interoperabilität |

**Hinweise für die Artikel:**

- Die **BVB (9010) tritt in zwei Rollen auf**: als KVP gegenüber dem Kunden und als DL im Fahrbetrieb. Genau diese Doppelrolle macht Beispiele zu Rollencodes anschaulich.
- Der **BVV (9020) ist PV und ALISE in einem**. Das ist bewusst so gewählt, weil der Aktionslistenservice häufig in das PV-System integriert ist ([Q06](../QUELLEN.md#q06), Kap. 1.2.2). Wo ein Beispiel die Rollen trennen muss, wird vom „ALISES des BVV“ gesprochen.
- Weil ALISE beim BVV **in das PV-System integriert** ist, tragen Transaktionen aus Aktionsausführungen im Bärenland den **Rollencode 3** (PV) und nicht 31 — so verlangt es die TMS-Schnittstelle ab KA 1.3.0 ([Q06](../QUELLEN.md#q06), Fußnote 7, PDF-S. 39). Beispiele sollen das so zeigen.
- Die **Trennung von 9020 (PV) und 9060 (Schlüsselstelle)** ist Absicht: Sie zeigt, dass Produktverantwortung und Schlüsselhoheit auseinanderfallen können.

---

## 3. Figuren

| Name | Rolle | Merkmale |
|---|---|---|
| **Pia Brummbär** | Auszubildende, 18 Jahre | Hauptfigur. Hat das **ABO Azubi** auf der BärenKarte. Wohnt in der Waldsiedlung, fährt mit der Linie 4 zur Berufsschule. Trägt den durchgehenden Beispielfall. |
| **Olli Tapsig** | Gelegenheitsfahrer | Kauft **Einzelfahrscheine**, meist per App. Figur für ABT-Beispiele und für Vergleiche zwischen Chipkarte und Ticket Cloud. |
| **Petra Pranke** | Prüferin bei der BVB | Kontrolliert in der Linie 4 mit einem mobilen Kontrollgerät. Figur für Kontrolle, Sperrlisten und Sichtkontrolle. |
| **Bodo Bärlauch** | Sachbearbeiter im Kundencenter | Nimmt Abo-Anträge an, prüft Ausbildungsnachweise, löst Sperrungen und Ersatzkarten aus. Figur für alles, was vor der KA-Transaktion passiert. |
| **Familie Tatze** | Gelegenheitsnutzer | Mutter mit zwei Kindern, Figur für Multiberechtigungen und Mitnahmeregelungen. |

Pronomen: Für alle Figuren wird im Text der Vorname verwendet oder „sie“ bzw. „er“ gemäß der Tabelle.

---

## 4. Orte, Terminals und Medien

| Ort | Beschreibung |
|---|---|
| **Bärstadt Hauptbahnhof** | zentraler Knoten; Automat, stationäres Lesegerät, Umstieg auf die Regionalbahn nach Luchsstadt |
| **Kundencenter am Honigmarkt** | Vertriebs- und Servicestelle der BVB; Arbeitsplatz von Bodo Bärlauch |
| **Linie 4** | Straßenbahn Hauptbahnhof – Waldsiedlung; Pias Schulweg, Petras Kontrollrevier |
| **Berufsschule Tannenweg** | Pias Ziel, Haltestelle an der Linie 4 |

| Kennung | Gerät oder Medium | Betreiber |
|---|---|---|
| **BärenKarte** | Nutzermedium, Chipkarte mit KA-Applikation | ausgegeben von der BVB (9010) |
| `appInstanz_ID` **90000042** / 9010 | Applikationsinstanz auf Pias BärenKarte | BVB |
| **T-4711** | Vertriebsterminal im Kundencenter am Honigmarkt | BVB |
| **T-4712** | stationäres Lesegerät Hauptbahnhof | BVB |
| **T-4713** | mobiles Kontrollgerät von Petra Pranke, mit SAM | BVB |
| **T-4714** | mobiles Gerät ohne SAM, nur Sichtkontrolle | BVB |
| **TG-40** | Terminalgruppe „Fahrzeuge Linie 4“ | BVB |
| **SAM-9010-7** | Secure Application Module im Gerät T-4713 | BVB |

---

## 5. Produkte

Produkte des Produktverantwortlichen **BVV (9020)**. Die Produktnummer ist nur zusammen mit der Organisation eindeutig; der Wertebereich einer Produktnummer reicht bis 65535 ([Q35](../QUELLEN.md#q35)).

| `prodProdukt_ID` | Produkt | Art | Personalisierung |
|---|---|---|---|
| **2001** / 9020 | ABO Azubi | Zeitkarte, Abonnement | tariflich personalisiert: Name und Geburtsdatum auf dem Medium |
| **2002** / 9020 | Einzelfahrschein Bärstadt | Einzelfahrt | nicht personalisiert, übertragbar |
| **2003** / 9020 | Monatskarte Bärstadt | Zeitkarte | nicht personalisiert, übertragbar |
| **2004** / 9020 | Tageskarte Familie | Zeitkarte, Multiberechtigung | nicht personalisiert |
| **2005** / 9020 | Bärenland-Ticket | landesweite Zeitkarte | tariflich personalisiert |
| **2101** / 9070 | Luchs-Monatskarte | Zeitkarte des Nachbarverbunds | nicht personalisiert |

---

## 6. Die durchgehende Beispiel-Transaktion

Der Fall, auf den sich möglichst viele Feldartikel beziehen: **Die BVB beauftragt, Pias ABO Azubi auf ihre BärenKarte zu schreiben.**

Die Nachricht ist dem Aufbau eines `txalisber`-Datensatzes nachempfunden ([Q11](../QUELLEN.md#q11)). **Alle Werte sind erfunden.**

### 6.1 Feldwerte

| Feld | Wert | Bedeutung im Beispiel |
|---|---|---|
| `amAuftragsTyp` | **13** | Auftragstyp. Spricht für „Ausgabe einer Berechtigung“ *(abgeleitet, [O2](../PLAN.md))* |
| `logTransaktionsTyp` | **37** | Ausgabe EFS über Aktionsliste |
| `berInfoText` | **ABO Azubi** | Klartext des Produkts |
| `prodProdukt_ID` | **2001** / **9020** | Produkt 2001 des PV BVV |
| `berBerechtigung_ID` | **400815** / **9010** | Berechtigungsnummer im Nummernraum der BVB |
| `appInstanz_ID` | **90000042** / **9010** | Zielmedium: Pias BärenKarte |
| `logTransaktionsOperator_ID` | **9010** | Erzeuger der Transaktion: die BVB als KVP |
| `prodKeyOrganisation_ID` | **9060** | Schlüsselstelle Bärenland |
| `berGueltigkeitsbeginn` | **01.09.2026 00:00:02** | Beginn der Ausbildung |
| `berGueltigkeitsende` | **31.08.2029 23:59:58** | Ende der dreijährigen Ausbildung |
| `berStatus` | **7** | aktiv / entsperrt *(im Bärenland wie im eTicket RheinMain, vgl. [Q05](../QUELLEN.md#q05); verbundspezifisch, [O3](../PLAN.md))* |
| `berSynchronNummer` | **1** | erster Stand der Berechtigung |
| `amAenderungsreferenz_ID` | **0** / **0** | keine Vorgänger-Berechtigung, also Neuausgabe |
| `amTerminalGruppe_ID` | **0** | an keine Terminalgruppe gebunden |
| `amTerminal_ID` | **0** | an kein bestimmtes Terminal gebunden |
| `berBezahlArt` | **0** | nicht angegeben; Bezahlung läuft im Vertragssystem |

### 6.2 Schlüsselreferenzen

Die Felder enthalten **Referenzen** auf Schlüssel — Nummer, Version und Inhaber — nicht die Schlüssel selbst.

| Feld | Schlüsselnr. | Version | Inhaber |
|---|---:|---:|---:|
| `amMKPV-NM-MAC_ID` | 110 | 1 | 9020 (BVV, PV) |
| `amMKKVP-NM-MAC_ID` | 120 | 1 | 9010 (BVB, KVP) |
| `amMKERF-NM-MAC_ID` | 130 | 1 | 9060 (SSB, Schlüsselstelle) |

Die Nummern **110, 120 und 130 sind frei gewählte Platzhalter**. Sie liegen bewusst außerhalb der belegten Key-Identifier-Bereiche, damit niemand sie für echte Schlüsselnummern eines Verbunds hält. Die belegte Systematik der Einsatzzwecke steht in [Key-Identifier](../lexikon/sicherheit/key-identifier.md).

### 6.3 Innere Konsistenz

Der Fall ist absichtlich stimmig gebaut, damit Artikel zur Plausibilitätsprüfung daran arbeiten können:

- KVP der Applikationsinstanz = KVP der Berechtigung = Transaktionsoperator = Inhaber des KVP-MAC-Schlüssels → alle **9010**
- Produktorganisation = Inhaber des PV-MAC-Schlüssels → **9020**
- Schlüsselstelle = Inhaber des ERF-MAC-Schlüssels → **9060**
- Gültigkeitsbeginn liegt vor dem Gültigkeitsende
- Neuausgabe: Änderungsreferenz 0, SynchronNummer 1 und Status 7 passen zusammen

### 6.4 Der Ablauf

```
Vertragssystem der BVB (Abo-Verwaltung)        VDV-KA-Hintergrundsystem
──────────────────────────────────────         ────────────────────────
Pia stellt den Abo-Antrag im
Kundencenter am Honigmarkt
   ↓
Bodo Bärlauch prüft den
Ausbildungsnachweis
   ↓
genehmigt  ────────────────────────────→   Berechtigung 400815 wird erzeugt
                                             Status 7, SynchronNummer 1
                                               ↓
                                           Aktion „Ausgabe EFS“ kommt in die
                                           Aktionsliste des ALISES beim BVV
                                               ↓
                                           Pia hält ihre BärenKarte an das
                                           Lesegerät T-4712 am Hauptbahnhof
                                               ↓
                                           Terminal schreibt die Berechtigung
                                           und bildet die MACs mit dem SAM
                                               ↓
                                           TXABER geht über die BVB zurück
                                           an BVV bzw. ALISE
```

**Zeitlicher Hinweis für Beispiele:** Die Aktionslisten im Bärenland werden **einmal täglich** erzeugt — wie im eTicket RheinMain ([Q06](../QUELLEN.md#q06), Kap. 3.2). Zwischen Bodos Genehmigung und dem Schreiben auf die Karte liegen also mindestens ein Listenzyklus und der nächste Terminalkontakt. Diese Verzögerung ist in mehreren Artikeln der Kern der Erklärung.

---

## 7. Weitere festgelegte Fälle

Damit nicht jeder Artikel eine neue Geschichte erfindet, sind diese Nebenfälle verbindlich festgelegt:

| Fall | Beschreibung | Nützlich für |
|---|---|---|
| **F1 — Neuausgabe** | Pias ABO Azubi, der durchgehende Fall aus Abschnitt 6 | Ausgabe EFS, TX 37, Aktionsliste, berStatus, SynchronNummer, Gültigkeit |
| **F2 — Verlust und Sperrung** | Pia verliert die BärenKarte. Bodo sperrt die Applikationsinstanz 90000042; der Eintrag geht über den KSB (9040) in die Sperrliste. Pia erhält die Ersatzkarte mit `appInstanz_ID` **90000043**, die Berechtigung wird neu ausgegeben, diesmal mit `amAenderungsreferenz_ID` auf 400815 und SynchronNummer 2. | Sperrliste, Sperrgrund, Sperrnachweis, Änderungsreferenz, SynchronNummer |
| **F3 — Prüfung ohne Nachweis** | Pia hat die Karte dabei, aber keinen Ausbildungsnachweis. Petra Pranke liest den personalisierten EFS, Name und Geburtsdatum stimmen, der Ausweis fehlt. | Personengebunden, Sichtkontrolle, produktspezifischer Teil, Tag 0xDB |
| **F4 — Entsperrung über Aktionsliste** | Eine Berechtigung liegt mit Status 8 (neu/nicht aktiv) auf der Karte und wird nach der Prüfung über die Aktion „Entsperren“ aktiviert, Transaktionstyp 38. | TX 38, Entsperrung, Entsperrnachweis, berStatus |
| **F5 — Rücknahme** | Pia bricht die Ausbildung ab. Das ABO Azubi wird über die Aktionsliste zurückgenommen, Transaktionstyp 39, Zielstatus 5. | TX 39, Rücknahme EFS, berStatus |
| **F6 — Fahrt nach Luchsstadt** | Pia fährt mit der Regionalbahn nach Luchsstadt. Ihr Medium wird dort gelesen, das Produkt 2001 des BVV ist aber nicht gültig; sie kauft die Luchs-Monatskarte 2101 des LVV (9070). | Interoperabilität, Org-ID, Produktnummer, Fremd-KVP |
| **F7 — Einzelfahrschein in der Cloud** | Olli Tapsig kauft in der App einen Einzelfahrschein. Die Berechtigung liegt im Hintergrundsystem, auf dem Medium steht nichts. Petra prüft mit zwischengespeicherter Liste und signiertem Nachweis. | ABT, MBT, ID-Token, Ticket Cloud, Offline-Kontrolle |
| **F8 — Familienausflug** | Familie Tatze nutzt die Tageskarte Familie 2004 als Multiberechtigung. | Multiberechtigung, Produkt |

---

## 8. Was in Beispielen nicht vorkommt

- **Keine echten Organisationen, Verbünde, Unternehmen oder Personen.** Reale Beispiele gehören ausschließlich in die fachliche Erklärung und nur mit Beleg.
- **Keine realen Org-IDs** und keine Originalwerte aus [Q11](../QUELLEN.md#q11).
- **Keine echten personenbezogenen Daten**, auch nicht maskiert.
- **Keine neuen IDs oder Namen außerhalb dieser Seite.** Bei Bedarf hier ergänzen.

---

**Navigation:** [Home](../README.md) · [Register](../REGISTER.md) · [Struktur](../STRUKTUR.md)
