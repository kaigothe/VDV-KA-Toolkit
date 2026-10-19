# Quellenverzeichnis VDV-KA / eTicket / ABT

Sammlung aller Quellen aus der Bearbeitung der LVB-Bewerberaufgabe (Oktober 2026). Sie dient als Ausgangsbasis für ein VDV-KA-Lexikon.

**Legende Status**

| Kürzel | Bedeutung |
|---|---|
| ✅ gelesen | Inhalt wurde abgerufen und ausgewertet |
| 🔎 gefunden | Existenz per Suche bestätigt, Inhalt nicht (vollständig) gelesen |
| 🔒 nicht öffentlich | Wird in anderen Dokumenten referenziert, ist nur für Lizenznehmer verfügbar (VDV eTS / KA KG) |
| 📄 lokal | Liegt als Datei vor, nicht online verlinkt |

**Legende Typ:** `Primär` = Standardgeber (VDV/VDV eTS), `Projekt` = Pflichtenheft/Spezifikation eines Verbunds, `Hersteller` = Produkt- oder Anbieterseite, `Sekundär` = Fachartikel, Verband, Erklärseite

---

## 1. Primärquellen des Standardgebers (VDV / VDV eTicket Service)

### [Q01] VDV eTS – Einordnung von Account Based Ticketing
- **URL:** https://www.kcd-nrw.de/fileadmin/user_upload/VDV-ETSEinordungvonAccountBasedTicketingV1_6602929704990.pdf
- **Typ / Status:** Primär / ✅ gelesen
- **Stand:** Arbeitsdokument V1.0, 25.03.2024
- **Inhalt:** Abgrenzung von ABT (Account Based Ticketing) und MBT (mediumbasiertem Ticketing). Kernzitat: „Das Account-Based-Ticketing dreht die Logik des Speicherortes um.“ Behandelt werden außerdem ID-Token, Online-Kontrolle, die Abhängigkeit von Konnektivität und hybride Systeme, die Synchronisation bei MBT (typisch 24 h), die Vorteile von ABT, das London-Beispiel („quasi-anonym“) und die nötigen KA-Ausbaustufen 4 und 5.
- **Lexikon-Stichworte:** ABT, MBT, ID-Token, Nutzermedium, Ticket Cloud, Online-/Offline-Kontrolle, Hybridsystem

### [Q02] VDV eTS – Glossar VDV-KA / etiCORE
- **URL:** https://www.eticket-deutschland.de/media/glossary_vdv_ka_eticore.pdf
- **Typ / Status:** Primär / ✅ gelesen (ca. 100.000 von 108.000 Zeichen)
- **Inhalt:** Offizielles Begriffsverzeichnis der VDV-KA. Ausgewertet wurden unter anderem Aktionsmanagement und Aktionsliste („Liste von auszuführenden Aktionen am Akzeptanzterminal“) sowie die Aktionstypen Ausgabe EFS, Entsperren und Rücknahme EFS. Die Einträge „Synchronnummer“ und „Berechtigungsstatus“ fehlen.
- **Lexikon-Stichworte:** **Grundgerüst für das Lexikon**, vollständig auswerten

### [Q03] VDV eTS – Standard (Website)
- **URL:** https://www.eticket-deutschland.de/standard
- **Typ / Status:** Primär / 🔎 gefunden (robots.txt blockiert den automatischen Abruf, im Browser öffnen)
- **Inhalt:** Übersichtsseite zum Standard der VDV-Kernapplikation.
- **Lexikon-Stichworte:** Einstieg, Versionen, Dokumentenübersicht

### [Q04] VDV – Der Weg zur einheitlichen Fahrkarte (eTicket)
- **URL:** https://www.vdv.de/der-weg-zur-einheitlichen-fahrkarte-eticket.aspx
- **Typ / Status:** Primär / ✅ gelesen (Kurzprüfung)
- **Inhalt:** Aufbau von eTicket Deutschland, technische Grundlage, zentrale Dienste, Teilnahmeregeln.
- **Lexikon-Stichworte:** eTicket Deutschland, Teilnehmer, zentrale Dienste

### Nicht öffentliche KA-Spezifikationen 🔒
Diese Dokumente werden in [Q06] referenziert und sind die eigentliche Normquelle. Sie stehen Lizenznehmern zur Verfügung, möglicherweise auch intern bei der LVB.

| Kürzel | Titel | Versionen | Relevanz fürs Lexikon |
|---|---|---|---|
| KA_SPEC_BOM | Hauptdokument mit Basisobjektmodell (BOM) | 1.107 (08/2010), 1.3.0 | Datenobjekte, Codelisten (z. B. `IONTransaktionsTyp_CODE`, Status-Codes) |
| KA_SPEC_SST | Schnittstellenspezifikationen der Referenzsysteme KVP, DL, PV, AH, KOSE | 1.107, 1.3.0 (06/2014) | TX-Nachrichten (TXABER, TXEBER, TXSNAWB, …) |
| KA_SPEC_AktM | Aktionsmanagement | 1.107, 1.3.0 (06/2014) | Aktion, Aktionsliste (TXAML), Auftragstypen |
| KA_SPEC_SAM | Spezifikation des SAM | 1.107, 1.3.0 | Schlüssel, MAC, LOAD KEY, Zertifikate |
| KA_SPEC_MULTIBER | Multiberechtigungen | 1.3.0 | TXAMBER, TXEMBER, TXRMBER |
| KA_XSD | KA XML-Schema | 1.107 K20120104, 1.3.0 | Feldnamen, Datentypen, Namespaces |
| HD_BOM | Hauptdokument BOM, u. a. Abschnitt 6.7.2 „Kürzungsregel für Namen“ | – | Namensfelder, Anonymisierung |
| SysLH (z. B. SYSLH_RTDL_V1107, SYSLH_DLRT_V130) | Systemlastenhefte für Terminalabläufe | 1.107, 1.3.0 | Kontrolltransaktion, EXECUTE TRANSACTION |
| Anlage TLV EFS (V1.90) | TLV-Struktur des EFS, u. a. Tag 0xDB „Fahrgast“ | 1.90 | Hex-Dekodierung, Tags |

---

## 2. Projekt- und Verbundspezifikationen

### [Q05] RMV – vHGS Pflichtenheft PH 05 Systemspezifikation, Anhang 1: RMV-EFS
- **URL:** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_24_EFM_Anh_1a_vHGS_PH05-A1_RMV-EFS_v1.6_190415_MVU_200122.pdf
- **Typ / Status:** Projekt / 🔎 gefunden (der Abruf scheiterte, Inhalt **nicht** gelesen)
- **Stand:** v1.6, 15.04.2019, Cubic Transportation Systems / eTicket RheinMain
- **Inhalt (laut Sekundärangabe):** Datenstruktur RMV-EFS, Codelisten, darunter die berStatus-Codes 5 = zurückgenommen, 7 = aktiv/entsperrt, 8 = neu/nicht aktiv und 19 = gesperrt (Abschnitt 2.1, S. 8, **unverifiziert**), Transaktionstyp (Abschnitt 4.4.4), Aktionsmanagement (Abschnitt 5.4.6), TXABER-Inhalte, BerechtigungTarifbereichZusatz.
- **Lexikon-Stichworte:** berStatus, RMV-EFS, produktspezifischer Teil. **Mit hoher Priorität beschaffen.**

### [Q06] RMV – vHGS Pflichtenheft PH 06-02 Schnittstellenspezifikation Terminalmanagementsysteme (TMS)
- **Fundort:** 📄 lokal (Anlage 24, Anhang 2), vermutlich ebenfalls auf mtv-unternehmen.de
- **Typ / Status:** Projekt / ✅ gelesen (vollständig, 46 Seiten)
- **Stand:** v2.3, 09.11.2018, Cubic Transportation Systems
- **Inhalt:**
  - KA-Rollen und Datenflüsse für Sperr- und Aktionsmanagement (Kap. 1.2)
  - **Transaktionstypen 37/38/39** (Ausgabe, Entsperrung, Rückgabe EFS über Aktionsliste; Kap. 2.1.5, Fußnote 1)
  - proprietäre TX-Codes 252–254 für das Schlüsselmanagement
  - Sperrlisten TXSLNM/TXSLK/TXSLOS (ab KA 1.3.0 als *RESP-Varianten)
  - Kontrollnachweise TXEBER, TXKNAWA/B, TXKNAWDM
  - Aktionsliste TXAML, Nachweise TXABER/TXRBER/TXSNAWB
  - Ablauf von Upload und Paket-Quittung (TXA/TXB), MAC-Prüfung
  - Rollencodes (KVP = 1, DL = 2, PV = 3, AH = 4, KOSE = 5, ALISE = 31)
  - CV-Zertifikat-Keytypes 1–7
  - Duplikaterkennung über die IONTransaktion_ID
  - Kodierung von Nullwerten (Leerzeichen 0x20, OrtsTyp 0xFF)
  - Datenschutzvorgaben für TXEBER
  - Mobile Kontrolle ohne SAM (Sichtkontrolle)
- **Lexikon-Stichworte:** sehr ergiebig, eigener Exzerpt-Durchgang empfohlen

### [Q07] RMV – Statische Berechtigung RMV-EFS, Spezifikation Datenlayout
- **URL:** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_24_EFM_Anh_8_StatBer_RMV-EFS_v1.9_210804_MVU_211020.pdf
- **Typ / Status:** Projekt / 🔎 gefunden
- **Stand:** v1.9, 04.08.2021
- **Inhalt (vermutet):** Datenlayout für statische Berechtigungen (Barcode bzw. Sichtausweis) im RMV.
- **Lexikon-Stichworte:** statische Berechtigung, Barcode, VDV-Barcode

### [Q08] RMV – EFM-Integration vHGS
- **URL:** https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_25_EFM_Integration_vHGS_v2.7.0_20211105_MVU_211105.pdf
- **Typ / Status:** Projekt / 🔎 gefunden
- **Stand:** v2.7.0, 05.11.2021
- **Inhalt (vermutet):** Integration von Abo-Verwaltung, pVKS und vHGS, Zeitlinien, Kommunikation.
- **Lexikon-Stichworte:** Abo-Verwaltung, pVKS, Prozessketten (relevant für die Frage nach Status und Prüfprozess)

### [Q09] KCD NRW – Abbildung und Kontrolle des AVV-Tarifs
- **URL:** https://www.kcd-nrw.de/fileadmin/03_KC_Seiten/KCD/Downloads/Technische_Dokumente/20171013_Abbildung_und_Kontrolle_des_AVV-Tarifs_Version_1.1.pdf
- **Typ / Status:** Projekt / 🔎 gefunden
- **Stand:** Version 1.1, 13.10.2017
- **Inhalt (vermutet):** Abbildung eines Verbundtarifs (AVV Aachen) in der KA und Kontrolllogik.
- **Lexikon-Stichworte:** Tarifabbildung, Kontrolle, Produktdefinition

### [Q10] KCD NRW – Technische Anforderung Deutschlandticket (V1.4 / V1.5)
- **URLs:**
  - https://www.kcd-nrw.de/fileadmin/user_upload/Technische_Anforderung_Deutschlandticket_V1.5.pdf
  - https://www.kcd-nrw.de/fileadmin/user_upload/Technische_Anforderung_Deutschlandticket_V1.4.pdf
- **Typ / Status:** Projekt / 🔎 gefunden
- **Inhalt (vermutet):** Technische Vorgaben für das Deutschlandticket (KA-Chipkarte, Barcode, Kontrolle).
- **Lexikon-Stichworte:** Deutschlandticket, Produktabbildung, Barcode-Kontrolle

### [Q11] LVB – Bewerberaufgabe Spezialist Vertriebssoftware EFM
- **Fundort:** 📄 lokal (PDF, 13.10.2026)
- **Typ / Status:** Projekt / ✅ gelesen
- **Inhalt:** Beispiel einer echten KA-Transaktion `txalisber` (Namespace `http://vdv/ka/alise/2`) mit dem Produkt „ABO Azubi“ und drei realen Org-IDs. Die konkreten Werte stehen bewusst nicht in diesem Repository.
- **Lexikon-Stichworte:** Beispieldatensatz für alle Feldnamen (`amAuftragsTyp`, `berSynchronNummer`, `prodKeyOrganisation_ID`, …)

---

## 3. Hersteller- und Anbieterquellen

### [Q12] TapConnect – VDV Barcode Field Mappings
- **URL:** https://documentation.tapconnect.io/public/specs/vdv-barcode-field-mappings.html
- **Typ / Status:** Hersteller / ✅ gelesen
- **Inhalt:** Zuordnung von Feldern zum VDV-Barcode. Tag 0xDB „Fahrgast“ mit `efsFahrgastGeschlecht`, `efsFahrgastGeburtsdatum` (Standardwert 1970-01-01) und `efsFahrgastName` (Typ-1-Anonymisierung). Verweise auf die Anlage TLV EFS V1.90 und die HD_BOM 6.7.2.
- **Lexikon-Stichworte:** VDV-Barcode, TLV, Fahrgastdaten, Namenskürzung

### [Q13] Krauth Technology – KA Background System / Interfaces
- **URLs:**
  - https://www.krauth-technology.de/en/solutions/ticketing-software/background-software/ka-background-system
  - https://www.krauth-technology.de/en/solutions/ticketing-software/interfaces
- **Typ / Status:** Hersteller / 🔎 gefunden
- **Inhalt:** Produktbeschreibung eines KA-Hintergrundsystems und seiner Schnittstellen.
- **Lexikon-Stichworte:** Hintergrundsystem, KVP-/PV-System

### [Q14] eos.uptrade – eos.ticketingsuite VDV-KA-zertifiziert
- **URL:** https://www.eos-uptrade.de/en/company/news/article/eos-ticketingsuite-vdv-ka-certified
- **Typ / Status:** Hersteller / 🔎 gefunden
- **Inhalt:** Meldung zur KA-Zertifizierung einer Ticketing-Suite.
- **Lexikon-Stichworte:** Zertifizierung, Marktübersicht

### [Q15] IVU – Referenzen E-Ticketing / VDV-KA-Zertifizierung
- **URLs:**
  - https://www.ivu.com/news/details/ivu-reference-for-e-ticketing
  - https://www.ivu.com/all-references/references/vdv-ka-certification-for-ivu-hardware-and-software
- **Typ / Status:** Hersteller / 🔎 gefunden
- **Lexikon-Stichworte:** Zertifizierung, Marktübersicht

### [Q16] amcon – Customers & Use Cases
- **URL:** https://amcon.de/en/customers-use-cases/
- **Typ / Status:** Hersteller / 🔎 gefunden
- **Lexikon-Stichworte:** Kontrollgeräte, Anwendungsfälle

### [Q17] Ximedes – Account Based Ticketing
- **URL:** https://ximedes.com/public-transport/abt
- **Typ / Status:** Hersteller / 🔎 gefunden
- **Inhalt:** ABT-Plattform eines Anbieters, der an OVpay (Niederlande) beteiligt ist.
- **Lexikon-Stichworte:** ABT, OVpay

### [Q18] Kentkart – To validate, or not to validate
- **URL:** https://www.kentkart.com/?p=15641
- **Typ / Status:** Hersteller / 🔎 gefunden
- **Inhalt:** Validierungs- und Kontrollkonzepte im ABT.
- **Lexikon-Stichworte:** Validierung, Kontrolle, ABT

### [Q19] Ticketer – PAR Deny Lists
- **URL:** https://ticketer.com/en/did-you-know/par-deny-lists
- **Typ / Status:** Hersteller / 🔎 gefunden
- **Inhalt:** Sperrlisten auf Basis der PAR (Payment Account Reference) bei bankkartenbasiertem ABT.
- **Lexikon-Stichworte:** Deny List, PAR, EMV-Token, Offline-Kontrolle

### [Q20] Genfare – Hand Held Validator
- **URL:** https://genfare.com/products/hand-held-validator/
- **Typ / Status:** Hersteller / 🔎 gefunden
- **Lexikon-Stichworte:** Kontrollgerät, Offline-Validierung

---

## 4. Sekundärquellen (Verbände, Fachartikel)

### [Q21] OSPT Alliance – Account-Based Ticketing
- **URL:** https://osptalliance.org/account-based-ticketing/
- **Typ / Status:** Sekundär / 🔎 gefunden
- **Inhalt:** Einordnung von ABT aus Sicht der CIPURSE/OSPT-Allianz.
- **Lexikon-Stichworte:** ABT, Sicherheitsmedien

### [Q22] UITP – Demystifying Ticketing and Payment in Public Transport
- **URL:** https://www.uitp.org/publications/demystifying-ticketing-and-payment-in-public-transport/
- **Typ / Status:** Sekundär / ✅ gelesen (Kurzprüfung)
- **Inhalt:** Überblick über Ticketing- und Zahlungstechnologien sowie Trends.
- **Lexikon-Stichworte:** internationale Begriffe, EMV, ABT, CiCo

### [Q23] UK Authority – Transport Scotland ABT Back Office
- **URL:** https://www.ukauthority.com/articles/transport-scotland-aims-for-back-office-upgrade/
- **Typ / Status:** Sekundär / 🔎 gefunden
- **Lexikon-Stichworte:** ABT-Beschaffung, Praxisbeispiel

### [Q24] Bundestag-Drucksache 18/11086
- **URL:** https://dserver.bundestag.de/btd/18/110/1811086.pdf
- **Typ / Status:** Sekundär / 🔎 gefunden (Bezug zum eTicket ungeprüft)
- **Lexikon-Stichworte:** politischer und rechtlicher Rahmen (prüfen)

---

## 5. Hinweise für den Aufbau des Lexikons mit Claude Code

**Vorschlag für die Repo-Struktur:**

```
vdv-ka-lexikon/
├── CLAUDE.md               # Regeln: Quellenpflicht, Status-Kennzeichnung, Sprache
├── QUELLEN.md              # diese Datei
├── quellen/                # lokale PDFs (nur eigene bzw. öffentlich erlaubte Kopien!)
├── exzerpte/               # je Quelle ein Exzerpt mit Seitenangaben (Q06.md, Q02.md, …)
└── lexikon/
    ├── A/Aktionsliste.md
    ├── A/ALISE.md
    ├── B/berStatus.md
    └── …
```

**Vorschlag für eine Eintragsvorlage:**

```markdown
# <Begriff>
**Kurzdefinition:** …
**Englisch / Abkürzung:** …
**Kontext:** Rolle / Nachricht / Feld / Codeliste
**Details:** …
**Codewerte:** (falls Codeliste; mit Quelle je Wert)
**Beispiel:** (z. B. aus Q11)
**Verwandte Begriffe:** [[…]]
**Quellen:** [Q06, Kap. 2.1.5, S. 13]
**Status:** belegt | abgeleitet | zu prüfen
```

**Empfohlene Reihenfolge:**

1. **Q02** (Glossar) als Begriffsgerüst.
2. **Q06** (PH 06-02) für Rollen, Nachrichten und Codes.
3. **Q05** (PH 05-A1) beschaffen, um berStatus und den EFS-Aufbau zu belegen.
4. **Q01** für ABT.

**Hinweis zum Urheberrecht:** Die RMV- und VDV-Dokumente sind zum Teil als „Vertraulich“ gekennzeichnet. Im Repo nur Exzerpte und Verweise ablegen, keine Volltexte. Ein öffentliches Repo sollte keine Kopien der PDFs enthalten.
