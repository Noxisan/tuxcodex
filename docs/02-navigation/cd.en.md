# cd

> Changes the current directory.

## Syntax

```bash
cd [OPTION] [DIRECTORY]
```

## Options

| Option / argument | Description |
|-------------------|-------------|
| *(none)* or `~` | Go to your home directory |
| `-` | Go back to the previous directory and print its path |
| `..` | Go one level up |
| `~USER` | Go to the home directory of `USER` |
| `-L` | Follow symbolic links logically (default) |
| `-P` | Resolve symbolic links and go to the physical directory |

## Examples

**Change to an absolute path:**

```bash
cd /etc/ssh
pwd
```

```text
/etc/ssh
```

**Go one level up:**

```bash
cd ..
pwd
```

```text
/etc
```

**Jump back to the previous directory:**

```bash
cd /var/log
cd -
```

```text
/etc
```

**Go back to your home directory:**

```bash
cd
pwd
```

```text
/home/nox
```

**Go to the home directory of another user:**

```bash
cd ~www-data
pwd
```

```text
/var/www
```

**Try to enter a directory without permission:**

```bash
cd /root
```

```text
-bash: cd: /root: Permission denied
```

![cd output](../assets/screenshots/02-navigation/cd.png)

## When do I need it?

- All the time: to get to configuration files (`/etc`), logs (`/var/log`) or web content
  (`/var/www`)
- To switch quickly between two directories with `cd -`, for example between a config
  directory and its log directory
- In scripts, to work in a fixed directory before running further commands

!!! tip "Use Tab completion"
    Type the first letters of a directory and press ++tab++. Bash completes the name, and
    pressing ++tab++ twice shows all matches. This saves typing and avoids typos.

!!! tip "Help for `cd`"
    `cd` is built into the shell, so there is no `man cd`. Use `help cd` instead.

!!! danger "`cd` in scripts: always check the result"
    If `cd` fails, the script keeps running in the **old** directory. Combined with `rm`,
    this can delete the wrong files. Always stop the script if `cd` fails:

    ```bash
    cd /var/www/example.com/cache || exit 1
    rm -rf ./*
    ```

## Related commands

[pwd](pwd.md) · [ls](ls.md)
