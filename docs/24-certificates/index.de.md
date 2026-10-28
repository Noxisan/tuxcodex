---
title: "Zertifikate und Verschlüsselung"
icon: material/certificate-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-certificate-outline:{ .tc-hero-icon }

# Zertifikate und Verschlüsselung

TLS-Zertifikate für deine Server: prüfen, was ein Server ausliefert, Schlüssel und
Zertifikatsanfragen erstellen, kostenlose Zertifikate von Let's Encrypt holen und Dateien
für Backups und Übertragungen verschlüsseln.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Wie TLS funktioniert, Zertifikatsketten, Dateiformate, wo Zertifikate liegen und was du installieren musst :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Zertifikate prüfen

<div class="grid cards" markdown>

-   :material-connection:{ .lg .middle } **[openssl s_client](openssl-s_client.md)**

    ---

    Was ein Server ausliefert: Kette, Protokoll, Verschlüsselung.

-   :material-card-account-details-outline:{ .lg .middle } **[openssl x509](openssl-x509.md)**

    ---

    Namen, Gültigkeit und Fingerabdrücke.

-   :material-shield-search:{ .lg .middle } **[testssl.sh](testssl.md)**

    ---

    Vollständige TLS-Prüfung mit Note.

</div>

## Schlüssel und Zertifikate erstellen

<div class="grid cards" markdown>

-   :material-key-plus:{ .lg .middle } **[openssl genpkey](openssl-genpkey.md)**

    ---

    Private Schlüssel erstellen.

-   :material-file-certificate-outline:{ .lg .middle } **[openssl req](openssl-req.md)**

    ---

    Zertifikatsanfragen und selbstsignierte Zertifikate.

</div>

## Let's Encrypt

<div class="grid cards" markdown>

-   :material-certificate-outline:{ .lg .middle } **[certbot](certbot.md)**

    ---

    Kostenlose Zertifikate, automatisch erneuert.

</div>

## Dateien verschlüsseln

<div class="grid cards" markdown>

-   :material-lock-outline:{ .lg .middle } **[gpg](gpg.md)**

    ---

    Verschlüsseln, signieren und prüfen.

-   :material-file-lock-outline:{ .lg .middle } **[age](age.md)**

    ---

    Einfache Dateiverschlüsselung.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-console-network:{ .lg .middle } **[ssh-keygen](../12-ssh/ssh-keygen.md)**

    ---

    SSH-Schlüssel funktionieren wie TLS-Schlüsselpaare; age kann sie sogar nutzen. Behandelt im Kapitel SSH.

-   :material-pound:{ .lg .middle } **[sha256sum](../14-archives/sha256sum.md)**

    ---

    Downloads und Backups mit Prüfsummen kontrollieren. Behandelt im Kapitel Archive.

-   :material-lock-outline:{ .lg .middle } **[ansible-vault](../21-ansible/ansible-vault.md)**

    ---

    Passwörter in Ansible-Projekten verschlüsseln. Behandelt im Kapitel Ansible.

</div>
