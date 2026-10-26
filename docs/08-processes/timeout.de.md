# timeout

> Startet einen Befehl und beendet ihn, wenn er länger als die angegebene Zeit braucht. Schützt Skripte und Cronjobs davor, ewig zu hängen.

![timeout output](../assets/screenshots/08-processes/timeout.png)

## Syntax

```bash
timeout [OPTION]... DAUER BEFEHL [ARGUMENT]...
```

`DAUER` ist eine Zahl mit optionaler Einheit: `s` Sekunden (Standard), `m` Minuten, `h`
Stunden, `d` Tage.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-s SIGNAL` | Signal, das nach Ablauf der Zeit gesendet wird, Standard ist `TERM` |
| `-k DAUER` | `KILL` senden, wenn der Befehl `DAUER` nach dem ersten Signal noch läuft |
| `-v` | Melden, wenn das Signal gesendet wird |
| `--preserve-status` | Den Exit-Code des Befehls zurückgeben, auch nach einem Timeout |

## Beispiele

**Ein Skript auf 30 Minuten begrenzen:**

```bash
timeout 30m ./backup.sh; echo $?
```

```text
124
```

Exit-Code `124` bedeutet: Die Zeit war abgelaufen, und `timeout` hat den Befehl beendet.

**Melden, wenn die Zeit abgelaufen ist:**

```bash
timeout -v 10 rsync -a /srv/ /mnt/backup/
```

```text
timeout: sending signal TERM to command ‘rsync’
```

**`KILL` senden, wenn der Befehl `TERM` ignoriert:**

```bash
timeout -k 10 60 ./backup.sh; echo $?
```

```text
137
```

Nach 60 Sekunden sendet `timeout` ein `TERM`. Das Skript hat es ignoriert und deshalb
10 Sekunden später `KILL` bekommen. `137` ist 128 + 9, die Nummer von `KILL`.

**Eine Prüfung im Skript nicht hängen lassen:**

```bash
timeout 5 ssh nox@192.0.2.20 uptime || echo "keine Antwort"
```

```text
keine Antwort
```

**Wenn der Befehl rechtzeitig fertig ist:**

```bash
timeout 60 ls /srv; echo $?
```

```text
backup  www
0
```

Ausgabe und Exit-Code sind die des Befehls selbst.

## Wann brauche ich das?

- In Cronjobs, damit ein hängendes Backup nicht den nächsten Lauf blockiert
- In Skripten, die auf das Netzwerk warten, z. B. `ssh`, `curl` oder eine Datenbankprüfung
- Beim Testen, um einen Befehl zuverlässig nach einer festen Zeit zu stoppen

!!! tip "Den Exit-Code auswerten"
    `124` heißt Timeout, `137` heißt, er musste mit `KILL` beendet werden. Jeder andere
    Wert kommt vom Befehl selbst. So kann dein Skript entscheiden, wie es weitergeht.

!!! warning "Shell-Funktionen und Builtins"
    `timeout` startet ein neues Programm. Shell-Funktionen, Aliase und Builtins wie `cd`
    funktionieren damit nicht. Für mehrere Befehle nimm `timeout 60 bash -c '…'`.

## Verwandte Befehle

[kill](kill.md) · [pkill](pkill.md) · [killall](killall.md) · [nice](nice.md) · [watch](watch.md)
