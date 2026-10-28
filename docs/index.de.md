---
icon: material/home
hide:
  - toc
---

<div class="tc-hero" markdown>

# TuxDex { .tc-sr-only }

![TuxDex Logo](assets/logo-hero.png){ width="350" }

Linux-Befehle. Echte Beispiele. Kein Rätselraten.
{ .tc-tagline }

Ein praxisnahes Nachschlagewerk für **Linux-Administration, Serverbetrieb und DevOps** mit
Befehlssyntax, funktionierenden Beispielen und Tipps für reale Einsatzszenarien.

<div class="tc-distros" markdown>
<span class="tc-badge tc-badge--debian" markdown="span">:simple-debian: Debian</span>
<span class="tc-badge tc-badge--ubuntu" markdown="span">:simple-ubuntu: Ubuntu</span>
<span class="tc-badge tc-badge--redhat" markdown="span">:simple-redhat: RHEL</span>
<span class="tc-badge tc-badge--arch" markdown="span">:simple-archlinux: Arch</span>
</div>

Englisch · Deutsch
{ .tc-languages }

Erstellt von [:simple-github: Nox](https://github.com/Noxisan){ .tc-author }

</div>

## Linux-Administration

<div class="grid cards" markdown>

-   :material-compass-outline:{ .lg .middle } **[Orientierung](01-orientation/index.md)**

    ---

    Wer bin ich, wo bin ich und was ist auf dieser Maschine gerade los?

-   :material-folder-outline:{ .lg .middle } **[Navigation](02-navigation/index.md)**

    ---

    Im Dateisystem bewegen und Dateien finden.

-   :material-file-document-outline:{ .lg .middle } **[Dateien](03-files/index.md)**

    ---

    Dateien und Verzeichnisse anlegen, kopieren, verschieben und löschen.

-   :material-text-box-search-outline:{ .lg .middle } **[Dateien anzeigen](04-viewing-files/index.md)**

    ---

    Dateien und Logs lesen, auch komprimierte und binäre Dateien.

-   :material-text-search:{ .lg .middle } **[Textverarbeitung](05-text-processing/index.md)**

    ---

    Text in Logs und Konfigurationsdateien suchen, filtern, sortieren und ändern.

-   :material-shield-lock-outline:{ .lg .middle } **[Rechte](06-permissions/index.md)**

    ---

    Besitzer, Gruppen und Zugriffsrechte, und wie man sie korrigiert.

-   :material-account-multiple-outline:{ .lg .middle } **[Benutzer und Gruppen](07-users-groups/index.md)**

    ---

    Benutzer und Gruppen anlegen und verwalten, `sudo` und `su`.

-   :material-cog-transfer-outline:{ .lg .middle } **[Prozesse](08-processes/index.md)**

    ---

    Laufende Programme finden, beobachten und beenden.

-   :material-cog-sync-outline:{ .lg .middle } **[systemd und Dienste](09-systemd/index.md)**

    ---

    Dienste verwalten, ihre Logs lesen und den Server sauber neu starten.

-   :material-package-variant-closed:{ .lg .middle } **[Pakete](10-packages/index.md)**

    ---

    Software mit `apt`, `dnf` und `pacman` installieren, aktualisieren und entfernen.

-   :material-lan:{ .lg .middle } **[Netzwerk](11-network/index.md)**

    ---

    Adressen, Verbindungen, DNS, Downloads, Netzwerkkonfiguration und Firewall.

-   :material-console-network-outline:{ .lg .middle } **[SSH](12-ssh/index.md)**

    ---

    Sicher anmelden, Schlüssel, Tunnel und Dateien zwischen Servern kopieren.

-   :material-harddisk:{ .lg .middle } **[Festplatten und Speicher](13-disks-storage/index.md)**

    ---

    Partitionen, Dateisysteme, Einhängen, Speicherplatz und LVM.

-   :material-archive-arrow-down-outline:{ .lg .middle } **[Archive](14-archives/index.md)**

    ---

    Packen und komprimieren mit `tar`, `gzip`, `zstd` und `zip`.

-   :material-text-box-multiple-outline:{ .lg .middle } **[Logs](15-logs/index.md)**

    ---

    Kernelmeldungen, Logrotation, fehlgeschlagene Anmeldungen, Audit und Log-Auswertung.

-   :material-calendar-clock:{ .lg .middle } **[Zeitgesteuerte Aufgaben](16-scheduling/index.md)**

    ---

    Jobs regelmäßig ausführen mit cron, `at` und systemd-Timern.

-   :material-speedometer:{ .lg .middle } **[Leistung und Kernel](27-performance/index.md)**

    ---

    Herausfinden, warum ein Server langsam ist, und Kernel-Parameter und Limits einstellen.

-   :material-backup-restore:{ .lg .middle } **[Backup](28-backup/index.md)**

    ---

    Datenbank-Dumps, verschlüsselte Backups mit restic und borg und die Wiederherstellung testen.

</div>

## Serverdienste

<div class="grid cards" markdown>

-   :material-web:{ .lg .middle } **[Webserver](29-webserver/index.md)**

    ---

    nginx und Apache: Konfiguration, Seiten, Reverse Proxy und Lasttests.

-   :material-folder-network-outline:{ .lg .middle } **[Dateifreigaben](30-file-shares/index.md)**

    ---

    Verzeichnisse mit NFS und Samba freigeben.

-   :material-database-outline:{ .lg .middle } **[Datenbanken](33-databases/index.md)**

    ---

    PostgreSQL und MariaDB: Benutzer, Datenbanken, Rechte und Health Checks.

-   :material-lightning-bolt-outline:{ .lg .middle } **[Caches und Message Queues](34-caches-queues/index.md)**

    ---

    Redis, Valkey und RabbitMQ: Speicher, Schlüssel, Benutzer, Queues und Health Checks.

-   :material-text-search:{ .lg .middle } **[Suche mit Elasticsearch und OpenSearch](35-search/index.md)**

    ---

    Zustand des Clusters, Indizes und Shards, Passwörter, Keystore und Plugins.

</div>

## Automatisierung & DevOps

<div class="grid cards" markdown>

-   :material-script-text-outline:{ .lg .middle } **[Bash-Skripte](17-bash-scripting/index.md)**

    ---

    Variablen, Bedingungen, Schleifen und Funktionen für eigene Admin-Skripte.

-   :material-git:{ .lg .middle } **[Git](18-git/index.md)**

    ---

    Konfigurationen und Skripte versionieren, Branches und Remotes.

-   :material-monitor-multiple:{ .lg .middle } **[Virtualisierung](31-virtualization/index.md)**

    ---

    Virtuelle Maschinen mit KVM und libvirt: installieren, klonen, Snapshots und Plattenabbilder.

-   :material-docker:{ .lg .middle } **[Docker](19-docker/index.md)**

    ---

    Dienste in Containern betreiben, Images, Volumes und Compose.

-   :material-kubernetes:{ .lg .middle } **[Kubernetes](20-kubernetes/index.md)**

    ---

    Container über viele Server verteilen mit `kubectl` und Helm.

-   :material-ansible:{ .lg .middle } **[Ansible](21-ansible/index.md)**

    ---

    Viele Server auf einmal mit Playbooks konfigurieren.

-   :material-infinity:{ .lg .middle } **[CI/CD](22-ci-cd/index.md)**

    ---

    Automatisch testen und ausliefern mit Pipelines.

-   :material-monitor-dashboard:{ .lg .middle } **[Monitoring](32-monitoring/index.md)**

    ---

    Prometheus, Node Exporter und Alertmanager: Metriken, Abfragen und Alarme.

</div>

## Sicherheit

<div class="grid cards" markdown>

-   :material-radar:{ .lg .middle } **[Sicherheitsprüfung](23-security-scanning/index.md)**

    ---

    Offene Ports, Härtung, Rootkits, Dateiintegrität und verwundbare Images.

-   :material-certificate-outline:{ .lg .middle } **[Zertifikate und Verschlüsselung](24-certificates/index.md)**

    ---

    TLS-Zertifikate, `openssl`, `gpg` und Let's Encrypt.

-   :material-shield-lock-outline:{ .lg .middle } **[SELinux und AppArmor](25-selinux-apparmor/index.md)**

    ---

    „Permission denied“ richtig beheben, statt den Schutz abzuschalten.

-   :material-vpn:{ .lg .middle } **[VPN mit WireGuard](26-wireguard/index.md)**

    ---

    Verschlüsselte Tunnel zwischen Servern und Admin-Rechnern, SSH nur über das VPN.

</div>

## Alle Befehle

<!-- COMMAND_INDEX -->
