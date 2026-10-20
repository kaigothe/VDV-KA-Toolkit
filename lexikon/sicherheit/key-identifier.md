---
titel: Key-Identifier
abkuerzung: KID
englisch: key identifier
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/schluesselarten.md, lexikon/sicherheit/schluesselreferenz.md]
quellen: [Q05, Q45]
status: belegt
offene_fragen: [O18]
stand: 2026-10-20
codes:
  - wert: 30
    codeliste: Key_Identifier
    bedeutung: Authentisierungsschlüssel
    quelle: Q45
    fundstelle: S. 19 („Key-Identifier“)
    status: belegt
  - wert: 40
    codeliste: Key_Identifier
    bedeutung: PV-Schlüssel
    quelle: Q45
    fundstelle: S. 19 („Key-Identifier“)
    status: belegt
  - wert: 50
    codeliste: Key_Identifier
    bedeutung: KVP-Schlüssel
    quelle: Q45
    fundstelle: S. 19 („Key-Identifier“)
    status: belegt
  - wert: 60
    codeliste: Key_Identifier
    bedeutung: Transaktionsprüfschlüssel
    quelle: Q45
    fundstelle: S. 19 („Key-Identifier“)
    status: belegt
  - wert: 70
    codeliste: Key_Identifier
    bedeutung: Transaktionssicherungsschlüssel
    quelle: Q45
    fundstelle: S. 19 („Key-Identifier“)
    status: belegt
  - wert: 91
    codeliste: Key_Identifier
    bedeutung: Sperrlistensicherungsschlüssel
    quelle: Q45
    fundstelle: S. 19 („Key-Identifier“)
    status: belegt
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Key-Identifier
<!-- /GEN:breadcrumb -->

# Key-Identifier

Der Key-Identifier „bezeichnet den Einsatzzweck des Schlüssels“ ([Q45](../../QUELLEN.md#q45), S. 19):

| KID | Einsatzzweck |
|---:|---|
| **30** | Authentisierungsschlüssel |
| **40** | PV-Schlüssel |
| **50** | KVP-Schlüssel |
| **60** | Transaktionsprüfschlüssel |
| **70** | Transaktionssicherungsschlüssel |
| **91** | Sperrlistensicherungsschlüssel |

Die Werte stehen für **Nummernbereiche**, nicht für einzelne Schlüssel: Welche konkrete Nummer eine Organisation darin vergibt, ist nicht öffentlich belegt (zu prüfen, O18). In den Feldern einer Nachricht erscheint die Nummer zusammen mit Version und Inhaber — siehe [Schlüsselreferenz](schluesselreferenz.md).

**Zum Authentisierungsschlüssel (30)** ist der Zweck genauer belegt: Er dient in Erfassungs- und Kontrollterminals der authentischen Kommunikation zwischen einem [SAM](sam.md) im Terminal und einer KA-Applikation auf einem [Nutzermedium](../medien/nutzermedium.md) oder einzelnen Berechtigungen darin. Bei der Ausgabe der Applikation oder Berechtigung wird er „authentisch und vertraulich vom SAM auf das NM“ übertragen; gesichert wird dieser Vorgang mit den vorhandenen asymmetrischen Schlüsseln von SAM und Nutzermedium ([Q45](../../QUELLEN.md#q45), S. 12).

**Zur Einordnung der übrigen Bereiche:** Die Namen 40 und 50 benennen die Inhaber — den [Produktverantwortlichen](../rollen/pv.md) und den [Kundenvertragspartner](../rollen/kvp.md) —, die Namen 60 und 70 die Aufgabe an der Transaktion, nämlich deren Sicherung und deren Prüfung. Das entspricht der Aufteilung, die [Q05](../../QUELLEN.md#q05) für die [MAC](mac.md)-Schlüssel auf dem Medium zeigt (abgeleitet).

**Stand der Quelle:** 2016. Für [etiCORE](../grundlagen/eticore.md) ist die Systematik nicht belegt.

## Einfach erklärt – Beispiel aus Bärstadt

Jeder Schlüssel im Bärenland trägt eine Nummer, und diese Nummer ist kein Zufall: Sie verrät, wozu der Schlüssel da ist.

Das ist derselbe Gedanke wie bei einer Telefonvorwahl. Wer die 030 sieht, weiß, dass es nach Berlin geht, ohne die Nummer anzurufen. Wer in einer Nachricht aus Bärstadt einen Schlüssel aus dem 40er-Bereich sieht, weiß: Das ist ein Schlüssel des Produktverantwortlichen, also des Bären-Verkehrsbunds.

Die Bereiche:

- **30er** — Authentisierung. Damit stellen Petras Kontrollgerät T-4713 und Pias BärenKarte fest, dass sie es wirklich miteinander zu tun haben und nicht mit einer Nachahmung. Dieser Schlüssel wird bei der Ausgabe der Applikation vom SAM auf die Karte gebracht, und zwar vertraulich: Niemand soll ihn unterwegs mitlesen.
- **40er** — Schlüssel des Produktverantwortlichen, also des BVV. Er gehört zum Produkt, hier zum ABO Azubi.
- **50er** — Schlüssel des Kundenvertragspartners, also der BVB. Er gehört zur einzelnen Berechtigung auf Pias Karte.
- **60er und 70er** — die Transaktionen. Der eine sichert sie, der andere prüft sie.
- **91** — die Sperrliste. Auch sie muss gesichert sein, sonst könnte jemand eine eigene Sperrliste in Umlauf bringen und fremde Karten lahmlegen.

**Warum das praktisch nützlich ist.** In einer Nachricht stehen drei Schlüsselreferenzen nebeneinander, jede mit Nummer, Version und Inhaber. Wer die Bereiche kennt, erkennt sofort, ob die drei zueinander passen: Ein Schlüssel aus dem 40er-Bereich, der als Inhaber die BVB nennt, wäre eine Auffälligkeit — das ist der Bereich des Produktverantwortlichen, und der ist der BVV.

**Eine Warnung, die zu diesem Lexikon gehört.** In den Beispielen der Welt-Bibel tragen die drei Schlüssel die Nummern 110, 120 und 130. Diese Zahlen sind **frei erfunden** und liegen bewusst außerhalb der hier aufgeführten Bereiche — damit niemand sie für echte Schlüsselnummern eines Verbunds hält. Die Systematik oben ist belegt, die Beispielnummern sind es nicht.

Und noch eines: Die Quelle ist von 2016. Dass es morgen noch so ist, steht dort nicht.

## Quellen

- [Q45](../../QUELLEN.md#q45) – ASM-Tool Glossar und Abkürzungsverzeichnis V1.03 (20.07.2016): S. 19 („Key-Identifier“ bezeichnet den Einsatzzweck des Schlüssels, mit den Werten 30 Authentisierungsschlüssel, 40 PV-Schlüssel, 50 KVP-Schlüssel, 60 Transaktionsprüfschlüssel, 70 Transaktionssicherungsschlüssel, 91 Sperrlistensicherungsschlüssel), S. 12 (Authentisierungsschlüssel: authentische Kommunikation zwischen SAM im Terminal und KA-Applikation bzw. einzelnen Berechtigungen; Aufbringen auf das Nutzermedium bei der Ausgabe; Sicherung über die vorhandenen asymmetrischen Schlüssel von SAM und Nutzermedium; authentische und vertrauliche Übermittlung vom SAM auf das NM)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Schlüsselarten](schluesselarten.md)
- [Schlüsselreferenz](schluesselreferenz.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
