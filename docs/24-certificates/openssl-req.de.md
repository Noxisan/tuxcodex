# openssl req

> Erstellt Zertifikatsanfragen (CSR) für eine CA oder selbstsignierte Zertifikate für den internen Einsatz.

![openssl-req output](../assets/screenshots/24-certificates/openssl-req.png)

## Syntax

```bash
openssl req -new -key SCHLÜSSEL -out CSR [OPTIONEN]
openssl req -x509 -newkey ALG -keyout SCHLÜSSEL -out ZERT [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-new -key DATEI` | Einen CSR für einen vorhandenen Schlüssel erstellen |
| `-x509` | Ein selbstsigniertes Zertifikat statt eines CSR erstellen |
| `-newkey ec -pkeyopt ec_paramgen_curve:P-256` | Gleichzeitig einen neuen Schlüssel erstellen |
| `-nodes` | Den neuen Schlüssel nicht mit einem Passwort schützen (nötig für Dienste) |
| `-subj "/CN=NAME"` | Inhaber ohne Rückfragen |
| `-addext "subjectAltName=DNS:..."` | Hostnamen; Clients prüfen nur den SAN, nicht den CN |
| `-days N` | Gültigkeit eines selbstsignierten Zertifikats |
| `-in CSR -noout -text` | Einen CSR anzeigen |

## Beispiele

**Ein CSR für einen vorhandenen Schlüssel:**

```bash
openssl req -new -key status.key -out status.csr -subj "/CN=status.example.com" \
  -addext "subjectAltName=DNS:status.example.com,DNS:www.status.example.com"
openssl req -in status.csr -noout -subject -text | grep -A1 "Alternative Name"
```

```text
subject=CN=status.example.com
                X509v3 Subject Alternative Name:
                    DNS:status.example.com, DNS:www.status.example.com
```

**Ein selbstsigniertes Zertifikat für einen internen Dienst:**

```bash
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:P-256 -nodes \
  -keyout monitor.key -out monitor.crt -days 365 \
  -subj "/CN=monitor.internal.example.com" \
  -addext "subjectAltName=DNS:monitor.internal.example.com"
openssl x509 -in monitor.crt -noout -subject -issuer -dates
```

```text
-----
subject=CN=monitor.internal.example.com
issuer=CN=monitor.internal.example.com
notBefore=Oct 26 09:42:17 2026 GMT
notAfter=Oct 26 09:42:17 2027 GMT
```

Inhaber und Aussteller sind gleich: Genau das macht ein Zertifikat selbstsigniert.

**Der Inhalt eines CSR:**

```bash
openssl req -in status.csr -noout -text | head -8
```

```text
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN=status.example.com
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
```

## Wann brauche ich das?

- Um ein Zertifikat bei einer kommerziellen CA oder einer internen Firmen-CA zu beantragen
- Für interne Dienste, die nur eigene Rechner nutzen, mit einem selbstsignierten Zertifikat
- Um zu prüfen, was ein CSR enthält, bevor du ihn abschickst

!!! tip "Immer subjectAltName setzen"
    Browser und aktuelle Werkzeuge ignorieren den CN und prüfen nur `subjectAltName`. Ein
    Zertifikat ohne wird abgelehnt, auch wenn der CN stimmt.

!!! warning "Selbstsigniert heißt: niemand vertraut ihm"
    Clients lehnen ein selbstsigniertes Zertifikat ab, bis es oder deine eigene CA als
    vertrauenswürdig installiert ist, siehe die [Grundlagen](basics.md). Für alles
    Öffentliche nimm Let's Encrypt.

## Verwandte Befehle

[openssl genpkey](openssl-genpkey.md) · [openssl x509](openssl-x509.md) · [certbot](certbot.md)
