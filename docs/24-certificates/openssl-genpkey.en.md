# openssl genpkey

> Creates private keys: RSA, elliptic curve (EC) or Ed25519.

![openssl-genpkey output](../assets/screenshots/24-certificates/openssl-genpkey.png)

## Syntax

```bash
openssl genpkey -algorithm ALGORITHM [-pkeyopt OPTION] -out FILE
```

## Options

| Option | Description |
|--------|-------------|
| `-algorithm EC -pkeyopt ec_paramgen_curve:P-256` | Elliptic curve key, the usual choice for TLS today |
| `-algorithm RSA -pkeyopt rsa_keygen_bits:4096` | RSA key, for old clients and some devices |
| `-algorithm ED25519` | Ed25519, small and fast, not yet accepted by every CA |
| `-out FILE` | Key file (created with mode `600`) |
| `-aes-256-cbc` | Protect the key with a password |

`openssl pkey -in FILE -noout -text` shows a key, `openssl pkey -in FILE -pubout` its public part.

## Examples

**An EC key for a server:**

```bash
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out status.key
ls -l status.key
```

```text
-rw------- 1 nox nox 241 Oct 26 10:42 status.key
```

**What's in the key:**

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

**An RSA key for old clients:**

```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out legacy.key 2>/dev/null
ls -l legacy.key
```

```text
-rw------- 1 nox nox 3272 Oct 26 10:42 legacy.key
```

Without `2>/dev/null`, OpenSSL prints rows of `.+++` while it searches for primes.

**An Ed25519 key is just one line:**

```bash
openssl genpkey -algorithm ED25519 -out sign.key
cat sign.key
```

```text
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEII31ugQAB88DM5A7BHnhAbw0i90cnLQF2BuLwKLkhtzN
-----END PRIVATE KEY-----
```

## When do I need it?

- Before requesting a certificate from a CA with your own key
- For internal certificates, VPNs or signing keys
- To renew a key after a leak or when switching from RSA to EC

!!! tip "EC P-256 for servers"
    An EC key with P-256 is as strong as RSA 3072, much smaller and faster in the handshake,
    and every current client supports it. certbot uses ECDSA by default too.

!!! danger "Never share the private key"
    The file contains the secret key in plain text. Keep it on the server with mode `600`,
    and never copy it to tickets, chats or repositories.

## Related commands

[openssl req](openssl-req.md) · [openssl x509](openssl-x509.md) · [ssh-keygen](../12-ssh/ssh-keygen.md)
