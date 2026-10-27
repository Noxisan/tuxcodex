---
icon: material/home
hide:
  - toc
---

<div class="tc-hero" markdown>

# TuxCodex { .tc-sr-only }

![TuxCodex Logo](assets/logo-hero.png){ width="350" }

<div class="tc-distros" markdown>
<span class="tc-badge tc-badge--debian" markdown="span">:simple-debian: Debian</span>
<span class="tc-badge tc-badge--ubuntu" markdown="span">:simple-ubuntu: Ubuntu</span>
<span class="tc-badge tc-badge--redhat" markdown="span">:simple-redhat: RHEL</span>
<span class="tc-badge tc-badge--arch" markdown="span">:simple-archlinux: Arch</span>
</div>

Das praxisnahe Nachschlagewerk für **Linux-Administration und DevOps**: jeder Befehl mit
Syntax, echten Beispielen und Tipps aus dem Server-Alltag. Für Debian, Ubuntu, RHEL und
Arch, auf Deutsch und Englisch.

Zusammengestellt von [:simple-github: Nox](https://github.com/Noxisan){ .tc-author }

</div>

## Linux-Grundlagen

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

</div>

## Automatisierung & DevOps

<div class="grid cards" markdown>

-   :material-script-text-outline:{ .lg .middle } **[Bash-Skripte](17-bash-scripting/index.md)**

    ---

    Variablen, Bedingungen, Schleifen und Funktionen für eigene Admin-Skripte.

-   :material-git:{ .lg .middle } **[Git](18-git/index.md)**

    ---

    Konfigurationen und Skripte versionieren, Branches und Remotes.

-   :material-docker:{ .lg .middle } **[Docker](19-docker/index.md)**

    ---

    Dienste in Containern betreiben, Images, Volumes und Compose.

-   :material-kubernetes:{ .lg .middle } **[Kubernetes](20-kubernetes/index.md)**

    ---

    Container über viele Server verteilen mit `kubectl` und Helm.

-   :material-ansible:{ .lg .middle } **Ansible** · *in Arbeit*

    ---

    Viele Server auf einmal mit Playbooks konfigurieren.

-   :material-infinity:{ .lg .middle } **CI/CD** · *in Arbeit*

    ---

    Automatisch testen und ausliefern mit Pipelines.

</div>

## Sicherheit

<div class="grid cards" markdown>

-   :material-radar:{ .lg .middle } **Netzwerk-Scans** · *in Arbeit*

    ---

    Offene Ports und Dienste finden mit `nmap` und Co.

-   :material-certificate-outline:{ .lg .middle } **Zertifikate und Verschlüsselung** · *in Arbeit*

    ---

    TLS-Zertifikate, `openssl`, `gpg` und Let's Encrypt.

</div>

## Alle Befehle

<!-- COMMAND_INDEX -->

## Was jede Befehlsseite enthält

<div class="grid cards" markdown>

-   :material-console:{ .lg .middle } **Syntax & Optionen**

    ---

    Der Befehl auf einen Blick, mit den Optionen, die du wirklich brauchst.

-   :material-play-box-outline:{ .lg .middle } **Echte Beispiele**

    ---

    Praxisnahe Beispiele mit Ausgabe und Screenshot.

-   :material-server:{ .lg .middle } **Admin-Praxis**

    ---

    Wann du den Befehl auf einem Server brauchst, mit Tipps und Stolperfallen.

-   :material-swap-horizontal:{ .lg .middle } **Unterschiede zwischen Distributionen**

    ---

    Wo sich Debian, Ubuntu, RHEL und Arch unterscheiden: Pakete, Standardwerte und Werkzeuge.

</div>

!!! tip "So nutzt du dieses Handbuch"
    Nutze die Suche oben oder arbeite die Kapitel der Reihe nach durch.
    Jedes Kapitel baut auf dem vorherigen auf.
