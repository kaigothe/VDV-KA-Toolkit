---
titel: Sperrung
englisch: blocking
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/sperrliste.md, lexikon/aktionsmanagement/entsperrung-ueber-aktionsliste.md]
quellen: [Q02]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Sperrung
<!-- /GEN:breadcrumb -->

# Sperrung

„Applikationen und Berechtigungen können gesperrt werden und können dann im Rahmen der Kernapplikation und etiCORE **nicht mehr verwendet werden, solange sie nicht wieder entsperrt werden**. Die Sperrung erfolgt aufgrund einer **Statusänderung** bei der Applikation oder Berechtigung auf dem Nutzermedium.“ ([Q02](../../QUELLEN.md#q02), S. 91)

Die Sperrung ist damit kein Löschen, sondern ein Zustand — und sie ist **umkehrbar** ([Entsperrung](../aktionsmanagement/entsperrung-ueber-aktionsliste.md), [Q02](../../QUELLEN.md#q02), S. 38 f.).

**Zwei Wirkungsarten** sind zu unterscheiden ([Q02](../../QUELLEN.md#q02), S. 89):

| Art | Gegenstand |
|---|---|
| **physische Sperre** | bei Berechtigungen und Applikationen — der Zustand wird auf dem Nutzermedium verändert |
| **logische Sperre bzw. Ablehnung** | aufgrund von SAM-, Schlüssel- oder Organisationssperreinträgen |

Der Unterschied ist folgenreich: Eine physische Sperre reist mit dem Medium und wirkt auch an Geräten ohne aktuelle Sperrliste; eine logische Sperre wirkt nur dort, wo die Liste vorliegt (abgeleitet).

**Wer sperren darf, hängt vom Objekt ab** ([Q02](../../QUELLEN.md#q02), S. 88) — in der KA:

- Berechtigung und Applikation: **Primär-Kundenvertragspartner**
- Secure Application Module: **Applikationsherausgeber**
- Schlüssel: der **Schlüsselbesitzer** (KVP, PV oder AH)
- Organisation: **Applikationsherausgeber**

In etiCORE verschiebt sich das: Berechtigung und Applikation bleiben beim Primär-KVP, bei SAM, Authentisierungsschlüsseln und Organisationen handelt der Scheme Manager **nur noch zum Aufräumen der Sperrliste** ([Q02](../../QUELLEN.md#q02), S. 88).

Das Sperren auf dem Nutzermedium kann ab 2GSI / etiCORE **ohne SAM** erfolgen ([Q02](../../QUELLEN.md#q02), S. 52).

## Einfach erklärt – Beispiel aus Bärstadt

Eine Sperrung nimmt nichts weg. Sie legt still.

Als Pia ihre BärenKarte als verloren meldete, wurde ihr ABO Azubi nicht gelöscht. Es wurde auf einen anderen Zustand gesetzt: gesperrt. Alles blieb, wo es war — Produkt, Gültigkeit, Name. Nur ein Byte änderte sich.

Das ist wichtig, weil Pia die Karte zwei Tage später wiederfand. Hätte man das Abo gelöscht, müsste es neu ausgegeben werden. So genügt eine Entsperrung, und alles ist wie vorher.

Nun der Teil, der beim ersten Lesen leicht untergeht: Es gibt **zwei Arten**, wie eine Sperre wirkt.

Bei Karten und Berechtigungen wird **physisch** gesperrt — der Vermerk kommt auf den Chip. Das ist mehr Aufwand, aber es hat einen großen Vorteil: Die Sperre reist mit. Auch ein Gerät in der Waldsiedlung, das seit zwei Tagen keine Liste geladen hat, sieht sie sofort.

Bei Schlüsseln, Sicherheitsbausteinen und ganzen Organisationen geht das nicht — auf Pias Karte steht ja nicht, ob der Schlüssel eines fremden Unternehmens noch gültig ist. Dort wirkt die Sperre nur **logisch**: Das Gerät schaut in seine Liste und lehnt ab. Hat es die Liste nicht, wirkt gar nichts.

Besonders aufschlussreich ist die Zuständigkeitsfrage. Bodo Bärlauch darf Pias Karte und ihr Abo sperren — das ist seine Kundenbeziehung. Einen Schlüssel oder eine ganze Organisation darf er nicht sperren; das kann nur die übergeordnete Stelle.

Jeder sperrt, was ihm gehört. Und niemand sperrt etwas, das einem anderen gehört — das wäre in einem System mit vielen beteiligten Unternehmen auch kaum vertretbar.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 91 („Sperrung / Blocking“: Applikationen und Berechtigungen können gesperrt werden, Unbenutzbarkeit bis zur Entsperrung, Sperrung als Statusänderung auf dem Nutzermedium), S. 89 („Sperrliste“: physische Sperre bei Berechtigungen und Applikationen gegenüber logischer Sperre bzw. Ablehnung bei SAM-, Schlüssel- und Organisationssperreinträgen), S. 88 (Initiatoren je Objekt für KA und etiCORE), S. 52 (Sperren auf dem Nutzermedium ohne SAM ab 2GSI), S. 38 f. („Entsperrung“)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
