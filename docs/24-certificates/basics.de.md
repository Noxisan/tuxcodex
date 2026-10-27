# Zertifikate verstehen

TLS (das „S“ in HTTPS) leistet zwei Dinge: Es verschlüsselt die Verbindung, und es beweist,
dass der Server wirklich `status.example.com` ist. Der Beweis ist das **Zertifikat**: ein
öffentlicher Schlüssel plus der Name des Servers, unterschrieben von einer
Zertifizierungsstelle (CA), der Browser und Betriebssysteme vertrauen.

## Schlüsselpaar und Zertifikat

| Teil | Was es ist | Wer es sehen darf |
|------|------------|-------------------|
| **Privater Schlüssel** | Die geheime Hälfte, bleibt auf dem Server, Datei `privkey.pem` oder `*.key` | Nur root und der Webserver |
| **Zertifikat** | Öffentlicher Schlüssel, Name(n), Gültigkeit, Unterschrift der CA | Alle, der Server schickt es bei jeder Verbindung mit |
| **CSR** | Certificate Signing Request: was du an eine CA schickst, um ein Zertifikat zu bekommen | Die CA |

## Die Vertrauenskette

```text
ISRG Root X1                 root certificate, built into browsers and the OS
   └── R13                   intermediate certificate of Let's Encrypt
         └── status.example.com    your server certificate, valid for 90 days
```

Der Server muss sein eigenes Zertifikat **und** das Zwischenzertifikat mitschicken
(`fullchain.pem`). Fehlt das Zwischenzertifikat, melden viele Clients „unable to verify“,
auch wenn Browser oft trotzdem funktionieren.

## Dateiformate

| Format | Endung | Inhalt |
|--------|--------|--------|
| **PEM** | `.pem`, `.crt`, `.key` | Text mit `-----BEGIN ...-----`, der Standard unter Linux |
| **DER** | `.der`, `.cer` | Dasselbe, binär |
| **PKCS#12** | `.p12`, `.pfx` | Zertifikat, Kette und privater Schlüssel in einer passwortgeschützten Datei (Windows, Java) |

[`openssl x509`](openssl-x509.md) zeigt den Inhalt jedes dieser Formate.

## Wo Zertifikate liegen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Vertrauenswürdige CAs (Bundle) | `/etc/ssl/certs/ca-certificates.crt` | `/etc/ssl/certs/ca-certificates.crt` | `/etc/pki/tls/certs/ca-bundle.crt` | `/etc/ssl/certs/ca-certificates.crt` |
| Eigene CA hinzufügen | nach `/usr/local/share/ca-certificates/` kopieren, dann `update-ca-certificates` | nach `/usr/local/share/ca-certificates/` kopieren, dann `update-ca-certificates` | nach `/etc/pki/ca-trust/source/anchors/` kopieren, dann `update-ca-trust` | `trust anchor DATEI` |
| Let's-Encrypt-Zertifikate | `/etc/letsencrypt/live/NAME/` | `/etc/letsencrypt/live/NAME/` | `/etc/letsencrypt/live/NAME/` | `/etc/letsencrypt/live/NAME/` |

## Was du installieren musst

| Werkzeug | Debian | Ubuntu | RHEL | Arch |
|----------|--------|--------|------|------|
| openssl | vorinstalliert | vorinstalliert | vorinstalliert | vorinstalliert |
| certbot | `sudo apt install certbot python3-certbot-nginx` | `sudo apt install certbot python3-certbot-nginx` | `sudo dnf install certbot python3-certbot-nginx` (EPEL) | `sudo pacman -S certbot certbot-nginx` |
| testssl.sh | `sudo apt install testssl.sh` | `sudo apt install testssl.sh` | von GitHub (`testssl/testssl.sh`) | `sudo pacman -S testssl.sh` |
| gpg | vorinstalliert | vorinstalliert | vorinstalliert | vorinstalliert |
| age | `sudo apt install age` | `sudo apt install age` | `sudo dnf install age` (EPEL) | `sudo pacman -S age` |

## Dateien verschlüsseln

Zertifikate schützen Verbindungen. Für Dateien wie Backups gibt es zwei Werkzeuge:

| | [`gpg`](gpg.md) | [`age`](age.md) |
|---|-----------------|-----------------|
| Zweck | Verschlüsseln und signieren, Mail, Pakete | Nur Dateien verschlüsseln |
| Schlüssel | Schlüsselbund mit Ablaufdatum, Vertrauen, Unterschlüsseln | Eine Zeile pro Schlüssel |
| Typischer Einsatz | Paketsignaturen, verschlüsselte Mail, bestehende Setups | Backups, Geheimnisse in Skripten und Git |

!!! tip "Das Ablaufdatum im Blick behalten"
    Ein abgelaufenes Zertifikat legt einen Dienst für alle Clients lahm. Prüfe die
    Restlaufzeit im Monitoring, etwa mit `openssl x509 -checkend`, und lass `certbot`
    automatisch erneuern.

!!! danger "Private Schlüssel schützen"
    Wer den privaten Schlüssel hat, kann sich als dein Server ausgeben. Er braucht die
    Rechte `600`, gehört root, kommt nie in ein Git-Repository und wird nie per Mail
    verschickt. Ist ein Schlüssel nach außen gelangt, widerrufe das Zertifikat und erstelle
    einen neuen Schlüssel.
