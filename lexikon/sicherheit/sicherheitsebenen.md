---
titel: Sicherheitsebenen
englisch: security levels
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/pki.md, lexikon/grundlagen/versionen.md]
quellen: [Q02, Q42]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Sicherheitsebenen
<!-- /GEN:breadcrumb -->

# Sicherheitsebenen

Zwei Einteilungen tragen ähnliche Namen und bedeuten Verschiedenes. Sie auseinanderzuhalten ist der Zweck dieses Artikels.

**Die Sicherheitsebenen (Level 1 bis 3)** sind Umgebungen ([Q02](../../QUELLEN.md#q02), S. 62 f.):

| Ebene | Bedeutung |
|---|---|
| **Level 1** | Development Environment |
| **Level 2** | Staging Environment — „hier sind alle Sicherheitskomponenten zur durchgängigen Sicherung der Teilnehmerinteressen geschützt und nicht für Dritte zugänglich“ |
| **Level 3** | Production Environment — „dem Wirkbetrieb vorbehalten“ |

Für Level 3 gilt eine strenge Regel: „Im Wirkbetrieb des eTicket Deutschland werden **ausschließlich** Wertobjekte verwendet und anerkannt, die mit **Level-3-Organisations-IDs** erstellt wurden. Für den etiCORE-Standard dürfen zusammen mit den Level-3-Organisations-IDs **nur Level-3-Zertifikate** verwendet werden.“ ([Q02](../../QUELLEN.md#q02), S. 63)

Die Trennung reicht also bis in die [Organisations-ID](../rollen/organisations-id.md) hinein: Eine Test-ID kann im Wirkbetrieb nichts Gültiges erzeugen (abgeleitet).

**Die Generationen (1GSI und 2GSI)** sind dagegen Technikstände ([Q02](../../QUELLEN.md#q02), S. 14 f.):

- **1GSI** ist die „erste Generation der Sicherheitsinfrastruktur, heutige Variante bis 2026 bzw. 2031“. Sie umfasst Algorithmen und Schlüssel in Nutzermedium und SAM „im definierten Format von 2006“ sowie die Schlüsselverwaltung und PKI, „welche seit 2006 im Einsatz ist“.
- **2GSI** ist die zweite Generation, „Variante ab 2026“.

Die Daten dazu sind belegt: neues Root-Zertifikat zur Einführung von etiCORE am **1. Dezember 2026**, SubCA-Zertifikate der 1GSI gültig bis **1. Dezember 2031**, dazwischen Parallelbetrieb ([Q42](../../QUELLEN.md#q42)) — siehe [PKI](pki.md) und [Versionen](../grundlagen/versionen.md).

Die Ebenen gelten in jeder Generation; die Generation wechselt, die Dreiteilung bleibt (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

„Sicherheitsebene" und „Sicherheitsgeneration" klingen verwandt und sind völlig verschiedene Dinge. Die Verwechslung führt zu absurden Sätzen wie „wir sind auf Level 2, müssen aber auf 2GSI".

**Die Ebenen sind Umgebungen.** Wie überall in der Softwareentwicklung: eine zum Entwickeln, eine zum Testen, eine für den Echtbetrieb.

Bemerkenswert ist, wie konsequent die Trennung durchgezogen wird. Sie steckt nicht nur in getrennten Servern, sondern in den **Organisations-IDs** selbst. Es gibt Test-IDs und es gibt Echt-IDs, und im Wirkbetrieb werden ausschließlich Dinge anerkannt, die mit einer Echt-ID erzeugt wurden.

Das verhindert einen Unfall, den man sich leicht vorstellen kann. Hätten die Bärstädter Verkehrsbetriebe beim Test versehentlich echte Abos erzeugt, wären sie wertlos — sie tragen eine Test-ID und werden im Wirkbetrieb nicht anerkannt. Umgekehrt kann niemand im Testsystem etwas erzeugen, das draußen gilt.

Für jeden, der mit echten Datensätzen arbeitet, ist das eine nützliche Information: Die Organisations-ID verrät, aus welcher Welt ein Datensatz kommt.

**Die Generationen sind Technikstände.** Die erste stammt aus dem Jahr 2006 — Algorithmen, Schlüsselformate und PKI sind zwanzig Jahre alt. Das ist für Kryptografie eine lange Zeit, und deshalb kommt die zweite Generation.

Deren Datum ist nah: **1. Dezember 2026.** Dann gibt es ein neues Wurzelzertifikat, und die alte Welt läuft noch fünf Jahre parallel weiter, bis Dezember 2031.

Für Bärstadt heißt das: Ein System, das 2026 gebaut wird, muss beide Generationen beherrschen. Nicht als Übergangslösung, sondern fünf Jahre lang.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 62 f. („Level-1 Development Environment“, „Level-2 Staging Environment“ mit dem Schutz aller Sicherheitskomponenten, „Level-3 Production Environment“ als dem Wirkbetrieb vorbehalten; ausschließliche Verwendung und Anerkennung von Wertobjekten mit Level-3-Organisations-IDs im Wirkbetrieb; für etiCORE nur Level-3-Zertifikate zusammen mit Level-3-Organisations-IDs), S. 14 f. („1GSI“ als erste Generation der Sicherheitsinfrastruktur mit Algorithmen und Schlüsseln im Format von 2006 und seit 2006 eingesetzter Schlüsselverwaltung und PKI, heutige Variante bis 2026 bzw. 2031; „2GSI“ als zweite Generation ab 2026), S. 81 („Sicherheitsebenen / Security Levels“: drei Sicherheitsebenen in der Sicherheitsarchitektur)
- [Q42](../../QUELLEN.md#q42) – KCD NRW, Newsletterarchiv (neues Root-Zertifikat zur Einführung von etiCORE am 01.12.2026, SubCA-Gültigkeit bis 01.12.2031, Parallelbetrieb im Übergangszeitraum) · *Sekundärquelle*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Public Key Infrastructure](pki.md) (PKI)
- [Versionen](../grundlagen/versionen.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
