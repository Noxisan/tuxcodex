# chattr

> Sets special file attributes, for example to protect a file against any change, even by `root`.

![chattr output](../assets/screenshots/06-permissions/chattr.png)

## Syntax

```bash
chattr [OPTION]... [+-=]ATTRIBUTES FILE...
```

## Options

| Option / form | Description |
|---------------|-------------|
| `+i` | Make the file immutable: no changes, no renaming, no deleting |
| `-i` | Remove the immutable attribute |
| `+a` | Append only: data can only be added at the end |
| `-a` | Remove the append only attribute |
| `-R` | Change all files and directories below as well |
| `-V` | Show what is being changed |

Setting and removing `i` and `a` requires `root`.

## Examples

**Protect a file against any change:**

```bash
sudo chattr +i /etc/resolv.conf
lsattr /etc/resolv.conf
```

```text
----i---------e------- /etc/resolv.conf
```

**Even `root` cannot delete it now:**

```bash
sudo rm /etc/resolv.conf
```

```text
rm: cannot remove '/etc/resolv.conf': Operation not permitted
```

**Or overwrite it:**

```bash
echo "nameserver 192.0.2.53" | sudo tee /etc/resolv.conf
```

```text
tee: /etc/resolv.conf: Operation not permitted
nameserver 192.0.2.53
```

`tee` still prints the line on the screen, but the file stays unchanged.

**Remove the protection again:**

```bash
sudo chattr -i /etc/resolv.conf
lsattr /etc/resolv.conf
```

```text
--------------e------- /etc/resolv.conf
```

**Make a log file append only:**

```bash
sudo chattr +a /var/log/app/audit.log
echo "test" | sudo tee /var/log/app/audit.log
echo "test" | sudo tee -a /var/log/app/audit.log
```

```text
tee: /var/log/app/audit.log: Operation not permitted
test
test
```

Overwriting fails, appending with `tee -a` works.

## When do I need it?

- To keep a file from being overwritten by a program, for example `/etc/resolv.conf`
  by a DHCP client
- To protect audit logs: with `+a`, entries can be added, but not deleted or changed
- To protect important configuration files against accidental changes, also by admins

!!! tip "Find out why `root` can't change a file"
    If even `sudo` gets `Operation not permitted`, check the attributes with
    [`lsattr`](lsattr.md). An `i` is often a leftover from someone who protected the
    file years ago.

!!! warning "Updates fail on protected files"
    `apt` cannot replace or delete files with `+i`. Package updates then fail with an
    error. Remove the attribute before updates, or only protect files that no package
    manages.

!!! warning "Logrotate and `+a`"
    A file with `+a` cannot be renamed or emptied, so log rotation fails. Only use `+a`
    for logs that are not rotated, or remove the attribute in the rotation script.

## Related commands

[lsattr](lsattr.md) · [chmod](chmod.md)
