---
titel: zSAM
abkuerzung: zSAM
englisch: additional SAM for barcode tickets
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/sam.md, lexikon/datenformate/vdv-barcode.md]
quellen: [Q45, Q46]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › zSAM
<!-- /GEN:breadcrumb -->

# zSAM

Das Abkürzungsverzeichnis löst **zSAM** als „zusätzliches [SAM](sam.md) für 2D-Barcode-Ticket“ auf ([Q45](../../QUELLEN.md#q45), S. 8).

Die Begriffsliste derselben Quelle beschreibt den Gegenstand genauer, und zwar über das **Zertifikat**: Das zSAM-Zertifikat ist ein spezielles, zusätzliches SAM-Zertifikat für Barcode-Tickets. Es wird für **jedes SAM benötigt, das für die Ausgabe von Barcode-Tickets verwendet werden soll**, und kann bei Bedarf über den PKI-Webservice beziehungsweise die [PKI](pki.md)-Webschnittstelle beantragt werden ([Q45](../../QUELLEN.md#q45), S. 35).

Unterscheidendes Merkmal ist demnach nicht ein eigenes Baumuster, sondern **ein zusätzliches Zertifikat auf einem SAM** (abgeleitet). Dazu passt, dass die Berechtigung auch für **bereits produzierte SAMs** beantragt werden kann ([Q45](../../QUELLEN.md#q45), S. 27).

**Der Weg der Beantragung** führt über die PKI-Webschnittstelle, auf der ein Ansprechpartner eines Unternehmens einzelne Zertifikate beantragt. Das Recht dazu wird eigens vergeben und ist in der Rechteliste als eigener Eintrag „zSAM“ aufgeführt: Bestellen und Abrufen von zSAM-Zertifikaten über die PKI-Webschnittstelle, etwa für die Erstellung von 2D-Barcodes ([Q45](../../QUELLEN.md#q45), S. 27).

**Warum es das braucht:** Bei der Ausgabe von Barcodetickets wird eine digitale Signatur über die Ticketdaten gebildet, wofür ein SAM mit einem geheimen Signaturschlüssel nötig ist ([Q46](../../QUELLEN.md#q46), Kap. 4.1, PDF-S. 8). Ein [VDV-Barcode](../datenformate/vdv-barcode.md) entsteht also nicht ohne Sicherheitsmodul — die Rechte und Zertifikate dafür sind von denen der Chipkartenausgabe getrennt (abgeleitet).

**Stand der Quelle:** 2016. Ob die Trennung unter [etiCORE](../grundlagen/eticore.md) fortbesteht, ist nicht belegt.

## Einfach erklärt – Beispiel aus Bärstadt

Die Bärstädter Verkehrsbetriebe wollen Handy-Tickets verkaufen. Technisch klingt das harmlos — ein Barcode auf einem Bildschirm, kein Chip, keine Karte, nichts Physisches.

Trotzdem brauchen sie ein Sicherheitsmodul.

**Warum.** Ein Barcode ist nur dann mehr als ein Bild, wenn er unterschrieben ist. Diese Unterschrift muss mit einem geheimen Schlüssel gebildet werden, und geheime Schlüssel liegen in der VDV-Welt in SAMs. Ohne ein Sicherheitsmodul kann die BVB also keinen gültigen Barcode erzeugen, so wie sie ohne SAM auch keine Berechtigung auf Pias BärenKarte schreiben kann.

**Was das Besondere ist.** Für Barcode-Tickets reicht nicht jedes SAM. Jedes Modul, das Barcodes ausgeben soll, braucht ein **zusätzliches Zertifikat** — und zwar genau für diesen Zweck. Das SAM-9010-7 in Petra Prankes Kontrollgerät hat keines; es kontrolliert, es gibt nichts aus. Ein Modul im Ausgabepfad der BVB-App bekommt eines.

Beantragt wird es über eine Webschnittstelle der Schlüsselstelle, und zwar von einer benannten Person bei der BVB — jemandem, der dieses Recht ausdrücklich zugeteilt bekommen hat. Nicht jeder Mitarbeiter kann Zertifikate bestellen.

**Ein beruhigender Nebensatz in der Quelle:** Das Zertifikat lässt sich auch für Module beantragen, die längst im Betrieb sind. Die BVB muss also keine neue Hardware kaufen, wenn sie zusätzlich Barcodes anbieten will. Sie erweitert, was sie hat.

**Was man daraus für die Rollentrennung lernt.** Chipkarte und Barcode laufen über getrennte Rechte, obwohl am Ende dieselbe Art Berechtigung entsteht. Wer wissen will, ob ein Verkehrsunternehmen Barcodes ausgeben darf, sieht nicht in die Kartenausgabe, sondern in die Zertifikatsrechte.

Ein Hinweis zum Alter: Diese Beschreibung stammt aus einem Dokument von 2016. Dass es den Begriff zSAM so noch gibt, ist für heute nicht belegt.

## Quellen

- [Q45](../../QUELLEN.md#q45) – ASM-Tool Glossar und Abkürzungsverzeichnis V1.03 (20.07.2016): S. 8 („zSAM: Zusätzliches SAM für 2D-Barcode-Ticket“), S. 27 (PKI-Webschnittstelle; Recht „zSAM: Bestellen und Abrufen von zSAM-Zertifikaten über die PKI-Webschnittstelle, z. B. für die Erstellung von 2D-Barcode“; Beantragung und Verwaltung auch für bereits produzierte SAMs), S. 35 („zSAM-Zertifikat“: spezielles zusätzliches SAM-Zertifikat für Barcode-Tickets, für jedes SAM nötig, das für die Ausgabe von Barcode-Tickets verwendet werden soll, Beantragung über den PKI-Webservice)
- [Q46](../../QUELLEN.md#q46) – Whitepaper Barcodes im ÖPNV (2021), Kap. 4.1, PDF-S. 8 (digitale Signatur über die Ticketdaten bei der Ausgabe; dafür ein SAM mit geheimem Signaturschlüssel nötig)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Secure Application Module](sam.md) (SAM)
- [VDV-Barcode](../datenformate/vdv-barcode.md)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
