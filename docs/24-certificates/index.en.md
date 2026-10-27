---
icon: material/certificate-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-certificate-outline:{ .tc-hero-icon }

# Certificates and encryption

TLS certificates for your servers: checking what a server delivers, creating keys and
certificate requests, getting free certificates from Let's Encrypt, and encrypting files
for backups and transfers.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** How TLS works, certificate chains, file formats, where certificates live and what to install :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Checking certificates

<div class="grid cards" markdown>

-   :material-connection:{ .lg .middle } **[openssl s_client](openssl-s_client.md)**

    ---

    What a server delivers: chain, protocol, cipher.

-   :material-card-account-details-outline:{ .lg .middle } **[openssl x509](openssl-x509.md)**

    ---

    Names, validity and fingerprints.

-   :material-shield-search:{ .lg .middle } **[testssl.sh](testssl.md)**

    ---

    Full TLS check with a grade.

</div>

## Creating keys and certificates

<div class="grid cards" markdown>

-   :material-key-plus:{ .lg .middle } **[openssl genpkey](openssl-genpkey.md)**

    ---

    Create private keys.

-   :material-file-certificate-outline:{ .lg .middle } **[openssl req](openssl-req.md)**

    ---

    Certificate requests and self-signed certificates.

</div>

## Let's Encrypt

<div class="grid cards" markdown>

-   :material-certificate-outline:{ .lg .middle } **[certbot](certbot.md)**

    ---

    Free certificates, renewed automatically.

</div>

## Encrypting files

<div class="grid cards" markdown>

-   :material-lock-outline:{ .lg .middle } **[gpg](gpg.md)**

    ---

    Encrypt, sign and verify.

-   :material-file-lock-outline:{ .lg .middle } **[age](age.md)**

    ---

    Simple file encryption.

</div>
