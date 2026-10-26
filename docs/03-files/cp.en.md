# cp

> Copies files and directories.

![cp output](../assets/screenshots/03-files/cp.png)

## Syntax

```bash
cp [OPTION]... SOURCE... DESTINATION
```

## Options

| Option | Description |
|--------|-------------|
| `-r`, `-R`, `--recursive` | Copy directories with all their contents |
| `-a`, `--archive` | Copy recursively and keep permissions, owner, timestamps and links |
| `-p` | Keep permissions, owner and timestamps (without copying recursively) |
| `-i`, `--interactive` | Ask before overwriting an existing file |
| `-u`, `--update` | Only copy if the source is newer than the destination |
| `-v`, `--verbose` | Show every copied file |
| `-b`, `--backup` | Rename an existing destination file to `FILE~` before overwriting it |
| `-t`, `--target-directory=DIR` | Copy all sources into `DIR` |

## Examples

**Make a backup copy before editing a configuration:**

```bash
sudo cp -v /etc/ssh/sshd_config{,.bak}
```

```text
'/etc/ssh/sshd_config' -> '/etc/ssh/sshd_config.bak'
```

`{,.bak}` is expanded by Bash to `sshd_config sshd_config.bak`, so you only have to type
the path once.

**Copy a file under a new name:**

```bash
cp notes.txt notes-copy.txt
ls notes*
```

```text
notes-copy.txt  notes.txt
```

**Copy files into a directory:**

```bash
cp -v notes.txt scripts/backup.sh backup/
```

```text
'notes.txt' -> 'backup/notes.txt'
'scripts/backup.sh' -> 'backup/backup.sh'
```

**Copy a directory with all its contents:**

```bash
cp -r scripts scripts-old
ls -d scripts*
```

```text
scripts  scripts-old
```

**Keep owner and timestamps with `-a`:**

```bash
sudo cp -r /var/www/example.com /tmp/copy-r
sudo cp -a /var/www/example.com /tmp/copy-a
ls -ld /var/www/example.com /tmp/copy-*
```

```text
drwxr-xr-x 4 www-data www-data 4096 Oct 20 09:30 /tmp/copy-a
drwxr-xr-x 4 root     root     4096 Oct 26 10:42 /tmp/copy-r
drwxr-xr-x 4 www-data www-data 4096 Oct 20 09:30 /var/www/example.com
```

With `-r`, the copy belongs to `root` and has a new date. With `-a`, it is an exact copy.

**Ask before overwriting:**

```bash
cp -i notes.txt notes-copy.txt
```

```text
cp: overwrite 'notes-copy.txt'?
```

Answer with `y` to overwrite or `n` to cancel.

## When do I need it?

- Before every change to a configuration file: `cp file{,.bak}` gives you a way back
- To copy websites, application data or configuration directories (`cp -a`)
- To roll out a configuration file from a template, for example from
  `/usr/share/doc` or a Git repository
- To copy files to a mounted backup drive

!!! tip "Use `-a` for directories"
    For backups and moves of whole directories, `cp -a` is almost always the right
    choice. `cp -r` loses the owner, permissions and timestamps, and services may then
    no longer be able to read their files.

!!! warning "`cp` overwrites without asking"
    If the destination file exists, `cp` replaces it silently. Use `-i` when you are not
    sure, or `-b` to keep the old version as `FILE~`.

!!! warning "Existing destination directory"
    `cp -r scripts scripts-old` creates `scripts-old` the first time. If you run the same
    command again, `scripts-old` already exists and the copy ends up in
    `scripts-old/scripts`.

## Related commands

[mkdir](mkdir.md) · [touch](touch.md) · [mv](mv.md)
