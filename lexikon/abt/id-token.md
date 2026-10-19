---
titel: ID-Token
englisch: ID token
parent: lexikon/abt.md
siehe_auch: [lexikon/abt/account.md, lexikon/abt/deny-list.md]
quellen: [Q01, Q02, Q30]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Account Based Ticketing](../abt.md) › ID-Token
<!-- /GEN:breadcrumb -->

# ID-Token

Beim ABT trägt das Medium **keine Berechtigung mehr, sondern nur eine Kennung** — den ID-Token. Über ihn wird der [Account](account.md) im Hintergrundsystem gefunden ([Q02](../../QUELLEN.md#q02), S. 16; [Q30](../../QUELLEN.md#q30), Kap. 5.2.1).

Ein **Open-Loop-System** „ermöglicht die Nutzung einer Vielzahl von Medien“ und „benötigt keine App oder spezielle Chip-Karte“; als Token kommen „kontaktlose Bank- oder Kreditkarten, mobile Wallets mit Zugriff auf Apple Pay und Google Pay sowie damit verknüpfte Wearables und Smartwatches“ in Frage ([Q30](../../QUELLEN.md#q30), Kap. 5.2.2).

Das Weißbuch unterscheidet **zwei Arten** ([Q30](../../QUELLEN.md#q30), Kap. 5.2.2):

| Art | Beschreibung |
|---|---|
| **unmittelbar mit Zahlungsmittel verknüpft** | Medien, die unmittelbar auf ein Bankkonto referenzieren, über das abgerechnet werden kann — z. B. Kreditkarte |
| **mittelbar mit Zahlungsmittel verknüpft** | Medien ohne Bankkontobezug; die Abrechnung erfolgt über das dem Account zugeordnete Zahlungsmittel — z. B. Lastschrift oder PayPal |

Diese Unterscheidung ist mehr als eine Nuance: Bei unmittelbar verknüpften Medien ist der Token zugleich ein Zahlungsmittel, was eigene Missbrauchsfragen aufwirft — siehe [Deny List](deny-list.md) (abgeleitet).

„Das Management der Nutzermedien obliegt weiterhin den ausstellenden Institutionen im ABT-Kontext. Auf Basis eines Open-Loop-Systems muss dies jedoch **nicht mehr ein Verkehrsunternehmen** sein.“ ([Q30](../../QUELLEN.md#q30), Kap. 5.2.2)

Daran zeigt sich der eigentliche Bruch gegenüber dem mediumbasierten Verfahren: Dort gibt der Kundenvertragspartner die Applikation aus ([Q02](../../QUELLEN.md#q02), S. 27) — hier kann das Medium von einer Bank stammen, die mit dem Verkehr nichts zu tun hat (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Ein ID-Token ist ein Medium, das nichts weiß.

Auf Pias BärenKarte steht ihr Abo. Auf einem ID-Token steht nur eine Nummer — und die ist für sich genommen bedeutungslos. Erst im Rechenzentrum wird daraus etwas: zu dieser Nummer gehört dieses Konto, und in diesem Konto liegt ein gültiges Ticket.

Der Reiz liegt darin, was als Token taugen kann. Praktisch alles, was eine eindeutige Kennung hat und sich kontaktlos lesen lässt: eine Bankkarte, ein Handy mit Apple Pay oder Google Pay, eine Smartwatch, ein einfacher NFC-Chip.

Für Olli Tapsig heißt das: Er braucht nichts Besonderes mehr. Keine BärenKarte, keine App des Verkehrsbunds. Seine Bankkarte genügt.

Nun zu einer Unterscheidung, die auf den ersten Blick trocken aussieht und erhebliche Folgen hat.

**Manche Token sind selbst ein Zahlungsmittel.** Ollis Bankkarte verweist direkt auf sein Konto; darüber wird abgerechnet. Bequem — und riskant, denn eine gestohlene Karte ist dann gleichzeitig ein gestohlener Fahrschein.

**Andere Token sind es nicht.** Ein einfacher NFC-Chip verweist nur auf Ollis Konto beim Verkehrsbund; bezahlt wird dort per Lastschrift. Der Chip allein nützt einem Finder wenig.

Diese zwei Welten erklären, warum es beim ABT eigene Missbrauchsschutzverfahren gibt, die es im mediumbasierten System nicht braucht.

Und ein Satz, der den eigentlichen Bruch markiert: **Das Medium muss nicht mehr vom Verkehrsunternehmen kommen.** Pias Karte hat die BVB ausgegeben und verwaltet sie. Ollis Bankkarte hat eine Bank ausgegeben, die vom Nahverkehr nichts weiß — und trotzdem fährt er damit.

## Quellen

- [Q30](../../QUELLEN.md#q30) – VDV eTS, Weißbuch ABT V1.0.1, Kap. 5.2.2 „ID-Medium“ (Open-Loop-System ohne App oder spezielle Chipkarte; kontaktlose Bank- und Kreditkarten, mobile Wallets mit Apple Pay und Google Pay, Wearables und Smartwatches als Token; Medienmanagement weiterhin bei den ausstellenden Institutionen, die kein Verkehrsunternehmen sein müssen; die beiden Arten unmittelbar und mittelbar mit Zahlungsmittel verknüpft samt Beispielen), Kap. 5.2.1 (Verbindung von ID und Account)
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 16 (Verknüpfung über eine eindeutige ID, Authentifizierung mit einem persönlichen Identifikationsmittel), S. 27 (Ausgabe der Applikation immer über einen Kundenvertragspartner)
- [Q01](../../QUELLEN.md#q01) – VDV eTS, Einordnung von Account Based Ticketing, V1.0 (ID-Token im Zusammenhang mit der Umkehrung der Speicherortlogik)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Account Based Ticketing](../abt.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
