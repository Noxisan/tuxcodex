# realpath

> Shows the full, absolute path of a file or directory, with all symbolic links and `..` resolved.

![realpath output](../assets/screenshots/02-navigation/realpath.png)

## Syntax

```bash
realpath [OPTION]... FILE...
```

## Options

| Option | Description |
|--------|-------------|
| `-e`, `--canonicalize-existing` | All parts of the path must exist, otherwise print an error |
| `-m`, `--canonicalize-missing` | No part of the path needs to exist |
| `-s`, `--no-symlinks` | Do not resolve symbolic links, only clean up `.` and `..` |
| `--relative-to=DIR` | Print the path relative to `DIR` |
| `-q`, `--quiet` | Do not print error messages |

## Examples

**Show the absolute path of a file:**

```bash
realpath notes.txt
```

```text
/home/nox/notes.txt
```

**Find out where a symbolic link really points to:**

```bash
realpath /bin/sh
```

```text
/usr/bin/dash
```

On Debian, `/bin` is a link to `/usr/bin`, and `sh` is a link to `dash`. `realpath`
follows the whole chain.

**Clean up a path with `..`:**

```bash
realpath ../../etc/ssh
```

```text
/etc/ssh
```

**Make sure that a path exists:**

```bash
realpath -e missing.txt
```

```text
realpath: missing.txt: No such file or directory
```

Without `-e`, `realpath` would print `/home/nox/missing.txt`, because by default only
the directory has to exist.

**Show a path relative to another directory:**

```bash
realpath --relative-to=/etc /etc/ssh/sshd_config
```

```text
ssh/sshd_config
```

## When do I need it?

- To find out which file a symbolic link really points to, for example in
  `/etc/nginx/sites-enabled` or `/etc/alternatives`
- To get absolute paths for configuration files, cron jobs or systemd units
- In scripts, to find the directory the script itself is located in

!!! tip "The script's own directory"
    This line gives a script the directory it is stored in, no matter from where it
    was started:

    ```bash
    SCRIPT_DIR="$(dirname "$(realpath "$0")")"
    ```

!!! tip "`readlink -f`"
    In older scripts, you often see `readlink -f` instead of `realpath`. On Linux,
    both give the same result.

## Related commands

[pwd](pwd.md) · [cd](cd.md)
