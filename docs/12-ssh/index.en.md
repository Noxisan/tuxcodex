---
title: "SSH"
icon: material/console-network-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-console-network-outline:{ .tc-hero-icon }

# SSH

Logging in to servers securely, working with keys instead of passwords, copying files,
tunnelling connections and protecting the SSH server against attacks.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Host keys, key authentication, the files in `~/.ssh` and the client configuration :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Connect

<div class="grid cards" markdown>

-   :material-console-network:{ .lg .middle } **[ssh](ssh.md)**

    ---

    Log in, run commands and tunnel connections.

</div>

## Keys

<div class="grid cards" markdown>

-   :material-key-plus:{ .lg .middle } **[ssh-keygen](ssh-keygen.md)**

    ---

    Create and manage SSH keys.

-   :material-key-arrow-right:{ .lg .middle } **[ssh-copy-id](ssh-copy-id.md)**

    ---

    Put your public key on a server.

-   :material-account-key-outline:{ .lg .middle } **[ssh-agent](ssh-agent.md)**

    ---

    Keep unlocked keys in memory.

-   :material-key-chain-variant:{ .lg .middle } **[ssh-add](ssh-add.md)**

    ---

    Load keys into the agent.

</div>

## Transfer files

<div class="grid cards" markdown>

-   :material-file-swap-outline:{ .lg .middle } **[scp](scp.md)**

    ---

    Copy files over SSH.

-   :material-folder-network-outline:{ .lg .middle } **[sftp](sftp.md)**

    ---

    Interactive file transfer over SSH.

-   :material-folder-sync-outline:{ .lg .middle } **[rsync](rsync.md)**

    ---

    Synchronise files, only changes are sent.

</div>

## Server

<div class="grid cards" markdown>

-   :material-server-security:{ .lg .middle } **[sshd](sshd.md)**

    ---

    Check and harden the SSH server.

-   :material-fingerprint:{ .lg .middle } **[ssh-keyscan](ssh-keyscan.md)**

    ---

    Fetch and check host keys.

</div>

## Hardening

<div class="grid cards" markdown>

-   :material-shield-alert-outline:{ .lg .middle } **[fail2ban-client](fail2ban-client.md)**

    ---

    Ban attackers after failed logins.

</div>
