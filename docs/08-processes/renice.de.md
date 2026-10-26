# renice

> Ändert die Priorität eines Prozesses, der bereits läuft.

![renice output](../assets/screenshots/08-processes/renice.png)

## Syntax

```bash
renice -n WERT [-p PID... | -u BENUTZER... | -g PGID...]
```

`WERT` ist der neue Nice-Wert, von `-20` (höchste Priorität) bis `19` (niedrigste). Siehe
[`nice`](nice.md).

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n WERT` | Neuer Nice-Wert |
| `-p PID` | Der Prozess mit dieser PID (Standard) |
| `-u BENUTZER` | Alle Prozesse dieses Benutzers |
| `-g PGID` | Alle Prozesse dieser Prozessgruppe |

Ohne Root-Rechte kannst du die Priorität deiner eigenen Prozesse nur senken, nicht erhöhen.

## Beispiele

**Ein laufendes Backup ausbremsen:**

```bash
renice -n 19 -p 4520
```

```text
4520 (process ID) old priority 15, new priority 19
```

**Alle Prozesse eines Benutzers ausbremsen:**

```bash
sudo renice -n 10 -u alice
```

```text
1001 (user ID) old priority 0, new priority 10
```

`1001` ist die Benutzer-ID von `alice`. Alle ihre Prozesse haben jetzt den Nice-Wert `10`.

**Die Priorität wieder erhöhen:**

```bash
sudo renice -n 0 -p 4520
```

```text
4520 (process ID) old priority 19, new priority 0
```

**Ohne Root-Rechte versuchen:**

```bash
renice -n 0 -p 4520
```

```text
renice: failed to set priority for 4520 (process ID): Permission denied
```

Von `19` zurück auf `0` hieße, die Priorität zu erhöhen. Das darf nur root.

## Wann brauche ich das?

- Wenn ein bereits laufender Job den Server ausbremst
- Um auf einem gemeinsam genutzten Server einem Benutzer mit schweren Jobs eine niedrigere
  Priorität zu geben
- Um einem wichtigen Prozess im Notfall mehr CPU-Zeit zu geben

!!! tip "Erst die PID finden"
    Den Prozess findest du mit [`pgrep`](pgrep.md) oder [`top`](top.md). In `top` kannst
    du auch ++r++ drücken und PID und neuen Wert direkt eingeben.

!!! warning "Ohne root gibt es keinen Weg zurück"
    Hast du den Nice-Wert deines eigenen Prozesses einmal erhöht, kannst du ihn ohne
    `sudo` nicht wieder senken. Wähle den Wert mit Bedacht.

## Verwandte Befehle

[nice](nice.md) · [ps](ps.md) · [top](top.md) · [pgrep](pgrep.md)
