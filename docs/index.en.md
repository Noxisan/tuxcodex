---
icon: material/home
hide:
  - toc
---

<div class="tc-hero" markdown>

# TuxDex { .tc-sr-only }

![TuxDex Logo](assets/logo-hero.png){ width="350" }

Linux commands. Real-world examples. No guesswork.
{ .tc-tagline }

A practical reference for **Linux administration, server operations, and DevOps** with
command syntax, working examples, and tips for real-world scenarios.

<div class="tc-distros" markdown>
<span class="tc-badge tc-badge--debian" markdown="span">:simple-debian: Debian</span>
<span class="tc-badge tc-badge--ubuntu" markdown="span">:simple-ubuntu: Ubuntu</span>
<span class="tc-badge tc-badge--redhat" markdown="span">:simple-redhat: RHEL</span>
<span class="tc-badge tc-badge--arch" markdown="span">:simple-archlinux: Arch</span>
</div>

English · German
{ .tc-languages }

Built by [:simple-github: Nox](https://github.com/Noxisan){ .tc-author }

</div>

## Linux administration

<div class="grid cards" markdown>

-   :material-compass-outline:{ .lg .middle } **[Orientation](01-orientation/index.md)**

    ---

    Who am I, where am I, and what is going on on this machine?

-   :material-folder-outline:{ .lg .middle } **[Navigation](02-navigation/index.md)**

    ---

    Moving around the file system and finding files.

-   :material-file-document-outline:{ .lg .middle } **[Files](03-files/index.md)**

    ---

    Creating, copying, moving and deleting files and directories.

-   :material-text-box-search-outline:{ .lg .middle } **[Viewing files](04-viewing-files/index.md)**

    ---

    Reading files and logs, also compressed and binary files.

-   :material-text-search:{ .lg .middle } **[Text processing](05-text-processing/index.md)**

    ---

    Searching, filtering, sorting and changing text in logs and configuration files.

-   :material-shield-lock-outline:{ .lg .middle } **[Permissions](06-permissions/index.md)**

    ---

    Owners, groups and access rights, and how to fix them.

-   :material-account-multiple-outline:{ .lg .middle } **[Users and groups](07-users-groups/index.md)**

    ---

    Creating and managing users and groups, `sudo` and `su`.

-   :material-cog-transfer-outline:{ .lg .middle } **[Processes](08-processes/index.md)**

    ---

    Finding, watching and stopping running programs.

-   :material-cog-sync-outline:{ .lg .middle } **[systemd and services](09-systemd/index.md)**

    ---

    Managing services, reading their logs and restarting the server cleanly.

-   :material-package-variant-closed:{ .lg .middle } **[Packages](10-packages/index.md)**

    ---

    Installing, updating and removing software with `apt`, `dnf` and `pacman`.

-   :material-lan:{ .lg .middle } **[Network](11-network/index.md)**

    ---

    Addresses, connections, DNS, downloads, network configuration and the firewall.

-   :material-console-network-outline:{ .lg .middle } **[SSH](12-ssh/index.md)**

    ---

    Logging in securely, keys, tunnels and copying files between servers.

-   :material-harddisk:{ .lg .middle } **[Disks and storage](13-disks-storage/index.md)**

    ---

    Partitions, file systems, mounting, disk space and LVM.

-   :material-archive-arrow-down-outline:{ .lg .middle } **[Archives](14-archives/index.md)**

    ---

    Packing and compressing with `tar`, `gzip`, `zstd` and `zip`.

-   :material-text-box-multiple-outline:{ .lg .middle } **[Logs](15-logs/index.md)**

    ---

    Kernel messages, log rotation, failed logins, audit and log analysis.

-   :material-calendar-clock:{ .lg .middle } **[Scheduling](16-scheduling/index.md)**

    ---

    Running jobs regularly with cron, `at` and systemd timers.

-   :material-speedometer:{ .lg .middle } **[Performance and kernel](27-performance/index.md)**

    ---

    Finding out why a server is slow, and tuning kernel parameters and limits.

-   :material-backup-restore:{ .lg .middle } **[Backup](28-backup/index.md)**

    ---

    Database dumps, encrypted backups with restic and borg, and testing the restore.

</div>

## Automation & DevOps

<div class="grid cards" markdown>

-   :material-script-text-outline:{ .lg .middle } **[Bash scripting](17-bash-scripting/index.md)**

    ---

    Variables, conditions, loops and functions for your own admin scripts.

-   :material-git:{ .lg .middle } **[Git](18-git/index.md)**

    ---

    Versioning configurations and scripts, branches and remotes.

-   :material-docker:{ .lg .middle } **[Docker](19-docker/index.md)**

    ---

    Running services in containers, images, volumes and Compose.

-   :material-kubernetes:{ .lg .middle } **[Kubernetes](20-kubernetes/index.md)**

    ---

    Running containers across many servers with `kubectl` and Helm.

-   :material-ansible:{ .lg .middle } **[Ansible](21-ansible/index.md)**

    ---

    Configuring many servers at once with playbooks.

-   :material-infinity:{ .lg .middle } **[CI/CD](22-ci-cd/index.md)**

    ---

    Testing and deploying automatically with pipelines.

</div>

## Security

<div class="grid cards" markdown>

-   :material-radar:{ .lg .middle } **[Security scanning](23-security-scanning/index.md)**

    ---

    Open ports, hardening, rootkits, file integrity and vulnerable images.

-   :material-certificate-outline:{ .lg .middle } **[Certificates and encryption](24-certificates/index.md)**

    ---

    TLS certificates, `openssl`, `gpg` and Let's Encrypt.

-   :material-shield-lock-outline:{ .lg .middle } **[SELinux and AppArmor](25-selinux-apparmor/index.md)**

    ---

    Fixing "Permission denied" properly instead of switching the protection off.

-   :material-vpn:{ .lg .middle } **[VPN with WireGuard](26-wireguard/index.md)**

    ---

    Encrypted tunnels between servers and admin machines, SSH only through the VPN.

</div>

## All commands

<!-- COMMAND_INDEX -->
