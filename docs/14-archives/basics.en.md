# Understanding archives

Two different things are often mixed up:

| Step | What happens | Tools |
|------|--------------|-------|
| **Archiving** | Many files and directories become one file, with names, permissions and dates | `tar`, `zip` |
| **Compressing** | One file becomes smaller | `gzip`, `bzip2`, `xz`, `zstd` |

On Linux, both are usually combined: `tar` packs the directory, a compressor shrinks the
result. `zip` does both in one step and is the standard for exchanging files with Windows.

## File extensions

| Extension | Content | Unpack with |
|-----------|---------|-------------|
| `.tar` | Archive, not compressed | `tar -xf` |
| `.tar.gz`, `.tgz` | tar archive compressed with gzip | `tar -xzf` |
| `.tar.bz2` | tar archive compressed with bzip2 | `tar -xjf` |
| `.tar.xz` | tar archive compressed with xz | `tar -xJf` |
| `.tar.zst` | tar archive compressed with zstd | `tar --zstd -xf` |
| `.gz`, `.bz2`, `.xz`, `.zst` | A single compressed file | `gunzip`, `bunzip2`, `unxz`, `unzstd` |
| `.zip` | Archive and compression in one | `unzip` |

Modern GNU tar detects the compression itself when unpacking: `tar -xf file.tar.zst` is
enough.

## The methods compared

Example values for a database dump of 412 MiB on the example server, each with the
default level:

| Method | Size afterwards | Time to compress | Time to decompress | Use |
|--------|-----------------|------------------|--------------------|-----|
| gzip | 77 MiB | 14 s | 3 s | Compatible everywhere, the classic |
| bzip2 | 69 MiB | 38 s | 12 s | Hardly used anymore |
| xz | 49 MiB | 2 min 10 s | 4 s | Smallest files, slow, for downloads and releases |
| zstd | 54 MiB | 2 s | 1 s | Fast and small, the best choice for backups today |

The values depend heavily on the data: text and SQL dumps shrink a lot, images, videos
and already compressed files hardly at all.

!!! tip "zstd for backups"
    zstd compresses almost as well as xz, but many times faster. For regular backups,
    that saves CPU time and shortens the backup window. Use gzip only when the archive
    has to be opened on old systems.

!!! warning "Compression doesn't replace verification"
    A broken archive is often only noticed when restoring. Test archives after creating
    them (`tar -tf`, `unzip -t`) and keep a checksum with [`sha256sum`](sha256sum.md).
