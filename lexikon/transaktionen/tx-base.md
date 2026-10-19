---
titel: TX_BASE
abkuerzung: TX_BASE
englisch: transaction base
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/duplikaterkennung.md, lexikon/transaktionen/logtransaktionstyp.md]
quellen: [Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › TX_BASE
<!-- /GEN:breadcrumb -->

# TX_BASE

`TX_BASE` ist der gemeinsame Kopf aller `TX*`-Nachrichten der VDV-KA. Die Struktur ist in der nicht öffentlichen KA SST-SPEC definiert ([Q06](../../QUELLEN.md#q06), Kap. 4.6; [Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 4); jede Datenstrukturbeschreibung in [Q06](../../QUELLEN.md#q06), Kap. 4, verweist für den `TX_BASE`-Teil auf Kap. 4.10.

Bekannte Attribute aus den öffentlichen Quellen:

- `transTransaktion_ID` enthält die Datenstruktur `IONTransaktion_ID`, zusammengesetzt aus `transSender_ID` (Org-ID), `transSenderRolle` (Rollen-Code) und `transSequenznummer` (`SequenceNumberFour`) ([Q06](../../QUELLEN.md#q06), Kap. 5.3).
- `transWiederholungsZaehler` unterscheidet wiederholtes Senden derselben Transaktion ([Q06](../../QUELLEN.md#q06), Kap. 5.3).
- `transSender_ID`, `transSenderRolle`, `transEmpfaenger` tragen Org-ID und Rollen-Code ([Q06](../../QUELLEN.md#q06), Kap. 4.10).
- `transTransaktionsTyp` trägt den `IONTransaktionsTyp_CODE` ([Q06](../../QUELLEN.md#q06), Kap. 4.6, 4.7, 4.9). **Nicht zu verwechseln** mit dem [`logTransaktionsTyp`](logtransaktionstyp.md) im Medienteil.

**Ab KA 1.3.0** wurden mit Einführung der ZVM und der Aufteilung der Schnittstellendefinitionen einige Attribute als optional deklariert (`minOccurs="0" maxOccurs="1"`). Die Handhabung im eTicket RheinMain ([Q06](../../QUELLEN.md#q06), Kap. 5.4) · *verbundspezifisch*:

| Attribut | Handhabung im RMV |
|---|---|
| `transAuftrag` | optional |
| `transStatus` | nicht optional |
| `transTransaktionsTyp` | nicht optional |
| `transVersion` | nicht optional |
| `transWiederholungsZaehler` | nicht optional |
| `transSignaturTyp` | optional |
| `transSignaturZertifikat` | optional |
| `transSignatur` | optional |

## Einfach erklärt – Beispiel aus Bärstadt

Jede Nachricht in der VDV-KA hat einen Briefkopf, und der heißt `TX_BASE`. Er ist bei allen Nachrichten gleich aufgebaut — egal ob eine Ausgabe gemeldet wird, eine Kontrolle oder eine Rücknahme.

Was auf diesem Briefkopf steht, kennt man von einem Geschäftsbrief:

**Von wem.** Die Organisations-ID des Absenders, in Bärstadt also 9010 für die Bärstädter Verkehrsbetriebe, und dazu die Rolle, in der er schreibt. Das ist nötig, weil dieselbe Organisation in mehreren Rollen auftreten kann — die BVB ist Kundenvertragspartner und Dienstleister zugleich.

**An wen.** Dasselbe für den Empfänger.

**Aktenzeichen.** Eine Nummer, die diese Nachricht eindeutig macht. Sie ist nicht einfach eine laufende Zahl, sondern aus drei Teilen gebaut: Absender-ID, Rolle und eine laufende Nummer. So kann die BVB ihre Nummern unabhängig von allen anderen zählen, ohne dass es Kollisionen gibt.

**Worum es geht.** Der Nachrichtentyp.

**Ein Wiederholungszähler.** Der ist die unscheinbarste und praktischste Angabe. Geht eine Nachricht verloren und die BVB schickt sie erneut, trägt die zweite Sendung dieselbe Nummer, aber einen höheren Zähler. Das Backend erkennt daran: Das ist kein neuer Vorgang, das ist derselbe noch einmal.

Interessant ist die Liste der Felder, die ab Version 1.3.0 weggelassen werden *dürfen*. Dazu gehören drei Signaturfelder. Das eTicket RheinMain nutzt diese Freiheit auch — Signatur und Auftrag sind dort optional, Status und Typ dagegen Pflicht.

Für jemanden, der eine solche Nachricht auswertet, heißt das: Fehlt ein Signaturfeld, ist das nicht zwingend ein Fehler. Es kann die bewusste Entscheidung des Verbunds sein.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.6, 4.7, 4.9 (`txbase`-Element mit Verweis auf die KA SST-SPEC, `IONTransaktionsTyp_CODE`), Kap. 4.10 (in `TX_BASE` verwendete Rollencodes und Org-IDs, Sender- und Empfängerattribute), Kap. 5.3 (`transTransaktion_ID` als `IONTransaktion_ID` aus Org-ID, Rollen-Code und Sequenznummer; `transWiederholungsZaehler`), Kap. 5.4 (ab KA 1.3.0 optionale Attribute samt Handhabung im RMV) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SST-SPEC, Inventarnummer 4; KA XML-Schemata und WSDL, Inventarnummer 5)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
