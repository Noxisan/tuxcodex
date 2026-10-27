# openssl genpkey

> Erstellt private Schlüssel: RSA, elliptische Kurven (EC) oder Ed25519.

![openssl-genpkey output](../assets/screenshots/24-certificates/openssl-genpkey.png)

## Syntax

```bash
openssl genpkey -algorithm ALGORITHMUS [-pkeyopt OPTION] -out DATEI
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-algorithm EC -pkeyopt ec_paramgen_curve:P-256` | Schlüssel mit elliptischer Kurve, heute die übliche Wahl für TLS |
| `-algorithm RSA -pkeyopt rsa_keygen_bits:4096` | RSA-Schlüssel, für alte Clients und manche Geräte |
| `-algorithm ED25519` | Ed25519, klein und schnell, noch nicht von jeder CA akzeptiert |
| `-out DATEI` | Schlüsseldatei (wird mit den Rechten `600` angelegt) |
| `-aes-256-cbc` | Den Schlüssel mit einem Passwort schützen |

`openssl pkey -in DATEI -noout -text` zeigt einen Schlüssel, `openssl pkey -in DATEI -pubout` seinen öffentlichen Teil.

## Beispiele

**Ein EC-Schlüssel für einen Server:**

```bash
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out status.key
ls -l status.key
```

```text
-rw------- 1 nox nox 241 Oct 26 10:42 status.key
```

**Was im Schlüssel steckt:**

```bash
openssl pkey -in status.key -noout -text | head -6
```

```text
Private-Key: (256 bit)
priv:
    7d:3a:ef:5c:00:e4:be:ed:0f:e7:1a:c6:10:36:e1:
    7f:c7:de:f6:d1:d9:9f:cc:e8:e4:49:a5:79:d5:26:
    4f:80
pub:
```

**Ein RSA-Schlüssel für alte Clients:**

```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out legacy.key 2>/dev/null
ls -l legacy.key
```

```text
-rw------- 1 nox nox 3272 Oct 26 10:42 legacy.key
```

Ohne `2>/dev/null` gibt OpenSSL Reihen von `.+++` aus, während es nach Primzahlen sucht.

**Ein Ed25519-Schlüssel ist nur eine Zeile:**

```bash
openssl genpkey -algorithm ED25519 -out sign.key
cat sign.key
```

```text
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEII31ugQAB88DM5A7BHnhAbw0i90cnLQF2BuLwKLkhtzN
-----END PRIVATE KEY-----
```

## Wann brauche ich das?

- Bevor du bei einer CA ein Zertifikat mit eigenem Schlüssel beantragst
- Für interne Zertifikate, VPNs oder Signaturschlüssel
- Um einen Schlüssel nach einem Leck zu erneuern oder von RSA auf EC umzusteigen

!!! tip "EC P-256 für Server"
    Ein EC-Schlüssel mit P-256 ist so stark wie RSA 3072, viel kleiner und schneller im
    Handshake, und jeder aktuelle Client unterstützt ihn. Auch certbot nutzt standardmäßig
    ECDSA.

!!! danger "Den privaten Schlüssel nie weitergeben"
    Die Datei enthält den geheimen Schlüssel im Klartext. Lass ihn mit den Rechten `600` auf
    dem Server und kopiere ihn nie in Tickets, Chats oder Repositorys.

## Verwandte Befehle

[openssl req](openssl-req.md) · [openssl x509](openssl-x509.md) · [ssh-keygen](../12-ssh/ssh-keygen.md)
