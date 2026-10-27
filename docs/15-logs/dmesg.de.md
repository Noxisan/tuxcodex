# dmesg

> Zeigt die Meldungen des Kernels: Hardwareerkennung, Treiberfehler, Platten, Netzwerkkarten und den OOM-Killer.

![dmesg output](../assets/screenshots/15-logs/dmesg.png)

## Syntax

```bash
dmesg [OPTION]...
```

Unter Debian und Ubuntu braucht das Lesen der Kernelmeldungen root: `sudo dmesg`. `journalctl -k` zeigt dieselben Meldungen, auch aus früheren Bootvorgängen.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-T` | Lesbare Zeitstempel statt Sekunden seit dem Booten |
| `-l LEVEL` | Nur diese Level, z. B. `err,warn` |
| `-w` | Neue Meldungen live verfolgen |
| `-H` | Lesbare Ausgabe mit Farben und Pager |
| `-c` | Ausgeben und den Puffer leeren (root) |

## Beispiele

**Nur Fehler und Warnungen anzeigen:**

```bash
sudo dmesg -T -l err,warn
```

```text
[Wed Oct 14 07:37:09 2026] ACPI Error: AE_NOT_FOUND, While resolving a named reference package element (20240827/dspkginit-438)
[Mon Oct 26 03:12:44 2026] php-fpm8.4 invoked oom-killer: gfp_mask=0x140cca(GFP_HIGHUSER_MOVABLE|__GFP_COMP), order=0, oom_score_adj=0
[Mon Oct 26 03:12:44 2026] Out of memory: Killed process 1314 (php-fpm8.4) total-vm:812344kB, anon-rss:612480kB, file-rss:0kB, shmem-rss:0kB, UID:33 pgtables:1436kB oom_score_adj:0
```

**Prüfen, ob eine neue Platte erkannt wurde:**

```bash
sudo dmesg -T | grep sdd
```

```text
[Mon Oct 26 10:40:51 2026] sd 2:0:0:3: [sdd] 104857600 512-byte logical blocks: (53.7 GB/50.0 GiB)
[Mon Oct 26 10:40:51 2026] sd 2:0:0:3: [sdd] Write Protect is off
[Mon Oct 26 10:40:51 2026] sd 2:0:0:3: [sdd] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[Mon Oct 26 10:40:51 2026] sd 2:0:0:3: [sdd] Attached SCSI disk
```

**Ohne Root-Rechte:**

```bash
dmesg
```

```text
dmesg: read kernel buffer failed: Operation not permitted
```

## Wann brauche ich das?

- Nach dem Anschließen einer Platte oder eines USB-Geräts: Wurde es erkannt, und unter welchem Namen?
- Wenn Prozesse verschwinden: Hat der OOM-Killer sie beendet?
- Bei Hardwareproblemen wie Platten- oder Netzwerkfehlern

!!! tip "Kernelmeldungen des letzten Bootvorgangs"
    `dmesg` kennt nur den aktuellen Bootvorgang. Nach einem Absturz zeigt `journalctl -k -b -1`
    die Kernelmeldungen von vor dem Neustart.

!!! warning "OOM-Killer heißt: zu wenig Arbeitsspeicher"
    `Out of memory: Killed process` bedeutet, dass der Kernel einen Prozess beendet hat, weil der
    Arbeitsspeicher ausging. Such die Ursache mit [`free`](../08-processes/free.md) und [`top`](../08-processes/top.md), statt nur den Dienst neu zu
    starten.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Ohne root lesbar | nein | nein | ja | abhängig von `kernel.dmesg_restrict` |

## Verwandte Befehle

[journalctl](../09-systemd/journalctl.md) · [lsblk](../13-disks-storage/lsblk.md) · [free](../08-processes/free.md)
