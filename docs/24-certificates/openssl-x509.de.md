# openssl x509

> Zeigt und konvertiert Zertifikate: Name, Aussteller, Gültigkeit, alternative Namen und Fingerabdrücke.

![openssl-x509 output](../assets/screenshots/24-certificates/openssl-x509.png)

## Syntax

```bash
openssl x509 -in DATEI [-noout] [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-in DATEI` | Zertifikatsdatei; ohne Angabe wird von der Standardeingabe gelesen |
| `-noout` | Das Zertifikat selbst nicht ausgeben, nur die gewünschten Felder |
| `-text` | Alles in lesbarer Form |
| `-subject`, `-issuer`, `-dates` | Inhaber, Aussteller, Gültigkeit |
| `-ext subjectAltName` | Die Hostnamen, für die das Zertifikat gilt |
| `-checkend SEKUNDEN` | Exit-Code 1, wenn das Zertifikat in dieser Zeit abläuft |
| `-fingerprint -sha256` | Fingerabdruck, um Zertifikate zu vergleichen |
| `-inform der -outform pem` | Zwischen DER und PEM umwandeln |

## Beispiele

**Namen, Aussteller und Gültigkeit:**

```bash
sudo openssl x509 -in /etc/letsencrypt/live/status.example.com/cert.pem -noout -subject -issuer -dates -ext subjectAltName
```

```text
subject=CN=status.example.com
issuer=C=US, O=Let's Encrypt, CN=R13
notBefore=Oct  1 08:15:12 2026 GMT
notAfter=Dec 30 08:15:11 2026 GMT
X509v3 Subject Alternative Name:
    DNS:status.example.com, DNS:www.status.example.com
```

**Prüfen, ob es in den nächsten 30 Tagen abläuft:**

```bash
sudo openssl x509 -in /etc/letsencrypt/live/status.example.com/cert.pem -noout -checkend $((30*86400))
echo "exit code: $?"
```

```text
Certificate will not expire
exit code: 0
```

**Das vollständige Zertifikat:**

```bash
sudo openssl x509 -in /etc/letsencrypt/live/status.example.com/cert.pem -noout -text | head -24
```

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            48:cc:34:4e:3c:b0:32:bd:78:74:83:4e:00:cf:32:55:7b:57:13:5a
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, O=Let's Encrypt, CN=R13
        Validity
            Not Before: Oct  1 08:15:12 2026 GMT
            Not After : Dec 30 08:15:11 2026 GMT
        Subject: CN=status.example.com
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
                    04:39:a4:20:28:25:5c:6c:58:aa:a3:cb:b8:8b:88:
                    4d:58:fc:15:a3:25:f4:5f:1d:e9:f5:7e:d9:90:d0:
                    59:8a:76:ed:2c:dd:fa:d4:32:17:06:5e:ee:ce:c1:
                    4a:35:16:7e:a3:1b:e0:4e:42:5b:25:5e:53:0e:15:
                    a7:19:b2:65:b2
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Basic Constraints: critical
```

**Prüfen, ob Schlüssel und Zertifikat zusammengehören:**

```bash
sudo openssl x509 -noout -pubkey -in /etc/letsencrypt/live/status.example.com/cert.pem | openssl sha256
sudo openssl pkey -pubout -in /etc/letsencrypt/live/status.example.com/privkey.pem | openssl sha256
```

```text
SHA2-256(stdin)= 19817f946442cef5830e80b2b8b250e672a0281c4c6e250e5820c0c688720120
SHA2-256(stdin)= 19817f946442cef5830e80b2b8b250e672a0281c4c6e250e5820c0c688720120
```

**Der Fingerabdruck:**

```bash
sudo openssl x509 -in /etc/letsencrypt/live/status.example.com/cert.pem -noout -fingerprint -sha256
```

```text
sha256 Fingerprint=9C:3F:E1:76:FB:BE:BD:4C:C9:A7:28:22:9B:16:40:6A:B1:BB:3D:50:0F:1E:DD:6C:BA:E6:C0:15:17:7D:1C:05
```

## Wann brauche ich das?

- Um zu prüfen, welche Namen und welche Gültigkeit eine Zertifikatsdatei hat
- In Monitoring-Skripten, um vor dem Ablauf eines Zertifikats zu warnen
- Um zu prüfen, ob ein Zertifikat und ein privater Schlüssel zusammengehören

!!! tip "Passt der Schlüssel zum Zertifikat?"
    Vergleiche die öffentlichen Schlüssel: `openssl x509 -noout -pubkey -in cert.pem |
    openssl sha256` und `openssl pkey -pubout -in privkey.pem | openssl sha256` müssen
    denselben Wert ausgeben. Sonst startet nginx nicht und meldet `key values mismatch`.

## Verwandte Befehle

[openssl s_client](openssl-s_client.md) · [openssl req](openssl-req.md) · [certbot](certbot.md) · [sha256sum](../14-archives/sha256sum.md)
