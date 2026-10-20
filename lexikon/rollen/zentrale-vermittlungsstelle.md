---
titel: Zentrale Vermittlungsstelle
abkuerzung: ZVM
englisch: central routing engine
parent: lexikon/rollen.md
siehe_auch: [lexikon/transaktionen/ion.md, lexikon/rollen/rollennamen-in-eticore.md, lexikon/transaktionen/fehlercodes-im-ion.md, lexikon/rollen/rollencodes.md]
quellen: [Q02, Q50]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Zentrale Vermittlungsstelle
<!-- /GEN:breadcrumb -->

# Zentrale Vermittlungsstelle

Die **Zentrale Vermittlungsstelle** (ZVM, englisch Central Routing Engine, CRE) gehört zum [Interoperabilitätsnetzwerk](../transaktionen/ion.md). Sie vermittelt die Nachrichten eines ION-Teilnehmers an den Empfänger, den die Nachricht über Organisations-ID, Rolle und Dienst nennt ([Q02](../../QUELLEN.md#q02), S. 100). Teilnehmer können der Applikationsherausgeber, der Scheme Manager, der Kontroll- und Sperrlistenservice, Kundenvertragspartner, Dienstleister und Produktverantwortliche sein, direkt oder über Adapter angebunden. Die CRE setzt die logische Adressierung in die physische um und stellt die Nachricht zu oder speichert sie zwischen ([Q02](../../QUELLEN.md#q02), S. 49).

In etiCORE ist die CRE ein zentraler Dienst, den die Rollenübersetzung der ZVM zuordnet ([Rollennamen in etiCORE](rollennamen-in-eticore.md)). Ihre Schnittstelle trägt die Rolle 254 und kennt eine Operation, `setServiceUnavailable`: Sie setzt einen Dienst (Dienst, Organisation und Rolle) als nicht verfügbar; aufrufen können sie die Systeme von PO, SO und CCP samt ihren Erweiterungen ([Q50](../../QUELLEN.md#q50), WSDL `cre`).

Fehler beim Zustellen melden Codes wie `E_IONC_RECEIVER_NOT_REACHABLE`, `E_IONC_NO_TARGET_ADDRESS_FOUND_FOR_ROUTING_PARAMETERS` und `E_CRE_SERVICE_NOT_CONFIGURED` ([Fehlercodes im ION](../transaktionen/fehlercodes-im-ion.md)). Die Angaben zu etiCORE stammen aus einem Release-Kandidaten (3.0.0-rc.6).

## Einfach erklärt – Beispiel aus Bärstadt

Die Zentrale Vermittlungsstelle ist das Verteilzentrum der Post. Wer einen Brief aufgibt, schreibt nicht die Straße des Empfängers darauf, sondern seine Organisation, die Rolle und den Dienst. Die Vermittlungsstelle weiß, wo dieser Dienst gerade zu erreichen ist.

Die BVB schickt eine Bestellung für Pias ABO Azubi an den Bären-Verkehrsbund. Sie adressiert: Organisation 9020, Rolle Produktverantwortlicher, Dienst Aktionsmanagement. Wo die Server des Verbunds im Netz stehen, braucht die BVB nicht zu wissen. Zieht der Verbund um, ändert sich nur der Eintrag in der Vermittlungsstelle, nicht die Adressierung bei den Teilnehmern.

Ist der Verbund gerade nicht zu erreichen, kann die Vermittlungsstelle die Nachricht zwischenspeichern und später zustellen. Denkbar ist auch: Muss der Verbund für Wartungsarbeiten abschalten, meldet er seinen Dienst vorher als nicht verfügbar. Dann weiß die Vermittlungsstelle Bescheid und liefert nicht ins Leere.

So bleibt jede Seite einfach: Sie muss nur wissen, mit wem sie sprechen will, und nicht, wo er wohnt.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 100 (Eintrag *Zentrale Vermittlungsstelle / Central Routing Engine*, Abkürzungen CRE und ZVM), S. 49
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: WSDL `cre` (Rolle 254, Operation `setServiceUnavailable`) · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Interoperabilitätsnetzwerk](../transaktionen/ion.md) – das Netz, zu dem sie gehört
- [Rollennamen in etiCORE](rollennamen-in-eticore.md) – ZVM und CRE
- [Fehlercodes im ION](../transaktionen/fehlercodes-im-ion.md) – Fehler beim Zustellen
- [Rollencodes](rollencodes.md) – die Rolle 254

<!-- GEN:siehe_auch -->
## Siehe auch

- [Interoperabilitätsnetzwerk](../transaktionen/ion.md) (ION)
- [Rollennamen in etiCORE](rollennamen-in-eticore.md)
- [Fehlercodes im ION](../transaktionen/fehlercodes-im-ion.md)
- [Rollencodes](rollencodes.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
