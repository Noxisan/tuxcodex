# umount

> Unmounts a file system, so the disk can be removed, checked or changed safely.

![umount output](../assets/screenshots/13-disks-storage/umount.png)

## Syntax

```bash
umount [OPTION]... MOUNTPOINT | DEVICE
```

The command is called `umount`, without the first `n`.

## Options

| Option | Description |
|--------|-------------|
| `MOUNTPOINT` | Unmount the file system mounted there |
| `-l` | Lazy: detach now, clean up as soon as it is no longer in use |
| `-R` | Also unmount everything mounted below |
| `-f` | Force, mainly for unreachable network file systems |

## Examples

**Unmount a file system:**

```bash
sudo umount /mnt/archive && echo "unmounted"
```

```text
unmounted
```

**The file system is still in use:**

```bash
sudo umount /mnt/backup
```

```text
umount: /mnt/backup: target is busy.
```

**Find the processes that block it:**

```bash
sudo fuser -vm /mnt/backup
```

```text
                     USER        PID ACCESS COMMAND
/mnt/backup:         root     kernel mount /mnt/backup
                     nox        2201 ..c.. bash
                     nox        4415 F.... rsync
```

`c` means: the shell has its working directory there, `F`: `rsync` has a file open.
Leave the directory and let `rsync` finish, then `umount` works.

## When do I need it?

- Before checking a file system with `fsck` or shrinking it
- Before removing or detaching a disk
- When a mount point should be released for something else

!!! tip "Find out who blocks it"
    `target is busy` means: a process has a file open there or a shell is in the
    directory. [`lsof +D`](../08-processes/lsof.md) or `fuser -vm` show which one.

!!! warning "`-l` hides the problem"
    A lazy unmount detaches the mount point immediately, but the processes keep writing to
    the disk. Don't remove the disk until they have ended.

## Related commands

[mount](mount.md) · [lsof](../08-processes/lsof.md) · [fsck](fsck.md)
