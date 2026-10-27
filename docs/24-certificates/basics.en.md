# Understanding certificates

TLS (the "S" in HTTPS) does two things: it encrypts the connection, and it proves that the
server really is `status.example.com`. The proof is the **certificate**: a public key plus
the name of the server, signed by a certificate authority (CA) that browsers and operating
systems trust.

## Key pair and certificate

| Part | What it is | Who may see it |
|------|------------|----------------|
| **Private key** | The secret half, stays on the server, file `privkey.pem` or `*.key` | Only root and the web server |
| **Certificate** | Public key, name(s), validity, signature of the CA | Everyone, the server sends it with every connection |
| **CSR** | Certificate signing request: what you send to a CA to get a certificate | The CA |

## The chain of trust

```text
ISRG Root X1                 root certificate, built into browsers and the OS
   └── R13                   intermediate certificate of Let's Encrypt
         └── status.example.com    your server certificate, valid for 90 days
```

The server has to send its own certificate **and** the intermediate certificate
(`fullchain.pem`). If the intermediate is missing, many clients report "unable to verify",
even though browsers often still work.

## File formats

| Format | Extension | Content |
|--------|-----------|---------|
| **PEM** | `.pem`, `.crt`, `.key` | Text with `-----BEGIN ...-----`, the standard on Linux |
| **DER** | `.der`, `.cer` | The same, binary |
| **PKCS#12** | `.p12`, `.pfx` | Certificate, chain and private key in one password-protected file (Windows, Java) |

[`openssl x509`](openssl-x509.md) shows the content of any of them.

## Where certificates live

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Trusted CAs (bundle) | `/etc/ssl/certs/ca-certificates.crt` | `/etc/ssl/certs/ca-certificates.crt` | `/etc/pki/tls/certs/ca-bundle.crt` | `/etc/ssl/certs/ca-certificates.crt` |
| Add your own CA | copy to `/usr/local/share/ca-certificates/`, then `update-ca-certificates` | copy to `/usr/local/share/ca-certificates/`, then `update-ca-certificates` | copy to `/etc/pki/ca-trust/source/anchors/`, then `update-ca-trust` | `trust anchor FILE` |
| Let's Encrypt certificates | `/etc/letsencrypt/live/NAME/` | `/etc/letsencrypt/live/NAME/` | `/etc/letsencrypt/live/NAME/` | `/etc/letsencrypt/live/NAME/` |

## What you need to install

| Tool | Debian | Ubuntu | RHEL | Arch |
|------|--------|--------|------|------|
| openssl | preinstalled | preinstalled | preinstalled | preinstalled |
| certbot | `sudo apt install certbot python3-certbot-nginx` | `sudo apt install certbot python3-certbot-nginx` | `sudo dnf install certbot python3-certbot-nginx` (EPEL) | `sudo pacman -S certbot certbot-nginx` |
| testssl.sh | `sudo apt install testssl.sh` | `sudo apt install testssl.sh` | from GitHub (`testssl/testssl.sh`) | `sudo pacman -S testssl.sh` |
| gpg | preinstalled | preinstalled | preinstalled | preinstalled |
| age | `sudo apt install age` | `sudo apt install age` | `sudo dnf install age` (EPEL) | `sudo pacman -S age` |

## Encrypting files

Certificates protect connections. For files such as backups, there are two tools:

| | [`gpg`](gpg.md) | [`age`](age.md) |
|---|-----------------|-----------------|
| Use | Encrypt and sign, mail, packages | Only encrypt files |
| Keys | Key ring with expiry, trust, subkeys | One line per key |
| Typical use | Package signatures, encrypted mail, existing setups | Backups, secrets in scripts and Git |

!!! tip "Watch the expiry date"
    An expired certificate takes a service offline for every client. Check the remaining
    days in your monitoring, for example with `openssl x509 -checkend`, and let `certbot`
    renew automatically.

!!! danger "Protect private keys"
    Whoever has the private key can impersonate your server. It needs mode `600`, belongs
    to root, never goes into a Git repository and is never sent by mail. If a key leaks,
    revoke the certificate and create a new key.
