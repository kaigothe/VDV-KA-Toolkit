---
titel: Duplikaterkennung
englisch: duplicate detection
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/tx-base.md, lexikon/transaktionen/txa-txb.md]
quellen: [Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Duplikaterkennung
<!-- /GEN:breadcrumb -->

# Duplikaterkennung

Ein Hintergrundsystem muss erkennen, wenn dieselbe Transaktion zweimal eintrifft. Im eTicket RheinMain wird dabei **nicht** auf eindeutige Dateinamen geprüft, sondern auf den Inhalt der Transaktionsdatensätze ([Q06](../../QUELLEN.md#q06), Kap. 5.3) · *verbundspezifisch*.

Ein Duplikat liegt auf zwei Weisen vor ([Q06](../../QUELLEN.md#q06), Kap. 5.3):

1. `transTransaktion_ID` **und** `transWiederholungsZaehler` aus dem [`TX_BASE`](tx-base.md) sind identisch zu einer bereits vorhandenen Transaktion.
2. Die ID einer in der XML-Transaktion enthaltenen **Nutzermedium-Transaktion in TLV-Form** ist identisch zu einer bereits vorhandenen NM-Transaktion.

Ein erkanntes Duplikat wird abgelehnt und mit einem [`TXA`](txa-txb.md) beantwortet. Bemerkenswert ist der dokumentierte Mangel: Um den Ablehnungsgrund differenziert zu übermitteln, müsste die Codeliste `AblehnungsTyp_CODE` erweitert werden, damit „XML-Tx-ID-Duplikat“ und „NM-Tx-ID-Duplikat“ unterschieden werden können; die zusätzlichen Codes waren bei der VDV KA **noch zu beantragen** ([Q06](../../QUELLEN.md#q06), Kap. 5.3).

Davon zu unterscheiden ist das **wiederholte Senden**: Trifft eine Transaktion mit gleicher Transaktions-ID, aber anderem Wiederholungszähler ein, antwortet das System mit einer **Kopie** der ursprünglichen Antwort (`TXA` bzw. `TXB`), wobei im Wiederholungszähler der Kopie der Wert der neuen Sendung eingesetzt wird ([Q06](../../QUELLEN.md#q06), Kap. 5.3).

Folge für Betreiber: Transaktions-IDs müssen eindeutig sein, notfalls über mehrere technische Systeme hinweg. Betreibt ein Absender mehrere Terminalmanagementsysteme, sind für die Sequenznummern **Nummernkreise** zu bilden ([Q06](../../QUELLEN.md#q06), Kap. 5.3).

## Einfach erklärt – Beispiel aus Bärstadt

Eine Rückmeldung kann verloren gehen. Dann schickt das Terminalmanagementsystem sie noch einmal — und das Backend muss unterscheiden, ob es einen neuen Vorgang vor sich hat oder denselben zum zweiten Mal.

Naiv würde man am Dateinamen erkennen wollen, dass etwas schon da war. Das reicht nicht: Derselbe Inhalt kann unter beliebigem Namen ankommen. Geprüft wird deshalb der Inhalt.

Dabei gibt es zwei Schlösser an derselben Tür.

Das erste ist das **Aktenzeichen der Nachricht** samt Wiederholungszähler. Kommt genau diese Kombination ein zweites Mal, ist es ein Duplikat.

Das zweite ist die **Kennung des Vorgangs auf der Karte**. Das ist das feinere Schloss. Es greift auch dann, wenn jemand den gleichen Kartenvorgang in zwei verschieden beschrifteten Nachrichten einreicht — gewollt oder aus Versehen. Pias Abo soll nicht zweimal verbucht werden, nur weil zwei Systeme dieselbe Meldung geschickt haben.

Besonders elegant ist der Umgang mit dem ehrlichen Wiederholungsfall. Die BVB schickt eine Meldung erneut, weil die Antwort ausblieb — diesmal mit höherem Wiederholungszähler. Das Backend verarbeitet sie nicht neu. Es holt die **damalige Antwort** hervor, setzt den neuen Zähler ein und schickt sie zurück. Die BVB bekommt also genau die Auskunft, die ihr zusteht, ohne dass irgendetwas doppelt gebucht wird.

Eine praktische Konsequenz für die BVB: Betreibt sie mehrere Terminalsysteme, dürfen die ihre Nummern nicht unabhängig voneinander vergeben — sonst zählen zwei Systeme beide ab 1 und erzeugen Nachrichten, die das Backend für Duplikate hält. Deshalb teilt man den Nummernraum auf.

Und ein ehrliches Detail aus dem Pflichtenheft: Das Backend *kann* ein Duplikat ablehnen, aber nicht genau sagen, welches der beiden Schlösser gegriffen hat. Dafür fehlten die Codes.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 5.3 „Duplikate und wiederholtes Senden“ (PDF-S. 41): keine Prüfung auf eindeutige Dateinamen, sondern auf den Inhalt; die zwei Duplikatfälle; Ablehnung mit `TXA`; fehlende Codes in `AblehnungsTyp_CODE`; Verfahren beim wiederholten Senden; Zusammensetzung der `IONTransaktion_ID`; Pflicht zur Bildung von Nummernkreisen · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
