# parted

> Legt Partitionen an, ändert und vergrößert sie, auch in einer einzigen Befehlszeile. Für Skripte besser geeignet als `fdisk`.

![parted output](../assets/screenshots/13-disks-storage/parted.png)

## Syntax

```bash
parted [OPTION]... GERÄT [BEFEHL [ARGUMENT]...]
```

Anders als `fdisk` schreibt `parted` jede Änderung **sofort**, es gibt kein `w` am Ende.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `print` | Die Partitionstabelle anzeigen |
| `mklabel gpt` | Eine neue, leere GPT-Tabelle anlegen |
| `mkpart NAME FS START ENDE` | Eine Partition anlegen, z. B. `data ext4 1MiB 100%` |
| `resizepart N ENDE` | Das Ende von Partition `N` verschieben, z. B. auf `100%` |
| `rm N` | Partition `N` löschen |
| `unit MiB` | Größen in MiB anzeigen und eingeben |
| `-s` | Skriptmodus: keine Rückfragen |

## Beispiele

**Die Partitionen der Systemplatte anzeigen:**

```bash
sudo parted /dev/sda print
```

```text
Model: QEMU QEMU HARDDISK (scsi)
Disk /dev/sda: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system     Name  Flags
 1      1049kB  538MB   537MB   fat32                 boot, esp
 2      538MB   41.9GB  41.3GB  ext4
 3      41.9GB  42.9GB  1074MB  linux-swap(v1)        swap
```

**Eine neue Platte in einer Zeile partitionieren:**

```bash
sudo parted -s /dev/sdd mklabel gpt mkpart data ext4 1MiB 100%
sudo parted /dev/sdd print
```

```text
Model: QEMU QEMU HARDDISK (scsi)
Disk /dev/sdd: 53.7GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name  Flags
 1      1049kB  53.7GB  53.7GB               data
```

Die Spalte `File system` bleibt leer: `ext4` in `mkpart` ist nur ein Hinweis, das
Dateisystem selbst legt [`mkfs`](mkfs.md) an.

**Größen in MiB anzeigen:**

```bash
sudo parted /dev/sdd unit MiB print
```

```text
Model: QEMU QEMU HARDDISK (scsi)
Disk /dev/sdd: 51200MiB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start    End       Size      File system  Name  Flags
 1      1.00MiB  51199MiB  51198MiB               data
```

## Wann brauche ich das?

- Um Platten in Skripten oder Automatisierung zu partitionieren
- Um eine Partition zu vergrößern, nachdem die virtuelle Platte vergrößert wurde
- Für Platten über 2 TiB, die GPT brauchen

!!! tip "Bei `1MiB` beginnen"
    `1MiB` als Anfang und `100%` als Ende richtet die Partition richtig für SSDs und RAID aus
    und nutzt die ganze Platte.

!!! danger "Änderungen wirken sofort"
    `mklabel` auf einer genutzten Platte löscht ihre Partitionstabelle sofort, im Skriptmodus
    ohne zweite Rückfrage. Prüfe den Gerätenamen doppelt.

## Verwandte Befehle

[fdisk](fdisk.md) · [lsblk](lsblk.md) · [resize2fs](resize2fs.md)
