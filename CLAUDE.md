# Arbeitsregeln für das VDV-KA-Toolkit

Dauerhafte Regeln für alle Sessions in diesem Repository. Sie gehen Gewohnheiten vor. Konzept und Begründungen: [PLAN.md](PLAN.md) · Begriffsbaum: [STRUKTUR.md](STRUKTUR.md) · Quellen: [QUELLEN.md](QUELLEN.md)

## Was dieses Repository ist

Stufe 1 ist ein **Lexikon** zur VDV-Kernapplikation 1.x, zu eTicket Deutschland und zu Account Based Ticketing, als reines Markdown. Stufe 2 wird ein **Werkzeug**, das ALISE-Nachrichten visualisiert und offensichtliche Fehler kennzeichnet. Das Lexikon ist die Datenbasis des Werkzeugs — deshalb ist das Frontmatter maschinenlesbar zu halten.

---

## 1. Sprache

- Alles auf **Deutsch**: Artikeltexte, Überschriften, Commit-Nachrichten, Kommentare im Code.
- **Fachbegriffe bleiben im Original**, auch wenn sie englisch sind: `Account Based Ticketing`, `Deny List`, `Secure Application Module`, `Post-Validation`. Nicht eindeutschen.
- **Feldnamen, Nachrichtentypen und Codebezeichner werden exakt geschrieben**, mit Binnenmajuskeln: `berSynchronNummer`, `amAuftragsTyp`, `logTransaktionsTyp`, `TXABER`, `TXAML`, `IONTransaktion_ID`. In Fließtext als Code gesetzt.
- Die englische Entsprechung gehört ins Frontmatter (`englisch:`), nicht in den Text. [Q02](QUELLEN.md#q02) ist zweisprachig und belegt sie.
- Dateinamen sind ASCII und kleingeschrieben (Regel 4).

## 2. Quellenpflicht

- **Jede fachliche Aussage braucht eine Quelle.** Keine Ausnahme für „ist doch bekannt“.
- Zitiert wird mit **Q-Nummer und Fundstelle**, nie nur mit der Q-Nummer:
  gut: `[Q06](../../QUELLEN.md#q06), Kap. 2.1.5` — schlecht: `laut Q06`
- Bei PDFs ohne Kapitelnummern die **Seite** angeben. Seitenzahlen über `tools/pdftext.py` ermitteln, nicht schätzen.
- Steht eine Q-Nummer nicht in [QUELLEN.md](QUELLEN.md), ist sie ungültig. Neue Quellen **zuerst** dort eintragen, dann zitieren. `tools/check.py` prüft das.
- [Quellen_LBV.md](Quellen_LBV.md), [QUELLEN_ALISE.md](QUELLEN_ALISE.md) und [QUELLEN_VDV-KA.md](QUELLEN_VDV-KA.md) sind **Auswertungen, keine Quellen**. Nie zitieren — immer das zugrunde liegende Dokument.
- Exzerpte liegen in `exzerpte/<Qxx>.md` mit Seitenangabe. Wo ein Exzerpt existiert, daraus arbeiten statt das PDF neu zu lesen.

## 3. Statuskennzeichnung

Drei Stufen, im Frontmatter **und** im Text:

| Status | Bedeutung | Markierung im Text |
|---|---|---|
| `belegt` | Quelle und Fundstelle vorhanden | keine — die Quellenangabe trägt die Aussage |
| `abgeleitet` | Schlussfolgerung aus belegten Fakten | `(abgeleitet)` hinter der Aussage |
| `zu prüfen` | unsicher oder nur sekundär belegt | `(zu prüfen)` hinter der Aussage |

- `status:` im Frontmatter nennt den **schwächsten** Beleg des Artikels. Enthält ein Artikel eine Aussage mit `zu prüfen`, ist der Artikelstatus `zu prüfen`.
- Jede Aussage mit `zu prüfen` gehört zusätzlich in die Tabelle „Offene Fragen“ in [PLAN.md](PLAN.md), Abschnitt 5. Wenn dort schon eine Nummer passt, diese im Text nennen: `(zu prüfen, O3)`.
- **Niemals** Vermutungen als Fakten formulieren. Nicht „Auftragstyp 13 bedeutet Ausgabe“, sondern „Die Indizien sprechen für Ausgabe einer Berechtigung (abgeleitet, O2)“.

## 4. Verbundspezifische Aussagen

Fakten aus Projektdokumenten ([Q05](QUELLEN.md#q05)–[Q10](QUELLEN.md#q10), [Q31](QUELLEN.md#q31)–[Q36](QUELLEN.md#q36)) sind Festlegungen **eines Verbunds**, nicht des Standards.

- Immer kennzeichnen: „im eTicket RheinMain“, „im Westfalen-Tarif“, „in NRW“.
- Nie zu einer KA-weiten Aussage verallgemeinern. Das betrifft insbesondere die **berStatus-Codes** (5/7/8/19, RMV), die **Transaktionstypen 37/38/39** und die **Rollencodes** (KVP 1 … ALISE 31).
- Legen zwei Verbünde unabhängig dasselbe fest, das vermerken. Es ist ein starkes Indiz, aber kein Beleg.

## 5. Aufbau jedes Artikels

Feste Reihenfolge. Kein Abschnitt entfällt, keiner kommt dazu:

1. **Breadcrumb** als erste Zeile — *generiert*
2. **H1** mit dem Titel
3. **Fachliche Erklärung** — höchstens **250 Wörter**, präzise, in Fachsprache, jede Aussage mit Quelle
4. **Einfach erklärt – Beispiel aus Bärstadt** — höchstens **600 Wörter**, gern kürzer, für Laien verständlich
5. **Quellen** — Q-Nummern mit Fundstelle, als Link auf den Anker in [QUELLEN.md](QUELLEN.md)
6. **Unterartikel** — *generiert*, fehlt bei Blattartikeln
7. **Siehe auch** — optional, Querverweise außerhalb des eigenen Zweigs
8. **Navigation** — *generiert*

Vorlagen: [vorlagen/artikel.md](vorlagen/artikel.md) für Blattartikel, [vorlagen/kategorie.md](vorlagen/kategorie.md) für Kategorien.

**Wortlimits sind harte Grenzen.** `tools/check.py` bricht ab, wenn sie überschritten sind. Lieber einen Unterartikel anlegen als den Text dehnen.

## 6. Navigation und Dateinamen

- **Nur relative Links.** Keine Wiki-Links `[[…]]`, kein HTML, keine generierte Website. Das Lexikon muss in GitHub, VS Code und Obsidian funktionieren.
- **Genau ein Parent je Artikel.** Der Baum hat keine Mehrfacheltern. Begriffe, die in mehrere Zweige passen, bekommen einen Platz und werden sonst über `siehe_auch` verlinkt. Die Zuordnung der Grenzfälle steht in [STRUKTUR.md](STRUKTUR.md), Abschnitt 12 — dort nachsehen, nicht neu entscheiden.
- Kategorieartikel liegt **neben** seinem Ordner: `lexikon/aktionsmanagement.md` und `lexikon/aktionsmanagement/`.
- **Dateiname = Slug des Titels:** Kleinbuchstaben, ASCII, Bindestriche, `ä`→`ae`, `ö`→`oe`, `ü`→`ue`, `ß`→`ss`. Feldnamen ohne Sonderbehandlung: `berSynchronNummer` → `bersynchronnummer.md`.
- **Breadcrumb, Unterartikel-Liste, Navigationszeile, [REGISTER.md](REGISTER.md) und [ABKUERZUNGEN.md](ABKUERZUNGEN.md) werden generiert.** Niemals von Hand ändern — Änderungen gehen beim nächsten Lauf verloren. Gepflegt werden nur `parent`, `siehe_auch` und der Fließtext.
- Die generierten Blöcke sind durch HTML-Kommentare begrenzt (`<!-- GEN:… -->`). Sie sind die **einzige** erlaubte HTML-Verwendung, weil sie in allen Viewern unsichtbar bleiben.

## 7. Frontmatter

Vollständig und maschinenlesbar — das spätere Analysewerkzeug liest es aus:

```yaml
---
titel: Aktionsliste
abkuerzung: TXAML
englisch: action list
parent: lexikon/aktionsmanagement.md       # immer relativ zur Repo-Wurzel
siehe_auch: [lexikon/rollen/alise.md]
quellen: [Q02, Q06]
status: belegt          # belegt | abgeleitet | zu prüfen
offene_fragen: []       # z. B. [O1, O2]
stand: 2026-10-19
codes: []               # Codelisten, siehe unten
---
```

- `children` wird **nicht** gepflegt, sondern aus `parent` berechnet.
- Codelisten immer strukturiert, nie nur als Tabelle im Text:
  ```yaml
  codes:
    - wert: 37
      bedeutung: Ausgabe EFS über Aktionsliste
      quelle: Q06
      fundstelle: Kap. 2.1.5, Fußnote 1
      status: belegt
      verbundspezifisch: true
  ```
- `stand:` bei jeder inhaltlichen Änderung auf das aktuelle Datum setzen.

## 8. Die Beispielwelt

- Alle Beispiele spielen in **Bärstadt im Bärenland**. [welt/baerstadt.md](welt/baerstadt.md) ist die verbindliche Referenz.
- **Keine neuen Namen, IDs, Produkte oder Figuren erfinden.** Wenn ein Beispiel etwas braucht, das dort fehlt: zuerst die Welt-Bibel ergänzen, dann im Artikel verwenden.
- Fiktive Org-IDs liegen im Bereich **9000–9099**. Niemals reale Org-IDs oder andere Originalwerte aus [Q11](QUELLEN.md#q11) verwenden — auch nicht beispielhaft, auch nicht in Kommentaren.
- **Echte Unternehmen, Verbünde und Personen kommen in Beispielen nicht vor.** In der fachlichen Erklärung sind reale Beispiele erlaubt, wenn sie belegt sind.
- Das Beispiel darf **vereinfachen, aber der fachlichen Erklärung nicht widersprechen** und nichts behaupten, was dort nicht steht.

## 9. Urheberrecht und Datenschutz

**Dieses Repository ist öffentlich.** Jede eingecheckte Datei ist für jeden lesbar. Das ist beim Schreiben jedes Satzes mitzudenken.

- `QUELLEN/` ist per `.gitignore` ausgeschlossen und bleibt lokal.
- **Keine Volltexte und keine langen Passagen** aus den Quellen ins Repository. Nur kurze Exzerpte mit Fundstelle — als Belegnachweis, nicht als Ersatz für das Dokument.
- [Q06](QUELLEN.md#q06) trägt den Vermerk „Cubic Transportation Systems (Deutschland) GmbH, Vertraulich“. Entsprechend sparsam zitieren.
- Die LVB-Bewerberaufgabe ([Q11](QUELLEN.md#q11)) kommt **nicht** ins Repository. Sie enthält personenbezogene Daten im produktspezifischen Teil. Aus ihr werden nur **Feldnamen und Strukturen** übernommen, niemals Werte.
- Beim späteren Werkzeug nur Testdaten oder ausreichend anonymisierte Daten verwenden.

## 10. Werkzeuge

| Werkzeug | Zweck |
|---|---|
| `python3 tools/check.py` | prüft Wortlimits, Links, Baumkonsistenz, Q-Nummern, Dateinamen |
| `python3 tools/gen.py` | erzeugt Breadcrumbs, Unterartikel-Listen, Navigation, Register, Abkürzungsverzeichnis |
| `python3 tools/pdftext.py DATEI [von] [bis]` | Textextraktion mit Seitenmarkern, nur Standardbibliothek |

- **Nur Python-Standardbibliothek.** Keine externen Abhängigkeiten, auch nicht für YAML — das Frontmatter wird mit einem eigenen, bewusst einfachen Parser gelesen. Auf dem Zielrechner gibt es weder `pip`-Pakete noch Homebrew.
- Nach jeder inhaltlichen Änderung: `python3 tools/gen.py && python3 tools/check.py`. Erst wenn `check.py` fehlerfrei durchläuft, ist die Arbeit fertig.
- `tools/pdftext.py` braucht bei [Q07](QUELLEN.md#q07) die Option `--shift=29` (verschobene Zeichenkodierung). Bei [Q25](QUELLEN.md#q25) fehlen in manchen Schriften Umlaute — Zitate von dort gegen das PDF prüfen.

## 11. Arbeitsweise

- **Erst Beleg, dann Artikel.** Wenn die Quelle nicht vorliegt, den Artikel nicht schreiben, sondern den Bedarf in [PLAN.md](PLAN.md) notieren.
- **Nicht raten, um eine Lücke zu schließen.** Eine ehrliche Lücke mit `(zu prüfen)` ist wertvoller als ein glatter Text, der im Werkzeug zu falschen Interpretationen führt.
- Keine Artikel außerhalb von [STRUKTUR.md](STRUKTUR.md) anlegen. Neue Begriffe zuerst dort mit Pfad, Quelle und Priorität eintragen.
- Bestehende Artikel beim Erweitern **nicht umstrukturieren**. Die Abschnittsfolge aus Regel 5 ist fest.
