---
titel: Aktionsfreigabe
englisch: action release
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktion.md, lexikon/aktionsmanagement/aktionsliste.md]
quellen: [Q02, Q25]
status: zu prüfen
offene_fragen: [O12]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktionsfreigabe
<!-- /GEN:breadcrumb -->

# Aktionsfreigabe

Die Aktionsfreigabe ist ein Schritt im Aktionsmanagement, der neben Beauftragung und Ausführung steht. Belegt ist bislang nur, **dass** es ihn gibt, nicht was er genau bewirkt (zu prüfen, O12).

Das eTicket-Regelwerk führt für das Kundenvertragspartner-System im Paket Aktionsmanagement zwei Anwendungsfälle: „Aktionsfreigabe senden“ und „Aktionsfreigabemitteilung entgegennehmen“ ([Q25](../../QUELLEN.md#q25), Anlage 2, Kap. 5.1.2, Tabelle 38).

Dass beide Richtungen aufgeführt sind — senden und entgegennehmen —, zeigt einen zweiseitigen Austausch zwischen Kundenvertragspartner und Produktverantwortlichem (abgeleitet).

Das Glossar [Q02](../../QUELLEN.md#q02) enthält **keinen** Eintrag „Aktionsfreigabe“; geprüft am Inhaltsverzeichnis, S. 2–13. Damit fehlt die begriffliche Definition des Standardgebers. Normquelle ist die nicht öffentliche KA AktM-SPEC ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 41).

Das in [Q02](../../QUELLEN.md#q02), S. 20 f., beschriebene Statusmodell der Aktion — „bestellt“, „aktiv“, „ausgeführt“ — nennt die Freigabe nicht. Sie ist also entweder ein Schritt innerhalb des Übergangs von „bestellt“ zu „aktiv“ oder ein davon unabhängiger Vorgang; beides ist aus den öffentlichen Quellen nicht zu entscheiden (zu prüfen, O12).

**Vor einer Verwendung in Entwurf oder Implementierung ist dieser Artikel zu verifizieren.**

## Einfach erklärt – Beispiel aus Bärstadt

Dieser Artikel ist ein Platzhalter mit Ansage — und das Beispiel soll zeigen, warum er trotzdem hier steht.

Bekannt ist: Im Aktionsmanagement gibt es einen Vorgang namens Aktionsfreigabe, und das Kundenvertragspartner-System kann eine solche Freigabe senden und eine Freigabemitteilung empfangen. Mehr sagen die öffentlichen Unterlagen nicht.

Was man daraus vorsichtig lesen kann: Zwischen „die BVB bestellt einen Auftrag“ und „der Auftrag steht in der Aktionsliste“ scheint es einen weiteren Handgriff zu geben. Dass es für beide Richtungen einen eigenen Anwendungsfall gibt, deutet auf ein Hin und Her hin — jemand gibt frei, jemand nimmt die Mitteilung darüber zur Kenntnis.

Man könnte sich das plausibel so vorstellen: Bodo Bärlauch erfasst Pias Abo-Auftrag heute, aber er soll erst zum Ausbildungsbeginn am 1. September wirksam werden. Eine Freigabe wäre der Schalter, der sagt: jetzt gilt er.

Das ist eine **Vermutung**, und es wäre falsch, sie in diesem Lexikon als Erklärung auszugeben. Eine Spezifikation, die nicht vorliegt, lässt sich nicht erraten — und bei einem Begriff, der zwischen zwei Organisationen etwas auslöst, wäre eine falsche Vorstellung besonders teuer.

Warum dann überhaupt ein Artikel? Weil die Lücke selbst eine nützliche Information ist. Wer eine Aktionsmanagement-Schnittstelle entwirft oder eine Nachricht auswertet und über diesen Begriff stolpert, soll hier sofort sehen: Das ist kein Nebenschauplatz, den man überlesen darf, sondern eine echte Wissenslücke mit einem Eintrag in der Liste der offenen Fragen.

Geklärt wird sie mit der KA AktM-SPEC — oder mit einer Rückfrage beim VDV eTicket Service.

## Quellen

- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Anlage 2 „KA Migrationsszenarien“ V1.6.0, Kap. 5.1.2, Tabelle 38 „Aktionsmanagement für das Kundenvertragspartner-System“ (Anlagenseite 95, PDF-S. 238): Anwendungsfälle „Aktionsfreigabe senden“ und „Aktionsfreigabemitteilung entgegennehmen“; Kap. 3 (KA AktM-SPEC, Inventarnummer 41)
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE: **kein** Eintrag „Aktionsfreigabe“ (geprüft am Inhaltsverzeichnis, S. 2–13); S. 20 f. zum Statusmodell der Aktion

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
