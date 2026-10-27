# lvcreate

> Creates a new logical volume in a volume group: a flexible "partition" that you can format, mount and grow later.

![lvcreate output](../assets/screenshots/13-disks-storage/lvcreate.png)

## Syntax

```bash
lvcreate [OPTION]... VG
```

## Options

| Option | Description |
|--------|-------------|
| `-L SIZE` | Size, e.g. `20G` |
| `-l 100%FREE` | Use all free space of the group |
| `-n NAME` | Name of the volume |
| `-s` | Create a snapshot of an existing volume |

## Examples

**Create a volume of 10 GiB for logs:**

```bash
sudo lvcreate -L 10G -n lv_logs vg_data
```

```text
  Logical volume "lv_logs" created.
```

**Format and mount it:**

```bash
sudo mkfs.ext4 -q -L logs /dev/vg_data/lv_logs
sudo mkdir -p /srv/logs
sudo mount /dev/vg_data/lv_logs /srv/logs
sudo lvs
```

```text
  LV      VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lv_logs vg_data -wi-ao---- 10.00g
  lv_srv  vg_data -wi-ao---- 30.00g
```

**Create a snapshot before an update:**

```bash
sudo lvcreate -s -L 5G -n lv_srv_snap vg_data/lv_srv
```

```text
  Logical volume "lv_srv_snap" created.
```

**Not enough free space:**

```bash
sudo lvcreate -L 30G -n lv_big vg_data
```

```text
  Volume group "vg_data" has insufficient free space (1279 extents): 7680 required.
```

After the two volumes above, less than 5 GiB are free. Add a disk with
[`vgextend`](vgs.md) first.

## When do I need it?

- To create a separate volume for data, logs or a database
- To use the free space of a volume group
- Before a risky update, as a snapshot you can return to

!!! tip "Leave space free"
    Don't assign all space at once. Free space in the volume group lets you grow exactly the
    volume that needs it later.

!!! warning "Snapshots fill up"
    A snapshot stores all changes since it was created. If it runs full, it becomes
    invalid. Remove snapshots after the update with `lvremove`.

## Related commands

[lvs](lvs.md) · [lvextend](lvextend.md) · [mkfs](mkfs.md) · [vgs](vgs.md)
