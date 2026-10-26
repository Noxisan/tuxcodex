# umask

> Shows or sets which permissions new files and directories do **not** get.

![umask output](../assets/screenshots/06-permissions/umask.png)

## Syntax

```bash
umask [-S] [MASK]
```

## Options

| Option | Description |
|--------|-------------|
| *(none)* | Show the current mask as a number |
| `-S` | Show the mask as allowed permissions (`u=rwx,g=rx,o=rx`) |
| `MASK` | Set a new mask, as a number (`027`) or symbolically (`u=rwx,g=rx,o=`) |

New files start with `666` (`rw-rw-rw-`), new directories with `777` (`rwxrwxrwx`).
The `umask` removes permissions from these:

| umask | New files | New directories | Use |
|-------|-----------|-----------------|-----|
| `022` | `644` `rw-r--r--` | `755` `rwxr-xr-x` | Debian default |
| `027` | `640` `rw-r-----` | `750` `rwxr-x---` | Servers: others get nothing |
| `077` | `600` `rw-------` | `700` `rwx------` | Private: only the owner |

## Examples

**Show the current mask:**

```bash
umask
```

```text
0022
```

**Show the mask as permissions:**

```bash
umask -S
```

```text
u=rwx,g=rx,o=rx
```

**Create files without rights for others:**

```bash
umask 027
touch report.txt
mkdir reports
ls -ld report.txt reports
```

```text
-rw-r----- 1 nox nox    0 Oct 26 10:42 report.txt
drwxr-x--- 2 nox nox 4096 Oct 26 10:42 reports
```

**Create private files for a single task:**

```bash
(umask 077; mysqldump shop > /tmp/shop.sql)
ls -l /tmp/shop.sql
```

```text
-rw------- 1 nox nox 2451873 Oct 26 10:42 /tmp/shop.sql
```

The brackets run the commands in a subshell. The `umask 077` only applies there, and
your shell keeps its normal mask.

## When do I need it?

- To make sure that new files on a server are not readable by every user (`027`)
- In scripts that write passwords, keys or database dumps (`077`)
- When files of a service end up with the wrong permissions: the service's `umask`
  decides that

!!! tip "Make it permanent"
    `umask` only applies to the current shell. To keep it, add `umask 027` to your
    `~/.bashrc`. For all users, change `UMASK` in `/etc/login.defs`. For a systemd
    service, use `UMask=0027` in its unit file.

!!! warning "`umask` never adds `x` to files"
    Files start with `666`, so even `umask 000` creates them without execute permission.
    Scripts still need a `chmod +x` after creating them.

## Related commands

[chmod](chmod.md) · [touch](../03-files/touch.md) · [mkdir](../03-files/mkdir.md)
