# systemd-cat

> Schickt die Ausgabe eines Befehls oder Skripts ins systemd-Journal, mit Tag und Priorität.

![systemd-cat output](../assets/screenshots/15-logs/systemd-cat.png)

## Syntax

```bash
systemd-cat [OPTION]... [BEFEHL [ARGUMENT]...]
```

Entweder führt `systemd-cat` den Befehl selbst aus, oder es liest aus einer Pipe.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-t TAG` | Name im Journal |
| `-p PRIORITÄT` | Priorität für die Standardausgabe, z. B. `info` |
| `--stderr-priority=PRIORITÄT` | Eigene Priorität für die Fehlerausgabe, z. B. `err` |

## Beispiele

**Ein Skript ausführen und seine Ausgabe protokollieren:**

```bash
systemd-cat -t backup --stderr-priority=err /usr/local/bin/backup.sh
journalctl -t backup --since "5 min ago"
```

```text
Oct 26 10:42:17 tuxdex-srv backup[4430]: dumping database shop
Oct 26 10:42:51 tuxdex-srv backup[4430]: compressing /srv/www
Oct 26 10:43:02 tuxdex-srv backup[4430]: tar: /mnt/backup/www.tar.gz: Cannot open: No space left on device
```

**Nur die Fehler des Laufs:**

```bash
journalctl -t backup -p err --since "5 min ago"
```

```text
Oct 26 10:43:02 tuxdex-srv backup[4430]: tar: /mnt/backup/www.tar.gz: Cannot open: No space left on device
```

**Die Ausgabe einer Pipe ins Journal schicken:**

```bash
df -h /mnt/backup | systemd-cat -t diskcheck
journalctl -t diskcheck -n 2
```

```text
Oct 26 10:43:10 tuxdex-srv diskcheck[4442]: Filesystem      Size  Used Avail Use% Mounted on
Oct 26 10:43:10 tuxdex-srv diskcheck[4442]: /dev/sdb1        98G   98G     0 100% /mnt/backup
```

## Wann brauche ich das?

- Um die komplette Ausgabe eines Skripts zu protokollieren, nicht nur einzelne Zeilen
- In Cronjobs, damit die Ausgabe nicht in Mails landet, sondern im Journal
- Um normale Ausgabe und Fehler nach Priorität zu trennen

!!! tip "Fehler mit eigener Priorität"
    Mit `--stderr-priority=err` erscheint alles, was ein Skript auf die Standardfehlerausgabe
    schreibt, im Journal als Fehler, und `journalctl -p err` findet es.

## Verwandte Befehle

[logger](logger.md) · [journalctl](../09-systemd/journalctl.md) · [systemd-run](../09-systemd/systemd-run.md)
