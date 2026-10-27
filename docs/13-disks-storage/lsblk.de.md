# lsblk

> Listet alle Blockgeräte als Baum auf: Platten, Partitionen, LVM-Volumes, mit Größe und Einhängepunkt.

![lsblk output](../assets/screenshots/13-disks-storage/lsblk.png)

## Syntax

```bash
lsblk [OPTION]... [GERÄT]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-f` | Dateisysteme zeigen: Typ, Label, UUID, freier Platz |
| `-o SPALTEN` | Die Spalten wählen, z. B. `NAME,SIZE,MODEL` |
| `-d` | Nur Platten, keine Partitionen |
| `-p` | Vollständige Pfade wie `/dev/sda1` zeigen |
| `-e 7` | Loop-Geräte ausschließen (Hauptnummer 7) |

## Beispiele

**Alle Platten und Partitionen anzeigen:**

```bash
lsblk
```

```text
NAME             MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                8:0    0   40G  0 disk
├─sda1             8:1    0  512M  0 part /boot/efi
├─sda2             8:2    0 38.5G  0 part /
└─sda3             8:3    0    1G  0 part [SWAP]
sdb                8:16   0  100G  0 disk
└─sdb1             8:17   0  100G  0 part /mnt/backup
sdc                8:32   0   50G  0 disk
└─vg_data-lv_srv 254:0    0   30G  0 lvm  /srv/data
sr0               11:0    1 1024M  0 rom
```

`sda` ist die Systemplatte mit drei Partitionen, `sdb` die Backup-Platte, und `sdc` gehört zu
LVM. `RM 1` markiert Wechseldatenträger wie das virtuelle DVD-Laufwerk `sr0`.

**Dateisysteme, UUIDs und freien Platz anzeigen:**

```bash
lsblk -f
```

```text
NAME             FSTYPE      FSVER    LABEL  UUID                                   FSAVAIL FSUSE% MOUNTPOINTS
sda
├─sda1           vfat        FAT32           4A1C-7F32                               505.8M     1% /boot/efi
├─sda2           ext4        1.0             c1f4e2a7-5b3d-4e8a-9f61-2d7b8c0e9a14     17.9G    47% /
└─sda3           swap        1               8e2b6d4f-1a3c-4f5e-b7d9-0c2e4a6f8b31                [SWAP]
sdb
└─sdb1           ext4        1.0      backup 87c6aa0c-cb18-455e-b534-d2864a90bb80     61.2G    33% /mnt/backup
sdc              LVM2_member LVM2 001        Qm3T9x-2kPa-7HcR-dL4e-Vn8s-Wf1y-Z6bJ0u
└─vg_data-lv_srv ext4        1.0      data   3d9f1b7e-6c2a-4e8d-a5f0-7b1c9e2d4f63     21.4G    23% /srv/data
```

**Nur die Platten mit Modell und Seriennummer:**

```bash
lsblk -d -e 7,11 -o NAME,SIZE,MODEL,SERIAL,TYPE
```

```text
NAME   SIZE MODEL           SERIAL       TYPE
sda     40G QEMU HARDDISK   drive-scsi0  disk
sdb    100G QEMU HARDDISK   drive-scsi1  disk
sdc     50G QEMU HARDDISK   drive-scsi2  disk
```

**Eine neu hinzugefügte Platte anzeigen:**

```bash
lsblk /dev/sdd
```

```text
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sdd    8:48   0  50G  0 disk
```

Keine Partitionen, kein Einhängepunkt: Die Platte ist leer und bereit für [`fdisk`](fdisk.md).

## Wann brauche ich das?

- Um sich einen Überblick über einen Server zu verschaffen: Welche Platten gibt es, und wie sind sie aufgeteilt?
- Nach dem Hinzufügen einer Platte, um ihren Namen zu finden
- Um die UUID oder das Dateisystem einer Partition zu finden

!!! tip "Die neue Platte finden"
    Eine neue Platte hat keine Partitionen und keinen Einhängepunkt. Vergleiche `lsblk`
    vor und nach dem Hinzufügen, die neue Zeile ist die neue Platte.

## Verwandte Befehle

[blkid](blkid.md) · [df](df.md) · [findmnt](findmnt.md) · [fdisk](fdisk.md) · [pvs](pvs.md)
