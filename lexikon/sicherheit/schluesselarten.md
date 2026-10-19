---
titel: Schlüsselarten
englisch: key types
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/keymanagement.md, lexikon/sicherheit/pki.md]
quellen: [Q02]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Schlüsselarten
<!-- /GEN:breadcrumb -->

# Schlüsselarten

Die VDV-KA verwendet beide Grundformen der Kryptografie, mit klarer Arbeitsteilung.

**Symmetrisch:** „Der gleiche geheime Schlüssel wird von beiden Kommunikationspartnern sowohl für die Verschlüsselung als auch für die Entschlüsselung verwendet.“ In KA 1.X werden symmetrische Schlüssel sowohl für die **gegenseitige Authentifizierung von Komponenten** — diese Schlüssel kommen vom Scheme Manager — als auch für den **authentischen Nachweis von Berechtigungsausgaben und Bezahlvorgängen** verwendet; letztere kommen von Produktverantwortlichem und Kundenvertragspartner ([Q02](../../QUELLEN.md#q02), S. 92).

Um bei einer Kompromittierung schnell reagieren zu können, arbeitet KA 1.X mit **Regulärversion und Notfallversion** der Schlüssel ([Q02](../../QUELLEN.md#q02), S. 92). Notfallversionen begrenzen Ausfälle und finanzielle Schäden; dazu werden neben den regulären Schlüsseln auch Notschlüssel in der Applikation gespeichert, auf die im Betrieb umgeschaltet werden kann. **Ab etiCORE entfällt der Begriff**, weil ein anderer Mechanismus verwendet wird ([Q02](../../QUELLEN.md#q02), S. 65).

**Asymmetrisch:** Hier gehören ein [öffentlicher und ein privater Schlüssel](pki.md) zusammen ([Q02](../../QUELLEN.md#q02), S. 25, S. 68, S. 73). In diesem Umfeld arbeitet die PKI ([Q02](../../QUELLEN.md#q02), S. 71).

**Abgeleitete Schlüssel:** Bei einer gegenseitigen Authentifizierung kann ein gemeinsamer **Startkey** vereinbart werden; daraus lassen sich dynamisch weitere Schlüssel — **Session Keys** — ableiten, die dann zur Verschlüsselung oder MAC-Bildung und -Prüfung dienen ([Q02](../../QUELLEN.md#q02), S. 91).

Das erklärt die Benennung der [Schlüsselreferenzen](schluesselreferenz.md) mit `MK` für Masterkey und `K` für den abgeleiteten Schlüssel (abgeleitet).

Eine Sonderform auf mobilen Geräten ist die **Secure Crypto Environment**: eine logische Komponente, die Schlüssel empfangen oder erzeugen und „unveränderlich an das mobile Gerät und eine Ticketing-App binden“ kann; sie muss gegen Auslesen und Kopieren resistent sein ([Q02](../../QUELLEN.md#q02), S. 81).

## Einfach erklärt – Beispiel aus Bärstadt

Es gibt zwei Arten von Schlüsseln, und die VDV-KA nutzt beide — für verschiedene Zwecke.

**Symmetrisch** heißt: beide Seiten haben dasselbe Geheimnis. Wie ein Haustürschlüssel, den zwei Leute besitzen. Das ist schnell, und Geschwindigkeit ist der Grund, warum die Karte damit arbeitet: Pia hält sie eine Sekunde hin.

Der Nachteil liegt auf der Hand. Wer dasselbe Geheimnis verteilt, muss es gut hüten — und es jedem geben, der mitspielen soll.

**Asymmetrisch** heißt: zwei verschiedene Schlüssel, die zusammengehören. Einer darf öffentlich sein, der andere bleibt geheim. Damit kann man Dinge bestätigen, ohne ein Geheimnis zu teilen — die Grundlage für Zertifikate.

Das ist langsamer, aber es löst das Problem, das symmetrische Verfahren nicht lösen können: Vertrauen zwischen Fremden.

Nun ein Mechanismus, der mir besonders gut gefällt, weil er ein echtes Betriebsproblem löst. Was tut man, wenn ein Schlüssel kompromittiert wird? Alle Karten einsammeln?

Die VDV-KA hat das vorhergesehen. Auf jeder Karte liegen neben den regulären Schlüsseln auch **Notschlüssel**. Wird ein Schlüssel kompromittiert, schaltet man im laufenden Betrieb um — die Karten sind vorbereitet.

Für die Bärstädter Verkehrsbetriebe heißt das: Ein kompromittierter Schlüssel wäre ein Zwischenfall, aber kein Weltuntergang. Niemand müsste zehntausend BärenKarten austauschen.

Und eine letzte Feinheit: Aus einem Startschlüssel lassen sich für jede einzelne Sitzung neue Schlüssel ableiten. Selbst wenn jemand einen davon abfängt, hat er damit nur eine Sitzung — nicht das Grundgeheimnis.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 92 („Symmetrischer Schlüssel“: gleicher geheimer Schlüssel für Ver- und Entschlüsselung, Verwendung in KA 1.X für gegenseitige Authentifizierung mit Schlüsseln vom Scheme Manager und für den authentischen Nachweis von Berechtigungsausgaben und Bezahlvorgängen mit Schlüsseln von PV und KVP, Regulär- und Notfallversion), S. 65 („Notfallversion“: Begrenzung von Ausfällen und finanziellen Schäden, Speicherung von Notschlüsseln in der Applikation, Umschalten im Betrieb, Wegfall des Begriffs ab etiCORE), S. 25 („Asymmetrische Kryptographie“), S. 68 („Öffentlicher Schlüssel“), S. 73 („Privater Schlüssel“), S. 71 („Public Key Infrastructure“), S. 91 („Start Key / Session Key“: Vereinbarung eines gemeinsamen Startkeys und dynamische Ableitung von Session Keys für Verschlüsselung und MAC-Bildung bzw. -Prüfung), S. 81 („Secure Crypto Environment“: logische Komponente auf dem mobilen Gerät, unveränderliche Bindung der Schlüssel an Gerät und Ticketing-App, Resistenz gegen Auslesen und Kopieren)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
