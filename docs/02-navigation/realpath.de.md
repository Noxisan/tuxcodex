# realpath

> Zeigt den vollständigen, absoluten Pfad einer Datei oder eines Verzeichnisses, mit aufgelösten symbolischen Links und `..`.

## Syntax

```bash
realpath [OPTION]... DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-e`, `--canonicalize-existing` | Alle Teile des Pfads müssen existieren, sonst Fehlermeldung |
| `-m`, `--canonicalize-missing` | Kein Teil des Pfads muss existieren |
| `-s`, `--no-symlinks` | Symbolische Links nicht auflösen, nur `.` und `..` bereinigen |
| `--relative-to=VERZ` | Pfad relativ zu `VERZ` ausgeben |
| `-q`, `--quiet` | Keine Fehlermeldungen ausgeben |

## Beispiele

**Den absoluten Pfad einer Datei anzeigen:**

```bash
realpath notes.txt
```

```text
/home/nox/notes.txt
```

**Herausfinden, wohin ein symbolischer Link wirklich zeigt:**

```bash
realpath /bin/sh
```

```text
/usr/bin/dash
```

Unter Debian ist `/bin` ein Link auf `/usr/bin`, und `sh` ist ein Link auf `dash`.
`realpath` folgt der ganzen Kette.

**Einen Pfad mit `..` bereinigen:**

```bash
realpath ../../etc/ssh
```

```text
/etc/ssh
```

**Sicherstellen, dass ein Pfad existiert:**

```bash
realpath -e missing.txt
```

```text
realpath: missing.txt: No such file or directory
```

Ohne `-e` würde `realpath` `/home/nox/missing.txt` ausgeben, denn standardmäßig muss nur
das Verzeichnis existieren.

**Einen Pfad relativ zu einem anderen Verzeichnis anzeigen:**

```bash
realpath --relative-to=/etc /etc/ssh/sshd_config
```

```text
ssh/sshd_config
```

![realpath output](../assets/screenshots/02-navigation/realpath.png)

## Wann brauche ich das?

- Um herauszufinden, auf welche Datei ein symbolischer Link wirklich zeigt, etwa in
  `/etc/nginx/sites-enabled` oder `/etc/alternatives`
- Um absolute Pfade für Konfigurationsdateien, Cronjobs oder systemd-Units zu bekommen
- In Skripten, um das Verzeichnis zu finden, in dem das Skript selbst liegt

!!! tip "Das eigene Verzeichnis des Skripts"
    Diese Zeile liefert einem Skript das Verzeichnis, in dem es gespeichert ist, egal
    von wo aus es gestartet wurde:

    ```bash
    SCRIPT_DIR="$(dirname "$(realpath "$0")")"
    ```

!!! tip "`readlink -f`"
    In älteren Skripten findest du oft `readlink -f` statt `realpath`. Unter Linux
    liefern beide dasselbe Ergebnis.

## Verwandte Befehle

[pwd](pwd.md) · [cd](cd.md)
