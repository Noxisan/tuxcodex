# locate

> Finds files by name in a moment, using a database of all file names instead of searching the disk.

## Syntax

```bash
locate [OPTION]... PATTERN...
```

## Options

| Option | Description |
|--------|-------------|
| `-i`, `--ignore-case` | Ignore upper and lower case |
| `-b`, `--basename` | Only match the file name, not the directories in the path |
| `-c`, `--count` | Only print the number of matches |
| `-l`, `--limit N` | Stop after `N` matches |
| `-e`, `--existing` | Only show files that still exist right now |
| `-r`, `--regexp` | Treat the pattern as a regular expression |

The database is updated with `sudo updatedb`.

## Examples

**Find a file by name:**

```bash
locate backup.sh
```

```text
/home/nox/scripts/backup.sh
```

**Find all paths that contain a name:**

```bash
locate sshd_config
```

```text
/etc/ssh/sshd_config
/etc/ssh/sshd_config.d
/usr/share/man/man5/sshd_config.5.gz
/usr/share/openssh/sshd_config
/usr/share/openssh/sshd_config.md5sum
```

**Find only files with exactly this name:**

```bash
locate -b -r '^sshd_config$'
```

```text
/etc/ssh/sshd_config
/usr/share/openssh/sshd_config
```

**Search without regard to upper and lower case:**

```bash
locate -i NOTES
```

```text
/home/nox/notes.txt
```

**Count the matches:**

```bash
locate -c "*.conf"
```

```text
312
```

**Find a file that was just created:**

```bash
sudo updatedb
locate report.pdf
```

```text
/home/nox/report.pdf
```

![locate output](../assets/screenshots/02-navigation/locate.png)

## When do I need it?

- When you know a file name, but have no idea where it is on the system
- To find configuration files, man pages or example files of a package quickly
- When [`find /`](find.md) would take too long on a large file system

!!! tip "Only files you are allowed to see"
    `locate` only shows files in directories you have access to. Run it with `sudo` to
    also find files in protected places like `/root`.

!!! warning "The database is not always up to date"
    The database is updated once a day. Files created since then are missing, deleted
    files are still listed. Run `sudo updatedb` before searching for new files, or use
    `locate -e` to hide files that no longer exist.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| Package | `plocate` (not always installed) | `plocate` (not installed by default) |
| Database | created during installation | created by the first `sudo updatedb` |
| Daily update | timer active automatically | enable the timer yourself |

Install on Debian:

```bash
sudo apt install plocate
```

Enable the daily update on Arch:

```bash
sudo systemctl enable --now plocate-updatedb.timer
```

## Related commands

[find](find.md) · [whereis](whereis.md)
