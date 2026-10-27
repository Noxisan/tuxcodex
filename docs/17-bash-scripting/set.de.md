# set

> Ändert, wie sich Bash verhält. In Skripten vor allem, um bei Fehlern abzubrechen, statt still weiterzumachen.

![set output](../assets/screenshots/17-bash-scripting/set.png)

## Syntax

```bash
set [-euxo OPTION]
```

Der übliche Anfang eines robusten Skripts ist `set -euo pipefail`.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-e` | Das Skript beenden, wenn ein Befehl scheitert |
| `-u` | Nicht gesetzte Variablen als Fehler behandeln |
| `-o pipefail` | Eine Pipe scheitert, wenn irgendein Teil scheitert, nicht nur der letzte |
| `-x` | Jeden Befehl vor dem Ausführen ausgeben (Debugging) |
| `+x` | Eine Option wieder abschalten, hier die Debug-Ausgabe |

## Beispiele

**Beim ersten Fehler abbrechen:**

```bash
set -e
cp /etc/nginx/nginx.conf /mnt/backup/
echo "not reached if cp fails"
```

```text
cp: cannot create regular file '/mnt/backup/nginx.conf': No space left on device
```

**Einen Tippfehler in einer Variable erwischen:**

```bash
set -u
target=/mnt/backup
rm -rf "$targte/old"
```

```text
bash: targte: unbound variable
```

Ohne `set -u` würde aus `"$targte/old"` einfach `/old`, und `rm -rf` würde es löschen.

**Fehler in der Mitte einer Pipe:**

```bash
set -o pipefail
false | sort
echo "exit code: $?"
```

```text
exit code: 1
```

**Zeigen, was das Skript tut:**

```bash
set -x
name=web01
echo "host $name"
```

```text
+ name=web01
+ echo 'host web01'
host web01
```

## Wann brauche ich das?

- Am Anfang jedes Skripts, damit Fehler nicht unbemerkt bleiben
- Um mit `set -x` herauszufinden, wo ein Skript falsch abbiegt
- Um mit `set -u` Tippfehler in Variablennamen zu erwischen

!!! tip "Einen einzelnen Teil untersuchen"
    Setze `set -x` vor und `set +x` nach den Teil, den du untersuchen willst. Oder starte das
    ganze Skript mit `bash -x skript.sh`.

!!! warning "`-e` hat Ausnahmen"
    `set -e` bricht nicht in Bedingungen ab (`if`, `&&`, `||`) und nicht bei Befehlen, deren
    Scheitern dort erwartet wird. Das ist gewollt, heißt aber: Wichtige Schritte musst du
    trotzdem prüfen.

## Verwandte Befehle

[trap](trap.md) · [exit](exit.md) · [shellcheck](shellcheck.md)
