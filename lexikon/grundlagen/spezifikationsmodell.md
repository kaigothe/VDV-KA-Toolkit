---
titel: Spezifikationsmodell
englisch: specification model
parent: lexikon/grundlagen.md
siehe_auch: [lexikon/grundlagen/eticore.md, lexikon/grundlagen/ka-spezifikationen.md]
quellen: [Q43, Q49]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Grundlagen](../grundlagen.md) › Spezifikationsmodell
<!-- /GEN:breadcrumb -->

# Spezifikationsmodell

Das Spezifikationsmodell ist die **maßgebliche Quelle der [etiCORE](eticore.md)-Spezifikation**; die Spezifikationsdokumente sind Exporte daraus ([Q43](../../QUELLEN.md#q43), Kap. 2.1, PDF-S. 23). Es liegt als Browser-Version online und zusätzlich als lokal installierbares Paket vor ([Q43](../../QUELLEN.md#q43), Kap. 2.1, PDF-S. 23; Kap. 1.1.6, PDF-S. 7).

**Es ist öffentlich erreichbar** ([Q43](../../QUELLEN.md#q43), Kap. 5.1, PDF-S. 30): die jeweils letzte Fassung unter `modell.eticket-deutschland.de/LATEST/EA/index.html`, daneben versionierte Einstiege. Damit ist es die **einzige frei zugängliche Vollspezifikation** im Umfeld dieses Lexikons (abgeleitet) — siehe [Q49](../../QUELLEN.md#q49).

**Gliederung** ([Q49](../../QUELLEN.md#q49)): Introduction, Role Model, Layer 1 und 2 mit Workflows und Basic Processes in BPMN, Layer 3 mit Use Cases, Layer 4 mit System Components and Interfaces, Layer 5 mit Implementation Details, ION Specification, allgemeine Terminalanteile, EUI/MPI/ESI, SAM-Server, User Manual, Types, Interfaces, Glossary, Operational parameters, List of References.

**Die Schnittstellen sind gesondert dokumentiert** ([Q43](../../QUELLEN.md#q43), Kap. 5.2, PDF-S. 30 ff.):

| Gegenstand | Einstieg |
|---|---|
| ASN.1-Datentypen | `…/LATEST/index-asn1.html` |
| WSDL und XSD | `…/LATEST/index-interfaces.html` |
| SAM-Server | je Gegenstelle, als OpenAPI über REST/JSON |

Die ASN.1-Module sind nach Gegenstand getrennt: `common`, `et`, `cv-certificates`, `payment`, `motics`, `ste`, `sam`, `tariff`, `user-medium` ([Q43](../../QUELLEN.md#q43), PDF-S. 31 f.).

**Beispieldaten** für Transaktionsnachweise, Kontrolle, Sperren, Signaturen statischer Berechtigungen und den SOAP-Austausch im ION sind vorhanden, aber **nicht Bestandteil des Spezifikationspakets** ([Q43](../../QUELLEN.md#q43), Kap. 7.2, PDF-S. 36).

**Vorbehalt:** Das Modell beschreibt etiCORE, also KA 3. Aussagen daraus gelten **nicht ohne Prüfung** für KA 1.x.

## Einfach erklärt – Beispiel aus Bärstadt

Stellen wir uns vor, der Hersteller des BVB-Systems bekommt den Auftrag, die Ausgabe von Pias ABO Azubi umzusetzen.

**Bisher** hätte er eine Reihe PDF-Dateien erhalten: ein Systemlastenheft, eine Schnittstellenspezifikation, ein Sicherheitskonzept. Darin hätte er sich die Stellen zusammengesucht, die seinen Fall betreffen — und die Verbindung zwischen ihnen selbst herstellen müssen.

**Jetzt** öffnet er eine Webseite und folgt einem Pfad: oben der Workflow „Berechtigung ausgeben“, darunter der Basisprozess, darunter der Anwendungsfall, darunter die beteiligten Systemkomponenten, darunter die konkrete Schnittstelle und der Datentyp. Fünf Schichten, miteinander verlinkt. Die PDF-Dokumente, die er weiterhin bekommt, sind Ausschnitte aus genau dieser Darstellung.

Der Unterschied ist nicht kosmetisch. Wenn in der Schicht der Datentypen ein Feld geändert wird, ändert sich das überall mit, wo dieses Feld vorkommt. Widersprüche zwischen zwei Dokumenten, wie sie bei Dokumentenstapeln unvermeidlich sind, werden dadurch unwahrscheinlicher.

**Und für uns hier ist etwas anderes wichtig.** Dieses Modell ist frei zugänglich. Fast alles, was dieses Lexikon über die VDV-KA 1.x sagt, musste aus öffentlichen Nebenquellen zusammengetragen werden: aus einem Glossar, aus Pflichtenheften von Verbünden, aus Prüfberichten. Die eigentlichen Spezifikationen sind nicht öffentlich.

Beim Nachfolger ist das anders. Wer wissen will, wie eine Kontrolle unter etiCORE abläuft, welche Felder eine Nachricht trägt oder wie ein Zertifikat aufgebaut ist, kann nachsehen.

**Ein Haken bleibt.** Das Modell beschreibt etiCORE und nicht die Welt, in der Pias BärenKarte heute lebt. Zwischen beiden liegen Namensänderungen und inhaltliche Änderungen. Wer eine Aussage aus dem Modell auf die KA 1.x überträgt, muss sie prüfen — sonst erklärt er den heutigen Bärstädter Betrieb mit den Regeln von morgen.

Dafür gibt es eine Hilfe: Zum Release gehören Gegenüberstellungen der alten und neuen Begriffe, getrennt für Spezifikationen, Binärdaten und XML-Schnittstellen. Sie sind allerdings nicht Teil des frei zugänglichen Modells.

## Quellen

- [Q43](../../QUELLEN.md#q43) – etiCORE Release Letter 3.0.0-rc.6: Kap. 1.1.6, PDF-S. 7 (lokale Installation des Modells), Kap. 2.1, PDF-S. 23 (Modell als Quelle, Dokumente als Export; Online- und lokale Variante), Kap. 5.1, PDF-S. 30 (öffentliche Adresse, auch von den Lastenheften verwendet), Kap. 5.2.1 bis 5.2.3, PDF-S. 30 ff. (ASN.1-Einstieg, WSDL/XSD-Einstieg, SAM-Server als OpenAPI über REST/JSON), PDF-S. 31 f. (ASN.1-Module), Kap. 7.1, PDF-S. 35 (Gegenüberstellungen alter und neuer Begriffe), Kap. 7.2, PDF-S. 36 (Beispieldaten, nicht Bestandteil des Spezifikationspakets)
- [Q49](../../QUELLEN.md#q49) – etiCORE Specification, Spezifikationsmodell online (oberste Gliederungsebene mit 18 Paketen) · *nur Struktur geprüft, Inhalte offen*

<!-- GEN:siehe_auch -->
## Siehe auch

- [etiCORE](eticore.md)
- [KA-Spezifikationen](ka-spezifikationen.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Grundlagen](../grundlagen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
