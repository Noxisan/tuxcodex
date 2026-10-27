# zstd

> Compresses very fast and still small. The modern choice for backups and logs.

![zstd output](../assets/screenshots/14-archives/zstd.png)

## Syntax

```bash
zstd [OPTION]... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-d`, `unzstd` | Decompress |
| `--rm` | Delete the original after compressing (it is kept by default) |
| `-l` | Show information about a `.zst` file |
| `-T0` | Use all CPU cores |
| `-1` … `-19` | Level, default `3` |
| `-o FILE` | Name of the output file |

## Examples

**Compress a dump:**

```bash
zstd -T0 db.sql
```

```text
db.sql               : 13.02%   (   412 MiB =>   53.6 MiB, db.sql.zst)
```

Unlike gzip, `zstd` keeps the original file.

**Show information about the file:**

```bash
zstd -l db.sql.zst
```

```text
Frames  Skips  Compressed  Uncompressed  Ratio  Check  Filename
     1      0    53.6 MiB     412 MiB  7.684  XXH64  db.sql.zst
```

**Decompress:**

```bash
zstd -d db.sql.zst -o restore.sql
```

```text
db.sql.zst          : 432013312 bytes
```

**A backup as `.tar.zst`:**

```bash
tar --zstd -cf etc-2026-10-26.tar.zst -C / etc
ls -lh etc-2026-10-26.tar.zst
```

```text
-rw-r--r-- 1 root root 1.2M Oct 26 10:42 etc-2026-10-26.tar.zst
```

## When do I need it?

- For daily backups, where speed matters
- For large log archives and database dumps
- Whenever you are free to choose the method: zstd is a very good default

!!! tip "Higher levels for archives"
    `zstd -19 -T0` compresses almost as strongly as xz. Unpacking stays just as fast,
    whatever level was used.

!!! tip "Not always installed"
    The library is part of every distribution, the command `zstd` not always. If it is
    missing, install the package `zstd`.

## Related commands

[tar](tar.md) · [xz](xz.md) · [gzip](gzip.md)
