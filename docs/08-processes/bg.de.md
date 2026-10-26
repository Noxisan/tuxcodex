# bg

> Lässt einen angehaltenen Job im Hintergrund weiterlaufen, damit die Shell wieder frei ist.

![bg output](../assets/screenshots/08-processes/bg.png)

## Syntax

```bash
bg [%JOB]...
```

Ohne Job nimmt `bg` den aktuellen Job (`+` bei [`jobs`](jobs.md)).

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `%NUMMER` | Der Job mit dieser Nummer, z. B. `%2` |
| `%TEXT` | Der Job, dessen Befehl mit `TEXT` beginnt, z. B. `%tar` |

## Beispiele

**Einen Befehl anhalten, der länger dauert als gedacht:**

```bash
tar -czf /mnt/backup/www.tar.gz /srv/www
```

```text
^Z
[1]+  Stopped                    tar -czf /mnt/backup/www.tar.gz /srv/www
```

Drücke ++ctrl+z++, während der Befehl läuft. Er wird angehalten, und du bekommst deinen
Prompt zurück.

**Im Hintergrund weiterlaufen lassen:**

```bash
bg
```

```text
[1]+ tar -czf /mnt/backup/www.tar.gz /srv/www &
```

Das `&` am Ende zeigt: Der Job läuft jetzt im Hintergrund.

**Einen bestimmten Job fortsetzen:**

```bash
bg %tar
```

```text
[1]+ tar -czf /mnt/backup/www.tar.gz /srv/www &
```

**Kein angehaltener Job:**

```bash
bg
```

```text
bash: bg: current: no such job
```

## Wann brauche ich das?

- Wenn du einen langen Befehl ohne `&` gestartet hast und deine Shell zurückwillst
- Um einen Job fortzusetzen, den du mit ++ctrl+z++ angehalten hast

!!! tip "Die Ausgabe landet weiter im Terminal"
    Ein Hintergrundjob schreibt weiter in dein Terminal und kann sich mit deiner Eingabe
    mischen. Leite bei langen Jobs die Ausgabe schon beim Start um:
    `tar … > /tmp/tar.log 2>&1 &`.

!!! warning "Nichts für interaktive Programme"
    Programme, die auf eine Eingabe warten, wie `vim` oder eine Passwortabfrage, halten
    im Hintergrund sofort wieder an. Hol sie mit [`fg`](fg.md) in den Vordergrund zurück.

## Verwandte Befehle

[jobs](jobs.md) · [kill](kill.md) · [fg](fg.md)
