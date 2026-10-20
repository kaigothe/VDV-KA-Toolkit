# Plan: VDV-KA-Lexikon

**Stand:** 2026-10-19 · **Status:** Planung, wartet auf Freigabe

Dieses Dokument hält das Konzept des Lexikons, die getroffenen Entscheidungen samt Begründung, die offenen Fragen und die Umsetzungsphasen fest. Die dauerhaften Arbeitsregeln stehen in [CLAUDE.md](CLAUDE.md), der Begriffsbaum in [STRUKTUR.md](STRUKTUR.md).

---

## 1. Ziel und Zweck

Ein Lexikon zur **VDV-Kernapplikation 1.x**, zu **eTicket Deutschland** und zu **Account Based Ticketing** als reines Markdown-Repository. Jeder Fachbegriff bekommt einen eigenen kleinen Artikel mit zwei Ebenen: einer präzisen fachlichen Erklärung und einem Beispiel aus der fiktiven Welt Bärstadt.

Das Lexikon ist die **erste Stufe** des VDV-KA-Toolkits. Die zweite Stufe ist ein Werkzeug, das ALISE-Nachrichten visualisiert und offensichtliche Fehler kennzeichnet. Diese Reihenfolge ist richtig: Das Werkzeug braucht genau das, was das Lexikon erarbeitet — Feldbedeutungen, Codelisten und die Unterscheidung zwischen belegtem Wissen und Vermutung. Das Lexikon ist deshalb bewusst so angelegt, dass es später **maschinenlesbar** ausgewertet werden kann (siehe Entscheidung E8).

---

## 2. Ausgangslage nach der Quellenbeschaffung

Alle erreichbaren Quellen liegen jetzt in [QUELLEN/](QUELLEN/) und sind in [QUELLEN.md](QUELLEN.md) verzeichnet: **19 PDFs und 19 HTML-Seiten**, zusammen rund 27 MB.

**Was dabei gewonnen wurde:**

- **Q06** (RMV PH 06-02, 46 Seiten) lag lokal vor und ist identifiziert. Die ergiebigste Quelle für Nachrichten, Rollencodes und Abläufe.
- **Q05, Q07, Q08, Q25** waren auf `mtv-unternehmen.de` gelöscht (HTTP 404) und wurden aus dem Internet Archive geholt. Damit ist auch **Q05** verfügbar — die einzige Quelle für die berStatus-Codes, die bisher überall nur zitiert wurden.
- **Q25** (eTicket-Regelwerk, 273 Seiten) ist der wichtigste Neuzugang. Es enthält das **vollständige Verzeichnis der KA-Spezifikationen mit Inventarnummern**, die **Ausbauvarianten** und die **Elementarprozesslisten je Rolle** — alles öffentlich belegbar.
- **Q30–Q36** wurden über die Downloadseite des KCD NRW neu gefunden, darunter das **Weißbuch ABT** des VDV eTS und mit **Q31** ein Dokument mit Stand April 2026.
- **Q02** (Glossar, 101 Seiten) ist als Begriffsgerüst ausgewertet: **138 zweisprachige Definitionen** mit Seitenzahl, jeweils mit deutscher und englischer Abkürzung. Das deckt die Felder `titel`, `englisch` und `abkuerzung` im Frontmatter direkt aus einer Primärquelle.

**Was weiterhin fehlt:** die KA-Spezifikationen selbst (BOM, SST, AktM, XSD) und damit die vollständigen Codelisten. Sie sind nur über das ASM-Tool des VDV eTS zu bekommen ([Q26](QUELLEN.md#q26)). Das ist die größte inhaltliche Schranke des Projekts und der Grund für die Statuskennzeichnung (Entscheidung E5).

**Werkzeug:** Auf dem Rechner war weder `pdftotext` noch eine Python-PDF-Bibliothek verfügbar. Es gibt daher [tools/pdftext.py](tools/pdftext.py), einen Extraktor allein mit der Standardbibliothek. Er setzt Zeilen über die Textposition zusammen, wertet Schriftgröße und Kerning aus und gibt den Text **seitenweise mit Seitenmarkern** aus. Letzteres ist der eigentliche Zweck: Ohne verlässliche Seitenzahlen sind die geforderten Fundstellen nicht zu belegen.

---

## 2a. Korrekturen gegenüber den Rechercheakten

Beim Prüfen der Fundstellen an den Dokumenten selbst haben sich drei Punkte ergeben, die von den bisherigen Notizen in [Quellen_LBV.md](Quellen_LBV.md) und [QUELLEN_ALISE.md](QUELLEN_ALISE.md) abweichen. Sie sind wichtig, weil sie in Artikel und später ins Analysewerkzeug eingehen.

**K1 — Der Rollencode 31 für ALISE gilt nicht pauschal.**
Bisherige Notiz: „ALISE ist eine eigene KA-Rolle mit dem Rollen-Code 31“. Tatsächlich steht in [Q06](QUELLEN.md#q06), Fußnote 7 (PDF-S. 40): In der Schnittstellenversion KA 1.1.07 wurde 31 *alternativ* akzeptiert. Ab KA 1.3.0 ist 31 „für einen aus dem PVS ausgelagerten eigenständigen zentralen ALISE-Server reserviert“; ist ALISE in das PV-System integriert, ist die **Rolle 3** zu verwenden — und in der TMS-Schnittstellenversion KA 1.3.0 ist für Transaktionen aus Aktionsausführungen **zwingend der Rollencode 3** zu verwenden. Die Versionshistorie des Dokuments führt das als „Wegfall des Rollen-Code 31 ALISE in KA 1.3.0“. Für die Interpretation einer Nachricht heißt das: Aus dem Rollencode allein lässt sich nicht auf ALISE schließen, und 31 ist ein Hinweis auf eine ältere Schnittstellenversion.

**K2 — Die Aktionsliste kennt vier Aktionen, nicht drei.**
Bisher wurden drei genannt (Ausgabe EFS, Entsperren, Rücknahme). [Q02](QUELLEN.md#q02), S. 19, nennt als vierte: **„Nur für (((etiCORE: Sperren einer Berechtigung auf Grundlage der ID des Aktionsauftrags“**. Die Rücknahme gilt dort außerdem für den EFS *oder* eine eBezahlberechtigung.

**K3 — KA 1.X und etiCORE unterscheiden sich bei der Aktionsliste.**
[Q02](QUELLEN.md#q02), S. 19: In etiCORE erhält jeder anfordernde ausführende KVP **dieselbe** Aktionsliste. In **KA 1.X** kann der ausführende KVP die Liste über die Konfiguration von Terminalgruppen und Produkten für sich aufbereiten, sodass eine **spezifische Aktionsliste je ausführendem KVP** entsteht. Das ist ein belegter Versionsunterschied und erklärt, warum die Felder `amTerminalGruppe_ID` und `amTerminal_ID` überhaupt existieren.

Zusätzlich bestätigt [Q02](QUELLEN.md#q02), S. 20 f., ein **Statusmodell der Aktion** („bestellt“ → „aktiv“ → „ausgeführt“), das in den Notizen fehlte und den Kern des Kategorieartikels bildet.

---

## 3. Entscheidungen

### E1 — Ein Baum, Kategorieartikel neben dem Ordner

Die Forderung „von jedem Artikel zu Home, Parent und allen Children“ erzwingt **genau einen Parent je Artikel**. Der Kategorieartikel liegt **neben** seinem Ordner, nicht darin:

```
lexikon/aktionsmanagement.md          ← Kategorieartikel
lexikon/aktionsmanagement/
    aktionsliste.md                   ← Unterartikel
    auftragstyp.md
```

**Begründung:** Der Breadcrumb eines Unterartikels wird damit genau so kurz wie gefordert — `[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktionsliste`. Die Alternative `index.md` im Ordner wurde verworfen: Zehn gleichnamige Dateien machen Editor-Tabs und die Obsidian-Schnellsuche unbrauchbar. Das Muster lässt sich beliebig tief fortsetzen.

### E2 — Dateinamen: streng aus dem Titel abgeleitet

Kleinbuchstaben, ASCII, Bindestriche, Umlaute ausgeschrieben (`ä` → `ae`), `ß` → `ss`.

Für Feldnamen gilt dieselbe Regel, ohne Sonderbehandlung von Binnenmajuskeln: `berSynchronNummer` → `bersynchronnummer.md`. Das ist weniger schön als `berSynchronNummer.md`, aber gemischte Groß- und Kleinschreibung in Dateinamen ist zwischen macOS (gleichgültig) und Linux (unterscheidend) eine verlässliche Fehlerquelle; der korrekt geschriebene Begriff steht ohnehin in `titel` und in der H1.

Der Dateiname ist damit **berechenbar**: `dateiname == slug(titel)` — oder `slug(abkuerzung)`, wo eine Abkürzung im Frontmatter steht. Diese zweite Form wurde nachträglich zugelassen, als die Kategorie Rollen entstand: Sie hätte sonst `rollen/kundenvertragspartner.md` erzwungen, obwohl `rollen/kvp.md` der gebräuchliche und besser verlinkbare Pfad ist und `KVP` als „Deutsche Abkürzung“ direkt aus dem Glossar stammt. Titel, H1 und Register zeigen weiterhin den vollen Begriff. [tools/check.py](tools/check.py) prüft beide Formen und lässt nichts dazwischen zu.

### E3 — Navigation wird generiert

Breadcrumb, Unterartikel-Liste, Navigationszeile, [REGISTER.md](REGISTER.md) und [ABKUERZUNGEN.md](ABKUERZUNGEN.md) erzeugt [tools/gen.py](tools/gen.py) aus dem Frontmatter. Von Hand gepflegt wird nur `parent`, `siehe_auch` und der Fließtext.

**Begründung:** Bei 60 Artikeln gibt es rund 180 Navigationslinks. Jede Umbenennung oder Verschiebung müsste sonst an drei Stellen je Artikel nachgezogen werden — das hält kein Mensch fehlerfrei durch. Außerdem ist `children` dann keine zweite Wahrheit: Es wird **aus** `parent` berechnet, womit sich Eltern- und Kindangabe nicht mehr widersprechen können.

**Abweichung von der Vorgabe „kein HTML“:** Die generierten Blöcke werden durch HTML-Kommentare begrenzt (`<!-- GEN:breadcrumb -->` … `<!-- /GEN:breadcrumb -->`). Sie sind in GitHub, VS Code und Obsidian unsichtbar und ändern die Darstellung nicht; die Anforderung „funktioniert in jedem Viewer“ bleibt also erfüllt. Die Alternative — Generieren anhand von Textpositionen — wäre brittle und würde bei jeder Textänderung Inhalt zerstören. Falls das unerwünscht ist, bitte sagen; dann werden die Blöcke an sichtbaren Überschriften verankert.

### E4 — Anker im Quellenverzeichnis: Überschrift ist nur die Q-Nummer

In [QUELLEN.md](QUELLEN.md) lautet jede Überschrift ausschließlich `## Q06`; der Titel steht als Fettzeile darunter.

**Begründung:** GitHub, VS Code und Obsidian erzeugen Anker aus dem **Überschriftentext**. Explizite Anker (`{#q06}`) funktionieren auf GitHub nicht, HTML-Anker sind ausgeschlossen. Nur eine Überschrift, die allein aus der Q-Nummer besteht, ergibt in allen drei Umgebungen denselben stabilen Anker `#q06`. Ein Titel in der Überschrift würde ihn bei jeder Titelkorrektur zerstören.

### E5 — Statuskennzeichnung auf Satzebene, nicht nur im Frontmatter

`status:` im Frontmatter nennt den **schwächsten** Beleg des Artikels. Zusätzlich wird im Text jede Aussage gekennzeichnet, die nicht `belegt` ist:

- **belegt** — mit Quelle und Seite oder Kapitel; Standardfall, wird im Text nicht markiert, sondern durch die Quellenangabe getragen.
- **abgeleitet** — Schlussfolgerung aus belegten Fakten. Markierung: `(abgeleitet)`.
- **zu prüfen** — unsicher oder nur sekundär belegt. Markierung: `(zu prüfen)` und Eintrag in Abschnitt 5 dieses Dokuments.

**Begründung:** Ein Artikel enthält typischerweise belegte *und* abgeleitete Sätze. Ein einziger Status je Artikel würde entweder zu viel versprechen oder belegtes Wissen entwerten. Diese Trennung ist zugleich die Vorarbeit für das Analysewerkzeug, das pro Feld „bestätigt / abgeleitet / unbekannt“ anzeigen soll.

### E6 — Verbundspezifisches wird immer gekennzeichnet

Aussagen aus Q05–Q10 und Q31–Q36 stammen aus Verbunddokumenten (RMV, AVV, NRW). Sie werden als verbundspezifisch gekennzeichnet, auch wenn sie plausibel allgemein gelten. Konkret heißt das für die meistzitierten Fakten:

- Die Transaktionstypen **37/38/39** sind über [Q06](QUELLEN.md#q06) belegt — aber als Festlegung im eTicket RheinMain. Ob sie KA-weit gelten, ist `zu prüfen`.
- Die **berStatus-Codes** 5/7/8/19 stammen aus dem RMV-EFS ([Q05](QUELLEN.md#q05)) und sind ausdrücklich RMV-Codes.
- Die **Rollencodes** KVP = 1 … ALISE = 31 stehen in [Q06](QUELLEN.md#q06), Kap. 4.10.

Wo zwei Verbünde unabhängig dasselbe festlegen (z. B. RMV und Westfalen-Tarif), wird das vermerkt — das ist ein starkes Indiz für eine KA-weite Festlegung, aber kein Beleg.

### E7 — Granularität: eigener Artikel, wenn es eigene Belege gibt

Ein Begriff bekommt einen eigenen Artikel, wenn mindestens eines zutrifft:

1. Er hat einen **eigenen Glossareintrag** in [Q02](QUELLEN.md#q02) — das sind 138 Begriffe und damit die verlässlichste Granularitätsgrenze, weil sie vom Standardgeber selbst gezogen wurde.
2. Er hat eine **eigene Codeliste oder einen eigenen Wertebereich** (`berStatus`, `logTransaktionsTyp`, `amAuftragsTyp`).
3. Er wird im Analysewerkzeug **einzeln angezeigt** — jedes Feld der Beispieltransaktion.

Gebündelt werden dagegen Felder ohne eigene Semantik: Die drei Schlüsselreferenzen `amMKPV-NM-MAC_ID`, `amMKKVP-NM-MAC_ID` und `amMKERF-NM-MAC_ID` erklärt **ein** Artikel „Schlüsselreferenz“, weil sie sich nur im Inhaber unterscheiden. Ebenso bilden `berGueltigkeitsbeginn` und `berGueltigkeitsende` einen Artikel „Gültigkeit“.

`berSynchronNummer` bekommt dagegen einen eigenen Artikel, obwohl das Glossar den Begriff **nicht** enthält: Das Feld trägt eine eigene Logik (Versionszähler, Erkennung veralteter Stände) und ist in der Praxis eine häufige Verwechslungsquelle mit `berStatus`.

### E8 — Frontmatter ist die Datenquelle, nicht Dekoration

Das YAML-Frontmatter wird vollständig und maschinenlesbar geführt, inklusive `codes:` für Codelisten:

```yaml
codes:
  - wert: 37
    bedeutung: Ausgabe EFS über Aktionsliste
    quelle: Q06
    fundstelle: Kap. 2.1.5, Fußnote 1
    status: belegt
```

**Begründung:** Daraus erzeugt das spätere Analysewerkzeug seine Codelisten-Auflösung samt Belegstatus, ohne dass die Fakten doppelt gepflegt werden. Das Lexikon wird so zur Datenbasis des Werkzeugs und nicht zu einem zweiten, konkurrierenden Wissensstand.

### E9 — Die Beispielwelt ist verbindlich und vollständig fiktiv

Alle Beispiele spielen in **Bärstadt im Bärenland**, festgelegt in [welt/baerstadt.md](welt/baerstadt.md). Fiktive Org-IDs liegen im Bereich **9000–9099**, der sich nicht mit den realen IDs aus [Q11](QUELLEN.md#q11) überschneidet und erkennbar künstlich ist.

Echte Unternehmen, Verbünde und Personen kommen in Beispielen nicht vor. In der **fachlichen** Erklärung sind reale Beispiele erlaubt, wenn sie belegt sind (etwa „im eTicket RheinMain“).

### E11 — Mermaid-Diagramme, sparsam und nur wo sie etwas zeigen

Diagramme werden als ```` ```mermaid ````-Codeblock eingebettet. GitHub und Obsidian rendern das nativ; die Vorschau von VS Code braucht je nach Version eine Erweiterung.

**Begründung und Abwägung:** Ein Mermaid-Block ist ein gewöhnlicher Codeblock. Wo er nicht gerendert wird, erscheint er als Quelltext — unschön, aber lesbar, und er zerstört nichts. Das ist ein echter, aber begrenzter Verstoß gegen „funktioniert in jedem Viewer“ (E3). Der Gegenwert: Schichten, Zeitachsen und Varianten­bäume sind als Text mühsam und als Bild sofort erfassbar.

**Regeln dazu:**

- Nur wo ein Diagramm **mehr zeigt als der Satz daneben**. Kein Diagramm als Dekoration.
- Jedes Diagramm bleibt **ohne Bild verständlich**: Was es zeigt, steht auch im Text.
- **Keine Klammern in Knotenbeschriftungen** — `(((etiCORE` bricht die Mermaid-Syntax. In Diagrammen heißt es `etiCORE`.
- Codeblöcke zählen **nicht** zu den Wortlimits, weil `zaehle_woerter` sie entfernt. Das ist Absicht für Code und Diagramme, darf aber nicht dazu dienen, Fließtext in Blöcke auszulagern.
- `check.py` prüft, ob jeder Mermaid-Block mit einem bekannten Diagrammtyp beginnt.

### E10 — Quellendateien bleiben lokal

`QUELLEN/` enthält Dokumente mit dem Vermerk „Vertraulich“ ([Q06](QUELLEN.md#q06): „Cubic Transportation Systems (Deutschland) GmbH, Vertraulich“). Der Ordner wird per `.gitignore` ausgeschlossen. Im Repository stehen nur Exzerpte mit Fundstelle. Die LVB-Bewerberaufgabe ([Q11](QUELLEN.md#q11)) kommt gar nicht ins Repository, weil sie personenbezogene Daten im produktspezifischen Teil enthält.

**Das Repository wird öffentlich** (Entscheidung vom 19.10.2026). Damit ist diese Regel keine Vorsichtsmaßnahme mehr, sondern zwingend: Jede Datei im Repository ist für jeden lesbar. Vor dem ersten Push ist zu klären, was mit den drei Rechercheakten im Wurzelverzeichnis geschieht — siehe Abschnitt 8.

---

## 4. Umsetzungsphasen

| Phase | Inhalt | Ergebnis |
|---|---|---|
| **0 — Planung** | dieses Dokument, [STRUKTUR.md](STRUKTUR.md), [CLAUDE.md](CLAUDE.md), Vorlagen, Welt-Bibel, Werkzeuge, Quellenbeschaffung | **fertig** |
| **1 — Gerüst** | Ordner, alle P1-Artikel als Rumpf mit Frontmatter | **angefangen:** Ordner, Startseite, Werkzeugkette und die zwei Musterartikel stehen; `gen.py` und `check.py` laufen fehlerfrei. Die übrigen Rümpfe folgen nach Freigabe des Tons. |
| **2 — Exzerpte** | `exzerpte/Q06.md`, `Q02.md`, `Q05.md`, `Q25.md` mit Begriffen, Codes und Seitenangaben | Belegbasis; danach muss kein Artikel mehr raten |
| **3 — Kernbegriffe** | P1-Artikel der Kategorien Grundlagen, Rollen, Aktionsmanagement, Transaktionen | **fertig:** Grundlagen (8), Rollen (10), Aktionsmanagement (12), Transaktionen (12) — 42 Blattartikel plus 4 Kategorieartikel. |
| **4 — Vertiefung** | restliche P1 | **fertig:** Berechtigungen (10), Medien (5), Datenformate (8), Kontrolle (8), ABT (8), Sicherheit (8). Damit sind alle zehn Kategorien geschrieben. |
| **5 — Review** | Wortlimits, Querverweise, offene Fragen, Widerspruchsfreiheit | **durchgeführt am 19.10.2026**, Ergebnis in [STRUKTUR.md](STRUKTUR.md), Abschnitt 14. Vier Mängel behoben: unsichtbare Querverweise, fehlende Codelistennamen, sechs unverlinkte Artikel, O11. Vier neue Prüfungen in `check.py`. |
| **6 — Übergabe ans Werkzeug** | `codes:` aus dem Frontmatter nach JSON exportieren | Datenbasis für den ALISE-Explorer |

**Reihenfolge innerhalb Phase 2 bis 4:** Zuerst Q02 (Begriffe), dann Q06 (Nachrichten und Codes), dann Q05 (berStatus, EFS-Aufbau), dann Q25 (Spezifikationen, Ausbauvarianten, Elementarprozesse), dann Q01 und Q30 (ABT).

---

## 5. Offene Fragen

Fachliche Punkte, die nicht aus den vorhandenen Quellen zu klären sind. Jeder Artikel, der einen dieser Punkte berührt, trägt dort `(zu prüfen)`.

Die meisten dieser Fragen lassen sich nur mit den nicht öffentlichen KA-Spezifikationen klären. Welche Dokumente das sind, wofür sie gebraucht werden und wo sie im Lexikon zitiert werden, steht in **[BESCHAFFUNG.md](BESCHAFFUNG.md)** — dort auch ein fertiger Anfragetext für den VDV eTicket Service. Der Verwendungsnachweis in Abschnitt 9a dieser Datei wird von `tools/gen.py` aus den Artikeln erzeugt.

| Nr. | Frage | Betrifft | Klärung über |
|---|---|---|---|
| **O1** | Gelten die Transaktionstypen 37/38/39 KA-weit oder nur im eTicket RheinMain? | `transaktionen/logtransaktionstyp.md` und die drei Aktionstyp-Artikel | KA SST-SPEC, KA AktM-SPEC |
| **O2** | Was bedeutet `amAuftragsTyp` = 13? Die Indizienkette (TX 37, Änderungsreferenz 0, SynchronNummer 1) spricht für „Ausgabe einer Berechtigung“, belegt ist das nicht. *Teilweise geklärt:* In etiCORE entfällt `amAuftragsTyp` in den Listeneinträgen für Ausgabe, Entsperrung und Rücknahme mit der Begründung „clear from context“ ([Q50](QUELLEN.md#q50), `po-oa-management_xsd`): Der Typ des Eintrags trägt die Information. Das Feld unterscheidet also die Auftragsarten (abgeleitet). **Offen bleibt der Zahlenwert** (13). | `aktionsmanagement/auftragstyp.md` | KA AktM-SPEC |
| **O4** | *Teilweise geklärt:* Die letzte Pfadstelle eines KA-Namensraums ist laut [Q25](QUELLEN.md#q25), Kap. 4.3.3, eine **Version**, und Releases innerhalb einer Version teilen den Namensraum (Kap. 4.3.1.4). Die `2` in `http://vdv/ka/alise/2` ist damit die Namensraum-Version. **Offen bleibt**, welches Release bzw. welche Schemafassung konkret zugrunde liegt. | `transaktionen/txalisber.md`, `datenformate/namespace.md`, Werkzeug | ALISE-XSD |
| **O3** | *Werte geklärt (Abschnitt 5a), Reichweite offen:* Gelten die Werte der Codeliste `WertobjektStatus_CODE` KA-weit? Dafür spricht, dass [Q05](QUELLEN.md#q05) sie als Auswahl aus einer Standardcodeliste führt — belegt ist es nicht. *Neu:* In etiCORE nennt `EntitlementStatusEnum` dieselben Zahlen 5 (terminated), 7 (ok) und 19 (blocked) und verweist auf EN 1545-1:2015 ([Q51](QUELLEN.md#q51), Modul `user-medium`). Die 8 („neu“) fehlt dort. Die Zahlen stammen danach aus einer Normliste (abgeleitet); ob die KA 1.x dieselbe Liste führt, bleibt offen. | `berechtigungen/berstatus.md`, `aktionsmanagement/ruecknahme-efs-ueber-aktionsliste.md` | KA BOM-SPEC (Inv. 1) |
| **O5** | Erhöht ein reiner Statuswechsel die `berSynchronNummer`? *Teilweise geklärt für etiCORE:* Die Nachfolgerin heißt `entitlementTransitionCounter`; sie ist eine „increasing sequence number which indicates if an entitlement's state has been changed. Each state transition causes an increasing of the counter“ ([Q51](QUELLEN.md#q51), Modul `user-medium`; Zuordnung über [Q50](QUELLEN.md#q50), `po-oa-management_xsd`). Danach erhöht jeder Zustandswechsel den Zähler (abgeleitet für die KA 1.x). | `berechtigungen/bersynchronnummer.md` | KA BOM-SPEC, KA AktM-SPEC |
| **O6** | *Teilweise geklärt:* Tag 0x85 ist belegt als „Statischer produktspezifischer Teil“ ([Q05](QUELLEN.md#q05), Kap. 2.1), die TLV-Lesart war also richtig; die Länge ist produktabhängig (0x44 im RMV-EFS). **Offen bleibt** die Abweichung zwischen angegebener Länge 0x57 = 87 Byte und 90 folgenden Byte. | `berechtigungen/produktspezifischer-teil.md`, `datenformate/tlv.md` | Anlage TLV EFS, vollständiger Originaldatensatz |
| **O9** | Verhältnis der Begriffe „Aktion“, „Aktionstyp“ und „Auftragstyp“: Das Glossar nennt Aktionstypen, die Nachricht ein Feld `amAuftragsTyp`. Synonym oder zwei Ebenen? | `aktionsmanagement/*` | KA AktM-SPEC |
| **O13** | Welchen Wert trägt `amAenderungsreferenz_ID` bei einer **tatsächlichen** Änderung, und nimmt es dann Berechtigungsnummer samt Organisation des Vorgängers auf? Es liegt nur ein Beispiel mit dem Wert 0 vor. *Teilweise geklärt, gegen die bisherige Deutung:* In etiCORE heißt das Feld `groupId` (Organisations-ID des bestellenden CCP und Gruppennummer): „Logically groups action list entries to be executed in a single transaction“, optional ([Q50](QUELLEN.md#q50), `po-oa-management_xsd`, Typ `ActionListEntryBaseInformation`). Die Änderungsreferenz wäre danach eine **Gruppe**, nicht der Verweis auf eine Vorgänger-Berechtigung (abgeleitet). Der Wert 0/0 hieße „keine Gruppe“. Der Verweis auf eine ersetzte Berechtigung ist in etiCORE ein eigenes, neues Feld (`replacedEntitlementId`, seit 3.0.0, ohne Altnamen); das stützt die Deutung als Gruppe. | `aktionsmanagement/aenderungsreferenz.md` | KA AktM-SPEC, weitere Beispielnachrichten |
| **O14** | Wie verhält sich `txalisber` zu `TXAML`? Ein Element innerhalb der `TXAML`, eine eigene Nachricht der ALISE-Schnittstelle oder eine verbund- bzw. herstellerspezifische Variante? [Q06](QUELLEN.md#q06) kennt `txalisber` nicht. *Teilweise geklärt:* In den etiCORE-Schnittstellen tragen die Typen der Listeneinträge `EntitlementIssuanceActionListEntry`, `…UnblockingActionListEntry` und `…TerminationActionListEntry` die Altbezeichner `TXALISBER_Type`, `TXELISBER_Type` und `TXRLISBER_Type` im Namensraum `http://vdv/ka/alise/2` ([Q50](QUELLEN.md#q50), [exzerpte/Q50.md](exzerpte/Q50.md)). Das spricht dafür, dass `txalisber` ein Eintrag in der `TXAML` ist (abgeleitet). **Offen bleibt**, ob das in der KA 1.x ebenso gilt. | `transaktionen/txalisber.md` | ALISE-XSD der KA 1.x |
| **O15** | Welcher Füllwert gilt für nicht benutzte Datenelemente einer Transaktion? [Q48](QUELLEN.md#q48), S. 7, nennt `0x00`; die Nullwert-Konvention der Datenformate sieht für andere Typen andere Füllwerte vor. Gilt `0x00` nur für die dort genannten Felder? | `transaktionen/pflichtelemente-einer-transaktion.md`, `datenformate/nullwerte.md` | KA NM-SPEC, KA BOM-SPEC |
| **O16** | Setzt der Download der KA-Spezifikationen im ASM-Tool einen Teilnahmevertrag voraus? [Q46](QUELLEN.md#q46), Kap. 6.1, nennt die Registrierung kostenlos und das ASM-Tool als Downloadort, ohne das Verhältnis zum Vertrag zu klären. | `grundlagen/ka-spezifikationen.md`, [BESCHAFFUNG.md](BESCHAFFUNG.md) | VDV eTicket Service |
| **O17** | Welcher Datensatz tritt im UIC 918-9\* an die Stelle des Datensatzes 0080BL? [Q46](QUELLEN.md#q46), Kap. 5, nennt den Wechsel, der Name ist in der Textextraktion verloren und am PDF zu prüfen. | `datenformate/uic-barcode.md` | [Q46](QUELLEN.md#q46) im Original, UIC 918-9 |
| **O18** | Welche konkreten Schlüsselnummern vergibt eine Organisation innerhalb der Key-Identifier-Bereiche 30, 40, 50, 60, 70 und 91? [Q45](QUELLEN.md#q45), S. 19, nennt nur die Bereiche und ihren Einsatzzweck. | `sicherheit/key-identifier.md` | KA SEC-SPEC, KA KM-Dokumentation |
| **O19** | Was bedeutet das Kürzel „FU“ im Kundenstatus „Teilnehmer Level-3“? [Q45](QUELLEN.md#q45), S. 10 und S. 22, nennt einen „FU-eTicket-Vertrag“ als Gegenstück zum eTicket-Ready-Vertrag; die Auflösung ist in der Textextraktion nicht enthalten. | `grundlagen/teilnahmevertrag.md` | [Q45](QUELLEN.md#q45) im Original, VDV eTicket Service |
| **O20** | *Richtung geklärt, Definition fehlt:* Was bewirkt der Aktionsfreigabeauftrag `TXAFREIBER`? Fünf unabhängige Belege sprechen für die **Rücknahme eines noch nicht ausgeführten Auftrags**: (1) das Benennungsmuster der KA — dem Sperrauftrag `TXSAUFB` steht der Sperrfreigabeauftrag `TXSFREIB` gegenüber ([Q39](QUELLEN.md#q39), Kap. 3.2.1 f., PDF-S. 50 f.); (2) ein NRW-Rahmenlastenheft paart „Sperraufhebungsanforderungen“ mit „die zugehörigen … Sperrfreigabemitteilungen“ ([Q40](QUELLEN.md#q40), PDF-S. 20, PDF-S. 16); (3) in etiCORE trägt `cancelOrder` („Cancel an order“, einziges Feld `orderId`) den Altbezeichner `TXAFREIBER`, und das Modell markiert den Auftrag als storniert und entfernt ihn aus der nächsten Aktionsliste ([Q50](QUELLEN.md#q50); [Q49](QUELLEN.md#q49), *Ordered action management › Ordering › Cancel order*); (5) das Glossar definiert den Sperrfreigabeauftrag als Auftrag, „ein Objekt von der jeweiligen Sperrliste zu nehmen“ ([Q02](QUELLEN.md#q02), S. 87 f.); (4) dieselbe Spezifikation bildet `TXSAUFB` auf `addEntitlementToHotlist` und `TXSFREIB` auf `removeEntitlementFromHotlist` ab, die „Freigabe“ ist dort also das Entfernen aus der Hotlist ([Q50](QUELLEN.md#q50), `hotlist-messaging_xsd`). **Offen bleibt** eine ausdrückliche Definition und die Frage, ob sich die Freigabe auf den Auftrag oder auf die Berechtigung bezieht. Die frühere Lesart „gibt einen vorbereiteten Auftrag frei“ ist aufgegeben. *Korrektur:* [Q39](QUELLEN.md#q39) ist eine **RMV**-Quelle („Aktionsmanagement RMV-EFS“), nicht aus NRW — eine frühere Fassung dieser Zeile ordnete sie NRW zu. | `aktionsmanagement/aktionsfreigabe.md` | KA AktM-SPEC, KA SST-SPEC |
| **O21** | Wozu führt der räumliche Geltungsbereich neben der `OriginalValidityAreaList` eine `AlternativeValidityAreaList`? Beide haben dieselben Felder (Typangabe, Organisation des Product Owners, Liste); die Typbeschreibung und das Modell ([Q51](QUELLEN.md#q51), Modul `et`; [Q49](QUELLEN.md#q49), Paket *Types*) erklären den Zweck der zweiten Liste nicht. | `berechtigungen/gueltigkeitsbereich-asn-1.md` | etiCORE-Spezifikation, Product-Owner-Vorgaben |
| **O22** | Der Warncode `W_CO_ENTITLEMENT_ISSUED_WITH_INVALID_ACTION_COUNTER` trägt in der Quelle die Beschreibung „The initial entitlement status is invalid“, die zum Namen (Aktionszähler) nicht passt. Welche Prüfung ist gemeint? ([Q50](QUELLEN.md#q50), `common-event-enums_xsd`.) | `transaktionen/warnungen-in-eticore.md` | etiCORE-Spezifikation, spätere Fassung |

---

## 5a. Inzwischen geklärte Fragen

Hier bleiben die Antworten stehen, damit die Nummern nachvollziehbar sind und nicht erneut gefragt wird.

**O7 — Zeitschiene für (((etiCORE als KA-Version 3: geklärt.**
Ein neues Root-Zertifikat gibt es erst für die 2. Generation der Sicherheitsinfrastruktur, „mit der Einführung der VDV-Kernapplikation 3.0 mit dem neuen Namen (((etiCORE zum **1. Dezember 2026**“. Die aktuellen SubCA-Zertifikate sind zehn Jahre bis zum **1. Dezember 2031** gültig, „also bis zum Ende der VDV-Kernapplikation 1.x“. Im Übergangszeitraum 2026 bis 2031 sind beide Zertifikate gültig und ermöglichen den **Parallelbetrieb von VDV-KA 1.x (1GSI) und (((etiCORE (2GSI)** ([Q42](QUELLEN.md#q42)). *Sekundärquelle — für verbindliche Aussagen beim VDV eTS bestätigen lassen.*

**O8 — Stand bei 1GSI und 2GSI: geklärt.**
Die aktive Gültigkeit des Root-Zertifikats der 1GSI ist **zum 1. Dezember 2021 abgelaufen**; damit lassen sich keine neuen Zertifikate mehr erstellen, die bestehenden SubCA-Zertifikate bleiben aber gültig ([Q42](QUELLEN.md#q42)).
Dazu ein praktisch wichtiger Nebenbefund: Einige Systeme prüfen bei Ausgabe oder Kontrolle, ob das Root-Zertifikat *zu diesem Zeitpunkt* gültig ist. Das ist **falsch** und führt seit dem 1. Dezember 2021 zu Fehlverhalten. Richtig ist die Prüfung, ob das Root-Zertifikat **zum Zeitpunkt der Erstellung des SubCA-Zertifikats** gültig war. Dieser Befund gehört in den Artikel `sicherheit/cv-zertifikat.md` und ist für das Analysewerkzeug eine Prüfregel.

**O11 — eTicket-Bezug der Bundestags-Drucksache: geklärt, Quelle bleibt.**
[Q24](QUELLEN.md#q24) ist die Antwort der Bundesregierung auf die Kleine Anfrage Drucksache 18/10915 mit dem Titel „Pläne der Bundesregierung für einheitliches elektronisches Ticketing (eTicketing) in Deutschland“ vom 06.02.2017 — am Dokument geprüft. Der Bezug besteht also; die Quelle dokumentiert den politischen Rahmen und wird in `grundlagen/eticket-deutschland.md` zitiert.

**O3 — Berechtigungsstatus-Werte: Werte geklärt.** Die Reichweite bleibt als O3 in der Tabelle oben offen.
[Q05](QUELLEN.md#q05), Kap. 2.1, nennt `berStatus` mit Datentyp `INT1`, einem Byte und der Codeliste **`WertobjektStatus_CODE`**; als „relevante Werte“ sind aufgeführt: **5** = Zurückgenommen / Cancelled, **7** = Aktiv / entsperrt / o.k., **8** = Neu, aber noch nicht aktiv / New, **19** = Gesperrt / Blocked. Ausgearbeitet in `berechtigungen/berstatus.md`.
Zur Reichweite: Die Formulierung „Codeliste `WertobjektStatus_CODE`, relevante Werte“ und die englischen Bezeichnungen zeigen eine **Auswahl aus einer Standardcodeliste**, nicht eine RMV-eigene Festlegung (abgeleitet). Die Liste selbst steht in der KA BOM-SPEC. Die Teilfrage, warum „neu“ (8) einen höheren Code als „aktiv“ (7) hat, ist damit beantwortet: Die Codes sind Zustandskennungen ohne Reihenfolge.

**O12 — Wirkung der Aktionsfreigabe: geklärt, verbundspezifisch.**
[Q39](QUELLEN.md#q39), Kap. 3.2.5, nennt die Nachrichten und ihre Richtung: `TXAFREIBER` ist der Aktionsfreigabeauftrag des beauftragenden KVP an PV bzw. ALISE, `TXAFREIMITBER` die Aktionsfreigabemitteilung des ALISE zurück an den beauftragenden KVP, beide asynchron. Ausgearbeitet in `aktionsmanagement/aktionsfreigabe.md`. **Offen bleibt**, wo die Freigabe im Statusmodell des Standards ansetzt — das Glossar kennt den Begriff nicht.

---

## 5b. Ein Vorfall, der die Fundstellen betraf

Am 19.10.2026 wurde `tools/pdftext.py` um die Unterstützung komprimierter Objektströme erweitert (PDF 1.5 und neuer). Der Regressionstest verglich damals die **Textmenge** je Quelle und war unauffällig. Unbemerkt blieb, dass der Seitenbaum nun mehr Seiten findet und sich die **Zählung** verschiebt.

Folge: In [Q06](QUELLEN.md#q06) lagen alle PDF-Seitenangaben um eine Seite zu niedrig, bei [Q25](QUELLEN.md#q25) vier und bei [Q39](QUELLEN.md#q39) eine. Betroffen waren **77 Fundstellen** in Artikeln und Frontmatter — alle vor der Werkzeugänderung geschrieben. Inhaltlich war nichts falsch, aber jede dieser Angaben hätte beim Nachschlagen auf die falsche Seite geführt.

Gefunden wurde das zufällig beim Vergleich zweier Kopien desselben Dokuments. Das ist der unbefriedigende Teil: Die Quellenpflicht dieses Lexikons steht und fällt mit der Richtigkeit der Fundstellen, und es gab keine Prüfung dafür.

**Behoben:** alle 77 Angaben korrigiert, verifiziert an den Seitenfüßen der Dokumente, die ihre eigene Seitenzahl nennen. Neu ist [tools/fundstellen.py](tools/fundstellen.py) mit 25 Stichproben; `CLAUDE.md`, Regel 10, verlangt den Lauf nach jeder Änderung am Extraktor.

**Lehre für künftige Werkzeugänderungen:** Ein Regressionstest auf Textmenge genügt nicht. Geprüft werden muss, was die Artikel tatsächlich zitieren.

### Zwei Nachträge vom 20.10.2026

**Der Steuerzeichenfilter, der nur in der Commit-Nachricht stand.** Der Commit `aadeeb8` nennt als
Behebung einen Filter, der Steuerzeichen aus der Extraktion entfernt. Im Code war er nie vorhanden —
die Änderung ging zwischen Beschreibung und Umsetzung verloren, und die Nachricht blieb unkorrigiert
stehen. Aufgefallen ist es, als eine neue Fundstellenprobe auf [Q48](QUELLEN.md#q48), S. 16,
scheiterte: Die Seite liefert UTF-16-kodierten Text, dessen NUL-Bytes jedes Suchmuster zerschneiden.
Der Filter steht jetzt am Ende von `extract()`; `tools/fundstellen.py` prüft seither 55 statt 25
Fundstellen und läuft fehlerfrei. **Lehre:** Eine Commit-Nachricht ist kein Beleg. Was sie behauptet,
muss im Code stehen — und geprüft sein.

**Rekonstruierte Zitate.** Für die Artikel zu [Q45](QUELLEN.md#q45) und [Q46](QUELLEN.md#q46) wurde
zunächst aus der gesäuberten Extraktion zitiert. Diese Quellen verlieren aber Umlaute und ganze
Wortteile; aus `f` wird beim Lesen stillschweigend `für`, aus `igt` ein `benötigt`. Das Ergebnis liest
sich wie ein wörtliches Zitat, ist aber eine Rekonstruktion. Die betroffenen Stellen in
`zsam.md`, `key-identifier.md`, `uic-barcode.md`, `vdv-barcode-mobile.md` und
`pflichtelemente-einer-transaktion.md` wurden in Paraphrasen umgeschrieben; in Anführungszeichen
steht nur noch, was im Rohtext wörtlich steht. [CLAUDE.md](CLAUDE.md), Regel 10, hält das fest.

---

## 6. Qualitätsregeln

Vollständig in [CLAUDE.md](CLAUDE.md). Die vier wichtigsten:

1. **Keine erfundenen Fakten.** Codewerte, Feldbedeutungen und Abläufe nur mit Quelle. Was nicht belegt ist, wird markiert und hier in Abschnitt 5 eingetragen.
2. **Fundstelle statt Dokumentname.** Nicht „laut Q06“, sondern „[Q06](QUELLEN.md#q06), Kap. 2.1.5“.
3. **Das Beispiel darf vereinfachen, aber der fachlichen Erklärung nicht widersprechen.** Es darf nichts behaupten, was dort nicht steht.
4. **Urheberrecht.** Keine Volltexte aus vertraulichen Dokumenten, nur kurze Exzerpte mit Fundstelle.

---

## 7. Was als Nächstes passiert

Die **zwei Musterartikel** liegen vor und sind der eigentliche Gegenstand der Freigabe:

- Kategorieartikel: [lexikon/aktionsmanagement.md](lexikon/aktionsmanagement.md)
- Blattartikel: [lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md](lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md) (Transaktionstyp 37)

Sie sind absichtlich zuerst entstanden, obwohl sie laut Phasenplan später kämen: Ohne zwei echte Artikel lässt sich weder der Ton beurteilen noch die Werkzeugkette prüfen. Beides ist jetzt belegt — `check.py` erfasst Wortlimits, Links, Anker, Baum, Dateinamen und veraltete Navigationsblöcke, geprüft an einem absichtlich fehlerhaften Testartikel.

**Erst nach Freigabe des Tons** entstehen die restlichen 64 Artikel der Startmenge. Diese Reihenfolge ist wichtig, weil eine Korrektur an Aufbau oder Tonfall sonst 66 Dateien betrifft.

Zur Freigabe gehören drei Fragen:

1. Stimmen **Länge und Tonfall** der beiden Abschnitte? Das Beispiel ist mit rund 320 Wörtern deutlich kürzer als erlaubt — bewusst, es ließe sich auch ausführlicher anlegen.
2. Ist der **Schnitt der Startmenge** richtig ([STRUKTUR.md](STRUKTUR.md), Abschnitt 11): zuerst die sechs Kategorien, die das Analysewerkzeug braucht, und Medien, Kontrolle, Sicherheit sowie ABT später?
3. Wie wird mit den drei Rechercheakten umgegangen (Abschnitt 8)?

---

## 8. Die drei Rechercheakten

**Entscheidung vom 19.10.2026:** Alle drei Dateien bleiben im öffentlichen Repository, `Quellen_LBV.md` jedoch nur **bereinigt**.

Durchgeführt:

- In [Quellen_LBV.md](Quellen_LBV.md) sind alle Werte des Originaldatensatzes durch die fiktiven Entsprechungen aus [welt/baerstadt.md](welt/baerstadt.md) ersetzt: Organisations-IDs, Berechtigungs- und Applikationsnummer, Produktnummer, die drei Schlüsselnummern sowie Name und Geburtsdatum im produktspezifischen Teil. Das Geburtsdatum ist maskiert, der codierte Bezahlmittel-Wert entfernt. Ein Hinweis am Dateianfang sagt das. Die fachliche Argumentation ist unverändert.
- Spekulationen darüber, welche realen Unternehmen hinter den IDs stehen, sind entfernt — mit fiktiven IDs wären sie ohnehin sinnlos.
- Dieselben Werte waren auch in [QUELLEN.md](QUELLEN.md), [STRUKTUR.md](STRUKTUR.md), [CLAUDE.md](CLAUDE.md), [welt/baerstadt.md](welt/baerstadt.md), [QUELLEN_VDV-KA.md](QUELLEN_VDV-KA.md) und [QUELLEN_ALISE.md](QUELLEN_ALISE.md) enthalten — teilweise in den Regeln, die ihre Verwendung verbieten. Auch dort sind sie durch abstrakte Formulierungen ersetzt. Eine Regel, die ihr eigenes Verbot unterläuft, taugt nicht.
- Die Zitate aus den Verbunddokumenten sind durchweg kurze Exzerpte mit Fundstelle und bleiben unverändert.

**Dauerhafte Regel:** Originalwerte aus [Q11](QUELLEN.md#q11) kommen nicht ins Repository, auch nicht beispielhaft, auch nicht in Kommentaren oder Regeltexten. Übernommen werden nur Feldnamen und Strukturen; Werte liefert die Welt-Bibel. Vor einem Push lohnt die Gegenprobe:

```sh
grep -rn --include='*.md' -E '<die betreffenden Werte>' .
```

[QUELLEN_VDV-KA.md](QUELLEN_VDV-KA.md) und [QUELLEN_ALISE.md](QUELLEN_ALISE.md) bleiben als Arbeitsstand erhalten. Sie sind durch [QUELLEN.md](QUELLEN.md) inhaltlich überholt und werden nicht zitiert.
