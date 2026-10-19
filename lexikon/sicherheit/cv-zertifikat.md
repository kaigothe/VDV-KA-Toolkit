---
titel: CV-Zertifikat
abkuerzung: CVC
englisch: card verifiable certificate
parent: lexikon/sicherheit.md
siehe_auch: [lexikon/sicherheit/pki.md, lexikon/sicherheit/sam.md]
quellen: [Q02, Q06, Q25]
status: belegt
offene_fragen: []
stand: 2026-10-19
codes:
  - wert: 1
    bedeutung: NM- und SAM-Autorisierungsschlüssel für PKCS#1-Signatur
    quelle: Q06
    fundstelle: Kap. 4.7 (PDF-S. 35)
    status: belegt
    verbundspezifisch: true
  - wert: 2
    bedeutung: SAM-Autorisierungsschlüssel für ISO-9796-2-Signatur
    quelle: Q06
    fundstelle: Kap. 4.7 (PDF-S. 35)
    status: belegt
    verbundspezifisch: true
  - wert: 3
    bedeutung: SAM-Encryption-Schlüssel
    quelle: Q06
    fundstelle: Kap. 4.7 (PDF-S. 35)
    status: belegt
    verbundspezifisch: true
  - wert: 4
    bedeutung: SAM-Signature-Schlüssel
    quelle: Q06
    fundstelle: Kap. 4.7 (PDF-S. 35)
    status: belegt
    verbundspezifisch: true
  - wert: 5
    bedeutung: Keymanagement-Aktivierungsschlüssel
    quelle: Q06
    fundstelle: Kap. 4.7 (PDF-S. 35)
    status: belegt
    verbundspezifisch: true
  - wert: 6
    bedeutung: Keymanagement- und Organisations-Signaturschlüssel
    quelle: Q06
    fundstelle: Kap. 4.7 (PDF-S. 35)
    status: belegt
    verbundspezifisch: true
  - wert: 7
    bedeutung: Zertifikat einer CA
    quelle: Q06
    fundstelle: Kap. 4.7 (PDF-S. 35)
    status: belegt
    verbundspezifisch: true
---

<!-- GEN:breadcrumb -->
[Home](../../README.md) › [Sicherheit](../sicherheit.md) › CV-Zertifikat
<!-- /GEN:breadcrumb -->

# CV-Zertifikat

CV-Zertifikate („card verifiable“) sind die Zertifikatsform der VDV-KA. Übertragen werden sie als Liste in der Nachricht `TXCVCERTL` mit dem `IONTransaktionsTyp_CODE` **254**; jedes Element beschreibt ein CV-Zertifikat ([Q06](../../QUELLEN.md#q06), Kap. 4.7) · *verbundspezifisch*.

Das Feld **`keytype`** gibt „die Bedeutung des Schlüssels innerhalb des Zertifikats“ an ([Q06](../../QUELLEN.md#q06), Kap. 4.7):

| Wert | Bedeutung |
|---:|---|
| **1** | NM- und SAM-Autorisierungsschlüssel für PKCS#1-Signatur |
| **2** | SAM-Autorisierungsschlüssel für ISO-9796-2-Signatur |
| **3** | SAM-Encryption-Schlüssel |
| **4** | SAM-Signature-Schlüssel |
| **5** | Keymanagement-Aktivierungsschlüssel |
| **6** | Keymanagement- und Organisations-Signaturschlüssel |
| **7** | **Zertifikat einer CA** |

An dieser Liste ist die Architektur ablesbar (abgeleitet): Fünf Typen betreffen Nutzermedium und [SAM](sam.md), einer das Keymanagement — und **Typ 7 ist das Zertifikat einer Zertifizierungsstelle**, also das Glied, über das die Kette nach oben schließt. Siehe [PKI](pki.md).

Das Zertifikat selbst steht im Feld `data` „als TLV-Struktur“; für den Aufbau mit Tags und Values verweist [Q06](../../QUELLEN.md#q06), Kap. 4.7, auf die nicht öffentliche **KA SAM-SPEC, Kapitel 4.3.3** ([Q25](../../QUELLEN.md#q25), Kap. 3, Inventarnummer 8).

Dass CV-Zertifikate selbst TLV-Strukturen sind, passt zu ihrer Bestimmung: Sie müssen von einer Chipkarte geprüft werden können — daher „card verifiable“ und daher ein kompaktes Binärformat statt X.509 (abgeleitet).

Eine Sonderform ist das **ZSAM-Zertifikat**: ein „zusätzliches SAM-bezogenes Zertifikat, das für die Ausgabe eines VDV-Barcodes auf Basis einer statischen Berechtigung erforderlich ist“ ([Q02](../../QUELLEN.md#q02), S. 100).

## Einfach erklärt – Beispiel aus Bärstadt

Ein CV-Zertifikat ist ein Zertifikat, das eine Chipkarte selbst prüfen kann. Daher der Name: card verifiable.

Das klingt nach einer Nebensächlichkeit und ist der Grund für das ganze Format. Die üblichen Zertifikate im Internet sind einige Kilobyte groß und setzen einen Rechner voraus, der sie zerlegt. Der Chip auf Pias BärenKarte hat davon nichts. Also wird dasselbe Prinzip in ein kompaktes Format gepackt, das auch ein kleiner Chip verarbeiten kann.

Die Liste der sieben Schlüsseltypen ist dabei ausgesprochen lehrreich, weil sie zeigt, wofür Zertifikate in diesem System überhaupt gebraucht werden.

Vier davon betreffen das **Sicherheitsmodul** im Terminal: Autorisierung, Verschlüsselung, Signatur. Das SAM muss sich ausweisen — gegenüber der Karte und gegenüber dem Hintergrundsystem.

Zwei betreffen das **Schlüsselmanagement**: Wer darf Schlüssel aktivieren, wer darf im Namen einer Organisation signieren?

Und der siebte Typ ist der interessanteste: **das Zertifikat einer Zertifizierungsstelle.** Damit schließt sich die Kette. Ein Zertifikat beweist etwas, weil eine höhere Stelle es signiert hat — und diese Stelle weist sich wiederum mit einem Zertifikat aus. Typ 7 ist das Glied, das nach oben zeigt.

Für Bärstadt bedeutet das konkret: Das Lesegerät am Hauptbahnhof vertraut einem Schlüssel nicht, weil es ihn kennt, sondern weil eine Stelle ihn bestätigt hat, der es vertraut. Diese Stelle muss es nie gesehen haben.

Ein Detail für die Praxis: Für den VDV-Barcode braucht es ein eigenes Zertifikat, das **ZSAM-Zertifikat**. Wer statische Berechtigungen ausgeben will, kommt mit den üblichen Zertifikaten nicht aus.

## Quellen

- [Q06](../../QUELLEN.md#q06) – RMV PH 06-02, Kap. 4.7 „Zertifikatsliste TXCVCERTL“ (PDF-S. 35): `IONTransaktionsTyp_CODE` 254; Element `cvcertificate` mit `keytype` und den sieben Bedeutungen 1 bis 7; Feld `data` mit dem Zertifikat als TLV-Struktur und Verweis auf `[KA_SPEC_SAM]` Kapitel 4.3.3; Verweis auf die XML-Strukturdefinition in den Anlagen `KA-vHGS-Schnittstellen-1.107K20120104.zip` und `KA-vHGS-Schnittstellen-1.3.0.zip` · *verbundspezifisch: eTicket RheinMain*
- [Q02](../../QUELLEN.md#q02) – Glossar VDV-KA / etiCORE, S. 100 („ZSAM-Zertifikat / ASAM certificate“: zusätzliches SAM-bezogenes Zertifikat, erforderlich für die Ausgabe eines VDV-Barcodes auf Basis einer statischen Berechtigung), S. 100 („Zertifizierung“ als Rolle des Scheme Manager)
- [Q25](../../QUELLEN.md#q25) – eTicket-Regelwerk, Kap. 3 (KA SAM-SPEC, Inventarnummer 8, als Normquelle des Zertifikatsaufbaus)

<!-- GEN:navigation -->
---

**Navigation:** [Home](../../README.md) · [Sicherheit](../sicherheit.md) · [Register](../../REGISTER.md)
<!-- /GEN:navigation -->
