# whereis

> Finds the program file, configuration and man pages of a command in the standard system directories.

![whereis output](../assets/screenshots/02-navigation/whereis.png)

## Syntax

```bash
whereis [OPTION]... NAME...
```

## Options

| Option | Description |
|--------|-------------|
| `-b` | Only search for program files (binaries) |
| `-m` | Only search for man pages |
| `-s` | Only search for source files |
| `-u` | Only show names with unusual entries (missing or multiple matches) |
| `-B DIR... -f` | Only search for programs in the given directories |
| `-M DIR... -f` | Only search for man pages in the given directories |
| `-l` | Show the directories that `whereis` searches |

## Examples

**Find program and man page of a command:**

```bash
whereis ls
```

```text
ls: /usr/bin/ls /usr/share/man/man1/ls.1.gz
```

**Find everything that belongs to a service:**

```bash
whereis nginx
```

```text
nginx: /usr/sbin/nginx /usr/lib/nginx /etc/nginx /usr/share/nginx /usr/share/man/man8/nginx.8.gz
```

**Only show program files and directories:**

```bash
whereis -b ssh
```

```text
ssh: /usr/bin/ssh /etc/ssh
```

**Only show the man page:**

```bash
whereis -m ssh
```

```text
ssh: /usr/share/man/man1/ssh.1.gz
```

**A program that is not installed:**

```bash
whereis nmap
```

```text
nmap:
```

## When do I need it?

- To find the configuration directory of a service quickly (`/etc/nginx`, `/etc/ssh`)
- To check whether a program and its man page are installed
- To find admin programs in `/usr/sbin` that [`which`](which.md) does not find as a
  normal user

!!! tip "`whereis` vs. `which`"
    `which` only searches your `$PATH` and shows the program that really runs.
    `whereis` searches a fixed list of system directories (`/usr/bin`, `/usr/sbin`,
    `/etc`, `/usr/share/man` …) and also finds man pages and configuration.

!!! warning "Only standard directories"
    Programs in unusual places, such as `/opt/app/bin`, are not found by `whereis`.
    Use [`locate`](locate.md) or [`find`](find.md) for those.

## Related commands

[which](which.md) · [locate](locate.md)
