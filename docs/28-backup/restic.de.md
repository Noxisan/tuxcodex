# restic

> Schnelle, verschlüsselte und deduplizierte Backups auf eine lokale Platte, einen anderen Server oder Cloud-Speicher.

![restic output](../assets/screenshots/28-backup/restic.png)

## Syntax

```bash
restic -r REPOSITORY BEFEHL [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `init` | Ein neues Repository anlegen |
| `backup PFAD...` | Sichern; nur geänderte Daten werden neu gespeichert |
| `--exclude MUSTER`, `--exclude-file DATEI` | Mit `backup`: Dateien auslassen |
| `snapshots` | Die Sicherungen auflisten |
| `restore ID --target VERZ` | Einen Snapshot zurückspielen; `latest` für den neuesten, `--include` für einzelne Dateien |
| `ls`, `diff`, `find` | In Snapshots schauen, sie vergleichen, Dateien suchen |
| `forget --keep-daily 7 ... --prune` | Alte Snapshots nach einer Aufbewahrungsregel löschen und den Platz freigeben |
| `check` | Das Repository prüfen; `--read-data-subset 10%` liest auch Daten |
| `mount VERZ` | Alle Snapshots als Dateisystem einhängen, zum Durchsuchen |

Repository und Passwort kommen meist aus Umgebungsvariablen: `RESTIC_REPOSITORY` und `RESTIC_PASSWORD_FILE`. Repository-Adressen sehen etwa so aus: `/mnt/backup/restic`, `sftp:backup@backup.example.com:/srv/restic` oder `s3:https://s3.example.com/bucket`.

## Beispiele

**Zum zweiten Mal sichern, nur Änderungen werden gespeichert:**

```bash
sudo -E restic backup /etc /srv /var/backups/db
```

```text
using parent snapshot 2a15a3ca

Files:           3 new,    12 changed,  4211 unmodified
Dirs:            0 new,     9 changed,   612 unmodified
Added to the repository: 18.412 MiB (6.207 MiB stored)

processed 4226 files, 1.284 GiB in 0:04
snapshot c391be73 saved
```

Von 1,28 GiB mussten nur 6 MiB gespeichert werden: Der Rest war schon im Repository.

**Ein Repository anlegen:**

```bash
export RESTIC_REPOSITORY=/mnt/backup/restic RESTIC_PASSWORD_FILE=/root/.restic-pass
sudo -E restic init
```

```text
created restic repository d97428fbea at /mnt/backup/restic

Please note that knowledge of your password is required to access
the repository. Losing your password means that your data is
irrecoverably lost.
```

**Die Snapshots auflisten:**

```bash
sudo -E restic snapshots
```

```text
ID        Time                 Host        Tags        Paths               Size
------------------------------------------------------------------------------------
2a15a3ca  2026-10-25 02:40:01  tuxdex-srv              /etc                1.281 GiB
                                                       /srv
                                                       /var/backups/db

c391be73  2026-10-26 02:40:02  tuxdex-srv              /etc                1.284 GiB
                                                       /srv
                                                       /var/backups/db
------------------------------------------------------------------------------------
2 snapshots
```

**Was sich zwischen zwei Snapshots geändert hat:**

```bash
sudo -E restic diff 2a15a3ca c391be73 | head -6
```

```text
comparing snapshot 2a15a3ca to c391be73:

M    /etc/nginx/conf.d/status.conf
M    /srv/www/index.html
+    /srv/www/img/new.jpg
+    /var/backups/db/statusdb-2026-10-26.dump
```

**Eine einzelne Datei zurückholen:**

```bash
sudo -E restic restore latest --target /tmp/restore --include /etc/nginx/conf.d/status.conf
```

```text
restoring snapshot c391be73 of [/etc /srv /var/backups/db] at 2026-10-26 02:40:02.001926226 +0100 CET by root@tuxdex-srv to /tmp/restore
Summary: Restored 5 / 1 files/dirs (412 B / 412 B) in 0:00
```

Die Datei landet unter `/tmp/restore/etc/nginx/conf.d/status.conf`, das Original bleibt unberührt. Erst vergleichen, dann zurückkopieren.

**Alte Snapshots löschen und das Repository prüfen:**

```bash
sudo -E restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune | tail -3
sudo -E restic check | tail -2
```

```text
this removes 3 snapshots and 0 B of data
[0:00] 100.00%  3 / 3 files deleted
done
[0:00] 100.00%  9 / 9 snapshots
no errors were found
```

## Wann brauche ich das?

- Für das tägliche Backup von `/etc`, `/srv` und den Datenbank-Dumps
- Um eine Kopie außer Haus zu halten, etwa in S3-kompatiblem Speicher
- Um eine einzelne Datei vom letzten Dienstag in Sekunden zurückzuholen

!!! tip "Passwort aus einer Datei"
    Leg das Passwort in `/root/.restic-pass` mit den Rechten `600` ab und setze
    `RESTIC_PASSWORD_FILE=/root/.restic-pass`. Dann brauchen Cronjobs und Timer das Passwort
    nicht auf der Kommandozeile.

!!! warning "forget ohne --prune gibt nichts frei"
    `restic forget` entfernt nur die Snapshot-Einträge. Die Daten werden erst mit `--prune`
    oder einem späteren `restic prune` gelöscht.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install restic` | `sudo apt install restic` | `sudo dnf install restic` (EPEL) | `sudo pacman -S restic` |

## Verwandte Befehle

[borg](borg.md) · [pg_dump](pg_dump.md) · [rsync](../12-ssh/rsync.md) · [crontab](../16-scheduling/crontab.md)
