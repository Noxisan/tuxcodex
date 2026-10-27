# batch

> Führt einen Befehl aus, sobald die Systemlast niedrig ist. Ideal für schwere Jobs, die den Server nicht ausbremsen sollen.

![batch output](../assets/screenshots/16-scheduling/batch.png)

## Syntax

```bash
batch
```

`batch` startet den Job, wenn der Load Average unter 1,5 fällt (einstellbar mit `atd -l`). Es gehört zum Paket `at`.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(stdin)* | Die auszuführenden Befehle, wie bei `at` |
| `-f DATEI` | Die Befehle aus einer Datei lesen |

## Beispiele

**Einen schweren Job einplanen:**

```bash
echo /usr/local/bin/reindex.sh | batch
```

```text
warning: commands will be executed using /bin/sh
job 8 at Mon Oct 26 10:42:00 2026
```

**Der Job wartet in Warteschlange `b`:**

```bash
atq
```

```text
8       Mon Oct 26 10:42:00 2026 b nox
```

Die Zeit ist der Zeitpunkt des Einplanens. Der Job startet, sobald die Last es zulässt.

## Wann brauche ich das?

- Für schwere Jobs wie das Neuindizieren einer Suche oder einen großen Import, wenn die Uhrzeit egal ist
- Auf einem ausgelasteten Server, damit ein Job auf einen ruhigen Moment wartet, statt Last hinzuzufügen
- Statt `at now`, wenn der Job warten darf

!!! tip "Mit `nice` kombinieren"
    `echo "nice -n 19 /usr/local/bin/reindex.sh" | batch` wartet auf einen ruhigen Moment und
    läuft dann zusätzlich mit niedriger Priorität, siehe [`nice`](../08-processes/nice.md).

## Verwandte Befehle

[at](at.md) · [atq](atq.md) · [nice](../08-processes/nice.md) · [uptime](../01-orientation/uptime.md)
