# borg

> BorgBackup: deduplizierte, komprimierte und verschlüsselte Backups in Archive, lokal oder per SSH auf einen anderen Server.

![borg output](../assets/screenshots/28-backup/borg.png)

## Syntax

```bash
borg BEFEHL [OPTIONEN] REPOSITORY[::ARCHIV] [PFAD...]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `init --encryption=repokey REPO` | Ein Repository anlegen; der Schlüssel liegt darin, geschützt durch die Passphrase |
| `create REPO::NAME PFAD...` | Ein Archiv erstellen, etwa `::www-{now:%Y-%m-%d}` |
| `--stats`, `--compression zstd` | Mit `create`: Statistik zeigen, mit zstd komprimieren |
| `list REPO[::ARCHIV]` | Die Archive auflisten oder die Dateien in einem Archiv |
| `extract REPO::ARCHIV [PFAD]` | Ins aktuelle Verzeichnis zurückspielen |
| `prune --keep-daily 7 ...` | Alte Archive nach einer Aufbewahrungsregel löschen; `compact` gibt den Platz frei |
| `check REPO` | Das Repository prüfen |
| `key export REPO DATEI` | Den Schlüssel exportieren, zur Aufbewahrung außerhalb des Servers |
| `mount REPO VERZ` | Archive als Dateisystem einhängen |

Entfernte Repositorys sehen so aus: `ssh://backup@backup.example.com/./borg`; auf dem Ziel muss ebenfalls `borg` installiert sein. Die Passphrase kommt aus `BORG_PASSPHRASE` oder `BORG_PASSCOMMAND`.

## Beispiele

**Ein Archiv mit Statistik erstellen:**

```bash
sudo -E borg create --stats --compression zstd /mnt/backup/borg::www-{now:%Y-%m-%d} /srv/www
```

```text
------------------------------------------------------------------------------
Repository: /mnt/backup/borg
Archive name: www-2026-10-26
Archive fingerprint: 17fd9523e77efecdf984ba545d72182d49ad4fcc81ab44e235f37060754ebcc3
Time (start): Mon, 2026-10-26 02:45:01
Time (end):   Mon, 2026-10-26 02:45:09
Duration: 8.12 seconds
Number of files: 3842
Utilization of max. archive size: 0%
------------------------------------------------------------------------------
                       Original size      Compressed size    Deduplicated size
This archive:              924.18 MB            612.40 MB              3.21 MB
All archives:               12.94 GB              8.57 GB            701.33 MB

                       Unique chunks         Total chunks
Chunk index:                    4185                58611
------------------------------------------------------------------------------
```

`Deduplicated size` ist, was dieses Archiv wirklich hinzufügt: 3,21 MB von 924 MB. Alle 14 Archive zusammen belegen nur 701 MB.

**Ein Repository anlegen:**

```bash
export BORG_PASSCOMMAND='cat /root/.borg-pass'
sudo -E borg init --encryption=repokey /mnt/backup/borg
```

```text
IMPORTANT: you will need both KEY AND PASSPHRASE to access this repo!

Key storage location depends on the mode:
- repokey modes: key is stored in the repository directory.
- keyfile modes: key is stored in the home directory of this user.

For any mode, you should:
1. Export the borg key and store the result at a safe place:
   borg key export           REPOSITORY encrypted-key-backup
   borg key export --paper   REPOSITORY encrypted-key-backup.txt
   borg key export --qr-html REPOSITORY encrypted-key-backup.html
2. Write down the borg key passphrase and store it at safe place.
```

**Die Archive auflisten und eine Datei zurückholen:**

```bash
sudo -E borg list /mnt/backup/borg | tail -2
cd /tmp && sudo -E borg extract /mnt/backup/borg::www-2026-10-26 srv/www/index.html
cat /tmp/srv/www/index.html
```

```text
www-2026-10-25                       Sun, 2026-10-25 02:45:02 [b4e1c09d7a35f2e8c6d0a9b1f3e5c7a2d4b6e8f0a1c3e5d7b9f1a3c5e7d9b1f3]
www-2026-10-26                       Mon, 2026-10-26 02:45:01 [17fd9523e77efecdf984ba545d72182d49ad4fcc81ab44e235f37060754ebcc3]
<h1>tuxdex-srv: all systems operational</h1>
```

**Alte Archive löschen:**

```bash
sudo -E borg prune --list --keep-daily 7 --keep-weekly 4 /mnt/backup/borg | tail -3
sudo -E borg compact /mnt/backup/borg
```

```text
Keeping archive (rule: daily #1):            www-2026-10-26                       Mon, 2026-10-26 02:45:01 [17fd9523e77efecdf984ba545d72182d49ad4fcc81ab44e235f37060754ebcc3]
Keeping archive (rule: daily #2):            www-2026-10-25                       Sun, 2026-10-25 02:45:02 [b4e1c09d7a35f2e8c6d0a9b1f3e5c7a2d4b6e8f0a1c3e5d7b9f1a3c5e7d9b1f3]
Pruning archive (1/1):                       www-2026-10-12                       Mon, 2026-10-12 02:45:01 [6a2c8e0f4b1d3e5a7c9e1f3a5b7d9e1c3a5f7b9d1e3c5a7f9b1d3e5c7a9b1d3e]
```

## Wann brauche ich das?

- Für Backups auf einen eigenen Backup-Server oder eine Storage Box per SSH
- Wenn Kompression wichtig ist, etwa bei vielen Textdateien und Logs
- Um ein altes Archiv einzuhängen und wie ein Verzeichnis zu durchsuchen

!!! tip "Den SSH-Schlüssel einschränken"
    Auf dem Backup-Server erlaubt `command="borg serve --restrict-to-path /srv/borg --append-only"`
    vor dem Schlüssel in `authorized_keys` nur borg und nur das Hinzufügen von Daten. Ein
    gehackter Server kann seine Backups dann nicht löschen.

!!! danger "Den Schlüssel exportieren"
    Mit `repokey` liegt der Schlüssel im Repository. Ist das Repository beschädigt oder die
    Passphrase vergessen, ist alles verloren. Führe `borg key export` aus und bewahre Datei
    und Passphrase sicher auf.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install borgbackup` | `sudo apt install borgbackup` | `sudo dnf install borgbackup` (EPEL) | `sudo pacman -S borg` |

## Verwandte Befehle

[restic](restic.md) · [mysqldump](mysqldump.md) · [ssh-keygen](../12-ssh/ssh-keygen.md) · [tar](../14-archives/tar.md)
