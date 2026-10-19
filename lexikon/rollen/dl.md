---
titel: Dienstleister
abkuerzung: DL
englisch: Service Operator
parent: lexikon/rollen.md
siehe_auch: [lexikon/rollen/kvp.md, lexikon/rollen/hintergrundsystem.md]
quellen: [Q02, Q06]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Rollen](../rollen.md) › Dienstleister
<!-- /GEN:breadcrumb -->

# Dienstleister

Der ÖPV-Dienstleister (DL) bietet Transportdienstleistungen für einen Kunden an, der eine entsprechende Berechtigung zur Nutzung dieser Dienstleistungen erworben hat ([Q02](../../QUELLEN.md#q02), S. 34).

Rechtlich entscheidend: Der **Beförderungsvertrag wird zwischen dem transportierenden Dienstleister und einem Nutzer beim Einstieg in das Transportmittel abgeschlossen** ([Q02](../../QUELLEN.md#q02), S. 34) — nicht beim Ticketkauf und nicht mit dem Kundenvertragspartner.

Der Dienstleister erwirbt über den eTicket-Teilnahmevertrag vom Scheme Manager das Recht zur Teilnahme am EFM-System. Er schließt Verträge mit den Produktverantwortlichen über die **Akzeptanz von Produkten** und über die **Bezahlung der erbrachten Beförderungsleistungen** sowie mit den Kundenvertragspartnern über den Ausgleich der entstandenen Forderungen via Forderungsclearing ([Q02](../../QUELLEN.md#q02), S. 34).

Das **Dienstleister-System** gehört zu den [Hintergrundsystemen](hintergrundsystem.md) und dient als Verbindung zwischen den Dienstleister-Terminals und den anderen beteiligten Systemen im EFM. Neben dem Sammeln und Weiterleiten von Daten nimmt es Aufgaben des Monitorings wahr; außerdem müssen die SAMs verwaltet werden ([Q02](../../QUELLEN.md#q02), S. 34).

Im `TX_BASE` trägt der DL den [Rollencode](rollencodes.md) **2** ([Q06](../../QUELLEN.md#q06), Kap. 4.10) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Der Dienstleister ist der, der fährt.

In Bärstadt sind das die Bärstädter Verkehrsbetriebe — dieselbe Organisation, die auch Pias Kundenvertragspartner ist, aber in anderer Funktion. Als Dienstleister betreiben sie die Linie 4 vom Hauptbahnhof zur Waldsiedlung.

Ein Punkt daran ist juristisch überraschend und lohnt die Aufmerksamkeit: Der **Beförderungsvertrag entsteht beim Einstieg**, nicht beim Kauf. Als Pia im Kundencenter ihr Abo abschloss, hat sie einen Kundenvertrag geschlossen — das Versprechen, fahren zu dürfen. Der eigentliche Vertrag über eine konkrete Fahrt entsteht erst, wenn sie an der Haltestelle Tannenweg einsteigt. Und er entsteht mit dem Unternehmen, das dort fährt.

Normalerweise merkt niemand den Unterschied, weil beides die BVB ist. Fährt Pia aber nach Luchsstadt, befördert sie dort der Luchs-Verkehrsverbund. Mit dem hat sie keinen Kundenvertrag — und schließt trotzdem beim Einstieg einen Beförderungsvertrag. Das ist der Grund, warum man die beiden Rollen trennen muss.

Daraus ergibt sich auch, wer wem Geld schuldet. Die BVB haben Pia befördert, also steht ihnen dafür etwas zu. Bezahlt hat Pia aber an ihren Kundenvertragspartner, und das Produkt gehört dem Verkehrsbund. Die Forderung läuft deshalb über zwei Verträge: einen mit dem Produktverantwortlichen über die Akzeptanz des Abos, einen mit dem Kundenvertragspartner über den Ausgleich. Der Ausgleich selbst heißt Forderungsclearing.

Technisch hat der Dienstleister sein eigenes Hintergrundsystem. Es sammelt die Daten der Fahrzeuggeräte, leitet sie weiter, überwacht den Betrieb — und verwaltet die Sicherheitsbausteine in den Geräten. Ohne die ginge keine Kontrolle.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 34 („Dienstleister / Service Operator“: Transportdienstleistung, Abschluss des Beförderungsvertrags beim Einstieg, Teilnahmerecht über den eTicket-Teilnahmevertrag, Verträge mit PV und KVP, Forderungsclearing; „Dienstleister-System“: Zugehörigkeit zu den Hintergrundsystemen, Verbindung zu den DL-Terminals, Monitoring, SAM-Verwaltung), S. 35 („Dienstleister-Terminal“)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.10 (Rollencode DL = 2) · *verbundspezifisch: eTicket RheinMain*

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Rollen](../rollen.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
