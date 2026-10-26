# rmdir

> Löscht leere Verzeichnisse und weigert sich, sobald ein Verzeichnis noch etwas enthält.

## Syntax

```bash
rmdir [OPTION]... VERZEICHNIS...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-p`, `--parents` | Auch die übergeordneten Verzeichnisse löschen, wenn sie dadurch leer werden |
| `-v`, `--verbose` | Jedes gelöschte Verzeichnis anzeigen |
| `--ignore-fail-on-non-empty` | Kein Fehler bei Verzeichnissen, die nicht leer sind |

## Beispiele

**Ein leeres Verzeichnis löschen:**

```bash
rmdir -v private
```

```text
rmdir: removing directory, 'private'
```

**Versuchen, ein nicht leeres Verzeichnis zu löschen:**

```bash
rmdir backup
```

```text
rmdir: failed to remove 'backup': Directory not empty
```

**Einen Pfad aus leeren Verzeichnissen von innen nach außen löschen:**

```bash
rmdir -pv backup/2026/10
```

```text
rmdir: removing directory, 'backup/2026/10'
rmdir: removing directory, 'backup/2026'
rmdir: removing directory, 'backup'
rmdir: failed to remove directory 'backup': Directory not empty
```

`10` und `2026` waren leer und sind weg. `backup` enthält noch Dateien und bleibt.

**Aufräumen ohne Fehlermeldungen:**

```bash
rmdir -p --ignore-fail-on-non-empty backup/2026/10
echo $?
```

```text
0
```

![rmdir output](../assets/screenshots/03-files/rmdir.png)

## Wann brauche ich das?

- Um leere Verzeichnisse nach dem Verschieben oder Löschen von Dateien aufzuräumen
- In Skripten, wenn ein Verzeichnis nur entfernt werden soll, wenn es wirklich leer ist
- Als sichere Alternative zu `rm -r`: `rmdir` kann nie versehentlich Dateien löschen

!!! tip "Alle leeren Verzeichnisse finden"
    Um alle leeren Verzeichnisse unterhalb eines Pfads zu entfernen, kombinierst du
    `find` mit `-empty`: `find /srv/backup -type d -empty -delete`. Prüfe die Liste
    vorher ohne `-delete`.

!!! warning "Versteckte Dateien zählen mit"
    Meldet `rmdir` `Directory not empty`, obwohl `ls` nichts zeigt, liegen versteckte
    Dateien darin. Prüfe mit `ls -A`.

## Verwandte Befehle

[rm](rm.md) · [mkdir](mkdir.md)
