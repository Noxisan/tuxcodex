# smartctl

> Liest die Selbstüberwachungsdaten (S.M.A.R.T.) von Festplatten und SSDs aus und startet Selbsttests. Warnt früh, wenn eine Platte bald ausfällt.

![smartctl output](../assets/screenshots/13-disks-storage/smartctl.png)

## Syntax

```bash
smartctl [OPTION]... GERÄT
```

Das Paket heißt `smartmontools`. Es enthält auch den Dienst `smartd`, der die Platten regelmäßig prüft und Mails schicken kann.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-H` | Gesamtzustand: `PASSED` oder `FAILED` |
| `-i` | Modell, Seriennummer, Kapazität |
| `-A` | Die SMART-Attribute, z. B. umgelagerte Sektoren und Temperatur |
| `-a` | Alles auf einmal |
| `-t short`, `-t long` | Einen kurzen oder langen Selbsttest starten |
| `-l selftest` | Ergebnisse der letzten Selbsttests |

## Beispiele

**Den Gesamtzustand einer Platte prüfen:**

```bash
sudo smartctl -H /dev/sda
```

```text
smartctl 7.4 2023-08-01 r5530 [x86_64-linux-6.12.48+deb13-amd64] (local build)
Copyright (C) 2002-23, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED
```

**Modell und Seriennummer anzeigen:**

```bash
sudo smartctl -i /dev/sda
```

```text
smartctl 7.4 2023-08-01 r5530 [x86_64-linux-6.12.48+deb13-amd64] (local build)
Copyright (C) 2002-23, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Model Family:     Samsung based SSDs
Device Model:     Samsung SSD 870 EVO 1TB
Serial Number:    S6PUNX0T812345K
User Capacity:    1,000,204,886,016 bytes [1.00 TB]
Rotation Rate:    Solid State Device
SMART support is: Available - device has SMART capability.
SMART support is: Enabled
```

**Die wichtigsten Attribute anzeigen:**

```bash
sudo smartctl -A /dev/sda
```

```text
smartctl 7.4 2023-08-01 r5530 [x86_64-linux-6.12.48+deb13-amd64] (local build)
Copyright (C) 2002-23, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF READ SMART DATA SECTION ===
SMART Attributes Data Structure revision number: 1
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  5 Reallocated_Sector_Ct   0x0033   100   100   010    Pre-fail  Always       -       0
  9 Power_On_Hours          0x0032   097   097   000    Old_age   Always       -       12842
 12 Power_Cycle_Count       0x0032   099   099   000    Old_age   Always       -       43
177 Wear_Leveling_Count     0x0013   098   098   000    Pre-fail  Always       -       21
194 Temperature_Celsius     0x0022   066   052   000    Old_age   Always       -       34
199 UDMA_CRC_Error_Count    0x003e   100   100   000    Old_age   Always       -       0
```

`RAW_VALUE` ist der echte Wert: 12842 Betriebsstunden, 34 °C, keine umgelagerten Sektoren.

**Einen kurzen Selbsttest starten:**

```bash
sudo smartctl -t short /dev/sda
```

```text
smartctl 7.4 2023-08-01 r5530 [x86_64-linux-6.12.48+deb13-amd64] (local build)
Copyright (C) 2002-23, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF OFFLINE IMMEDIATE AND SELF-TEST SECTION ===
Sending command: "Execute SMART Short self-test routine immediately in off-line mode".
Drive command "Execute SMART Short self-test routine immediately in off-line mode" successful.
Testing has begun.
Please wait 2 minutes for test to complete.
Test will complete after Mon Oct 26 10:44:17 2026 CET
Use smartctl -X to abort test.
```

**Auf einem virtuellen Server:**

```bash
sudo smartctl -i /dev/sda
```

```text
smartctl 7.4 2023-08-01 r5530 [x86_64-linux-6.12.48+deb13-amd64] (local build)
Copyright (C) 2002-23, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Vendor:               QEMU
Product:              QEMU HARDDISK
Revision:             2.5+
User Capacity:        42,949,672,960 bytes [42.9 GB]
Logical block size:   512 bytes
Device type:          disk
Local Time is:        Mon Oct 26 10:42:17 2026 CET
SMART support is:     Unavailable - device lacks SMART capability.
```

## Wann brauche ich das?

- Auf physischen Servern, um sterbende Platten zu bemerken, bevor Daten verloren gehen
- Wenn eine Platte in `journalctl -k` Lesefehler meldet
- Bevor du eine alte Platte wiederverwendest

!!! tip "Auf diese Attribute achten"
    `Reallocated_Sector_Ct`, `Current_Pending_Sector` und `Offline_Uncorrectable` sollten `0`
    sein. Steigen sie, tausche die Platte bald aus, auch wenn der Gesamtzustand noch `PASSED`
    meldet.

!!! warning "Nicht auf virtuellen Servern"
    Virtuelle Platten haben keine SMART-Daten. Auf einer VM oder einem Cloud-Server überwacht
    der Hoster die physischen Platten.

## Verwandte Befehle

[lsblk](lsblk.md) · [journalctl](../09-systemd/journalctl.md)
