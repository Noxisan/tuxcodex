# batch

> Runs a command as soon as the system load is low. Ideal for heavy jobs that should not slow down the server.

![batch output](../assets/screenshots/16-scheduling/batch.png)

## Syntax

```bash
batch
```

`batch` starts the job when the load average drops below 1.5 (adjustable with `atd -l`). It belongs to the package `at`.

## Options

| Option | Description |
|--------|-------------|
| *(stdin)* | The commands to run, like with `at` |
| `-f FILE` | Read the commands from a file |

## Examples

**Schedule a heavy job:**

```bash
echo /usr/local/bin/reindex.sh | batch
```

```text
warning: commands will be executed using /bin/sh
job 8 at Mon Oct 26 10:42:00 2026
```

**The job waits in queue `b`:**

```bash
atq
```

```text
8       Mon Oct 26 10:42:00 2026 b nox
```

The time is the time of scheduling. The job starts as soon as the load allows.

## When do I need it?

- For heavy jobs like reindexing a search or a large import, when the time doesn't matter
- On a busy server, so a job waits for a quiet moment instead of adding load
- Instead of `at now`, if the job may wait

!!! tip "Combine with `nice`"
    `echo "nice -n 19 /usr/local/bin/reindex.sh" | batch` waits for a quiet moment and then
    also runs with low priority, see [`nice`](../08-processes/nice.md).

## Related commands

[at](at.md) · [atq](atq.md) · [nice](../08-processes/nice.md) · [uptime](../01-orientation/uptime.md)
