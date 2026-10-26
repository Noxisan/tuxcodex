# find

> Durchsucht einen Verzeichnisbaum nach Dateien anhand von Name, Typ, Größe, Alter, Besitzer oder Rechten und kann Befehle auf die Treffer anwenden.

## Syntax

```bash
find [VERZEICHNIS]... [TEST]... [AKTION]
```

## Optionen

| Test / Aktion | Beschreibung |
|---------------|--------------|
| `-name MUSTER` | Name passt auf `MUSTER` (z. B. `"*.log"`), Groß- und Kleinschreibung zählt |
| `-iname MUSTER` | Wie `-name`, aber ohne Unterscheidung von Groß- und Kleinschreibung |
| `-type TYP` | `f` Datei, `d` Verzeichnis, `l` symbolischer Link |
| `-size N` | Größe: `+500M` größer als 500 MB, `-10k` kleiner als 10 KB |
| `-mtime N` | Vor `N` Tagen zuletzt geändert: `+14` älter als 14 Tage, `-1` innerhalb des letzten Tages |
| `-mmin N` | Wie `-mtime`, aber in Minuten |
| `-user NAME` | Gehört dem Benutzer `NAME` |
| `-perm MODUS` | Hat die Rechte `MODUS` (z. B. `-perm 777`) |
| `-empty` | Leere Datei oder leeres Verzeichnis |
| `-maxdepth N` | Höchstens `N` Ebenen tief suchen |
| `-xdev` | Im aktuellen Dateisystem bleiben (nicht in `/proc`, Mounts usw. absteigen) |
| `-exec BEFEHL {} +` | `BEFEHL` mit den gefundenen Dateien als Argumente ausführen |
| `-delete` | Gefundene Dateien löschen |

## Beispiele

**Dateien nach Namen suchen:**

```bash
find /etc/ssh -name "*.pub"
```

```text
/etc/ssh/ssh_host_ecdsa_key.pub
/etc/ssh/ssh_host_ed25519_key.pub
/etc/ssh/ssh_host_rsa_key.pub
```

**Nur Verzeichnisse suchen:**

```bash
find ~ -type d
```

```text
/home/nox
/home/nox/backup
/home/nox/scripts
```

**Große Dateien finden, wenn die Platte voll ist:**

```bash
find / -xdev -type f -size +500M 2>/dev/null
```

```text
/home/nox/backup/db-2026-10-20.sql.gz
```

**Alte Dateien finden:**

```bash
find /var/log/apt -name "*.gz" -mtime +14
```

```text
/var/log/apt/history.log.1.gz
/var/log/apt/term.log.1.gz
```

**Konfigurationsdateien finden, die in der letzten Stunde geändert wurden:**

```bash
sudo find /etc -type f -mmin -60
```

```text
/etc/nginx/sites-available/example.com
```

**Einen Befehl auf alle Treffer anwenden:**

```bash
find ~/scripts -name "*.sh" -exec chmod 750 {} +
ls -l ~/scripts
```

```text
total 8
-rwxr-x--- 1 nox nox 1200 Oct 22 18:40 backup.sh
-rwxr-x--- 1 nox nox  640 Oct 22 18:35 cleanup.sh
```

![find output](../assets/screenshots/02-navigation/find.png)

## Wann brauche ich das?

- Wenn die Platte voll ist: große Dateien mit `-size` finden
- Um alte Logs, Backups oder temporäre Dateien aufzuräumen (`-mtime` zusammen mit `-delete`)
- Um herauszufinden, welche Konfigurationsdateien zuletzt geändert wurden (`-mmin`, `-newer`)
- Um Besitzer oder Rechte vieler Dateien auf einmal zu korrigieren (`-exec chown` / `-exec chmod`)
- Wenn du einen Dateinamen kennst, aber nicht weißt, wo die Datei liegt

!!! tip "\"Permission denied\" ausblenden"
    Als normaler Benutzer meldet `find /` für jedes Verzeichnis, das du nicht lesen
    darfst, einen Fehler. Mit `2>/dev/null` blendest du diese Meldungen aus, oder du
    suchst mit `sudo`.

!!! warning "Muster immer in Anführungszeichen"
    Schreib `-name "*.log"`, nicht `-name *.log`. Ohne Anführungszeichen ersetzt die Shell
    `*.log` schon im aktuellen Verzeichnis, bevor `find` überhaupt startet, und die Suche
    liefert falsche Ergebnisse.

!!! danger "Erst testen, dann löschen"
    Führe die Suche zuerst ohne `-delete` aus und prüfe die Liste. Setz `-delete` immer
    ans **Ende**: `find . -delete -name "*.tmp"` löscht **alles** im aktuellen
    Verzeichnis, weil `-delete` vor dem Namenstest ausgeführt wird.

    ```bash
    find /tmp -type f -name "*.tmp" -mtime +7          # erst die Liste prüfen
    find /tmp -type f -name "*.tmp" -mtime +7 -delete  # dann löschen
    ```

## Verwandte Befehle

[ls](ls.md) · [tree](tree.md)
