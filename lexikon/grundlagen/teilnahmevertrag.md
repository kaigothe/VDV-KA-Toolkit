---
titel: Teilnahmevertrag
englisch: participation agreement
parent: lexikon/grundlagen.md
siehe_auch: [lexikon/grundlagen/eticket-deutschland.md, lexikon/sicherheit/sicherheitsebenen.md]
quellen: [Q02, Q25, Q45, Q46]
status: zu prüfen
offene_fragen: [O19]
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Grundlagen](../grundlagen.md) › Teilnahmevertrag
<!-- /GEN:breadcrumb -->

# Teilnahmevertrag

Der Teilnahmevertrag ist die Eintrittskarte in [eTicket Deutschland](eticket-deutschland.md) ([Q02](../../QUELLEN.md#q02), S. 94); Muster und Regelwerk liegen in [Q25](../../QUELLEN.md#q25) vor.

**Er ist nicht die einzige Vertragsform.** Das ASM-Tool-Glossar nennt zwei kleinere ([Q45](../../QUELLEN.md#q45), S. 10):

- Der **eTicket-Ready-Vertrag** steht Verkehrsunternehmen und -verbünden offen, die die Leistungen des VDV eTicket Service **ausschließlich zum Testbetrieb** in Anspruch nehmen wollen. Zugewiesen wird dann nur ein Identifikator für den Testbetrieb.
- Der **2D-Barcode-Vertrag** ermöglicht die ausschließliche Nutzung der [statischen Berechtigung](../berechtigungen/statische-berechtigung.md), insbesondere für den [VDV-Barcode](../datenformate/vdv-barcode.md). Nach Vertragsschluss erhalten die Teilnehmer ihre Organisations-IDs für Test- **und** Wirkbetrieb.

**Vertragsform und Organisations-IDs hängen zusammen.** Im ASM-Tool wird der Kundenstatus nach Unternehmensart und Vertragsverhältnis unterschieden ([Q45](../../QUELLEN.md#q45), S. 22):

| Kundenstatus | Vertragsverhältnis | Organisations-IDs |
|---|---|---|
| Teilnehmer Level-1 | VU/VV ohne eTicket-Vertrag | keine |
| Teilnehmer Level-2 | VU/VV mit eTicket-Ready-Vertrag | Level-2 |
| Teilnehmer Level-3 | VU/VV mit „FU“-eTicket-Vertrag (zu prüfen, O19) | Level-2 und Level-3 |
| Teilnehmer 2D-Barcode | VU/VV mit eTicket-2D-Barcode-Vertrag | Level-2 und Level-3 |
| Hersteller | Industrie oder Hersteller ohne Hersteller-Paket | keine |
| Hersteller | Industrie oder Hersteller mit Hersteller-Paket | Level-2 |
| Berater, Dienstleister | kein Vertragsabschluss möglich | keine |

Daran ist eine Systematik ablesbar: **Wer nur testen darf, bekommt keine Wirk-ID** — und wer gar keinen Vertrag hat, bekommt überhaupt keine (abgeleitet). Siehe [Sicherheitsebenen](../sicherheit/sicherheitsebenen.md).

**Kosten:** Der Abschluss des Vertrages ist kostenlos; Kosten entstehen erst bei der Realisierung eines Systems. Weil es ein offener Standard ist, darf jeder Hersteller auf Grundlage der KA-Spezifikationen entwickeln ([Q46](../../QUELLEN.md#q46), Kap. 6.1, PDF-S. 15).

**Stand der Vertragsarten:** 2016.

## Einfach erklärt – Beispiel aus Bärstadt

Angenommen, ein kleines Busunternehmen aus Luchsstadt möchte mitmachen. Es muss nicht gleich alles unterschreiben.

**Stufe eins: nur ausprobieren.** Das Unternehmen schließt einen eTicket-Ready-Vertrag. Damit darf es die Dienste nutzen — aber nur zum Testen. Es bekommt eine Kennung für den Testbetrieb, und mit dieser Kennung erzeugte Berechtigungen erkennt kein Wirksystem an. Petra Pranke würde ein so erzeugtes Ticket in der Linie 4 abweisen, und das ist beabsichtigt.

Das ist eine kluge Konstruktion. Ein Unternehmen kann ein halbes Jahr entwickeln, ohne dass ein Fehler im Wirkbetrieb Schaden anrichtet.

**Stufe zwei: nur Barcodes.** Vielleicht will das Unternehmen gar keine Chipkarten ausgeben, sondern nur Handy-Tickets verkaufen. Dafür gibt es einen eigenen Vertrag, der sich auf die statische Berechtigung beschränkt. Und hier bekommt es beide Kennungen — für Test und für den echten Betrieb. Wer Barcodes verkaufen will, soll sie auch verkaufen dürfen.

**Stufe drei: alles.** Das ist der Weg, den die Bärstädter Verkehrsbetriebe gegangen sind. Sie geben Karten aus, schreiben Berechtigungen, kontrollieren, rechnen ab. Dafür braucht es den vollen Vertrag — und zwei Kennungen: die 9010 für den Wirkbetrieb und eine zweite für die Testumgebung.

**Und wer nichts bekommt.** Zwei Gruppen sind ausdrücklich genannt. Hersteller ohne das zugehörige Paket erhalten keine Kennung. Und Berater oder Dienstleister können gar keinen Vertrag abschließen — für sie ist in diesem System kein Platz vorgesehen.

Das erklärt eine Hürde, die dieses Lexikon selbst betrifft: Wer sich aus Interesse in die VDV-KA einarbeitet, ohne für ein Verkehrsunternehmen zu arbeiten, findet keine Vertragsform, die auf ihn passt.

**Was es kostet.** Der Vertrag selbst nichts. Teuer wird erst das System dahinter. Und weil es ein offener Standard ist, darf jeder Hersteller dafür bauen — man muss nicht beim VDV einkaufen.

## Quellen

- [Q45](../../QUELLEN.md#q45) – ASM-Tool Glossar und Abkürzungsverzeichnis V1.03 (20.07.2016): S. 10 („eTicket Ready Vertrag“: ausschließlicher Testbetrieb, Zuweisung nur eines Identifikators bzw. einer Organisations-ID für den Testbetrieb; „2D-Barcode-Vertrag“: ausschließliche Nutzung der statischen Berechtigung, insbesondere für den 2D- bzw. VDV-Barcode, Organisations-IDs für Test- und Wirkbetrieb), S. 22 („Kundenstatus“: Unterscheidung nach Unternehmensart und ETS-Vertragsverhältnis mit den sieben aufgeführten Zeilen; „Kundenrolle“: Kundenvertragspartner, Produktverantwortlicher, Dienstleister)
- [Q46](../../QUELLEN.md#q46) – Whitepaper Barcodes im ÖPNV (2021), Kap. 6.1, PDF-S. 15 (eTicket-Teilnahmevertrag als Voraussetzung für VDV-Barcode und VDV-Barcode mobile+; Vertragsunterlagen nach kostenloser Registrierung; kostenloser Vertragsabschluss; Kosten erst bei der Realisierung; offener Standard, jeder Hersteller darf auf Grundlage der KA-Spezifikationen entwickeln)
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 94 („Teilnahmevertrag“)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk mit Teilnahmevertrag und Anlagen

<!-- GEN:siehe_auch -->
## Siehe auch

- [eTicket Deutschland](eticket-deutschland.md)
- [Sicherheitsebenen](../sicherheit/sicherheitsebenen.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Grundlagen](../grundlagen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
