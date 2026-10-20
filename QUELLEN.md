# Quellenverzeichnis

Zentrales Verzeichnis aller Quellen des VDV-KA-Lexikons. Jeder Lexikonartikel belegt seine Aussagen über die hier vergebenen **Q-Nummern**, zusammen mit Kapitel oder Seite.

**Ankerkonvention:** Jede Überschrift besteht **nur** aus der Q-Nummer. Damit ist der Link-Anker in GitHub, VS Code und Obsidian gleich und stabil: `[Q06](../../QUELLEN.md#q06)`. Der Titel steht als Fettzeile darunter. Diese Überschriften bitte nicht umbenennen.

**Dateien:** Alle beschafften Dokumente liegen in [QUELLEN/](QUELLEN/). Dateinamen beginnen mit der Q-Nummer.

## Legenden

| Typ | Bedeutung |
|---|---|
| `Primär` | Standardgeber: VDV bzw. VDV eTicket Service |
| `Projekt` | Pflichtenheft oder Spezifikation eines Verbunds (verbundspezifisch!) |
| `Hersteller` | Produkt- oder Anbieterseite |
| `Sekundär` | Fachartikel, Verband, Erklärseite |

| Auswertung | Bedeutung |
|---|---|
| `vollständig` | Dokument durchgearbeitet, Fundstellen notiert |
| `teilweise` | Struktur und einzelne Kapitel ausgewertet |
| `offen` | Datei liegt vor, inhaltlich noch nicht ausgewertet |
| `nicht beschafft` | Dokument nicht verfügbar |

| Herkunft | Bedeutung |
|---|---|
| `Original` | direkt von der Originalseite geladen |
| `Webarchiv` | von der Originalseite entfernt, aus dem Internet Archive geladen |
| `lokal` | lag bereits lokal vor |

> **Urheberrecht:** Mehrere Dokumente sind als „Vertraulich“ gekennzeichnet (siehe Spalte „Rechte“). Im Lexikon stehen nur **kurze Exzerpte mit Fundstelle**, keine Volltexte. Der Ordner `QUELLEN/` gehört **nicht** in ein öffentliches Repository, siehe [CLAUDE.md](CLAUDE.md).

---

---

# 1. Primärquellen des Standardgebers

## Q01

**VDV eTicket Service – Einordnung von Account Based Ticketing**

- **Datei:** `QUELLEN/Q01_VDV-eTS_Einordnung-Account-Based-Ticketing_V1.0_2024-03-25.pdf` (11 Seiten)
- **Typ:** Primär · **Herkunft:** Original (kcd-nrw.de) · **Auswertung:** teilweise
- **Stand:** Arbeitsdokument V1.0, 25.03.2024
- **Inhalt:** Abgrenzung von ABT (Account Based Ticketing) und MBT (mediumbasiertes Ticketing). Kernaussage: „Das Account-Based-Ticketing dreht die Logik des Speicherortes um.“ Weiter: ID-Token, Online-Kontrolle, Abhängigkeit von Konnektivität, hybride Systeme, Synchronisation bei MBT (typisch 24 h), Vorteile von ABT, London als „quasi-anonymes“ Beispiel, Bezug zu den KA-Ausbaustufen.
- **Stichworte:** ABT, MBT, ID-Token, Nutzermedium, Ticket Cloud, Online-/Offline-Kontrolle, Hybridsystem
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/VDV-ETSEinordungvonAccountBasedTicketingV1_6602929704990.pdf

## Q02

**VDV eTicket Service – Glossar VDV-KA 1.X / (((etiCORE**

- **Datei:** `QUELLEN/Q02_VDV-eTS_Glossar-VDV-KA-etiCORE.pdf` (101 Seiten)
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** teilweise (Inhaltsverzeichnis vollständig, Einträge selektiv)
- **Inhalt:** Offizielles, **zweisprachiges** Begriffsverzeichnis. Struktur: Releases (S. 2), Abkürzungen ÖPV (S. 8), technische Abkürzungen (S. 12), **138 Definitionen (S. 15–100)**. Jeder Eintrag hat „English Description“, „Deutsche Beschreibung“, „English Abbreviation“, „Deutsche Abkürzung“ — damit Primärbeleg für Begriff, englische Entsprechung **und** Abkürzung.
- **Wichtig:** Die Einträge „Synchronnummer“ und „Berechtigungsstatus“ fehlen im Glossar.
- **Stichworte:** **Begriffsgerüst des Lexikons.** Hauptquelle für fast alle Artikel der Kategorien Rollen, Medien, Berechtigungen, Sicherheit.
- **URL:** https://www.eticket-deutschland.de/media/glossary_vdv_ka_eticore.pdf

## Q03

**VDV eTicket Service – Standard (Website)**

- **Datei:** `QUELLEN/Q03_VDV-eTS_Standard.html`
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** offen
- **Inhalt:** Übersichtsseite zum Standard der VDV-Kernapplikation. Enthält keine direkten Dokument-Downloads.
- **Stichworte:** Einstieg, Versionen, Dokumentenübersicht
- **URL:** https://www.eticket-deutschland.de/standard

## Q04

**VDV – Der Weg zur einheitlichen Fahrkarte (eTicket)**

- **Datei:** `QUELLEN/Q04_VDV_Weg-zur-einheitlichen-Fahrkarte.html`
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** teilweise
- **Inhalt:** Aufbau von eTicket Deutschland, technische Grundlage, zentrale Dienste, Teilnahmeregeln.
- **Stichworte:** eTicket Deutschland, Teilnehmer, zentrale Dienste
- **URL:** https://www.vdv.de/der-weg-zur-einheitlichen-fahrkarte-eticket.aspx

## Q25

**(((eTicket Deutschland – eTicket-Regelwerk / Teilnahmevertrag mit Anlagen (Muster)**

- **Datei:** `QUELLEN/Q25_eTicket-Regelwerk_Teilnahmevertrag-Muster_v1.27_2018-05-16.pdf` (**273 Seiten**)
- **Typ:** Primär · **Herkunft:** Webarchiv (von mtv-unternehmen.de entfernt) · **Auswertung:** teilweise
- **Stand:** Teilnahmevertrag Stand 01.08.2017; Anlage 2 „KA Migrationsszenarien“ V1.6.0, Stand September 2016
- **Inhalt — die wichtigste öffentliche Primärquelle neben Q02:**
  - **Kapitel 3 „VDV-KA-Dokumentation“ (PDF-S. 34 ff.):** vollständiges Verzeichnis der KA-Spezifikationen mit **Inventarnummern 0–59** und Kurzbezeichnungen (KA Glossar = 0, KA BOM-SPEC = 1, Anlage TLV EFS = 2, KA SST-SPEC = 4, KA XML-Schemata/WSDL = 5, KA SEC-SPEC = 6, KA NM-SPEC = 7, KA SAM-SPEC = 8, KA ION-SPEC = 9, KA KOSES-Spec = 11, SysLH 12–21, KA TXx-Prüfungs-ANW = 33, KA MultiBER-SPEC = 40, **KA AktM-SPEC = 41**, KA STB-Spec = 42, PKM 53–57, KA SAM-Server-SPEC = 59).
  - **Kapitel 4 „Markenbuch“ (PDF-S. 38 ff.):** Marke eTicket Deutschland.
  - **Anlage 2, Migrationsszenarien (PDF-S. 158):** **Ausbauvarianten** 1 (eBezahlen), 2 / 2a / 2b-1 / 2b-2 (eFahrschein, eKontrolle EFS), 3 / 3a-1 / 3a-2 (IN-OUT) sowie die **optionalen Ergänzungen** MultiBER, AktM, PKM, STB/VDV-Barcode, tarifliche Besonderheiten — jeweils mit Zuordnung, welche Ergänzung zu welcher Variante zulässig ist.
  - **Kapitel 5 (PDF-S. ~95–102 der Anlage):** **Elementarprozesslisten je Rolle** (KVPS, KVPT, PVS) mit den Aktionsmanagement-Prozessen im Klartext: „Aktionsauftrag EFS_Berechtigung ausgeben“, „… zurücknehmen“, „Berechtigung entsperren“, „Aktionsfreigabe senden“, „Aktionsfreigabemitteilung entgegennehmen“, „Applikationsinformation anfordern und empfangen“, „Aktionslisten anfordern und empfangen“, „Aktionsdifferenzliste anfordern und empfangen“, „Terminalaktionslisten bereitstellen“, „Entsperrnachweis bearbeiten“, „Entsperrnachweis an PV melden“, „TG_Terminal anlegen/entfernen/ändern“.
- **Stichworte:** KA-Spezifikationen und ihre Kurzzeichen, Ausbauvarianten, Elementarprozesse, Aktionsmanagement, Teilnahmevertrag, Markenbuch, zentrale Dienste
- **Rechte:** Mustervertrag, öffentlich ausgeschrieben. Trotzdem nur Exzerpte.
- **URL (tot, 404):** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_27a_EFM_Teilnvertrag____eTicketDeutschl_mAnl_Muster_Stand_170801_MVU.pdf

## Q26

**VDV eTicket Service – Support / ASM-Tool**

- **Datei:** `QUELLEN/Q26_VDV-eTS_Support-ASM-Tool.html`
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** offen
- **Inhalt:** Offizieller Zugang zu Spezifikationen und KA-Releases über das ASM-Tool. Kontakt: service@eticket-deutschland.de.
- **Stichworte:** Bezugsweg der Spezifikationen, Releases, ASM-Tool
- **URL:** https://www.eticket-deutschland.de/support

## Q27

**VDV eTicket Service – Lösungen / (((etiCORE**

- **Datei:** `QUELLEN/Q27_VDV-eTS_Loesungen-etiCORE.html`
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** offen
- **Inhalt:** (((etiCORE als VDV-KA-Version 3, laut Sekundärangabe ab 2026 mit Parallelbetrieb zur VDV-KA 1.x bis 2031. **Vor Verwendung am Dokument selbst prüfen.**
- **Stichworte:** etiCORE, KA-Version 3, Migration, Parallelbetrieb
- **URL:** https://www.eticket-deutschland.de/loesungen

## Q30

**VDV eTicket Service – Weißbuch ABT**

- **Datei:** `QUELLEN/Q30_VDV-eTS_Weissbuch-ABT_v1.0.1.pdf` (37 Seiten)
- **Typ:** Primär · **Herkunft:** Original (kcd-nrw.de) · **Auswertung:** offen
- **Stand:** Version 1.0.1
- **Inhalt:** Weißbuch zum Account Based Ticketing. Inhaltlich noch nicht ausgewertet; nach Umfang und Herkunft die **ergiebigste deutschsprachige Primärquelle zu ABT** und damit Vorrang gegenüber den Herstellerquellen Q17–Q21.
- **Stichworte:** ABT, Architektur, Rollen im ABT, Migration MBT → ABT
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/Weissbuch_ABT_1.0.1.pdf

## Nicht öffentliche KA-Spezifikationen

Die eigentlichen Normdokumente sind **nicht öffentlich** und nur für Lizenznehmer über das ASM-Tool verfügbar ([Q26](#q26)). Ihre Existenz, Kurzbezeichnung und Inventarnummer sind über [Q25](#q25), Kapitel 3, belegt — die **Inhalte** nicht. Artikel, die sich auf diese Dokumente stützen, sind daher `zu prüfen`, solange der Beleg nur aus Projekt- oder Sekundärquellen stammt.

| Inv.-Nr. | Kurzzeichen | Titel | Relevanz |
|---:|---|---|---|
| 0 | KA Glossar | Glossar | öffentlich verfügbar als [Q02](#q02) |
| 1 | KA BOM-SPEC | Hauptdokument mit Basisobjektmodell (BOM) | Datenobjekte, Codelisten, Datentypen |
| 2 | Anlage TLV EFS | Anlage 1 zur technischen Spezifikation | TLV-Struktur des EFS, Tags |
| 3 | Anlage Datenschutz | Anlage 2 zum Hauptdokument | Datenschutzvorgaben |
| 4 | KA SST-SPEC | Schnittstellenspezifikation der Referenzsysteme | TX-Nachrichten (TXABER, TXEBER, TXSNAWB, …) |
| 5 | KA XML-Schemata / WSDL | XML-Schemata und WSDL der TX-Transaktionen | Feldnamen, Datentypen, Namespaces |
| 6 | KA SEC-SPEC | Technisches Konzept Sicherheit | Schlüssel, Zertifikate, PKI |
| 7 | KA NM-SPEC | Spezifikation Nutzermedium | Medien, Applikation, Speicher |
| 8 | KA SAM-SPEC | Spezifikation des SAM | MAC, Schlüssel, Zertifikate |
| 9 | KA ION-SPEC | Datenaustausch im Interoperabilitätsnetzwerk | ION, Transport, Quittung |
| 10 | KA WSS-SPEC | Webservice Security | Transportsicherung |
| 11 | KA KOSES-Spec | Sperrlistenmanagementsystem (KOSE) | Sperrlisten, Kontrolllisten |
| 12–21 | KA SysLH … | Systemlastenhefte (HD, PVS, KVPS, KVPRT, DLS, DLRT, NM) | Terminalabläufe, Kontrolltransaktion |
| 33 | KA TXx-Prüfungs-ANW | Verfahrensanweisung Prüfung von Transaktionen | Plausibilitäts- und MAC-Prüfung |
| 35 | KA PROD_ID-ANW | Vergabe von Produkt_IDs | Produktnummern, Nummernräume |
| 37 | KA App-Ber-Sperr-ANW | Applikations- und Berechtigungssperre | Sperrmanagement |
| 40 | KA MultiBER-SPEC | Multiberechtigungen | TXAMBER, TXEMBER, TXRMBER |
| **41** | **KA AktM-SPEC** | **Aktionsmanagement für die Berechtigungsart EFS** | **Aktion, Aktionsliste (TXAML), Auftragstypen** |
| 42 | KA STB-Spec | Statische Berechtigungen für 2D-Barcode-Tickets | VDV-Barcode |
| 53–57 | KA PKM-… | Produkt-, Kontroll- und Tarifmodule | Fachdaten, Fachfunktionen |
| 59 | KA SAM-Server-SPEC | Schnittstellenspezifikation SAM-Server | SAM-Server |

## Q45

**VDV eTicket Service – ASM-Tool, Glossar und Abkürzungsverzeichnis**

- **Datei:** `QUELLEN/Q45_VDV-eTS_ASM-Tool-Glossar-und-Abkuerzungsverzeichnis_V1.03_2016-07-20.pdf` (35 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** teilweise (Inhaltsverzeichnis geprüft)
- **Stand:** V1.02/1.03, erstellt 10.07.2014, geändert 20.07.2016, Ersteller VDV eTS
- **Inhalt:** **Zweites offizielles Glossar** neben [Q02](#q02), bezogen auf das ASM-Tool. Kap. 1 Abkürzungsverzeichnis (S. 7), Kap. 2 Begriffe (S. 9 ff.), darunter Einträge, die in [Q02](#q02) fehlen — etwa „eTicket Ready Vertrag“ (S. 10).
- **Bedeutung:** direkt verwertbar für [ABKUERZUNGEN.md](ABKUERZUNGEN.md) und als Gegenprobe zu [Q02](#q02).
- **Stichworte:** Abkürzungen, Begriffe, ASM-Tool, eTicket Ready

## Q46

**VDV eTicket Service – Whitepaper Barcodes im ÖPNV**

- **Datei:** `QUELLEN/Q46_VDV-eTS_Whitepaper-Barcode-OEPNV_2021.pdf` (16 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** teilweise
- **Stand:** 2021
- **Inhalt (am Dokument geprüft):** Behandelt **dynamisierte Barcodes** — der signierte Barcode wird dynamisiert, etwa über ein Zeitmerkmal, sodass Kopien zum Kontrollzeitpunkt ein veraltetes Merkmal tragen und erkannt werden. Weiter: Abgrenzung des **UIC-Barcodes** des internationalen Eisenbahnverbands gegenüber dem **VDV-Barcode**, die daraus folgende Notwendigkeit, beide in Kontrollgeräten zu unterstützen, **Kombi-Tickets** mit Grund- und Zusatzfunktion sowie der Datenaustausch bei **NFC-Endgeräten** ohne Visualisierung als 2D-Barcode.
- **Technischer Hinweis:** Die Extraktion verliert Umlaute und Wortteile. Zitate am PDF prüfen.
- **Stichworte:** VDV-Barcode, UIC-Barcode, dynamischer Barcode, Kopierschutz, Kombi-Ticket, NFC

## Q47

**VDV-Kernapplikation – Schlussbericht 2005**

- **Datei:** `QUELLEN/Q47_VDV-Kernapplikation_Schlussbericht_2005.pdf` (89 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** **nicht möglich**
- **Inhalt (unverifiziert):** Schlussbericht zum Vorhaben VDV-Kernapplikation, 2005 — mutmaßlich das Ursprungsdokument des Standards und damit für die historische Einordnung interessant.
- **Technischer Hinweis:** Die Datei ist **verschlüsselt**; `tools/pdftext.py` gewinnt daraus nur 1.771 Zeichen. In einem PDF-Betrachter lässt sie sich öffnen — Inhalte sind dort **von Hand zu prüfen**, bevor sie zitiert werden. Dasselbe gilt für [Q41](#q41).
- **Stichworte:** Historie, Entstehung der KA, 2005 (zu prüfen)

## Q48

**eTicket Deutschland – Teilnehmerbrief Datenschutz**

- **Datei:** `QUELLEN/Q48_eTicket-Deutschland_Teilnehmerbrief-Datenschutz_2014-12-22.pdf` (17 Seiten, geschwärzte Fassung)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** teilweise (Inhaltsverzeichnis geprüft)
- **Stand:** 22.12.2014
- **Inhalt:** Datenschutzrechtliche Grundanforderungen für das EFM, mit den Datenschutzbeauftragten des Bundes und der Länder abgestimmt, gegliedert in **elf Anforderungen**: 1. Transparenz, 2. Widerspruchsrecht, 3. Wahlmöglichkeit, 4. Datensparsamkeit, 5. Getrennte Verarbeitung, 6. Zweckbindung der Ticketdaten, 7. Vorabkontrolle, 8. Zugriffsberechtigung, 9. Datenschutzgerechte Gestaltung der Systemkomponenten, 10. Schutz gegen Missbrauch, 11. Löschung. Jeder Anforderung sind die Maßnahmen zu ihrer Erfüllung gegenübergestellt. Dazu ein Auszug aus **Kapitel 6 des Regelwerks** („Datenschutz-Grundsätze“, S. 13 ff.) und als Anlage das Schreiben des LDI NRW vom 30.10.2012, das die Abstimmung unter den Aufsichtsbehörden für abgeschlossen erklärt.
- **Besonders verwertbar:** Anforderung 4 nennt die **Muss- und Kann-Datenelemente einer Transaktion** (S. 7) — die einzige öffentlich belegte Liste dazu, siehe [Pflichtelemente einer Transaktion](lexikon/transaktionen/pflichtelemente-einer-transaktion.md).
- **Bedeutung:** erste Primärquelle der Sammlung zum Datenschutz. Ergänzt die bisher nur verbundspezifisch belegte Vorgabe zum Leeren der Fahrt- und Linienangaben in Kontrollnachweisen ([Q06](#q06), Kap. 5.1.2).
- **Rechte:** geschwärzte Fassung; Schwärzungen respektieren und nicht zu rekonstruieren versuchen.
- **Stichworte:** Datenschutz, Datensparsamkeit, Zweckbindung, getrennte Verarbeitung, Vorabkontrolle

---

# 2. Die KA-Spezifikationen 1.12.0

Die Normquellen des Standards, am **20.10.2026** beschafft. Sie lösen die bis dahin nötige
Rekonstruktion aus Nebenquellen ab: Wo eine Aussage des Lexikons bisher aus einem Pflichtenheft
eines Verbunds, einem Prüfbericht oder einer Herstellerseite stammte, ist hier der Standard selbst
nachzulesen.

> **Urheberrecht — hier besonders wichtig.** Diese Dokumente sind **nicht öffentlich**, das
> Repository ist es. `QUELLEN/` ist per `.gitignore` ausgeschlossen. Ins Repository kommen **kurze
> Exzerpte mit Fundstelle als Belegnachweis**: Ein Codewert mit Bedeutung und Fundstelle ist ein
> Beleg, eine abgetippte Tabelle mit 200 Zeilen ist eine Vervielfältigung. Im Zweifel weniger
> zitieren.

**Gemeinsame Eigenschaften** — einmal geprüft, gelten für alle Dokumente dieses Abschnitts:

- **Version 1.12.0, Stand 10. Mai 2023.** Damit eine Patch-Version unter dem Stand, den
  [Q43](#q43), Kap. 3, belegt (1.12.1). Für Codelisten und Abläufe unerheblich, für
  Versionsaussagen nicht.
- **Die PDF-Seitenzahl entspricht der gedruckten Seitenzahl**, geprüft an den Seitenfüßen aller
  Dokumente, die eigene Seitenzahlen nennen. Ausnahmen ohne Seitenfuß und damit ohne Gegenprobe:
  [Q58](#q58), [Q79](#q79), [Q81](#q81) und die englische Fassung von [Q69](#q69).
- **Zitiert wird mit Kapitelnummer**, die alle Dokumente führen; die Seite kommt zusätzlich dazu,
  wo das Auffinden es erleichtert.
- **Typ:** Primär · **Herkunft:** lokal (Download aus dem ASM-Tool) · **Rechte:** nicht
  öffentlich, nur Verweis und Kurzexzerpt.
- Die Releaseverwaltung auf Seite 2 jedes Dokuments ist eine eigene Fundgrube: Sie nennt für jede
  Änderung Datum, Kapitel und oft die CR-Nummer und erlaubt damit, Aussagen einer Version
  zuzuordnen.

## Q52

**VDV-Kernapplikation – Hauptdokument mit Basisobjektmodell (KA HD_BOM-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q52_VDV-KA_HD-BOM-SPEC_V1.12.0_2023-05-10.pdf` (186 Seiten)
- **Auswertung:** teilweise — die Aufzählungstypen in Kap. 6 sind erschlossen, die Codelisten zu
  O1, O2 und O3 ausgewertet; Datentypen, Identifikationen und das Objektmodell sind offen
- **Bedeutung:** Das zentrale Dokument des Standards und **die Quelle der Codelisten**. Kapitel 6
  führt die Aufzählungstypen mit Tabellennummern; die hier bestätigten Tabellennummern sind
  `AuftragsTyp_CODE` (Tab. 6-43, S. 69), `IONTransaktionsTyp_CODE` (Tab. 6-59, S. 77 ff.),
  `NmTransaktionsTyp_CODE` (Tab. 6-65, S. 85 ff.), `Mitteilung_CODE` (Tab. 6-63, S. 84),
  `OrtsTyp_CODE` (Tab. 6-69, S. 88 ff.), `Richtung_CODE` (Tab. 6-73, S. 92),
  `SperrlistenStatus_CODE` (Tab. 6-81, S. 95 f.), `SperrmodusTyp_CODE` (Tab. 6-82, S. 96),
  `SperrStatusTyp_CODE` (Tab. 6-83, S. 96), `WertobjektStatus_CODE` (Tab. 6-91, S. 102) und
  `Nutzermedien_ID` (Tab. 6-133, S. 122 f.).
- **Drei Befunde, die bisherige Annahmen betreffen:**
  - `AuftragsTyp_CODE` (Tab. 6-43, S. 69) belegt **13 für den Aktionsauftrag Ausgabe**, 14 für
    Rücknahme, 15 für Entsperrung. Die Vermutung in O2 ist damit bestätigt.
  - `NmTransaktionsTyp_CODE` (Tab. 6-65, S. 86 f.) führt **37, 38 und 39** als Werte der
    Standardcodeliste. Sie sind damit **nicht verbundspezifisch** (O1).
  - `WertobjektStatus_CODE` (Tab. 6-91, S. 102) führt **genau vier Werte: 0, 5, 7 und 19** — die
    **8 fehlt**. Der in [Q05](#q05) genannte Wert 8 ist keine Auswahl aus der Standardliste (O3).
- **Technischer Hinweis:** Die Codelisten stehen in sehr eng gesetzten Tabellen; die zeilenweise
  Extraktion verschmilzt benachbarte Einträge. Werte nur spaltenweise über die X-Position lesen,
  siehe [CLAUDE.md](CLAUDE.md), Regel 10.
- **Stichworte:** Basisobjektmodell, Codelisten, Aufzählungstypen, Datentypen, Identifikationen, Kap. 6

## Q53

**VDV-Kernapplikation – Spezifikation Nutzermedium (KA NM-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q53_VDV-KA_NM-SPEC_V1.12.0_2023-05-10.pdf` (253 Seiten)
- **Auswertung:** offen
- **Inhalt:** „Spezifikation Nutzermedium für elektronisches Fahrgeldmanagement“. Definiert die
  Datenstrukturen auf dem Nutzermedium, darunter die Referenz-Berechtigungen, auf die
  [Q70](#q70) verweist.
- **Gebraucht für:** O15 (Füllwerte nicht benutzter Datenelemente), die Artikel zu Nutzermedium,
  Applikation und EFS, sowie `SAM_ID.samNummer` (nach [Q12](#q12) in Tab. 5-12).
- **Stichworte:** Nutzermedium, Applikation, Referenz-EFS, Datenstrukturen, Füllwerte

## Q54

**VDV-Kernapplikation – Schnittstellenspezifikationen der Referenzsysteme (KA SST-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q54_VDV-KA_SST-SPEC_V1.12.0_2023-05-10.pdf` (253 Seiten)
- **Auswertung:** teilweise — Aufbau und die Kapitel zum Sperrmanagement gesichtet, die
  TX-Nachrichten im Einzelnen offen
- **Inhalt:** Die Schnittstellen der Referenzsysteme KVP, DL, PV, Applikationsherausgeber (AH) und
  Sperrlistenservice (KOSE) — also die **TX-Nachrichten**, auf denen das geplante Prüfwerkzeug
  aufsetzt.
- **Hinweis zur Versionsgeschichte:** Die Releaseverwaltung vermerkt, dass die Versionsnummern der
  KA-Spezifikationen zur besseren Adressierung angeglichen wurden, wobei die KA NM-SPEC als
  Referenz dient; die SST-SPEC wurde dabei auf 1.106 **zurückgesetzt**. Wer Versionsangaben aus
  Fremdquellen deutet, muss das kennen.
- **Gebraucht für:** O13, O14 (Änderungsreferenz, `txalisber`), die ALISE-Schnittstelle, alle
  Artikel unter `transaktionen/`.
- **Stichworte:** TX-Nachrichten, Referenzsysteme, KVP, DL, PV, AH, KOSE, Sperrmanagement

## Q55

**VDV-Kernapplikation – Aktionsmanagement für die Berechtigungsart EFS und Entsperrung von AFB (KA AktM-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q55_VDV-KA_AktM-SPEC_V1.12.0_2023-05-10.pdf` (150 Seiten)
- **Auswertung:** teilweise — Kap. 4.1.2.2, 4.2.2.3 und 4.2.4 ausgewertet (O5 und O20 geklärt);
  die Anwendungsfälle in Kap. 7 und die Datenstrukturen in Kap. 6 sind offen
- **Bedeutung:** Die Normquelle des Aktionsmanagements und damit der Kategorie
  [lexikon/aktionsmanagement.md](lexikon/aktionsmanagement.md).
- **Zwei Befunde:**
  - **Kap. 4.1.2.2, S. 28** nennt die Transaktionen, die die `berSynchronNummer` erhöhen, und die
    Rechenregeln für ihren Wert im Aktionsauftrag — einschließlich des Falls „um zwei größer“.
    Damit ist O5 geklärt.
  - **Kap. 4.2.2.3, S. 48** definiert den Aktionsfreigabeauftrag `TXAFREIBER` ausdrücklich und
    beschränkt ihn auf die Freigabe einer **Entsperrung**. **Kap. 4.2.4, S. 49** ordnet
    `TXAFREIMITBER` dem **Aktionsclearing** zu; der Aktionsfreigabeauftrag selbst wird mit `TXB`
    bestätigt. Damit ist O20 geklärt und die aus [Q39](#q39) abgeleitete Zuordnung zu korrigieren.
- **Stichworte:** Aktionsmanagement, Aktionsliste, `TXAFREIBER`, `TXAFREIMITBER`, Aktionsclearing, `berSynchronNummer`

## Q56

**VDV-Kernapplikation – Technisches Konzept Sicherheit (KA SEC-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q56_VDV-KA_SEC-SPEC_V1.12.0_2023-05-10.pdf` (121 Seiten)
- **Auswertung:** offen — Kapitelübersicht erfasst
- **Inhalt:** Kapitel u. a. 1 Einleitung · 2 Vertrauenswürdigkeit des Systems · 3 Kryptografische
  Verfahren und Mechanismen · 4 Key Management · 5 Sichere Datenübertragung · 6 Nutzermedium ·
  7 Sperrmanagement.
- **Gebraucht für:** O18 (Schlüsselnummern in den Key-Identifier-Bereichen), zusammen mit
  [Q76](#q76); die Artikel unter `sicherheit/`.
- **Stichworte:** Key Management, Kryptografie, Schlüsselhierarchie, CV-Zertifikat, Sperrmanagement

## Q57

**VDV-Kernapplikation – Spezifikation des SAM (KA SAM-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q57_VDV-KA_SAM-SPEC_V1.12.0_2023-05-10.pdf` (274 Seiten)
- **Auswertung:** offen — Kapitelübersicht erfasst
- **Inhalt:** „Spezifikation des SAM … mit Unterstützung der Anwendung der Multiberechtigung“.
  Kapitel u. a. 3 Allgemeines zu Datenstrukturen · 5 Daten im SAM · 6 SAM-Services und Prozesse ·
  7 Kommandos · 8 Standard-Kommandos · 9 Applikationsspezifische Kommandos.
- **Stichworte:** Secure Application Module, SAM-Kommandos, Schlüssel im SAM, Multiberechtigung

## Q58

**VDV-Kernapplikation – Funktionale Spezifikation KA-Sperrlistenmanagementsystem (KA KOSES-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q58_VDV-KA_KOSES-SPEC_V1.12.0_2023-05-10.pdf` (240 Seiten)
- **Auswertung:** offen — Kapitelübersicht erfasst
- **Inhalt:** Kapitel u. a. 1 Systemüberblick · 3 Geschäftsprozesse · 4 Nicht funktionale Aufgaben ·
  5 Nichtfunktionale Anforderungen. Normquelle für die Rolle KOSE und die Sperrlistenarten.
- **Achtung bei Fundstellen:** Dieses Dokument führt **keine Seitenzahl im Seitenfuß**. Die
  PDF-Seitenlage ist damit nicht gegen das Dokument prüfbar; Seitenangaben immer zusätzlich mit der
  Kapitelnummer absichern.
- **Stichworte:** KOSE, Sperrlistenmanagement, Sperrliste, Differenzsperrliste, Geschäftsprozesse

## Q59

**VDV-Kernapplikation – Spezifikation zur Multi-Berechtigungsausgabe (KA MultiBER-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q59_VDV-KA_MultiBER-SPEC_V1.12.0_2023-05-10.pdf` (69 Seiten)
- **Auswertung:** offen
- **Inhalt:** „Ergänzende Spezifikationen zur Performanceverbesserung bei der EFS Ausgabe –
  Spezifikation zur Multi-Berechtigungsausgabe“. Kapitel 2 spezifiziert die Ausgabe,
  **Kapitel 3 nennt den Ergänzungs- und Änderungsbedarf an den übrigen KA-Specs** — nützlich, um
  Abhängigkeiten zwischen den Dokumenten zu finden.
- **Gebraucht für:** `lexikon/berechtigungen/multiberechtigung.md`, dessen Titelzitat bisher aus
  [Q37](#q37) stammt.
- **Stichworte:** Multiberechtigung, EFS-Ausgabe, Performance

## Q60

**VDV-Kernapplikation – Spezifikation des Datenaustausches im Interoperabilitätsnetzwerk (KA ION-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q60_VDV-KA_ION-SPEC_V1.12.0_2023-05-10.pdf` (52 Seiten)
- **Auswertung:** offen — Kapitelübersicht erfasst
- **Inhalt:** Datenaustausch über die Zentrale Vermittlungsstelle und Zugang zu den zentralen
  Diensten. Kapitel u. a. 2 Architektur des ION · 3 Betriebskonzept · 6 Sicherung der
  Datenübertragung · **7 Nachrichtenformat** · 9 Komprimierung von Nachrichten.
- **Gebraucht für:** `lexikon/grundlagen/ion.md`, `zentrale-vermittlungsstelle.md`; das
  Nachrichtenformat ist für das Prüfwerkzeug einschlägig.
- **Stichworte:** ION, Zentrale Vermittlungsstelle, Nachrichtenformat, Komprimierung

## Q61

**VDV-Kernapplikation – Spezifikation des ION-Adapters (KA IONA-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q61_VDV-KA_IONA-SPEC_V1.12.0_2023-05-10.pdf` (29 Seiten)
- **Auswertung:** offen
- **Inhalt:** „Spezifikation des Lokalen Adapters für Protokollwandlung und WS-Security“ zum
  Anschluss bestehender Systeme an die Zentrale Vermittlungsstelle. Kapitel u. a. 2 Systemüberblick ·
  5 Sicherheit · 7 Zwischenspeichern von Korrelationsdaten.
- **Stichworte:** ION-Adapter, Protokollwandlung, WS-Security, Korrelationsdaten

## Q62

**VDV-Kernapplikation – Webservice Security Spezifikation (KA WSS-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q62_VDV-KA_WSS-SPEC_V1.12.0_2023-05-10.pdf` (23 Seiten)
- **Auswertung:** offen
- **Inhalt:** Kapitel u. a. 1 Systemüberblick · 3 Transportsicherung · **5 Rollenautorisierung** ·
  9 Key Management. Die Rollenautorisierung ist für die Frage einschlägig, ob die Rollencodes
  (KVP 1 … ALISE 31) KA-weit festgelegt sind.
- **Stichworte:** Webservice Security, Transportsicherung, Rollenautorisierung, Rollencodes

## Q63

**VDV-Kernapplikation – Schnittstelle KVP-Vertriebseinheit zu KVP-Personalisierungseinheit (KA PE-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q63_VDV-KA_PE-SPEC_V1.12.0_2023-05-10.pdf` (148 Seiten)
- **Auswertung:** offen
- **Inhalt:** Schnittstelle zwischen Vertriebseinheit (KVP-VE) und Personalisierungseinheit
  (KVP-PE) eines KVP-Terminals. Enthält eine Statuscode-Liste (Kap. 5).
- **Stichworte:** KVP-Terminal, Personalisierung, Vertriebseinheit, Statuscodes

## Q64

**VDV-Kernapplikation – Spezifikation Aktivierungsmedium (KA AM-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q64_VDV-KA_AM-SPEC_V1.12.0_2023-05-10.pdf` (50 Seiten)
- **Auswertung:** offen
- **Inhalt:** Aktivierungsmedium für VDV-KA-Sicherheitsmodule. Betrifft die Aktivierung von SAMs.
- **Stichworte:** Aktivierungsmedium, SAM-Aktivierung, Sicherheitsmodul, Keymanagement

## Q65

**VDV-Kernapplikation – Schnittstellenspezifikation SAM-Server (KA SAM-Server-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q65_VDV-KA_SAM-Server-SPEC_V1.12.0_2023-05-10.pdf` (44 Seiten)
- **Auswertung:** offen
- **Inhalt:** Schnittstellen des SAM-Servers für Phase 1 und Phase 2. Gegenstück zum SAM-Server in
  etiCORE ([Q50](#q50) nennt dort zwei OpenAPI-Schnittstellen) — für den Versionsvergleich nützlich.
- **Stichworte:** SAM-Server, Phase 1, Phase 2, Schnittstelle

## Q66

**VDV-Kernapplikation – Fremdsystemgesteuerte Ausgabe über ein KVP-Terminal (KA Fremdsystem-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q66_VDV-KA_Fremdsystem-SPEC_V1.12.0_2023-05-10.pdf` (23 Seiten)
- **Auswertung:** offen
- **Inhalt:** Schnittstellen für eine durch ein Fremdsystem gesteuerte Ausgabe von (((eTickets über
  ein KVP-Terminal.
- **Stichworte:** Fremdsystem, KVP-Terminal, Ausgabe, Schnittstelle

## Q67

**VDV-Kernapplikation – Spezifikation statischer Berechtigungen für 2D-Barcode-Tickets (KA STB-SPEC), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q67_VDV-KA_STB-SPEC_V1.12.0_2023-05-10.pdf` (98 Seiten)
- **Auswertung:** offen
- **Inhalt:** „Verwendung von Statischen Berechtigungen auf der Grundlage des KA-Referenz_EFS /
  KA-TLV-Referenz-EFS für 2D Barcode“. Die Normquelle zum VDV-Barcode. Nach [Q12](#q12) stehen in
  Tab. 3-1 die Kennung „VDV“, die Version und die Füllbyteregel — das ist jetzt am Original
  prüfbar.
- **Gebraucht für:** `lexikon/datenformate/vdv-barcode.md`,
  `lexikon/berechtigungen/statische-berechtigung.md`.
- **Stichworte:** Statische Berechtigung, VDV-Barcode, 2D-Barcode, Referenz-EFS, TLV-Referenz-EFS

## Q68

**VDV-Kernapplikation – Statische Berechtigung in IN/OUT-Systemen als CIBO-STB (KA STB-SPEC CIBO-STB), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q68_VDV-KA_STB-SPEC-CIBO-STB_V1.12.0_2023-05-10.pdf` (30 Seiten)
- **Auswertung:** offen
- **Inhalt:** Anlage 2 zu [Q67](#q67): Ergänzung zum Einsatz in IN/OUT-Systemen. Betrifft Check-in
  und Check-out mit statischer Berechtigung.
- **Stichworte:** CIBO, IN/OUT, Check-in, Check-out, statische Berechtigung

## Q69

**VDV-Kernapplikation – Kryptographischer Kopierschutz für statische Berechtigungen, VDV-Barcode mobile+ (KA STB-SPEC mobile plus), 1.12.0**

- **Dateien:** `QUELLEN/KA-1.12.0/spezifikationen/Q69_VDV-KA_STB-SPEC-mobile-plus_V1.12.0_2023-05-10_de.pdf`
  (46 Seiten) und `…_en.pdf` (43 Seiten, englische Fassung desselben Dokuments)
- **Auswertung:** offen
- **Inhalt:** Anlage 1 zu [Q67](#q67): Kopierschutz für statische Berechtigungen. Zusammen mit
  [Q81](#q81) (Motics) die Normquelle zum Kopierschutz des VDV-Barcodes.
- **Hinweis:** Die englische Fassung führt keine Seitenzahl im Seitenfuß; Fundstellen dort über das
  Kapitel angeben. Deutsche und englische Fassung haben **unterschiedliche Seitenzahlen** (46 zu
  43) — bei Fundstellen die Sprache mitangeben.
- **Stichworte:** mobile+, Kopierschutz, Motics, statische Berechtigung, VDV-Barcode

## Q70

**VDV-Kernapplikation – Anlage 1: Definition des TLV EFS (Anlage TLV EFS), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/anlagen/Q70_VDV-KA_Anlage-TLV-EFS_V1.12.0_2023-05-10.pdf` (22 Seiten)
- **Auswertung:** teilweise — Kap. 1, 2 und 2.5 ausgewertet (O21 geklärt), die Typ-Definitionen in
  Kap. 2.4 offen
- **Bedeutung:** Die Normquelle der TLV-Struktur, die das Lexikon bisher aus einer
  Herstellerdokumentation ([Q12](#q12)) rekonstruiert hat. Definiert die Tags **0x8A**
  (Transaktion Produktspezifischer Teil, Kap. 2, Tab. 2-1, S. 7), **0xC7** (Infotext), **0xDA**
  (Grundlegende Daten, Kap. 2.1), **0xDB** (Fahrgast, Kap. 2.2, mit den Kürzungsregeln für den
  Fahrgastnamen in Kap. 2.2.1), **0xD7** (Identifikationsmedium, Kap. 2.3), **0xDC** (Liste
  originärer Geltungsbereich, Kap. 2.4), **0xD9** (Liste alternativer Geltungsbereich, Kap. 2.5),
  **0xDD** (Linie, Kap. 2.6), **0xD8** (Linienfahrtnummer, Kap. 2.7), **0xDE** (PV_Container,
  Kap. 2.8) und **0xD6** (`sceId`, Kap. 2.9).
- **Zwei Befunde:**
  - **Kap. 1, Fußnote 1, S. 6:** Das Datenobjekt 0x85 ist **als primitives Tag kodiert**, obwohl
    darunter weitere TLV-Elemente liegen; das Dokument verlangt ausdrücklich, das beim Parsen zu
    berücksichtigen. Für das geplante Prüfwerkzeug eine zentrale Regel, und ein Kandidat für die
    offene Längenfrage in O6.
  - **Kap. 2.5, S. 18:** Der alternative Geltungsbereich ist der, den ein EFS außerhalb des
    Normalfalles hat, als Beispiel nennt das Dokument Schwachlastzeiten. Damit ist O21 geklärt.
- **Stichworte:** TLV EFS, Tags, produktspezifischer Teil, Geltungsbereich, Kürzungsregel, `sceId`

## Q71

**VDV-Kernapplikation – Anlage 2: Rahmenrichtlinie EFM, datenschutzrechtliche Grundanforderungen (Anlage Datenschutz), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/anlagen/Q71_VDV-KA_Anlage-Datenschutz_V1.12.0_2023-05-10.pdf` (7 Seiten)
- **Auswertung:** offen
- **Inhalt:** Anlage 2 zum Hauptdokument: datenschutzrechtliche Grundanforderungen.
- **Hinweis:** `lexikon/grundlagen/datenschutz.md` nennt bisher eine Fassung `v1121`; dies ist die
  Fassung zu 1.12.0. Beim Auswerten die Versionsangabe im Artikel prüfen.
- **Stichworte:** Datenschutz, Rahmenrichtlinie, Grundanforderungen, EFM

## Q72

**VDV-Kernapplikation – Verfahrensanweisung zur Prüfung von Transaktionen (KA TXx_Prüfungs-ANW), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/anwendungshinweise/Q72_VDV-KA_TXx-Pruefungs-ANW_V1.12.0_2023-05-10.pdf` (65 Seiten)
- **Auswertung:** offen
- **Bedeutung — für Stufe 2 das wichtigste Dokument dieses Abschnitts:** „Verfahrensanweisung zur
  Transaktionsprüfung in KA-RefererenzHGS“ (Schreibweise so im Original). Es beschreibt, **wie
  Transaktionen auf Anwendungsebene zu prüfen sind** — also genau die Aufgabe des geplanten
  Werkzeugs. In [BESCHAFFUNG.md](BESCHAFFUNG.md) als Inventarnummer 33 geführt.
- **Stichworte:** Transaktionsprüfung, Prüfregeln, Referenz-Hintergrundsystem, Anwendungsebene

## Q73

**VDV-Kernapplikation – Verfahrensanweisung zum Umgang mit TXTRANSABBRUCH (KA TXTRANSABBRUCH-ANW), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/anwendungshinweise/Q73_VDV-KA_TXTRANSABBRUCH-ANW_V1.12.0_2023-05-10.pdf` (22 Seiten)
- **Auswertung:** offen
- **Inhalt:** Umgang mit `TXTRANSABBRUCH` bei undefiniertem Abschluss einer Nutzermedium-Transaktion.
- **Stichworte:** `TXTRANSABBRUCH`, Transaktionsabbruch, undefinierter Abschluss

## Q74

**VDV-Kernapplikation – Verfahrensanweisung zum Umgang mit defekten und verloren gemeldeten Medien (KA Medien-ANW), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/anwendungshinweise/Q74_VDV-KA_Medien-ANW_V1.12.0_2023-05-10.pdf` (16 Seiten)
- **Auswertung:** offen
- **Inhalt:** Umgang mit defekten Medien in VDV-KA-EFM-Systemen. Betrifft Sperrung, Ersatzausgabe
  und das Aktionsmanagement.
- **Stichworte:** defektes Medium, Verlustmeldung, Ersatzausgabe, Sperrung

## Q75

**VDV-Kernapplikation – Verfahrensanweisung zur Vergabe von Produkt_IDs (KA Produkt_ID-ANW), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/anwendungshinweise/Q75_VDV-KA_Produkt-ID-ANW_V1.12.0_2023-05-10.pdf` (14 Seiten)
- **Auswertung:** offen
- **Inhalt:** Vergabe von `Produkt_ID`s in VDV-KA-EFM-Systemen. Normquelle zur Struktur der
  Produkt-ID, die [Q12](#q12) als 2 Byte Produktnummer plus 2 Byte Organisations-ID beschreibt.
- **Gebraucht für:** `lexikon/berechtigungen/produktnummer.md`, `produkt.md`.
- **Stichworte:** `Produkt_ID`, Produktnummer, Organisations-ID, Vergabeverfahren

## Q76

**VDV-Kernapplikation – Verfahrensanweisung zur Nutzung des AH-Transaktionsschlüssels (KA TR-Schlüssel-ANW), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/anwendungshinweise/Q76_VDV-KA_TR-Schluessel-ANW_V1.12.0_2023-05-10.pdf` (7 Seiten)
- **Auswertung:** offen
- **Inhalt:** Nutzung des AH-Transaktionsschlüssels (MK_TR bzw. K_TR) in KA-Terminals.
- **Gebraucht für:** O18, zusammen mit [Q56](#q56).
- **Stichworte:** Transaktionsschlüssel, MK_TR, K_TR, Applikationsherausgeber, Key Identifier

## Q77

**VDV-Kernapplikation – Verfahrensanweisung zur Nutzung der Applikations- oder Berechtigungssperre (KA App-Berr-Sperre-ANW), 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/anwendungshinweise/Q77_VDV-KA_App-Berr-Sperre-ANW_V1.12.0_2023-05-10.pdf` (4 Seiten)
- **Auswertung:** offen
- **Inhalt:** Wann die Applikationssperre und wann die Berechtigungssperre zu verwenden ist.
- **Stichworte:** Applikationssperre, Berechtigungssperre, Sperrmanagement

## Q78

**VDV-Kernapplikation – Release Letter zum KA-Release 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/release/Q78_VDV-KA_Release-Letter_V1.12.0_2023-05-10.pdf` (42 Seiten)
- **Auswertung:** offen
- **Bedeutung:** Nennt die zum Release 1.12.0 gehörenden Dokumente mit Version und beschreibt die
  Änderungen gegenüber dem Vorgänger. Damit die **Bezugsliste für den Umfang dieses Abschnitts**
  und das Gegenstück zum etiCORE-Release-Letter [Q43](#q43).
- **Gebraucht für:** `lexikon/grundlagen/versionen.md`, `ka-spezifikationen.md`.
- **Stichworte:** Release 1.12.0, Dokumentenliste, Änderungen, Versionsnachweis

## Q79

**VDV-Kernapplikation – Release Notes Schnittstellen 1.11.1**

- **Datei:** `QUELLEN/KA-1.12.0/release/Q79_VDV-KA_Release-Notes-Schnittstellen_1.11.1.pdf` (18 Seiten)
- **Auswertung:** offen
- **Inhalt:** Release Notes zu den **Schnittstellen** in Version 1.11.1 — also zu den XML-Schemata
  und WSDL, die das Lexikon für den ALISE-Decoder braucht. Herausgeber: VDV eTicket Service GmbH
  & Co. KG, Köln.
- **Achtung:** Abweichende Version (**1.11.1**, nicht 1.12.0) und **kein Seitenfuß**. Die
  Extraktion streut Sprachmarken (`en-US`) in den Text, teils innerhalb eines Wortes —
  Suchmuster und Zitate daran ausrichten.
- **Stichworte:** Schnittstellen, Release Notes, 1.11.1, XML-Schemata, WSDL

## Q80

**VDV-Kernapplikation – Anlage 2 zum (((eTicket-Teilnahmevertrag: Migrationsszenarien in den Ausbauvarianten, 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/release/Q80_VDV-KA_Anlage-2-Migrationsszenarien_V1.12.0_2023-05-10.pdf` (120 Seiten)
- **Auswertung:** offen
- **Inhalt:** Migrationsszenarien in den Ausbauvarianten des (((eTicket Deutschland. Anlage 2 zum
  Teilnahmevertrag und damit das Gegenstück zu [Q25](#q25), dessen Kap. zu den Ausbauvarianten
  (PDF-S. 159) die Varianten 1 bis 3 auflistet.
- **Gebraucht für:** `lexikon/grundlagen/ausbauvarianten.md`, O4 (Namensraum-Version).
- **Stichworte:** Migration, Ausbauvarianten, Teilnahmevertrag, (((eTicket Deutschland

## Q81

**Motics – Verification of Copy Protection and Entitlement Data, 1.12.0**

- **Datei:** `QUELLEN/KA-1.12.0/spezifikationen/Q81_VDV-KA_Motics-Copy-Protection-Verification_V1.12.0.pdf` (21 Seiten)
- **Auswertung:** offen
- **Inhalt:** Englischsprachiges Spezifikationsdokument, Autor Dr. Joseph Lutgen / VDV ETS. In
  [Q37](#q37) als Position 11 der Prüfgrundlagen geführt („Motics — Verification of Copy Protection
  and Entitlement Data“), hier im Original.
- **Achtung bei Fundstellen:** kein Seitenfuß, Lage nicht gegenprüfbar.
- **Stichworte:** Motics, Kopierschutz, Prüfung, mobile+, statische Berechtigung

---

# 3. etiCORE

Die Quellen zur kommenden Version des Standards. **Aussagen daraus gelten nicht ohne Prüfung für
die KA 1.x**, auf die sich dieses Lexikon vorrangig bezieht, und sind entsprechend zu kennzeichnen.

**Zum Verhältnis der Versionen:** Der erfasste Stand ist **3.0.0-rc.6** ([Q43](#q43), [Q49](#q49)
bis [Q51](#q51)). Die am 20.10.2026 beschafften PDF sind überwiegend **3.0.0-rc.1** und damit fünf
Release-Kandidaten älter. Sie taugen zum Vergleich und für Prosa, die es in rc.6 nur im Modell
gibt, **niemals** dazu, eine rc.6-Aussage zu überschreiben. Beispiel: In rc.1 heißt die Komponente
noch `SPEC-ASM`, in rc.6 `ESH`.

**Keines der etiCORE-Dokumente führt eine Seitenzahl im Seitenfuß.** Die PDF-Seitenlage ist damit
nicht gegen das Dokument prüfbar — anders als bei den KA-Spezifikationen in Abschnitt 2. Zitiert
wird hier über **Kapitel- oder Elementnamen**; wo eine PDF-Seite angegeben wird, ist sie als
`PDF-S.` zu kennzeichnen und bleibt eine Angabe über die Datei, nicht über das Dokument.

## Q43

**VDV eTicket Service – etiCORE Release Letter, Specification Artefacts Overview, 3.0.0-rc.6**

- **Datei:** `QUELLEN/Q43_VDV-eTS_etiCORE-Release-Letter_v3.0.0-rc.6.pdf` (37 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** teilweise (Inhaltsverzeichnis und Kap. 2.1 geprüft)
- **Stand:** Version 3.0.0-rc.6, **24.11.2025**, Autor Wilk Hoffmann
- **Inhalt — das etiCORE-Gegenstück zum KA-Inventar aus [Q25](#q25):**
  - **Kap. 1 Änderungshistorie** mit je einem Abschnitt für die Release-Kandidaten 1 bis 6, darunter „Aufteilung Basispakete, optionale Anwendungsfälle“, „Neue Spezifikationen“, „Änderungen Schnittstellen“ und „Installation des lokalen Spezifikationsmodells“.
  - **Kap. 2 Übersicht der Spezifikationsartefakte** (ab PDF-S. 22), Kap. 2.1 „Spezifikationsmodell und daraus exportierte Dokumente“ (PDF-S. 23), Kap. 2.2 „Weitere Spezifikationsdokumente“ (PDF-S. 25).
  - Nennt die **öffentlich erreichbare Adresse des Spezifikationsmodells**, siehe [Q49](#q49).
- **Bedeutung:** jüngste Primärquelle der Sammlung und einzige Quelle zum Stand von etiCORE als KA 3.
- **Technischer Hinweis:** Die Seiten ab 22 sind CID-kodiert; `tools/pdftext.py` wertet dafür die ToUnicode-CMaps aus. Die Sprachmarker `de-DE` und `en-GB` aus der Auszeichnung stehen im extrahierten Text und sind beim Zitieren zu entfernen.
- **Stichworte:** etiCORE, KA 3, Release-Kandidaten, Spezifikationsartefakte, Spezifikationsmodell

## Q44

**VDV eTicket Service – etiCORE Release Letter 3.0.0-rc.1**

- **Datei:** `QUELLEN/Q44_VDV-eTS_etiCORE-Release-Letter_v3.0.0-rc.1.pdf` (14 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** offen
- **Inhalt:** ältere Fassung des Release Letters. Erlaubt zusammen mit [Q43](#q43) den Vergleich, was zwischen rc.1 und rc.6 hinzukam.
- **Stichworte:** etiCORE, Versionsvergleich

## Q49

**VDV eTicket Service – etiCORE Specification (Spezifikationsmodell, online)**

- **URL:** https://modell.eticket-deutschland.de/LATEST/EA/index.html — die jeweils aktuelle Fassung; versionierte Einstiege wie `…/3.0.0-rc.6/EA/` existieren ebenfalls
- **Datei:** `QUELLEN/Q49_etiCORE-Spezifikation_3.0.0-rc.6/` — lokale Gesamtkopie der Version **3.0.0-rc.6** (30.605 Seiten): `html/` Originale, `md/` Markdown-Umwandlung. Sie enthält auch die Unterlagen zu [Q50](#q50) und [Q51](#q51). Nutzungsbedingungen als `nutzungsbedingungen_de.txt` und `nutzungsbedingungen_en.txt` daneben.
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** teilweise — Glossar gelesen, Zugehöriges zum Aktionsmanagement in [Q50](#q50) ausgewertet; der Modellbaum `EA/EARoot/` (Layer 1 bis 5) ist noch nicht durchgearbeitet
- **Fundstelle:** Das Modell hat keine Kapitelnummern. Zitiert wird mit dem **Paket- oder Elementnamen** und der Versionsangabe, etwa „Glossary, Eintrag *Ordered action*, 3.0.0-rc.6“.
- **Version:** **3.0.0-rc.6 ist ein Release Candidate**, keine endgültige Fassung. Aussagen daraus sind bei Erscheinen der Endfassung zu prüfen.
- **Rechte:** Die Nutzungsbedingungen (Punkt 1) gewähren ein „nicht ausschließliches, nicht übertragbares, unentgeltliches und zeitlich unbegrenztes Nutzungsrecht“. Die Kopie bleibt deshalb **lokal**; ins Repository gehören nur kurze Exzerpte mit Fundstelle.
- **Inhalt — potenziell die wichtigste öffentliche Quelle des Projekts:** Ein HTML-Export des etiCORE-Spezifikationsmodells aus Enterprise Architect, Titel „etiCORE Specification“. Die oberste Ebene hat 18 Pakete:
  - Introduction · **Role Model** · Layer 1 und 2 (Workflows und Basic Processes in BPMN) · Layer 3 (Use Cases in UML) · **Layer 4 (System Components and Interfaces in UML)** · Layer 5 (Implementation Details in UML) · **ION Specification** · General Specification Parts for Terminals · Spec EUI, MPI, ESI · SAM-Server · User Manual · **Types** · **Interfaces** · **Glossary** · Operational parameters · List of References
  - Allein unter „Types“ hängen über 100 Unterpakete.
- **Einschränkung, die zu beachten ist:** Das Modell beschreibt **etiCORE, also KA Version 3** — nicht die KA 1.x, auf die sich dieses Lexikon vorrangig bezieht. Aussagen daraus gelten **nicht ohne Prüfung** für KA 1.x und sind entsprechend zu kennzeichnen.
- **Erschließung:** Der Export verschachtelt Pakete tief. Die lokale Kopie macht das Abrufen einzelner Seiten überflüssig; `md/EA/glossary.md` (englisch, rund 30 KB) ist der schnellste Einstieg.
- **Das Glossar nennt** unter anderem: *ALISE* = „Action List Service“; *Ordered action* (OA) = „an action to be done on a user medium“, im Produktowner-System bestellt und über Aktionslisten an ausführende CCP verteilt; *ESH* = „E-Ticket Security Hub. The successor to the ASM“; *CRE* = Central Routing Engine; *EO* = Entitlement owner; *TO* = Terminal Operator; *UMO* = User Medium Application Instance Owner; *Level-3* = Produktivumgebung. *etiCORE* sei der Name der neuen Version des deutschen eTicket-Standards.
- **Stichworte:** etiCORE, Spezifikationsmodell, Datentypen, Codelisten, Schnittstellen, Rollenmodell, ION

## Q50

**VDV eTicket Service – etiCORE Interfaces Documentation (WSDL und XSD)**

- **Datei:** `QUELLEN/Q49_etiCORE-Spezifikation_3.0.0-rc.6/md/` — Einstieg `index-interfaces.md`; je Schnittstelle ein Ordner (`PO-Action-Management/`, `CCP-Action-Ordering/`, `CCP-Action-Execution/` u. a.)
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** teilweise — Aktionsmanagement (PO, CCP-Ordering, CCP-Execution), Hotlist und ESH sowie **alle 203 Fehler- und Warncodes** ausgewertet; CRE, SO, die Static-Entitlement-Erweiterungen und die XSD-Datentypen sind offen
- **Stand:** Version **3.0.0-rc.6** (Release Candidate), geladen am 2026-10-20
- **Fundstelle:** Dateiname und Element- oder Typname, etwa „`po-oa-management-messaging_xsd`, Element `cancelOrder`“.
- **Rechte:** wie [Q49](#q49) — Kopie lokal, im Repository nur kurze Exzerpte ([exzerpte/Q50.md](exzerpte/Q50.md)).
- **Inhalt:** Neunzehn Schnittstellen — zwölf WSDL (ESH, CCP mit den Erweiterungen Action Execution, Action Ordering und Static Entitlement, CRE, Hotlist, PO mit Action Management und Static Entitlement, SO mit Static Entitlement), fünf weitere XSD-Gruppen (EUI, ESI, MPI, Terminal, Media Shipment List) und zwei OpenAPI-Schnittstellen des SAM-Servers.
  - Die Namensräume haben die Form `https://eticore.org/<schnittstelle>/messaging/3`.
  - Das WSDL `po-oa-management` nennt als Rolle (dezimal) die **3**.
  - Das Aktionsmanagement umfasst die Aufträge `orderEntitlementIssuance`, `…Blocking`, `…Unblocking`, `…Termination`, `orderGroup` (seit 3.0.0) und `cancelOrder`, den Abruf `getActionList`, `getIncrementalActionList` und `verifyActionListUpdatedViaIncrements` sowie Meldungen wie `notifyOrderedEntitlementIssued`.
  - Rund 30 Fehlercodes mit den Präfixen `E_POOAM_`, `E_CO_`, `E_PO_` und `E_CCP_` sind benannt.
- **Wertvoll für dieses Lexikon:** Die XSDs tragen zu rund 850 Elementen und Typen einen Vermerk `meta:old`, der den **Namen in der KA 1.x mit Namensraum** angibt (etwa `http://vdv/ka/alise/2`). Das ist die bislang einzige öffentliche Verbindung zwischen den KA-1.x-Nachrichten und ihren etiCORE-Nachfolgern. Ausgewertet in [exzerpte/Q50.md](exzerpte/Q50.md).
- **Einschränkung:** Das Modell beschreibt **etiCORE**. Die `meta:old`-Angaben belegen die Abbildung der Namen, nicht, dass sich Inhalt und Semantik in KA 1.x genauso verhalten. Und: Felder wie `amAuftragsTyp` tauchen als Altname **nicht** auf; die Aktionstypen sind in etiCORE offenbar nicht als Codeliste, sondern als eigene Operationen modelliert (abgeleitet).
- **Stichworte:** WSDL, XSD, Aktionsmanagement, `meta:old`, Altbezeichner, ALISE, Hotlist, Fehlercodes

## Q51

**VDV eTicket Service – etiCORE ASN.1 Data Type Description**

- **Datei:** `QUELLEN/Q49_etiCORE-Spezifikation_3.0.0-rc.6/md/asn.1/` — Einstieg `index-asn1.md`
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** vollständig — alle 220 Typen sind einem Artikel zugeordnet ([exzerpte/Q51.md](exzerpte/Q51.md)); die Beschreibungstexte sind nach Typenkreisen zusammengefasst
- **Stand:** Version **3.0.0-rc.6**, geladen am 2026-10-20
- **Fundstelle:** Modul und Typname, etwa „`ste`, Typ `StaticElectronicTicketParameters`“.
- **Rechte:** wie [Q49](#q49).
- **Inhalt:** Neun ASN.1-Module — Electronic Ticket (`et`), Payment, Static Entitlement (`ste`), Tariff, User Medium (`user-medium`), Common, CV Certificate (`cv-certificates`), Mobile Ticketing Crypto Service (`motics`) und Secure Application Module (`sam`). Je Typ stehen Tag (hexadezimal), Art (`SEQUENCE`, `CHOICE`, `ENUMERATED` u. a.), eine Feldtabelle mit Tag, Elementname, Typname, Optional-Kennzeichen und Beschreibung sowie bei Aufzählungen die Werte mit Bezeichnern. Das Modul `common` enthält 44 Typen.
- **Bedeutung:** maschinenlesbare Grundlage für Tags und Aufzählungen im Chip- und Barcode-Bereich — soweit etiCORE betroffen. Verweise auf EN 1545-1:2015 bei `DeviceTypeCode` und `LocationTypeCode`.
- **Einschränkung:** etiCORE-Typen, nicht die KA-1.x-Strukturen. Gleiche Namen bedeuten nicht gleiche Kodierung.
- **Stichworte:** ASN.1, Tags, Static Entitlement, User Medium, Aufzählungen, CV-Zertifikat, MOTICS

## Q82

**VDV eTicket Service – etiCORE-Spezifikationssatz 3.0.0-rc.1 (13 Dokumente, Sammelnummer)**

- **Ordner:** `QUELLEN/etiCORE-3.0.0-rc.1/` — alle Dateien mit dem Präfix `Q82_`
- **Typ:** Primär · **Herkunft:** lokal (Download aus dem ASM-Tool) · **Auswertung:** offen
- **Stand:** Version 3.0.0-rc.1, Dokumente zuletzt geändert am 28./29.09.2023
- **Warum eine Sammelnummer:** Diese 13 Dokumente sind durch **3.0.0-rc.6** überholt, das als
  [Q49](#q49) bis [Q51](#q51) vollständiger erfasst ist (Spezifikationsmodell, Schnittstellen,
  ASN.1-Typen). Einzelne Q-Nummern würden eine Zitierfähigkeit suggerieren, die sie für
  Standardaussagen nicht haben. Sie bleiben als **Versionsvergleich** erhalten: Wo rc.6 eine
  Aussage nur im Modell führt, kann die rc.1-Prosa den Hintergrund liefern.
- **Fundstelle:** Dateiname, Kapitel und Version, etwa „`Q82_etiCORE_SPEC-ION_v3.0.0-rc.1.pdf`,
  Kap. 4“. Die Angabe der Version ist hier **Pflicht**, damit nicht später eine rc.1-Aussage für
  den aktuellen Stand gelesen wird.
- **Inhalt:**
  - `Release-Letter` (14 S.) — weitgehend grafisch, Textextraktion ergibt kaum etwas; inhaltlich
    dasselbe Dokument wie [Q44](#q44), eine andere Ausfertigung derselben Version
  - `User-Manual` deutsch (58 S.) und englisch (59 S.)
  - `Glossar` (100 S.) — „Main glossary for the specifications of … and (((etiCORE“, das
    zweisprachige Gegenstück zu [Q02](#q02) in der rc.1-Fassung
  - `SPEC-ION` (279 S.) — Interoperable Network
  - `SPEC-CCP-RS` (209 S.) und `SPEC-CCP-RT` (177 S.) — Customer Contract Partner, Referenzsystem
    und Referenzterminal
  - `SPEC-PO-RS` (154 S.) — Product Owner Reference System
  - `SPEC-SO-RS` (106 S.) und `SPEC-SO-RT` (88 S.) — Service Operator
  - `SPEC-Hotlist` (46 S.) · `SPEC-CRE` (15 S.) — Central Routing Engine · `SPEC-ASM` (20 S.) —
    Application and Security Management, in rc.6 als **ESH** geführt
- **Rechte:** nicht öffentlich, nur Verweis und Kurzexzerpt.
- **Stichworte:** etiCORE, 3.0.0-rc.1, Versionsvergleich, CCP, PO, SO, ION, Hotlist, CRE, ASM

## Q83

**VDV eTicket Service – etiCORE User Medium Specification (SPEC-UM), 1.0.5-rc.1**

- **Datei:** `QUELLEN/etiCORE-eigenstaendig/Q83_etiCORE_SPEC-UM_v1.0.5-rc.1.pdf` (170 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** offen
- **Stand:** Version 1.0.5-RC.1, Autor Dr. Joseph Lutgen / VDV ETS, zuletzt geändert 28.09.2023
- **Warum eine eigene Nummer:** Dieses Dokument trägt eine **eigene Versionslinie** (1.0.5), nicht
  3.0.0-rc.1. Es ist damit nicht im selben Sinn überholt wie die Dokumente unter [Q82](#q82), und
  es ist mit 170 Seiten die ausführlichste vorliegende Beschreibung des Nutzermediums unter
  etiCORE. Ob 1.0.5-rc.1 der aktuelle Stand ist, ist **nicht geprüft** — der erfasste
  rc.6-Satz ([Q49](#q49)) enthält kein Dokument dieses Namens.
- **Gebraucht für:** die Artikel unter `lexikon/medien/`, Gegenstück zu [Q53](#q53).
- **Rechte:** nicht öffentlich, nur Verweis und Kurzexzerpt.
- **Technischer Hinweis:** Die Extraktion streut die Sprachmarken `en-GB` und `en-US` in den Text,
  teils innerhalb eines Wortes — Suchmuster und Zitate daran ausrichten.
- **Stichworte:** User Medium, Nutzermedium, etiCORE, Applikationsinstanz

## Q84

**VDV eTicket Service – etiCORE Secure Application Module Specification (SPEC-SAM), 1.0.8**

- **Datei:** `QUELLEN/etiCORE-eigenstaendig/Q84_etiCORE_SPEC-SAM_v1.0.8.pdf` (108 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** offen
- **Stand:** Version 1.0.8, Autor Dr. Joseph Lutgen / VDV ETS, zuletzt geändert 28.09.2023
- **Inhalt:** Das SAM unter etiCORE. Eigene Versionslinie, siehe die Begründung bei [Q83](#q83).
  Gegenstück zu [Q57](#q57) für die KA 1.x.
- **Rechte:** nicht öffentlich · **Technischer Hinweis:** Sprachmarken wie bei [Q83](#q83).
- **Stichworte:** SAM, Secure Application Module, etiCORE, Schlüssel

## Q85

**VDV eTicket Service – etiCORE SAM Individualisation Specification (SPEC-SAM-I), 1.1.6**

- **Datei:** `QUELLEN/etiCORE-eigenstaendig/Q85_etiCORE_SPEC-SAM-I_v1.1.6.pdf` (23 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** offen
- **Stand:** Version 1.1.6, Autoren Gero Galka / eSol GmbH und Dr. Joseph Lutgen / VDV ETS
- **Inhalt:** Individualisierung von SAMs. Gegenstück zu [Q64](#q64) (Aktivierungsmedium) für die
  KA 1.x.
- **Rechte:** nicht öffentlich · **Technischer Hinweis:** Sprachmarken wie bei [Q83](#q83).
- **Stichworte:** SAM-Individualisierung, Personalisierung, etiCORE

## Q86

**VDV eTicket Service – etiCORE Cipher Suite Specification (SPEC-CipherSuite), 1.0.1**

- **Datei:** `QUELLEN/etiCORE-eigenstaendig/Q86_etiCORE_SPEC-CipherSuite_v1.0.1.pdf` (18 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** offen
- **Stand:** Version 1.0.1, Autor Dr. Joseph Lutgen / VDV ETS
- **Inhalt:** Die kryptografischen Verfahren der 2. Generation der Sicherheitsinfrastruktur
  (2GSI). Gegenstück zu Kap. 3 von [Q56](#q56).
- **Gebraucht für:** die Artikel unter `lexikon/sicherheit/`, insbesondere zum Übergang 1GSI auf
  2GSI, den [Q42](#q42) datiert.
- **Rechte:** nicht öffentlich · **Technischer Hinweis:** Sprachmarken wie bei [Q83](#q83).
- **Stichworte:** Cipher Suite, Kryptografie, 2GSI, etiCORE

## Q87

**VDV eTicket Service – etiCORE M2M Certificates Specification (SPEC-M2MC), 2.0.2**

- **Datei:** `QUELLEN/etiCORE-eigenstaendig/Q87_etiCORE_SPEC-M2MC_v2.0.2.pdf` (19 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** offen
- **Stand:** Version 2.0.2, Autor Dr. Joseph Lutgen / VDV ETS
- **Inhalt:** Maschine-zu-Maschine-Zertifikate. Betrifft die Nachfolge der CV-Zertifikate der
  KA 1.x.
- **Rechte:** nicht öffentlich · **Technischer Hinweis:** Sprachmarken wie bei [Q83](#q83).
- **Stichworte:** M2M-Zertifikat, CV-Zertifikat, PKI, etiCORE

## Q88

**VDV eTicket Service – etiCORE Media PKI Specification (SPEC-Media-PKI), 1.0.0**

- **Datei:** `QUELLEN/etiCORE-eigenstaendig/Q88_etiCORE_SPEC-Media-PKI_v1.0.0.pdf` (10 Seiten)
- **Typ:** Primär · **Herkunft:** lokal · **Auswertung:** offen
- **Stand:** Version 1.0.0, Autor Dr. Joseph Lutgen / VDV ETS
- **Inhalt:** Die PKI für Nutzermedien unter etiCORE.
- **Rechte:** nicht öffentlich · **Technischer Hinweis:** Sprachmarken wie bei [Q83](#q83).
- **Stichworte:** Media PKI, Nutzermedium, Zertifikate, etiCORE

---

# 4. Projekt- und Verbundspezifikationen

> **Grundregel:** Alle Aussagen aus diesem Abschnitt sind **verbundspezifisch** und müssen im Artikel als solche gekennzeichnet werden. Codewerte können bei anderen Verbünden abweichen.

## Q05

**RMV – vHGS Pflichtenheft PH 05 Systemspezifikation, Anhang 1: RMV-EFS**

- **Datei:** `QUELLEN/Q05_RMV_PH05-A1_RMV-EFS_v1.6_2019-04-15.pdf` (39 Seiten)
- **Typ:** Projekt · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** offen
- **Stand:** v1.6, 15.04.2019, Cubic Transportation Systems / eTicket RheinMain
- **Inhalt (laut Sekundärangabe, noch nicht am Dokument verifiziert):** Datenstruktur RMV-EFS und Codelisten, darunter die **berStatus-Codes** 5 = zurückgenommen, 7 = aktiv/entsperrt, 8 = neu/nicht aktiv, 19 = gesperrt (dort Abschnitt 2.1, S. 8); Transaktionstyp (Abschnitt 4.4.4); Aktionsmanagement (Abschnitt 5.4.6); TXABER-Inhalte; BerechtigungTarifbereichZusatz.
- **Stichworte:** berStatus, RMV-EFS, produktspezifischer Teil
- **Priorität:** **P1 auswerten.** Dies ist der einzige Beleg für die berStatus-Codes, die bisher überall nur zitiert werden.
- **Rechte:** Cubic Transportation Systems, vermutlich „Vertraulich“ — prüfen.
- **URL (tot, 404):** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_24_EFM_Anh_1a_vHGS_PH05-A1_RMV-EFS_v1.6_190415_MVU_200122.pdf

## Q06

**RMV – vHGS Pflichtenheft PH 06-02 Schnittstellenspezifikation Terminalmanagementsysteme (TMS)**

- **Datei:** `QUELLEN/Q06_RMV_PH06-02_Terminalmanagementsysteme_v2.3_2018-11-09.pdf` (46 Seiten)
- **Typ:** Projekt · **Herkunft:** lokal · **Auswertung:** teilweise — Kap. 1.2.2, 2.1.5, 3.2, 4.10 sowie die Fußnoten 1 und 7 sind am Dokument selbst geprüft
- **Stand:** v2.3, 09.11.2018, Cubic Transportation Systems
- **Inhalt — ergiebigste Quelle für Nachrichten, Codes und Abläufe:**
  - KA-Rollen und Datenflüsse für Sperr- und Aktionsmanagement (Kap. 1.2, 1.2.2)
  - Ausschluss der Abo-Ausgabe an Offline-Verkaufsgeräten (Kap. 1.1)
  - **Transaktionstypen 37 / 38 / 39** = Ausgabe, Entsperrung, Rückgabe EFS über Aktionsliste (Kap. 2.1.5, Fußnote 1)
  - KVP-Aktionen über Aktionsliste: Berechtigung-Ausgabe, -Rücknahme, -Entsperrung (Kap. 2.1.5)
  - proprietäre TX-Codes 252–254 für das Schlüsselmanagement
  - Sperrlisten TXSLNM / TXSLK / TXSLOS (ab KA 1.3.0 als *RESP-Varianten)
  - Kontrollnachweise TXEBER, TXKNAWA / TXKNAWB, TXKNAWDM
  - Aktionsliste TXAML, Nachweise TXABER / TXRBER / TXSNAWB (Kap. 4.3, 4.3.1)
  - Upload und Paket-Quittung (TXA / TXB), MAC-Prüfung, Ablehnungsdatensatz (Kap. 3.1)
  - **Rollencodes** in TX_BASE, dargestellt je Anwendungsfall (Kap. 4.10): KVP = 1, DL = 2, PV = 3, AH = 4, KOSE = 5. Der Rollencode für den AH wurde laut Versionshistorie (v2.2, 16.03.2018) „von 5 auf 4 korrigiert“.
  - **Rollencode 31 (ALISE) — wichtige Einschränkung** (Fußnote 7, PDF-S. 39): In der Schnittstellenversion KA 1.1.07 wurde 31 alternativ akzeptiert. Ab KA 1.3.0 ist 31 „für einen aus dem PVS ausgelagerten eigenständigen zentralen ALISE-Server reserviert“; ist ALISE in das PVS integriert, ist die **Rolle 3** zu verwenden. In der TMS-Schnittstellenversion KA 1.3.0 ist für Transaktionen aus Aktionsausführungen **zwingend der Rollencode 3** zu verwenden.
  - Multiberechtigungen ab KA 1.3.0: TXAMBER, TXEMBER, TXRMBER
  - Differenzlisten und terminal- bzw. terminalgruppenspezifische Aktionslisten sind spezifiziert, werden aber „zum Systemstart des eTicket RheinMain nicht eingesetzt“ (Kap. 2.1.5)
  - CV-Zertifikat-Keytypes 1–7
  - Duplikaterkennung über die IONTransaktion_ID (Kap. 5.3)
  - Kodierung von Nullwerten: Leerzeichen 0x20 bei PrintableString, 0xFF bei OrtsTyp (Kap. 5.2)
  - MAC-Bildung über Transaktionsdaten, Kennzeichnung nachträglich geänderter Felder (Kap. 5.1.2)
  - Transaktionskopf TX_BASE mit optionalen Signaturfeldern `transSignatur…` (Kap. 5.4)
  - täglicher Zyklus: Sperr- und Aktionslisten werden einmal täglich erstellt (Kap. 3.2)
  - Datenschutzvorgaben für TXEBER; mobile Kontrolle ohne SAM (Sichtkontrolle)
- **Stichworte:** sehr ergiebig — **eigener Exzerptdurchgang, P1**
- **Technischer Hinweis:** Das PDF mischt Zeichenkodierungen. Teile des Textes — vor allem Passagen in Anführungszeichen — kommen nur mit `tools/pdftext.py --shift=29` lesbar heraus. Zitate daraus gegen beide Varianten prüfen.
- **Rechte:** Titelseite: „Cubic Transportation Systems (Deutschland) GmbH, **Vertraulich**“. Nur kurze Exzerpte mit Fundstelle.
- **URL (tot, 404):** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_24_EFM_Anh_2_vHGS_PH06-02_TeminalMgmtSys_v2.3_181109_MVU_211020.pdf

## Q07

**RMV – Statische Berechtigung RMV-EFS, Spezifikation Datenlayout**

- **Datei:** `QUELLEN/Q07_RMV_Statische-Berechtigung-RMV-EFS_v1.9_2021-08-04.pdf` (17 Seiten)
- **Typ:** Projekt · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** offen
- **Stand:** v1.9, 04.08.2021
- **Inhalt:** Datenlayout statischer Berechtigungen (Barcode bzw. Sichtausweis) im RMV.
- **Technischer Hinweis:** Das PDF verwendet eine verschobene Zeichenkodierung. Textextraktion mit `tools/pdftext.py --shift=29`.
- **Stichworte:** statische Berechtigung, Barcode, VDV-Barcode
- **URL (tot, 404):** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_24_EFM_Anh_8_StatBer_RMV-EFS_v1.9_210804_MVU_211020.pdf

## Q08

**RMV – EFM-Integration vHGS**

- **Datei:** `QUELLEN/Q08_RMV_EFM-Integration-vHGS_v2.7.0_2021-11-05.pdf` (10 Seiten)
- **Typ:** Projekt · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** offen
- **Stand:** v2.7.0, 05.11.2021
- **Inhalt:** Integrationsleitfaden: Vorgehen, Ansprechpartner, Basistest, SAM-Anbindung, vHGS-Arbeitsplatz, pVKS-Verkauf, Chipkarten- und Papierfahrkartendrucker, Terminalanbindung.
- **Stichworte:** Abo-Verwaltung, pVKS, vHGS, Prozessketten, Zulassung
- **URL (tot, 404):** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_25_EFM_Integration_vHGS_v2.7.0_20211105_MVU_211105.pdf

## Q09

**AVV / KCD NRW – Abbildung und Kontrolle des AVV-Tarifs**

- **Datei:** `QUELLEN/Q09_KCD-NRW_Abbildung-Kontrolle-AVV-Tarif_v1.1_2017-10-13.pdf` (22 Seiten)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** offen
- **Stand:** Version 1.1, 13.10.2017, Aachener Verkehrsverbund
- **Inhalt:** Abbildung eines Verbundtarifs in der KA und die zugehörige Kontrolllogik.
- **Stichworte:** Tarifabbildung, Kontrolle, Produktdefinition
- **URL:** https://www.kcd-nrw.de/fileadmin/03_KC_Seiten/KCD/Downloads/Technische_Dokumente/20171013_Abbildung_und_Kontrolle_des_AVV-Tarifs_Version_1.1.pdf

## Q10

**KCD NRW – Technische Anforderung Deutschlandticket**

- **Dateien:**
  - `QUELLEN/Q10c_KCD-NRW_Technische-Anforderung-Deutschlandticket_V1.9.pdf` (17 Seiten, 16.08.2024) — **aktuellste Fassung, diese zitieren**
  - `QUELLEN/Q10a_…_V1.5.pdf` (15 Seiten, 15.03.2023)
  - `QUELLEN/Q10b_…_V1.4.pdf` (14 Seiten, 31.01.2023)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** offen
- **Inhalt:** „Technische Beschreibung der Ausgabe und Kontrolle“ des Deutschlandtickets. Die drei Fassungen erlauben einen **Versionsvergleich**, der für Artikel zur Produktabbildung nützlich ist.
- **Zitierweise:** immer mit Version, z. B. `Q10c, V1.9, S. 7`.
- **Stichworte:** Deutschlandticket, Produktabbildung, Barcode-Kontrolle
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/Technische_Anforderung_Deutschlandticket_V1.9.pdf

## Q11

**LVB – Bewerberaufgabe Spezialist Vertriebssoftware EFM**

- **Datei:** **nicht im Repository** (liegt nur lokal beim Autor vor)
- **Typ:** Projekt · **Herkunft:** lokal · **Auswertung:** vollständig (ausgewertet in [Quellen_LBV.md](Quellen_LBV.md))
- **Stand:** 13.10.2026
- **Inhalt:** Beispiel einer echten KA-Transaktion `txalisber` (Namespace `http://vdv/ka/alise/2`), Produkt „ABO Azubi“, drei reale Org-IDs in den Rollen KVP, PV und Produktschlüsselorganisation, Transaktionstyp 37, Auftragstyp 13, berStatus 7, berSynchronNummer 1. Die konkreten Werte stehen bewusst **nicht** in diesem Repository.
- **Verwendung im Lexikon:** **Nur als Strukturvorlage.** Echte Werte, Org-IDs und der produktspezifische Teil werden **nicht** übernommen. Die Beispiele arbeiten mit der fiktiven Entsprechung aus [welt/baerstadt.md](welt/baerstadt.md).
- **Rechte:** Bewerbungsunterlage eines Dritten mit personenbezogenen Daten im produktspezifischen Teil. Gehört **nicht** ins Repository.
- **Stichworte:** Feldnamen `amAuftragsTyp`, `logTransaktionsTyp`, `berSynchronNummer`, `prodKeyOrganisation_ID`, `appInstanz_ID`, `amAenderungsreferenz_ID`, `amTerminalGruppe_ID`

## Q31

**KCD NRW – Abbildung und Kontrolle in NRW**

- **Datei:** `QUELLEN/Q31_KCD-NRW_Abbildung-und-Kontrolle-in-NRW_v2.0_2026-06.pdf` (77 Seiten)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** offen
- **Stand:** Version 2.0, Stand April 2026, gültig ab Juni 2026
- **Inhalt:** Elektronisches Fahrgeldmanagement, Abbildung und Kontrolle der Tarife in NRW. **Aktuellstes Projektdokument der Sammlung** und damit der beste Beleg für den heutigen Stand der Kontrollpraxis.
- **Stichworte:** Tarifabbildung, Kontrolle, Produktparameter, aktuelle Praxis
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/Abbildung_und_Kontrolle_in_NRW_2_0_ab_Juni_2026.pdf

## Q32

**KCD NRW – Abbildung und Kontrolle von (((eTickets im Westfalen-Tarif**

- **Datei:** `QUELLEN/Q32_KCD-NRW_Abbildung-Kontrolle-eTickets-Westfalen-Tarif_v2.4.4.pdf` (92 Seiten)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** offen
- **Stand:** Version 2.4.4, 31.10.2018
- **Inhalt:** Umfangreiche Abbildung eines Verbundtarifs auf EFS-Felder samt Kontrolllogik. Mit 92 Seiten die **zweitergiebigste Projektquelle** für Feld- und Produktartikel; gute Vergleichsquelle zu den RMV-Dokumenten, um verbundspezifische von allgemeinen Festlegungen zu unterscheiden.
- **Stichworte:** EFS-Felder, Produktabbildung, Kontrolle, Tarifbereiche
- **URL:** https://www.kcd-nrw.de/fileadmin/03_KC_Seiten/KCD/Downloads/Technische_Dokumente/Dokumente_WestfalenTarif/Abbildung_und_Kontrolle_von_eTickets_im_Westfalen-Tarif_V2.4.4_final.pdf

## Q33

**KCD NRW – Ergebnisdokument der Arbeitsgruppe Kontrolle**

- **Datei:** `QUELLEN/Q33_KCD-NRW_Ergebnisdokument-AG-Kontrolle_v1.3_2024-06-25.pdf` (25 Seiten)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** offen
- **Stand:** Version 1.3, 25.06.2024
- **Inhalt:** Ergebnisse zur Kontrolle von Tickets, u. a. Akzeptanz und Sonderfälle (Bahncard).
- **Stichworte:** Kontrolle, Kontrollgeräte, Sichtkontrolle, Sonderfälle
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/240625_Ergebnisdokument_der_Arbeitsgruppe_Kontrolle_V1.3.pdf

## Q34

**KCD NRW – Ergebnisdokument Deutschlandticket / UIC**

- **Datei:** `QUELLEN/Q34_KCD-NRW_Ergebnisdokument-Deutschlandticket-UIC_v1.04.pdf` (40 Seiten)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** offen
- **Stand:** Version 1.04
- **Inhalt:** Einheitliche Umsetzung des Deutschlandtickets, Bezug zum UIC-Barcode.
- **Stichworte:** Deutschlandticket, UIC-Barcode, VDV-Barcode, Abgrenzung der Barcode-Welten
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/01_Ergebnisdokument_Deutschlandticket_UIC__V1.04.pdf

## Q35

**KCD NRW – Produktparameter der Tarife in NRW**

- **Datei:** `QUELLEN/Q35_KCD-NRW_Produktparameter-der-Tarife-in-NRW_v1.0_2021-04-30.pdf` (10 Seiten)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** teilweise
- **Stand:** Version 1.0, 30.04.2021
- **Inhalt:** Parametergruppen und Parameter je Produkt mit Format und Wertebereich, u. a. `produktNummer` (Wertebereich bis 65535), Zuordnung zum PV, Vorverkaufsbeginn, Vertriebs- und Gültigkeitsdaten. **Kompakte und gut zitierbare Quelle für die Kategorie „Berechtigungen und Produkte“.**
- **Stichworte:** Produkt, produktNummer, Produktparameter, Vorverkauf, Gültigkeit
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/2021-04-30_Produktparameter_der_Tarife_in_NRW_1_0.pdf

## Q36

**KCD NRW – Vertriebliche Umsetzung der eTarife in NRW**

- **Datei:** `QUELLEN/Q36_KCD-NRW_Vertriebliche-Umsetzung-eTarife-NRW_v1.8_2026-08-12.pdf` (51 Seiten)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** offen
- **Stand:** Version 1.8, 12.08.2026
- **Inhalt:** Vertriebliche Umsetzung der eTarife in NRW (eezy und weitere), Check-in/Check-out-Praxis.
- **Stichworte:** eTarif, CiCo, Bestpreis, Vertrieb, Luftlinientarif
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/2026-08-12_vertriebliche_Umsetzung_der_eTarife_in_NRW_-_V_1.8_clean.pdf

## Q38

**bwtarif – Vertriebskonzept mit technischen Anlagen**

- **Datei:** `QUELLEN/Q38_bwtarif_Vertriebskonzept_v2.5_2024-08-08.pdf` (158 Seiten)
- **Typ:** Projekt · **Herkunft:** Original · **Auswertung:** offen
- **Stand:** v2.5, 08.08.2024, bwtarif GmbH
- **Inhalt:** Vertriebskonzept des landesweiten Tarifs in Baden-Württemberg mit technischen Vorgaben zu Aktionsmanagement, Multiberechtigungen, PKM und statischen Berechtigungen. **Jüngstes Projektdokument neben [Q31](#q31)** und damit nützlich als Vergleichsquelle zu den älteren RMV-Unterlagen: Wo bwtarif und RMV unabhängig dasselbe festlegen, ist das ein starkes Indiz für eine KA-weite Festlegung.
- **Stichworte:** Aktionsmanagement, Multiberechtigung, PKM, statische Berechtigung, Vertrieb
- **URL:** https://www.bwtarif.gmbh/wp-content/uploads/2024/09/240808-bwtarif-Vertriebskonzept-v2.5.pdf

## Q39

**RMV – vHGS-Vertrag mit Anlagen (Muster), darin Anlage 6 „Konzept Externer Mandant“**

- **Datei:** `QUELLEN/Q39_RMV_vHGS-Vertrag-mit-Anlagen_2021-10-01.pdf` (135 Seiten)
- **Typ:** Projekt · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** teilweise — Kap. 3.2.5, 3.2.6, 3.3.1, 3.3.2 und der Glossarteil sind am Dokument geprüft
- **Stand:** Vertrag Stand 01.10.2021; Anlage 6 „Konzept Externer Mandant“ v1.4, 04.10.2011, Cubic Transportation Systems
- **Inhalt — nach [Q06](#q06) die zweite tragende RMV-Quelle, mit teils neuen Informationen:**
  - **Vollständiger Nachrichtenfluss des Aktionsmanagements** (Kap. 3.2.5, PDF-S. 51 f.) mit **Auftragsnachrichten**, die in [Q06](#q06) fehlen: `TXAAUFBER` (Berechtigung-Ausgabe), `TXRAUFBER` (Rücknahme), `TXEAUFBER` (Entsperrung), `TXAFREIBER` (Aktionsfreigabeauftrag des beauftragenden KVP), `TXAFREIMITBER` (Aktionsfreigabemitteilung des ALISE an den beauftragenden KVP), `TXAS` (Anforderung der Aktionsliste, synchron, Antwort `TXAML`) sowie `TXABER`, `TXRBER`, `TXSNAWB` als Nachweise und deren Weiterleitung an den beauftragenden KVP.
  - **ALISE-Definition:** „Der ALISE ist eine **Spezialisierung der Rolle PV**, die bei Anwendung des Aktionsmanagements die entsprechende Funktionalität eines Aktionslistenservice-Systems (ALISES) in ihrem PVS vorzuhalten hat.“ (Glossarteil)
  - **Rollentabelle:** „vHGS als ALISE PV … **Rollencode 3**“ (Kap. 3.3.2, PDF-S. 53) — **unabhängige Bestätigung** des Befunds aus [Q06](#q06), Fußnote 7.
  - **Aktionsliste:** „Vom ALISE erstellte **KVP-spezifische** Liste der Aktionsaufträge.“ (Glossarteil)
  - **Aktionsmanagement:** Vorgänge werden „an einem beliebigen Vertriebsterminal“ beauftragt und später automatisch ausgeführt; im eTicket RheinMain läuft z. B. der Verkauf im TicketShop darüber. Möglich sind auch **Rückgabe, Änderung oder Sperrung** von Berechtigungen und die Sperrung der Applikation. (Glossarteil)
  - **TX_BASE:** verwendet nach KA-Spezifikationsversion 1.107; die Signaturattribute `transSignaturTyp`, `transSignaturZertifikat` und `transSignatur` werden **nicht verwendet und nicht gefüllt** (Kap. 3.3.1).
  - `TXA`/`TXB` werden in einem eigenen Kommunikationsvorgang gesendet; zunächst quittiert nur der HTTP-Rückgabewert (Kap. 3.2.6).
  - Weitere Nachrichtennamen im Dokument: `TXSAUFA`, `TXSAUFB`, `TXSFREIA`, `TXSFREIB`, `TXSNAWA`, `TXAGB`, `TXAGBBER`, `TXAGBKUNDE`, `TXAGBPINPUC`, `TXAA`, `TXKNAWDM`, `TXSLNM`, `TXSLK`, `TXSLOS`.
- **Stichworte:** Auftragsnachrichten, Aktionsfreigabe, ALISE als PV-Spezialisierung, TXAS/TXAML, TX_BASE-Signatur
- **Rechte:** „Cubic Transportation Systems Deutschland GmbH, **Vertraulich**“. Nur kurze Exzerpte mit Fundstelle.
- **URL (tot, 404):** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_26_EFM_vHGS-Vertrag_mAnl_Muster_Stand_211001_MVU_211206.pdf

## Q40

**KCD NRW – Rahmenlastenheft DL-System**

- **Datei:** `QUELLEN/Q40_KCD-NRW_Rahmenlastenheft-DL-System_v2.4.pdf` (44 Seiten)
- **Typ:** Projekt · **Herkunft:** Original (Archivbereich kcd-nrw.de) · **Auswertung:** offen
- **Stand:** Version 2.4
- **Inhalt:** Rahmenlastenheft für ein Dienstleister-System; Kontroll- und Sperrprozesse. Verweist durchgehend auf KA-Dokumente der **Version 1.107** (13 Fundstellen, am Dokument geprüft) und ist damit ein Beleg für die ältere Schnittstellenversion.
- **Stichworte:** DL-System, Kontrolle, Sperrprozesse, Transaktionsprüfung, Version 1.107
- **URL:** https://www.kcd-nrw.de/fileadmin/03_KC_Seiten/KCD/Downloads/Technische_Dokumente/Archiv/Rahmenlastenheft_DL-System_2_4.pdf

---

# 5. Hersteller- und Anbieterquellen

> Herstellerquellen belegen **Marktpraxis**, nicht den Standard. Für Standardaussagen nicht zitierfähig.

## Q12

**TapConnect – VDV Barcode Field Mappings**

- **Datei:** `QUELLEN/Q12_TapConnect_VDV-Barcode-Field-Mappings.html`
- **Typ:** Hersteller · **Herkunft:** Original · **Auswertung:** teilweise
- **Inhalt — weit ergiebiger als der Titel vermuten lässt:** eine **feldweise Abbildung des VDV-Barcodes** mit **seitengenauen Verweisen in die nicht öffentlichen Spezifikationen**, jeweils in der Fassung **V190**:
  - **KA HD_BOM-Spec_V190:** S. 50 Tab. 6-10 (`dateTimeCompact`), S. 84 Tab. 6-69 (OrtTyp), S. 92 Tab. 6-85 (TerminalTyp), S. 104 Tab. 6-103 (Produkt-ID-Struktur), S. 110 Tab. 6-123 (`Ort_ID`), S. 112 Tab. 6-127 (`Terminal_ID`), S. 113 Tab. 6-130, S. 130 Tab. 6-152, S. 132 Tab. 6-158, S. 140 Tab. 6-162, Abschn. **6.7.2 „Kürzungsregel für Namen und Vornamen“**
  - **Anlage TLV EFS_V190:** S. 9 Abschn. 2.2 (Tag 0xDB „Fahrgast“), S. 18 Tab. 2-8 (Variante D, `0x0F`)
  - **KA STB-SPEC_V190:** Tab. 3-1, S. 12 (Kennung „VDV“, Version `0x19 0x00`, Füllbytes auf mindestens 111 Byte)
  - **KA SAM-Spec_V190** S. 205 und **KA NM-SPEC_V190** S. 199 Tab. 5-12 (`SAM_ID.samNummer`, 3 Byte)
  - **Technische Anforderung Deutschlandticket V1.7:** S. 5 (Produktnummern 9999 regulär, 9998 Jobticket, 9995 Schüler), S. 15 Kap. 4.3 (Feldliste)
  - Belegte Werte: `efsFahrgastGeschlecht` fest `0x00`; `efsFahrgastGeburtsdatum` sonst 1970-01-01; `efsFahrgastName` Typ-1-anonymisiert mit **wörtlichem Beispiel**; Tag `0x8A` als leerer Transaktion produktspezifischer Teil; TerminalTyp `0x11` = Online Ticket Server; OrtTyp `0xC9` = Massenpersonalisierer; `prodProdukt_ID` als 2 Byte Produktnummer + 2 Byte Org-ID (Beispiel `0x270f0bb8`)
  - Nennt mit **V190 = 1.9.0** eine weitere Spezifikationsversion neben 1.1.07, 1.3.0, 1.5.0 und 1.12.0.
- **Stichworte:** VDV-Barcode, TLV, Tag 0xDB, Fahrgastdaten, Namenskürzung
- **URL:** https://documentation.tapconnect.io/public/specs/vdv-barcode-field-mappings.html

## Q13

**Krauth Technology – KA Background System / Interfaces**

- **Dateien:** `QUELLEN/Q13a_Krauth_KA-Background-System.html`, `QUELLEN/Q13b_Krauth_Interfaces.html`
- **Typ:** Hersteller · **Herkunft:** Original · **Auswertung:** offen
- **Inhalt:** Produktbeschreibung eines KA-Hintergrundsystems und seiner Schnittstellen.
- **Stichworte:** Hintergrundsystem, KVP-System, PV-System
- **URL:** https://www.krauth-technology.de/en/solutions/ticketing-software/background-software/ka-background-system

## Q14

**eos.uptrade – eos.ticketingsuite VDV-KA-zertifiziert**

- **Datei:** `QUELLEN/Q14_eos-uptrade_VDV-KA-zertifiziert.html`
- **Typ:** Hersteller · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** teilweise — Aussagen zur Zertifizierung (Testprogramm, Sperrlisten, ungültige SAMs) ausgewertet
- **Stichworte:** Zertifizierung, Marktübersicht
- **URL:** https://www.eos-uptrade.de/en/company/news/article/eos-ticketingsuite-vdv-ka-certified

## Q15

**IVU – VDV-KA-Zertifizierung für Hard- und Software**

- **Datei:** `QUELLEN/Q15b_IVU_VDV-KA-Certification.html`
- **Typ:** Hersteller · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** teilweise — Aussagen zur Zertifizierung (Testfälle, Notfallschlüssel, ungültige SAMs) ausgewertet
- **Hinweis:** Die zweite IVU-Seite („reference for e-ticketing“) ist weder online noch im Archiv verfügbar — **nicht beschafft**.
- **Stichworte:** Zertifizierung, Marktübersicht
- **URL:** https://www.ivu.com/all-references/references/vdv-ka-certification-for-ivu-hardware-and-software

## Q16

**amcon – Customers & Use Cases**

- **Datei:** `QUELLEN/Q16_amcon_Customers-Use-Cases.html`
- **Typ:** Hersteller · **Herkunft:** Original · **Auswertung:** offen
- **Stichworte:** Kontrollgeräte, Anwendungsfälle
- **URL:** https://amcon.de/en/customers-use-cases/

## Q17

**Ximedes – Account Based Ticketing**

- **Datei:** `QUELLEN/Q17_Ximedes_Account-Based-Ticketing.html`
- **Typ:** Hersteller · **Herkunft:** Original · **Auswertung:** offen
- **Inhalt:** ABT-Plattform eines an OVpay (Niederlande) beteiligten Anbieters.
- **Stichworte:** ABT, OVpay
- **URL:** https://ximedes.com/public-transport/abt

## Q18

**Kentkart – To validate, or not to validate**

- **Datei:** `QUELLEN/Q18_Kentkart_To-validate-or-not-to-validate.html`
- **Typ:** Hersteller · **Herkunft:** Original · **Auswertung:** offen
- **Inhalt:** Validierungs- und Kontrollkonzepte im ABT.
- **Stichworte:** Validierung, Kontrolle, ABT
- **URL:** https://www.kentkart.com/?p=15641

## Q19

**Ticketer – PAR Deny Lists**

- **Datei:** `QUELLEN/Q19_Ticketer_PAR-Deny-Lists.html`
- **Typ:** Hersteller · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** offen
- **Inhalt:** Sperrlisten auf Basis der PAR (Payment Account Reference) bei bankkartenbasiertem ABT.
- **Stichworte:** Deny List, PAR, EMV-Token, Offline-Kontrolle
- **URL:** https://ticketer.com/en/did-you-know/par-deny-lists

## Q20

**Genfare – Hand Held Validator**

- **Datei:** `QUELLEN/Q20_Genfare_Hand-Held-Validator.html`
- **Typ:** Hersteller · **Herkunft:** Original · **Auswertung:** offen
- **Stichworte:** Kontrollgerät, Offline-Validierung
- **URL:** https://genfare.com/products/hand-held-validator/

## Q37

**cetecom advanced – Prüfbericht Akzeptanzterminal PM95**

- **Datei:** `QUELLEN/Q37_CETECOM_Pruefbericht-Akzeptanzterminal-PM95.pdf` (8 Seiten)
- **Typ:** Hersteller / Zulassungsprüfung · **Herkunft:** Original (carema.de) · **Auswertung:** teilweise — die Spezifikationsliste auf S. 4 ist am Dokument geprüft
- **Stand:** Prüfbericht 1-8334/24-01-02_TR1-R01 (2024)
- **Inhalt — wichtigster Versionsnachweis der Sammlung:** Der Bericht einer Zulassungsprüfung für ein Akzeptanzterminal listet die zugrunde gelegten Spezifikationen mit Version. **Alle zwölf Einträge tragen die Version 1.12.0:**
  1. KA SysLH PbKVPRT — Systemlastenheft Personalbediente KVP-ReferenzTerminals
  2. KA SysLH DLRT — Systemlastenheft DL-ReferenzTerminals
  3. **KA HD_BOM-SPEC** — Hauptdokument mit Basisobjektmodell
  4. **KA SAM-SPEC**
  5. **KA NM-SPEC**
  6. **KA MultiBER-SPEC** — „Performanceverbesserung bei der EFS-Ausgabe … Spezifikation zur Multi-Berechtigungsausgabe“
  7. **KA AktM-SPEC** — „Aktionsmanagement für die Berechtigungsart EFS **und Entsperrung von AF…**“ (vollständigerer Titel als in [Q25](#q25))
  8. **KA SST-SPEC** — „Schnittstellenspezifikationen der Referenzsysteme … Applikationsherausgeber (AH), Sperrlistenservice (KOSE)“
  9. **KA STB-SPEC** — statische Berechtigungen für 2D-Barcode-Tickets
  10. **KA STB-SPEC mobile plus** — „Kryptographischer Kopierschutz für statische Berechtigungen VDV-Barcode mobile+“
  11. Motics — „Verification of Copy Protection and Entitlement Data“
  12. **KA XML-Schemata und WSDL** der TX-Transaktionen sowie KA-XML-Schema der KA-NM-Lieferliste
- **Bedeutung:** Damit ist eine **Version 1.12.0** der KA-Spezifikationen belegt — deutlich neuer als die bisher bekannten 1.1.07, 1.3.0 und 1.5.0. Daraus folgt **nicht**, welches Release heute verbindlich unterstützt wird; der Bericht belegt nur, wogegen dieses Terminal 2024 geprüft wurde. Konsequenz für die Beschaffung: Die Anfrage muss auch Version 1.12.0 nennen, siehe [BESCHAFFUNG.md](BESCHAFFUNG.md).
- **Stichworte:** KA-Versionen, 1.12.0, Zulassung von Akzeptanzterminals, vollständige Spezifikationstitel
- **Rechte:** „geistiges Eigentum der cetecom advanced GmbH“, bestimmt zur Beantragung einer Akzeptanzterminalzulassung bei der Zulassungsstelle des VDV eTS. Nur Verweis und Kurzexzerpt.
- **URL:** https://www.carema.de/wp-content/uploads/2024/10/CETECOM-Test-Report-Akzeptanzterminal-PM95.pdf

---

# 6. Sekundärquellen

## Q21

**OSPT Alliance – Account-Based Ticketing**

- **Datei:** `QUELLEN/Q21_OSPT-Alliance_Account-Based-Ticketing.html`
- **Typ:** Sekundär · **Herkunft:** Original · **Auswertung:** offen
- **Stichworte:** ABT, Sicherheitsmedien, CIPURSE
- **URL:** https://osptalliance.org/account-based-ticketing/

## Q22

**UITP – Demystifying Ticketing and Payment in Public Transport**

- **Datei:** `QUELLEN/Q22_UITP_Demystifying-Ticketing-and-Payment.html` (Publikationsseite, nicht der Bericht selbst)
- **Typ:** Sekundär · **Herkunft:** Original · **Auswertung:** teilweise
- **Inhalt:** Überblick über Ticketing- und Zahlungstechnologien sowie Trends. Der eigentliche Bericht steht nicht frei zum Download.
- **Stichworte:** internationale Begriffe, EMV, ABT, CiCo
- **URL:** https://www.uitp.org/publications/demystifying-ticketing-and-payment-in-public-transport/

## Q23

**UK Authority – Transport Scotland ABT Back Office**

- **Datei:** `QUELLEN/Q23_UKAuthority_Transport-Scotland-ABT-Back-Office.html`
- **Typ:** Sekundär · **Herkunft:** Webarchiv (Original 403) · **Auswertung:** offen
- **Stichworte:** ABT-Beschaffung, Praxisbeispiel
- **URL:** https://www.ukauthority.com/articles/transport-scotland-aims-for-back-office-upgrade/

## Q24

**Bundestag-Drucksache 18/11086**

- **Datei:** `QUELLEN/Q24_Bundestag_Drucksache_18-11086.pdf` (8 Seiten)
- **Typ:** Sekundär · **Herkunft:** Original · **Auswertung:** offen
- **Stand:** 06.02.2017, 18. Wahlperiode
- **Inhalt (am Dokument geprüft):** Antwort der Bundesregierung auf die Kleine Anfrage der Fraktion BÜNDNIS 90/DIE GRÜNEN, Drucksache 18/10915, mit dem Titel **„Pläne der Bundesregierung für einheitliches elektronisches Ticketing (eTicketing) in Deutschland“**. Damit ist der eTicket-Bezug belegt; die Quelle dokumentiert den politischen Rahmen, nicht die Technik.
- **Technischer Hinweis:** Die Extraktion streut Sprachmarker („de“) in den Text. Für Zitate `sed -e 's/de//g'` anwenden oder am PDF prüfen.
- **Stichworte:** politischer und rechtlicher Rahmen, Bundespolitik, eTicketing in Deutschland
- **URL:** https://dserver.bundestag.de/btd/18/110/1811086.pdf

## Q28

**KCD NRW – Technische Dokumente (Downloadseite)**

- **Datei:** `QUELLEN/Q28_KCD-NRW_Technische-Dokumente.html`
- **Typ:** Sekundär · **Herkunft:** Original · **Auswertung:** teilweise (als Fundstelle ausgewertet)
- **Inhalt:** Einstiegsseite, über die Q30–Q36 gefunden wurden. **Bei Bedarf erneut prüfen**, dort erscheinen regelmäßig neue Dokumente.
- **Stichworte:** Bezugsquelle, Dokumentenübersicht NRW
- **URL:** https://www.kcd-nrw.de/service/downloads/technische-dokumente.html

## Q29

**itcs-info – VDV-KA Release 1.5.0 veröffentlicht**

- **Datei:** `QUELLEN/Q29_itcs-info_VDV-KA-Release-1.5.0.html`
- **Typ:** Sekundär · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** offen
- **Inhalt:** Meldung zu Änderungen in Release 1.5.0, u. a. beim Aktionsmanagement und bei der Verarbeitung von Berechtigungen. Einziger Beleg für Release 1.5.0 in der Sammlung, aber **Sekundärquelle** — Aussagen als `zu prüfen` führen.
- **Stichworte:** KA-Versionen, Release 1.5.0, Versionsunterschiede
- **URL:** https://www.itcs-info.de/index.php/news/145-e-ticket/490-vdv-ka-release-1-5-0-veroeffentlicht

## Q41

**VDV-Schrift 436-1 – Offene Mobilitätsplattform, Rollenmodell**

- **Datei:** `QUELLEN/Q41_VDV-Schrift-436-1_Offene-Mobilitaetsplattform-Rollenmodell.pdf` (26 Seiten)
- **Typ:** Primär (VDV-Schrift) · **Herkunft:** Original (vdv.de) · **Auswertung:** **nicht möglich**
- **Inhalt (unverifiziert):** Soll im Quellenverzeichnis die **KA BOM-SPEC Version 1.5.0 von 2016** nennen. Das ist **nicht geprüft**.
- **Technischer Hinweis:** Die Datei ist **AES-256-verschlüsselt** (`/CFM /AESV3`). `tools/pdftext.py` kann daraus keinen Text gewinnen; eine AES-Implementierung mit der Standardbibliothek wäre für diesen Zweck unverhältnismäßig. In einem PDF-Betrachter lässt sich das Dokument öffnen — die Angabe auf der gedruckten Seite 20 ist dort **von Hand zu prüfen**, bevor sie zitiert wird.
- **Stichworte:** Rollenmodell, Versionsnachweis BOM 1.5.0 (zu prüfen)
- **URL:** https://www.vdv.de/downloads/4016/436%201%20%20SDS%281%29/forced

## Q42

**KCD NRW – Newsletterarchiv**

- **Datei:** `QUELLEN/Q42_KCD-NRW_Newsletterarchiv.html`
- **Typ:** Sekundär · **Herkunft:** Original · **Auswertung:** teilweise — die Zertifikats- und Zeitangaben sind in der Seite geprüft
- **Inhalt — klärt zwei offene Fragen:** Das Archiv gibt die Teilnehmerinformationen des (((eTicket Service wieder und nennt dabei harte Daten zur Sicherheitsinfrastruktur:
  - Die aktuellen SubCA-Zertifikate sind die letzten, die mit dem **Root-Zertifikat der 1. Generation (1GSI)** erstellt wurden. Die aktive Gültigkeit dieses Root-Zertifikats ist **planmäßig zum 1. Dezember 2021 abgelaufen**; neue Zertifikate lassen sich damit nicht mehr erstellen, die SubCA-Zertifikate bleiben aber gültig.
  - **Häufiger Implementierungsfehler:** Einige Systeme prüfen bei Ausgabe oder Kontrolle, ob das Root-Zertifikat *zu diesem Zeitpunkt* gültig ist. Das ist falsch und führt seit dem 1. Dezember 2021 zu Fehlverhalten. Richtig ist die Prüfung, ob das Root-Zertifikat **zum Zeitpunkt der Erstellung des SubCA-Zertifikats** gültig war.
  - Ein neues Root-Zertifikat gibt es erst für die **2. Generation (2GSI)**, und zwar mit der Einführung der **VDV-Kernapplikation 3.0 unter dem Namen (((etiCORE zum 1. Dezember 2026**.
  - Die aktuellen SubCA-Zertifikate sind **10 Jahre bis zum 1. Dezember 2031** gültig — „also bis zum Ende der VDV-Kernapplikation 1.x“. Im Übergangszeitraum 2026 bis 2031 sind beide Zertifikate gültig und ermöglichen den **Parallelbetrieb von VDV-KA 1.x (1GSI) und (((etiCORE (2GSI)**.
- **Quellenkritik:** Sekundärquelle. Das KCD NRW gibt Informationen des (((eTicket Service wieder; die Angaben sind konkret und datiert, stammen aber nicht aus einer Primärquelle. Für verbindliche Aussagen beim VDV eTS bestätigen lassen.
- **Stichworte:** 1GSI, 2GSI, Root- und SubCA-Zertifikate, etiCORE, KA 3.0, Parallelbetrieb, 01.12.2026, 01.12.2031
- **URL:** https://www.kcd-nrw.de/service/newsletter/archiv.html

---

# 7. Nicht beschaffte Quellen

Mit den Spezifikationen in Abschnitt 2 ist der größte Teil der früheren Anfrageliste erledigt. Was
hier steht, ist der **Rest** — Stand 20.10.2026.

| Gesucht | Zweck | Stand |
|---|---|---|
| KA XML-Schemata und WSDL (Inv. 5) | XSD zu `http://vdv/ka/alise/2` | nicht öffentlich — **blockiert weiterhin den geplanten ALISE-Decoder**. [Q79](#q79) beschreibt die Schnittstellen-Releases, enthält die Schemata aber nicht |
| ALISE-Schnittstellenbeschreibung | Nachrichtenaufbau der Aktionsliste | nicht öffentlich. [Q54](#q54) und [Q55](#q55) beschreiben die Nachrichten fachlich, die Schnittstelle selbst fehlt |
| `Mapping-old-new-*.xlsx` (drei Dateien) | Abbildung KA 1.x auf etiCORE | nicht beschafft; die Abbildung der Namen ist über die `meta:old`-Vermerke in [Q50](#q50) teilweise rekonstruierbar |
| Beispieldatenpaket, Beispielnachrichten | Prüfdaten für das Werkzeug | nicht beschafft — ohne echte Nachrichten bleibt O13 offen |
| Ältere Versionen 1.3.0 und 1.5.0 | Versionsvergleich, Deutung von Fremdquellen | nicht beschafft. Vorliegend ist 1.12.0, belegt ist 1.12.1 ([Q43](#q43), Kap. 3) |
| IVU „reference for e-ticketing“ | Marktübersicht | online und im Archiv nicht verfügbar |
| UITP-Bericht (Volltext zu [Q22](#q22)) | internationale Begriffe | nur gegen Registrierung |

**Was inzwischen vorliegt** und hier gestrichen ist: KA AktM-SPEC ([Q55](#q55)), KA HD_BOM-SPEC
([Q52](#q52), mit den vollständigen Codelisten), KA SST-SPEC ([Q54](#q54)) sowie 27 weitere
Spezifikationen und Anwendungshinweise. Siehe [BESCHAFFUNG.md](BESCHAFFUNG.md).

> **Eine Quelle fehlt auf der Platte.** [Q49](#q49) bis [Q51](#q51) verweisen auf die lokale
> Gesamtkopie `QUELLEN/Q49_etiCORE-Spezifikation_3.0.0-rc.6/`. Dieser Ordner **existiert nicht**;
> vorhanden sind nur die daraus gezogenen Exzerpte [exzerpte/Q50.md](exzerpte/Q50.md) und
> [exzerpte/Q51.md](exzerpte/Q51.md). Aussagen, die auf Q49 bis Q51 beruhen, sind damit derzeit
> **nicht am Original nachprüfbar**. Die Kopie ist erneut zu ziehen (Modell online, siehe
> [Q49](#q49)).

---

# 8. Herkunft dieses Verzeichnisses

Dieses Verzeichnis führt drei ältere Rechercheakten zusammen. Sie bleiben als Arbeitsstand erhalten und werden nicht zitiert:

| Datei | Rolle | Nummerierung dort |
|---|---|---|
| [QUELLEN_VDV-KA.md](QUELLEN_VDV-KA.md) | Ausgangsverzeichnis | Q01–Q24 — **hier übernommen** |
| [QUELLEN_ALISE.md](QUELLEN_ALISE.md) | Recherche zu ALISE und Werkzeugidee | Quellen A–E → hier Q25, Q26, Q27, Q28, Q29 |
| [Quellen_LBV.md](Quellen_LBV.md) | ausgearbeitete LVB-Aufgabe, dichteste Faktensammlung | Fußnoten [1]–[8] → [1] = Q11, [2] = Q01, [3] = Q02, [4] = Q05, [5] = Q18, [6] = Q19, [7] = Q12, [8] = Q06 |

`Quellen_LBV.md` ist **keine Quelle, sondern eine Auswertung**. Artikel zitieren immer das zugrunde liegende Dokument (Q01–Q36), nie diese Datei.
