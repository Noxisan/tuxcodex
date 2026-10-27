# iotop

> Zeigt live, welche Prozesse auf den Platten lesen und schreiben, wie top, aber für Platten-I/O.

![iotop output](../assets/screenshots/27-performance/iotop.png)

## Syntax

```bash
iotop [-o] [-a] [-b] [-n ANZAHL] [-d SEKUNDEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-o`, `--only` | Nur Prozesse, die gerade lesen oder schreiben |
| `-a`, `--accumulated` | Das I/O seit dem Start aufaddieren, statt Raten zu zeigen |
| `-P`, `--processes` | Prozesse statt einzelner Threads |
| `-b`, `--batch` | Einfache Textausgabe, für Logs und Skripte |
| `-n ANZAHL`, `-d SEKUNDEN` | Anzahl der Aktualisierungen, Intervall |

In `iotop`: ++o++ schaltet „nur aktive“ um, ++a++ aufaddierte Werte, ++left++ und ++right++ wechseln die Sortierspalte, ++q++ beendet.

## Beispiele

**Nur Prozesse, die gerade I/O verursachen:**

```bash
sudo iotop -o -P -b -n 1
```

```text
Total DISK READ:        51.41 M/s | Total DISK WRITE:        23.56 M/s
Current DISK READ:      51.41 M/s | Current DISK WRITE:      23.62 M/s
    PID  PRIO  USER     DISK READ  DISK WRITE>    COMMAND
  48211 be/4 root       51.38 M/s   23.51 M/s tar --zstd -cf /mnt/backup/www-2026-10-26.tar.zst -C /srv www
    905 be/4 postgres    0.00 B/s   42.10 K/s postgres: walwriter
    812 be/4 root        0.00 B/s    4.00 K/s nginx: master process /usr/sbin/nginx
```

Das Backup mit `tar` verursacht fast das gesamte I/O. Mit `nice` und `ionice -c3` gestartet, lässt es andere Prozesse vor.

**Wer seit dem Start am meisten geschrieben hat:**

```bash
sudo iotop -a -o -P -b -n 3 -d 5 | tail -4
```

```text
    PID  PRIO  USER     DISK READ  DISK WRITE>    COMMAND
    905 be/4 postgres    0.00 B     18.42 M postgres: checkpointer
   1310 be/4 www-data    0.00 B      6.13 M php-fpm: pool www
    640 be/4 root        0.00 B     32.00 K sshd: nox [priv]
```

## Wann brauche ich das?

- Wenn `iostat` eine beschäftigte Platte zeigt und du wissen musst, welcher Prozess dahintersteckt
- Um eine ausufernde Logdatei oder ein Backup zu finden, das alles ausbremst
- Um zu prüfen, wie viel eine Datenbank oder ein Container über die Zeit schreibt (`-a`)

!!! tip "iotop-c statt des alten iotop"
    Das ursprüngliche `iotop` ist ein Python-Programm und wird nicht mehr gepflegt. `iotop-c`
    ist ein kompatibler Nachbau in C und wird auf vielen Distributionen als `iotop`
    installiert.

!!! warning "Braucht root"
    iotop braucht Root-Rechte (oder die Capability `CAP_NET_ADMIN`), um die I/O-Statistik
    anderer Prozesse zu lesen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install iotop-c` | `sudo apt install iotop-c` | `sudo dnf install iotop` | `sudo pacman -S iotop-c` |

## Verwandte Befehle

[iostat](iostat.md) · [vmstat](vmstat.md) · [nice](../08-processes/nice.md) · [top](../08-processes/top.md)
