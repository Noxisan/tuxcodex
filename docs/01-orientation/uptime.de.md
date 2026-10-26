# uptime

> Zeigt, wie lange das System schon läuft, wie viele Benutzer angemeldet sind und wie hoch die Last ist.

## Syntax

```bash
uptime [OPTION]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-p`, `--pretty` | Nur die Laufzeit anzeigen, gut lesbar formatiert |
| `-s`, `--since` | Den Startzeitpunkt des Systems anzeigen (`yyyy-mm-dd HH:MM:SS`) |

## Beispiele

**Laufzeit mit Uhrzeit, Benutzern und Last anzeigen:**

```bash
uptime
```

```text
 10:42:17 up 12 days,  3:05,  2 users,  load average: 0.08, 0.03, 0.01
```

Die Ausgabe enthält: aktuelle Uhrzeit, Laufzeit, Anzahl der angemeldeten Benutzer und
die durchschnittliche Last der letzten 1, 5 und 15 Minuten.

**Laufzeit gut lesbar anzeigen:**

```bash
uptime -p
```

```text
up 1 week, 5 days, 3 hours, 5 minutes
```

**Anzeigen, wann das System gestartet wurde:**

```bash
uptime -s
```

```text
2026-10-14 07:37:05
```

**Die Last ins Verhältnis zur Anzahl der CPU-Kerne setzen:**

```bash
nproc
uptime
```

```text
4
 10:42:17 up 12 days,  3:05,  2 users,  load average: 3.92, 2.10, 1.05
```

Bei 4 Kernen bedeutet eine Last von `3.92`, dass die CPUs fast voll ausgelastet sind.
Außerdem steigt die Last seit 15 Minuten an (`1.05` → `2.10` → `3.92`).

<!-- SCREENSHOT: assets/screenshots/01-orientation/uptime.png -->

## Wann brauche ich das?

- Um zu prüfen, ob ein Server unerwartet neu gestartet ist (Absturz, Stromausfall,
  automatisches Update)
- Als erster schneller Check, wenn ein Server träge wirkt: Ist die Last hoch – und
  steigt oder fällt sie?
- Um zu bestätigen, dass ein geplanter Neustart wirklich stattgefunden hat
- In Monitoring-Skripten, die nur den Startzeitpunkt brauchen (`uptime -s`)

!!! tip "Den Load Average lesen"
    Der Load Average zählt Prozesse, die laufen oder auf CPU bzw. Festplatten-I/O
    warten. Als Faustregel gilt: Liegt die Last über der Anzahl der CPU-Kerne (`nproc`),
    staut sich Arbeit. Die drei Werte zeigen den Trend – ist der 1-Minuten-Wert höher
    als der 15-Minuten-Wert, steigt die Last.

!!! warning "Hohe Last heißt nicht immer CPU"
    Unter Linux zählen auch Prozesse zur Last, die auf Festplatte oder Netzwerkspeicher
    warten (Zustand `D`). Hohe Last bei untätiger CPU deutet oft auf langsamen Speicher hin.

## Verwandte Befehle

[uname](uname.md)
