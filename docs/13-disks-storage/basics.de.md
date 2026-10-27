# Speicher verstehen

Bevor eine Platte Dateien speichern kann, durchläuft sie vier Schichten: die **Platte**
selbst, eine **Partitionstabelle**, die sie aufteilt, ein **Dateisystem** auf jeder
Partition und einen **Einhängepunkt**, an dem das Dateisystem im Verzeichnisbaum erscheint.

## Platten und Partitionen

Linux zeigt jede Platte als Datei in `/dev`:

| Name | Typisches Gerät |
|------|-----------------|
| `/dev/sda`, `/dev/sdb` | SATA- und SCSI-Platten, auch die meisten virtuellen Platten |
| `/dev/vda` | Virtuelle Platten mit virtio-Treiber (KVM, viele Cloud-Anbieter) |
| `/dev/nvme0n1` | NVMe-SSDs |
| `/dev/sda1`, `/dev/nvme0n1p1` | Die erste Partition auf dieser Platte |
| `/dev/mapper/vg_data-lv_srv` | Ein logisches Volume von LVM |

Auf dem Beispielserver `tuxdex-srv` hat die Systemplatte `sda` drei Partitionen, die
Backup-Platte `sdb` eine, und die Platte `sdc` gehört zu LVM.

## Partitionstabellen

| Typ | Größte Plattengröße | Partitionen | Einsatz |
|-----|---------------------|-------------|---------|
| **GPT** | praktisch unbegrenzt | 128 | Heute Standard, nötig für Platten über 2 TiB und für UEFI |
| **MBR** (DOS) | 2 TiB | 4 primäre | Alte Systeme und alter BIOS-Start |

Nimm für neue Platten GPT.

## Dateisysteme

| Dateisystem | Stärken | Vergrößern | Verkleinern |
|-------------|---------|------------|-------------|
| **ext4** | Robust, universell, der Klassiker unter Linux | ja, auch eingehängt | ja, nur ausgehängt |
| **XFS** | Sehr gut bei großen Dateien und vielen parallelen Zugriffen | ja, eingehängt | nein |
| **Btrfs** | Snapshots, Prüfsummen, Komprimierung, mehrere Platten | ja | ja |
| **vfat** | Überall lesbar, Pflicht für die EFI-Partition | selten | selten |
| **swap** | Kein Dateisystem: Auslagerungsspeicher für den Arbeitsspeicher | | |

## `/etc/fstab`: Einhängen beim Booten

Jede Zeile in `/etc/fstab` beschreibt ein Dateisystem, das beim Booten eingehängt wird:

```text
# <file system>                           <mount point> <type> <options>         <dump> <pass>
UUID=c1f4e2a7-5b3d-4e8a-9f61-2d7b8c0e9a14 /             ext4   errors=remount-ro 0      1
UUID=4A1C-7F32                            /boot/efi     vfat   umask=0077        0      1
UUID=8e2b6d4f-1a3c-4f5e-b7d9-0c2e4a6f8b31 none          swap   sw                0      0
UUID=87c6aa0c-cb18-455e-b534-d2864a90bb80 /mnt/backup   ext4   defaults,nofail   0      2
/dev/mapper/vg_data-lv_srv                /srv/data     ext4   defaults          0      2
```

| Feld | Bedeutung |
|------|-----------|
| Dateisystem | Welches Gerät. Nimm `UUID=` aus `blkid`, weil sich Namen wie `sdb` ändern können |
| Einhängepunkt | Wo es im Verzeichnisbaum erscheint |
| Optionen | `defaults`, dazu z. B. `nofail` (booten, auch wenn die Platte fehlt) oder `noatime` |
| Pass | Reihenfolge der Prüfung beim Booten: `1` für `/`, `2` für den Rest, `0` nie |

## LVM: flexible Volumes

LVM legt eine Schicht zwischen Platten und Dateisysteme:

| Schicht | Name | Befehl |
|---------|------|--------|
| Platten oder Partitionen | **Physical Volumes** (PV) | `pvs`, `pvcreate` |
| Pool aus einem oder mehreren PVs | **Volume Groups** (VG) | `vgs`, `vgcreate`, `vgextend` |
| „Partitionen“ aus dem Pool | **Logical Volumes** (LV) | `lvs`, `lvcreate`, `lvextend` |

Der große Vorteil: Wird ein Volume voll, fügst du der Volume Group eine Platte hinzu und
vergrößerst das logische Volume, während der Server weiterläuft.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Standard-Dateisystem des Installers | ext4 | ext4 | XFS | bei der Installation gewählt |
| LVM in der Standardinstallation | optional | ja | ja | nein |
| `/tmp` im Arbeitsspeicher (tmpfs) | ja, seit Debian 13 | nein | nein | ja |

!!! tip "UUIDs statt Gerätenamen"
    Die Reihenfolge der Platten kann sich nach einem Neustart oder beim Hinzufügen einer
    Platte ändern: Das `sdb` von gestern kann heute `sdc` sein. UUIDs in `/etc/fstab`
    zeigen immer auf das richtige Dateisystem.

!!! danger "`/etc/fstab` vor dem Neustart testen"
    Eine falsche Zeile in `/etc/fstab` kann den Bootvorgang anhalten. Führe nach jeder
    Änderung `sudo findmnt --verify` und `sudo mount -a` aus. Starte erst neu, wenn beide
    keine Fehler melden.
