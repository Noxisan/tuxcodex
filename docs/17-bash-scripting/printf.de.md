# printf

> Gibt formatierten Text aus: Spalten, Zahlen mit fester Stellenzahl, aufgefüllte Werte. Genauer und portabler als `echo`.

![printf output](../assets/screenshots/17-bash-scripting/printf.png)

## Syntax

```bash
printf FORMAT [ARGUMENT]...
```

Das Format wird wiederverwendet, solange Argumente übrig sind. `printf` fügt nie von selbst einen Zeilenumbruch an.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `%s` | Eine Zeichenkette einsetzen |
| `%d` | Eine Ganzzahl einsetzen |
| `%.2f` | Kommazahl mit zwei Nachkommastellen |
| `%-12s`, `%8s` | Links- oder rechtsbündig in einer Spalte dieser Breite |
| `\n`, `\t` | Neue Zeile, Tab |
| `%%` | Ein echtes Prozentzeichen |
| `%(%F %T)T` | Datum und Uhrzeit (Bash), mit `-1` für jetzt |

## Beispiele

**Eine ausgerichtete Tabelle:**

```bash
printf "%-12s %8s\n" "Service" "Status" "nginx" "active" "postgresql" "active"
```

```text
Service        Status
nginx          active
postgresql     active
```

**Text mit Zahlen:**

```bash
printf "Disk %s is %d%% full\n" /dev/sda2 50
```

```text
Disk /dev/sda2 is 50% full
```

**Eine Zeile pro Argument:**

```bash
printf "%s\n" web01 web02 db01
```

```text
web01
web02
db01
```

**Ein Zeitstempel für Logzeilen:**

```bash
printf '%(%F %T)T backup started\n' -1
```

```text
2026-10-26 10:42:17 backup started
```

## Wann brauche ich das?

- Für Tabellen und ausgerichtete Ausgaben in Skripten
- Für exakte Ausgaben ohne Überraschungen, etwa in Dateien, die andere Programme lesen
- Statt `echo -e` und `echo -n`

!!! tip "Zeitstempel ohne `date`"
    `printf '%(%F %T)T\n' -1` gibt Datum und Uhrzeit aus, ohne das Programm `date` zu starten.

## Verwandte Befehle

[echo](echo.md) · [column](../05-text-processing/column.md) · [date](../01-orientation/date.md)
