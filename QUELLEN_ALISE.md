# VDV-KA / ALISE – Dokumentation, Nachrichtenformate und Entwicklung eines grafischen Analysewerkzeugs

Für dein Vorhaben würde ich eine **technische Wissensbasis zur VDV-Kernapplikation (VDV-KA), insbesondere zu ALISE und dem Aktionsmanagement**, aufbauen.

Dein Ziel lässt sich in zwei Bereiche aufteilen:

**1. VDV-KA-Nachrichten verstehen und interpretieren**

Du möchtest XML-Nachrichten wie die aus deiner LVB-Bewerberaufgabe lesen und verstehen können. Dazu gehören die Bedeutung einzelner XML-Elemente, Transaktionstypen, Statuscodes, Organisationskennungen und die Zusammenhänge zwischen den Nachrichten.

**2. Später ein grafisches Analysewerkzeug entwickeln**

Das Werkzeug soll idealerweise eine VDV-KA-Nachricht einlesen, ihre Struktur erkennen und die enthaltenen Informationen verständlich darstellen.

Dafür brauchen wir nicht nur allgemeine Beschreibungen der VDV-KA, sondern vor allem die **technischen Schnittstellenspezifikationen, XML-Schemas (XSD), Codelisten und Beschreibungen der Transaktionsabläufe**.

Ein besonders wichtiger Hinweis: ALISE ist nicht mit der gesamten VDV-Kernapplikation gleichzusetzen. Es handelt sich um einen speziellen Teilbereich. Ein vollständiger Nachrichtenanalysator müsste später auch andere KA-Nachrichtentypen unterstützen.

## 1. Die wichtigsten gefundenen Dokumentationsquellen

Bei der Recherche habe ich eine besonders wichtige Entdeckung gemacht: In einem öffentlich zugänglichen eTicket-Regelwerk gibt es ein eigenes Kapitel **„VDV-KA-Dokumentation“**, das die offiziellen Spezifikationen einzeln auflistet.

Damit haben wir eine gute Grundlage, um die benötigten Dokumente systematisch zusammenzutragen.

### Quelle A: Offizielles Verzeichnis der VDV-KA-Spezifikationen

**Dokument:** eTicket-Regelwerk, Version 1.27, Stand 16.05.2018

[PDF – eTicket-Regelwerk mit Dokumentationsverzeichnis](https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_27a_EFM_Teilnvertrag____eTicketDeutschl_mAnl_Muster_Stand_170801_MVU.pdf)

Das PDF umfasst 273 Seiten. Kapitel 3 enthält das Verzeichnis der technischen KA-Dokumentation. Es ist besonders wertvoll, weil dort auch die genauen Bezeichnungen der benötigten Spezifikationen aufgeführt werden. [mtv-unternehmen.de](https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_27a_EFM_Teilnvertrag____eTicketDeutschl_mAnl_Muster_Stand_170801_MVU.pdf?utm_source=chatgpt.com)

Für dein Vorhaben sind insbesondere diese Dokumenttypen relevant:

| Dokument | Inhalt | Wichtigkeit |
|---|---|---|
| KA BOM-SPEC | Basisobjektmodell, Datentypen und grundlegende Strukturen | Sehr hoch |
| KA SST-SPEC | Schnittstellen zwischen KA-Referenzsystemen | Sehr hoch |
| KA XML-Schemata | XSD-Dateien für Transaktionsnachrichten | Sehr hoch |
| KA AktM-SPEC | Aktionsmanagement und Aktionslisten | Sehr hoch |
| KA Glossar | Begriffe, Abkürzungen und Rollen | Hoch |
| KA TXx-Prüfungs-ANW | Prüfung von Transaktionen | Hoch |
| KA SysLH | Systemlastenhefte | Mittel |

Die Dokumenttitel und die Existenz der XML-Schemata werden durch das Regelwerk bestätigt. Das bedeutet allerdings nicht, dass alle Dokumente ohne Registrierung öffentlich heruntergeladen werden können. [VergabeHero](https://vergabehero.eu/ausschreibungen/oeffentliche-busverkehrsleistungen-auf-den-linien-mr-61-bis-mr-65--cmti9ia4t008v14arrzwe203i/unterlagen/cmun1rorg2s3a8im7jxfd5niy?utm_source=chatgpt.com)

### Quelle B: Offizieller Zugang zu den technischen Spezifikationen

**VDV eTicket Service – Support und ASM-Tool**

https://www.eticket-deutschland.de/support

Der VDV eTicket Service erklärt ausdrücklich, dass über das ASM-Tool Spezifikationen und aktuelle VDV-KA-Releases bereitgestellt werden.

Das ist der wichtigste offizielle Zugang, wenn du die vollständige Dokumentation benötigst. [eTicket Deutschland](https://www.eticket-deutschland.de/support?utm_source=chatgpt.com)

Für eine Anfrage kannst du folgende E-Mail-Adresse verwenden:

**service@eticket-deutschland.de**

Ich würde gezielt nach folgenden Dateien fragen:

- VDV-KA Aktionsmanagement-Spezifikation (KA AktM-SPEC)
- ALISE-Schnittstellenbeschreibung
- ALISE-XML-Schemata einschließlich XSD-Abhängigkeiten
- KA-Schnittstellenspezifikation (SST-SPEC)
- Basisobjektmodell (BOM-SPEC)
- Codelisten und Enumerationen
- Dokumentation der logischen Transaktionstypen
- Beispielnachrichten und Testdaten

Frage ausdrücklich nach den Versionen **1.3.0 und 1.5.0** sowie nach dem aktuell unterstützten Release. Für die LVB-Beispielnachricht mit dem Namespace `http://vdv/ka/alise/2` ist die tatsächlich zugehörige Schema- und Spezifikationsversion entscheidend.

### Quelle C: RMV-Terminalmanagement – besonders relevant für ALISE

**Dokument:** PH06-02 – Terminalmanagementsysteme, Version 2.3 vom 09.11.2018

[RMV-Terminalmanagement-Pflichtenheft (PDF)](https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_24_EFM_Anh_2_vHGS_PH06-02_TeminalMgmtSys_v2.3_181109_MVU_211020.pdf)

Dieses Dokument enthält einen besonders wichtigen Abschnitt:

**Kapitel 4.3 – Aktionsliste und Transaktionsnachweise**

Darin werden ausdrücklich folgende Nachrichtentypen genannt:

| Nachricht | Bedeutung bzw. Einordnung |
|---|---|
| `TXAML` | Aktionsliste |
| `TXABER` | Transaktionsnachweis im Zusammenhang mit einer Aktionsausführung |
| `TXRBER` | Transaktionsnachweis im Zusammenhang mit einer Aktionsausführung |
| `TXSNAWB` | Weiterer im Aktionskontext genannter Transaktionsnachweis |

Das Pflichtenheft verweist für `TXAML` ausdrücklich auf die Spezifikation `KA_SPEC_AktM`.

Für die Transaktionsnachweise verweist es zusätzlich auf die Schnittstellenspezifikationen `KA_SPEC_SST_1107` beziehungsweise `KA_SPEC_SST_1300` und die entsprechenden Aktionsmanagement-Spezifikationen. [Main-Taunus-Verkehrsgesellschaft](https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_24_EFM_Anh_2_vHGS_PH06-02_TeminalMgmtSys_v2.3_181109_MVU_211020.pdf?utm_source=chatgpt.com)

**Das ist für dein späteres Tool entscheidend:** Du kannst aus diesen Verweisen ableiten, welche offiziellen Spezifikationen zusammen benötigt werden, um einen Transaktionsnachweis korrekt zu interpretieren.

### Quelle D: Technische Dokumente des Kompetenzcenters Digitalisierung NRW

https://www.kcd-nrw.de/service/downloads/technische-dokumente.html

Das Kompetenzcenter Digitalisierung NRW stellt technische Informationen zum elektronischen Ticketing bereit.

Dort wird die VDV-Kernapplikation als offener Daten- und Schnittstellenstandard beschrieben. Außerdem wird zwischen den allgemeinen KA-Spezifikationen und ergänzenden Dokumenten für einzelne Tarife unterschieden. [Kompetenzcenter Digitalisierung NRW](https://www.kcd-nrw.de/service/downloads/technische-dokumente.html?utm_source=chatgpt.com)

Das ist besonders relevant, wenn dein Tool später nicht nur technische Felder, sondern auch tarifliche Informationen interpretieren soll.

### Quelle E: VDV-KA-Releases und Versionsunterschiede

[VDV-KA Release 1.5.0 – Informationen](https://www.itcs-info.de/index.php/news/145-e-ticket/490-vdv-ka-release-1-5-0-veroeffentlicht)

Der Bericht beschreibt Änderungen der Version 1.5.0, unter anderem beim Aktionsmanagement und bei der Verarbeitung von Berechtigungen.

Das zeigt, weshalb ein Analysewerkzeug verschiedene KA-Versionen berücksichtigen sollte. [itcs-info](https://www.itcs-info.de/index.php/news/145-e-ticket/490-vdv-ka-release-1-5-0-veroeffentlicht?utm_source=chatgpt.com)

Außerdem kündigt der VDV eTicket Service für 2026 die Einführung von **(((etiCORE als VDV-KA-Version 3** an. Nach den veröffentlichten Angaben soll diese neue Generation bis 2031 parallel zur bisherigen VDV-KA betrieben werden. [eTicket Deutschland](https://www.eticket-deutschland.de/loesungen?utm_source=chatgpt.com)

Für ein langfristiges Softwareprojekt würde ich deshalb die Nachrichtenverarbeitung von Anfang an versionsabhängig gestalten.

---

## 2. Was wir über ALISE und das Aktionsmanagement bereits belegen können

Ein besonders hilfreicher Fund befindet sich im bereits verlinkten eTicket-Regelwerk.

Dort werden konkrete Anwendungsfälle des Aktionsmanagements beschrieben.

### 2.1 Welche Aktionen gibt es?

Die Dokumentation nennt unter anderem:

| Aktion | Bedeutung |
|---|---|
| EFS-Berechtigung ausgeben | Eine elektronische Fahrberechtigung ausgeben |
| EFS-Berechtigung zurücknehmen | Eine vorhandene Berechtigung zurücknehmen |
| Berechtigung entsperren | Eine zuvor gesperrte Berechtigung entsperren |
| Aktionsliste bereitstellen | Aufträge für die spätere Verarbeitung bereitstellen |
| Aktionsdifferenzliste bereitstellen | Änderungen an Aktionslisten übertragen |
| Aktionsfreigabe senden | Eine Aktion zur weiteren Verarbeitung freigeben |
| Entsperrnachweis bearbeiten | Die Durchführung einer Entsperrung verarbeiten |
| Aktionsclearing bearbeiten | Ergebnisse zwischen beteiligten Systemen verarbeiten |

Diese Anwendungsfälle sind im eTicket-Regelwerk ausdrücklich dokumentiert. [Main-Taunus-Verkehrsgesellschaft](https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_27a_EFM_Teilnvertrag____eTicketDeutschl_mAnl_Muster_Stand_170801_MVU.pdf?utm_source=chatgpt.com)

Eine wichtige Erkenntnis ist, dass das Aktionsmanagement verschiedene Systemrollen umfasst:

**Produktverantwortlicher (PV):** Stellt Produktinformationen bereit und übernimmt im Aktionsmanagement bestimmte Steuerungsaufgaben.

**Kundenvertragspartner (KVP):** Verwaltet die Kundenbeziehung und die zugehörigen Berechtigungen.

**Terminal:** Führt vorgesehene Aktionen am Nutzermedium aus.

Die tatsächliche Verteilung der Aufgaben richtet sich nach den spezifizierten Prozessen.

### 2.2 Beispiel für einen Aktionsablauf

Vereinfacht könnte die Ausgabe eines elektronischen Fahrscheins so aussehen:

```text
┌──────────────────────────┐
│ Produktverantwortlicher  │
│           PV             │
└────────────┬─────────────┘
             │
             │ Aktionsauftrag
             ▼
┌──────────────────────────┐
│    Aktionsmanagement     │
│                          │
│   Bereitstellung einer   │
│       Aktionsliste       │
└────────────┬─────────────┘
             │
             │ Aktionsliste
             ▼
┌──────────────────────────┐
│       KVP-System         │
│                          │
│  Verarbeitung und        │
│  Weitergabe der Aktion   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        Terminal          │
│                          │
│  Ausgabe des Tickets     │
│  auf dem Nutzermedium    │
└────────────┬─────────────┘
             │
             │ Transaktionsnachweis
             ▼
┌──────────────────────────┐
│       Backend            │
│                          │
│  Verarbeitung des        │
│  Transaktionsergebnisses │
└──────────────────────────┘
```

Das ist eine vereinfachte Darstellung zur Veranschaulichung, kein vollständiges normatives Sequenzdiagramm.

Die offizielle Dokumentation beschreibt Ausgabe, Rücknahme und Entsperrung über Aktionslisten als mögliche Verfahren. [Main-Taunus-Verkehrsgesellschaft](https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_27a_EFM_Teilnvertrag____eTicketDeutschl_mAnl_Muster_Stand_170801_MVU.pdf?utm_source=chatgpt.com)

---

## 3. Die XML-Nachricht aus deiner LVB-Bewerberaufgabe verstehen

Deine Beispielnachricht beginnt mit:

```xml
<ns:txalisber xmlns:ns="http://vdv/ka/alise/2">
```

Hier sind zwei Informationen wichtig.

**`txalisber`** bezeichnet das XML-Element der Nachricht.

**`http://vdv/ka/alise/2`** ist der XML-Namespace. Er ermöglicht die eindeutige Zuordnung der XML-Elemente zu einem bestimmten Namensraum.

Die abschließende `2` ist Bestandteil dieses Namespace-Namens. Daraus allein lässt sich nicht zuverlässig auf eine bestimmte VDV-KA-Releaseversion schließen.

Für die exakte Interpretation benötigen wir die zugehörige XSD-Datei und die fachliche ALISE-Spezifikation.

### 3.1 Welche Informationen sollte dein Tool erkennen?

Nehmen wir einen Ausschnitt deiner Nachricht:

```xml
<ns:amAuftragsTyp>13</ns:amAuftragsTyp>

<ns:logTransaktionsTyp>37</ns:logTransaktionsTyp>

<ns:berInfoText>ABO Azubi</ns:berInfoText>
```

Ein grafisches Werkzeug könnte diese Werte folgendermaßen darstellen:

| XML-Feld | Rohwert | Fachliche Interpretation |
|---|---|---|
| `amAuftragsTyp` | 13 | Aktionsauftragstyp; genaue Codelistenzuordnung erforderlich |
| `logTransaktionsTyp` | 37 | Hinweis auf Ausgabe EFS über Aktionsliste |
| `berInfoText` | ABO Azubi | Informationstext zur Berechtigung |

Besonders wichtig wäre eine vierte Spalte: **Quelle beziehungsweise Sicherheit der Interpretation**.

Damit könnte dein Tool zwischen drei Fällen unterscheiden:

- **Bestätigt:** Bedeutung durch die passende Spezifikation belegt.
- **Abgeleitet:** Interpretation anhand des Nachrichtenkontexts.
- **Unbekannt:** Bedeutung ohne zusätzliche Dokumentation nicht bestimmbar.

Das würde verhindern, dass beispielsweise eine unbekannte Statusnummer versehentlich falsch interpretiert wird.

---

# 4. Mein Vorschlag für dein grafisches VDV-KA-Analysewerkzeug

Ich würde die Anwendung zunächst als **lokalen VDV-KA XML Explorer** entwickeln.

Der erste Schwerpunkt sollte ALISE sein. Später könnten weitere VDV-KA-Nachrichtenformate ergänzt werden.

## 4.1 Geplante Funktionen

| Funktion | Beschreibung | Priorität |
|---|---|---|
| XML-Dateien öffnen | Einzelne VDV-KA-Nachrichten laden | 1 |
| XML-Struktur anzeigen | Baumansicht aller XML-Elemente | 1 |
| Nachrichten erkennen | Identifikation anhand von Element und Namespace | 1 |
| Feldbeschreibungen | Technische und fachliche Bedeutung anzeigen | 1 |
| Codelisten | Numerische Werte verständlich auflösen | 1 |
| XSD-Validierung | Nachrichten gegen das passende Schema prüfen | 1 |
| Organisationskennungen | Organisationen anhand eines Verzeichnisses zuordnen | 2 |
| Hex-Daten analysieren | Binäre Datenstrukturen untersuchen | 2 |
| Nachrichten vergleichen | Unterschiede zwischen zwei Transaktionen erkennen | 2 |
| Transaktionsabläufe | Mehrere Nachrichten als Prozess darstellen | 3 |
| Export | Analyse als Markdown, JSON oder PDF speichern | 3 |

## 4.2 Beispiel für die grafische Oberfläche

```text
┌─────────────────────────────────────────────────────────────┐
│ VDV-KA XML Explorer                                         │
├─────────────────────────────────────────────────────────────┤
│ Datei öffnen   XSD laden   Validieren   Exportieren         │
├───────────────────────┬─────────────────────────────────────┤
│ XML-Struktur          │ Fachliche Interpretation            │
│                       │                                     │
│ ▼ txalisber           │ Nachricht: ALISE                    │
│   ├ amAuftragsTyp     │                                     │
│   ├ logTransaktionsTyp│ Transaktionstyp: 37                 │
│   ├ berInfoText       │ EFS-Ausgabe über Aktionsliste       │
│   ├ tx_ber            │                                     │
│   │ ├ Gueltigkeits... │ Produkt: ABO Azubi                  │
│   │ └ BezahlArt       │                                     │
│   ├ tx_identam        │ Berechtigung: 400815                │
│   │ ├ appInstanz_ID   │                                     │
│   │ ├ berStatus       │ Status: 7                           │
│   │ └ prodProdukt_ID  │                                     │
│   └ berProduktspezTeil│                                     │
├───────────────────────┴─────────────────────────────────────┤
│ Feldinformationen                                           │
│                                                             │
│ XML: logTransaktionsTyp                                     │
│ Wert: 37                                                    │
│ Bedeutung: Ausgabe EFS über Aktionsliste                    │
│ Quelle: RMV PH06-02 / KA-Spezifikation                       │
└─────────────────────────────────────────────────────────────┘
```

Das ist ein erster Entwurf der Oberfläche, keine bereits implementierte Anwendung.

## 4.3 Empfohlene technische Architektur

Für einen ersten Prototyp würde ich Python verwenden.

| Komponente | Technologie | Aufgabe |
|---|---|---|
| Benutzeroberfläche | PySide6 | Grafische Desktopanwendung |
| XML-Verarbeitung | lxml | XML einlesen und auswerten |
| Schema-Validierung | lxml / XMLSchema | XSD-Prüfung |
| Felddefinitionen | JSON oder YAML | Beschreibungen und Zuordnungen |
| Lokale Datenbank | SQLite | Codelisten, Organisationen und Versionen |
| Diagramme | Qt Graphics View | Darstellung von Transaktionsabläufen |

**Warum diese Architektur?**

Die eigentliche Interpretation sollte von der Benutzeroberfläche getrennt sein.

So könntest du später dieselbe Auswertungslogik in einer Desktopanwendung, einer Webanwendung oder einer automatisierten Prüfsoftware verwenden.

Außerdem sollten alle Codelisten und Feldbeschreibungen versionsabhängig gespeichert werden.

Beispielsweise:

```json
{
  "namespace": "http://vdv/ka/alise/2",
  "message_type": "txalisber",
  "fields": {
    "logTransaktionsTyp": {
      "description": "Logischer Transaktionstyp",
      "values": {
        "37": {
          "meaning": "Ausgabe EFS über Aktionsliste",
          "verification": "secondary_source"
        }
      }
    },
    "amAuftragsTyp": {
      "description": "Typ des Aktionsauftrags",
      "values": {}
    }
  }
}
```

Dies ist ein **vorgeschlagenes internes Datenformat**, kein offizielles VDV-KA-Schema.

---

# 5. Was für einen vollständigen ALISE-Decoder noch fehlt

Die Recherche hat einige wichtige Quellen geliefert. Die entscheidenden Originaldateien konnte ich bislang jedoch nicht vollständig als öffentlich zugängliche Downloads nachweisen.

| Benötigte Unterlage | Status | Zweck |
|---|---|---|
| VDV-KA-Regelwerk | Gefunden | Allgemeine Grundlagen und Dokumentationsverzeichnis |
| RMV PH06-02 | Gefunden | Technische Hinweise zu Aktionslisten und Transaktionen |
| KA AktM-SPEC | Existenz bestätigt, Originaldatei noch nicht gefunden | Aktionsmanagement |
| ALISE-XSD | Noch nicht gefunden | Strukturvalidierung und Datentypen |
| KA BOM-SPEC | Existenz bestätigt, Originaldatei noch nicht gefunden | Basisdatentypen |
| KA SST-SPEC | Existenz bestätigt, Originaldatei noch nicht gefunden | Schnittstellen und Transaktionen |
| Vollständige Codelisten | Noch nicht gefunden | Interpretation numerischer Werte |
| ALISE-Beispielnachrichten | Bisher nur deine LVB-Beispielnachricht | Testdaten |

Die **KA AktM-SPEC** ist besonders wichtig. Im offiziellen Dokumentationsverzeichnis wird sie unter der Inventarnummer 41 als „Aktionsmanagement für die Berechtigungsart EFS“ aufgeführt. [mtv-unternehmen.de](https://mtv-unternehmen.de/fileadmin/user_upload/E_Anlage_27a_EFM_Teilnvertrag____eTicketDeutschl_mAnl_Muster_Stand_170801_MVU.pdf?utm_source=chatgpt.com)

Ohne diese Spezifikation und die zugehörigen XML-Schemas könnten wir zwar einen XML-Viewer bauen, aber noch keinen vollständig spezifikationskonformen ALISE-Decoder.

---

## 6. Wie ich weiter vorgehen würde

Ich empfehle drei aufeinander aufbauende Entwicklungsphasen.

**Phase 1 – Dokumentation und Verständnis**

Zunächst sollten wir die originalen ALISE-Spezifikationen und XSD-Dateien beschaffen. Anschließend erstellen wir ein Nachschlagewerk für sämtliche relevanten XML-Elemente, Datentypen, Codelisten und Nachrichtentypen.

**Phase 2 – XML-Decoder**

Danach entwickeln wir einen Parser, der ALISE-Nachrichten automatisch erkennt, validiert und in ein verständliches internes Datenmodell überführt. Für unbekannte Felder zeigt er den Rohwert und einen entsprechenden Hinweis an.

**Phase 3 – Grafische Anwendung**

Auf dieser Grundlage entwickeln wir eine Oberfläche mit XML-Baumansicht, fachlicher Interpretation, Suchfunktion, Validierung und später einer grafischen Darstellung zusammengehöriger Transaktionen.

Für die Entwicklung sollten wir ausschließlich Testdaten oder ausreichend anonymisierte Echtdaten verwenden. Bei realen EFM-Nachrichten können insbesondere Kunden-, Berechtigungs- und Bewegungsdaten schutzbedürftig sein.

---

## 7. Eine wichtige Frage zur weiteren Recherche

**Hast du über die LVB, deinen Arbeitgeber oder einen anderen Verkehrsverbund Zugang zum VDV eTicket Service beziehungsweise zum ASM-Tool?**

Das wäre für unser Vorhaben besonders hilfreich. Dort werden nach Angaben des VDV eTicket Service die offiziellen Spezifikationen und Releases bereitgestellt.

Wenn du keinen Zugang hast, können wir zunächst mit den öffentlich verfügbaren Unterlagen arbeiten und beim VDV eTicket Service gezielt die ALISE-XSD-Dateien sowie die Aktionsmanagement-Spezifikation anfragen.

**Mein Vorschlag:** Wir konzentrieren uns zuerst auf die vollständige Dokumentation von `txalisber`, `TXAML`, `TXABER` und den zugehörigen Datenstrukturen. Damit hätten wir eine fachlich sinnvolle Grundlage für einen ersten funktionsfähigen ALISE-Explorer.