# gzip

> Compresses single files quickly and replaces them with a `.gz` file. The most widespread compression on Linux.

![gzip output](../assets/screenshots/14-archives/gzip.png)

## Syntax

```bash
gzip [OPTION]... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-k` | Keep the original file |
| `-d`, `gunzip` | Decompress |
| `-v` | Show the compression ratio |
| `-l` | Show compressed and uncompressed size |
| `-1` … `-9` | Fast or strong, default `6` |
| `-c` | Write to standard output, keep the file |

## Examples

**Compress a database dump:**

```bash
gzip -v db.sql
```

```text
db.sql:  81.4% -- replaced with db.sql.gz
```

The original `db.sql` is gone, only `db.sql.gz` remains.

**Show the sizes:**

```bash
gzip -l db.sql.gz
```

```text
         compressed        uncompressed  ratio uncompressed_name
           80427365           432013312  81.4% db.sql
```

**Decompress again:**

```bash
gunzip -v db.sql.gz
```

```text
db.sql.gz:       81.4% -- replaced with db.sql
```

**Compress a dump directly while creating it:**

```bash
pg_dump shop | gzip > shop.sql.gz
ls -lh shop.sql.gz
```

```text
-rw-r--r-- 1 nox nox 77M Oct 26 10:42 shop.sql.gz
```

## When do I need it?

- For log files, database dumps and other text files that are kept
- When the file has to be opened on any system, also very old ones
- Together with `tar` for `.tar.gz` archives

!!! tip "Read without unpacking"
    [`zcat`](../04-viewing-files/zcat.md) and [`zless`](../04-viewing-files/zless.md) show the content of `.gz` files directly,
    without unpacking them first.

!!! warning "The original disappears"
    Without `-k`, `gzip` deletes the original file after compressing. Use `-k` if you still
    need it.

## Related commands

[tar](tar.md) · [zstd](zstd.md) · [zcat](../04-viewing-files/zcat.md)
