# cat

> Prints the content of one or more files, and joins files together.

![cat output](../assets/screenshots/04-viewing-files/cat.png)

## Syntax

```bash
cat [OPTION]... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-n`, `--number` | Number all lines |
| `-b`, `--number-nonblank` | Number only lines that are not empty |
| `-A`, `--show-all` | Show hidden characters: `^I` tab, `$` end of line, `^M` Windows line ending |
| `-s`, `--squeeze-blank` | Show several empty lines in a row as one |
| `-E`, `--show-ends` | Show `$` at the end of every line |
| `-T`, `--show-tabs` | Show tabs as `^I` |

## Examples

**Show a short file:**

```bash
cat /etc/hostname
```

```text
tuxcodex-srv
```

**Show a file with line numbers:**

```bash
cat -n /etc/hosts
```

```text
     1  127.0.0.1       localhost
     2  127.0.1.1       tuxcodex-srv.example.com        tuxcodex-srv
     3
     4  # The following lines are desirable for IPv6 capable hosts
     5  ::1     localhost ip6-localhost ip6-loopback
     6  ff02::1 ip6-allnodes
     7  ff02::2 ip6-allrouters
```

**Make hidden characters visible:**

```bash
cat -A site.conf
```

```text
server {$
^Ilisten 80;$
    server_name example.com; $
}^M$
```

Now you can see the tab (`^I`), the space before the line end and the Windows line ending
(`^M`) in the last line.

**Join split files into one:**

```bash
cat backup.sql.part-aa backup.sql.part-ab > backup.sql
ls -lh backup.sql*
```

```text
-rw-r--r-- 1 nox nox 1.5G Oct 26 10:42 backup.sql
-rw-r--r-- 1 nox nox 1.0G Oct 26 10:30 backup.sql.part-aa
-rw-r--r-- 1 nox nox 512M Oct 26 10:30 backup.sql.part-ab
```

**Show your public SSH key to copy it:**

```bash
cat ~/.ssh/id_ed25519.pub
```

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIExampleKeyOnlyForThisHandbook0123456789ab nox@tuxcodex-srv
```

## When do I need it?

- To quickly look at short configuration files like `/etc/hostname` or `/etc/hosts`
- To copy a public key or a short configuration into a ticket or another server
- To find invisible problems like tabs, trailing spaces or Windows line endings (`-A`)
- To join files, for example split backups, into one

!!! tip "Long files belong in `less`"
    `cat` prints everything at once, and long files rush past. For anything longer than
    one screen, use [`less`](less.md).

!!! warning "Binary files mess up the terminal"
    `cat` on a binary file can print control characters that switch the terminal into a
    strange state. Type `reset` and press ++enter++ to fix it, even if you can't see
    what you type. Check unknown files with [`file`](../03-files/file.md) first.

## Related commands

[file](../03-files/file.md) · [tac](tac.md) · [nl](nl.md) · [less](less.md) · [head](head.md)
