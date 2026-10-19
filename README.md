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

## Kategorien

1. **Grundlagen** — VDV-KA, eTicket Deutschland, Versionen, Ausbauvarianten, Verzeichnis der Spezifikationen
2. **Rollen und Organisationen** — KVP, DL, PV, AH, KOSE, ALISE, Rollencodes, Organisations-ID
3. **Medien und Applikationen** — Nutzermedium, Applikation, Applikationsinstanz, Lebenszyklus
4. **Berechtigungen und Produkte** — Berechtigung, EFS, Produkt, berStatus, berSynchronNummer, Gültigkeit
5. **Transaktionen und Nachrichten** — TX_BASE, TXABER, TXEBER, TXSNAWB, TXAML, Duplikaterkennung
6. **[Aktionsmanagement](lexikon/aktionsmanagement.md)** — Aktion, Aktionsliste, Auftragstyp, Ausgabe und Rücknahme über Aktionsliste
7. **Sperr- und Kontrollmanagement** — Sperrlisten, Sperrnachweise, Kontrollnachweise, Sichtkontrolle
8. **Sicherheit und Schlüssel** — MAC, Schlüsselreferenzen, SAM, CV-Zertifikate, Sicherheitsebenen
9. **Datenformate und Kodierung** — XSD, TLV, Nullwerte, VDV-Barcode, Basisobjektmodell
10. **Account Based Ticketing** — ABT und MBT, ID-Token, Ticket Cloud, Offline-Kontrolle, Deny List

> **Stand der Arbeit:** Die Kategorie **[Aktionsmanagement](lexikon/aktionsmanagement.md)** ist mit allen zwölf Kernartikeln fertig und zeigt, wie das Lexikon aussieht. Die übrigen neun Kategorien folgen; der vollständige Bauplan mit Quellen und Prioritäten steht in [STRUKTUR.md](STRUKTUR.md), der Arbeitsstand in [PLAN.md](PLAN.md).

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
