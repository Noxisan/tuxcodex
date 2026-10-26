# locate

> Finds files by name in a moment, using a database of all file names instead of searching the disk.

![locate output](../assets/screenshots/02-navigation/locate.png)

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

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `plocate` | `plocate` | `mlocate` (RHEL 9), `plocate` (RHEL 10) | `plocate` |
| Installed by default | not always | not always | not always | no |
| Daily update | automatic | automatic | automatic | enable the timer yourself |
| Install | `sudo apt install plocate` | `sudo apt install plocate` | `sudo dnf install plocate` | `sudo pacman -S plocate` |

Enable the daily update on Arch:

```bash
sudo systemctl enable --now plocate-updatedb.timer
```

## Related commands

[find](find.md) · [whereis](whereis.md)
