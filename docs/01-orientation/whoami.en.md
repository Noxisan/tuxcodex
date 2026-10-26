# whoami

> Shows the name of the user you are currently working as (the effective user).

## Syntax

```bash
whoami [OPTION]
```

## Options

`whoami` has no options of its own. It does exactly one thing.

| Option      | Description                          |
|-------------|--------------------------------------|
| `--help`    | Show the help text and exit          |
| `--version` | Show version information and exit    |

## Examples

**Check your own user name:**

```bash
whoami
```

```text
nox
```

**Check which user a command runs as with `sudo`:**

```bash
sudo whoami
```

```text
root
```

**Check where you ended up after switching users:**

```bash
sudo -i
whoami
```

```text
root
```

**Make a script refuse to run as root:**

```bash
if [ "$(whoami)" = "root" ]; then
    echo "Please do not run this script as root." >&2
    exit 1
fi
```

```text
Please do not run this script as root.
```

![whoami output](../assets/screenshots/01-orientation/whoami.png)

## When do I need it?

- After `su`, `sudo -i` or `sudo -u <user> -s`, to make sure you are working as the user you think you are
- Before running something destructive (`rm -rf`, `chown -R`, `systemctl stop`): one quick `whoami` prevents surprises
- In scripts that must, or must not, run as a certain user
- When you have several SSH sessions open and lose track of which one is which

!!! tip "Good to know"
    `whoami` shows the **effective** user, which is why `sudo whoami` prints `root`.
    It is the same as `id -un`.

!!! warning "`whoami` is not `who am i`"
    `who am i` (with spaces) is a different command: it shows the user who **logged in**
    to the current terminal, including login time and origin. After `sudo -i`, `whoami`
    prints `root`, while `who am i` still shows `nox`.

## Related commands

[id](id.md) · [hostname](hostname.md) · [who](who.md)
