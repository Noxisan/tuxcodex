# pidof

> Prints the PIDs of a running program, found by its exact program name.

![pidof output](../assets/screenshots/08-processes/pidof.png)

## Syntax

```bash
pidof [OPTION]... PROGRAM...
```

## Options

| Option | Description |
|--------|-------------|
| `-s` | Only print one PID |
| `-x` | Also find scripts by their name |
| `-o PID` | Ignore this PID |

## Examples

**Find all PIDs of a program:**

```bash
pidof nginx
```

```text
814 813 812
```

All PIDs are printed in one line, separated by spaces.

**Get only one PID:**

```bash
pidof -s nginx
```

```text
814
```

**Find the main SSH server process:**

```bash
pidof sshd
```

```text
640
```

**A program that is not running:**

```bash
pidof redis-server
echo $?
```

```text
1
```

**Find a running script:**

```bash
pidof -x backup.sh
```

```text
4410
```

## When do I need it?

- In scripts that need the PID of a program, for example to send it a signal
- To check quickly whether a program is running (exit status `0` or `1`)

!!! tip "`pidof` or `pgrep`?"
    `pidof` only looks for the exact program name and prints all PIDs in one line.
    [`pgrep`](pgrep.md) can also search by user or command line and prints one PID per
    line.

!!! warning "The name must match exactly"
    `pidof php-fpm` finds nothing if the program is called `php-fpm8.4`. Check the exact
    name with `ps -e` or `pgrep -l` first.

## Related commands

[pgrep](pgrep.md) · [ps](ps.md) · [lsof](lsof.md)
