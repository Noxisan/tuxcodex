# renice

> Changes the priority of a process that is already running.

![renice output](../assets/screenshots/08-processes/renice.png)

## Syntax

```bash
renice -n VALUE [-p PID... | -u USER... | -g PGID...]
```

`VALUE` is the new nice value, from `-20` (highest priority) to `19` (lowest). See
[`nice`](nice.md).

## Options

| Option | Description |
|--------|-------------|
| `-n VALUE` | New nice value |
| `-p PID` | The process with this PID (default) |
| `-u USER` | All processes of this user |
| `-g PGID` | All processes of this process group |

Without root rights, you can only lower the priority of your own processes, not raise it.

## Examples

**Slow down a running backup:**

```bash
renice -n 19 -p 4520
```

```text
4520 (process ID) old priority 15, new priority 19
```

**Slow down all processes of a user:**

```bash
sudo renice -n 10 -u alice
```

```text
1001 (user ID) old priority 0, new priority 10
```

`1001` is the user ID of `alice`. All of their processes now have the nice value `10`.

**Raise the priority again:**

```bash
sudo renice -n 0 -p 4520
```

```text
4520 (process ID) old priority 19, new priority 0
```

**Try it without root rights:**

```bash
renice -n 0 -p 4520
```

```text
renice: failed to set priority for 4520 (process ID): Permission denied
```

Going back from `19` to `0` would raise the priority. Only root is allowed to do that.

## When do I need it?

- When a job that is already running slows down the server
- To give a user with heavy jobs a lower priority on a shared server
- To give an important process more CPU time in an emergency

!!! tip "Find the PID first"
    Find the process with [`pgrep`](pgrep.md) or [`top`](top.md). In `top`, you can also
    press ++r++ and enter the PID and the new value directly.

!!! warning "There is no way back without root"
    Once you have raised the nice value of your own process, you can't lower it again
    without `sudo`. Choose the value carefully.

## Related commands

[nice](nice.md) · [ps](ps.md) · [top](top.md) · [pgrep](pgrep.md)
