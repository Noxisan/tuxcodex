# source

> Führt eine Datei in der aktuellen Shell statt in einer neuen aus. Variablen und Funktionen daraus bleiben danach verfügbar. `.` ist derselbe Befehl.

![source output](../assets/screenshots/17-bash-scripting/source.png)

## Syntax

```bash
source DATEI [ARGUMENT]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `source DATEI` | Die Datei in der aktuellen Shell ausführen |
| `. DATEI` | Dasselbe, portabel für andere Shells |

## Beispiele

**Eine Konfigurationsdatei laden:**

```bash
cat app.env
source app.env
echo "$DB_HOST/$DB_NAME"
```

```text
DB_HOST=192.0.2.20
DB_NAME=shop
192.0.2.20/shop
```

**`~/.bashrc` nach einer Änderung neu laden:**

```bash
echo "alias ll='ls -lh'" >> ~/.bashrc
source ~/.bashrc
alias ll
```

```text
alias ll='ls -lh'
```

**Eine Datei, die es nicht gibt:**

```bash
source nosuch.env
```

```text
bash: nosuch.env: No such file or directory
```

## Wann brauche ich das?

- Um eine Konfigurationsdatei mit Variablen in ein Skript zu laden
- Um Funktionen zwischen mehreren Skripten zu teilen
- Um Änderungen an `~/.bashrc` zu übernehmen, ohne sich neu anzumelden

!!! tip "Konfiguration in einer eigenen Datei"
    Halte Hostnamen, Pfade und Zugangsdaten in einer Datei wie `/etc/backup.conf` und lade sie
    mit `source`. Das Skript selbst bleibt dann auf jedem Server gleich.

!!! danger "`source` führt alles aus"
    `source` führt die Datei als Code aus. Eine Konfigurationsdatei, in die andere schreiben
    können, ist ein Sicherheitsloch: Mach sie nur für root beschreibbar.

## Verwandte Befehle

[export](export.md) · [function](function.md)
