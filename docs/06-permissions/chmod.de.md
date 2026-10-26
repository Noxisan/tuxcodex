# chmod

> Ändert die Rechte von Dateien und Verzeichnissen, als Zahl (`640`) oder mit Buchstaben (`u+x`).

![chmod output](../assets/screenshots/06-permissions/chmod.png)

## Syntax

```bash
chmod [OPTION]... MODUS DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-R`, `--recursive` | Auch alle Dateien und Verzeichnisse darunter ändern |
| `-v`, `--verbose` | Jede Änderung anzeigen |
| `-c`, `--changes` | Nur Dateien anzeigen, deren Rechte sich wirklich geändert haben |
| `--reference=DATEI` | Die Rechte von `DATEI` übernehmen |

Den `MODUS` kannst du auf zwei Arten schreiben:

| Form | Beispiel | Bedeutung |
|------|----------|-----------|
| Zahl | `640` | Besitzer `rw-`, Gruppe `r--`, andere `---` |
| Buchstaben | `u+x` | Ausführrecht für den Besitzer (`u`) hinzufügen |
| | `g-w` | Schreibrecht für die Gruppe (`g`) entfernen |
| | `o=` | Alle Rechte für andere (`o`) entfernen |
| | `a+r` | Leserecht für alle (`a` = `u`, `g` und `o`) |
| | `g+s` | SGID-Bit auf einem Verzeichnis setzen |

## Beispiele

**Ein Skript ausführbar machen:**

```bash
chmod -v u+x deploy.sh
```

```text
mode of 'deploy.sh' changed from 0644 (rw-r--r--) to 0744 (rwxr--r--)
```

**Rechte als Zahl setzen:**

```bash
chmod -v 640 /etc/app/secrets.conf
```

```text
mode of '/etc/app/secrets.conf' changed from 0644 (rw-r--r--) to 0640 (rw-r-----)
```

**Alle Rechte für andere entfernen:**

```bash
chmod -v o-rwx deploy.sh
```

```text
mode of 'deploy.sh' changed from 0744 (rwxr--r--) to 0740 (rwxr-----)
```

**Einen privaten SSH-Schlüssel schützen:**

```bash
chmod 600 ~/.ssh/id_ed25519
ls -l ~/.ssh/id_ed25519
```

```text
-rw------- 1 nox nox 411 Oct 20 14:12 /home/nox/.ssh/id_ed25519
```

**Die Rechte einer ganzen Website korrigieren, Verzeichnisse und Dateien getrennt:**

```bash
find /var/www/example.com -type d -exec chmod 755 {} +
find /var/www/example.com -type f -exec chmod 644 {} +
stat -c '%a %n' /var/www/example.com/public /var/www/example.com/public/index.html
```

```text
755 /var/www/example.com/public
644 /var/www/example.com/public/index.html
```

**Ein gemeinsames Verzeichnis für eine Gruppe einrichten:**

```bash
sudo chmod 2775 /srv/shared
ls -ld /srv/shared
```

```text
drwxrwsr-x 2 root developers 4096 Oct 26 10:42 /srv/shared
```

Das `s` bei den Gruppenrechten ist das SGID-Bit: Neue Dateien in `/srv/shared` gehören
automatisch der Gruppe `developers`.

## Wann brauche ich das?

- Um Skripte ausführbar zu machen
- Um private Schlüssel, Passwörter und Konfigurationsdateien mit Geheimnissen zu schützen
  (`600`, `640`)
- Um Rechte nach dem Kopieren oder Entpacken zu korrigieren, etwa bei einer Website
- Wenn SSH einen Schlüssel mit `UNPROTECTED PRIVATE KEY FILE!` ablehnt, weil seine Rechte
  zu offen sind

!!! tip "Zahlen oder Buchstaben?"
    Zahlen setzen **alle** Rechte auf einmal und sind eindeutig: `chmod 640` liefert
    immer dasselbe Ergebnis. Buchstaben ändern nur einzelne Rechte und lassen den Rest,
    wie er ist, praktisch für `chmod +x`.

!!! warning "`chmod -R 755` macht jede Datei ausführbar"
    `-R` behandelt Dateien und Verzeichnisse gleich. Verzeichnisse brauchen `x`, normale
    Dateien meist nicht. Nimm `find -type d` und `find -type f` wie oben gezeigt.

!!! danger "Niemals `chmod 777`"
    `777` erlaubt **jedem** auf dem Server, die Dateien zu ändern und zu ersetzen. Eine
    Website mit `777` kann jeder Prozess und jeder Benutzer übernehmen. Wenn ein Dienst
    nicht schreiben kann, gib stattdessen dem richtigen Besitzer oder der richtigen Gruppe
    Zugriff (`chown`, `chgrp`).

## Verwandte Befehle

[ls](../02-navigation/ls.md) · [stat](../03-files/stat.md) · [chown](chown.md) · [chgrp](chgrp.md) · [umask](umask.md)
