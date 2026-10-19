---
titel: Transaktion
englisch: transaction
parent: lexikon/transaktionen.md
siehe_auch: [lexikon/transaktionen/nachweis.md, lexikon/aktionsmanagement/aktion.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Transaktionen](../transaktionen.md) › Transaktion
<!-- /GEN:breadcrumb -->

# Transaktion

Als Transaktion wird in der Informatik eine Folge von Programmschritten bezeichnet, die als eine logische Einheit betrachtet werden, weil sie den Datenbestand nach fehlerfreier und vollständiger Ausführung in einem konsistenten Zustand hinterlassen. Gefordert ist daher, dass eine Transaktion **entweder vollständig und fehlerfrei oder gar nicht** ausgeführt wird ([Q02](../../QUELLEN.md#q02), S. 96).

Entscheidend ist die Einschränkung, die das Glossar daran anschließt: Im Kontext von KA und (((etiCORE finden Transaktionen im Sinne dieser Definition **ausschließlich zwischen Nutzermedium — insbesondere Chipkarte — und Akzeptanzterminal unter Mithilfe eines SAM** statt ([Q02](../../QUELLEN.md#q02), S. 96).

Daraus folgt die wichtigste Abgrenzung dieser Kategorie: Die `TX*`-Nachrichten der Hintergrundsysteme heißen zwar ebenfalls Transaktionen, sind aber XML-Datenstrukturen für den Datenaustausch zwischen Systemen ([Q06](../../QUELLEN.md#q06), Kap. 2.1.2) und keine Transaktionen im obigen, strengen Sinn (abgeleitet).

Zur [Aktion](../aktionsmanagement/aktion.md) grenzt das Glossar ausdrücklich ab: Anders als bei einer Transaktion ist der Vorgang bei einer Aktion noch nicht zwingend beendet und bedarf einer zusätzlichen Betätigung für den Abschluss und damit einen potentiellen Schreibvorgang im Nutzermedium ([Q02](../../QUELLEN.md#q02), S. 18).

Abgebrochene Transaktionen sind ab Schnittstellenversion KA 1.3.0 ebenfalls zu melden, als `TXTRANSABBRUCH` ([Q06](../../QUELLEN.md#q06), Kap. 4.5).

## Einfach erklärt – Beispiel aus Bärstadt

„Alles oder nichts“ klingt nach einer technischen Spitzfindigkeit. Für Pia Brummbär ist es der Unterschied zwischen einer brauchbaren und einer unbrauchbaren Karte.

Stellen wir uns vor, das Schreiben ihres ABO Azubi bestünde aus mehreren Einzelschritten: Produktnummer eintragen, Gültigkeitsdatum eintragen, Name eintragen, Sicherungscode berechnen, Status auf „aktiv“ setzen. Nun zieht Pia die Karte nach dem dritten Schritt weg.

Was läge jetzt auf dem Chip? Ein halbes Abo. Mit Produktnummer und Datum, aber ohne Sicherungscode. Für die Kontrolle wäre es nicht prüfbar, für das Hintergrundsystem nicht nachvollziehbar, und niemand könnte sagen, ob Pia ein gültiges Ticket hat oder nicht. Noch schlimmer: Beim nächsten Versuch wüsste das Terminal nicht, ob es von vorn anfangen oder fortsetzen soll.

Genau das verhindert die Regel. Der Vorgang gilt erst als geschehen, wenn er komplett durchgelaufen ist. Bricht er vorher ab, ist die Karte so, wie sie vorher war — als hätte Pia sie nie hingehalten. Beim nächsten Kontakt beginnt alles neu.

Bemerkenswert ist, wo dieser Vorgang stattfindet: **nur zwischen Karte und Terminal**, mit dem Sicherheitsbaustein des Terminals als Helfer. Das Rechenzentrum ist in diesem Moment nicht beteiligt und könnte auch nicht eingreifen.

Das ist der Grund für ein Missverständnis, das man häufig antrifft. Weil die Meldungen an das Backend ebenfalls „Transaktionen“ heißen, denkt man leicht, dort passiere das Eigentliche. Es ist umgekehrt: Dort kommen nur die Belege an. Das Eigentliche geschah an der Haltestelle — in einer Sekunde, ganz oder gar nicht.

Und bricht es ab, gibt es dafür seit der Version 1.3.0 eine eigene Meldung.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 96 („Transaktion / Transaction“: Definition als logische Einheit, Forderung „vollständig und fehlerfrei oder gar nicht“, Beschränkung auf Nutzermedium und Akzeptanzterminal unter Mithilfe eines SAM), S. 18 („Aktion“, Abgrenzung)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.2 (`TX*`-Datenstrukturen für den Austausch zwischen Hintergrundsystemen), Kap. 4.5 (`TXTRANSABBRUCH` ab KA 1.3.0) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Nachweis](nachweis.md)
- [Aktion](../aktionsmanagement/aktion.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Transaktionen](../transaktionen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
