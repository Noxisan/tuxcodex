# nice

> Starts a command with a different priority. A high nice value means: be nice to the others and let them go first.

![nice output](../assets/screenshots/08-processes/nice.png)

## Syntax

```bash
nice [-n VALUE] COMMAND [ARGUMENT]...
```

The nice value ranges from `-20` (highest priority) to `19` (lowest). Normal is `0`.

## Options

| Option | Description |
|--------|-------------|
| *(no command)* | Show the current nice value |
| `-n VALUE` | Add `VALUE` to the current nice value, default is `10` |

Only root may use negative values, that is, raise the priority.

## Examples

**Show the current nice value:**

```bash
nice
```

```text
0
```

**Start a backup with low priority:**

```bash
nice -n 15 tar -czf /mnt/backup/www.tar.gz /srv/www &
```

```text
[1] 4520
```

**Check the nice value of a process:**

```bash
ps -o pid,ni,comm -p 4520
```

```text
    PID  NI COMMAND
   4520  15 tar
```

The column `NI` shows the nice value. [`top`](top.md) and [`htop`](htop.md) show it as
well.

**Try to raise the priority without root rights:**

```bash
nice -n -5 ./import.sh
```

```text
nice: cannot set niceness: Permission denied
```

The script still runs, but with the normal value `0`. With `sudo`, it would get `-5`.

## When do I need it?

- For backups, compression or builds that must not slow down the web server or database
- For one-off reports or exports on a production server
- In cron jobs that run during the day

!!! tip "Also slow down disk access"
    `nice` only affects CPU time. For jobs that mainly read and write a lot, combine it
    with `ionice`: `nice -n 19 ionice -c 3 tar …` gives disk access only when nobody
    else needs it.

!!! warning "Little effect on idle servers"
    The nice value only matters when processes compete for the CPU. If the CPU is mostly
    idle, a niced job is not slower.

## Related commands

[ps](ps.md) · [top](top.md) · [timeout](timeout.md) · [renice](renice.md)
