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
| **41** | **KA AktM-SPEC** | Aktionsmanagement für die Berechtigungsart EFS und Entsperrung von AF… (vollständiger Titel nach [Q37](QUELLEN.md#q37)) | **Das wichtigste Dokument der Liste**, mit Abstand am häufigsten als Normquelle genannt (siehe Abschnitt 9a). Klärt vier der offenen Fragen: die Codeliste des Auftragstyps, das Verhältnis von Aktionstyp und Auftragstyp, die Bedeutung der Aktionsfreigabe und die Semantik der Änderungsreferenz. Außerdem die Struktur der `TXAML`. |
| **4** | **KA SST-SPEC** | Schnittstellenspezifikationen der Referenzsysteme, einschließlich Applikationsherausgeber (AH) und Sperrlistenservice (KOSE) | Struktur von `TX_BASE`, `TXABER`, `TXRBER`, `TXSNAWB`, `TXEBER`, `TXEMBER`, `TXKNAWA/B/DM`, `TXTRANSABBRUCH`. Nach der KA AktM-SPEC das zweithäufigst genannte Dokument (siehe Abschnitt 9a). |
| **1** | **KA BOM-SPEC** / **KA HD_BOM-SPEC** | Hauptdokument mit Basisobjektmodell (BOM) | Die Codelisten selbst: `IONTransaktionsTyp_CODE`, `NmTransaktionsTyp_CODE`, `AblehnungsTyp_CODE`, Berechtigungsstatus. Damit ließe sich endlich entscheiden, welche Codewerte KA-weit gelten und welche verbundspezifisch sind. |
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

Dank der Namenskonvention im eTicket-Regelwerk lässt sich die Bitte **präzise** formulieren. [Q25](QUELLEN.md#q25), Kap. 4.3.2 f. (PDF-S. 114 f.), definiert Dateinamen und Namensräume in EBNF. Dort erscheinen ausdrücklich:

- **WSDL-Bereiche** `PV_ALISE` und `KVP_ALISE`
- **Namensraum-Bereiche** `pv-alise` und `kvp-alise`
- der Namensraum endet auf `NamensraumBereich, ["types"], "/", Version`

Es gibt also offenbar **zwei** ALISE-Schnittstellen — eine zum Produktverantwortlichen und eine zum Kundenvertragspartner.

**Konkret benötigt:**

1. die **WSDL** für die Bereiche `PV_ALISE` und `KVP_ALISE`,
2. die zugehörigen **XSD samt allen Includes und Imports** für die Namensraum-Bereiche `pv-alise` und `kvp-alise`,
3. die fachliche **ALISE-Schnittstellenbeschreibung**,
4. **Beispielnachrichten** zu beiden Bereichen,
5. die Auskunft, welcher **Version** im Sinne der Namensraumkonvention die Angabe `http://vdv/ka/alise/2` entspricht und welche Releases unter dieser Version geführt werden.

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

- **KA 1.12.0** — **die wichtigste Bitte.** Ein Zulassungs-Prüfbericht von 2024 führt zwölf KA-Spezifikationen samt XML-Schemata und WSDL durchgehend in dieser Version auf ([Q37](QUELLEN.md#q37)), darunter KA AktM-SPEC, KA SST-SPEC, KA HD_BOM-SPEC und KA XML-Schemata. Sie ist damit deutlich neuer als alles, was in den öffentlichen Projektdokumenten referenziert wird.
- **KA 1.1.07** — die ältere Schnittstellenversion, in den Projektdokumenten als `*_1107` referenziert und dort weiterhin maßgeblich
- **KA 1.3.0** — als `*_1300` referenziert; bringt Multiberechtigungen, die `*RESP`-Sperrlistenvarianten und geänderte Pflichtfelder im `TX_BASE`
- **KA 1.5.0** — Änderungen u. a. beim Aktionsmanagement, bisher nur über eine Sekundärquelle bekannt
- **das aktuell verbindlich unterstützte Release** sowie, falls abweichend, das für Neuanbindungen vorgesehene

Hilfreich wäre außerdem eine **Einordnung des Verhältnisses von „Version“ und „Release“**. [Q25](QUELLEN.md#q25), Kap. 4.3.1.3 f., beschreibt, dass nur zwei Versionen gleichzeitig unterstützt werden und Releases innerhalb einer Version über den gemeinsamen Namensraum kompatibel bleiben. Wie sich dazu die Nummern 1.1.07, 1.3.0, 1.5.0 und 1.12.0 verhalten, ist von außen nicht erkennbar.

---

## 9. Offene Fachfragen und das jeweils klärende Dokument

Die Nummern entsprechen der Liste „Offene Fragen“ in [PLAN.md](PLAN.md), Abschnitt 5. Jede dieser Fragen ist in mindestens einem Lexikonartikel sichtbar als `zu prüfen` gekennzeichnet.

| Nr. | Frage | Klärendes Dokument |
|---|---|---|
| **O1** | Gelten die Transaktionstypen 37, 38 und 39 für Ausgabe, Entsperrung und Rücknahme über Aktionsliste KA-weit oder nur im eTicket RheinMain? | KA BOM-SPEC (Inv. 1), KA SST-SPEC (Inv. 4), KA AktM-SPEC (Inv. 41) |
| **O2** | Was bedeutet `amAuftragsTyp` = 13? | KA AktM-SPEC (Inv. 41) |
| **O3** | Sind die Berechtigungsstatus-Werte 5, 7, 8 und 19 KA-weit festgelegt? Warum hat „neu“ einen höheren Code als „aktiv“? | KA BOM-SPEC (Inv. 1) |
| **O4** | *Teilweise geklärt:* Die letzte Pfadstelle ist laut Namensraumkonvention eine Version. **Offen:** welches Release bzw. welche Schemafassung dahintersteht. | ALISE-XSD, KA XML-Schemata (Inv. 5) |
| **O5** | Erhöht ein reiner Statuswechsel die `berSynchronNummer`? | KA BOM-SPEC (Inv. 1), KA AktM-SPEC (Inv. 41) |
| **O6** | In einem vorliegenden produktspezifischen Teil gibt die TLV-Länge 87 Byte an, es folgen 90 Byte. Füllbytes, Übertragungsfehler oder falsche TLV-Annahme? | Anlage TLV EFS (Inv. 2) |
| **O9** | Verhältnis der Begriffe „Aktion“, „Aktionstyp“ und „Auftragstyp“ — synonym oder zwei Ebenen? | KA AktM-SPEC (Inv. 41) |
| **O13** | Welchen Wert trägt `amAenderungsreferenz_ID` bei einer tatsächlichen Änderung, und nimmt es Berechtigungsnummer samt Organisation des Vorgängers auf? | KA AktM-SPEC (Inv. 41), Beispielnachrichten |
| **O14** | Wie verhält sich `txalisber` zu `TXAML`? | ALISE-Schnittstellenbeschreibung, KA AktM-SPEC (Inv. 41) |

Drei der ursprünglich zwölf Fragen (O7, O8, O12) sind inzwischen aus öffentlichen Quellen geklärt, siehe [PLAN.md](PLAN.md), Abschnitt 5a.

**Zusammengefasst:** Die **KA AktM-SPEC** allein würde von den verbleibenden Fragen die Mehrzahl klären, zusammen mit **KA BOM-SPEC** und den **XML-Schemata** nahezu alle.

---

## 9a. Verwendung im Lexikon

Dieser Abschnitt wird von `tools/gen.py` aus den Artikeln erzeugt und ist **nicht von Hand zu pflegen**. Er zeigt, welcher Artikel welches nicht öffentliche Dokument als Normquelle nennt — damit auf der Gegenseite nachvollziehbar ist, dass die Anfrage aus konkretem Bedarf entsteht und nicht pauschal gestellt wird.

<!-- GEN:verwendung -->
**15 nicht öffentliche Dokumente** werden derzeit in 90 Artikeln als Normquelle genannt, nach Häufigkeit:

| Nennungen | Inv.-Nr. | Dokument | genannt in |
|---:|---:|---|---|
| 29 | 41 | **KA AktM-SPEC** | [Aktionsdifferenzliste](lexikon/aktionsmanagement/aktionsdifferenzliste.md), [Aktionsfreigabe](lexikon/aktionsmanagement/aktionsfreigabe.md), [Aktionsliste](lexikon/aktionsmanagement/aktionsliste.md), [Aktionsmanagement](lexikon/aktionsmanagement.md), [Änderungsreferenz](lexikon/aktionsmanagement/aenderungsreferenz.md), [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md), [Ausgabe EFS über Aktionsliste](lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md), [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md), [Terminalaktionsliste](lexikon/aktionsmanagement/terminalaktionsliste.md), [TXABER](lexikon/transaktionen/txaber.md), [TXAML](lexikon/transaktionen/txaml.md), [TXRBER](lexikon/transaktionen/txrber.md), [TXSNAWB](lexikon/transaktionen/txsnawb.md) |
| 28 | 4 | **KA SST-SPEC** | [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md), [Kontrollnachweise](lexikon/kontrolle/kontrollnachweise.md), [Rollen](lexikon/rollen.md), [Sperrliste](lexikon/kontrolle/sperrliste.md), [Transaktionen](lexikon/transaktionen.md), [TX_BASE](lexikon/transaktionen/tx-base.md), [TXABER](lexikon/transaktionen/txaber.md), [TXAML](lexikon/transaktionen/txaml.md), [TXEBER](lexikon/transaktionen/txeber.md), [TXRBER](lexikon/transaktionen/txrber.md), [TXSNAWB](lexikon/transaktionen/txsnawb.md) |
| 12 | 1 | **KA BOM-SPEC** | [Basisobjektmodell](lexikon/datenformate/bom.md), [berStatus](lexikon/berechtigungen/berstatus.md), [Datenformate](lexikon/datenformate.md), [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md), [Kürzungsregel für Namen](lexikon/datenformate/kuerzungsregel-fuer-namen.md), [logTransaktionsTyp](lexikon/transaktionen/logtransaktionstyp.md), [Rollencodes](lexikon/rollen/rollencodes.md), [Sperrgrund](lexikon/kontrolle/sperrgrund.md) |
| 11 | 2 | **Anlage TLV EFS** | [Datenformate](lexikon/datenformate.md), [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md), [Produktspezifischer Teil](lexikon/berechtigungen/produktspezifischer-teil.md), [Tag 0xDB Fahrgast](lexikon/datenformate/tag-0xdb-fahrgast.md), [TLV-Kodierung](lexikon/datenformate/tlv.md) |
| 10 | 5 | **KA XML-Schemata und WSDL** | [Datenformate](lexikon/datenformate.md), [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md), [Transaktionen](lexikon/transaktionen.md), [TX_BASE](lexikon/transaktionen/tx-base.md), [XSD und WSDL](lexikon/datenformate/xsd.md) |
| 6 | 42 | **KA STB-Spec** | [Datenformate](lexikon/datenformate.md), [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md), [Statische Berechtigung](lexikon/berechtigungen/statische-berechtigung.md), [VDV-Barcode](lexikon/datenformate/vdv-barcode.md) |
| 5 | 7 | **KA NM-SPEC** | [Applikation](lexikon/medien/applikation.md), [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md), [Nutzermedium](lexikon/medien/nutzermedium.md) |
| 3 | 40 | **KA MultiBER-SPEC** | [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md), [Multiberechtigung](lexikon/berechtigungen/multiberechtigung.md) |
| 2 | 12–21 | **KA SysLH** | [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md) |
| 2 | 35 | **KA PROD_ID-ANW** | [Produktnummer](lexikon/berechtigungen/produktnummer.md) |
| 2 | 9 | **KA ION-SPEC** | [Interoperabilität](lexikon/grundlagen/interoperabilitaet.md), [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md) |
| 1 | 11 | **KA KOSES-Spec** | [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md) |
| 1 | 33 | **KA TXx-Prüfungs-ANW** | [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md) |
| 1 | 6 | **KA SEC-SPEC** | [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md) |
| 1 | 8 | **KA SAM-SPEC** | [KA-Spezifikationen](lexikon/grundlagen/ka-spezifikationen.md) |

### Artikel, die ohne diese Dokumente unvollständig bleiben

| Artikel | offene Fragen |
|---|---|
| [Änderungsreferenz](lexikon/aktionsmanagement/aenderungsreferenz.md) | O13 |
| [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md) | O2, O9 |
| [txalisber](lexikon/transaktionen/txalisber.md) | O4, O14 |

### Offene Fragen und die betroffenen Artikel

| Frage | betrifft |
|---|---|
| **O1** | [Ausgabe EFS über Aktionsliste](lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md), [Entsperrung über Aktionsliste](lexikon/aktionsmanagement/entsperrung-ueber-aktionsliste.md), [logTransaktionsTyp](lexikon/transaktionen/logtransaktionstyp.md), [Rücknahme EFS über Aktionsliste](lexikon/aktionsmanagement/ruecknahme-efs-ueber-aktionsliste.md), [Transaktionen](lexikon/transaktionen.md), [TXABER](lexikon/transaktionen/txaber.md), [TXRBER](lexikon/transaktionen/txrber.md), [TXSNAWB](lexikon/transaktionen/txsnawb.md) |
| **O2** | [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md), [Ausgabe EFS über Aktionsliste](lexikon/aktionsmanagement/ausgabe-efs-ueber-aktionsliste.md) |
| **O3** | [berStatus](lexikon/berechtigungen/berstatus.md), [Rücknahme EFS über Aktionsliste](lexikon/aktionsmanagement/ruecknahme-efs-ueber-aktionsliste.md) |
| **O4** | [txalisber](lexikon/transaktionen/txalisber.md), [Versionen](lexikon/grundlagen/versionen.md), [XML-Namensraum](lexikon/datenformate/xml-namensraum.md) |
| **O5** | [berSynchronNummer](lexikon/berechtigungen/bersynchronnummer.md) |
| **O6** | [Produktspezifischer Teil](lexikon/berechtigungen/produktspezifischer-teil.md), [TLV-Kodierung](lexikon/datenformate/tlv.md) |
| **O9** | [Aktion](lexikon/aktionsmanagement/aktion.md), [Aktionsmanagement](lexikon/aktionsmanagement.md), [Auftragstyp](lexikon/aktionsmanagement/auftragstyp.md) |
| **O13** | [Änderungsreferenz](lexikon/aktionsmanagement/aenderungsreferenz.md) |
| **O14** | [txalisber](lexikon/transaktionen/txalisber.md) |

*Erzeugt aus 90 Artikeln. Die Links führen in das Lexikon.*
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
> Zur **Version**: Ein Zulassungs-Prüfbericht für ein Akzeptanzterminal von 2024 führt zwölf KA-Spezifikationen einschließlich XML-Schemata und WSDL durchgehend in **Version 1.12.0** auf. Diese Fassung wäre mir am wichtigsten. Daneben benötige ich **1.1.07** und **1.3.0**, weil die öffentlichen Projektdokumente ausdrücklich zwischen beiden unterscheiden, sowie die Auskunft, welches Release heute verbindlich unterstützt wird.
>
> Zu ALISE kann ich die Bitte dank der Namenskonvention im eTicket-Regelwerk (Kapitel 4.3.2 f.) genauer fassen: Dort erscheinen die WSDL-Bereiche `PV_ALISE` und `KVP_ALISE` sowie die Namensraum-Bereiche `pv-alise` und `kvp-alise`. Ich bräuchte die WSDL beider Bereiche und die zugehörigen XSD mit allen Includes und Imports — und die Auskunft, welcher Version im Sinne dieser Konvention die Angabe `http://vdv/ka/alise/2` entspricht.
>
> Weiter wären hilfreich: Codelisten in maschinenlesbarer Form und Beispielnachrichten je Nachrichtentyp.
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
