# VDV-KA-Toolkit

Lexikon und Werkzeuge zur **VDV-Kernapplikation 1.x**, zu **eTicket Deutschland** und zu **Account Based Ticketing**.

Das Repository hat zwei Stufen. Stufe 1 ist dieses **Lexikon**: ein Nachschlagewerk in reinem Markdown, in dem jeder Fachbegriff einen eigenen kleinen Artikel hat — mit einer präzisen fachlichen Erklärung und einem Beispiel, das auch ohne Vorkenntnisse verständlich ist. Stufe 2 wird ein **Werkzeug**, das ALISE-Nachrichten visualisiert und offensichtliche Fehler kennzeichnet. Das Lexikon ist dessen Datenbasis.

**Zwei Dinge, die dieses Lexikon anders macht als ein Glossar:**

1. **Jede Aussage nennt ihre Quelle** mit Kapitel oder Seite. Die eigentlichen KA-Spezifikationen sind nicht öffentlich, viele Fakten sind daher nur über Projektdokumente einzelner Verbünde belegt. Wo etwas nur erschlossen oder unsicher ist, steht das ausdrücklich dabei: `(abgeleitet)` oder `(zu prüfen)`.
2. **Alle Beispiele spielen in einer einzigen fiktiven Welt** — [Bärstadt in Bärenland](welt/baerstadt.md). Namen, Nummern und Zusammenhänge bleiben dadurch über alle Artikel hinweg gleich.

---

## Einstieg

| | |
|---|---|
| [Alphabetisches Register](REGISTER.md) | alle Artikel von A bis Z |
| [Abkürzungsverzeichnis](ABKUERZUNGEN.md) | TXAML, KVP, PV, SAM, ALISE … |
| [Bärstadt in Bärenland](welt/baerstadt.md) | die Beispielwelt mit dem durchgehenden Beispielfall |
| [Quellenverzeichnis](QUELLEN.md) | alle Quellen Q01–Q36 mit Fundstellen |
| [Benötigte Dokumentation](BESCHAFFUNG.md) | was an nicht öffentlichen KA-Spezifikationen fehlt, wofür, und ein fertiger Anfragetext |

## Kategorien

1. **[Grundlagen](lexikon/grundlagen.md)** — VDV-KA, eTicket Deutschland, EFM, Versionen, Ausbauvarianten, KA-Spezifikationen, Interoperabilität, Elementarprozess
2. **[Rollen](lexikon/rollen.md)** — KVP, DL, PV, AH, KOSE, ALISE, Rollencodes, Organisations-ID, Hintergrundsystem, Akzeptanzterminal
3. **[Medien](lexikon/medien.md)** — Nutzermedium, Applikation, Applikationsinstanz-ID, Lebenszyklus der Applikation, personengebunden
4. **[Berechtigungen](lexikon/berechtigungen.md)** — Berechtigung, EFS, Produkt, Produktnummer, berStatus, berSynchronNummer, Gültigkeit, produktspezifischer Teil, statische Berechtigung, Multiberechtigung
5. **[Transaktionen](lexikon/transaktionen.md)** — TX_BASE, `logTransaktionsTyp`, TXABER, TXRBER, TXSNAWB, TXEBER, TXAML, `txalisber`, TXA/TXB, Duplikaterkennung
6. **[Aktionsmanagement](lexikon/aktionsmanagement.md)** — Aktion, Aktionsliste, Auftragstyp, Ausgabe und Rücknahme über Aktionsliste
7. **[Kontrolle](lexikon/kontrolle.md)** — Sperrung, Sperrliste, Sperrlisteneintrag, Sperrgrund, Sperrnachweis, Kontrollnachweise, Sichtkontrolle, Kontrollgerät
8. **[Sicherheit](lexikon/sicherheit.md)** — MAC, Schlüsselreferenz, Schlüsselarten, Keymanagement, SAM, CV-Zertifikat, PKI, Sicherheitsebenen
9. **[Datenformate](lexikon/datenformate.md)** — Basisobjektmodell, TLV, Tag 0xDB, Kürzungsregel für Namen, Nullwerte, XSD und WSDL, XML-Namensraum, VDV-Barcode
10. **[Account Based Ticketing](lexikon/abt.md)** — MBT, Account, ID-Token, Ticket Cloud, Online- und Offline-Kontrolle, Hybridsystem, Deny List, ABT in der Kernapplikation

> **Stand der Arbeit:** Alle zehn Kategorien sind geschrieben, insgesamt **157 Artikel**: [Grundlagen](lexikon/grundlagen.md) (13), [Rollen](lexikon/rollen.md) (13), [Berechtigungen](lexikon/berechtigungen.md) (19), [Medien](lexikon/medien.md) (6), [Transaktionen](lexikon/transaktionen.md) (23), [Aktionsmanagement](lexikon/aktionsmanagement.md) (13), [Kontrolle](lexikon/kontrolle.md) (12), [Sicherheit](lexikon/sicherheit.md) (20), [Datenformate](lexikon/datenformate.md) (19) und [ABT](lexikon/abt.md) (9). Neu seit Oktober 2026 ist die Auswertung der öffentlichen **etiCORE-Spezifikation 3.0.0-rc.6**: ASN.1-Typen, Schnittstellen, alle 203 Fehler- und Warncodes und die Zuordnung der KA-1.x-Nachrichten zu ihren etiCORE-Nachfolgern. Der Bauplan steht in [STRUKTUR.md](STRUKTUR.md), der Arbeitsstand in [PLAN.md](PLAN.md), die offenen Fragen zur Abstimmung in [OFFENE-FRAGEN-ETICORE.md](OFFENE-FRAGEN-ETICORE.md).

---

## Für Mitarbeit

| Dokument | Inhalt |
|---|---|
| [CLAUDE.md](CLAUDE.md) | die verbindlichen Arbeitsregeln: Quellenpflicht, Statuskennzeichnung, Wortlimits, Navigation |
| [PLAN.md](PLAN.md) | Konzept, Entscheidungen mit Begründung, offene Fachfragen, Phasen |
| [STRUKTUR.md](STRUKTUR.md) | Begriffsbaum mit Pfaden, Quellen und Prioritäten |
| [vorlagen/artikel.md](vorlagen/artikel.md) | Vorlage für einen Blattartikel |
| [vorlagen/kategorie.md](vorlagen/kategorie.md) | Vorlage für einen Kategorieartikel |

### Werkzeuge

```sh
python3 tools/gen.py        # Navigation, Register und Abkürzungsverzeichnis erzeugen
python3 tools/check.py      # Wortlimits, Links, Baum, Q-Nummern prüfen
python3 tools/pdftext.py QUELLEN/Q06_….pdf 13 14    # Quelltext mit Seitenmarkern
```

Nur Python-Standardbibliothek, keine Installation nötig. Nach jeder Änderung `gen.py` und dann `check.py` laufen lassen.

**Navigation in jedem Artikel:** Breadcrumb oben, Unterartikel und Navigationszeile unten — alles aus dem Frontmatter erzeugt und nicht von Hand zu pflegen. Es werden ausschließlich relative Links verwendet, damit das Lexikon in GitHub, VS Code und Obsidian gleich funktioniert.

### Quellendateien

Der Ordner `QUELLEN/` mit den beschafften PDFs ist **nicht** Teil des Repositories (siehe `.gitignore`). Mehrere Dokumente sind als „Vertraulich“ gekennzeichnet. Im Repository stehen nur kurze Exzerpte mit Fundstelle. Was fehlt und wie es zu beschaffen ist, steht in [QUELLEN.md](QUELLEN.md), Abschnitt 5.
