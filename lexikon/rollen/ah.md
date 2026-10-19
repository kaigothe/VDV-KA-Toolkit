---
titel: Applikationsherausgeber
abkuerzung: AH
englisch: Application Owner
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/organisations-id.md, lexikon/rollen/rollencodes.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Applikationsherausgeber
<!-- /GEN:breadcrumb -->

# Applikationsherausgeber

Der Applikationsherausgeber (AH) ist **Teil des Scheme Manager** und hält den Anwendungsvertrag für die Nutzung der Nutzermedium-Applikation. Er autorisiert den Weiterverkauf der Applikation durch einen Kundenvertragspartner an einen Kunden ([Q02](../../QUELLEN.md#q02), S. 23).

Seine Befugnisse machen ihn zur Eintrittspforte des Systems ([Q02](../../QUELLEN.md#q02), S. 23):

- Er definiert die **Anwendungsregeln**.
- Er gewährt einem Produktverantwortlichen, einem Kundenvertragspartner und einem Dienstleister das **Recht zur Teilnahme** an den EFM-Systemen, stellt ihnen die erforderlichen Kennungen zur Verfügung und gewährt das Recht zur Nutzung der entsprechenden, vom Sicherheitsmanagement des Scheme Manager verwalteten Schlüssel.
- Er berechtigt Kundenvertragspartner zur **Ausgabe von Applikationen** im Nutzermedium an ihre Kunden.
- Er ist verantwortlich für die Bereitstellung von Informationen über die **Applikationsinstanz-ID** bei Anfragen zu defekten Nutzermedien.
- Er implementiert ein **Zertifikatsmanagement** für alle Applikationsinstanzen.

Im `TX_BASE` trägt der AH den [Rollencode](rollencodes.md) **4**. Dieser Wert ist eine Korrektur: Die Versionshistorie von [Q06](../../QUELLEN.md#q06) vermerkt unter dem 16.03.2018 „In Kap. 4.10 Rollencode für den AH von 5 auf 4 korrigiert“ ([Q06](../../QUELLEN.md#q06), Versionshistorie, Kap. 4.10) · *verbundspezifisch*.

Weitere Details sind den Rollenbeschreibungen im nicht öffentlichen Hauptdokument der Spezifikation zu entnehmen ([Q02](../../QUELLEN.md#q02), S. 23).

## Einfach erklärt – Beispiel aus Bärstadt

Der Bärenland eTicket Service verkauft nichts und fährt nichts. Er entscheidet, wer mitspielen darf.

Ohne ihn gäbe es das System nicht. Als die Bärstädter Verkehrsbetriebe anfingen, Chipkarten auszugeben, mussten sie zuvor von ihm die Erlaubnis erhalten: eine Organisations-ID, das Recht zur Teilnahme und die Berechtigung, Schlüssel zu nutzen. Dasselbe gilt für den Bären-Verkehrsbund und für jeden anderen Beteiligten.

Der Name ist etwas sperrig, aber präzise: Es geht um die **Applikation** — also um das Stück Software und Datenstruktur, das auf Pias BärenKarte liegt und die Karte überhaupt zu einem KA-Medium macht. Für dieses Stück hält der eTicket Service den Vertrag. Die Verkehrsbetriebe dürfen es nur deshalb an Pia weitergeben, weil er es ihnen erlaubt hat.

Vergleichbar ist das mit einem Franchise. Der Franchisegeber besitzt die Marke und das Regelwerk. Die Filialen betreiben das Geschäft, aber nach seinen Regeln und mit seiner Erlaubnis.

Zwei praktische Aufgaben hat er noch. Erstens kann er sagen, zu welcher Karte eine Applikationsinstanz gehört — wenn Pias Karte kaputt ist und niemand mehr etwas auslesen kann, bleibt die Nummer 90000042 die einzige Spur, und er kann sie zuordnen. Zweitens verwaltet er die Zertifikate aller Applikationsinstanzen.

Eine Fußnote für Nachrichtenleser: Der Rollencode des Applikationsherausgebers war im RMV-Pflichtenheft zunächst falsch angegeben und wurde 2018 von 5 auf 4 korrigiert. Wer mit älteren Unterlagen arbeitet, kann also auf die 5 stoßen. Die 5 gehört aber zum Kontroll- und Sperrlistenservice.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 23 („Applikationsherausgeber / Application Owner“: Teil des Scheme Manager, Anwendungsvertrag, Autorisierung des Weiterverkaufs, Anwendungsregeln, Gewährung des Teilnahmerechts an PV, KVP und DL, Kennungen und Schlüsselnutzung, Berechtigung der KVP zur Applikationsausgabe, Informationen zur Applikationsinstanz-ID bei defekten Medien, Zertifikatsmanagement, Verweis auf das Hauptdokument; Abkürzungen AH und AO)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Versionshistorie zu v2.2 („In Kap. 4.10 Rollencode für den AH von 5 auf 4 korrigiert“, 16.03.2018), Kap. 4.10 · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Organisations-ID](organisations-id.md) (Org-ID)
- [Rollencodes](rollencodes.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
