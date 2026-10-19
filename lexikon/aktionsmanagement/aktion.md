---
titel: Aktion
englisch: action
parent: lexikon/aktionsmanagement.md
siehe_auch: [lexikon/aktionsmanagement/aktionsliste.md]
quellen: [Q02]
status: belegt
offene_fragen: [O9]
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Aktionsmanagement](../aktionsmanagement.md) › Aktion
<!-- /GEN:breadcrumb -->

# Aktion

Eine Aktion bedeutet insbesondere im Kontext von (((etiCORE eine von einem Terminal getriggerte Handlung, die auf dem Nutzermedium mit Hilfe eines SAM durchgeführt wird ([Q02](../../QUELLEN.md#q02), S. 18).

Sie unterscheidet sich darin von einer **Transaktion**: Der Vorgang ist noch nicht zwingend beendet und bedarf einer zusätzlichen Betätigung für den Abschluss und damit einen potentiellen Schreibvorgang im Nutzermedium ([Q02](../../QUELLEN.md#q02), S. 18).

Das Glossar nennt ausdrücklich eine **zweite, abstrahierte Bedeutung**: Im Aktionsmanagement werden ebenfalls Aktionen verwaltet, die später auf einem Nutzermedium durchgeführt werden sollen ([Q02](../../QUELLEN.md#q02), S. 18). Das ist die im Lexikon meist gemeinte Lesart — der vorbereitete Auftrag in einer Aktionsliste.

Beide Bedeutungen tragen denselben Namen, und das Glossar trennt sie nicht durch zwei Begriffe (abgeleitet). Beim Lesen von Spezifikationen lohnt es sich deshalb zu prüfen, ob die Handlung am Medium oder der verwaltete Auftrag gemeint ist. Wie sich dazu „Aktionstyp“ und das Feld `amAuftragsTyp` verhalten, ist offen (zu prüfen, O9).

Aktionen unterliegen einem Lebenszyklus und müssen deshalb verwaltet werden ([Q02](../../QUELLEN.md#q02), S. 20). Sie sind zudem Bausteine größerer Abläufe: Ein Elementarprozess bezeichnet eine fachlich zusammenhängende Menge von Transaktionen, Aktionen, Nachrichten und Prüfungen ([Q02](../../QUELLEN.md#q02), S. 38).

## Einfach erklärt – Beispiel aus Bärstadt

Pia Brummbär hält ihre BärenKarte an das Lesegerät T-4712 am Hauptbahnhof. Was in dieser knappen Sekunde passiert, ist eine Aktion im engeren Sinn: Das Gerät spricht mit dem Chip in der Karte und nutzt dabei sein SAM, also den Sicherheitsbaustein, der die nötigen Schlüssel hält.

Wichtig ist der Unterschied zu einem abgeschlossenen Vorgang. Die Aktion ist nicht schon dadurch fertig, dass das Gerät angefangen hat. Sie braucht einen Abschluss — und erst der führt dazu, dass tatsächlich etwas auf die Karte geschrieben wird. Zieht Pia die Karte zu früh weg, ist die Handlung begonnen, aber nichts ist geschrieben.

Nun gibt es dasselbe Wort noch in einer zweiten, weiteren Bedeutung, und die begegnet einem im Alltag häufiger. Als die Bärstädter Verkehrsbetriebe beim Bären-Verkehrsbund hinterlegen „schreibe das ABO Azubi auf die Karte 90000042“, nennt man diesen Merkposten ebenfalls eine Aktion. Zu diesem Zeitpunkt war Pias Karte an keinem Gerät, und es wurde nichts geschrieben.

Man kann sich das wie eine Notiz am Kühlschrank vorstellen. „Milch kaufen“ ist eine Aktion in diesem weiteren Sinn: ein Vorhaben, das notiert ist und auf seine Gelegenheit wartet. Das tatsächliche Zugreifen im Laden ist die Aktion im engeren Sinn.

Beide Bedeutungen heißen gleich, weil sie dasselbe Vorhaben in zwei Lebensphasen beschreiben: einmal als Plan, einmal als Vollzug. Wenn in einem Dokument von einer Aktion die Rede ist, ist es deshalb immer eine gute Frage, ob gerade die Notiz oder der Griff ins Regal gemeint ist.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 18 („Aktion“, einschließlich des Hinweises auf die abstrahierte Bedeutung im Aktionsmanagement), S. 20 (Lebenszyklus), S. 38 („Elementarprozess“)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Aktionsmanagement](../aktionsmanagement.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
