---
titel: Secure Application Module
abkuerzung: SAM
englisch: Secure Application Module
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/mac.md, lexikon/kontrolle/sichtkontrolle.md]
quellen: [Q02, Q06, Q12, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Secure Application Module
<!-- /GEN:breadcrumb -->

# Secure Application Module

Das Secure Application Module „wird als Sicherheitsmodul für Kundenvertragspartner und Dienstleister genutzt. Es führt die **sicherheitsrelevanten Funktionen der Akzeptanzterminals** aus, die direkt mit dem Nutzermedium kommunizieren.“ ([Q02](../../QUELLEN.md#q02), S. 80)

In der KA kann es zusätzlich **in den Hintergrundsystemen** des Kundenvertragspartners, des Produktverantwortlichen und des Scheme Manager verwendet werden, „um die vom Nutzermedium erzeugten Signaturen zu prüfen“ ([Q02](../../QUELLEN.md#q02), S. 80).

Das SAM ist damit die Stelle, an der kryptografische Geheimnisse liegen (abgeleitet). Daraus folgen drei belegte Konsequenzen:

- **Eine [Transaktion](../transaktionen/transaktion.md) findet ausschließlich zwischen Nutzermedium und Akzeptanzterminal unter Mithilfe eines SAM statt** ([Q02](../../QUELLEN.md#q02), S. 96).
- Ohne SAM „erfolgen keine kryptographischen Prüfungen des KA-Nutzermediums und der KA-Berechtigungen und es können keine Transaktionen mit dem Nutzermedium durchgeführt werden“ ([Q06](../../QUELLEN.md#q06), Kap. 6.1) — siehe [Sichtkontrolle](../kontrolle/sichtkontrolle.md).
- SAMs sind **sperrbar**: Der Sperrlistenservice führt Sperreinträge für SAMs ([Q02](../../QUELLEN.md#q02), S. 54).

**Verwaltung:** Das Dienstleister-System muss die SAMs verwalten ([Q02](../../QUELLEN.md#q02), S. 34). Der Nachschub läuft über eigene Nachrichten — `TXSYMKEYL` mit Kryptogrammen der zu ladenden symmetrischen Schlüssel (`IONTransaktionsTyp_CODE` 252), `TXSYMKEYACK` als Bestätigung, „dass ein Kryptogramm in ein SAM geladen wurde“ (253), und `TXCVCERTL` für Zertifikate (254) ([Q06](../../QUELLEN.md#q06), Kap. 4.6, 4.7, 4.9) · *verbundspezifisch*. Die `SAM_ID.samNummer` ist 3 Byte lang und wird bei der Bestellung über das ASM-Tool vergeben ([Q12](../../QUELLEN.md#q12)).

**Die große Verschiebung:** „In etiCORE erfolgt die Signaturprüfung mit asymmetrischer Kryptographie **ohne SAMs**.“ ([Q02](../../QUELLEN.md#q02), S. 80)

## Einfach erklärt – Beispiel aus Bärstadt

Das SAM ist ein kleiner Chip mit einer großen Aufgabe: Es hütet die Geheimnisse.

Es steckt im Lesegerät am Hauptbahnhof, im Automaten und in Petra Prankes Prüfgerät. Wenn eines dieser Geräte etwas auf Pias Karte schreiben oder ein Siegel prüfen will, kann es das nicht selbst — es fragt das SAM. Die Schlüssel verlassen den Baustein nie.

Das ist dieselbe Idee wie bei einer Bankkarte: Der Chip rechnet mit dem Geheimnis, gibt es aber nicht heraus. Selbst wer das Gerät aufschraubt, kommt an die Schlüssel nicht heran.

Daraus folgt ein Satz, der in diesem Lexikon immer wieder auftaucht: **Ohne SAM geht kryptografisch nichts.** Ein Smartphone ohne Sicherheitsbaustein kann Pias Abo lesen und anzeigen — aber es kann nicht prüfen, ob es echt ist, und es kann nichts schreiben.

Das SAM ist auch ein logistischer Gegenstand. Es wird bestellt, geliefert, in Geräte eingebaut, mit Schlüsseln bestückt und kann **gesperrt** werden. Für das Nachladen von Schlüsseln und Zertifikaten gibt es eigene Nachrichtentypen, und jedes SAM hat eine Nummer, die bei der Bestellung vergeben wird.

Für die Bärstädter Verkehrsbetriebe heißt das: Jedes Gerät mit SAM ist ein verwaltetes Objekt mit eigenem Lebenszyklus. Das ist ein guter Teil des Aufwands beim Betrieb eines KA-Systems.

Und nun der Satz, der diese ganze Welt in Frage stellt: In der neuen Generation erfolgt die Signaturprüfung asymmetrisch — **ohne SAM.**

Damit verliert der Baustein seine Monopolstellung. Geräte werden billiger, Kontrolle mit gewöhnlichen Smartphones wird möglich, und ein ganzer Verwaltungszweig schrumpft. Wer heute über Gerätebeschaffung entscheidet, sollte dieses Datum kennen.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 80 („Secure Application Module“: Sicherheitsmodul für KVP und DL, Ausführung der sicherheitsrelevanten Funktionen der Akzeptanzterminals, Einsatz in den Hintergrundsystemen zur Signaturprüfung, Signaturprüfung in etiCORE ohne SAMs), S. 96 (Transaktion ausschließlich zwischen Nutzermedium und Akzeptanzterminal unter Mithilfe eines SAM), S. 54 (Sperreinträge für SAMs), S. 34 (SAM-Verwaltung im Dienstleister-System)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.6 (`TXSYMKEYL`, `IONTransaktionsTyp_CODE` 252), Kap. 4.7 (`TXCVCERTL`, 254), Kap. 4.9 (`TXSYMKEYACK`, 253, als Bestätigung des Ladens eines Kryptogramms in ein SAM), Kap. 6.1 (ohne SAM keine kryptographischen Prüfungen und keine Transaktionen) · *verbundspezifisch*
- [Q12](../../QUELLEN.md#q12) – TapConnect, VDV Barcode Field Mappings (`SAM_ID.samNummer` mit 3 Byte, Vergabe im Bestellprozess über das ASM-Tool; Verweise auf KA SAM-Spec_V190 S. 205 und KA NM-SPEC_V190 S. 199) · *Herstellerquelle*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SAM-SPEC Inv. 8, KA SAM-Server-SPEC Inv. 59)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
