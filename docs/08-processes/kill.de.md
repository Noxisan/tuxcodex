# kill

> Sendet einem Prozess über seine PID ein Signal. Meist die Bitte, sich zu beenden, manchmal die Anweisung, seine Konfiguration neu zu laden.

![kill output](../assets/screenshots/08-processes/kill.png)

## Syntax

```bash
kill [-SIGNAL] PID...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Sendet `TERM`: Bitte beende dich sauber |
| `-HUP` | Konfiguration neu laden (bei vielen Diensten) |
| `-KILL`, `-9` | Sofort beenden, der Prozess kann nicht reagieren |
| `-STOP`, `-CONT` | Einen Prozess anhalten und fortsetzen |
| `-0` | Nichts senden, nur prüfen, ob der Prozess existiert |
| `-l` | Alle Signale auflisten |

## Beispiele

**Einen Prozess sauber beenden:**

```bash
kill 4410
ps -p 4410
```

```text
    PID TTY          TIME CMD
```

`ps` gibt nur noch die Kopfzeile aus: Der Prozess ist weg.

**Alle Signale anzeigen:**

```bash
kill -l
```

```text
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
```

Für den Alltag reichen die ersten Zeilen. Die Übersicht dieses Kapitels erklärt die
[wichtigsten Signale](index.md#prozesse-verstehen).

**Prüfen, ob ein Prozess noch läuft:**

```bash
kill -0 812 && echo "läuft"
```

```text
läuft
```

**Eine PID, die es nicht gibt:**

```bash
kill 99999
```

```text
bash: kill: (99999) - No such process
```

**Einen hängenden Prozess zwangsweise beenden:**

```bash
kill -9 4410
```

```text
[1]+  Killed                     ./backup.sh
```

Die Meldung erscheint, wenn der Prozess aus deiner Shell als Job gestartet wurde.

## Wann brauche ich das?

- Um einen Prozess zu beenden, den du mit [`ps`](ps.md) oder [`pgrep`](pgrep.md)
  gefunden hast
- Um einen Dienst mit `HUP` seine Konfiguration neu laden zu lassen
- In Skripten, um einen Hintergrundprozess zu beenden oder zu prüfen, ob er noch läuft

!!! tip "Erst `TERM`, dann `KILL`"
    Versuche immer zuerst ein einfaches `kill` und warte ein paar Sekunden. Nur wenn der
    Prozess dann noch da ist, nimm `kill -9`. Mit `TERM` kann er noch Daten speichern
    und Sperrdateien aufräumen.

!!! warning "Dienste gehören systemd"
    Für Prozesse, die systemd verwaltet, nimm `sudo systemctl stop` oder
    `sudo systemctl reload`. Beendest du sie mit `kill`, startet systemd sie
    womöglich sofort neu, oder der Dienst landet im Fehlerzustand.

!!! danger "Falsche PID"
    `kill` fragt nicht nach. Als root beendet eine vertippte PID jeden beliebigen
    Prozess, auch den SSH-Server oder die Datenbank. Prüfe die PID mit `ps -p PID`,
    bevor du `KILL` schickst.

## Verwandte Befehle

[ps](ps.md) · [pgrep](pgrep.md) · [pidof](pidof.md) · [top](top.md) · [pkill](pkill.md) · [timeout](timeout.md) · [jobs](jobs.md)
