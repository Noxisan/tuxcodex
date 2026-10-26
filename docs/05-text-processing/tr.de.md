# tr

> Ersetzt, verdichtet oder löscht einzelne Zeichen in einem Textstrom.

![tr output](../assets/screenshots/05-text-processing/tr.png)

## Syntax

```bash
tr [OPTION]... MENGE1 [MENGE2]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Jedes Zeichen aus `MENGE1` durch das passende aus `MENGE2` ersetzen |
| `-d`, `--delete` | Alle Zeichen aus `MENGE1` löschen |
| `-s`, `--squeeze-repeats` | Wiederholte Zeichen zu einem zusammenfassen |
| `-c`, `--complement` | Alle Zeichen verwenden, die **nicht** in `MENGE1` sind |

Nützliche Zeichenmengen: `a-z`, `A-Z`, `0-9`, `[:upper:]`, `[:lower:]`, `[:digit:]`,
`[:space:]`, `'\n'` (Zeilenumbruch), `'\r'` (Windows-Zeilenende), `'\t'` (Tab).

## Beispiele

**In Großbuchstaben umwandeln:**

```bash
echo "Hello World" | tr 'a-z' 'A-Z'
```

```text
HELLO WORLD
```

**In Kleinbuchstaben umwandeln:**

```bash
echo "Hello World" | tr '[:upper:]' '[:lower:]'
```

```text
hello world
```

**Windows-Zeilenenden aus einem Skript entfernen:**

```bash
tr -d '\r' < deploy.sh > deploy-fixed.sh
file deploy-fixed.sh
```

```text
deploy-fixed.sh: Bourne-Again shell script, ASCII text executable
```

**Mehrere Leerzeichen zu einem zusammenfassen:**

```bash
echo "too    many   spaces" | tr -s ' '
```

```text
too many spaces
```

**Eine durch Doppelpunkte getrennte Liste zeilenweise anzeigen:**

```bash
echo "/usr/local/bin:/usr/bin:/bin" | tr ':' '\n'
```

```text
/usr/local/bin
/usr/bin
/bin
```

**Ein zufälliges Passwort erzeugen:**

```bash
tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 20; echo
```

```text
q8ZkT3vNw1LpXa7RcY0m
```

`-dc` löscht jedes Zeichen, das **kein** Buchstabe und keine Ziffer ist, sodass nur diese
übrig bleiben.

## Wann brauche ich das?

- Um Dateien mit Windows-Zeilenenden zu reparieren (`tr -d '\r'`)
- Um Groß- und Kleinschreibung vor dem Vergleichen oder Zählen zu vereinheitlichen
- Um Listen wie `$PATH` in Zeilen aufzuteilen oder Zeilen zu einer Liste zu verbinden
  (`tr '\n' ','`)
- Um Ausgaben mit mehreren Leerzeichen aufzuräumen, bevor sie an `cut` gehen

!!! tip "Ein Eintrag pro Zeile"
    `echo "$PATH" | tr ':' '\n'` zeigt jedes Verzeichnis deines Suchpfads in einer eigenen
    Zeile. Das ist viel leichter zu lesen.

!!! warning "`tr` liest nur von der Standardeingabe"
    `tr` nimmt keinen Dateinamen an. `tr a b users.csv` scheitert mit
    `tr: extra operand ‘users.csv’`. Nimm stattdessen `tr a b < users.csv` oder eine Pipe.

!!! warning "Keine Umlaute"
    GNU `tr` arbeitet Byte für Byte. Zeichen wie `ä` oder `é` bestehen in UTF-8 aus
    mehreren Bytes und werden nicht umgewandelt oder sogar beschädigt. Für solchen Text
    nimm `sed`.

## Verwandte Befehle

[cut](cut.md) · [file](../03-files/file.md)
