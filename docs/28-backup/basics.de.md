# Backups verstehen

Ein Backup ist nur etwas wert, wenn du daraus wiederherstellen kannst. Alles in diesem
Kapitel dient diesem einen Ziel: Nach einer gelöschten Datei, einer kaputten Platte,
Ransomware oder einem Brand im Rechenzentrum bekommst du deine Daten zurück, und du weißt,
wie lange das dauert.

## Die 3-2-1-Regel

| | Bedeutung | Auf tuxdex-srv |
|---|-----------|----------------|
| **3** Kopien | Das Original plus zwei Backups | Daten auf `sda`, Backup unter `/mnt/backup`, ein zweites Backup außer Haus |
| **2** verschiedene Medien | Nicht alles auf derselben Platte oder demselben System | Lokale Backup-Platte plus Speicher bei einem anderen Anbieter |
| **1** Kopie außer Haus | Mindestens eine Kopie an einem anderen Ort | restic- oder borg-Repository auf einem externen Server oder in S3 |

Dazu kommt eine weitere Regel: Mindestens eine Kopie muss **außer Reichweite** des Servers
sein, damit ein Angreifer oder Ransomware mit Root-Zugriff sie nicht löschen kann
(Append-only-Repository, Object Lock oder ein Backup-Server, der sich die Daten holt).

## Was gesichert wird

| Was | Wie | Warum nicht einfach die Dateien kopieren |
|-----|-----|------------------------------------------|
| Konfiguration (`/etc`) | restic oder borg | Klein, aber aufwendig neu aufzubauen |
| Webinhalte, Uploads (`/srv`) | restic oder borg | |
| Datenbanken | Erst [`pg_dump`](pg_dump.md), [`mysqldump`](mysqldump.md), dann den Dump sichern | Die Datendateien einer laufenden Datenbank zu kopieren, ergibt ein kaputtes Backup |
| Docker-Volumes | Dump der Datenbank darin, plus die Volume-Verzeichnisse | Derselbe Grund |
| Paketliste | `dpkg --get-selections`, `dnf history` | Um dieselbe Software wieder einzurichten |

Nicht nötig: `/proc`, `/sys`, `/dev`, `/run`, `/tmp`, Caches und alles, was aus Paketen oder
Git kommt.

## restic oder borg?

Beide deduplizieren (jeder Block wird nur einmal gespeichert), komprimieren, verschlüsseln
und halten viele Versionen mit wenig Platz vor.

| | [`restic`](restic.md) | [`borg`](borg.md) |
|---|-----------------------|-------------------|
| Ziele | Lokal, SFTP, S3, Azure, Google Cloud, REST-Server, rclone | Lokal oder SSH mit `borg` auf der Gegenseite |
| Verschlüsselung | Immer | Wählbar, meist `repokey` |
| Tempo | Schnell | Sehr schnell, sehr gute Kompression |
| Typischer Einsatz | Backups in Cloud-Speicher | Backups auf eigene Server oder Hetzner Storage Box, BorgBase |

## Ein Backup-Ablauf

```text
02:30  database dumps     pg_dump / mysqldump → /var/backups/db/
02:40  restic backup      /etc /srv /var/backups/db  → repository
03:30  restic forget      keep 7 daily, 4 weekly, 6 monthly, then prune
Sunday restic check       read part of the data and verify it
Monthly restore test      restore one file and one database into a test system
```

Lass das als systemd-Timer oder Cronjob laufen, siehe [`crontab`](../16-scheduling/crontab.md),
und Fehler melden, etwa mit `logger` ins Journal und an dein Monitoring.

## Was du installieren musst

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| restic | `sudo apt install restic` | `sudo apt install restic` | `sudo dnf install restic` (EPEL) | `sudo pacman -S restic` |
| borg | `sudo apt install borgbackup` | `sudo apt install borgbackup` | `sudo dnf install borgbackup` (EPEL) | `sudo pacman -S borg` |
| pg_dump | mit `postgresql-client` | mit `postgresql-client` | mit `postgresql` | mit `postgresql` |
| mysqldump | mit `mariadb-client` | mit `mysql-client` oder `mariadb-client` | mit `mysql` oder `mariadb` | mit `mariadb-clients` |

!!! tip "Die Wiederherstellung testen"
    Plane einen Wiederherstellungstest ein, etwa einmal im Monat: Stell eine zufällige Datei
    und einen Datenbank-Dump in einem Testsystem wieder her und prüf sie. Erst dann weißt du,
    dass das Backup funktioniert und wie lange eine Wiederherstellung dauert.

!!! danger "Ohne Passwort ist das Backup weg"
    restic und borg verschlüsseln alles. Bewahre das Repository-Passwort (bei borg auch den
    exportierten Schlüssel) außerhalb des Servers auf, etwa in deinem Passwortmanager.
    Brennt der Server ab, darf das Passwort nicht mit abbrennen.
