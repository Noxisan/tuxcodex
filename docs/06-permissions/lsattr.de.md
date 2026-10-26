# lsattr

> Zeigt die besonderen Dateiattribute auf ext4 und ähnlichen Dateisystemen, zum Beispiel „unveränderlich“ oder „nur anhängen“.

![lsattr output](../assets/screenshots/06-permissions/lsattr.png)

## Syntax

```bash
lsattr [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-d` | Das Verzeichnis selbst zeigen, nicht seinen Inhalt |
| `-R` | Auch alle Unterverzeichnisse zeigen |
| `-a` | Auch versteckte Dateien zeigen |
| `-l` | Namen der Attribute statt Buchstaben zeigen |

Die wichtigsten Attribute:

| Buchstabe | Name | Bedeutung |
|-----------|------|-----------|
| `i` | Immutable | Niemand darf die Datei ändern, umbenennen oder löschen, auch nicht `root` |
| `a` | Append only | Daten können nur am Ende angehängt, nicht überschrieben werden |
| `e` | Extents | Die Datei nutzt Extents (normal bei ext4, kein Schutz) |
| `A` | No atime | Die Zugriffszeit wird nicht aktualisiert |

## Beispiele

**Die Attribute einer Datei anzeigen:**

```bash
lsattr /etc/resolv.conf
```

```text
--------------e------- /etc/resolv.conf
```

Nur `e` ist gesetzt, das ist bei ext4 normal. Die Datei ist nicht geschützt.

**Eine geschützte Datei:**

```bash
lsattr /etc/resolv.conf
```

```text
----i---------e------- /etc/resolv.conf
```

Das `i` bedeutet: Die Datei ist unveränderlich.

**Die Attribute mit Namen anzeigen:**

```bash
lsattr -l /etc/resolv.conf
```

```text
/etc/resolv.conf             Immutable, Extents
```

**Alle Dateien in einem Verzeichnis prüfen:**

```bash
lsattr /var/log/app/
```

```text
-----a--------e------- /var/log/app/audit.log
--------------e------- /var/log/app/error.log
```

`audit.log` ist „nur anhängen“: Einträge können ergänzt, aber nicht gelöscht oder
geändert werden.

**Die Attribute eines Verzeichnisses selbst anzeigen:**

```bash
lsattr -d /var/log/app
```

```text
--------------e------- /var/log/app
```

## Wann brauche ich das?

- Wenn selbst `root` beim Ändern oder Löschen einer Datei `Operation not permitted`
  bekommt: Oft ist ein `i`- oder `a`-Attribut der Grund
- Wenn ein Paket-Update scheitert, weil eine Konfigurationsdatei nicht ersetzt werden kann
- Um zu prüfen, ob Schutzattribute, die du mit `chattr` gesetzt hast, noch aktiv sind

!!! tip "„Operation not permitted“ als root"
    Schlägt `sudo rm` oder das Bearbeiten mit `sudo` mit `Operation not permitted` fehl,
    führe zuerst `lsattr` auf die Datei aus. Normale Rechte halten `root` nie auf,
    Attribute schon.

!!! warning "Nur auf bestimmten Dateisystemen"
    Attribute sind eine Funktion von ext2/3/4 und teilweise von Btrfs und XFS. Auf anderen
    Dateisystemen wie `tmpfs` oder Netzwerkfreigaben meldet `lsattr` einen Fehler.

## Verwandte Befehle

[stat](../03-files/stat.md) · [ls](../02-navigation/ls.md)
