# setfacl

> Setzt Zugriffskontrolllisten (ACLs): gibt einzelnen Benutzern oder Gruppen Rechte zusätzlich zu Besitzer, Gruppe und anderen.

![setfacl output](../assets/screenshots/06-permissions/setfacl.png)

## Syntax

```bash
setfacl [OPTION]... EINTRAG DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-m EINTRAG`, `--modify` | Einen Eintrag hinzufügen oder ändern, z. B. `u:alice:r` oder `g:developers:rwx` |
| `-x EINTRAG`, `--remove` | Einen Eintrag entfernen, z. B. `u:alice` |
| `-b`, `--remove-all` | Alle zusätzlichen Einträge entfernen |
| `-d`, `--default` | Die Default-ACL eines Verzeichnisses ändern (wird an neue Dateien vererbt) |
| `-R`, `--recursive` | Auch auf alle Dateien und Verzeichnisse darunter anwenden |
| `-k`, `--remove-default` | Die Default-ACL entfernen |

Einträge schreibst du als `TYP:NAME:RECHTE`: `u` für einen Benutzer, `g` für eine Gruppe,
danach `r`, `w` und `x`.

## Beispiele

**Einem einzelnen Benutzer Lesezugriff geben:**

```bash
setfacl -m u:alice:r report.pdf
getfacl -c report.pdf
```

```text
user::rw-
user:alice:r--
group::r--
mask::r--
other::---
```

**Einer Gruppe vollen Zugriff auf ein Verzeichnis geben:**

```bash
sudo setfacl -m g:developers:rwx /srv/shared
ls -ld /srv/shared
```

```text
drwxrwx---+ 2 root root 4096 Oct 26 10:42 /srv/shared
```

Das `+` zeigt, dass das Verzeichnis jetzt eine ACL hat.

**Neue Dateien die Rechte erben lassen:**

```bash
sudo setfacl -d -m g:developers:rwx /srv/shared
getfacl -c -d /srv/shared
```

```text
getfacl: Removing leading '/' from absolute path names
user::rwx
group::r-x
group:developers:rwx
mask::rwx
other::---
```

Jede Datei, die ab jetzt in `/srv/shared` entsteht, bekommt den Eintrag für `developers`.

**Dem Webserver Lesezugriff auf einen vorhandenen Verzeichnisbaum geben:**

```bash
sudo setfacl -R -m u:www-data:rX /srv/app/public
getfacl -c /srv/app/public/index.html
```

```text
getfacl: Removing leading '/' from absolute path names
user::rw-
user:www-data:r--
group::r--
mask::r--
other::---
```

**Einen einzelnen Eintrag entfernen:**

```bash
setfacl -x u:alice report.pdf
getfacl -c report.pdf
```

```text
user::rw-
group::r--
mask::r--
other::---
```

**Alle zusätzlichen Einträge entfernen:**

```bash
sudo setfacl -b /srv/shared
ls -ld /srv/shared
```

```text
drwxr-x--- 2 root root 4096 Oct 26 10:42 /srv/shared
```

## Wann brauche ich das?

- Wenn ein zweiter Benutzer oder Dienst Zugriff braucht, du aber Besitzer oder Gruppe
  nicht ändern willst, etwa ein Backup-Benutzer, der ein Webverzeichnis liest
- Für gemeinsame Verzeichnisse, in denen mehrere Teams unterschiedliche Rechte brauchen
- Wenn neue Dateien automatisch bestimmte Rechte bekommen sollen (Default-ACL), egal mit
  welcher `umask` das erzeugende Programm arbeitet

!!! tip "`X` statt `x`"
    Ein großes `X` gibt das Ausführrecht nur Verzeichnissen (und Dateien, die schon
    ausführbar sind). `setfacl -R -m u:www-data:rX VERZ` macht einen Baum lesbar, ohne
    jede Datei ausführbar zu machen.

!!! warning "`chmod` ändert die Maske"
    Nach einem `chmod g-w` auf eine Datei mit ACLs wird auch die Maske verkleinert, und
    die zusätzlichen Einträge verlieren eventuell Rechte. `getfacl` zeigt dann
    `#effective:`. Prüfe die ACL nach jedem `chmod`.

## Verwandte Befehle

[getfacl](getfacl.md) · [chmod](chmod.md)
