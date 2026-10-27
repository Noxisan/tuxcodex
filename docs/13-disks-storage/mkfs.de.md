# mkfs

> Legt ein Dateisystem auf einer Partition oder einem Volume an, kurz: formatiert sie. `mkfs.ext4`, `mkfs.xfs` und andere sind die Varianten für jedes Dateisystem.

![mkfs output](../assets/screenshots/13-disks-storage/mkfs.png)

## Syntax

```bash
mkfs.TYP [OPTION]... GERÄT
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `mkfs.ext4 GERÄT` | Ein ext4-Dateisystem anlegen |
| `mkfs.xfs GERÄT` | Ein XFS-Dateisystem anlegen |
| `-L LABEL` | Dem Dateisystem einen Namen geben |
| `-m 1` | ext4: nur 1 % statt 5 % für root reservieren (sinnvoll für Datenplatten) |
| `-f` | XFS: ein vorhandenes Dateisystem überschreiben |
| `-n` | ext4: nur zeigen, was passieren würde |

## Beispiele

**Ein ext4-Dateisystem mit Label anlegen:**

```bash
sudo mkfs.ext4 -L archive /dev/sdd1
```

```text
mke2fs 1.47.2 (1-Jan-2025)
Discarding device blocks: done
Creating filesystem with 13106688 4k blocks and 3276800 inodes
Filesystem UUID: 5b8e2d71-9c4f-4a36-b1e7-0d3f6a2c8e94
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
        4096000, 7962624, 11239424

Allocating group tables: done
Writing inode tables: done
Creating journal (65536 blocks): done
Writing superblocks and filesystem accounting information: done
```

**Ein XFS-Dateisystem anlegen (Standard unter RHEL):**

```bash
sudo mkfs.xfs -L archive /dev/sdd1
```

```text
meta-data=/dev/sdd1              isize=512    agcount=4, agsize=3276672 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=1
         =                       reflink=1    bigtime=1 inobtcount=1 nrext64=1
         =                       exchange=0   metadir=0
data     =                       bsize=4096   blocks=13106688, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1, parent=0
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
         =                       rgcount=0    rgsize=0 extents
Discarding blocks...Done.
```

**Schutz vor dem Formatieren der falschen Partition:**

```bash
sudo mkfs.ext4 /dev/sdb1
```

```text
mke2fs 1.47.2 (1-Jan-2025)
/dev/sdb1 contains a ext4 file system labelled 'backup'
        last mounted on /mnt/backup on Mon Oct 26 03:00:12 2026
Proceed anyway? (y,N) n
```

`/dev/sdb1` ist die Backup-Platte. Die Antwort `n` hat die Daten gerettet.

## Wann brauche ich das?

- Nach dem Partitionieren einer neuen Platte, vor dem Einhängen
- Für ein neues logisches Volume von LVM
- Um eine Datenplatte komplett zu leeren und neu anzufangen

!!! tip "Nach dem Formatieren prüfen"
    [`blkid`](blkid.md) zeigt die neue UUID. Du brauchst sie für die Zeile in `/etc/fstab`.

!!! danger "Formatieren löscht alles"
    `mkfs` zerstört alle Daten auf dem Gerät, ohne Sicherung und ohne Rückgängig. ext4 fragt
    nach, wenn es ein vorhandenes Dateisystem findet, XFS weigert sich ohne `-f`. Nimm diese
    Warnungen ernst.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| ext4-Werkzeuge | `e2fsprogs`, installiert | `e2fsprogs`, installiert | `e2fsprogs`, installiert | `e2fsprogs`, installiert |
| XFS-Werkzeuge | `xfsprogs`, nicht installiert | `xfsprogs`, installiert | `xfsprogs`, installiert | `xfsprogs`, nicht installiert |

## Verwandte Befehle

[fdisk](fdisk.md) · [blkid](blkid.md) · [mount](mount.md) · [mkswap](mkswap.md)
