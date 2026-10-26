# nice

> Startet einen Befehl mit einer anderen Priorität. Ein hoher Nice-Wert heißt: Sei nett zu den anderen und lass sie vor.

![nice output](../assets/screenshots/08-processes/nice.png)

## Syntax

```bash
nice [-n WERT] BEFEHL [ARGUMENT]...
```

Der Nice-Wert reicht von `-20` (höchste Priorität) bis `19` (niedrigste). Normal ist `0`.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(kein Befehl)* | Den aktuellen Nice-Wert anzeigen |
| `-n WERT` | `WERT` zum aktuellen Nice-Wert addieren, Standard ist `10` |

Nur root darf negative Werte verwenden, also die Priorität erhöhen.

## Beispiele

**Den aktuellen Nice-Wert anzeigen:**

```bash
nice
```

```text
0
```

**Ein Backup mit niedriger Priorität starten:**

```bash
nice -n 15 tar -czf /mnt/backup/www.tar.gz /srv/www &
```

```text
[1] 4520
```

**Den Nice-Wert eines Prozesses prüfen:**

```bash
ps -o pid,ni,comm -p 4520
```

```text
    PID  NI COMMAND
   4520  15 tar
```

Die Spalte `NI` zeigt den Nice-Wert. [`top`](top.md) und [`htop`](htop.md) zeigen ihn
ebenfalls.

**Ohne Root-Rechte versuchen, die Priorität zu erhöhen:**

```bash
nice -n -5 ./import.sh
```

```text
nice: cannot set niceness: Permission denied
```

Das Skript läuft trotzdem, aber mit dem normalen Wert `0`. Mit `sudo` bekäme es `-5`.

## Wann brauche ich das?

- Für Backups, Komprimierung oder Builds, die Webserver oder Datenbank nicht ausbremsen
  dürfen
- Für einmalige Berichte oder Exporte auf einem Produktivserver
- In Cronjobs, die tagsüber laufen

!!! tip "Auch Plattenzugriffe bremsen"
    `nice` wirkt nur auf die CPU-Zeit. Für Jobs, die vor allem viel lesen und schreiben,
    kombiniere es mit `ionice`: `nice -n 19 ionice -c 3 tar …` bekommt Plattenzugriff nur,
    wenn sonst niemand ihn braucht.

!!! warning "Wenig Wirkung auf ruhigen Servern"
    Der Nice-Wert zählt nur, wenn Prozesse um die CPU konkurrieren. Ist die CPU meist
    untätig, ist ein Job mit hohem Nice-Wert nicht langsamer.

## Verwandte Befehle

[ps](ps.md) · [top](top.md) · [timeout](timeout.md) · [renice](renice.md)
