---
titel: Kontrollgerät
englisch: inspection device
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/sichtkontrolle.md, lexikon/rollen/akzeptanzterminal.md]
quellen: [Q02, Q06, Q16, Q20, Q33]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Kontrollgerät
<!-- /GEN:breadcrumb -->

# Kontrollgerät

Ein Kontrollgerät ist eine Ausprägung des [Akzeptanzterminals](../rollen/akzeptanzterminal.md). Das Glossar führt in der Aufzählung der Gerätearten „**mobile Geräte für die Kontrolle und/oder Entwertung von Tickets**“ ([Q02](../../QUELLEN.md#q02), S. 22).

Welche Prüfungen ein Gerät durchführen können muss, ergibt sich aus den vier Voraussetzungen der [Kontrolle](../kontrolle.md) ([Q02](../../QUELLEN.md#q02), S. 52) — und aus der Frage, ob es ein **SAM** besitzt: Ohne SAM sind keine kryptographischen Prüfungen und keine Transaktionen mit dem Nutzermedium möglich ([Q06](../../QUELLEN.md#q06), Kap. 6.1), siehe [Sichtkontrolle](sichtkontrolle.md).

**Geräteverwaltung** im Hintergrundsystem ([Q06](../../QUELLEN.md#q06), Kap. 6.1) · *verbundspezifisch*: Für jede Geräteart wird ein eigener **Gerätetypcode** eingerichtet; je Gerätetyp können beliebig viele Geräte mit individueller **Geräte-ID** angelegt werden. Die Geräte-ID setzt sich zusammen aus **Org-ID des Unternehmens + Gerätetypcode + Nummer**. Dieselbe Device-ID dient dem Hintergrundsystem zur Mandantenzuordnung — nicht die Sender- und Empfängerattribute des `TX_BASE` ([Q06](../../QUELLEN.md#q06), Kap. 2.1.2).

**Grenze der automatischen Prüfung:** „Nach aktuellem Stand können nur Tickets nach VDV-KA per PKM-Kontrollmodul automatisiert geprüft werden, keine UIC-Tickets.“ ([Q33](../../QUELLEN.md#q33), Kap. 7.1) · *produktbezogen* Ein Kontrollgerät im Deutschlandticket-Umfeld muss daher mehrere Ticketwelten unterscheiden (abgeleitet).

Zur Marktpraxis — Handgeräte und Anwendungsfälle — siehe [Q20](../../QUELLEN.md#q20) und [Q16](../../QUELLEN.md#q16) · *Herstellerquellen, belegen nicht den Standard*.

## Einfach erklärt – Beispiel aus Bärstadt

Ein Kontrollgerät ist im Modell der VDV-KA nichts Besonderes: Es ist ein Akzeptanzterminal wie der Automat am Hauptbahnhof, nur mobil und auf Prüfen statt Verkaufen ausgelegt.

Petra Pranke hat zwei davon im Dienst, und der Unterschied zwischen ihnen ist lehrreich.

Ihr **Gerät T-4713** hat einen Sicherheitsbaustein. Es prüft Echtheit, kann eine Karte sperren und hinterlässt einen Kontrollnachweis. Das volle Programm.

Ihr **Gerät T-4714** hat keinen. Es liest, zeigt an, vergleicht mit der Sperrliste — und das ist alles.

Beide stehen in derselben Geräteverwaltung, und die ist bemerkenswert systematisch aufgebaut. Jede Geräte-ID besteht aus drei Teilen: der Organisations-ID der Bärstädter Verkehrsbetriebe, einem Code für die Geräteart, und einer laufenden Nummer.

Das klingt bürokratisch, löst aber ein echtes Problem. Das Hintergrundsystem bedient viele Unternehmen gleichzeitig. Wenn ein Gerät anklopft, muss sofort klar sein, wessen Gerät es ist — und zwar bevor irgendeine Nachricht gelesen wird. Deshalb hängt die Zuordnung an der Geräte-ID und nicht an Angaben im Nachrichtenkopf.

Für Petras Alltag ist eine andere Einschränkung wichtiger. Ihr Gerät kann VDV-KA-Tickets automatisch prüfen — bei UIC-Tickets der Bahn geht das derzeit nicht. Trifft sie jemanden mit einem Deutschlandticket in der Bahn-App, bleibt ihr der Blick auf den Bildschirm und das eigene Urteil.

Das ist der unspektakuläre Grund, warum Kontrolle in der Praxis so viel schwieriger ist als in der Spezifikation: Es gibt nicht ein Ticketformat, sondern mehrere — und nicht jedes Gerät versteht jedes.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 22 (mobile Geräte für die Kontrolle und/oder Entwertung als Geräteart des Akzeptanzterminals), S. 52 (die vier Voraussetzungen der Kontrolle)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 6.1 (eigener Gerätetypcode je Geräteart; beliebig viele Geräte je Typ mit individueller Geräte-ID aus Org-ID, Gerätetypcode und Nummer; kein SAM, daher keine kryptographischen Prüfungen), Kap. 2.1.2 (Mandantenzuordnung im Hintergrundsystem über die Device-ID, nicht über die `TX_BASE`-Attribute) · *verbundspezifisch: eTicket RheinMain*
- [Q33](../../QUELLEN.md#q33) – KCD NRW, Ergebnisdokument der Arbeitsgruppe Kontrolle, V1.3, Kap. 7.1 (automatisierte Prüfung per PKM-Kontrollmodul nur für VDV-KA-Tickets, nicht für UIC-Tickets) · *produktbezogen auf das Deutschlandticket*
- [Q20](../../QUELLEN.md#q20) – Genfare, Hand Held Validator · *Herstellerquelle*
- [Q16](../../QUELLEN.md#q16) – amcon, Customers & Use Cases · *Herstellerquelle*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
