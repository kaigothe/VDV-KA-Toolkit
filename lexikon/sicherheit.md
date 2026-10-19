---
titel: Sicherheit
englisch: security and keys
parent: README.md
siehe_auch: [lexikon/grundlagen/versionen.md, lexikon/kontrolle.md]
quellen: [Q02, Q06, Q25, Q42]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../README.md) › Sicherheit
<!-- /GEN:breadcrumb -->

# Sicherheit

Die Sicherheit der VDV-KA ruht auf zwei Säulen, die sauber getrennt sind.

**Symmetrische Verfahren** sichern das Geschehen am Nutzermedium. Mit symmetrischen Schlüsseln werden in KA 1.X sowohl die gegenseitige Authentifizierung von Komponenten als auch der authentische Nachweis von Berechtigungsausgaben und Bezahlvorgängen abgewickelt ([Q02](../QUELLEN.md#q02), S. 92). Praktisch heißt das: [MAC](sicherheit/mac.md)-Bildung durch ein [SAM](sicherheit/sam.md), referenziert über [Schlüsselreferenzen](sicherheit/schluesselreferenz.md).

**Asymmetrische Verfahren** sichern die Infrastruktur. In ihrem Umfeld arbeitet die [PKI](sicherheit/pki.md), „ein System, das digitale Zertifikate ausstellen, verteilen und prüfen kann“ ([Q02](../QUELLEN.md#q02), S. 71). Die KA verwendet dafür [CV-Zertifikate](sicherheit/cv-zertifikat.md) mit sieben Schlüsseltypen ([Q06](../QUELLEN.md#q06), Kap. 4.7).

Verwaltet wird das Ganze durch das [Keymanagement](sicherheit/keymanagement.md) — „der gesamte Umgang mit kryptografischen Schlüsseln, also die Erzeugung, die Verteilung, die Verwaltung, die Speicherung und die Ersetzung“ ([Q02](../QUELLEN.md#q02), S. 51) — mit dem **ASM** als zentralem Service- und Verwaltungssystem ([Q02](../QUELLEN.md#q02), S. 25).

Darüber liegen zwei unabhängige Einteilungen, die man nicht verwechseln darf ([Sicherheitsebenen](sicherheit/sicherheitsebenen.md)):

| Einteilung | Bedeutung |
|---|---|
| **Level 1, 2, 3** | Entwicklungs-, Test- und Wirkbetriebsumgebung ([Q02](../QUELLEN.md#q02), S. 62 f.) |
| **1GSI, 2GSI** | Generationen der Sicherheitsinfrastruktur, mit Übergang zum 1. Dezember 2026 ([Q02](../QUELLEN.md#q02), S. 14 f.; [Q42](../QUELLEN.md#q42)) |

**Die große Verschiebung:** In etiCORE erfolgt die Signaturprüfung „mit asymmetrischer Kryptographie **ohne SAMs**“ ([Q02](../QUELLEN.md#q02), S. 80). Das SAM verliert damit seine zentrale Stellung (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Bei der Sicherheit der VDV-KA hilft es, zwei Welten auseinanderzuhalten — sie arbeiten mit verschiedenen Verfahren und lösen verschiedene Probleme.

**Die erste Welt ist die Karte.** Wenn das Lesegerät am Hauptbahnhof Pias Abo schreibt, muss hinterher beweisbar sein, dass die Daten echt sind. Dafür wird eine Art Prüfsiegel berechnet — ein MAC. Beide Seiten kennen dasselbe Geheimnis, deshalb heißt es symmetrisch. Das Geheimnis steckt im Sicherheitsbaustein des Terminals, dem SAM.

Symmetrische Verfahren sind schnell, und das ist hier entscheidend: Pia hält die Karte eine Sekunde hin.

**Die zweite Welt ist die Infrastruktur.** Hier geht es nicht um eine Karte, sondern um Vertrauen zwischen Organisationen. Wie weiß ein Gerät in Bärstadt, dass ein Schlüssel aus Luchsstadt echt ist? Nicht über ein gemeinsames Geheimnis — es gibt keines. Sondern über **Zertifikate**: Eine übergeordnete Stelle bestätigt mit ihrer Signatur, dass ein Schlüssel zu wem gehört.

Dafür braucht man asymmetrische Verfahren mit Schlüsselpaaren, und das Ganze heißt PKI.

Der Unterschied in einem Bild: Das Siegel auf der Karte beweist, dass dieser Fahrschein echt ist. Das Zertifikat beweist, dass dieses Unternehmen dazugehört.

Nun zwei Nummerierungen, die regelmäßig verwechselt werden. **Level 1, 2, 3** sind Umgebungen — Entwicklung, Test, Wirkbetrieb. **1GSI und 2GSI** sind Generationen der Sicherheitstechnik, und der Wechsel steht unmittelbar an.

Und eine Entwicklung, die Beschaffungen betrifft: In der neuen Generation wird die Signaturprüfung asymmetrisch — **ohne SAM**. Der Baustein, der heute in jedem Terminal steckt und die Geräte teuer macht, verliert seine zentrale Rolle.

## Quellen

- [Q02](../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 92 („Symmetrischer Schlüssel“: Verwendung in KA 1.X für gegenseitige Authentifizierung und authentischen Nachweis), S. 71 („Public Key Infrastructure“), S. 51 („Keymanagement“), S. 25 („Applikations- und Sicherheitsmanagement“ als zentrales Service- und Verwaltungssystem), S. 80 („Secure Application Module“; Signaturprüfung in etiCORE ohne SAMs), S. 62 f. (Level-1- bis Level-3-Umgebungen), S. 14 f. (1GSI und 2GSI)
- [Q06](../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.7 (CV-Zertifikate mit sieben Keytypes), Kap. 3.1 und 5.1.2 (MAC-Prüfung) · *verbundspezifisch*
- [Q42](../QUELLEN.md#q42) – KCD NRW, Newsletterarchiv (Root- und SubCA-Zertifikate, Übergang 1GSI zu 2GSI) · *Sekundärquelle*
- [Q25](../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SEC-SPEC Inv. 6, KA SAM-SPEC Inv. 8)

<!-- GEN:unterartikel -->
## Unterartikel

- [CV-Zertifikat](sicherheit/cv-zertifikat.md)
- [Keymanagement](sicherheit/keymanagement.md)
- [MAC](sicherheit/mac.md)
- [Public Key Infrastructure](sicherheit/pki.md)
- [Schlüsselarten](sicherheit/schluesselarten.md)
- [Schlüsselreferenz](sicherheit/schluesselreferenz.md)
- [Secure Application Module](sicherheit/sam.md)
- [Sicherheitsebenen](sicherheit/sicherheitsebenen.md)
<!-- /GEN:unterartikel -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../README.md) · [Register](../REGISTER.md)
<!-- /GEN:navigation -->
