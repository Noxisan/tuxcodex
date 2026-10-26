# ls

> Lists the contents of a directory, optionally with permissions, owner, size and date.

![ls output](../assets/screenshots/02-navigation/ls.png)

## Syntax

```bash
ls [OPTION]... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-l` | Long format: permissions, owner, group, size and date |
| `-a`, `--all` | Also show hidden files (starting with `.`), including `.` and `..` |
| `-A`, `--almost-all` | Show hidden files, but without `.` and `..` |
| `-h`, `--human-readable` | Sizes in K, M, G instead of bytes (with `-l`) |
| `-t` | Sort by modification time, newest first |
| `-r`, `--reverse` | Reverse the sort order |
| `-S` | Sort by size, largest first |
| `-R`, `--recursive` | Also list all subdirectories |
| `-d`, `--directory` | Show the directory itself, not its contents |
| `-1` | One entry per line |
| `-F`, `--classify` | Mark the type: `/` directory, `*` executable, `@` link |
| `-i`, `--inode` | Show the inode number |
| `--group-directories-first` | Show directories before files |

## Examples

**List the current directory:**

```bash
ls
```

```text
backup  notes.txt  scripts
```

**Show details in long format:**

```bash
ls -l
```

```text
total 12
drwxr-xr-x 2 nox nox 4096 Oct 20 14:03 backup
-rw-r--r-- 1 nox nox  812 Oct 26 09:15 notes.txt
drwxr-xr-x 2 nox nox 4096 Oct 22 18:40 scripts
```

| Column | Meaning |
|--------|---------|
| `drwxr-xr-x` | Type (`d` directory, `-` file, `l` link) and permissions |
| `2` | Number of hard links |
| `nox nox` | Owner and group |
| `4096` | Size in bytes |
| `Oct 20 14:03` | Time of the last change |
| `backup` | Name |

**Also show hidden files:**

```bash
ls -la
```

```text
total 36
drwx------ 4 nox  nox  4096 Oct 26 09:15 .
drwxr-xr-x 3 root root 4096 Sep  9 14:25 ..
-rw------- 1 nox  nox  1843 Oct 26 10:40 .bash_history
-rw-r--r-- 1 nox  nox   220 Sep  9 14:25 .bash_logout
-rw-r--r-- 1 nox  nox  3526 Sep  9 14:25 .bashrc
-rw-r--r-- 1 nox  nox   807 Sep  9 14:25 .profile
drwxr-xr-x 2 nox  nox  4096 Oct 20 14:03 backup
-rw-r--r-- 1 nox  nox   812 Oct 26 09:15 notes.txt
drwxr-xr-x 2 nox  nox  4096 Oct 22 18:40 scripts
```

**Show sizes in a readable format:**

```bash
ls -lh backup
```

```text
total 1.3G
-rw-r--r-- 1 nox nox 1.2G Oct 20 14:03 db-2026-10-20.sql.gz
-rw-r--r-- 1 nox nox  98M Oct 20 14:01 etc-2026-10-20.tar.gz
```

**Sort by time, newest at the bottom (handy for logs):**

```bash
ls -ltr /var/log/nginx/access*
```

```text
-rw-r----- 1 www-data adm  3518 Oct 24 23:59 /var/log/nginx/access.log.2.gz
-rw-r----- 1 www-data adm 12873 Oct 25 23:59 /var/log/nginx/access.log.1
-rw-r----- 1 www-data adm  4102 Oct 26 10:41 /var/log/nginx/access.log
```

**Show only directories:**

```bash
ls -d */
```

```text
backup/  scripts/
```

**Show the permissions of a directory itself:**

```bash
ls -ld /etc
```

```text
drwxr-xr-x 79 root root 4096 Oct 26 08:01 /etc
```

## When do I need it?

- Constantly: to see what is in a directory before you work with it
- To check owner and permissions when a service cannot read a file (`ls -l`)
- To find the newest log file or the most recent backup (`ls -ltr`)
- To find large files in a directory (`ls -lhS`)
- To spot hidden configuration files such as `.htaccess` or `.env` (`ls -la`)

!!! tip "Shortcuts with aliases"
    Debian's default `.bashrc` already contains aliases like `ll` for `ls -l`, but they
    are commented out. Remove the `#` in front of `alias ll='ls -l'` in `~/.bashrc` and
    open a new shell to use them.

!!! warning "Don't use `ls` output in scripts"
    File names can contain spaces and special characters that break the output of `ls`.
    In scripts, use `for f in /path/*` or [`find`](find.md) instead.

## Related commands

[cd](cd.md) · [pwd](pwd.md) · [tree](tree.md) · [find](find.md)
