---
titel: KA-Spezifikationen
englisch: register of KA specifications
parent: lexikon/grundlagen.md
siehe_auch: [lexikon/grundlagen/versionen.md, lexikon/grundlagen/vdv-kernapplikation.md]
quellen: [Q02, Q25, Q26, Q37]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Grundlagen](../grundlagen.md) › KA-Spezifikationen
<!-- /GEN:breadcrumb -->

# KA-Spezifikationen

Die VDV-Kernapplikation ist ein **Dokumentenpaket**. Kapitel 3 des eTicket-Regelwerks verzeichnet es mit **Inventarnummern von 0 bis 59** ([Q25](../../QUELLEN.md#q25), Kap. 3, PDF-S. 34 ff.). Damit sind Existenz, Kurzzeichen und Nummer öffentlich belegt — die **Inhalte** nicht.

Die für dieses Lexikon wichtigsten Einträge:

| Inv. | Kurzzeichen | Gegenstand |
|---:|---|---|
| 0 | KA Glossar | Begriffe — öffentlich als [Q02](../../QUELLEN.md#q02) |
| 1 | KA BOM-SPEC | Hauptdokument mit Basisobjektmodell, Datentypen, **Codelisten** |
| 2 | Anlage TLV EFS | TLV-Struktur des EFS |
| 4 | KA SST-SPEC | Schnittstellen der Referenzsysteme, `TX*`-Nachrichten |
| 5 | KA XML-Schemata und WSDL | XSD und WSDL der TX-Transaktionen |
| 6 | KA SEC-SPEC | Technisches Konzept Sicherheit |
| 7 | KA NM-SPEC | Nutzermedium |
| 8 | KA SAM-SPEC | SAM |
| 9 | KA ION-SPEC | Datenaustausch im Interoperabilitätsnetzwerk |
| 11 | KA KOSES-Spec | Sperrlistenmanagementsystem |
| 12–21 | KA SysLH … | Systemlastenhefte für Systeme und Terminals |
| 33 | KA TXx-Prüfungs-ANW | Prüfung von Transaktionen |
| 40 | KA MultiBER-SPEC | Multiberechtigungen |
| **41** | **KA AktM-SPEC** | **Aktionsmanagement für die Berechtigungsart EFS** |
| 42 | KA STB-Spec | Statische Berechtigungen für 2D-Barcode-Tickets |
| 53–57 | KA PKM-… | Produkt-, Kontroll- und Tarifmodule |
| 59 | KA SAM-Server-SPEC | SAM-Server |

Zwei Einträge sind ausdrücklich **„entfallen ab Release 1.6.0“** (Inv. 52 und 58) — ein Hinweis, dass das Verzeichnis selbst versioniert ist ([Q25](../../QUELLEN.md#q25), Kap. 3).

**Versionsstand:** Ein Zulassungs-Prüfbericht von 2024 führt zwölf dieser Dokumente in **Version 1.12.0** auf, teils mit vollständigeren Titeln als im Regelwerk — die KA AktM-SPEC etwa als „Aktionsmanagement für die Berechtigungsart EFS **und Entsperrung von AF…**“ ([Q37](../../QUELLEN.md#q37)).

**Bezug:** Die Dokumente sind nicht öffentlich. Der offizielle Weg führt über das ASM-Tool des VDV eTicket Service ([Q26](../../QUELLEN.md#q26)); die Anfrageliste steht in [BESCHAFFUNG.md](../../BESCHAFFUNG.md).

## Einfach erklärt – Beispiel aus Bärstadt

„Die VDV-Kernapplikation“ klingt nach einem Buch. Es sind etwa sechzig.

Diese Zahl ist der nützlichste Teil dieses Artikels, denn sie verändert die Erwartung. Wer hofft, mit *einem* Dokument alles zu verstehen, sucht vergeblich. Die Festlegungen sind nach Gegenstand verteilt: Datentypen in einem Dokument, Nachrichten in einem zweiten, das Aktionsmanagement in einem dritten, die Sicherheit in einem vierten.

Entsprechend verweisen die Dokumente ständig aufeinander. Wer verstehen will, wie Pias Abo auf die Karte kommt, braucht mindestens drei: das Aktionsmanagement für den Auftrag, die Schnittstellenspezifikation für die Nachricht und das Basisobjektmodell für die Bedeutung der Zahlen darin.

Das Praktische am Verzeichnis im eTicket-Regelwerk ist, dass es **öffentlich** ist. Man kann also genau benennen, was man braucht — Inventarnummer 41 für das Aktionsmanagement, Nummer 1 für die Codelisten — auch wenn man die Dokumente selbst nicht hat. Für eine Anfrage ist das der Unterschied zwischen „schicken Sie mir mal alles“ und einer Liste, über die jemand entscheiden kann.

Zwei Details verraten etwas über das Alter des Gebildes. Erstens stehen im Verzeichnis zwei Einträge mit dem Vermerk „entfallen ab Release 1.6.0“ — es gibt also Dokumente, die es gab und nicht mehr gibt. Zweitens nennt ein Prüfbericht von 2024 dieselben Dokumente in Version 1.12.0, während die öffentlich auffindbaren Projektunterlagen noch von 1.1.07 und 1.3.0 sprechen.

Daraus folgt eine nützliche Vorsicht: Ein Kurzzeichen wie „KA AktM-SPEC“ allein genügt nicht. Ohne Versionsangabe weiß man nicht, welche Fassung gemeint ist.

## Quellen

- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 „VDV-KA-Dokumentation“ (PDF-S. 34 ff.): vollständiges Verzeichnis mit Inventarnummern 0 bis 59 und Kurzzeichen; Vermerke „entfallen ab Release 1.6.0“ zu den Nummern 52 und 58
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht (2024), S. 4: zwölf Spezifikationen in Version 1.12.0, teils mit vollständigeren Titeln
- [Q26](../../QUELLEN.md#q26) – VDV eTicket Service, Support: Bereitstellung von Spezifikationen und Releases über das ASM-Tool
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE als öffentlich verfügbares Dokument der Inventarnummer 0

<!-- GEN:siehe_auch -->
## Siehe auch

- [Versionen](versionen.md)
- [VDV-Kernapplikation](vdv-kernapplikation.md) (KA)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Grundlagen](../grundlagen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
