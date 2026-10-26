# chgrp

> Changes only the group of files and directories.

![chgrp output](../assets/screenshots/06-permissions/chgrp.png)

## Syntax

```bash
chgrp [OPTION]... GROUP FILE...
```

## Options

| Option | Description |
|--------|-------------|
| `-R`, `--recursive` | Change all files and directories below as well |
| `-v`, `--verbose` | Show every change |
| `-c`, `--changes` | Only show files whose group really changed |
| `-h`, `--no-dereference` | Change a symbolic link itself, not its target |
| `--reference=FILE` | Copy the group of `FILE` |

## Examples

**Give a group access to a directory:**

```bash
sudo chgrp -v developers /srv/shared
```

```text
changed group of '/srv/shared' from root to developers
```

**Change the group of a whole directory tree:**

```bash
sudo chgrp -R developers /srv/shared
ls -l /srv/shared
```

```text
total 8
-rw-rw-r-- 1 nox   developers 1840 Oct 26 10:12 notes.md
drwxrwsr-x 2 alice developers 4096 Oct 26 10:30 scripts
```

**Let a service read a key without giving it the file:**

```bash
sudo chgrp ssl-cert /etc/ssl/private/example.com.key
sudo chmod 640 /etc/ssl/private/example.com.key
ls -l /etc/ssl/private/example.com.key
```

```text
-rw-r----- 1 root ssl-cert 1704 Oct 20 11:05 /etc/ssl/private/example.com.key
```

`root` remains the owner, members of `ssl-cert` may read the key.

**Change to a group you don't belong to:**

```bash
chgrp www-data notes.txt
```

```text
chgrp: changing group of 'notes.txt': Operation not permitted
```

Without `sudo`, you can only change to groups you are a member of yourself.

## When do I need it?

- To set up shared directories for a team (together with `chmod g+s`)
- To let a service read a file through its group, while `root` stays the owner,
  for example TLS keys and the group `ssl-cert`
- When you only want to change the group and leave the owner as it is

!!! tip "Which groups do I have?"
    `id -Gn` lists all groups you belong to. These are the groups you can use with
    `chgrp` without `sudo`.

!!! warning "Group permissions must fit"
    Changing the group alone doesn't give anyone access. The group also needs the right
    permissions: check with `ls -l` and adjust with `chmod g+r` or `chmod g+w`.

## Related commands

[chown](chown.md) · [chmod](chmod.md) · [id](../01-orientation/id.md)
