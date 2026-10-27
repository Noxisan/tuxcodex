# flock

> Führt einen Befehl nur aus, während er eine Sperrdatei hält. Verhindert, dass ein Cronjob ein zweites Mal startet, während der erste Lauf noch läuft.

![flock output](../assets/screenshots/16-scheduling/flock.png)

## Syntax

```bash
flock [OPTION]... SPERRDATEI BEFEHL [ARGUMENT]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n` | Nicht warten: sofort aufgeben, wenn die Sperre vergeben ist |
| `-w SEKUNDEN` | Höchstens so lange auf die Sperre warten |
| `-E CODE` | Exit-Code, wenn die Sperre vergeben ist, Standard `1` |
| `--verbose` | Melden, wie lange es gedauert hat, die Sperre zu bekommen |

## Beispiele

**Ein Backup mit Sperre ausführen:**

```bash
flock --verbose -n /run/lock/backup.lock /usr/local/bin/backup.sh
```

```text
flock: getting lock took 0.000003 seconds
flock: executing /usr/local/bin/backup.sh
```

**Ein zweiter Start, während der erste läuft:**

```bash
flock -n /run/lock/backup.lock /usr/local/bin/backup.sh; echo "exit $?"
```

```text
exit 1
```

Das zweite Backup startet gar nicht.

**Bis zu 30 Sekunden auf die Sperre warten:**

```bash
flock -w 30 /run/lock/backup.lock echo "got the lock"
```

```text
got the lock
```

**Die Sperre in einem Skript nutzen:**

```bash
exec 9>/run/lock/backup.lock
flock -n 9 || { echo "backup already running"; exit 1; }
```

```text
backup already running
```

Die Sperre gilt, solange das Skript läuft, und wird am Ende automatisch freigegeben.

## Wann brauche ich das?

- Für Cronjobs, die länger dauern können als ihr Intervall, etwa ein stündliches Backup
- Für Skripte, die nie zweimal gleichzeitig laufen dürfen
- Um Jobs nacheinander auszuführen, die dieselbe Ressource nutzen

!!! tip "In einer Crontab"
    `*/10 * * * * flock -n /run/lock/sync.lock /usr/local/bin/sync.sh` startet den Abgleich alle
    10 Minuten, aber nie einen zweiten, während der erste noch läuft.

!!! tip "Still in cron"
    Mit `-n -E 0` endet ein übersprungener Lauf mit `0`, damit cron und Monitoring ihn nicht
    als Fehler werten.

## Verwandte Befehle

[crontab](crontab.md) · [timeout](../08-processes/timeout.md) · [systemd-run](../09-systemd/systemd-run.md)
