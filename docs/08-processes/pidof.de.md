# pidof

> Gibt die PIDs eines laufenden Programms aus, gefunden über seinen exakten Programmnamen.

![pidof output](../assets/screenshots/08-processes/pidof.png)

## Syntax

```bash
pidof [OPTION]... PROGRAMM...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-s` | Nur eine PID ausgeben |
| `-x` | Auch Skripte anhand ihres Namens finden |
| `-o PID` | Diese PID ignorieren |

## Beispiele

**Alle PIDs eines Programms finden:**

```bash
pidof nginx
```

```text
814 813 812
```

Alle PIDs stehen in einer Zeile, durch Leerzeichen getrennt.

**Nur eine PID holen:**

```bash
pidof -s nginx
```

```text
814
```

**Den Hauptprozess des SSH-Servers finden:**

```bash
pidof sshd
```

```text
640
```

**Ein Programm, das nicht läuft:**

```bash
pidof redis-server
echo $?
```

```text
1
```

**Ein laufendes Skript finden:**

```bash
pidof -x backup.sh
```

```text
4410
```

## Wann brauche ich das?

- In Skripten, die die PID eines Programms brauchen, etwa um ihm ein Signal zu senden
- Um schnell zu prüfen, ob ein Programm läuft (Exit-Status `0` oder `1`)

!!! tip "`pidof` oder `pgrep`?"
    `pidof` sucht nur nach dem exakten Programmnamen und gibt alle PIDs in einer Zeile aus.
    [`pgrep`](pgrep.md) kann auch nach Benutzer oder Kommandozeile suchen und gibt eine PID
    pro Zeile aus.

!!! warning "Der Name muss exakt passen"
    `pidof php-fpm` findet nichts, wenn das Programm `php-fpm8.4` heißt. Prüfe den genauen
    Namen vorher mit `ps -e` oder `pgrep -l`.

## Verwandte Befehle

[pgrep](pgrep.md) · [ps](ps.md) · [lsof](lsof.md) · [kill](kill.md)
