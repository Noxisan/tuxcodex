# head

> Shows the first lines of a file, by default the first 10.

![head output](../assets/screenshots/04-viewing-files/head.png)

## Syntax

```bash
head [OPTION]... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-n N`, `--lines=N` | Show the first `N` lines instead of 10 |
| `-n -N` | Show everything except the last `N` lines |
| `-c N`, `--bytes=N` | Show the first `N` bytes |
| `-q`, `--quiet` | Don't print file names when showing several files |
| `-v`, `--verbose` | Always print the file name |

## Examples

**Show the first lines of a file:**

```bash
head -n 3 /etc/os-release
```

```text
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
```

**Show the oldest entries of a log:**

```bash
head -n 2 /var/log/nginx/access.log
```

```text
192.0.2.10 - - [26/Oct/2026:09:12:03 +0100] "GET / HTTP/1.1" 200 6512 "-" "Mozilla/5.0"
192.0.2.10 - - [26/Oct/2026:09:12:03 +0100] "GET /style.css HTTP/1.1" 200 1840 "-" "Mozilla/5.0"
```

**Look at the beginning of several files:**

```bash
head -n 1 /etc/hostname /etc/os-release
```

```text
==> /etc/hostname <==
tuxcodex-srv

==> /etc/os-release <==
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
```

**Show everything except the last line:**

```bash
head -n -1 deploy.log
```

```text
2026-10-26 10:40:01 deploy started
2026-10-26 10:40:12 files copied
```

**Find the newest file in a directory:**

```bash
ls -t backup | head -n 1
```

```text
db-2026-10-20.sql.gz
```

## When do I need it?

- To check what a file looks like before you open or process it, for example the
  column headers of a CSV export
- To see where a log starts, for example to find out how far back it goes
- Together with other commands: `ls -t | head -n 1` for the newest file, `sort | head`
  for the top entries of a list

!!! tip "Combine with `tail` for a range"
    `head -n 20 FILE | tail -n 5` shows lines 16 to 20. This way you can cut any range
    out of a file.

!!! warning "Not the newest log entries"
    Log files grow at the end. `head` shows the **oldest** entries. For the newest ones,
    use `tail`.

## Related commands

[cat](cat.md) · [less](less.md)
