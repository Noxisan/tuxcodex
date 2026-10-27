# Understanding storage

Before a disk can store files, it goes through four layers: the **disk** itself, a
**partition table** that divides it, a **file system** on each partition, and a
**mount point** where the file system appears in the directory tree.

## Disks and partitions

Linux shows every disk as a file in `/dev`:

| Name | Typical device |
|------|----------------|
| `/dev/sda`, `/dev/sdb` | SATA and SCSI disks, also most virtual disks |
| `/dev/vda` | Virtual disks with the virtio driver (KVM, many cloud providers) |
| `/dev/nvme0n1` | NVMe SSDs |
| `/dev/sda1`, `/dev/nvme0n1p1` | The first partition on that disk |
| `/dev/mapper/vg_data-lv_srv` | A logical volume of LVM |

On the example server `tuxcodex-srv`, the system disk `sda` has three partitions, the
backup disk `sdb` one, and the disk `sdc` belongs to LVM.

## Partition tables

| Type | Maximum disk size | Partitions | Use |
|------|-------------------|------------|-----|
| **GPT** | practically unlimited | 128 | Standard today, required for disks larger than 2 TiB and for UEFI |
| **MBR** (DOS) | 2 TiB | 4 primary | Old systems and old BIOS boot |

Use GPT for new disks.

## File systems

| File system | Strengths | Grow | Shrink |
|-------------|-----------|------|--------|
| **ext4** | Robust, universal, the classic on Linux | yes, also while mounted | yes, only unmounted |
| **XFS** | Very good with large files and many parallel accesses | yes, while mounted | no |
| **Btrfs** | Snapshots, checksums, compression, several disks | yes | yes |
| **vfat** | Readable everywhere, required for the EFI partition | rarely | rarely |
| **swap** | Not a file system: swap space for memory | | |

## `/etc/fstab`: mounting at boot

Every line in `/etc/fstab` describes one file system that is mounted at boot:

```text
# <file system>                           <mount point> <type> <options>         <dump> <pass>
UUID=c1f4e2a7-5b3d-4e8a-9f61-2d7b8c0e9a14 /             ext4   errors=remount-ro 0      1
UUID=4A1C-7F32                            /boot/efi     vfat   umask=0077        0      1
UUID=8e2b6d4f-1a3c-4f5e-b7d9-0c2e4a6f8b31 none          swap   sw                0      0
UUID=87c6aa0c-cb18-455e-b534-d2864a90bb80 /mnt/backup   ext4   defaults,nofail   0      2
/dev/mapper/vg_data-lv_srv                /srv/data     ext4   defaults          0      2
```

| Field | Meaning |
|-------|---------|
| File system | Which device. Use `UUID=` from `blkid`, because names like `sdb` can change |
| Mount point | Where it appears in the directory tree |
| Options | `defaults`, plus e.g. `nofail` (boot even if the disk is missing) or `noatime` |
| Pass | Order of the check at boot: `1` for `/`, `2` for the rest, `0` never |

## LVM: flexible volumes

LVM puts a layer between disks and file systems:

| Layer | Name | Command |
|-------|------|---------|
| Disks or partitions | **Physical volumes** (PV) | `pvs`, `pvcreate` |
| Pool from one or more PVs | **Volume groups** (VG) | `vgs`, `vgcreate`, `vgextend` |
| "Partitions" taken from the pool | **Logical volumes** (LV) | `lvs`, `lvcreate`, `lvextend` |

The big advantage: when a volume gets full, you add a disk to the volume group and grow
the logical volume, while the server keeps running.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Default file system of the installer | ext4 | ext4 | XFS | chosen during installation |
| LVM in the default installation | optional | yes | yes | no |
| `/tmp` in memory (tmpfs) | yes, since Debian 13 | no | no | yes |

!!! tip "UUIDs instead of device names"
    The order of disks can change after a reboot or when a disk is added: yesterday's
    `sdb` can be `sdc` today. UUIDs in `/etc/fstab` always point to the right file system.

!!! danger "Test `/etc/fstab` before rebooting"
    A wrong line in `/etc/fstab` can stop the boot process. After every change, run
    `sudo findmnt --verify` and `sudo mount -a`. Only reboot if both report no errors.
