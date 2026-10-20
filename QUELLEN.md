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

---

# 2. Projekt- und Verbundspezifikationen

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
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** teilweise — Aktionsmanagement (PO, CCP-Ordering, CCP-Execution) ausgewertet, Rest offen
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
- **Typ:** Primär · **Herkunft:** Original · **Auswertung:** offen — Struktur geprüft, Typen noch nicht ausgewertet
- **Stand:** Version **3.0.0-rc.6**, geladen am 2026-10-20
- **Fundstelle:** Modul und Typname, etwa „`ste`, Typ `StaticElectronicTicketParameters`“.
- **Rechte:** wie [Q49](#q49).
- **Inhalt:** Neun ASN.1-Module — Electronic Ticket (`et`), Payment, Static Entitlement (`ste`), Tariff, User Medium (`user-medium`), Common, CV Certificate (`cv-certificates`), Mobile Ticketing Crypto Service (`motics`) und Secure Application Module (`sam`). Je Typ stehen Tag (hexadezimal), Art (`SEQUENCE`, `CHOICE`, `ENUMERATED` u. a.), eine Feldtabelle mit Tag, Elementname, Typname, Optional-Kennzeichen und Beschreibung sowie bei Aufzählungen die Werte mit Bezeichnern. Das Modul `common` enthält 44 Typen.
- **Bedeutung:** maschinenlesbare Grundlage für Tags und Aufzählungen im Chip- und Barcode-Bereich — soweit etiCORE betroffen. Verweise auf EN 1545-1:2015 bei `DeviceTypeCode` und `LocationTypeCode`.
- **Einschränkung:** etiCORE-Typen, nicht die KA-1.x-Strukturen. Gleiche Namen bedeuten nicht gleiche Kodierung.
- **Stichworte:** ASN.1, Tags, Static Entitlement, User Medium, Aufzählungen, CV-Zertifikat, MOTICS

---

# 3. Hersteller- und Anbieterquellen

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
- **Typ:** Hersteller · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** offen
- **Stichworte:** Zertifizierung, Marktübersicht
- **URL:** https://www.eos-uptrade.de/en/company/news/article/eos-ticketingsuite-vdv-ka-certified

## Q15

**IVU – VDV-KA-Zertifizierung für Hard- und Software**

- **Datei:** `QUELLEN/Q15b_IVU_VDV-KA-Certification.html`
- **Typ:** Hersteller · **Herkunft:** Webarchiv (Original 404) · **Auswertung:** offen
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

# 4. Sekundärquellen

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

# 5. Nicht beschaffte Quellen

| Gesucht | Zweck | Stand |
|---|---|---|
| KA AktM-SPEC (Inv. 41) | Aktionsmanagement, Auftragstypen, TXAML | nicht öffentlich, über [Q26](#q26) anfragen |
| KA BOM-SPEC (Inv. 1) | Datentypen, Codelisten, `IONTransaktionsTyp_CODE` | nicht öffentlich |
| KA SST-SPEC (Inv. 4) | TX-Nachrichten | nicht öffentlich |
| KA XML-Schemata / WSDL (Inv. 5) | XSD zu `http://vdv/ka/alise/2` | nicht öffentlich — **blockiert den geplanten ALISE-Decoder** |
| Vollständige Codelisten | `amAuftragsTyp`, `berBezahlArt`, `prodAbrechnungsVerfahren` | nicht öffentlich |
| IVU „reference for e-ticketing“ | Marktübersicht | online und im Archiv nicht verfügbar |
| UITP-Bericht (Volltext zu [Q22](#q22)) | internationale Begriffe | nur gegen Registrierung |

**Vollständige Anfrageliste mit Begründung je Dokument:** [BESCHAFFUNG.md](BESCHAFFUNG.md)

**Anfrage beim VDV eTicket Service** ([Q26](#q26), service@eticket-deutschland.de) für: KA AktM-SPEC, ALISE-Schnittstellenbeschreibung, ALISE-XSD samt Abhängigkeiten, KA SST-SPEC, KA BOM-SPEC, Codelisten, Dokumentation der logischen Transaktionstypen, Beispielnachrichten. Dabei ausdrücklich nach den Versionen **1.3.0 und 1.5.0** sowie dem aktuell unterstützten Release fragen.

---

# 6. Herkunft dieses Verzeichnisses

Dieses Verzeichnis führt drei ältere Rechercheakten zusammen. Sie bleiben als Arbeitsstand erhalten und werden nicht zitiert:

| Datei | Rolle | Nummerierung dort |
|---|---|---|
| [QUELLEN_VDV-KA.md](QUELLEN_VDV-KA.md) | Ausgangsverzeichnis | Q01–Q24 — **hier übernommen** |
| [QUELLEN_ALISE.md](QUELLEN_ALISE.md) | Recherche zu ALISE und Werkzeugidee | Quellen A–E → hier Q25, Q26, Q27, Q28, Q29 |
| [Quellen_LBV.md](Quellen_LBV.md) | ausgearbeitete LVB-Aufgabe, dichteste Faktensammlung | Fußnoten [1]–[8] → [1] = Q11, [2] = Q01, [3] = Q02, [4] = Q05, [5] = Q18, [6] = Q19, [7] = Q12, [8] = Q06 |

`Quellen_LBV.md` ist **keine Quelle, sondern eine Auswertung**. Artikel zitieren immer das zugrunde liegende Dokument (Q01–Q36), nie diese Datei.
