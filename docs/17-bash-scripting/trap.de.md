# trap

> Führt einen Befehl aus, wenn das Skript endet oder ein Signal bekommt. Zum Aufräumen temporärer Dateien und zum Freigeben von Sperren, auch nach Fehlern und ++ctrl+c++.

![trap output](../assets/screenshots/17-bash-scripting/trap.png)

## Syntax

```bash
trap 'BEFEHLE' SIGNAL...
```

## Optionen

| Signal | Wann |
|--------|------|
| `EXIT` | Immer, wenn das Skript endet, erfolgreich oder nicht |
| `ERR` | Wenn ein Befehl scheitert (mit `set -e`) |
| `INT` | ++ctrl+c++ |
| `TERM` | `kill` oder `systemctl stop` |
| `trap - SIGNAL` | Die Falle entfernen |
| `trap -p` | Die aktiven Fallen anzeigen |

## Beispiele

**Am Ende eine temporäre Datei löschen:**

```bash
tmp=$(mktemp)
trap 'rm -f "$tmp"; echo "cleaned up"' EXIT
echo "working in $tmp"
```

```text
working in /tmp/tmp.k3Jx9QfL2a
cleaned up
```

**Auf ++ctrl+c++ reagieren:**

```bash
trap 'echo "interrupted, stopping"; exit 130' INT
sleep 60
```

```text
^Cinterrupted, stopping
```

**Einen Dienst neu starten, auch wenn das Skript scheitert:**

```bash
systemctl stop php8.4-fpm
trap 'systemctl start php8.4-fpm' EXIT
/usr/local/bin/migrate.sh
```

```text
migrate.sh: column "email" already exists
```

Die Migration ist gescheitert, aber die Falle startet PHP-FPM wieder, und der Shop läuft
weiter.

## Wann brauche ich das?

- Um temporäre Dateien zu löschen, egal wie das Skript endet
- Um Sperren freizugeben oder einen Dienst neu zu starten, den das Skript gestoppt hat
- Um Fehler mit Zeilennummer zu melden

!!! tip "`EXIT` reicht zum Aufräumen"
    Eine Falle auf `EXIT` läuft auch nach Fehlern mit `set -e` und nach `exit`. Eine Falle deckt
    alle Wege ab, auf denen das Skript enden kann.

!!! tip "Die Zeile eines Fehlers finden"
    `trap 'echo "Fehler in Zeile $LINENO" >&2' ERR` meldet, wo ein Skript gescheitert ist.

## Verwandte Befehle

[set](set.md) · [exit](exit.md) · [kill](../08-processes/kill.md) · [flock](../16-scheduling/flock.md)
