# pwd

> Zeigt den vollständigen Pfad des Verzeichnisses, in dem du dich gerade befindest.

![pwd output](../assets/screenshots/02-navigation/pwd.png)

## Syntax

```bash
pwd [OPTION]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-L` | Logischen Pfad anzeigen, mit symbolischen Links (Standard) |
| `-P` | Physischen Pfad anzeigen, alle symbolischen Links aufgelöst |

## Beispiele

**Das aktuelle Verzeichnis anzeigen:**

```bash
pwd
```

```text
/home/nox
```

**Nach einem Verzeichniswechsel prüfen, wo du bist:**

```bash
cd /etc/ssh
pwd
```

```text
/etc/ssh
```

**Den echten Pfad hinter einem symbolischen Link anzeigen:**

```bash
cd /var/run
pwd
pwd -P
```

```text
/var/run
/run
```

Unter Debian ist `/var/run` nur ein Link auf `/run`. `pwd` zeigt den Pfad, über den du
gekommen bist, `pwd -P` zeigt, wo du wirklich bist.

**Das aktuelle Verzeichnis in einem Befehl verwenden:**

```bash
echo "Backup of $(pwd)"
```

```text
Backup of /home/nox
```

## Wann brauche ich das?

- Wenn der Prompt nur einen verkürzten oder gar keinen Pfad zeigt
- Bevor du Befehle mit relativen Pfaden wie `rm *.log` ausführst, um sicher im richtigen
  Verzeichnis zu sein
- In Skripten, um sich das Startverzeichnis zu merken oder absolute Pfade zu bauen
- Um bei symbolischen Links den echten Ort herauszufinden (`pwd -P`)

!!! tip "Gut zu wissen"
    Die Shell speichert das aktuelle Verzeichnis immer in der Variablen `$PWD`.
    `echo "$PWD"` liefert dasselbe wie `pwd`. Das vorherige Verzeichnis steht in `$OLDPWD`.

!!! warning "Erst prüfen, dann löschen"
    Führe vor `rm`, `chmod -R` oder `chown -R` mit relativen Pfaden einmal `pwd` aus.
    Derselbe Befehl im falschen Verzeichnis kann großen Schaden anrichten.

## Verwandte Befehle

[whoami](../01-orientation/whoami.md) · [cd](cd.md) · [ls](ls.md) · [realpath](realpath.md)
