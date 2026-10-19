---
titel: Keymanagement
abkuerzung: KM
englisch: Key Management
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/schluesselarten.md, lexikon/berechtigungen/multiberechtigung.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › Keymanagement
<!-- /GEN:breadcrumb -->

# Keymanagement

„Keymanagement betrifft den gesamten Umgang mit kryptografischen Schlüsseln, also die **Erzeugung, die Verteilung, die Verwaltung, die Speicherung und die Ersetzung** von kryptografischen Schlüsseln.“ ([Q02](../../QUELLEN.md#q02), S. 51)

Die Aufgaben werden in Deutschland durch den **Scheme Manager** sichergestellt und von einer zentralen Instanz, der Unterrolle des Sicherheitsmanagers, übernommen ([Q02](../../QUELLEN.md#q02), S. 51). Zentrales Service- und Verwaltungssystem ist das **ASM**, das Applikations- und Sicherheitsmanagement — es verantwortet unter anderem die „Bestellung von Sicherheitskomponenten, Bestellbearbeitung und -prüfung“ und ist für KA 1.X über das ASM-Tool erreichbar ([Q02](../../QUELLEN.md#q02), S. 25).

**Das Schlüsselregister auf dem Medium.** Es ist „eine besondere Funktion der Applikation auf dem Nutzermedium“ und wird „bereits bei der Ausgabe der Applikation mit fertigen, authentischen Schlüsseln gefüllt“. Die Schlüssel hängen „von der Instanz-ID der Applikation ab, **nicht** von einer individuellen Berechtigungs-ID“. Bei der Ausgabe einer Berechtigung werden nur noch die **Schlüsselreferenzen** auf die vorhandenen Schlüssel eingetragen; passende Schlüssel lassen sich dadurch „wiederverwenden“, was „die kryptographischen Prozesse zwischen Nutzermedium und Terminal für die Ausgabe einer Berechtigung **erheblich beschleunigt**“ ([Q02](../../QUELLEN.md#q02), S. 79 f.).

Damit erklärt sich der Titel der [Multiberechtigungs](../berechtigungen/multiberechtigung.md)-Spezifikation, „Performanceverbesserung bei der EFS-Ausgabe“ (abgeleitet).

**Zwei Änderungen in etiCORE** ([Q02](../../QUELLEN.md#q02), S. 52, S. 80): Die Schlüsselverwaltung für symmetrische Schlüssel in den Teilnehmersystemen von Produktverantwortlichem und Kundenvertragspartner **entfällt**. Das Schlüsselregister in dieser Form wird nicht mehr benötigt; für die Authentisierung tritt ein **Symmetric Key Directory** an seine Stelle.

Operativ läuft das Nachladen über `TXSYMKEYL` und `TXSYMKEYACK` ([Q06](../../QUELLEN.md#q06), Kap. 4.6, 4.9); Normquellen sind KA SEC-SPEC und KA SAM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3).

## Einfach erklärt – Beispiel aus Bärstadt

Keymanagement ist die unspektakulärste und aufwendigste Seite der Sicherheit: Schlüssel erzeugen, verteilen, verwalten, speichern, austauschen.

Das Besondere an der VDV-KA ist, dass dieser Aufwand **zentral** gebündelt wird. Nicht jedes Verkehrsunternehmen bastelt sich seine Schlüsselwelt; es gibt eine zentrale Stelle beim Scheme Manager und ein zentrales System, über das Sicherheitskomponenten bestellt und geprüft werden.

Für die Bärstädter Verkehrsbetriebe ist das eine Erleichterung. Sie bestellen SAMs und bekommen Schlüssel — sie müssen keine Kryptografie-Abteilung aufbauen.

Nun zu einem Mechanismus, der ein hübsches Stück Ingenieurskunst ist: dem **Schlüsselregister**.

Das Problem: Kryptografie auf einer Chipkarte ist langsam. Müsste das Terminal bei jeder Ausgabe einer Berechtigung erst neue Schlüssel aushandeln, würde das Schreiben spürbar dauern — und Pia steht an der Haltestelle.

Die Lösung: Die Schlüssel werden **vorab** auf die Karte gebracht, nämlich schon bei der Ausgabe der Karte selbst. Sie hängen an der Karte, nicht an einer einzelnen Berechtigung. Wird später ein Abo geschrieben, wird kein neuer Schlüssel erzeugt — es wird nur noch notiert, welcher der vorhandenen zu verwenden ist.

Vorbereitung statt Rechenarbeit im entscheidenden Moment. Das Glossar nennt die Wirkung „eine erhebliche Beschleunigung".

Und hier schließt sich ein Kreis zu einem früheren Artikel: Die Spezifikation für Multiberechtigungen heißt „Performanceverbesserung bei der EFS-Ausgabe". Jetzt weiß man, worin diese Verbesserung besteht.

In der neuen Generation wird das überflüssig — die kryptografischen Prozesse sind schnell genug.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 51 f. („Keymanagement“: Erzeugung, Verteilung, Verwaltung, Speicherung und Ersetzung; Sicherstellung durch den Scheme Manager über die Unterrolle des Sicherheitsmanagers; Wegfall der Schlüsselverwaltung für symmetrische Schlüssel in den Teilnehmersystemen von PV und KVP in etiCORE; Abkürzung KM), S. 25 („Applikations- und Sicherheitsmanagement“ als zentrales Service- und Verwaltungssystem, Bestellung und Prüfung von Sicherheitskomponenten, ASM-Tool für KA 1.X), S. 79 f. („Schlüsselregister“: Funktion der Applikation auf dem Nutzermedium, Füllung bei der Ausgabe der Applikation, Abhängigkeit von der Instanz-ID statt der Berechtigungs-ID, Eintragung von Schlüsselreferenzen, Wiederverwendung und erhebliche Beschleunigung, Entbehrlichkeit ab etiCORE, Symmetric Key Directory für die Authentisierung)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.6 und 4.9 (`TXSYMKEYL` und `TXSYMKEYACK`), Kap. 2.1.7 (Schlüsselmanagement) · *verbundspezifisch*
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SEC-SPEC Inv. 6, KA SAM-SPEC Inv. 8)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Schlüsselarten](schluesselarten.md)
- [Multiberechtigung](../berechtigungen/multiberechtigung.md) (MultiBER)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
