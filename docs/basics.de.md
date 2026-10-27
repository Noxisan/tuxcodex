---
icon: material/school-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-school-outline:{ .tc-hero-icon }

# Grundlagen im Überblick

Jedes Kapitel beginnt mit einer Grundlagen-Seite: die Begriffe, Tabellen und Abläufe, die
du brauchst, bevor die einzelnen Befehle Sinn ergeben. Hier stehen sie alle an einem Ort,
in der Reihenfolge des Handbuchs.

</div>

## Linux-Grundlagen

<div class="grid cards tc-basics-cards" markdown>

-   :material-compass-outline:{ .lg .middle } **[Die erste Minute auf einem neuen Server](01-orientation/basics.md)**

    ---

    Orientierung: als Befehlsfolge

-   :material-folder-outline:{ .lg .middle } **[Die wichtigsten Verzeichnisse auf einem Linux-Server](02-navigation/basics.md)**

    ---

    Navigation

-   :material-file-document-outline:{ .lg .middle } **[Sicher arbeiten mit Dateien](03-files/basics.md)**

    ---

    Dateien: Regeln für sicheres Arbeiten mit Dateien

-   :material-text-box-search-outline:{ .lg .middle } **[Logs lesen](04-viewing-files/basics.md)**

    ---

    Dateien anzeigen: der passende Befehl für jede Aufgabe

-   :material-text-search:{ .lg .middle } **[Befehle mit Pipes verbinden](05-text-processing/basics.md)**

    ---

    Textverarbeitung

-   :material-shield-lock-outline:{ .lg .middle } **[Rechte verstehen](06-permissions/basics.md)**

    ---

    Rechte: Besitzer, Gruppe, rwx und Oktalschreibweise erklärt

-   :material-account-multiple-outline:{ .lg .middle } **[Die wichtigen Dateien](07-users-groups/basics.md)**

    ---

    Benutzer und Gruppen: passwd, shadow, group, sudoers

-   :material-cog-transfer-outline:{ .lg .middle } **[Prozesse verstehen](08-processes/basics.md)**

    ---

    Prozesse: PID, Prozesszustände und Signale

-   :material-cog-sync-outline:{ .lg .middle } **[systemd verstehen](09-systemd/basics.md)**

    ---

    systemd und Dienste: Units, Unit-Dateien und ihre Zustände

-   :material-package-variant-closed:{ .lg .middle } **[Pakete verstehen](10-packages/basics.md)**

    ---

    Pakete: Paketquellen, Abhängigkeiten und `apt`, `dnf` und `pacman` im Vergleich

-   :material-lan:{ .lg .middle } **[Netzwerke verstehen](11-network/basics.md)**

    ---

    Netzwerk: IP-Adressen, Subnetze, Ports, DNS und wo jede Distribution ihre Netzwerkkonfiguration ablegt

-   :material-console-network-outline:{ .lg .middle } **[SSH verstehen](12-ssh/basics.md)**

    ---

    SSH: Host-Keys, Anmeldung per Schlüssel, die Dateien in `~/.ssh` und die Client-Konfiguration

-   :material-harddisk:{ .lg .middle } **[Speicher verstehen](13-disks-storage/basics.md)**

    ---

    Festplatten und Speicher: Blockgeräte, Partitionstabellen, Dateisysteme, `/etc/fstab` und LVM

-   :material-archive-arrow-down-outline:{ .lg .middle } **[Archive verstehen](14-archives/basics.md)**

    ---

    Archive: Archivieren und Komprimieren, Dateiendungen und die Verfahren im Vergleich

-   :material-text-box-multiple-outline:{ .lg .middle } **[Logs verstehen](15-logs/basics.md)**

    ---

    Logs: Wo Logs liegen, Log-Level und Logrotation

-   :material-calendar-clock:{ .lg .middle } **[Zeitsteuerung verstehen](16-scheduling/basics.md)**

    ---

    Zeitgesteuerte Aufgaben: cron-Syntax, wo Cronjobs liegen und systemd-Timer im Vergleich

-   :material-speedometer:{ .lg .middle } **[Leistung verstehen](27-performance/basics.md)**

    ---

    Leistung und Kernel: Die vier Ressourcen, Last richtig lesen, wo der Engpass liegt und was du installieren musst

-   :material-backup-restore:{ .lg .middle } **[Backups verstehen](28-backup/basics.md)**

    ---

    Backup: Die 3-2-1-Regel, was gesichert wird, restic oder borg und ein vollständiger Backup-Ablauf

</div>

## Automatisierung & DevOps

<div class="grid cards tc-basics-cards" markdown>

-   :material-script-text-outline:{ .lg .middle } **[Skripte verstehen](17-bash-scripting/basics.md)**

    ---

    Bash-Skripte: Wie ein Skript aufgebaut ist: Shebang, Quoting, Variablen, Argumente und Exit-Codes

-   :material-git:{ .lg .middle } **[Git verstehen](18-git/basics.md)**

    ---

    Git: Arbeitsverzeichnis, Staging-Bereich und Repository, `.gitignore`, SSH-Schlüssel und der tägliche Ablauf

-   :material-docker:{ .lg .middle } **[Docker verstehen](19-docker/basics.md)**

    ---

    Docker: Images und Container, Installation, Ports und Volumes, ein Dockerfile und eine compose.yaml

-   :material-kubernetes:{ .lg .middle } **[Kubernetes verstehen](20-kubernetes/basics.md)**

    ---

    Kubernetes: Was du installieren musst, Pods, Deployments und Services, Manifeste und kubeconfig

-   :material-ansible:{ .lg .middle } **[Ansible verstehen](21-ansible/basics.md)**

    ---

    Ansible: Steuerrechner und verwaltete Server, Inventar, Module, Playbooks, Rollen und Installation

-   :material-infinity:{ .lg .middle } **[CI/CD verstehen](22-ci-cd/basics.md)**

    ---

    CI/CD: Pipelines, Jobs und Runner, was du installieren musst, ein Workflow für GitHub und einer für GitLab

</div>

## Sicherheit

<div class="grid cards tc-basics-cards" markdown>

-   :material-radar:{ .lg .middle } **[Sicherheitsprüfung verstehen](23-security-scanning/basics.md)**

    ---

    Sicherheitsprüfung: Angriffsfläche, was welches Werkzeug findet, was du installieren musst, und die Regeln fürs Scannen

-   :material-certificate-outline:{ .lg .middle } **[Zertifikate verstehen](24-certificates/basics.md)**

    ---

    Zertifikate und Verschlüsselung: Wie TLS funktioniert, Zertifikatsketten, Dateiformate, wo Zertifikate liegen und was du installieren musst

-   :material-shield-lock-outline:{ .lg .middle } **[SELinux und AppArmor verstehen](25-selinux-apparmor/basics.md)**

    ---

    SELinux und AppArmor: Wie SELinux und AppArmor arbeiten, welche Distribution was nutzt, und der Weg von der Ablehnung zur Lösung

-   :material-vpn:{ .lg .middle } **[WireGuard verstehen](26-wireguard/basics.md)**

    ---

    VPN mit WireGuard: Wie WireGuard funktioniert, was du installieren musst, eine vollständige Einrichtung von Server und Client und die Firewall

</div>
