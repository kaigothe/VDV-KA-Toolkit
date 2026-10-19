---
titel: Sperrgrund
englisch: Blocking Reason
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/sperrlisteneintrag.md, lexikon/kontrolle/sperrliste.md]
quellen: [Q02, Q25, Q33]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Sperrgrund
<!-- /GEN:breadcrumb -->

# Sperrgrund

„Der Sperrgrund beschreibt, **warum** ein Objekt gesperrt wurde bzw. gesperrt werden soll.“ ([Q02](../../QUELLEN.md#q02), S. 88)

Das Glossar nennt keine Werteliste. Welche Sperrgründe zulässig sind, steht in der nicht öffentlichen KA BOM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 1) (abgeleitet). Die allgemeine Richtung gibt der Eintrag zum Sperrlistenservice: Einträge geben einen Hinweis darauf, „dass die referenzierte Instanz **gestohlen, kompromittiert, ungültig** usw. ist“ ([Q02](../../QUELLEN.md#q02), S. 54).

**Warum ein Grund überhaupt mitgeführt wird** (abgeleitet): Die Sperre allein sagt nur, dass etwas nicht gilt. Erst der Grund entscheidet über die Folgen — ob ein Ersatzmedium ausgegeben wird, ob ein Entgelt zurückzuzahlen ist, ob der Vorgang strafrechtlich relevant ist und ob eine Entsperrung überhaupt in Frage kommt.

Welche Fälle praktisch auftreten, lässt sich aus einem aktuellen Branchendokument ablesen. Für das Deutschlandticket auf Chipkarte werden als Anlässe für eine unmittelbare Sperre genannt: **Kündigung, Stornierung und Zahlungsrückläufer**. Begründet wird das mit dem „Potential für großen wirtschaftlichen Schaden“, da es sich um **Dauerberechtigungen** handelt; außerdem sei nur so „der Ersatz des Tickets bei unabsichtlichem Verlust“ umsetzbar ([Q33](../../QUELLEN.md#q33), Kap. 7.2) · *produktbezogen*.

Daran zeigt sich die Bandbreite: Vom Verlust ohne Verschulden — mit Anspruch auf Ersatz — bis zum Zahlungsausfall reicht dieselbe technische Maßnahme, aber mit völlig verschiedenen kaufmännischen Folgen (abgeleitet).

Zur Prüfung auf Betrug nennt [Q33](../../QUELLEN.md#q33), Kap. 4.2, außerdem stornierte oder erstattete Tickets, den Kauf nach einem Erhöhten Beförderungsentgelt und gekündigte Tickets.

## Einfach erklärt – Beispiel aus Bärstadt

Dass etwas gesperrt ist, genügt nicht. Man muss wissen, warum.

Für Pia ist das von erheblicher Bedeutung. Sie hat ihre BärenKarte verloren — unverschuldet, und sie hat ihr Abo bezahlt. Entsprechend bekommt sie eine Ersatzkarte und ihr Abo neu darauf.

Nun ein anderer Fall. Jemandes Abbuchung platzt zum dritten Mal. Auch dann wird gesperrt, und die technische Maßnahme ist genau dieselbe: ein Eintrag in der Liste, ein Sperrvermerk auf dem Chip. Aber hier gibt es keine Ersatzkarte und kein Geld zurück.

Dritter Fall: Jemand hat die Karte manipuliert. Wieder dieselbe Maßnahme — und diesmal wird niemand entsperren.

Drei identische Sperren, drei völlig verschiedene Geschichten. Deshalb trägt jeder Sperrlisteneintrag einen Grund mit sich. Er entscheidet über alles, was danach kommt: Ersatz oder nicht, Rückzahlung oder nicht, Entsperrung möglich oder nicht.

Für Bodo Bärlauch im Kundencenter ist das die eigentliche Arbeitsgrundlage. Pia steht vor ihm und will ihre Karte wiederhaben. Er schaut nach, warum sie gesperrt ist — und erst diese Angabe sagt ihm, ob er entsperren darf oder ob er Nein sagen muss.

Welche Gründe es im Standard genau gibt, ist eine der Lücken dieses Lexikons. Das Glossar erklärt, was ein Sperrgrund ist, nennt aber keine Werte; die Liste steht im nicht öffentlichen Basisobjektmodell.

Aus einem aktuellen Branchenpapier kennt man wenigstens die praktisch wichtigen Anlässe beim Deutschlandticket: Kündigung, Stornierung, Zahlungsrückläufer — und der Verlust, bei dem ein Ersatz möglich sein soll.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 88 („Sperrgrund / Blocking Reason“: wörtliche Definition, ohne Werteliste), S. 54 (Einträge als Hinweis darauf, dass die referenzierte Instanz gestohlen, kompromittiert oder ungültig ist)
- [Q33](../../QUELLEN.md#q33) – KCD NRW, Ergebnisdokument der Arbeitsgruppe Kontrolle, V1.3, Kap. 7.2 (Kündigung, Stornierung und Zahlungsrückläufer als Anlässe für eine unmittelbare Sperre; Begründung über das wirtschaftliche Schadenspotential von Dauerberechtigungen; Ersatz des Tickets bei unabsichtlichem Verlust), Kap. 4.2 (stornierte bzw. erstattete Tickets, Kauf nach EBE, gekündigte Tickets) · *produktbezogen auf das Deutschlandticket*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA BOM-SPEC, Inventarnummer 1, als Normquelle der Codelisten)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Sperrlisteneintrag](sperrlisteneintrag.md)
- [Sperrliste](sperrliste.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
