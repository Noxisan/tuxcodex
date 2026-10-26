# zcat

> Prints the content of gzip-compressed files without unpacking them on the disk.

![zcat output](../assets/screenshots/04-viewing-files/zcat.png)

## Syntax

```bash
zcat [OPTION]... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-f`, `--force` | Also print files that are not compressed, unchanged |
| `-l`, `--list` | Show compressed size, original size and compression ratio |
| `-t`, `--test` | Check whether the compressed file is intact |

## Examples

**Read a rotated log:**

```bash
zcat /var/log/nginx/access.log.2.gz | head -n 2
```

```text
192.0.2.10 - - [24/Oct/2026:00:03:17 +0200] "GET / HTTP/1.1" 200 6512 "-" "Mozilla/5.0"
198.51.100.7 - - [24/Oct/2026:00:05:42 +0200] "GET /robots.txt HTTP/1.1" 200 68 "-" "Mozilla/5.0"
```

**Look into a compressed database dump:**

```bash
zcat backup/db-2026-10-20.sql.gz | head -n 3
```

```text
--
-- PostgreSQL database dump
--
```

**Show how big the file is when unpacked:**

```bash
zcat -l /var/log/nginx/access.log.2.gz
```

```text
         compressed        uncompressed  ratio uncompressed_name
               3518               28734  87.8% /var/log/nginx/access.log.2
```

**Read all rotated logs at once, compressed or not:**

```bash
zcat -f /var/log/nginx/access.log* | wc -l
```

```text
18342
```

`-f` passes uncompressed files like `access.log` and `access.log.1` through unchanged.

**Check whether a backup is intact:**

```bash
zcat -t backup/db-2026-10-20.sql.gz && echo OK
```

```text
OK
```

## When do I need it?

- To read older, rotated logs (`*.gz` in `/var/log`) without unpacking them
- To check what is inside a compressed backup or dump before restoring it
- To search old logs together with `grep`, or to pipe a dump directly into a database:
  `zcat dump.sql.gz | psql mydb`

!!! tip "Other compression formats"
    Each format has its own `cat`: `xzcat` for `.xz`, `bzcat` for `.bz2` and `zstdcat`
    for `.zst`. They work exactly like `zcat`.

!!! warning "Only for gzip files"
    On a file that is not compressed, `zcat` stops with `gzip: notes.txt: not in gzip
    format`. Use `zcat -f` when a list contains both compressed and uncompressed files.

## Related commands

[cat](cat.md) · [less](less.md) · [zless](zless.md)
