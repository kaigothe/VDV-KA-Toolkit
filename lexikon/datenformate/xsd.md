---
titel: XSD und WSDL
abkuerzung: XSD
englisch: XML schema and WSDL
parent: lexikon/datenformate.md
siehe_auch: [lexikon/datenformate/xml-namensraum.md, lexikon/grundlagen/versionen.md]
quellen: [Q06, Q25, Q37]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Datenformate](../datenformate.md) › XSD und WSDL
<!-- /GEN:breadcrumb -->

# XSD und WSDL

Die Nachrichten zwischen den Hintergrundsystemen sind XML. Ihre Struktur beschreiben **XSD**-Schemadateien, die Dienste beschreiben **WSDL**-Dateien. Beide sind als „KA-XML-Schemata und WSDL der TX-Transaktionen“ mit der **Inventarnummer 5** verzeichnet ([Q25](../../QUELLEN.md#q25), Kap. 3) und nicht öffentlich.

Die **Dateinamen** sind in EBNF festgelegt ([Q25](../../QUELLEN.md#q25), Kap. 4.3.2):

```text
Basis-XSD-Name = "XML-Schema_", XSD-Bereich, "_", [Funktion]
XSD-Bereich    = "KA_COMMON" | "COMMON" | "KVP_DL_PV" | "KOSE" | "AH"
               | "ALISE" | "PE" | "STATBER" | "FREMD" | "RVS" | "ZVM"
Funktion       = "Types" | "Attachments"
Erweiterung    = Basis-XSD-Name, "_ext-", Releasenummer, ".xsd"

WSDL-Name      = WSDL-Bereich, "_Services", ".wsdl"
WSDL-Bereich   = "KOSE" | "AH" | "PV" | "KVP" | "DL" | "PV_ALISE"
               | "KVP_ALISE" | "PV_STATBER" | "KVP_STATBER" | "DL_STATBER"
```

Daraus lassen sich Dateinamen **vorhersagen**, ohne die Dateien zu haben: `XML-Schema_ALISE.xsd`, `XML-Schema_ALISE_Types.xsd`, `PV_ALISE_Services.wsdl`, `KVP_ALISE_Services.wsdl` (abgeleitet). Das macht eine gezielte Anfrage möglich, siehe [BESCHAFFUNG.md](../../BESCHAFFUNG.md).

Zwei Dinge sind daran bemerkenswert: Es gibt einen Bereich **`ALISE`** bei den Schemata, aber **zwei** ALISE-WSDLs — je eine für die Sicht des Produktverantwortlichen und des Kundenvertragspartners. Und Fehlerkorrekturen erzeugen **eigene Dateien** mit dem Zusatz `_ext-` plus Releasenummer, während der [Namensraum](xml-namensraum.md) unverändert bleibt ([Q25](../../QUELLEN.md#q25), Kap. 4.3.3).

Die Releasenummer gilt verbindlich für alle Komponenten, WSDLs und XSDs eingeschlossen ([Q25](../../QUELLEN.md#q25), Kap. 4.3.1.2). Ein Prüfbericht nennt für die XML-Schemata und WSDL die Version **1.12.0** ([Q37](../../QUELLEN.md#q37)).

[Q06](../../QUELLEN.md#q06) führt die XSD als eigenen Anhang (Kap. 7.1) und nennt als Bezug die Anlagen `KA-vHGS-Schnittstellen-1.107K20120104.zip` und `KA-vHGS-Schnittstellen-1.3.0.zip` ([Q06](../../QUELLEN.md#q06), Kap. 4.8) · *verbundspezifisch*.

## Einfach erklärt – Beispiel aus Bärstadt

Ohne Schema kann man eine XML-Nachricht lesen, aber nicht prüfen.

Der Unterschied ist erheblich. Pias Aktionslisteneintrag liegt als XML vor, und man erkennt darin `berStatus`, `prodProdukt_ID`, Datumsangaben. Lesen geht also. Aber die Fragen, die zählen, bleiben offen: Ist dieses Feld überhaupt erlaubt? Fehlt ein Pflichtfeld? Hat die Zahl den richtigen Typ? Darf dieses Element an dieser Stelle stehen?

Das beantwortet nur das Schema — und das ist nicht öffentlich.

Nun kommt eine angenehme Überraschung. Das eTicket-Regelwerk legt die **Dateinamen** dieser Schemata fest, und zwar formal in EBNF. Damit lässt sich ausrechnen, wie die gesuchten Dateien heißen, auch ohne sie zu besitzen: `XML-Schema_ALISE.xsd` für die Struktur, `PV_ALISE_Services.wsdl` und `KVP_ALISE_Services.wsdl` für die Dienste.

Für eine Anfrage ist das ein großer Unterschied. „Schicken Sie mir bitte die ALISE-Schemata" ist eine Bitte. „Ich benötige `XML-Schema_ALISE.xsd` samt Includes sowie `PV_ALISE_Services.wsdl` und `KVP_ALISE_Services.wsdl`" ist eine Bestellung.

Zwei Details verraten etwas über den Aufbau.

**Es gibt zwei ALISE-Dienstbeschreibungen**, nicht eine. Eine für die Sicht des Produktverantwortlichen, eine für die des Kundenvertragspartners. Dieselbe Schnittstelle, zwei Perspektiven — passend dazu, dass der eine Aufträge annimmt und der andere Listen abholt.

**Fehlerkorrekturen bekommen eigene Dateien** mit einem Anhängsel wie `_ext-3.1.1`, während der Namensraum gleich bleibt. Das ist der Mechanismus, mit dem ältere und neuere Systeme weiter miteinander reden können.

## Quellen

- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA XML-Schemata und WSDL, Inventarnummer 5), Kap. 4.3.1.2 (Verbindlichkeit der Releasenummer für alle Komponenten), Kap. 4.3.2.1 f. (PDF-S. 113 f.): EBNF der XSD- und WSDL-Dateinamen samt der Listen zulässiger Bereiche und der Erweiterung `_ext-` bei Korrekturen, Kap. 4.3.3 (Namensraum bleibt bei Service-Packs bestehen), Kap. 4.3.4 (Namenskonventionen innerhalb der WSDL)
- [Q37](../../QUELLEN.md#q37) – cetecom-Prüfbericht (2024), S. 4 (KA-XML-Schemata und WSDL der TX-Transaktionen in Version 1.12.0)
- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 7.1 (XSD als Anhang), Kap. 4.8 (Anlagen `KA-vHGS-Schnittstellen-1.107K20120104.zip` und `KA-vHGS-Schnittstellen-1.3.0.zip`) · *verbundspezifisch*

**Hinweis zur Extraktion:** Die EBNF in [Q25](../../QUELLEN.md#q25) enthält im extrahierten Text Lücken durch fehlende Umlaute und Sonderzeichen. Die hier wiedergegebenen Produktionen sind die vollständig lesbaren; Zitate sind vor verbindlicher Verwendung am PDF zu prüfen.

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Datenformate](../datenformate.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
