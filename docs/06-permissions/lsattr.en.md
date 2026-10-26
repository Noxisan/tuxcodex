# lsattr

> Shows the special file attributes on ext4 and similar file systems, for example "immutable" or "append only".

![lsattr output](../assets/screenshots/06-permissions/lsattr.png)

## Syntax

```bash
lsattr [OPTION]... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-d` | Show the directory itself, not its contents |
| `-R` | Also show all subdirectories |
| `-a` | Also show hidden files |
| `-l` | Show the attribute names instead of letters |

The most important attributes:

| Letter | Name | Meaning |
|--------|------|---------|
| `i` | Immutable | Nobody may change, rename or delete the file, not even `root` |
| `a` | Append only | Data can only be added at the end, not overwritten |
| `e` | Extents | The file uses extents (normal on ext4, not a protection) |
| `A` | No atime | The access time is not updated |

## Examples

**Show the attributes of a file:**

```bash
lsattr /etc/resolv.conf
```

```text
--------------e------- /etc/resolv.conf
```

Only `e` is set, which is normal on ext4. The file is not protected.

**A protected file:**

```bash
lsattr /etc/resolv.conf
```

```text
----i---------e------- /etc/resolv.conf
```

The `i` means: the file is immutable.

**Show the attributes with names:**

```bash
lsattr -l /etc/resolv.conf
```

```text
/etc/resolv.conf             Immutable, Extents
```

**Check all files in a directory:**

```bash
lsattr /var/log/app/
```

```text
-----a--------e------- /var/log/app/audit.log
--------------e------- /var/log/app/error.log
```

`audit.log` is append only: entries can be added, but not deleted or changed.

**Show the attributes of a directory itself:**

```bash
lsattr -d /var/log/app
```

```text
--------------e------- /var/log/app
```

## When do I need it?

- When even `root` gets `Operation not permitted` while changing or deleting a file:
  an `i` or `a` attribute is often the reason
- When a package update fails because a configuration file cannot be replaced
- To check whether protective attributes you set with `chattr` are still active

!!! tip "\"Operation not permitted\" as root"
    If `sudo rm` or `sudo` editing fails with `Operation not permitted`, run `lsattr` on
    the file first. Normal permissions never stop `root`, attributes do.

!!! warning "Only on certain file systems"
    Attributes are a feature of ext2/3/4 and partly of Btrfs and XFS. On other file
    systems like `tmpfs` or network shares, `lsattr` reports an error.

## Related commands

[stat](../03-files/stat.md) · [ls](../02-navigation/ls.md) · [chattr](chattr.md)
