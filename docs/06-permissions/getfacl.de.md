# getfacl

> Zeigt die Zugriffskontrolllisten (ACLs) von Dateien und Verzeichnissen: zusätzliche Rechte für einzelne Benutzer und Gruppen.

![getfacl output](../assets/screenshots/06-permissions/getfacl.png)

## Syntax

```bash
getfacl [OPTION]... DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-c`, `--omit-header` | Kommentarzeilen mit Dateiname, Besitzer und Gruppe weglassen |
| `-R`, `--recursive` | Auch die ACLs aller Dateien darunter zeigen |
| `-a`, `--access` | Nur die Zugriffs-ACL zeigen |
| `-d`, `--default` | Nur die Default-ACL eines Verzeichnisses zeigen |
| `-p`, `--absolute-names` | Den führenden `/` in Pfadnamen behalten |

| Eintrag | Bedeutung |
|---------|-----------|
| `user::rw-` | Rechte des Besitzers |
| `user:alice:r--` | Zusätzliche Rechte für den Benutzer `alice` |
| `group::r--` | Rechte der besitzenden Gruppe |
| `group:developers:rwx` | Zusätzliche Rechte für die Gruppe `developers` |
| `mask::r--` | Obergrenze für alle zusätzlichen Einträge und die Gruppe |
| `other::---` | Rechte für alle anderen |
| `default:…` | Rechte, die neue Dateien in einem Verzeichnis erben |

## Beispiele

**Die ACL einer Datei ohne zusätzliche Einträge anzeigen:**

```bash
getfacl report.pdf
```

```text
# file: report.pdf
# owner: nox
# group: nox
user::rw-
group::r--
other::---
```

Ohne zusätzliche Einträge ist das dasselbe, was `ls -l` zeigt: `rw-r-----`.

**Eine Datei mit einem zusätzlichen Benutzer:**

```bash
getfacl report.pdf
```

```text
# file: report.pdf
# owner: nox
# group: nox
user::rw-
user:alice:r--
group::r--
mask::r--
other::---
```

`alice` darf die Datei lesen, ohne Besitzer oder Mitglied der Gruppe zu sein.

**Die ACL eines Verzeichnisses mit vererbten Rechten anzeigen:**

```bash
getfacl /srv/shared
```

```text
getfacl: Removing leading '/' from absolute path names
# file: srv/shared
# owner: root
# group: root
user::rwx
group::r-x
group:developers:rwx
mask::rwx
other::---
default:user::rwx
default:group::r-x
default:group:developers:rwx
default:mask::rwx
default:other::---
```

Die `default:`-Einträge erbt jede neue Datei in `/srv/shared`.

**Rechte finden, die durch die Maske eingeschränkt sind:**

```bash
getfacl -c /srv/shared/new.txt
```

```text
getfacl: Removing leading '/' from absolute path names
user::rw-
group::r-x      #effective:r--
group:developers:rwx    #effective:rw-
mask::rw-
other::---
```

`#effective` zeigt, was wirklich gilt: Die Maske `rw-` nimmt das `x` weg.

## Wann brauche ich das?

- Wenn `ls -l` hinter den Rechten ein `+` zeigt (`-rw-r-----+`): Es gibt zusätzliche
  ACL-Einträge, die `ls` nicht anzeigt
- Um herauszufinden, warum ein Benutzer auf eine Datei zugreifen kann, obwohl Besitzer,
  Gruppe und Rechte das nicht erlauben, oder umgekehrt
- Um gemeinsame Verzeichnisse zu prüfen, in denen mehrere Gruppen unterschiedliche Rechte
  haben

!!! tip "Das `+` bei `ls -l`"
    Ein `+` am Ende der Rechte bei `ls -l` ist das Zeichen, dass eine Datei ACLs hat. Was
    darin steht, zeigt nur `getfacl`.

!!! warning "Paket `acl`"
    `getfacl` und `setfacl` stecken im Paket `acl`, das unter RHEL und Arch und meist auch
    unter Debian und Ubuntu installiert ist. Fehlen die Befehle, installierst du es mit
    `sudo apt install acl`.

## Verwandte Befehle

[chmod](chmod.md) · [ls](../02-navigation/ls.md) · [setfacl](setfacl.md)
