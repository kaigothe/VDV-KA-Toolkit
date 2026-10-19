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

---

# 3. Hersteller- und Anbieterquellen

> Herstellerquellen belegen **Marktpraxis**, nicht den Standard. Für Standardaussagen nicht zitierfähig.

## Q12

**TapConnect – VDV Barcode Field Mappings**

- **Datei:** `QUELLEN/Q12_TapConnect_VDV-Barcode-Field-Mappings.html`
- **Typ:** Hersteller · **Herkunft:** Original · **Auswertung:** teilweise
- **Inhalt:** Zuordnung von Feldern zum VDV-Barcode. **Tag 0xDB „Fahrgast“** mit `efsFahrgastGeschlecht`, `efsFahrgastGeburtsdatum` (Standardwert 1970-01-01) und `efsFahrgastName` (Typ-1-Anonymisierung). Verweist auf Anlage TLV EFS V1.90 und HD_BOM Abschnitt 6.7.2 „Kürzungsregel für Namen“.
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
- **Inhalt:** Antwort der Bundesregierung auf eine Kleine Anfrage zur Drucksache 18/10915; Thema digitale Angebote im öffentlichen Verkehr. **Bezug zum eTicket noch ungeprüft** — falls kein inhaltlicher Bezug besteht, Quelle streichen.
- **Stichworte:** politischer und rechtlicher Rahmen (zu prüfen)
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
