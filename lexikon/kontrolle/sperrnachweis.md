---
titel: Sperrnachweis
englisch: Blocking Attestation
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/sperrlisteneintrag.md, lexikon/aktionsmanagement/aktionsclearing.md]
quellen: [Q02, Q39]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Sperrnachweis
<!-- /GEN:breadcrumb -->

# Sperrnachweis

Ein Sperrnachweis entsteht, „wenn beim Prüfen von Applikation und Berechtigungen gegen die entsprechenden Sperrlisten ein **relevanter Sperrlisteneintrag gefunden wird**. Das dann folgende physikalische Sperren einer Applikation oder Berechtigung wird jeweils durch einen **authentischen** Sperrnachweis dokumentiert, der zusätzlich noch per Meldung vom **Terminal** an die verantwortlichen Instanzen geschickt wird.“ ([Q02](../../QUELLEN.md#q02), S. 90)

Drei Eigenschaften sind daran wesentlich:

- Er entsteht **bei der Kontrolle**, nicht beim Sperrauftrag. Der Auftrag sagt, dass gesperrt werden soll; der Nachweis belegt, dass es geschehen ist (abgeleitet).
- Er ist **authentisch**, also kryptografisch gesichert — wie jeder [Nachweis](../transaktionen/nachweis.md) protokolliert er eine ausgeführte Transaktion auf Nutzermedium-Ebene ([Q02](../../QUELLEN.md#q02), S. 65).
- Er wird **vom Terminal** gemeldet, nicht vom Hintergrundsystem ([Q02](../../QUELLEN.md#q02), S. 90).

In der KA werden Sperrnachweise im Rahmen von Collecting and Forwarding nach ISO 24014-1 bearbeitet: Sie beziehen sich auf eine Berechtigung oder eine Applikation, werden von den Dienstleistern **gesammelt und weitergeleitet** ([Q02](../../QUELLEN.md#q02), S. 54). In etiCORE entfällt diese Funktion; Sperrnachweise gehen dann direkt vom Dienstleister an den Produktverantwortlichen ([Q02](../../QUELLEN.md#q02), S. 54).

Im eTicket RheinMain läuft der Weg vom Dienstleister als `TXSNAWB` bzw. `TXSNAWA` an den Kundenvertragspartner ([Q39](../../QUELLEN.md#q39)) · *verbundspezifisch*.

Praktisch wichtig: Ein Sperrnachweis belegt gegenüber dem [Aktionsclearing](../aktionsmanagement/aktionsclearing.md), dass auf dem Medium etwas geschehen ist — auch wenn der erwartete Ausgabe- oder Entsperrnachweis fehlt ([Q02](../../QUELLEN.md#q02), S. 18).

## Einfach erklärt – Beispiel aus Bärstadt

Der Sperrnachweis ist der Beleg: „Diese Karte ist jetzt wirklich stillgelegt."

Der Weg dorthin ist weniger offensichtlich, als man denkt. Als Bodo Bärlauch Pias Karte sperrte, entstand **kein** Sperrnachweis. Er hat nur einen Eintrag in eine Liste geschrieben — eine Absicht, nicht eine Tat. Die Karte selbst war davon unberührt und lag irgendwo auf der Straße.

Der Nachweis entsteht erst später, und zwar an einer überraschenden Stelle: **bei der Kontrolle.**

Angenommen, jemand findet Pias Karte und fährt damit. Petra Pranke prüft sie in der Linie 4. Ihr Gerät findet den Sperreintrag in seiner Liste und tut jetzt zwei Dinge: Es setzt den Sperrvermerk auf den Chip — und schreibt einen Nachweis darüber.

Erst in diesem Moment ist die Sperre auf der Karte angekommen. Von nun an wirkt sie überall, auch an Geräten, die die Liste gar nicht haben.

Dass der Nachweis vom **Gerät** kommt und nicht vom Rechenzentrum, ist konsequent: Nur das Gerät war dabei. Und dass er kryptografisch gesichert ist, auch — eine Behauptung „wir haben gesperrt" wäre wertlos, wenn sie sich nicht beweisen lässt.

Dieser Nachweis hat noch einen zweiten, weniger offensichtlichen Nutzen. Beim Aktionsclearing dient er als Indiz: Wenn ein Sperrnachweis für eine Karte vorliegt, dann war die Karte nachweislich an einem Gerät. Ein noch offener Auftrag für diese Karte kann also abgeräumt werden, auch wenn seine eigene Rückmeldung verloren ging.

Ein Beleg über eine Sperrung hilft also dabei, eine Ausgabe zu verbuchen. Das ist unerwartet und ziemlich elegant.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 90 („Sperrnachweis / Blocking Attestation“: Entstehung beim Prüfen gegen die Sperrlisten, Dokumentation des physikalischen Sperrens durch einen authentischen Nachweis, Meldung vom Terminal an die verantwortlichen Instanzen), S. 54 (Bearbeitung im Rahmen von Collecting and Forwarding nach ISO 24014-1, Sammeln und Weiterleiten durch die Dienstleister, Wegfall in etiCORE mit direktem Weg zum Produktverantwortlichen), S. 65 („Nachweis“ als authentisches Protokoll), S. 18 („Aktionsclearing“: Kontroll- oder Sperrnachweis als Auslöser)
- [Q39](../../QUELLEN.md#q39) – RMV vHGS-Vertrag (`TXSNAWA` und `TXSNAWB` als Sperrnachweise vom Dienstleister an den Kundenvertragspartner) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
