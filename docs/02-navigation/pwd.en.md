# pwd

> Shows the full path of the directory you are currently in.

## Syntax

```bash
pwd [OPTION]
```

## Options

| Option | Description |
|--------|-------------|
| `-L` | Show the logical path, including symbolic links (default) |
| `-P` | Show the physical path, with all symbolic links resolved |

## Examples

**Show the current directory:**

```bash
pwd
```

```text
/home/nox
```

**Check where you are after changing directory:**

```bash
cd /etc/ssh
pwd
```

```text
/etc/ssh
```

**Show the real path behind a symbolic link:**

```bash
cd /var/run
pwd
pwd -P
```

```text
/var/run
/run
```

On Debian, `/var/run` is only a link to `/run`. `pwd` shows the path you used,
`pwd -P` shows where you really are.

**Use the current directory in a command:**

```bash
echo "Backup of $(pwd)"
```

```text
Backup of /home/nox
```

![pwd output](../assets/screenshots/02-navigation/pwd.png)

## When do I need it?

- When the prompt only shows a shortened path, or no path at all
- Before running commands with relative paths like `rm *.log`, to be sure you are in
  the right directory
- In scripts, to remember the starting directory or to build absolute paths
- To find out the real location when symbolic links are involved (`pwd -P`)

!!! tip "Good to know"
    The shell always stores the current directory in the variable `$PWD`. `echo "$PWD"`
    prints the same as `pwd`. The previous directory is stored in `$OLDPWD`.

!!! warning "Check before you delete"
    Before `rm`, `chmod -R` or `chown -R` with relative paths, run `pwd` once.
    The same command in the wrong directory can do a lot of damage.

## Related commands

[whoami](../01-orientation/whoami.md) · [cd](cd.md)
