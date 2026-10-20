# Struktur: Begriffsbaum des VDV-KA-Lexikons

**Stand:** 2026-10-19 · **Zielbild:** 97 P1-Artikel (10 Kategorieartikel + 87 Blattartikel) · **Startmenge Phase 1–3: 66 Artikel** (Begründung und Schnitt in Abschnitt 11) · dazu 24 P2 und 7 P3 sowie der Backlog in Abschnitt 13.

Dieses Dokument ist der verbindliche Bauplan. Jeder Eintrag nennt den geplanten Dateipfad, die Hauptquelle mit Fundstelle und die Priorität. Die Begründungen für die Entscheidungen stehen in [PLAN.md](PLAN.md), die Grenzfälle in Abschnitt 12.

**Prioritäten**

| Prio | Bedeutung |
|---|---|
| **P1** | Kernbegriff. Ohne ihn ist das Lexikon nicht benutzbar; Beleglage ausreichend. |
| **P2** | Wichtig, aber erst nach den Exzerpten sinnvoll zu schreiben. |
| **P3** | Backlog. Vollständigkeit, nicht Verständnis. |

**Pfadkonvention** — Kategorieartikel liegt neben seinem Ordner (siehe [PLAN.md](PLAN.md), E1):

```
lexikon/aktionsmanagement.md        ← Kategorieartikel
lexikon/aktionsmanagement/…         ← Unterartikel
```

---

## 1. Grundlagen

**Kategorie:** `lexikon/grundlagen.md` · P1 · Quellen: [Q02](QUELLEN.md#q02) S. 50, [Q04](QUELLEN.md#q04), [Q25](QUELLEN.md#q25)

| Artikel | Pfad (unter `lexikon/grundlagen/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| VDV-Kernapplikation | `vdv-kernapplikation.md` | Q02 S. 50 „Kernapplikation / etiCORE“; Q04 | **P1** |
| eTicket Deutschland | `eticket-deutschland.md` | Q25 Kap. 4 „Markenbuch“ (PDF-S. 39 ff.); Q04 | **P1** |
| Elektronisches Fahrgeldmanagement (EFM) | `efm.md` | Q02 S. 36 | **P1** |
| KA-Versionen und Releases | `versionen.md` | Q02 S. 2 „Releases“; Q25 Kap. 3 (Hinweise „entfallen ab Release 1.6.0“); Q29 | **P1** |
| Ausbauvarianten | `ausbauvarianten.md` | Q25, Anlage 2 Migrationsszenarien, PDF-S. 159 | **P1** |
| Verzeichnis der KA-Spezifikationen | `ka-spezifikationen.md` | Q25 Kap. 3, PDF-S. 35 ff. (Inventarnummern 0–59) | **P1** |
| (((etiCORE / KA-Version 3 | `eticore.md` | Q02 S. 50; Q27 — **O7** | P2 |
| Interoperabilität | `interoperabilitaet.md` | Q02 S. 48, S. 49 (Interoperabilitätsnetzwerk) | **P1** |
| Teilnahmevertrag und Regelwerk | `teilnahmevertrag.md` | Q02 S. 94; Q25 (Mustervertrag) | P2 |
| Elementarprozess | `elementarprozess.md` | Q02 S. 38; Q25 Kap. 5 (Prozesslisten je Rolle) | **P1** |
| Zertifizierung | `zertifizierung.md` | Q02 S. 100; Q14, Q15 (Marktpraxis) | P2 |

---

## 2. Rollen und Organisationen

**Kategorie:** `lexikon/rollen.md` · P1 · Quellen: [Q02](QUELLEN.md#q02) S. 58 ff., [Q06](QUELLEN.md#q06) Kap. 1.2, 4.10

| Artikel | Pfad (unter `lexikon/rollen/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| Kundenvertragspartner (KVP) | `kvp.md` | Q02 S. 58; Q06 Kap. 1.2.2 | **P1** |
| Produktverantwortlicher (PV) | `pv.md` | Q02 S. 74 | **P1** |
| Dienstleister (DL) | `dl.md` | Q02 S. 34 | **P1** |
| Applikationsherausgeber (AH) | `ah.md` | Q02 S. 23 | **P1** |
| Kontroll- und Sperrlistenservice (KOSE) | `kose.md` | Q02 S. 53 | **P1** |
| Aktionslistenservice (ALISE) | `alise.md` | Q02 S. 21; Q06 Kap. 4.10 (Rollencode 31) | **P1** |
| Rollencodes | `rollencodes.md` | Q06 Kap. 4.10: KVP 1, DL 2, PV 3, AH 4, KOSE 5, ALISE 31 — **verbundspezifisch, O1** | **P1** |
| Organisations-ID | `organisations-id.md` | Q02 S. 69 | **P1** |
| Hintergrundsystem | `hintergrundsystem.md` | Q02 S. 46; Q13 (Marktpraxis) | **P1** |
| Akzeptanzterminal | `akzeptanzterminal.md` | Q02 S. 21 | **P1** |
| Beauftragender und ausführender KVP | `kvp-rollenvarianten.md` | Q02 S. 26, S. 30, S. 45, S. 72; Q06 Kap. 1.2.2 („beauftragender KVP“) | P2 |
| Zentrale Vermittlungsstelle | `zentrale-vermittlungsstelle.md` | Q02 S. 99 | P2 |
| Gemeinsame Servicestelle | `gemeinsame-servicestelle.md` | Q02 S. 45 | P3 |
| Scheme Manager | `scheme-manager.md` | Q02 S. 78 | P3 |

**Bündelung:** `kvp-rollenvarianten.md` fasst Primär-, Fremd-, beauftragenden und ausführenden KVP zusammen. Sie haben zwar je einen Glossareintrag, unterscheiden sich aber nur in der Rolle zum selben Begriff; vier Artikel wären Redundanz. Das weicht bewusst von Kriterium 1 in [PLAN.md](PLAN.md) E7 ab.

---

## 3. Medien und Applikationen

**Kategorie:** `lexikon/medien.md` · P1 · Quellen: [Q02](QUELLEN.md#q02) S. 22, S. 66

| Artikel | Pfad (unter `lexikon/medien/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| Nutzermedium (NM) | `nutzermedium.md` | Q02 S. 66 | **P1** |
| Applikation | `applikation.md` | Q02 S. 22 | **P1** |
| Applikationsinstanz | `applikationsinstanz.md` | Q02 S. 24; Q11 (Feld `appInstanz_ID`) | **P1** |
| Applikations-Kennung | `applikations-kennung.md` | Q02 S. 24 | P2 |
| Lebenszyklus der Applikation | `lebenszyklus-applikation.md` | Q02 S. 17 (Aktivieren), S. 27 (Ausgabe), S. 46 (Initialisierung), S. 70 (Personalisierung) | **P1** |
| Kartentyp | `kartentyp.md` | Q02 S. 50 | P3 |
| Personengebunden | `personengebunden.md` | Q02 S. 71; Q11 (Name und Geburtsdatum im produktspez. Teil) | **P1** |
| Fehlbedienungszähler | `fehlbedienungszaehler.md` | Q02 S. 44 | P3 |

**Bündelung:** `lebenszyklus-applikation.md` fasst Initialisierung, Ausgabe, Personalisierung und Aktivierung zusammen — vier Glossareinträge, die nur gemeinsam verständlich sind, weil sie Stationen eines Ablaufs beschreiben.

---

## 4. Berechtigungen und Produkte

**Kategorie:** `lexikon/berechtigungen.md` · P1 · Quellen: [Q02](QUELLEN.md#q02) S. 30, S. 73, [Q05](QUELLEN.md#q05), [Q35](QUELLEN.md#q35)

| Artikel | Pfad (unter `lexikon/berechtigungen/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| Berechtigung | `berechtigung.md` | Q02 S. 30 | **P1** |
| Elektronischer Fahrschein (EFS) | `efs.md` | Q02 S. 37 | **P1** |
| Produkt | `produkt.md` | Q02 S. 73; Q35 S. 1 ff. | **P1** |
| Produktnummer und Produkt-ID | `produktnummer.md` | Q35 (Wertebereich bis 65535, Zuordnung zum PV); Q25 Kap. 3 Inv. 35 (KA PROD_ID-ANW); Q11 (`prodProdukt_ID` als Paar aus Nummer und Organisation) | **P1** |
| berStatus | `berstatus.md` | Q05 Abschn. 2.1 (RMV-Codes 5/7/8/19) — **verbundspezifisch, O3** | **P1** |
| berSynchronNummer | `bersynchronnummer.md` | Q11 (Feld, Wert 1); **nicht im Glossar** — Deutung als Versionszähler ist abgeleitet, **O5** | **P1** |
| Gültigkeit | `gueltigkeit.md` | Q11 (`berGueltigkeitsbeginn`/`-ende`); Q35 (Vertriebs- und Gültigkeitsdaten, Vorverkaufsbeginn) | **P1** |
| Produktspezifischer Teil | `produktspezifischer-teil.md` | Q05 (Datenstruktur RMV-EFS); Q12 (Tag 0xDB) | **P1** |
| Statische Berechtigung | `statische-berechtigung.md` | Q02 S. 92; Q07; Q25 Kap. 3 Inv. 42 (KA STB-Spec) | **P1** |
| Multiberechtigung | `multiberechtigung.md` | Q25 Kap. 3 Inv. 40 (KA MultiBER-SPEC), Anlage 2 (Ergänzung MultiBER); Q06 (TXAMBER/TXEMBER/TXRMBER) | **P1** |
| Bezahlart | `bezahlart.md` | Q02 S. 31; Q11 (`berBezahlArt` 0, `berBezahlMittel`) | P2 |
| Tarifprodukt und Tarif | `tarif.md` | Q02 S. 93, S. 94; Q09, Q31, Q32 | P2 |
| Referenz-Berechtigung | `referenz-berechtigung.md` | Q02 S. 75 | P3 |
| Werteinheitenberechtigung | `werteinheitenberechtigung.md` | Q02 S. 98, S. 97 (ÖPV-Werteinheit), S. 99 (WE-preload/postload) | P3 |
| Fahrtberechtigung | `fahrtberechtigung.md` | Q02 S. 42 | P2 |

---

## 5. Transaktionen und Nachrichten

**Kategorie:** `lexikon/transaktionen.md` · P1 · Quellen: [Q02](QUELLEN.md#q02) S. 96, [Q06](QUELLEN.md#q06) Kap. 3, 4.3, 5

| Artikel | Pfad (unter `lexikon/transaktionen/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| Transaktion | `transaktion.md` | Q02 S. 96 | **P1** |
| Nachweis | `nachweis.md` | Q02 S. 64; S. 39 (Entsperrnachweis), S. 61 (Leistungsnachweis), S. 90 (Sperrnachweis) | **P1** |
| TX_BASE (Transaktionskopf) | `tx-base.md` | Q06 Kap. 5.4 (optionale Signaturfelder `transSignatur…`) | **P1** |
| logTransaktionsTyp | `logtransaktionstyp.md` | Q06 Kap. 2.1.5 Fußnote 1 (37/38/39), proprietäre Codes 252–254 — **O1** | **P1** |
| TXABER | `txaber.md` | Q06 Kap. 4.3, 4.3.1 | **P1** |
| TXRBER | `txrber.md` | Q06 Kap. 4.3 | **P1** |
| TXSNAWB | `txsnawb.md` | Q06 Kap. 4.3 | **P1** |
| TXEBER | `txeber.md` | Q06 Kap. 4.3; Datenschutzvorgaben | **P1** |
| TXAML (Aktionsliste als Nachricht) | `txaml.md` | Q06 Kap. 2.1.5, 4.3.1; verweist auf KA_SPEC_AktM | **P1** |
| txalisber | `txalisber.md` | Q11 (Elementname, Namespace `http://vdv/ka/alise/2`) — Deutung „ALISE-Eintrag Berechtigung“ ist **abgeleitet** | **P1** |
| TXA / TXB (Quittung und Ablehnung) | `txa-txb.md` | Q06 Kap. 3.1 (Ablehnung bei negativer MAC-Prüfung oder inkonsistenten Daten) | **P1** |
| Duplikaterkennung | `duplikaterkennung.md` | Q06 Kap. 5.3 (IONTransaktion_ID aus Org-ID + Rollencode + Sequenznummer samt Wiederholungszähler) | **P1** |
| Interoperabilitätsnetzwerk (ION) | `ion.md` | Q02 S. 49; Q25 Kap. 3 Inv. 9 (KA ION-SPEC), Inv. 39 (KA IONA-Spec) | P2 |
| Transaktionsprüfung | `transaktionspruefung.md` | Q25 Kap. 3 Inv. 33 (KA TXx-Prüfungs-ANW); Q06 Kap. 3.1 | P2 |

---

## 6. Aktionsmanagement

**Kategorie:** `lexikon/aktionsmanagement.md` · P1 · Quellen: [Q02](QUELLEN.md#q02) S. 18–21, [Q06](QUELLEN.md#q06) Kap. 1.2.2, 2.1.5, [Q25](QUELLEN.md#q25) Kap. 5

| Artikel | Pfad (unter `lexikon/aktionsmanagement/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| Aktion | `aktion.md` | Q02 S. 18 | **P1** |
| Aktionsliste | `aktionsliste.md` | Q02 S. 19 („Liste von auszuführenden Aktionen am Akzeptanzterminal“); Q06 Kap. 2.1.5, 3.2 (täglicher Zyklus) | **P1** |
| Aktionsdifferenzliste | `aktionsdifferenzliste.md` | Q25 Kap. 5 („Aktionsdifferenzliste anfordern und empfangen“) | **P1** |
| Terminalaktionsliste | `terminalaktionsliste.md` | Q25 Kap. 5 („Terminalaktionslisten bereitstellen“); Q06 Kap. 2.1.5 (im RMV zunächst nicht eingesetzt) | **P1** |
| Auftragstyp (`amAuftragsTyp`) | `auftragstyp.md` | Q11 (Wert 13) — **unbelegt, O2, O9** | **P1** |
| Ausgabe EFS über Aktionsliste (TX 37) | `ausgabe-efs-ueber-aktionsliste.md` | Q06 Kap. 2.1.5 Fußnote 1; Q02 S. 19; Q25 Kap. 5 | **P1** |
| Entsperrung über Aktionsliste (TX 38) | `entsperrung-ueber-aktionsliste.md` | Q06 Kap. 2.1.5 Fußnote 1; Q02 S. 19, S. 38 | **P1** |
| Rücknahme EFS über Aktionsliste (TX 39) | `ruecknahme-efs-ueber-aktionsliste.md` | Q06 Kap. 2.1.5 Fußnote 1; Q02 S. 19 | **P1** |
| Aktionsfreigabe | `aktionsfreigabe.md` | Q25 Kap. 5 („Aktionsfreigabe senden“, „Aktionsfreigabemitteilung entgegennehmen“) | **P1** |
| Aktionsclearing | `aktionsclearing.md` | Q02 S. 18 | **P1** |
| Entsperrnachweis | `entsperrnachweis.md` | Q02 S. 39; Q25 Kap. 5 („Entsperrnachweis bearbeiten“, „… an PV melden“) | **P1** |
| Änderungsreferenz | `aenderungsreferenz.md` | Q11 (`amAenderungsreferenz_ID` = 0/0); Q50 (etiCORE: `groupId`, Gruppe von Einträgen) — Deutung **abgeleitet** | **P1** |
| Terminalgruppe | `terminalgruppe.md` | Q25 Kap. 5 („TG_Terminal anlegen/entfernen/ändern“); Q11 (`amTerminalGruppe_ID`, `amTerminal_ID` = 0) | P2 |
| Lebenszyklus einer Aktion | `lebenszyklus-aktion.md` | Q02 S. 20 (Aktionen haben einen Lebenszyklus); Q06 Kap. 1.2.2 (Datenfluss) | P2 |

---

## 7. Sperr- und Kontrollmanagement

**Kategorie:** `lexikon/kontrolle.md` · P1 · Quellen: [Q02](QUELLEN.md#q02) S. 52, S. 82–91, [Q06](QUELLEN.md#q06), [Q33](QUELLEN.md#q33)

| Artikel | Pfad (unter `lexikon/kontrolle/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| ~~Kontrolle~~ | *entfallen* | Der Begriff ist im Kategorieartikel `lexikon/kontrolle.md` erklärt — das ist die natürliche Stelle und vermeidet den Pfad `kontrolle/kontrolle.md`. Stattdessen ist `kontrollgeraet.md` von P2 auf P1 gezogen. | — |
| Sperrung und Entsperrung | `sperrung.md` | Q02 S. 91, S. 38 | **P1** |
| Sperrliste | `sperrliste.md` | Q02 S. 89; Q06 (TXSLNM/TXSLK/TXSLOS, ab KA 1.3.0 als *RESP-Varianten), Kap. 3.2 | **P1** |
| Sperrlisteneintrag und Sperrobjekt | `sperrlisteneintrag.md` | Q02 S. 89, S. 90 | **P1** |
| Sperrgrund | `sperrgrund.md` | Q02 S. 88 | **P1** |
| Sperranforderung und Sperrauftrag | `sperranforderung.md` | Q02 S. 82, S. 84, S. 86, S. 87 | P2 |
| Sperrnachweis | `sperrnachweis.md` | Q02 S. 90 | **P1** |
| Kontrollnachweise (TXKNAWA/B, TXKNAWDM) | `kontrollnachweise.md` | Q06 Kap. 4.3 | **P1** |
| Kontrollgerät | `kontrollgeraet.md` | Q02 S. 22; Q06 Kap. 6.1; Q33 Kap. 7.1; Q16, Q20 (Marktpraxis) | **P1** |
| Sichtkontrolle (mobile Kontrolle ohne SAM) | `sichtkontrolle.md` | Q06 (mobile Kontrolle ohne SAM); Q33 | **P1** |
| Entwertung | `entwertung.md` | Q02 S. 39 | P2 |
| Erhöhtes Beförderungsentgelt | `erhoehtes-befoerderungsentgelt.md` | Q02 S. 42 | P3 |

---

## 8. Sicherheit und Schlüssel

**Kategorie:** `lexikon/sicherheit.md` · P1 · Quellen: [Q02](QUELLEN.md#q02) S. 51, S. 80 f., [Q06](QUELLEN.md#q06) Kap. 5.1.2

| Artikel | Pfad (unter `lexikon/sicherheit/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| MAC (Message Authentication Code) | `mac.md` | Q06 Kap. 3.1, 5.1.2 | **P1** |
| Schlüsselreferenz | `schluesselreferenz.md` | Q11 (`amMKPV-NM-MAC_ID`, `amMKKVP-NM-MAC_ID`, `amMKERF-NM-MAC_ID` mit Nummer, Version, Inhaber) | **P1** |
| SAM (Secure Application Module) | `sam.md` | Q02 S. 80; Q25 Kap. 3 Inv. 8 (KA SAM-SPEC), Inv. 59 (SAM-Server) | **P1** |
| Keymanagement | `keymanagement.md` | Q02 S. 51; S. 79 (Schlüsselregister) | **P1** |
| Symmetrische und asymmetrische Schlüssel | `schluesselarten.md` | Q02 S. 25, S. 68, S. 73, S. 92 | **P1** |
| CV-Zertifikat | `cv-zertifikat.md` | Q06 (Keytypes 1–7); Q02 S. 100 (ZSAM-Zertifikat) | **P1** |
| Public Key Infrastructure (PKI) | `pki.md` | Q02 S. 71; S. 31 (Certification Authority), S. 77 (Registrierung) | P2 |
| Sicherheitsebenen und 1GSI/2GSI | `sicherheitsebenen.md` | Q02 S. 14 f. (1GSI bis 2026/2031, 2GSI ab 2026 — **O8**), S. 81 | **P1** |
| Authentifizierung | `authentifizierung.md` | Q02 S. 29 | P2 |

---

## 9. Datenformate und Kodierung

**Kategorie:** `lexikon/datenformate.md` · P1 · Quellen: [Q06](QUELLEN.md#q06) Kap. 5.2, [Q12](QUELLEN.md#q12), [Q25](QUELLEN.md#q25) Kap. 3

| Artikel | Pfad (unter `lexikon/datenformate/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| XML-Schema (XSD) und WSDL | `xsd.md` | Q25 Kap. 3 Inv. 5 (KA XML-Schemata und WSDL) | **P1** |
| XML-Namespace | `namespace.md` | Q11 (`http://vdv/ka/alise/2`) — Releasezuordnung **O4** | **P1** |
| TLV-Kodierung | `tlv.md` | Q02 S. 96 (TLV-EFS); Q25 Kap. 3 Inv. 2 (Anlage TLV EFS); Q11 (Längenabweichung **O6**) | **P1** |
| Tag 0xDB „Fahrgast“ | `tag-db-fahrgast.md` | Q12 (`efsFahrgastName`, `efsFahrgastGeburtsdatum`, `efsFahrgastGeschlecht`) | **P1** |
| Kodierung von Nullwerten | `nullwerte.md` | Q06 Kap. 5.2 (PrintableString 0x20, OrtsTyp 0xFF) | **P1** |
| Kürzungsregel für Namen | `namenskuerzung.md` | Q12 (Typ-1-Anonymisierung, Verweis auf HD_BOM Abschn. 6.7.2) | **P1** |
| VDV-Barcode | `vdv-barcode.md` | Q25 Kap. 3 Inv. 42 (KA STB-Spec); Q12; Q07 | **P1** |
| UIC-Barcode und Abgrenzung | `uic-barcode.md` | Q34; Q10c | P2 |
| Basisobjektmodell (BOM) | `bom.md` | Q25 Kap. 3 Inv. 1 (KA BOM-SPEC) | **P1** |
| Datentypen und Bytestrings | `datentypen.md` | Q06 Kap. 5.2; Q35 (Format- und Wertangaben) | P2 |

---

## 10. Account Based Ticketing

**Kategorie:** `lexikon/abt.md` · P1 · Quellen: [Q01](QUELLEN.md#q01), [Q30](QUELLEN.md#q30)

| Artikel | Pfad (unter `lexikon/abt/`) | Hauptquelle, Fundstelle | Prio |
|---|---|---|---|
| Account Based Ticketing (ABT) | `abt-begriff.md` | Q02 S. 16; Q01; Q30 | **P1** |
| Mediumbasiertes Ticketing (MBT) | `mbt.md` | Q01 (Abgrenzung, Synchronisation typisch 24 h) | **P1** |
| ID-Token | `id-token.md` | Q01 | **P1** |
| Ticket Cloud | `ticket-cloud.md` | Q01 | **P1** |
| Online- und Offline-Kontrolle | `online-offline-kontrolle.md` | Q01 (Abhängigkeit von Konnektivität); Q18 | **P1** |
| Hybridsystem | `hybridsystem.md` | Q01 | **P1** |
| Deny List und PAR | `deny-list.md` | Q19 (Payment Account Reference) — Herstellerquelle, **zu prüfen** | **P1** |
| Post-Validation | `post-validation.md` | Q18; Q01 — teils **abgeleitet** | P2 |
| Check-in/Check-out und Bestpreis | `cico.md` | Q36 (eTarife NRW); Q02 S. 32 (Check-In innerhalb einer Reise), S. 47 (IN-OUT System) | P2 |
| Internationale Beispiele | `internationale-beispiele.md` | Q01 (London); Q17 (OVpay); Q23 (Transport Scotland); Q22 | P2 |
| ABT in der VDV-KA | `abt-in-der-ka.md` | Q30; Q25 Anlage 2 (Ausbauvarianten 3, 3a) — **zu prüfen** | P2 |

---

## 11. Zählung der Startmenge

| Kategorie | P1-Blattartikel | P2 | P3 | in der Startmenge? |
|---|---:|---:|---:|---|
| Grundlagen | 8 | 3 | 0 | **ja** |
| Rollen und Organisationen | 10 | 2 | 2 | **ja** |
| Berechtigungen und Produkte | 10 | 3 | 2 | **ja** |
| Transaktionen und Nachrichten | 12 | 2 | 0 | **ja** |
| Aktionsmanagement | 12 | 2 | 0 | **ja** |
| Datenformate und Kodierung | 8 | 2 | 0 | **ja** |
| Medien und Applikationen | 5 | 1 | 2 | Phase 4 |
| Sperr- und Kontrollmanagement | 8 | 3 | 1 | Phase 4 |
| Sicherheit und Schlüssel | 7 | 2 | 0 | Phase 4 |
| Account Based Ticketing | 7 | 4 | 0 | Phase 4 |
| **Summe** | **87** | **24** | **7** | |

Alle P1 zusammen sind **97 Artikel** (87 Blattartikel + 10 Kategorieartikel) und damit mehr als die angepeilten 40–80.

**Vorschlag für den Schnitt:** Die Startmenge der Phasen 1 bis 3 umfasst die sechs oben mit „ja“ markierten Kategorien, also **60 Blattartikel + 6 Kategorieartikel = 66 Artikel**. Das ist genau der Kern, den das spätere Analysewerkzeug braucht, um eine `txalisber`-Nachricht Feld für Feld zu erklären: Rollen und Org-IDs, Berechtigungs- und Produktfelder, Transaktionstypen, Aktionsmanagement und die Kodierung.

Medien, Kontrolle, Sicherheit und ABT folgen in Phase 4 (31 Blattartikel + 4 Kategorieartikel). Das hat einen inhaltlichen Grund und nicht nur einen zeitlichen: Für Sicherheit und Kontrolle ist die Beleglage dünner, und ABT hängt an der Auswertung des Weißbuchs [Q30](QUELLEN.md#q30), die noch aussteht.

---

## 12. Grenzfälle und ihre Zuordnung

Jeder Begriff hat genau einen Platz im Baum. Begriffe, die in mehrere Zweige passen, werden anderswo über `siehe_auch` verlinkt. Die Entscheidungen:

| Begriff | Zugeordnet zu | Begründung | Querverweis von |
|---|---|---|---|
| **ALISE** | `rollen/alise.md` | ALISE ist eine KA-Rolle mit eigenem Rollencode (31, Q06 Kap. 4.10). Dass sie Aktionslisten bereitstellt, ist ihre Aufgabe, nicht ihre Natur. | `aktionsmanagement.md`, `transaktionen/txalisber.md` |
| **SAM** | `sicherheit/sam.md` | Das SAM ist physisch im Terminal, seine Funktion aber durchgängig kryptografisch (MAC-Bildung, Schlüsselhaltung). Die Zuordnung folgt der Funktion. | `medien.md`, `kontrolle/sichtkontrolle.md` |
| **Entsperrung** | zwei Artikel | `kontrolle/sperrung.md` erklärt den **Zustandswechsel**, `aktionsmanagement/entsperrung-ueber-aktionsliste.md` den **Transaktionstyp 38**. Zwei verschiedene Sachen mit verschiedenen Quellen. | gegenseitig |
| **Duplikaterkennung** | `transaktionen/duplikaterkennung.md` | Beruht auf der IONTransaktion_ID, also auf der Transaktionsidentität — nicht auf Kryptografie. | `sicherheit.md` |
| **Statische Berechtigung** | `berechtigungen/statische-berechtigung.md` | Sie ist eine Berechtigungsart; der Barcode ist nur ihr Träger. | `datenformate/vdv-barcode.md` |
| **Nachweis** | `transaktionen/nachweis.md` | Oberbegriff für Entsperr-, Leistungs-, Sperr- und Kontrollnachweis. Alle sind Transaktionen; sie dort zu sammeln hält die Nachweisartikel beieinander. | `kontrolle.md`, `aktionsmanagement.md` |
| **Kontrolle** | `kontrolle/kontrolle-begriff.md` | Der Kategoriename ist „Sperr- und Kontrollmanagement“; der gleichnamige Fachbegriff braucht trotzdem einen eigenen Artikel. Dateiname mit Zusatz `-begriff`, damit er nicht mit dem Kategorieartikel kollidiert. | — |
| **Produktnummer** | `berechtigungen/produktnummer.md` | Eindeutig nur zusammen mit der Organisation (Q11). Gehört damit zum Produkt, nicht zu den Rollen. | `rollen/organisations-id.md` |
| **Interoperabilitätsnetzwerk** | `transaktionen/ion.md` | Das ION ist der Transportweg der Transaktionen. Der Begriff *Interoperabilität* dagegen ist ein Grundlagenthema. | `grundlagen/interoperabilitaet.md` |
| **Online-/Offline-Kontrolle** | `abt/online-offline-kontrolle.md` | Die Frage stellt sich fachlich erst im ABT. Die mediumbasierte Kontrolle ist in `kontrolle/` beschrieben. | `kontrolle.md` |

---

## 13. Backlog

Begriffe aus [Q02](QUELLEN.md#q02), die noch keinen Platz haben. Sie werden aufgenommen, sobald ein Artikel sie braucht oder die Quellenlage es erlaubt.

**Kunde und Vertrag:** Kunde (S. 55), Kundendaten (S. 55), Kundenmedium (S. 55), Kundenpräferenzen (S. 56), Kundenprofil (S. 56), Kundenservice (S. 57), Kundenvertrag (S. 57), Beförderungsvertrag (S. 31), Nutzer (S. 66)

**Erfassung und Fahrt:** Erfassung (S. 40), Erfassungsdaten (S. 41), Erfassungsterminal (S. 41), Fahrt (S. 44), Fahrtabschnitt (S. 44), Reise (S. 78), Automatisierte Fahrpreisermittlung (S. 42), Nutzungszähler bei AFE (S. 67), Verspätungszeitzähler (S. 97)

**Bezahlen:** eBezahlberechtigung (S. 15), Abschlagsbetrag (S. 16), Autoload (S. 27), Prepaid-Konto (S. 71), Postpaid-Konto (S. 73), Forderungsclearing (S. 33), Produktclearing (S. 74), ÖPV-Werteinheit (S. 68)

**Systeme und Umgebungen:** KVP-System (S. 60), KVP-Terminal (S. 61), KVP-Personalisierungseinheit (S. 59), KVP-Vertriebseinheit (S. 60), DL-System (S. 34), DL-Terminal (S. 35), Vertriebsterminal (S. 97), Referenzsystem und Referenzterminal (S. 76), Level 1/2/3-Umgebungen (S. 62 f.), Notfallversion (S. 65), Regulärversion (S. 77)

**Weiteres:** Chipkarten-Übertragungsprotokoll (S. 32), Persönliche Identifikationsnummer (S. 69), Nutzertarifparameter (S. 67), Start Key / Session Key (S. 91), Secure Crypto Environment (S. 81), Motics / Mobile Ticketing Crypto Service (S. 64), Einheitliche Kundenschnittstelle KUSCH (Q25 Inv. 29), Produkt- und Kontrollmodule PKM (Q25 Inv. 53–57), LuKA-Spezifikationen für NFC-Mobiltelefone (Q25 Inv. 44–49), Wide Range (S. 99), Ticket (S. 95)

**Aus dem Analysewerkzeug heraus zu ergänzen:** `prodAbrechnungsVerfahren`, `berInfoText`, `logTransaktionsOperator_ID`, `prodKeyOrganisation_ID`, `berBezahlMittel` — jeweils sobald eine Codeliste vorliegt.

---

## 14. Stand nach dem Review (2026-10-19)

Alle zehn Kategorien sind geschrieben: **99 Artikel** — 10 Kategorieartikel und 89 Blattartikel. Das liegt über der geplanten Startmenge von 66, weil die Kategorien Medien, Datenformate, Kontrolle, Sicherheit und ABT vorgezogen wurden.

**Abweichungen vom Bauplan oben**, jeweils mit Grund:

| Geplant | Umgesetzt | Grund |
|---|---|---|
| `kontrolle/kontrolle-begriff.md` | entfallen | Der Begriff steht im Kategorieartikel [lexikon/kontrolle.md](lexikon/kontrolle.md) — die natürliche Stelle, und der Pfad `kontrolle/kontrolle.md` wäre verwirrend. |
| `kontrolle/kontrollgeraet.md` als P2 | P1 | Ergibt sich zwingend aus der Sichtkontrolle und ist über Q06 Kap. 6.1 gut belegt. |
| — | `abt/account.md` | Der Account ist die erste Basisanforderung des Weißbuchs und das Gegenstück zum ID-Token. |
| `abt/abt-in-der-ka.md` als P2 | P1, als `abt-in-der-kernapplikation.md` | Q01 belegt die Ausbaustufen 4 und 5 konkret. |
| `sicherheit/pki.md` als P2 | P1 | Die Zertifikatshierarchie und die Daten aus Q42 sind zu wichtig für den Backlog. |
| `medien/applikationsinstanz.md` | `applikationsinstanz-id.md` | Der Glossarbegriff lautet „Applikationsinstanz-ID“. |
| `medien/lebenszyklus-applikation.md` | `lebenszyklus-der-applikation.md` | Dateiname folgt dem Titel. |
| `datenformate/namespace.md` | `xml-namensraum.md` | deutscher Titel |
| `datenformate/namenskuerzung.md` | `kuerzungsregel-fuer-namen.md` | Titel nach BOM-Abschnitt 6.7.2 |
| `datenformate/tag-db-fahrgast.md` | `tag-0xdb-fahrgast.md` | Tag im Dateinamen sichtbar |

**Statusverteilung:** 95 `belegt`, 3 `zu prüfen` (Auftragstyp, Aktionsfreigabe entfiel, `txalisber`, Änderungsreferenz), 1 `abgeleitet` (`berSynchronNummer`).

**Noch nicht ausgewertete Quellen** (17 von 42). Sie sind beschafft und verzeichnet, aber in keinem Artikel zitiert:

- **Projektdokumente mit Potenzial:** [Q31](QUELLEN.md#q31) (Abbildung und Kontrolle in NRW, 77 S., Stand 2026), [Q32](QUELLEN.md#q32) (Westfalen-Tarif, 92 S.), [Q38](QUELLEN.md#q38) (bwtarif, 158 S.), [Q36](QUELLEN.md#q36) (eTarife NRW), [Q40](QUELLEN.md#q40) (Rahmenlastenheft DL-System), [Q09](QUELLEN.md#q09) (AVV-Tarif), [Q08](QUELLEN.md#q08) (EFM-Integration)
- **Hersteller- und Sekundärquellen:** [Q14](QUELLEN.md#q14), [Q15](QUELLEN.md#q15), [Q17](QUELLEN.md#q17), [Q21](QUELLEN.md#q21), [Q22](QUELLEN.md#q22), [Q23](QUELLEN.md#q23)
- **Einstiegsseiten ohne eigenen Inhalt:** [Q03](QUELLEN.md#q03), [Q27](QUELLEN.md#q27), [Q28](QUELLEN.md#q28)
- **Nicht auswertbar:** [Q41](QUELLEN.md#q41) (AES-256-verschlüsselt)

Für die P2-Artikel des Bauplans sind vor allem Q31, Q32 und Q38 die nächsten Schritte: Sie decken Tarifabbildung, Produktparameter und Kontrolle in drei weiteren Verbünden ab und erlauben damit erstmals den Vergleich, welche Festlegungen **verbundübergreifend gleich** sind — der einzige Weg, ohne die KA-Spezifikationen etwas über KA-weite Geltung zu sagen.

---

## 15. Erweiterung aus den Quellen Q43 bis Q49 (2026-10-20)

Sechs neue Dokumente und das öffentlich erreichbare etiCORE-Spezifikationsmodell haben **zwölf Artikel** möglich gemacht. Damit stehen **111 Artikel** — 10 Kategorieartikel und 101 Blattartikel.

| Artikel | Pfad | Quelle | Grund für diesen Platz |
|---|---|---|---|
| **Datenschutz** | `grundlagen/datenschutz.md` | [Q48](QUELLEN.md#q48) | Querschnittsthema über alle Rollen und Nachrichten; es gehört zu den Grundlagen, nicht in eine Fachkategorie. |
| **Pflichtelemente einer Transaktion** | `transaktionen/pflichtelemente-einer-transaktion.md` | [Q48](QUELLEN.md#q48) | Gegenstand sind die Inhalte einer Transaktion. Der Platz bei den Transaktionen ist eindeutig; der Datenschutzbezug läuft über `siehe_auch`. |
| **etiCORE** | `grundlagen/eticore.md` | [Q43](QUELLEN.md#q43) | Eine Version des Standards, also ein Grundlagenbegriff neben [Versionen](lexikon/grundlagen/versionen.md). |
| **Spezifikationsmodell** | `grundlagen/spezifikationsmodell.md` | [Q43](QUELLEN.md#q43), [Q49](QUELLEN.md#q49) | Form der Spezifikation, Geschwister von [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md). |
| **Rollennamen in etiCORE** | `rollen/rollennamen-in-eticore.md` | [Q43](QUELLEN.md#q43), [Q45](QUELLEN.md#q45) | Eine Übersetzungstabelle der Rollen. Sie gehört zu den Rollen, nicht zu etiCORE — sonst müsste jeder Rollenartikel dorthin verweisen. |
| **UIC-Barcode** | `datenformate/uic-barcode.md` | [Q46](QUELLEN.md#q46) | Ein zweites Datenformat neben dem VDV-Barcode, beide im selben Zweig. |
| **VDV-Barcode mobile+** | `sicherheit/vdv-barcode-mobile.md` | [Q46](QUELLEN.md#q46) | Gegenstand ist der Kopierschutz, also eine Sicherheitsfunktion — nicht das Format. Dateiname ohne `+`, weil der Slug Sonderzeichen entfernt. |
| **MOTICS** | `sicherheit/motics.md` | [Q46](QUELLEN.md#q46), [Q43](QUELLEN.md#q43) | Dienst und Container des Kopierschutzes. |
| **zSAM** | `sicherheit/zsam.md` | [Q45](QUELLEN.md#q45) | Sonderform des SAM; steht bei den Sicherheitsmodulen. |
| **Key-Identifier** | `sicherheit/key-identifier.md` | [Q45](QUELLEN.md#q45) | Eigener Artikel statt Abschnitt in [Schlüsselarten](lexikon/sicherheit/schluesselarten.md): Die Tabelle samt Erläuterung hätte dort das Wortlimit um 90 Wörter überschritten. |
| **ASM** | `sicherheit/asm.md` | [Q45](QUELLEN.md#q45), [Q43](QUELLEN.md#q43) | Applikations- und Sicherheitsmanagement-System samt ASM-Tool. Steht bei der Sicherheit, weil Gegenstand die Verwaltung von Schlüsseln, SAMs und Zertifikaten ist. |
| **Teilnahmevertrag** | `grundlagen/teilnahmevertrag.md` | [Q45](QUELLEN.md#q45), [Q46](QUELLEN.md#q46) | Die Vertragsarten und der Kundenstatus entscheiden, welche Organisations-IDs eine Organisation erhält. Das ist eine Grundlage, keine Sicherheitsfunktion. |

**Erweitert** wurden [versionen.md](lexikon/grundlagen/versionen.md) (Release 1.12.1), [ka-spezifikationen.md](lexikon/grundlagen/ka-spezifikationen.md) (drei Anlagen zur KA STB-Spec, Bezugsweg), [vdv-barcode.md](lexikon/datenformate/vdv-barcode.md) (Signatur, Sperrbarkeit, Identifikationsmerkmal) und [schluesselarten.md](lexikon/sicherheit/schluesselarten.md) (Verweis auf den Key-Identifier) sowie [sicherheitsebenen.md](lexikon/sicherheit/sicherheitsebenen.md) (Zweck der Organisations-IDs je Ebene, zwei IDs je Teilnehmer).

**Eine Korrektur:** [vdv-barcode.md](lexikon/datenformate/vdv-barcode.md) behauptete im Beispielteil, ein Barcode lasse sich nicht sperren. [Q46](QUELLEN.md#q46), Kap. 4.1, PDF-S. 9, sagt das Gegenteil: Ein gesperrtes Barcodeticket wird bei der Kontrolle erkannt und muss abgewiesen werden. Unveränderlich ist der **Inhalt des Barcodes**, nicht die Sperrbarkeit des Tickets.

**Neue offene Fragen:** O15 (Füllwert nicht benutzter Datenelemente), O16 (Zugang zu den Spezifikationen über das ASM-Tool), O17 (Datensatz im UIC 918-9\*), O18 (konkrete Schlüsselnummern in den Key-Identifier-Bereichen), O19 (Bedeutung des Kürzels „FU“ im Kundenstatus).

---

## 16. Erweiterung aus den Quellen Q50 und Q51 (2026-10-20)

Die Schnittstellendokumentation der etiCORE-Spezifikation ([Q50](QUELLEN.md#q50)) und die ASN.1-Typen ([Q51](QUELLEN.md#q51)) liegen als lokale Kopie vor. **Eine eigene Kategorie „etiCORE“ entsteht nicht**: etiCORE ist ein Grundlagenbegriff ([eticore.md](lexikon/grundlagen/eticore.md)), und die Rollenübersetzung steht bei den Rollen. Die neuen Artikel gehören in die Fachkategorien, in denen ihr Gegenstand liegt. Version und Geltung stehen im Text und in den Quellenangaben; ein eigenes Frontmatter-Feld dafür ist nicht nötig.

| Artikel | Pfad | Quelle | Grund für diesen Platz | Prio |
|---|---|---|---|---|
| **Nachrichten in KA 1.x und etiCORE** | `transaktionen/nachrichten-in-ka-1-x-und-eticore.md` | [Q50](QUELLEN.md#q50), Elemente mit `meta:old` | Gegenstand sind Nachrichtennamen; er steht bei den Transaktionen und Nachrichten, Geschwister von [TXAML](lexikon/transaktionen/txaml.md). Ergänzt die Rollenübersetzung. | **P1** |
| **Aktionsmanagement in etiCORE** | `aktionsmanagement/aktionsmanagement-in-eticore.md` | [Q50](QUELLEN.md#q50), `po-oa-management` und `ccp-oa-ordering`; [Q49](QUELLEN.md#q49), Glossar | Zeigt, wie Bestellen, Abrufen und Melden in etiCORE zugeschnitten sind (`orderGroup`, Differenzliste mit Prüfsumme). Gehört zum Aktionsmanagement. | **P1** |
| **Fehlercodes in etiCORE** | `transaktionen/fehlercodes-eticore.md` | [Q50](QUELLEN.md#q50), Fehlerelemente der Aktionsverwaltung | Rückmeldungen auf Nachrichten; Platz bei den Nachrichten. Offen, ob die vollständige Codeliste lesbar ist. | P2 |
| **Hotlist Service** | `kontrolle/hotlist-service.md` | [Q50](QUELLEN.md#q50), `hotlist`; [Q49](QUELLEN.md#q49), Glossar | Nachfolger der Rolle KOSE; die Sperraufträge haben Altbezeichner (`TXSAUF…`, `TXSFREI…`). Gegenstand ist die Sperrliste, also Kontrollmanagement. | P2 |
| **ESH** | `sicherheit/esh.md` | [Q50](QUELLEN.md#q50), `esh`; [Q49](QUELLEN.md#q49), Glossar („successor to the ASM“) | Nachfolger des [ASM](lexikon/sicherheit/asm.md); die Schnittstelle ist noch nicht gelesen. | P2 |
| **Statische Berechtigung in etiCORE** | `berechtigungen/statische-berechtigung-in-eticore.md` | [Q51](QUELLEN.md#q51), Modul `ste` und `user-medium` | Gegenstand ist die Berechtigung als signierter Datensatz; sie gehört zu den Berechtigungen, Geschwister von [Statische Berechtigung](lexikon/berechtigungen/statische-berechtigung.md). | **P1** |

**Erweitert** werden, ohne Umbau: [rollennamen-in-eticore.md](lexikon/rollen/rollennamen-in-eticore.md) (die Gleichsetzung von ALISE und PO-Aktionsmanagement ist über die Altbezeichner im Namensraum `http://vdv/ka/alise/2` gestützt), [spezifikationsmodell.md](lexikon/grundlagen/spezifikationsmodell.md) (Verweis auf Q50 und Q51), [txalisber.md](lexikon/transaktionen/txalisber.md) (O14), [aktionsfreigabe.md](lexikon/aktionsmanagement/aktionsfreigabe.md) (O20).

**Neue offene Frage:** O20 (`TXAFREIBER` wird in etiCORE zu `cancelOrder`).

**Stand 2026-10-20:** geschrieben sind *Nachrichten in KA 1.x und etiCORE*, *Aktionsmanagement in etiCORE*, *Hotlist Service* und *ESH*; damit stehen **117 Artikel**. Dazu kamen *Statische Berechtigung in etiCORE* und *Fehlercodes (etiCORE)* mit 38 Codes (Aktionsverwaltung, allgemein, PO). Nachgezogen wurden außerdem [berSynchronNummer](lexikon/berechtigungen/bersynchronnummer.md), [Rollencodes](lexikon/rollen/rollencodes.md), [Änderungsreferenz](lexikon/aktionsmanagement/aenderungsreferenz.md) und [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md).
