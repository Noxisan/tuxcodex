# testssl.sh

> Prüft die TLS-Konfiguration eines Servers gründlich: Protokolle, Verschlüsselung, Zertifikat, Header und bekannte Schwächen, mit einer Note.

![testssl output](../assets/screenshots/24-certificates/testssl.png)

## Syntax

```bash
testssl.sh [OPTIONEN] HOST[:PORT]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| (keine) | Alle Tests, dauert etwa eine Minute |
| `-p` | Nur die Protokolle |
| `-S` | Nur die Server-Voreinstellungen und das Zertifikat |
| `-h` | Nur die HTTP-Sicherheits-Header |
| `-U` | Nur die bekannten Schwachstellen (Heartbleed, ROBOT, ...) |
| `--quiet` | Ohne das Banner |
| `--severity HIGH` | Nur Funde ab diesem Schweregrad melden |
| `--jsonfile DATEI`, `--htmlfile DATEI` | Die Ergebnisse speichern |
| `--starttls smtp` | Mailserver und andere STARTTLS-Dienste |

## Beispiele

**Die Protokolle prüfen:**

```bash
testssl.sh --quiet -p status.example.com
```

```text
 Start 2026-10-26 10:42:17        -->> 198.51.100.7:443 (status.example.com) <<--

 Testing protocols via sockets except NPN+ALPN

 SSLv2      not offered (OK)
 SSLv3      not offered (OK)
 TLS 1      not offered
 TLS 1.1    not offered
 TLS 1.2    offered (OK)
 TLS 1.3    offered (OK): final
 NPN/SPDY   not offered
 ALPN/HTTP2 http/1.1 (offered)

 Done 2026-10-26 10:42:21 [   5s] -->> 198.51.100.7:443 (status.example.com) <<--
```

**Zertifikat und Server-Voreinstellungen:**

```bash
testssl.sh --quiet -S status.example.com | sed -n '/Signature Algorithm/,/Intermediate cert/p'
```

```text
 Signature Algorithm          SHA256 with RSA
 Server key size              EC 256 bits (curve P-256)
 Server key usage             Digital Signature
 Server extended key usage    TLS Web Server Authentication, TLS Web Client Authentication
 Serial                       48CC344E3CB032BD7874834E00CF32557B57135A (OK: length 20)
 Fingerprints                 SHA1 F23ED1761E4DEB37AF9C03DF6E78F0A046456FDB
                              SHA256 9C3FE176FBBEBD4CC9A728229B16406AB1BB3D500F1EDD6CBAE6C015177D1C05
 Common Name (CN)             status.example.com
 subjectAltName (SAN)         status.example.com www.status.example.com
 Trust (hostname)             Ok via SAN and CN (same w/o SNI)
 Chain of trust               Ok
 EV cert (experimental)       no
 Certificate Validity (UTC)   64 >= 30 days (2026-10-01 08:15 --> 2026-12-30 08:15)
 Certificate Revocation List  http://r13.c.lencr.org/112.crl
 OCSP URI                     --
 OCSP stapling                not offered
 Certificates provided        2
 Issuer                       R13 (Let's Encrypt from US)
 Intermediate cert validity   #1: ok > 40 days (2027-03-12 23:59). R13 <-- ISRG Root X1
```

**Die Note am Ende eines vollständigen Laufs:**

```bash
testssl.sh --quiet status.example.com | grep -A8 'Rating (experimental)'
```

```text
 Rating (experimental)

 Rating specs (not complete)  SSL Labs's 'SSL Server Rating Guide' (version 2009r from 2025-05-16)
 Specification documentation  https://github.com/ssllabs/research/wiki/SSL-Server-Rating-Guide
 Protocol Support (weighted)  100 (30)
 Key Exchange     (weighted)  100 (30)
 Cipher Strength  (weighted)  90 (36)
 Final Score                  96
 Overall Grade                A+
```

Für A+ braucht es unter anderem HSTS (`Strict-Transport-Security`) von mindestens sechs Monaten.

## Wann brauche ich das?

- Nach dem Einrichten von HTTPS auf einem Server, als abschließende Prüfung
- Nach Änderungen an Protokollen oder Verschlüsselung in nginx oder Apache
- Regelmäßig, weil neue Schwächen bekannt werden

!!! tip "Wie SSL Labs, aber lokal"
    testssl.sh bewertet ähnlich wie die Website von SSL Labs, funktioniert aber auch für
    interne Server, Mailserver und andere Ports, und die Ergebnisse bleiben bei dir.

!!! warning "Nur eigene Server"
    testssl.sh öffnet Hunderte Verbindungen. Wie bei jedem Scan: Prüfe nur Server, die du
    verwaltest, siehe das Kapitel [Sicherheitsprüfung](../23-security-scanning/basics.md).

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install testssl.sh` | `sudo apt install testssl.sh` | von GitHub (`testssl/testssl.sh`) | `sudo pacman -S testssl.sh` |

## Verwandte Befehle

[openssl s_client](openssl-s_client.md) · [certbot](certbot.md) · [nmap](../23-security-scanning/nmap.md)
