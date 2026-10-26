# cd

> Wechselt das aktuelle Verzeichnis.

## Syntax

```bash
cd [OPTION] [VERZEICHNIS]
```

## Optionen

| Option / Argument | Beschreibung |
|-------------------|--------------|
| *(keins)* oder `~` | Ins eigene Home-Verzeichnis wechseln |
| `-` | Zurück ins vorherige Verzeichnis und dessen Pfad ausgeben |
| `..` | Eine Ebene nach oben |
| `~BENUTZER` | Ins Home-Verzeichnis von `BENUTZER` wechseln |
| `-L` | Symbolischen Links logisch folgen (Standard) |
| `-P` | Symbolische Links auflösen und ins physische Verzeichnis wechseln |

## Beispiele

**In einen absoluten Pfad wechseln:**

```bash
cd /etc/ssh
pwd
```

```text
/etc/ssh
```

**Eine Ebene nach oben gehen:**

```bash
cd ..
pwd
```

```text
/etc
```

**Ins vorherige Verzeichnis zurückspringen:**

```bash
cd /var/log
cd -
```

```text
/etc
```

**Zurück ins eigene Home-Verzeichnis:**

```bash
cd
pwd
```

```text
/home/nox
```

**Ins Home-Verzeichnis eines anderen Benutzers wechseln:**

```bash
cd ~www-data
pwd
```

```text
/var/www
```

**Versuchen, ein Verzeichnis ohne Berechtigung zu betreten:**

```bash
cd /root
```

```text
-bash: cd: /root: Permission denied
```

![cd output](../assets/screenshots/02-navigation/cd.png)

## Wann brauche ich das?

- Ständig: um zu Konfigurationsdateien (`/etc`), Logs (`/var/log`) oder Webinhalten
  (`/var/www`) zu kommen
- Um mit `cd -` schnell zwischen zwei Verzeichnissen zu wechseln, etwa zwischen einem
  Konfigurationsverzeichnis und dem zugehörigen Logverzeichnis
- In Skripten, um vor weiteren Befehlen in einem festen Verzeichnis zu arbeiten

!!! tip "Tab-Vervollständigung nutzen"
    Tippe die ersten Buchstaben eines Verzeichnisses und drücke ++tab++. Bash ergänzt den
    Namen, zweimal ++tab++ zeigt alle Treffer. Das spart Tipparbeit und verhindert Tippfehler.

!!! tip "Hilfe zu `cd`"
    `cd` ist in die Shell eingebaut, deshalb gibt es kein `man cd`. Nimm stattdessen `help cd`.

!!! danger "`cd` in Skripten: immer das Ergebnis prüfen"
    Schlägt `cd` fehl, läuft das Skript im **alten** Verzeichnis weiter. Zusammen mit `rm`
    kann das die falschen Dateien löschen. Brich das Skript deshalb ab, wenn `cd` scheitert:

    ```bash
    cd /var/www/example.com/cache || exit 1
    rm -rf ./*
    ```

## Verwandte Befehle

[pwd](pwd.md)
