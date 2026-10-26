# sftp

> Eine interaktive Dateiübertragung über SSH, ähnlich wie FTP: Verzeichnisse auf dem Server durchsuchen, Dateien holen und hochladen.

![sftp output](../assets/screenshots/12-ssh/sftp.png)

## Syntax

```bash
sftp [OPTION]... [BENUTZER@]HOST[:PFAD]
```

Optionen beim Start: `-P PORT` für einen anderen Port, `-b DATEI` für eine Batch-Datei mit Befehlen.

## Optionen

| Befehl in `sftp` | Beschreibung |
|------------------|--------------|
| `ls`, `cd`, `pwd` | Verzeichnis auf dem Server auflisten, wechseln und anzeigen |
| `lls`, `lcd`, `lpwd` | Dasselbe auf deinem eigenen Rechner |
| `get DATEI` | Eine Datei herunterladen (`get -r` für Verzeichnisse) |
| `put DATEI` | Eine Datei hochladen (`put -r` für Verzeichnisse) |
| `mkdir`, `rm`, `rename` | Auf dem Server anlegen, löschen und umbenennen |
| `bye` | Die Sitzung beenden |

## Beispiele

**Eine Sitzung öffnen und Dateien übertragen:**

```bash
sftp nox@192.0.2.10
```

```text
Connected to 192.0.2.10.
sftp> pwd
Remote working directory: /home/nox
sftp> cd /srv/backup
sftp> ls -l
-rw-r--r--    1 nox      nox      30000000 Oct 26 03:00 db.sql.gz
-rw-r--r--    1 nox      nox      1481408512 Oct 26 03:00 www.tar.gz
sftp> get db.sql.gz
Fetching /srv/backup/db.sql.gz to db.sql.gz
db.sql.gz                                     100%   29MB  11.2MB/s   00:02
sftp> put notes.txt
Uploading notes.txt to /srv/backup/notes.txt
notes.txt                                     100%  412   102.1KB/s   00:00
sftp> bye
```

Befehle mit einem `l` davor wirken auf deinem eigenen Rechner: `lls` listet das lokale
Verzeichnis.

**Eine einzelne Datei direkt holen:**

```bash
sftp nox@192.0.2.10:/srv/backup/db.sql.gz
```

```text
Connected to 192.0.2.10.
Fetching /srv/backup/db.sql.gz to db.sql.gz
db.sql.gz                                     100%   29MB  11.2MB/s   00:02
```

**Die Batch-Datei:**

```bash
cat transfer.txt
```

```text
cd /srv/backup
get db.sql.gz
put notes.txt
```

**Vorbereitete Befehle aus einer Datei ausführen:**

```bash
sftp -b transfer.txt nox@192.0.2.10
```

```text
sftp> cd /srv/backup
sftp> get db.sql.gz
Fetching /srv/backup/db.sql.gz to db.sql.gz
sftp> put notes.txt
Uploading notes.txt to /srv/backup/notes.txt
```

## Wann brauche ich das?

- Wenn du dich auf dem Server umsehen willst, bevor du Dateien kopierst
- Für Benutzer, die nur Dateien übertragen, sich aber nicht anmelden dürfen (reine
  SFTP-Konten)
- Mit grafischen Programmen wie FileZilla oder WinSCP, die dasselbe Protokoll nutzen

!!! tip "Reine SFTP-Benutzer"
    Mit `ForceCommand internal-sftp` und `ChrootDirectory` in `sshd_config` gibst du
    Benutzern Zugriff auf nur ein Verzeichnis, ohne Shell. Ideal für Kunden, die Dateien
    hochladen.

!!! warning "Nicht FTP"
    Trotz des Namens hat SFTP nichts mit FTP oder FTPS zu tun. Es läuft über SSH auf
    Port 22 und nutzt dieselben Benutzer und Schlüssel.

## Verwandte Befehle

[scp](scp.md) · [rsync](rsync.md) · [sshd](sshd.md) · [rsync](rsync.md)
