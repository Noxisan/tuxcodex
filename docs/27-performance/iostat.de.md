# iostat

> Zeigt, wie ausgelastet die Platten sind: Lese- und Schreibvorgänge pro Sekunde, Durchsatz, Wartezeiten und Auslastung.

![iostat output](../assets/screenshots/27-performance/iostat.png)

## Syntax

```bash
iostat [OPTIONEN] [GERÄT...] [INTERVALL [ANZAHL]]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-x` | Erweiterte Statistik mit Wartezeiten und Auslastung |
| `-z` | Geräte ohne Aktivität ausblenden |
| `-m`, `-h` | Werte in MB oder menschenlesbar |
| `-d` | Nur Platten, ohne CPU-Zusammenfassung |
| `-p sda` | Auch die Partitionen einer Platte zeigen |
| `-y` | Den ersten Bericht überspringen (Durchschnitt seit dem Start) |

Die wichtigsten Spalten mit `-x`:

| Spalte | Bedeutung |
|--------|-----------|
| `r/s`, `w/s` | Lese- und Schreibvorgänge pro Sekunde |
| `rkB/s`, `wkB/s` | Durchsatz |
| `r_await`, `w_await` | Durchschnittliche Wartezeit pro Vorgang in Millisekunden |
| `aqu-sz` | Durchschnittliche Länge der Warteschlange |
| `%util` | Anteil der Zeit, in der das Gerät beschäftigt war |

## Beispiele

**Durchsatz in MB seit dem Start:**

```bash
iostat -dm
```

```text
Linux 6.12.48+deb13-amd64 (tuxdex-srv)   10/26/2026   _x86_64_  (2 CPU)

Device             tps    MB_read/s    MB_wrtn/s    MB_dscd/s    MB_read    MB_wrtn    MB_dscd
sda               4.18         0.04         0.21         0.00      42611     223904          0
sdb               1.02         0.06         0.18         0.00      61290     190341          0
sdc               0.84         0.01         0.05         0.00      10248      52867          0
```

**Die beschäftigte Platte finden:**

```bash
iostat -dxzy 2 1
```

```text
Linux 6.12.48+deb13-amd64 (tuxdex-srv)   10/26/2026   _x86_64_  (2 CPU)

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
sda              2.50     40.00     0.00   0.00    0.80    16.00   18.00    196.00     6.50  26.53    1.42    10.89    0.00      0.00     0.00   0.00    0.00     0.00    1.00    0.50    0.03   2.60
sdb            412.00  52736.00     0.00   0.00   11.84   128.00  188.50  24128.00     0.00   0.00   38.10   128.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00   12.06  99.80
```

`sdb` (die Backup-Platte unter `/mnt/backup`) ist ständig beschäftigt und hat lange Wartezeiten, `sda` mit dem System ist ruhig. Hier läuft gerade ein Backup.

**CPU-Zusammenfassung mit I/O-Wait:**

```bash
iostat -c 2 2 | tail -3
```

```text
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           5.82    0.00    8.94   47.61    0.00   37.63
```

## Wann brauche ich das?

- Wenn `vmstat` ein hohes `wa` zeigt und du wissen musst, welche Platte beschäftigt ist
- Um zu prüfen, ob eine Platte oder ein Speichersystem einfach zu langsam ist (`await`)
- Während Backups oder Datenbankwartung, um die Last auf den Platten zu sehen

!!! tip "%util bei SSDs"
    SSDs und NVMe-Platten bearbeiten viele Anfragen parallel. `%util` nahe 100 heißt bei
    ihnen nicht, dass sie am Limit sind; schau stattdessen auf `r_await` und `w_await`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install sysstat` | `sudo apt install sysstat` | `sudo dnf install sysstat` | `sudo pacman -S sysstat` |

## Verwandte Befehle

[vmstat](vmstat.md) · [iotop](iotop.md) · [sar](sar.md) · [smartctl](../13-disks-storage/smartctl.md)
