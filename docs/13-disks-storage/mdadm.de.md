# mdadm

> Legt Software-RAIDs an und verwaltet sie: Platten spiegeln, den Zustand prüfen und eine ausgefallene Platte tauschen.

![mdadm output](../assets/screenshots/13-disks-storage/mdadm.png)

## Syntax

```bash
mdadm --create /dev/mdN --level=LEVEL --raid-devices=N GERÄT...
mdadm --detail /dev/mdN
mdadm /dev/mdN --fail | --remove | --add GERÄT
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--create`, `-C` | Ein neues Array anlegen |
| `--level=`, `-l` | RAID-Level: `1`, `5`, `6`, `10` oder `0` |
| `--raid-devices=`, `-n` | Anzahl der aktiven Platten im Array |
| `--detail`, `-D` | Zustand, Platten und UUID eines Arrays zeigen |
| `--detail --scan` | Eine `ARRAY`-Zeile pro Array, für `mdadm.conf` |
| `--fail`, `--remove`, `--add` | Eine Platte als defekt markieren, herausnehmen, eine neue hinzufügen |
| `--examine`, `-E` | Den RAID-Superblock auf einer einzelnen Platte zeigen |
| `--zero-superblock` | Den RAID-Superblock von einer nicht mehr genutzten Platte löschen |

Den Zustand aller Arrays zeigt der Kernel in `/proc/mdstat`. `[UU]` heißt, alle Platten laufen, `[U_]`, dass eine fehlt.

## Beispiele

**Der Zustand aller Arrays:**

```bash
cat /proc/mdstat
```

```text
Personalities : [raid1]
md0 : active raid1 sde[1] sdd[0]
      20954112 blocks super 1.2 [2/2] [UU]

unused devices: <none>
```

**Zwei neue Platten spiegeln (RAID 1):**

```bash
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdd /dev/sde
```

```text
mdadm: Note: this array has metadata at the start and
    may not be suitable as a boot device.  If you plan to
    store '/boot' on this device please ensure that
    your boot-loader understands md/v1.x metadata, or use
    --metadata=0.90
mdadm: size set to 20954112K
Continue creating array? y
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.
```

Das Array ist sofort nutzbar. Im Hintergrund kopiert der Kernel die erste Platte auf die zweite; `/proc/mdstat` zeigt den Fortschritt. Danach legst du mit `sudo mkfs.ext4 /dev/md0` ein Dateisystem an.

**Details eines Arrays:**

```bash
sudo mdadm --detail /dev/md0
```

```text
/dev/md0:
           Version : 1.2
     Creation Time : Mon Oct 26 10:42:17 2026
        Raid Level : raid1
        Array Size : 20954112 (19.98 GiB 21.46 GB)
     Used Dev Size : 20954112 (19.98 GiB 21.46 GB)
      Raid Devices : 2
     Total Devices : 2
       Persistence : Superblock is persistent

       Update Time : Mon Oct 26 10:44:03 2026
             State : clean
    Active Devices : 2
   Working Devices : 2
    Failed Devices : 0
     Spare Devices : 0

Consistency Policy : resync

              Name : tuxdex-srv:0  (local to host tuxdex-srv)
              UUID : 3f8a2c1e:9b47d6a0:5e21c8f4:7d03b9e2
            Events : 17

    Number   Major   Minor   RaidDevice State
       0       8       48        0      active sync   /dev/sdd
       1       8       64        1      active sync   /dev/sde
```

**Das Array speichern, damit es beim Booten denselben Namen bekommt:**

```bash
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
sudo update-initramfs -u
```

```text
ARRAY /dev/md0 metadata=1.2 name=tuxdex-srv:0 UUID=3f8a2c1e:9b47d6a0:5e21c8f4:7d03b9e2
update-initramfs: Generating /boot/initrd.img-6.12.48+deb13-amd64
```

**Eine Platte ist ausgefallen:**

```bash
cat /proc/mdstat
```

```text
Personalities : [raid1]
md0 : active raid1 sde[1](F) sdd[0]
      20954112 blocks super 1.2 [2/1] [U_]

unused devices: <none>
```

`(F)` markiert die defekte Platte, `[U_]` zeigt, dass das Array nur noch auf einer Platte läuft. Die Daten sind noch da.

**Die defekte Platte herausnehmen und die neue hinzufügen:**

```bash
sudo mdadm /dev/md0 --remove /dev/sde
# swap the disk, then:
sudo mdadm /dev/md0 --add /dev/sde
cat /proc/mdstat
```

```text
mdadm: hot removed /dev/sde from /dev/md0
mdadm: added /dev/sde
Personalities : [raid1]
md0 : active raid1 sde[2] sdd[0]
      20954112 blocks super 1.2 [2/1] [U_]
      [====>................]  recovery = 23.6% (4946304/20954112) finish=1.3min speed=203472K/sec

unused devices: <none>
```

Während der `recovery` bleibt das Array nutzbar. Ist sie fertig, zeigt `/proc/mdstat` wieder `[UU]`.

## Wann brauche ich das?

- Um zwei Datenplatten zu spiegeln, damit der Server weiterläuft, wenn eine ausfällt
- Um nach einer Warnmail oder in einem Monitoring-Skript den Zustand eines Arrays zu prüfen
- Um eine defekte Platte zu tauschen und das Array neu aufzubauen

!!! tip "Mails bei Plattenausfall"
    Der Dienst `mdmonitor` überwacht alle Arrays und schickt Mails an die Adresse aus
    `MAILADDR` in `mdadm.conf`. Zum Testen: `sudo mdadm --monitor --scan --test --oneshot`
    schickt für jedes Array eine Testmail.

!!! warning "RAID ist kein Backup"
    Ein Spiegel schützt vor einer defekten Platte, nicht vor `rm -rf`, Ransomware oder einem
    kaputten Dateisystem: Das wird sofort mitgespiegelt. Ein Backup brauchst du trotzdem.

!!! danger "`--create` überschreibt die Platten"
    `mdadm --create` schreibt neue Superblöcke auf die genannten Platten. Prüf die
    Gerätenamen vorher mit `lsblk`: Ein falscher Buchstabe zerstört die Daten einer anderen
    Platte.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install mdadm` | auf Ubuntu Server vorinstalliert | `sudo dnf install mdadm` | `sudo pacman -S mdadm` |
| Konfigurationsdatei | `/etc/mdadm/mdadm.conf` | `/etc/mdadm/mdadm.conf` | `/etc/mdadm.conf` | `/etc/mdadm.conf` |
| initramfs aktualisieren | `update-initramfs -u` | `update-initramfs -u` | `dracut -f` | `mkinitcpio -P` (Hook `mdadm_udev`) |

## Verwandte Befehle

[lsblk](lsblk.md) · [mkfs](mkfs.md) · [mount](mount.md) · [smartctl](smartctl.md) · [pvs](pvs.md)
