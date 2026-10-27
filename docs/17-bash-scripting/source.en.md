# source

> Runs a file in the current shell instead of a new one. Variables and functions from it stay available afterwards. `.` is the same command.

![source output](../assets/screenshots/17-bash-scripting/source.png)

## Syntax

```bash
source FILE [ARGUMENT]...
```

## Options

| Option | Description |
|--------|-------------|
| `source FILE` | Run the file in the current shell |
| `. FILE` | The same, portable to other shells |

## Examples

**Load a configuration file:**

```bash
cat app.env
source app.env
echo "$DB_HOST/$DB_NAME"
```

```text
DB_HOST=192.0.2.20
DB_NAME=shop
192.0.2.20/shop
```

**Reload `~/.bashrc` after a change:**

```bash
echo "alias ll='ls -lh'" >> ~/.bashrc
source ~/.bashrc
alias ll
```

```text
alias ll='ls -lh'
```

**A file that doesn't exist:**

```bash
source nosuch.env
```

```text
bash: nosuch.env: No such file or directory
```

## When do I need it?

- To load a configuration file with variables into a script
- To share functions between several scripts
- To apply changes to `~/.bashrc` without logging in again

!!! tip "Configuration in a separate file"
    Keep host names, paths and credentials in a file like `/etc/backup.conf` and load it with
    `source`. The script itself then stays the same on every server.

!!! danger "`source` runs everything"
    `source` executes the file as code. A configuration file that others can write to is a
    security hole: make it only writable by root.

## Related commands

[export](export.md) · [function](function.md)
