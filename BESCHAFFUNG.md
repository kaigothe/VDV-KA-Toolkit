# Benötigte VDV-KA-Dokumentation

**Stand:** 2026-10-19 · **Zweck:** Anfrageliste für den VDV eTicket Service bzw. für Kontakte, die Zugang zu den KA-Spezifikationen haben.

Diese Liste ist zum Weitergeben gedacht. Sie nennt zu jedem Dokument, **warum** es gebraucht wird und **welche konkrete Frage** es klärt — das erleichtert die Entscheidung auf der Gegenseite und zeigt, dass nicht pauschal „alles“ angefragt wird.

Die Inventarnummern und Kurzzeichen stammen aus Kapitel 3 „VDV-KA-Dokumentation“ des öffentlich auffindbaren eTicket-Regelwerks ([Q25](QUELLEN.md#q25)). Die Existenz der Dokumente ist damit belegt, ihr Inhalt nicht.

---

## 1. Hintergrund der Anfrage

Es entsteht ein **Lexikon zur VDV-Kernapplikation 1.x** als Nachschlagewerk: ein kleiner Artikel je Fachbegriff, jede Aussage mit Quelle und Fundstelle, klar getrennt in *belegt*, *abgeleitet* und *zu prüfen*. In einer zweiten Stufe soll daraus ein Werkzeug entstehen, das ALISE-Nachrichten einliest, ihre Felder erklärt und offensichtliche Fehler kennzeichnet.

Gearbeitet wird bisher ausschließlich mit **öffentlich verfügbaren** Unterlagen: dem Glossar des VDV eTicket Service, dem eTicket-Regelwerk, Pflichtenheften einzelner Verbünde (RMV, AVV, Westfalen-Tarif, NRW) und Sekundärquellen.

Das führt zu einem Problem, das sich mit öffentlichen Quellen nicht lösen lässt: **Codewerte und Feldbedeutungen sind nur aus den Festlegungen einzelner Verbünde bekannt.** Ob sie KA-weit gelten, ist nicht feststellbar. Das Lexikon kennzeichnet solche Aussagen bisher als verbundspezifisch und `zu prüfen` — brauchbar, aber unbefriedigend, und für ein Auswertungswerkzeug riskant: Eine falsch interpretierte Statusnummer erzeugt überzeugend formatierte Fehlauskünfte.

**Nutzung und Vertraulichkeit:** Die Dokumente werden ausschließlich zum Verstehen und Prüfen verwendet. Das Lexikon-Repository ist öffentlich; darin stehen nur **Verweise und kurze Exzerpte mit Fundstelle**, keine Volltexte, keine Dateien. Gern wird vorab abgestimmt, in welchem Umfang aus den Dokumenten zitiert werden darf.

---

## 2. Was bereits vorliegt

Damit nichts doppelt angefragt wird:

| Dokument | Fundort |
|---|---|
| KA Glossar (Inv. 0), Fassung „VDV-KA 1.X / (((etiCORE“ | öffentlich auf eticket-deutschland.de |
| eTicket-Regelwerk / Teilnahmevertrag mit Anlagen, V1.27 | öffentlich auffindbar |
| RMV vHGS Pflichtenhefte PH 05-A1, PH 06-02, EFM-Integration, Statische Berechtigung | öffentlich auffindbar |
| Technische Dokumente des KCD NRW (Deutschlandticket, Abbildung und Kontrolle, Produktparameter, Weißbuch ABT) | öffentlich auf kcd-nrw.de |

Falls vom **Glossar eine neuere Fassung** existiert, wäre sie willkommen — der vorliegenden fehlen die Einträge „Synchronnummer“, „Berechtigungsstatus“ und „Aktionsfreigabe“.

---

## 3. Priorität 1 — ohne diese Dokumente bleiben zentrale Artikel unbelegt

| Inv.-Nr. | Kurzzeichen | Titel | Wofür konkret |
|---:|---|---|---|
| **41** | **KA AktM-SPEC** | Aktionsmanagement für die Berechtigungsart EFS | **Das wichtigste Dokument der Liste**, mit Abstand am häufigsten als Normquelle genannt (siehe Abschnitt 9a). Klärt vier der offenen Fragen: die Codeliste des Auftragstyps, das Verhältnis von Aktionstyp und Auftragstyp, die Bedeutung der Aktionsfreigabe und die Semantik der Änderungsreferenz. Außerdem die Struktur der `TXAML`. |
| **4** | **KA SST-SPEC** | Schnittstellenspezifikation der Referenzsysteme | Struktur von `TX_BASE`, `TXABER`, `TXRBER`, `TXSNAWB`, `TXEBER`, `TXEMBER`, `TXKNAWA/B/DM`, `TXTRANSABBRUCH`. Nach der KA AktM-SPEC das zweithäufigst genannte Dokument (siehe Abschnitt 9a). |
| **1** | **KA BOM-SPEC** | Hauptdokument mit Basisobjektmodell (BOM) | Die Codelisten selbst: `IONTransaktionsTyp_CODE`, `NmTransaktionsTyp_CODE`, `AblehnungsTyp_CODE`, Berechtigungsstatus. Damit ließe sich endlich entscheiden, welche Codewerte KA-weit gelten und welche verbundspezifisch sind. |
| **5** | **KA XML-Schemata und WSDL** | XSD der TX-Transaktionen, einschließlich Abhängigkeiten | Ohne Schema ist keine Validierung möglich. Benötigt werden die **vollständigen** Schemadateien mit allen Includes und Imports, nicht einzelne Dateien. |
| — | **ALISE** | ALISE-Schnittstellenbeschreibung und ALISE-XSD | Siehe Abschnitt 6: die Nachricht `txalisber` ist in keiner öffentlichen Quelle dokumentiert. |

---

## 4. Priorität 2 — für geplante Kategorien des Lexikons

| Inv.-Nr. | Kurzzeichen | Titel | Wofür |
|---:|---|---|---|
| 2 | Anlage TLV EFS | Anlage 1 zur technischen Spezifikation (TLV-Struktur des EFS) | TLV-Tags des produktspezifischen Teils, u. a. Tag 0xDB „Fahrgast“. Klärt eine Längenabweichung in einem vorliegenden Datensatz. |
| 40 | KA MultiBER-SPEC | Multiberechtigungen | `TXAMBER`, `TXEMBER`, `TXRMBER` |
| 8 | KA SAM-SPEC | Spezifikation des SAM | MAC-Bildung, Schlüsselreferenzen, CV-Zertifikate und ihre Keytypes |
| 6 | KA SEC-SPEC | Technisches Konzept Sicherheit | Sicherheitsebenen, Schlüsselhierarchie, Verhältnis von 1GSI und 2GSI |
| 11 | KA KOSES-Spec | Funktionale Spezifikation Sperrlistenmanagementsystem | Sperrlisten `TXSLNM`, `TXSLK`, `TXSLOS` und die `*RESP`-Varianten ab KA 1.3.0 |
| 42 | KA STB-Spec | Statische Berechtigungen für 2D-Barcode-Tickets | VDV-Barcode, Abgrenzung zum UIC-Barcode |
| 33 | KA TXx-Prüfungs-ANW | Verfahrensanweisung zur Prüfung von Transaktionen in EFM-Systemen | Direkt relevant für das Werkzeug: welche Prüfungen sind vorgesehen und in welcher Reihenfolge |
| 3 | Anlage Datenschutz | Anlage 2 zum Hauptdokument | Welche Attribute dürfen bzw. müssen reduziert werden, und wie verhält sich das zur MAC-Validierung |

---

## 5. Priorität 3 — Vollständigkeit

| Inv.-Nr. | Kurzzeichen | Wofür |
|---:|---|---|
| 7 | KA NM-SPEC | Nutzermedium, Applikation, Speicheraufbau |
| 9 | KA ION-SPEC | Datenaustausch im Interoperabilitätsnetzwerk |
| 12–21 | KA SysLH (HD, PVS, KVPS, KVPRT, DLS, DLRT, NM) | Terminalabläufe, Kontrolltransaktion, `EXECUTE TRANSACTION` |
| 35 | KA PROD_ID-ANW | Vergabe von Produkt-IDs und Nummernräume |
| 37 | KA App-Ber-Sperr-ANW | Nutzung der Applikations- und Berechtigungssperre |
| 53–57 | KA PKM-… | Produkt-, Kontroll- und Tarifmodule |
| 59 | KA SAM-Server-SPEC | SAM-Server-Schnittstelle |

---

## 6. Besonders dringlich: ALISE

Ausgangspunkt des Vorhabens war eine reale Nachricht, die so beginnt:

```xml
<ns:txalisber xmlns:ns="http://vdv/ka/alise/2">
```

Zu dieser Nachricht ist in **keiner** öffentlichen Quelle etwas zu finden. Das umfangreichste verfügbare Projektdokument (RMV PH 06-02) kennt `txalisber` nicht; dort heißt die Aktionsliste `TXAML`.

Offen ist deshalb:

1. **Was ist `txalisber`?** Ein Element innerhalb einer `TXAML`, eine eigene Nachricht der ALISE-Schnittstelle oder eine verbund- bzw. herstellerspezifische Variante?
2. **Welche Schema- und Spezifikationsversion gehört zum Namespace `http://vdv/ka/alise/2`?** Aus der Ziffer 2 lässt sich kein Release ableiten, sie ist Bestandteil des Namensraums.
3. **Gibt es eine eigenständige ALISE-Schnittstellenbeschreibung** neben der KA AktM-SPEC — etwa für einen aus dem PV-System ausgelagerten zentralen ALISE-Server, für den laut RMV PH 06-02 ab KA 1.3.0 der Rollencode 31 reserviert ist?

Benötigt werden: die **ALISE-Schnittstellenbeschreibung**, die **ALISE-XSD samt allen Abhängigkeiten** und, falls vorhanden, **Beispielnachrichten**.

---

## 7. Über die Dokumente hinaus nützlich

| Gegenstand | Wofür |
|---|---|
| **Codelisten in maschinenlesbarer Form**, falls es sie gibt (XML, CSV, Excel) | Das Werkzeug soll numerische Werte auflösen. Eine Liste als Datei erspart das Abtippen aus PDFs und damit Übertragungsfehler. |
| **Beispielnachrichten und Testdaten** je Nachrichtentyp | Zum Prüfen des Parsers. Eine einzige Beispielnachricht reicht nicht, um ein Feld zu verstehen — etwa die Änderungsreferenz, die im vorliegenden Datensatz den Wert 0 trägt und deren Aussehen im Änderungsfall deshalb unbekannt ist. |
| **Release- und Versionsübersicht** mit Gültigkeitszeiträumen | Welche Releases sind aktuell unterstützt, welche abgekündigt? Das Regelwerk erwähnt „entfallen ab Release 1.6.0“, ohne dass dieses Release anderweitig greifbar ist. |
| **Stand von (((etiCORE als KA-Version 3** | Einführungszeitpunkt und Dauer des Parallelbetriebs zur VDV-KA 1.x. Bisher nur über Sekundärangaben bekannt. |
| **Verhältnis von 1GSI und 2GSI** | Das Glossar datiert 1GSI „bis 2026 bzw. 2031“ und 2GSI „ab 2026“. Wie ist der Stand heute? |
| **Organisationsverzeichnis** (Org-ID zu Organisation und Rolle), soweit zugänglich | Das Werkzeug soll Organisationskennungen auflösen können. Falls nicht herausgebbar, genügt die Auskunft, ob und wie Lizenznehmer darauf zugreifen. |

---

## 8. Benötigte Versionen

Für die Schnittstellen- und Objektmodell-Dokumente werden **mehrere Versionen** gebraucht, weil die vorliegenden Projektdokumente ausdrücklich zwischen ihnen unterscheiden und Nachrichten aus verschiedenen Releases auftreten können:

- **KA 1.1.07** — die ältere Schnittstellenversion, in den Projektdokumenten als `*_1107` referenziert
- **KA 1.3.0** — in den Projektdokumenten als `*_1300` referenziert; bringt Multiberechtigungen, die `*RESP`-Sperrlistenvarianten und geänderte Pflichtfelder im `TX_BASE`
- **KA 1.5.0** — Änderungen u. a. beim Aktionsmanagement, bisher nur über eine Sekundärquelle bekannt
- **das aktuell unterstützte Release** sowie, falls abweichend, das für Neuanbindungen vorgesehene

---

## 9. Offene Fachfragen und das jeweils klärende Dokument

Die Nummern entsprechen der Liste „Offene Fragen“ in [PLAN.md](PLAN.md), Abschnitt 5. Jede dieser Fragen ist in mindestens einem Lexikonartikel sichtbar als `zu prüfen` gekennzeichnet.

| Nr. | Frage | Klärendes Dokument |
|---|---|---|
| **O1** | Gelten die Transaktionstypen 37, 38 und 39 für Ausgabe, Entsperrung und Rücknahme über Aktionsliste KA-weit oder nur im eTicket RheinMain? | KA BOM-SPEC (Inv. 1), KA SST-SPEC (Inv. 4), KA AktM-SPEC (Inv. 41) |
| **O2** | Was bedeutet `amAuftragsTyp` = 13? | KA AktM-SPEC (Inv. 41) |
| **O3** | Sind die Berechtigungsstatus-Werte 5, 7, 8 und 19 KA-weit festgelegt? Warum hat „neu“ einen höheren Code als „aktiv“? | KA BOM-SPEC (Inv. 1) |
| **O4** | Welche Spezifikations- und Schemaversion gehört zu `http://vdv/ka/alise/2`? | ALISE-XSD, KA XML-Schemata (Inv. 5) |
| **O5** | Erhöht ein reiner Statuswechsel die `berSynchronNummer`? | KA BOM-SPEC (Inv. 1), KA AktM-SPEC (Inv. 41) |
| **O6** | In einem vorliegenden produktspezifischen Teil gibt die TLV-Länge 87 Byte an, es folgen 90 Byte. Füllbytes, Übertragungsfehler oder falsche TLV-Annahme? | Anlage TLV EFS (Inv. 2) |
| **O7** | Zeitschiene für (((etiCORE als KA-Version 3 und Dauer des Parallelbetriebs? | Release-/Versionsübersicht |
| **O8** | Aktueller Stand bei 1GSI und 2GSI? | KA SEC-SPEC (Inv. 6), aktuelle Fassung des Glossars |
| **O9** | Verhältnis der Begriffe „Aktion“, „Aktionstyp“ und „Auftragstyp“ — synonym oder zwei Ebenen? | KA AktM-SPEC (Inv. 41) |
| **O12** | Was bewirkt die „Aktionsfreigabe“? Das Glossar kennt den Begriff nicht, das Regelwerk nennt nur die Anwendungsfälle „Aktionsfreigabe senden“ und „Aktionsfreigabemitteilung entgegennehmen“. | KA AktM-SPEC (Inv. 41) |
| **O13** | Welchen Wert trägt `amAenderungsreferenz_ID` bei einer tatsächlichen Änderung, und nimmt es Berechtigungsnummer samt Organisation des Vorgängers auf? | KA AktM-SPEC (Inv. 41), Beispielnachrichten |
| **O14** | Wie verhält sich `txalisber` zu `TXAML`? | ALISE-Schnittstellenbeschreibung, KA AktM-SPEC (Inv. 41) |

**Zusammengefasst:** Die **KA AktM-SPEC** allein würde sechs der zwölf Fragen klären, zusammen mit **KA BOM-SPEC** und den **XML-Schemata** zehn von zwölf.

---

## 9a. Verwendung im Lexikon

Dieser Abschnitt wird von `tools/gen.py` aus den Artikeln erzeugt und ist **nicht von Hand zu pflegen**. Er zeigt, welcher Artikel welches nicht öffentliche Dokument als Normquelle nennt — damit auf der Gegenseite nachvollziehbar ist, dass die Anfrage aus konkretem Bedarf entsteht und nicht pauschal gestellt wird.

<!-- GEN:verwendung -->
**5 nicht öffentliche Dokumente** werden derzeit in 26 Artikeln als Normquelle genannt, nach Häufigkeit:

| Nennungen | Inv.-Nr. | Dokument | genannt in |
|---:|---:|---|---|
| 27 | 41 | **KA AktM-SPEC** | [Aktionsdifferenzliste](lexikon/aktionsmanagement/aktionsdifferenzliste.md), [Aktionsfreigabe](lexikon/aktionsmanagement/aktionsfreigabe.md), [Aktionsliste](lexikon/aktionsmanagement/aktionsliste.md), [Aktionsmanagement](lexikon/aktionsmanagement.md), [Änderungsreferenz](lexikon/aktionsmanagement/aenderungsreferenz.md), [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md), [Ausgabe EFS über Aktionsliste](lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md), [Terminalaktionsliste](lexikon/aktionsmanagement/terminalaktionsliste.md), [TXABER](lexikon/transaktionen/txaber.md), [TXAML](lexikon/transaktionen/txaml.md), [TXRBER](lexikon/transaktionen/txrber.md), [TXSNAWB](lexikon/transaktionen/txsnawb.md) |
| 19 | 4 | **KA SST-SPEC** | [Transaktionen](lexikon/transaktionen.md), [TX_BASE](lexikon/transaktionen/tx-base.md), [TXABER](lexikon/transaktionen/txaber.md), [TXAML](lexikon/transaktionen/txaml.md), [TXEBER](lexikon/transaktionen/txeber.md), [TXRBER](lexikon/transaktionen/txrber.md), [TXSNAWB](lexikon/transaktionen/txsnawb.md) |
| 4 | 5 | **KA XML-Schemata und WSDL** | [Transaktionen](lexikon/transaktionen.md), [TX_BASE](lexikon/transaktionen/tx-base.md) |
| 2 | 1 | **KA BOM-SPEC** | [logTransaktionsTyp](lexikon/transaktionen/logtransaktionstyp.md) |
| 1 | — | **ALISE-Schnittstelle und ALISE-XSD** | [txalisber](lexikon/transaktionen/txalisber.md) |

### Artikel, die ohne diese Dokumente unvollständig bleiben

| Artikel | offene Fragen |
|---|---|
| [Aktionsfreigabe](lexikon/aktionsmanagement/aktionsfreigabe.md) | O12 |
| [Änderungsreferenz](lexikon/aktionsmanagement/aenderungsreferenz.md) | O13 |
| [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md) | O2, O9 |
| [txalisber](lexikon/transaktionen/txalisber.md) | O4, O14 |

### Offene Fragen und die betroffenen Artikel

| Frage | betrifft |
|---|---|
| **O1** | [Ausgabe EFS über Aktionsliste](lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md), [Entsperrung über Aktionsliste](lexikon/aktionsmanagement/entsperrung-ueber-aktionsliste.md), [logTransaktionsTyp](lexikon/transaktionen/logtransaktionstyp.md), [Rücknahme EFS über Aktionsliste](lexikon/aktionsmanagement/ruecknahme-efs-ueber-aktionsliste.md), [Transaktionen](lexikon/transaktionen.md), [TXABER](lexikon/transaktionen/txaber.md), [TXRBER](lexikon/transaktionen/txrber.md), [TXSNAWB](lexikon/transaktionen/txsnawb.md) |
| **O2** | [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md), [Ausgabe EFS über Aktionsliste](lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md) |
| **O3** | [Rücknahme EFS über Aktionsliste](lexikon/aktionsmanagement/ruecknahme-efs-ueber-aktionsliste.md) |
| **O4** | [txalisber](lexikon/transaktionen/txalisber.md) |
| **O9** | [Aktion](lexikon/aktionsmanagement/aktion.md), [Aktionsmanagement](lexikon/aktionsmanagement.md), [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md) |
| **O12** | [Aktionsfreigabe](lexikon/aktionsmanagement/aktionsfreigabe.md) |
| **O13** | [Änderungsreferenz](lexikon/aktionsmanagement/aenderungsreferenz.md) |
| **O14** | [txalisber](lexikon/transaktionen/txalisber.md) |

*Erzeugt aus 26 Artikeln. Die Links führen in das Lexikon.*
<!-- /GEN:verwendung -->

---

## 10. Anfragetext zum Weitergeben

Der folgende Text lässt sich direkt verwenden — per E-Mail an `service@eticket-deutschland.de` oder über einen persönlichen Kontakt. Die Liste oben kann als Anlage beigelegt werden.

> **Betreff:** Zugang zu VDV-KA-Spezifikationen für ein Dokumentationsvorhaben
>
> Guten Tag,
>
> ich arbeite mich in die VDV-Kernapplikation ein und baue dabei ein strukturiertes Nachschlagewerk zu Begriffen, Nachrichten und Codelisten auf. In einem zweiten Schritt soll daraus ein Werkzeug entstehen, das KA-Nachrichten — zunächst aus dem Aktionsmanagement bzw. von ALISE — einliest, ihre Felder erklärt und Inkonsistenzen kennzeichnet.
>
> Bisher arbeite ich ausschließlich mit öffentlich verfügbaren Unterlagen: dem Glossar VDV-KA / (((etiCORE, dem eTicket-Regelwerk und Pflichtenheften einzelner Verbünde. Damit komme ich bei den fachlichen Grundlagen weit, bei den **Codelisten und Feldsemantiken** aber nicht: Dort sind mir nur die Festlegungen einzelner Verbünde bekannt, und ich kann nicht entscheiden, ob sie KA-weit gelten. Für ein Auswertungswerkzeug ist das heikel — eine falsch interpretierte Statusnummer führt zu überzeugend aussehenden Fehlauskünften.
>
> Ich würde daher gern Zugang zu folgenden Dokumenten erhalten, in dieser Reihenfolge der Dringlichkeit:
>
> 1. **KA AktM-SPEC** (Inventarnummer 41, „Aktionsmanagement für die Berechtigungsart EFS“)
> 2. **KA SST-SPEC** (Inventarnummer 4, Schnittstellenspezifikation der Referenzsysteme)
> 3. **KA BOM-SPEC** (Inventarnummer 1, Hauptdokument mit Basisobjektmodell) — vor allem wegen der Codelisten
> 4. **KA XML-Schemata und WSDL** (Inventarnummer 5), vollständig mit allen Abhängigkeiten
> 5. **ALISE-Schnittstellenbeschreibung und ALISE-XSD**
>
> Besonders zu ALISE habe ich eine konkrete Frage: Mir liegt eine Nachricht mit dem Element `txalisber` im Namespace `http://vdv/ka/alise/2` vor. Dieses Element finde ich in keiner öffentlichen Unterlage; im RMV-Pflichtenheft PH 06-02 heißt die Aktionsliste `TXAML`. Ist `txalisber` ein Element innerhalb der `TXAML`, eine eigene Nachricht der ALISE-Schnittstelle oder eine herstellerspezifische Variante? Und welche Spezifikations- und Schemaversion gehört zu diesem Namespace?
>
> Weiter wären hilfreich: Codelisten in maschinenlesbarer Form, Beispielnachrichten je Nachrichtentyp sowie eine Übersicht der aktuell unterstützten Releases. Bei den Schnittstellendokumenten benötige ich die Versionen **1.1.07** und **1.3.0** — die Projektdokumente unterscheiden ausdrücklich zwischen beiden — sowie **1.5.0** und das aktuell unterstützte Release.
>
> Eine Anlage mit der vollständigen Liste, der Begründung je Dokument und den konkreten offenen Fragen kann ich gern beifügen.
>
> Zur Nutzung: Die Dokumente verwende ich ausschließlich zum Verstehen und Prüfen. Mein Nachschlagewerk ist öffentlich, enthält aber nur Verweise und kurze Exzerpte mit Fundstelle, keine Volltexte und keine Dateien. Falls das zu weit geht oder Sie eine andere Handhabung wünschen, richte ich mich danach — sagen Sie mir gern, in welchem Umfang ich zitieren darf.
>
> Falls der Zugang über das ASM-Tool oder eine Lizenznehmerschaft läuft: Können Sie mir sagen, welche Voraussetzungen dafür gelten und ob es für Einzelpersonen oder für Mitarbeitende eines Verkehrsunternehmens einen Weg gibt?
>
> Vielen Dank und freundliche Grüße

---

## 11. Was mit den Dokumenten geschieht

Damit die Zusage überprüfbar bleibt:

- Die Dateien kommen in `QUELLEN/` und damit **nicht** ins öffentliche Repository (`.gitignore`).
- Im Repository entstehen daraus **Exzerpte mit Fundstelle** in `exzerpte/` und Zitate in den Artikeln — kurz, mit Quellenangabe, nach den Regeln in [CLAUDE.md](CLAUDE.md), Abschnitt 9.
- Jede Quelle wird in [QUELLEN.md](QUELLEN.md) mit Stand, Version und Rechtehinweis eingetragen.
- Aussagen wechseln dann von `zu prüfen` auf `belegt`, und die betreffenden Einträge verschwinden aus der Liste der offenen Fragen.

**Navigation:** [Home](README.md) · [Quellenverzeichnis](QUELLEN.md) · [Plan](PLAN.md)
