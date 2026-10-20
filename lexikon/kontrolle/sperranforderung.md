---
titel: Sperranforderung
englisch: hotlisting demand
parent: lexikon/kontrolle.md
siehe_auch: [lexikon/kontrolle/sperrliste.md, lexikon/kontrolle/sperrung.md, lexikon/aktionsmanagement/aktionsfreigabe.md, lexikon/rollen/scheme-manager.md]
quellen: [Q02, Q50]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Kontrolle](../kontrolle.md) › Sperranforderung
<!-- /GEN:breadcrumb -->

# Sperranforderung

Vier Begriffe beschreiben, wie ein Objekt auf die [Sperrliste](sperrliste.md) kommt und wieder herunter ([Q02](../../QUELLEN.md#q02), S. 82–88):

- Die **Sperranforderung** (Hotlisting Demand) soll bewirken, dass ein *verantwortlicher Dritter* ein Objekt auf die Liste setzt. Initiator ist je nach Objekt ein anderer CCP, ein Dienstleister, der Product Owner oder der Applikationsherausgeber.
- Der **Sperrauftrag** (Hotlisting Order) setzt das Objekt auf die Liste. Ihn erteilt der Verantwortliche selbst.
- Die **Sperraufhebungsanforderung** (Hotlisting Demand Revocation) nimmt eine frühere Sperranforderung zurück und kann dazu führen, dass der Verantwortliche das Objekt entfernt.
- Der **Sperrfreigabeauftrag** (Hotlisting Removal Order) „dient dazu, ein Objekt von der jeweiligen Sperrliste zu nehmen“.

Für Berechtigungen und Applikationen ist in KA und etiCORE der **primäre CCP** verantwortlich. Bei SAM, Schlüsseln und Organisationen ändert sich das: In der KA liegt es beim Applikationsherausgeber; in etiCORE beim SAM-Inhaber (SO oder CCP) für das SAM, sonst beim Scheme Manager, der SAMs, Authentisierungsschlüssel und Organisationen nur noch „zum Aufräumen der Sperrliste“ entfernt ([Q02](../../QUELLEN.md#q02), S. 86–88). Das deckt sich mit den Aufrufern der Hotlist-Operationen ([Q50](../../QUELLEN.md#q50), WSDL `hotlist`).

Die Nachrichten der KA 1.x tragen die Namen `TXSAUF…` (Sperrauftrag) und `TXSFREI…` (Sperrfreigabeauftrag), in etiCORE `add…ToHotlist` und `remove…FromHotlist` ([exzerpte/Q50.md](../../exzerpte/Q50.md)). Hier ist „Freigabe“ also eindeutig das Entfernen.

## Einfach erklärt – Beispiel aus Bärstadt

Pia verliert ihre BärenKarte, und die Karte taucht in Luchsstadt auf. Der Luchs-Verkehrsverbund (LVV) bemerkt es bei einer Kontrolle. Er darf die Karte aber nicht selbst sperren, denn verantwortlich ist der primäre Kundenvertragspartner der Karte, die Bärstädter Verkehrsbetriebe.

Also schickt der LVV eine **Sperranforderung** an die BVB: „Bitte lasst diese Karte sperren.“ Die BVB prüft und erteilt den **Sperrauftrag** an den Kontrollservice: Die Applikation 90000042 kommt auf die Sperrliste.

Zwei Tage später findet Pia die Karte wieder. Bodo Bärlauch zieht die Sperre zurück: Er erteilt einen **Sperrfreigabeauftrag**, der den Eintrag von der Sperrliste nimmt. Hätte der LVV seine Anforderung zurückgezogen, wäre das eine **Sperraufhebungsanforderung**. Sie bittet die BVB, den Eintrag zu entfernen, entscheidet aber nicht selbst.

Der Name „Freigabe“ ist hier unmissverständlich: Etwas, das auf der Liste steht, wird von ihr genommen. Beim Aktionsmanagement kehrt das Wort in der Aktionsfreigabe wieder, und die Parallele liegt nahe (abgeleitet).

Bei einer Organisation oder einem Schlüssel wäre es anders: Die könnte nur der Scheme Manager eintragen, und entfernen würde er sie nur beim Aufräumen der Liste.

## Quellen

- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 82–84 (*Sperranforderung*), S. 84 f. (*Sperraufhebungsanforderung*), S. 86 f. (*Sperrauftrag*), S. 87 f. (*Sperrfreigabeauftrag*)
- [Q50](../../QUELLEN.md#q50) – etiCORE Interfaces Documentation 3.0.0-rc.6: WSDL `hotlist`, Operationen `add…ToHotlist` und `remove…FromHotlist` · *Release-Kandidat*

<!-- GEN:unterartikel -->
<!-- /GEN:unterartikel -->

## Siehe auch

- [Sperrliste](sperrliste.md) – die Liste
- [Sperrung](sperrung.md) – der Zustandswechsel
- [Aktionsfreigabe](../aktionsmanagement/aktionsfreigabe.md) – dasselbe Wort im Aktionsmanagement
- [Scheme Manager](../rollen/scheme-manager.md) – verantwortlich für Organisationen und Schlüssel

<!-- GEN:siehe_auch -->
## Siehe auch

- [Sperrliste](sperrliste.md)
- [Sperrung](sperrung.md)
- [Aktionsfreigabe](../aktionsmanagement/aktionsfreigabe.md)
- [Scheme Manager](../rollen/scheme-manager.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Kontrolle](../kontrolle.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
