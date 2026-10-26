# pkill

> Sends a signal to all processes whose name matches a pattern. Like `kill`, but without looking up the PID first.

![pkill output](../assets/screenshots/08-processes/pkill.png)

## Syntax

```bash
pkill [-SIGNAL] [OPTION]... PATTERN
```

## Options

| Option | Description |
|--------|-------------|
| `-SIGNAL` | Signal to send, default is `TERM` |
| `-e` | Print every process that was signalled |
| `-f` | Match the pattern against the whole command line |
| `-x` | The name must match exactly |
| `-o`, `-n` | Only the oldest or newest matching process |
| `-u USER` | Only processes of this user |
| `-t TERMINAL` | Only processes on this terminal, e.g. `pts/1` |

## Examples

**End all processes of a script and show what happened:**

```bash
pkill -e backup.sh
```

```text
backup.sh killed (pid 4410)
```

**Match the full command line:**

```bash
pkill -e -f "rsync .*/mnt/backup"
```

```text
rsync killed (pid 4415)
```

The process name is only `rsync`. With `-f`, the arguments are searched as well.

**End all processes of a user:**

```bash
sudo pkill -e -u alice
```

```text
sshd-session killed (pid 3118)
bash killed (pid 3120)
```

The SSH session of `alice` is closed as well.

**Make a service reload its configuration:**

```bash
sudo pkill -e -HUP -o -x nginx
```

```text
nginx killed (pid 812)
```

`-o` picks the oldest matching process, here the nginx master. `killed` only means that
the signal was sent: with `HUP`, nginx keeps running and reloads its configuration.

**Nothing found:**

```bash
pkill nosuchprocess; echo $?
```

```text
1
```

Exit code `1` means: no process matched.

## When do I need it?

- To end all processes of a program at once, e.g. hanging workers
- To end all processes of a user whose account you locked
- In scripts, to end a helper by name

!!! tip "Test with `pgrep` first"
    `pkill` takes the same options as [`pgrep`](pgrep.md). Run `pgrep -a` with the same
    pattern first and check the list. Only then replace `pgrep -a` with `pkill`.

!!! warning "`-f` also finds your own shell"
    With `-f`, the pattern is also found in command lines that only contain it as text,
    for example a `bash -c "…"` or an `ssh` call with that command. Without a check, you
    end processes you didn't mean.

!!! danger "Short patterns as root"
    `pkill` matches parts of names: `sudo pkill ss` also ends `sshd`, and you lose your
    connection. Use `-x` for exact names.

## Related commands

[pgrep](pgrep.md) · [kill](kill.md) · [ps](ps.md) · [killall](killall.md)
