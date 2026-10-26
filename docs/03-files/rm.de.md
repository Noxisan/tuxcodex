# rm

> Löscht Dateien und Verzeichnisse endgültig, ohne Papierkorb.

![rm output](../assets/screenshots/03-files/rm.png)

## Syntax

```bash
rm [OPTION]... DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-r`, `-R`, `--recursive` | Verzeichnisse mit ihrem ganzen Inhalt löschen |
| `-f`, `--force` | Nie nachfragen, nicht vorhandene Dateien ignorieren |
| `-i` | Vor jeder einzelnen Datei nachfragen |
| `-I` | Einmal nachfragen, bevor mehr als drei Dateien oder rekursiv gelöscht wird |
| `-v`, `--verbose` | Jede gelöschte Datei anzeigen |
| `-d`, `--dir` | Leere Verzeichnisse löschen |
| `--` | Ende der Optionen: alles danach ist ein Dateiname |

## Beispiele

**Eine Datei löschen:**

```bash
rm -v notes-old.txt
```

```text
removed 'notes-old.txt'
```

**Ein Verzeichnis ohne `-r` löschen:**

```bash
rm scripts-2026
```

```text
rm: cannot remove 'scripts-2026': Is a directory
```

**Ein Verzeichnis mit seinem ganzen Inhalt löschen:**

```bash
rm -rv scripts-2026
```

```text
removed 'scripts-2026/cleanup.sh'
removed 'scripts-2026/backup.sh'
removed directory 'scripts-2026'
```

**Vor dem Löschen vieler Dateien einmal nachfragen:**

```bash
rm -I *.log
```

```text
rm: remove 5 arguments?
```

**Eine schreibgeschützte Datei löschen:**

```bash
rm notes.txt
```

```text
rm: remove write-protected regular file 'notes.txt'?
```

`rm` fragt nach, weil die Datei keine Schreibrechte hat. Mit `y` löschst du sie trotzdem.

**Eine Datei löschen, deren Name mit `-` beginnt:**

```bash
rm -file.txt
rm ./-file.txt
```

```text
rm: invalid option -- 'l'
Try 'rm ./-file.txt' to remove the file '-file.txt'.
Try 'rm --help' for more information.
```

Der erste Befehl scheitert, weil `rm` `-file.txt` als Optionen liest. Der zweite funktioniert.

## Wann brauche ich das?

- Um alte Logs, Backups, temporäre Dateien und Reste von Installationen aufzuräumen
- Um eine Website, eine Anwendung oder die Daten eines Benutzers zu entfernen, die nicht
  mehr gebraucht werden
- Um Platz zu schaffen, wenn eine Partition voll ist

!!! tip "Sicherheitsnetz mit `-I`"
    `rm -I` fragt nur einmal, aber vor großen Löschaktionen. Das nervt viel weniger als
    `-i` und verhindert trotzdem die meisten Unfälle mit Wildcards.

!!! warning "Es gibt keinen Papierkorb"
    Mit `rm` gelöschte Dateien sind weg. Nur ein Backup bringt sie zurück. Prüfe
    Wildcards vorher mit `ls`: erst `ls *.log`, dann `rm *.log`.

!!! danger "`rm -rf` mit Variablen in Skripten"
    Ist eine Variable leer, wird aus `rm -rf "$DIR/"*` ein `rm -rf /*`, und das ganze
    System ist gelöscht. Lass Bash abbrechen, wenn die Variable leer ist:

    ```bash
    rm -rf "${DIR:?}/"*
    ```

    `/` selbst löscht `rm` nicht (`--preserve-root` ist Standard), `/*` ist aber nicht
    geschützt.

## Verwandte Befehle

[mv](mv.md) · [find](../02-navigation/find.md) · [rmdir](rmdir.md) · [truncate](truncate.md) · [shred](shred.md)
