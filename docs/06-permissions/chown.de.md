# chown

> Ändert Besitzer und Gruppe von Dateien und Verzeichnissen.

![chown output](../assets/screenshots/06-permissions/chown.png)

## Syntax

```bash
chown [OPTION]... [BESITZER][:[GRUPPE]] DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-R`, `--recursive` | Auch alle Dateien und Verzeichnisse darunter ändern |
| `-v`, `--verbose` | Jede Änderung anzeigen |
| `-c`, `--changes` | Nur Dateien anzeigen, deren Besitzer sich wirklich geändert hat |
| `-h`, `--no-dereference` | Einen symbolischen Link selbst ändern, nicht sein Ziel |
| `--reference=DATEI` | Besitzer und Gruppe von `DATEI` übernehmen |

| Form | Bedeutung |
|------|-----------|
| `nox` | Nur den Besitzer ändern |
| `nox:www-data` | Besitzer und Gruppe ändern |
| `:www-data` | Nur die Gruppe ändern (wie `chgrp`) |
| `nox:` | Besitzer `nox` und die Login-Gruppe von `nox` |

## Beispiele

**Eine Website dem Webserver-Benutzer übergeben:**

```bash
sudo chown -v www-data:www-data /var/www/example.com
```

```text
changed ownership of '/var/www/example.com' from root:root to www-data:www-data
```

**Besitzer und Gruppe eines ganzen Verzeichnisbaums ändern:**

```bash
sudo chown -R www-data:www-data /var/www/example.com
ls -l /var/www/example.com
```

```text
total 8
drwxr-xr-x 2 www-data www-data 4096 Oct 20 09:30 logs
drwxr-xr-x 4 www-data www-data 4096 Oct 20 09:30 public
```

**Nur den Besitzer ändern:**

```bash
sudo chown -v nox report.txt
```

```text
changed ownership of 'report.txt' from root to nox
```

**Dateien zurückholen, die mit `sudo` angelegt wurden:**

```bash
sudo chown -Rc nox: ~/projects
```

```text
changed ownership of '/home/nox/projects/app/.env' from root:root to nox:nox
changed ownership of '/home/nox/projects/app' from root:root to nox:nox
```

`-c` listet nur die Dateien auf, die sich wirklich geändert haben.

**Ohne `sudo` versuchen:**

```bash
chown www-data /var/www/example.com/public/index.html
```

```text
chown: changing ownership of '/var/www/example.com/public/index.html': Operation not permitted
```

Nur `root` darf Dateien einem anderen Benutzer übergeben.

## Wann brauche ich das?

- Wenn ein Dienst seine Dateien nicht schreiben kann, etwa Uploads oder Cache einer
  Website (`www-data`), ein Datenbankverzeichnis (`postgres`) oder ein Anwendungsbenutzer
- Nach dem Kopieren oder Entpacken als `root`, wenn die Dateien danach `root` gehören
- Wenn Dateien in deinem Home-Verzeichnis `root` gehören, weil du etwas mit `sudo`
  ausgeführt hast

!!! tip "Besitzer und Gruppe in einem Schritt"
    `chown benutzer:gruppe` ersetzt ein separates `chgrp`. Mit `benutzer:` (Doppelpunkt,
    keine Gruppe) wird die Login-Gruppe des Benutzers gesetzt.

!!! warning "Einem Dienst nur geben, was er braucht"
    Ein Webserver sollte nur die Verzeichnisse besitzen, in die er wirklich schreibt
    (Uploads, Cache). Gehört ihm die ganze Anwendung, kann ein Angreifer, der den
    Webserver übernimmt, auch den Code ändern.

!!! danger "`chown -R` auf den falschen Pfad"
    `sudo chown -R nox / var/www` (mit einem Leerzeichen zu viel) ändert den Besitzer des
    **ganzen Systems**, und der Server startet danach nicht mehr richtig. Prüfe den Pfad
    zweimal, bevor du ++enter++ drückst.

## Verwandte Befehle

[chmod](chmod.md) · [id](../01-orientation/id.md)
