# kill

> Sends a signal to a process by its PID. Usually the request to end itself, sometimes the order to reload its configuration.

![kill output](../assets/screenshots/08-processes/kill.png)

## Syntax

```bash
kill [-SIGNAL] PID...
```

## Options

| Option | Description |
|--------|-------------|
| *(none)* | Sends `TERM`: please end yourself cleanly |
| `-HUP` | Reload the configuration (for many services) |
| `-KILL`, `-9` | End immediately, the process can't react |
| `-STOP`, `-CONT` | Pause and continue a process |
| `-0` | Send nothing, only check whether the process exists |
| `-l` | List all signals |

## Examples

**End a process cleanly:**

```bash
kill 4410
ps -p 4410
```

```text
    PID TTY          TIME CMD
```

`ps` only prints its header: the process is gone.

**Show all signals:**

```bash
kill -l
```

```text
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
```

The first lines are enough for everyday use. The overview of this chapter explains the
[most important signals](index.md#understanding-processes).

**Check whether a process is still running:**

```bash
kill -0 812 && echo "running"
```

```text
running
```

**A PID that doesn't exist:**

```bash
kill 99999
```

```text
bash: kill: (99999) - No such process
```

**Force a hanging process to end:**

```bash
kill -9 4410
```

```text
[1]+  Killed                     ./backup.sh
```

The message appears when the process was started from your shell as a job.

## When do I need it?

- To end a process that you found with [`ps`](ps.md) or [`pgrep`](pgrep.md)
- To make a service reload its configuration with `HUP`
- In scripts, to end a background process or check whether it is still running

!!! tip "First `TERM`, then `KILL`"
    Always try plain `kill` first and wait a few seconds. Only use `kill -9` if the
    process is still there. With `TERM`, it can save data and remove lock files.

!!! warning "Services belong to systemd"
    For processes that systemd manages, use `sudo systemctl stop` or
    `sudo systemctl reload`. If you end them with `kill`, systemd may restart them
    right away, or the service ends up in a failed state.

!!! danger "Wrong PID"
    `kill` doesn't ask. As root, a mistyped PID ends any process, also the SSH server or
    the database. Check the PID with `ps -p PID` before you send `KILL`.

## Related commands

[ps](ps.md) · [pgrep](pgrep.md) · [pidof](pidof.md) · [top](top.md) · [pkill](pkill.md) · [timeout](timeout.md)
