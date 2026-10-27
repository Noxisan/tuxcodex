# findmnt

> Shows mounted file systems as a tree, finds out where a path is mounted from, and checks `/etc/fstab` for errors.

![findmnt output](../assets/screenshots/13-disks-storage/findmnt.png)

## Syntax

```bash
findmnt [OPTION]... [DEVICE | MOUNTPOINT]
```

## Options

| Option | Description |
|--------|-------------|
| `-t TYPES` | Only these file system types, e.g. `ext4,xfs` |
| `-T PATH` | The file system that contains `PATH` |
| `-D` | Output like `df`: size, used, available |
| `--verify` | Check `/etc/fstab` for errors |
| `-s` | Show `/etc/fstab` instead of the mounted file systems |

## Examples

**Show the real file systems as a tree:**

```bash
findmnt -t ext4,xfs,vfat
```

```text
TARGET        SOURCE                     FSTYPE OPTIONS
/             /dev/sda2                  ext4   rw,relatime,errors=remount-ro
├─/boot/efi   /dev/sda1                  vfat   rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=mixed,utf8,errors=remount-ro
├─/mnt/backup /dev/sdb1                  ext4   rw,relatime
└─/srv/data   /dev/mapper/vg_data-lv_srv ext4   rw,relatime
```

**Find out on which file system a directory is:**

```bash
findmnt -T /srv/data/uploads
```

```text
TARGET    SOURCE                     FSTYPE OPTIONS
/srv/data /dev/mapper/vg_data-lv_srv ext4   rw,relatime
```

**Size and usage of a mount point:**

```bash
findmnt -D /srv/data
```

```text
SOURCE                     FSTYPE  SIZE USED AVAIL USE% TARGET
/dev/mapper/vg_data-lv_srv ext4   29.4G 6.8G 21.1G  23% /srv/data
```

**Check `/etc/fstab` after a change:**

```bash
sudo findmnt --verify
```

```text
Success, no errors or warnings detected
```

## When do I need it?

- To see which file systems are mounted, without the noise of `mount`
- To find out on which disk a directory really is
- After every change to `/etc/fstab`, before rebooting

!!! tip "Clearer than `mount`"
    `mount` without arguments lists dozens of virtual file systems. `findmnt -t ext4,xfs,vfat`
    only shows the real ones, as a tree.

## Related commands

[mount](mount.md) · [df](df.md) · [lsblk](lsblk.md)
