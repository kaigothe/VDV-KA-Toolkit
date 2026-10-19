---
titel: Transaktionen
englisch: transactions and messages
parent: README.md
siehe_auch: [lexikon/aktionsmanagement.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: [O1]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../README.md) › Transaktionen
<!-- /GEN:breadcrumb -->

# Transaktionen

Diese Kategorie behandelt zwei Ebenen, die leicht verwechselt werden und sorgfältig zu trennen sind.

Auf der **Nutzermedium-Ebene** ist eine Transaktion eine Folge von Programmschritten, die als logische Einheit gilt, weil sie den Datenbestand nach fehlerfreier und vollständiger Ausführung in einem konsistenten Zustand hinterlässt; gefordert ist, dass sie entweder vollständig und fehlerfrei oder gar nicht ausgeführt wird. Im Kontext der KA finden Transaktionen in diesem Sinn **ausschließlich zwischen Nutzermedium und Akzeptanzterminal unter Mithilfe eines SAM** statt ([Q02](../QUELLEN.md#q02), S. 96).

Auf der **Hintergrundsystem-Ebene** sind Transaktionen XML-Datenstrukturen, die `TX*`-Nachrichten. Sie wurden ursprünglich für den Datenaustausch zwischen KA-Hintergrundsystemen entworfen ([Q06](../QUELLEN.md#q06), Kap. 2.1.2) und stammen aus der nicht öffentlichen KA SST-SPEC ([Q25](../QUELLEN.md#q25), Kap. 3, Inventarnummer 4).

Was auf dem Medium geschah, wird dem Hintergrund durch einen **Nachweis** mitgeteilt — eine Nachricht, die eine zuvor ausgeführte Transaktion auf Nutzermedium-Ebene authentisch protokolliert ([Q02](../QUELLEN.md#q02), S. 65).

Jede `TX*`-Nachricht trägt einen gemeinsamen Kopf, das `TX_BASE`. Dort steht unter anderem die Transaktions-ID, über die Duplikate erkannt werden ([Q06](../QUELLEN.md#q06), Kap. 5.3).

Achtung bei den Typfeldern: `transTransaktionsTyp` im `TX_BASE` und `logTransaktionsTyp` im Medienteil sind **zwei verschiedene Codelisten**.

## Einfach erklärt – Beispiel aus Bärstadt

Ein Vergleich hilft, die zwei Ebenen auseinanderzuhalten: Transaktion ist hier wie beim Geldautomaten gemeint.

Wenn Pia Brummbär ihre BärenKarte an das Lesegerät T-4712 am Hauptbahnhof hält, läuft dort eine Transaktion im engen Sinn: ein Schreibvorgang auf dem Chip, der entweder ganz gelingt oder gar nicht stattfindet. Ein halb geschriebenes Abo darf es nicht geben — sonst hätte Pia eine Karte in einem undefinierten Zustand. Deshalb die strenge Regel: alles oder nichts.

Dieser Vorgang passiert **zwischen zwei Geräten**, der Karte und dem Terminal, und ein Sicherheitsbaustein im Terminal, das SAM, hilft dabei. Kein Rechenzentrum ist beteiligt. Das ist wichtig: Die eigentliche Transaktion findet an der Haltestelle statt, nicht im Backend.

Nun braucht aber das Backend die Information. Und hier kommt die zweite Ebene: Das Terminal schreibt eine **Nachricht** darüber, was geschehen ist, und schickt sie los. Diese Nachrichten heißen ebenfalls Transaktionen und tragen Namen wie `TXABER` oder `TXEBER`.

Der Unterschied in einem Bild: Das eine ist der Vorgang am Schalter, das andere der Beleg, der danach in die Buchhaltung geht. Beide heißen in der VDV-KA „Transaktion“, und wer beim Lesen einer Spezifikation nicht aufpasst, verwechselt den Beleg mit dem Vorgang.

Jeder Beleg hat einen gleich aufgebauten Briefkopf, das `TX_BASE`. Darin stehen Absender, Empfänger, eine laufende Nummer und der Nachrichtentyp — genug, damit das Backend weiß, worum es geht, und erkennt, wenn derselbe Beleg zweimal ankommt.

Die Unterartikel gehen die einzelnen Belegarten durch: den Ausgabenachweis, den Rücknahmenachweis, den Entsperrnachweis, den Kontrollnachweis und die Quittung, mit der das Backend antwortet.

## Quellen

- [Q02](../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 96 („Transaktion“: Definition und Beschränkung auf Nutzermedium und Akzeptanzterminal unter Mithilfe eines SAM), S. 65 („Nachweis“)
- [Q06](../QUELLEN.md#q06) – RMV PH 06-02, Kap. 2.1.2 (`TX*`-Datenstrukturen aus der KA SST-SPEC, ursprünglich für den Austausch zwischen Hintergrundsystemen entworfen), Kap. 4 (Datenstrukturen), Kap. 5.3 (Transaktions-ID und Duplikate) · *verbundspezifisch: eTicket RheinMain*
- [Q25](../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SST-SPEC als Inventarnummer 4, KA XML-Schemata und WSDL als Inventarnummer 5)

<!-- GEN:unterartikel -->
## Unterartikel

- [Duplikaterkennung](transaktionen/duplikaterkennung.md)
- [logTransaktionsTyp](transaktionen/logtransaktionstyp.md)
- [Nachweis](transaktionen/nachweis.md)
- [Pflichtelemente einer Transaktion](transaktionen/pflichtelemente-einer-transaktion.md)
- [Transaktion](transaktionen/transaktion.md)
- [TX_BASE](transaktionen/tx-base.md)
- [TXA/TXB](transaktionen/txa-txb.md)
- [TXABER](transaktionen/txaber.md)
- [txalisber](transaktionen/txalisber.md)
- [TXAML](transaktionen/txaml.md)
- [TXEBER](transaktionen/txeber.md)
- [TXRBER](transaktionen/txrber.md)
- [TXSNAWB](transaktionen/txsnawb.md)
<!-- /GEN:unterartikel -->

<!-- GEN:siehe_auch -->
## Siehe auch

- [Aktionsmanagement](aktionsmanagement.md) (AktM)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../README.md) · [Register](../REGISTER.md)
<!-- /GEN:navigation -->
