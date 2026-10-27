# atrm

> Entfernt wartende Jobs aus der Warteschlange von `at`, bevor sie laufen.

![atrm output](../assets/screenshots/16-scheduling/atrm.png)

## Syntax

```bash
atrm JOB...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `JOB` | Die Jobnummer aus `atq`; mehrere Nummern sind möglich |

## Beispiele

**Einen Job entfernen und die Warteschlange prüfen:**

```bash
sudo atrm 6
sudo atq
```

```text
5       Mon Oct 26 22:00:00 2026 a nox
7       Tue Oct 27 09:00:00 2026 a nox
```

**Eine Jobnummer, die es nicht gibt:**

```bash
atrm 9
```

```text
Cannot find jobid 9
```

**Den Sicherheitsjob nach einer erfolgreichen Firewall-Änderung entfernen:**

```bash
sudo atq
sudo atrm 8
```

```text
8       Mon Oct 26 10:47:00 2026 a root
```

## Wann brauche ich das?

- Wenn ein eingeplanter Job nicht mehr gebraucht wird
- Nach einer erfolgreichen Änderung, um den Sicherheitsjob zu entfernen, der sie zurücknehmen würde
- Wenn ein Job für die falsche Zeit eingeplant wurde

!!! tip "Danach prüfen"
    `atrm` gibt bei Erfolg nichts aus. Prüfe mit `atq`, ob der Job weg ist.

## Verwandte Befehle

[at](at.md) · [atq](atq.md)
