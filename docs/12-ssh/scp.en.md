# scp

> Copies files and directories over SSH, between your computer and a server or between two servers.

![scp output](../assets/screenshots/12-ssh/scp.png)

## Syntax

```bash
scp [OPTION]... SOURCE... TARGET
```

A remote path has the form `USER@HOST:PATH`. Without a leading `/`, the path is relative to the home directory on the server.

## Options

| Option | Description |
|--------|-------------|
| `-r` | Copy directories recursively |
| `-P PORT` | SSH port of the server (capital `P`) |
| `-p` | Keep modification times and permissions |
| `-i FILE` | Use this private key |
| `-l LIMIT` | Limit the bandwidth in Kbit/s |
| `-3` | Copy between two servers through your computer |

## Examples

**Copy a file to the server:**

```bash
scp db.sql.gz nox@192.0.2.10:/srv/backup/
```

```text
db.sql.gz                                     100%   29MB  11.2MB/s   00:02
```

**Fetch a file from the server:**

```bash
scp nox@192.0.2.10:/var/log/nginx/error.log .
```

```text
error.log                                     100%   84KB   1.9MB/s   00:00
```

`.` at the end means: into the current directory.

**Copy a whole directory:**

```bash
scp -r ~/srv/www nox@192.0.2.10:/tmp/
```

```text
file1.bin                                     100%  195KB   8.1MB/s   00:00
file2.bin                                     100%  195KB   8.4MB/s   00:00
file3.bin                                     100%  195KB   8.3MB/s   00:00
index.html                                    100% 6512     1.1MB/s   00:00
```

**Use a different SSH port:**

```bash
scp -P 2222 config.tar.gz nox@192.0.2.20:
```

```text
config.tar.gz                                 100%   12KB   2.0MB/s   00:00
```

## When do I need it?

- To quickly copy a single file to or from a server
- To fetch a backup or a log file for analysis
- When `rsync` isn't installed on the server

!!! tip "`rsync` for larger jobs"
    `scp` always copies everything again and can't resume an interrupted transfer. For
    directories and large files, [`rsync`](rsync.md) is faster and more robust.

!!! warning "Spaces and special characters in remote paths"
    Remote paths are interpreted by the shell on the server. Quote paths with spaces
    twice: `scp nox@192.0.2.10:"'/srv/old backup.tar.gz'" .`

## Related commands

[rsync](rsync.md) · [sftp](sftp.md) · [ssh](ssh.md) · [cp](../03-files/cp.md)
