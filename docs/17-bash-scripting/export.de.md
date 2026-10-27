# export

> Macht eine Variable für Programme und Skripte verfügbar, die aus der aktuellen Shell gestartet werden (Umgebungsvariable).

![export output](../assets/screenshots/17-bash-scripting/export.png)

## Syntax

```bash
export NAME[=WERT]...
```

Eine normale Variable gibt es nur in der aktuellen Shell. Nur exportierte Variablen werden an Kindprozesse weitergegeben.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `NAME=WERT` | Setzen und exportieren in einem Schritt |
| `-p` | Alle exportierten Variablen auflisten |
| `-n NAME` | Den Export aufheben, die Variable behalten |

## Beispiele

**Ohne und mit `export`:**

```bash
BACKUP_DIR=/mnt/backup
bash -c 'echo "child sees: [$BACKUP_DIR]"'
export BACKUP_DIR
bash -c 'echo "child sees: [$BACKUP_DIR]"'
```

```text
child sees: []
child sees: [/mnt/backup]
```

**Die exportierte Variable anzeigen:**

```bash
export -p | grep BACKUP
```

```text
declare -x BACKUP_DIR="/mnt/backup"
```

**Den Editor für alle Programme setzen:**

```bash
export EDITOR=vim
echo "$EDITOR"
```

```text
vim
```

## Wann brauche ich das?

- Um ein Programm über Umgebungsvariablen zu konfigurieren, etwa `EDITOR` oder `http_proxy`
- Um Einstellungen an Skripte weiterzugeben, die dein Skript startet
- In `~/.bashrc`, um Variablen für jede neue Shell zu setzen

!!! tip "Nur für einen Befehl"
    `BACKUP_DIR=/mnt/backup ./backup.sh` setzt die Variable nur für diesen einen Befehl, ohne
    `export` und ohne deine Shell zu ändern.

!!! warning "Exportierte Variablen fließen nicht zurück"
    Ein Skript kann die Variablen der Shell, die es gestartet hat, nicht ändern. Um Variablen
    in die aktuelle Shell zu laden, nimm [`source`](source.md).

## Verwandte Befehle

[source](source.md)
