# exit

> Beendet ein Skript mit einem Exit-Code: `0` bei Erfolg, alles andere bei einem Fehler. Aufrufer, cron und Monitoring werten diesen Code aus.

![exit output](../assets/screenshots/17-bash-scripting/exit.png)

## Syntax

```bash
exit [CODE]
```

Ohne `exit` endet ein Skript mit dem Exit-Code seines letzten Befehls.

## Optionen

| Code | Übliche Bedeutung |
|------|-------------------|
| `0` | Erfolg |
| `1` | Allgemeiner Fehler |
| `2` | Falsche Benutzung, z. B. fehlende Argumente |
| `126`, `127` | Befehl nicht ausführbar, Befehl nicht gefunden |
| `128 + N` | Durch Signal `N` beendet, z. B. `130` bei ++ctrl+c++ |
| `$?` | Exit-Code des letzten Befehls |

## Beispiele

**Eine Voraussetzung prüfen und abbrechen:**

```bash
if [[ $EUID -ne 0 ]]; then
    echo "please run as root" >&2
    exit 1
fi
```

```text
please run as root
```

**Den Exit-Code eines Skripts prüfen:**

```bash
./backup-www /nope; echo "exit code: $?"
```

```text
10:42:17 Source /nope does not exist
exit code: 1
```

**Ein Befehl, den es nicht gibt:**

```bash
backupp; echo $?
```

```text
bash: backupp: command not found
127
```

## Wann brauche ich das?

- Am Ende jeder Prüfung: Hat es geklappt oder nicht?
- Um ein Skript früh zu beenden, wenn eine Voraussetzung fehlt
- Damit cron, systemd und Monitoring fehlgeschlagene Läufe erkennen

!!! tip "Früh scheitern"
    Prüfe Voraussetzungen am Anfang und brich mit einer klaren Meldung und `exit 1` ab. Das ist
    leichter zu untersuchen als ein Fehler mittendrin.

!!! warning "`exit` in einer geladenen Datei"
    In einer mit `source` geladenen Datei schließt `exit` deine ganze Shell. Nimm dort `return`.

## Verwandte Befehle

[function](function.md) · [set](set.md) · [trap](trap.md) · [getopts](getopts.md)
