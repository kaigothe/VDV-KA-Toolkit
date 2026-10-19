---
titel: Deny List
englisch: deny list
parent: lexikon/abt.md
siehe_auch: [lexikon/kontrolle/sperrliste.md, lexikon/abt/id-token.md]
quellen: [Q19, Q30]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Account Based Ticketing](../abt.md) › Deny List
<!-- /GEN:breadcrumb -->

# Deny List

Die Deny List ist das ABT-Gegenstück zur [Sperrliste](../kontrolle/sperrliste.md) — mit einem grundlegenden Unterschied in der Begründung.

Das Weißbuch hält fest: „**Sperrlisten im Sinne der VDV-KA sind nicht erforderlich**, da die Prüfung der ID-Token in **Echtzeit** mittels Abgleich mit dem Kontroll-Hintergrundsystem erfolgt. Es muss jedoch sichergestellt werden, dass alle dem ABT-System angeschlossenen Institutionen, die Medien ausgeben, **Sperrungen unverzüglich in den zentralen Systemen abbilden**, um u. a. die missbräuchliche Nutzung gestohlener Kreditkarten zu minimieren.“ ([Q30](../../QUELLEN.md#q30), Kap. 5.2.9)

Die Sperre verschwindet also nicht, sie **wandert**: Statt verteilter Listen auf den Geräten gibt es einen zentralen Zustand (abgeleitet). Wo offline geprüft werden muss, kehren Listen zurück — siehe [Online- und Offline-Kontrolle](online-und-offline-kontrolle.md).

**Bei bankkartenbasiertem ABT gibt es zwei Ebenen** ([Q19](../../QUELLEN.md#q19)) · *Herstellerquelle*:

| Ebene | Wirkung |
|---|---|
| **Karten-Ebene (PAN)** | sperrt eine einzelne Kartennummer |
| **Account-Ebene (PAR)** | sperrt **alle Karten**, die zum Konto eines Nutzers gehören, unabhängig von der jeweiligen Kartennummer |

PAR steht für **Payment Account Reference**. Der Anlass für diese zweite Ebene ist konkret benannt: Nutzer umgehen Sperren, indem sie Karten in ihrer Mobile-Wallet **wiederholt neu registrieren** — dabei entstehen neue Kartennummern, aber derselbe Kontobezug ([Q19](../../QUELLEN.md#q19)).

Daran zeigt sich ein Muster, das es im mediumbasierten Verfahren nicht gibt: Weil der Token aus der Zahlungswelt stammt, muss auch die Sperre auf der Ebene der Zahlungswelt ansetzen (abgeleitet).

## Einfach erklärt – Beispiel aus Bärstadt

Eine Deny List ist eine Sperrliste — und sie ist beim ABT eigentlich gar nicht nötig.

So jedenfalls die Theorie im Weißbuch, und die Begründung ist schlüssig: Wenn ohnehin bei jeder Prüfung zentral nachgefragt wird, braucht kein Gerät eine Liste. Die Antwort „dieser Token ist gesperrt" kommt aus demselben System wie die Antwort „dieser Token hat ein Ticket".

Die Sperre verschwindet also nicht. Sie zieht um — von vielen verteilten Listen in einen zentralen Zustand.

Aber das Weißbuch schiebt sofort eine Bedingung nach, und die ist der eigentliche Knackpunkt: Alle Stellen, die Medien ausgeben, müssen Sperrungen **unverzüglich** zentral abbilden. Bei Pias BärenKarte ist das einfach — die Bärstädter Verkehrsbetriebe haben sie ausgegeben und melden selbst. Bei Ollis Bankkarte hat eine Bank sie ausgegeben, die vom Nahverkehr nichts weiß.

Und nun wird es richtig interessant, denn aus der Praxis kennt man ein Umgehungsmuster, das diese Lücke ausnutzt.

Jemand fährt ohne zu zahlen. Seine Kartennummer wird gesperrt. Er löscht die Karte aus seinem Handy-Wallet und registriert sie neu — und bekommt dabei eine **neue Kartennummer**. Die Sperre greift nicht mehr. Das lässt sich beliebig wiederholen.

Die Antwort darauf ist eine Sperre auf der **Kontoebene**. Die Payment Account Reference bezeichnet nicht die Karte, sondern das Konto dahinter. Wird sie gesperrt, sind alle Karten dieses Kontos gesperrt — egal wie oft jemand sie neu registriert.

Man sieht daran etwas Grundsätzliches: Wer Zahlungsmittel als Fahrschein nutzt, erbt die Betrugsmuster der Zahlungswelt.

## Quellen

- [Q30](../../QUELLEN.md#q30) – VDV eTS, Weißbuch ABT V1.0.1, Kap. 5.2.9 „Keine Sperrlisten / Schutz gegen Missbrauch“ (Sperrlisten im Sinne der VDV-KA nicht erforderlich wegen Echtzeitabgleich der ID-Token mit dem Kontroll-Hintergrundsystem; Pflicht aller medienausgebenden Institutionen, Sperrungen unverzüglich in den zentralen Systemen abzubilden; Bezug auf gestohlene Kreditkarten)
- [Q19](../../QUELLEN.md#q19) – Ticketer, „PAR Deny Lists“ (16.02.2024): Deny Lists auf Account-Ebene über die Payment Account Reference gegenüber bisherigen Listen auf Ebene der einzelnen Kartennummer (PAN); Sperrung aller einem Konto zugeordneten Karten unabhängig von der Kartennummer der Mobile-Wallet; Anlass ist das wiederholte Neuregistrieren von Karten in Mobile-Wallets zur Umgehung von Sperren · *Herstellerquelle, belegt Marktpraxis, nicht den Standard*

<!-- GEN:siehe_auch -->
## Siehe auch

- [Sperrliste](../kontrolle/sperrliste.md)
- [ID-Token](id-token.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Account Based Ticketing](../abt.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
