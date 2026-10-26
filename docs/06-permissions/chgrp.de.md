# chgrp

> Ändert nur die Gruppe von Dateien und Verzeichnissen.

![chgrp output](../assets/screenshots/06-permissions/chgrp.png)

## Syntax

```bash
chgrp [OPTION]... GRUPPE DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-R`, `--recursive` | Auch alle Dateien und Verzeichnisse darunter ändern |
| `-v`, `--verbose` | Jede Änderung anzeigen |
| `-c`, `--changes` | Nur Dateien anzeigen, deren Gruppe sich wirklich geändert hat |
| `-h`, `--no-dereference` | Einen symbolischen Link selbst ändern, nicht sein Ziel |
| `--reference=DATEI` | Die Gruppe von `DATEI` übernehmen |

## Beispiele

**Einer Gruppe Zugriff auf ein Verzeichnis geben:**

```bash
sudo chgrp -v developers /srv/shared
```

```text
changed group of '/srv/shared' from root to developers
```

**Die Gruppe eines ganzen Verzeichnisbaums ändern:**

```bash
sudo chgrp -R developers /srv/shared
ls -l /srv/shared
```

```text
total 8
-rw-rw-r-- 1 nox   developers 1840 Oct 26 10:12 notes.md
drwxrwsr-x 2 alice developers 4096 Oct 26 10:30 scripts
```

**Einen Dienst einen Schlüssel lesen lassen, ohne ihm die Datei zu geben:**

```bash
sudo chgrp ssl-cert /etc/ssl/private/example.com.key
sudo chmod 640 /etc/ssl/private/example.com.key
ls -l /etc/ssl/private/example.com.key
```

```text
-rw-r----- 1 root ssl-cert 1704 Oct 20 11:05 /etc/ssl/private/example.com.key
```

`root` bleibt Besitzer, Mitglieder von `ssl-cert` dürfen den Schlüssel lesen.

**In eine Gruppe wechseln, zu der du nicht gehörst:**

```bash
chgrp www-data notes.txt
```

```text
chgrp: changing group of 'notes.txt': Operation not permitted
```

Ohne `sudo` kannst du nur in Gruppen wechseln, in denen du selbst Mitglied bist.

## Wann brauche ich das?

- Um gemeinsame Verzeichnisse für ein Team einzurichten (zusammen mit `chmod g+s`)
- Um einen Dienst eine Datei über seine Gruppe lesen zu lassen, während `root` Besitzer
  bleibt, etwa TLS-Schlüssel und die Gruppe `ssl-cert`
- Wenn du nur die Gruppe ändern und den Besitzer lassen willst, wie er ist

!!! tip "Welche Gruppen habe ich?"
    `id -Gn` listet alle Gruppen auf, zu denen du gehörst. Das sind die Gruppen, die du
    ohne `sudo` mit `chgrp` verwenden kannst.

!!! warning "Die Gruppenrechte müssen passen"
    Die Gruppe zu ändern gibt allein noch niemandem Zugriff. Die Gruppe braucht auch die
    passenden Rechte: prüfe mit `ls -l` und passe mit `chmod g+r` oder `chmod g+w` an.

## Verwandte Befehle

[chown](chown.md) · [chmod](chmod.md) · [id](../01-orientation/id.md)
