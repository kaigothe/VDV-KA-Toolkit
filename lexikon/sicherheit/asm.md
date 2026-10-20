---
titel: ASM
abkuerzung: ASM
englisch: application and security management system
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/rollen/rollennamen-in-eticore.md, lexikon/sicherheit/keymanagement.md]
quellen: [Q43, Q45, Q46]
status: belegt
offene_fragen: []
stand: 2026-10-20
codes: []
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › ASM
<!-- /GEN:breadcrumb -->

# ASM

**ASM steht für „Applikations- und Sicherheitsmanagement-System des eTicket Deutschland“ und beinhaltet das System des [Applikationsherausgebers](../rollen/ah.md)** ([Q45](../../QUELLEN.md#q45), S. 7).

**Das ASM-Tool ist sein Zugang nach außen.** Eine Organisation, die es nutzen will oder muss — etwa zur Bestellung von Sicherheitskomponenten —, registriert sich einmalig online ([Q45](../../QUELLEN.md#q45), S. 22). Darüber laufen ([Q45](../../QUELLEN.md#q45), S. 11):

- Bestellung symmetrischer und asymmetrischer Schlüssel samt Freigabe der Nutzungsberechtigung,
- Bestellung von [SAMs](sam.md) und Kryptogrammen,
- Verwaltung der token- und zertifikatsbasierten Rechte in der [PKI](pki.md).

Handeln dürfen das nur benannte **Ansprechpartner (ASP)**, unterteilt in Admin-ASP und Nutzer-ASP; Voraussetzung ist ein gültiger Vertrag mit dem IT-Dienstleister und die Zuordnung einer [Organisations-ID](../rollen/organisations-id.md) zum Kunden im ASM-Tool ([Q45](../../QUELLEN.md#q45), S. 11). Ein Benutzer authentisiert sich mit persönlichem Kennwort, der Admin-ASP zusätzlich mit einem **OTP-Token** ([Q45](../../QUELLEN.md#q45), S. 12).

**Das ASM-Tool ist zugleich der Bezugsweg der Spezifikationen.** Ein Whitepaper nennt es ausdrücklich als Downloadort und die Registrierung als kostenlos ([Q46](../../QUELLEN.md#q46), Kap. 6.1, PDF-S. 15) — ob der vollständige Zugriff einen [Teilnahmevertrag](../grundlagen/teilnahmevertrag.md) voraussetzt, geht daraus nicht hervor (zu prüfen, O16).

**Unter [etiCORE](../grundlagen/eticore.md) wird daraus der ESH**, der e-Ticket Security Hub; der Release Letter führt die Schnittstelle als „ESH (ehem. ASM)“ ([Q43](../../QUELLEN.md#q43), Kap. 5.2.2, PDF-S. 33) und nennt ein eigenes Migrationsdokument für die Gegenüberstellung der Anwendungsfälle ([Q43](../../QUELLEN.md#q43), Kap. 7.1, PDF-S. 35).

**Stand der Quelle zum ASM-Tool:** 2016.

## Einfach erklärt – Beispiel aus Bärstadt

Das ASM ist die Stelle, bei der die Bärstädter Verkehrsbetriebe alles bestellen, was geheim ist.

Man kann sich das wie ein Behördenportal vorstellen, nur für Kryptografie. Die BVB braucht Schlüssel für ihre Terminals, Sicherheitsmodule für die Geräte und Zertifikate für den Nachrichtenverkehr. Nichts davon kauft man im Laden. Alles läuft über das ASM-Tool des Bärenland eTicket Service.

**Wer darf das bedienen?** Nicht jeder bei der BVB. Es gibt benannte Ansprechpartner, und die Rollen sind gestaffelt. Ein Nutzer-Ansprechpartner darf bestellen. Ein Admin-Ansprechpartner darf zusätzlich weitere Ansprechpartner anlegen und sperren — und er braucht zum Anmelden nicht nur ein Kennwort, sondern einen zusätzlichen Token, der laufend neue Einmalkennwörter erzeugt.

Das ist dieselbe Logik wie überall sonst in der KA: Wer über Schlüssel verfügt, muss stärker nachweisen, dass er es wirklich ist.

**Was Voraussetzung ist.** Zwei Dinge. Erstens ein Vertrag — ohne Vertragsverhältnis kein Zugang. Zweitens eine Organisations-ID, die dem Kunden im Tool zugeordnet ist. Die 9010 der BVB ist also keine Nummer, die man sich selbst gibt; sie wird zugeteilt und ist die Voraussetzung dafür, überhaupt bestellen zu können.

**Und noch etwas liegt dort.** Die Spezifikationen selbst. Wer wissen will, wie eine Transaktion aufgebaut ist, lädt das Dokument im ASM-Tool herunter. Das ist der Grund, warum dieses Lexikon so viel aus Nebenquellen rekonstruieren muss: Der direkte Weg führt durch diese Tür, und wer keinen Vertrag hat, steht möglicherweise davor. Wie weit die kostenlose Registrierung allein reicht, ist offen.

**Ein Hinweis auf die Zukunft.** Unter etiCORE heißt diese Stelle nicht mehr ASM, sondern ESH — e-Ticket Security Hub. Die Aufgabe bleibt, der Name wechselt. Wer alte und neue Unterlagen vergleicht, findet dafür ein eigenes Gegenüberstellungsdokument.

## Quellen

- [Q45](../../QUELLEN.md#q45) – ASM-Tool Glossar und Abkürzungsverzeichnis V1.03 (20.07.2016): S. 7 (ASM als Applikations- und Sicherheitsmanagement-System des eTicket Deutschland, beinhaltet das AH-System), S. 10 (Admin-ASP als administrativer Ansprechpartner im KM- und PKI-System, Spezialisierung des Nutzer-ASP mit dem Recht, Nutzer-ASPs anzulegen und zu sperren; administrative Benutzer im ASM-Tool), S. 11 (Ansprechpartner als Gruppe berechtigter Benutzer; Bestellung symmetrischer und asymmetrischer Schlüssel samt Nutzungsberechtigungsfreigabe, Bestellung von SAMs und Kryptogrammen, Verwaltung token- und zertifikatsbasierter Rechte in der PKI; Voraussetzung gültiger Vertrag mit dem IT-Dienstleister und Zuordnung einer Org-ID), S. 12 (Authentisierung mit persönlichem Kennwort, Admin-ASP zusätzlich mit OTP-Token), S. 22 (einmalige Kundenregistrierung online über die Begrüßungsseite des ASM-Tools)
- [Q46](../../QUELLEN.md#q46) – Whitepaper Barcodes im ÖPNV (2021), Kap. 6.1, PDF-S. 15 (ASM-Tool als Downloadort der Spezifikationen, kostenlose Registrierung)
- [Q43](../../QUELLEN.md#q43) – etiCORE Release Letter 3.0.0-rc.6, Kap. 5.2.2, PDF-S. 33 („e-Ticket Security Hub (ehem. ASM)“), Kap. 7.1, PDF-S. 35 (Migrationsdokument zur Gegenüberstellung der Anwendungsfälle von ASM und ESH)

<!-- GEN:siehe_auch -->
## Siehe auch

- [Rollennamen in etiCORE](../rollen/rollennamen-in-eticore.md)
- [Keymanagement](keymanagement.md) (KM)
<!-- /GEN:siehe_auch -->

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
