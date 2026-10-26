# timeout

> Starts a command and ends it when it takes longer than the given time. Protects scripts and cron jobs from hanging forever.

![timeout output](../assets/screenshots/08-processes/timeout.png)

## Syntax

```bash
timeout [OPTION]... DURATION COMMAND [ARGUMENT]...
```

`DURATION` is a number with an optional unit: `s` seconds (default), `m` minutes, `h`
hours, `d` days.

## Options

| Option | Description |
|--------|-------------|
| `-s SIGNAL` | Signal to send when the time is up, default is `TERM` |
| `-k DURATION` | Send `KILL` if the command is still running `DURATION` after the first signal |
| `-v` | Report when the signal is sent |
| `--preserve-status` | Return the exit code of the command, even after a timeout |

## Examples

**Limit a script to 30 minutes:**

```bash
timeout 30m ./backup.sh; echo $?
```

```text
124
```

Exit code `124` means: the time was up and `timeout` ended the command.

**Report when the time is up:**

```bash
timeout -v 10 rsync -a /srv/ /mnt/backup/
```

```text
timeout: sending signal TERM to command ‘rsync’
```

**Send `KILL` if the command ignores `TERM`:**

```bash
timeout -k 10 60 ./backup.sh; echo $?
```

```text
137
```

After 60 seconds, `timeout` sends `TERM`. The script ignored it, so it got `KILL` 10
seconds later. `137` is 128 + 9, the number of `KILL`.

**Don't let a check hang in a script:**

```bash
timeout 5 ssh nox@192.0.2.20 uptime || echo "no answer"
```

```text
no answer
```

**When the command finishes in time:**

```bash
timeout 60 ls /srv; echo $?
```

```text
backup  www
0
```

The output and the exit code are those of the command itself.

## When do I need it?

- In cron jobs, so that a hanging backup doesn't block the next run
- In scripts that wait for the network, e.g. `ssh`, `curl` or a database check
- When testing, to stop a command reliably after a fixed time

!!! tip "Evaluate the exit code"
    `124` means timeout, `137` means it had to be ended with `KILL`. Any other value
    comes from the command itself. This lets your script decide what to do next.

!!! warning "Shell functions and builtins"
    `timeout` starts a new program. Shell functions, aliases and builtins like `cd` don't
    work with it. For several commands, use `timeout 60 bash -c '…'`.

## Related commands

[kill](kill.md) · [pkill](pkill.md) · [killall](killall.md)
