# htop

> Die komfortablere Variante von `top`: farbige Balken, Scrollen, Mausbedienung, Suche, Baumansicht und Prozesse mit wenigen Tasten beenden.

![htop output](../assets/screenshots/08-processes/htop.png)

## Syntax

```bash
htop [OPTION]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-u BENUTZER` | Nur Prozesse von `BENUTZER` anzeigen |
| `-p PID,PID` | Nur diese Prozesse anzeigen |
| `-t`, `--tree` | In der Baumansicht starten |
| `-s SPALTE` | Nach dieser Spalte sortieren, z. B. `PERCENT_MEM` |
| `-d ZEHNTEL` | Aktualisierungsintervall in Zehntelsekunden |

Tasten innerhalb von `htop`:

| Taste | Aktion |
|-------|--------|
| ++f3++ / ++slash++ | Nach einem Prozess suchen |
| ++f4++ / ++backslash++ | Filtern: nur passende Prozesse zeigen |
| ++f5++ / ++t++ | Baumansicht ein- und ausschalten |
| ++f6++ | Sortierspalte wählen |
| ++f9++ / ++k++ | Ein Signal an den markierten Prozess senden |
| ++space++ | Prozesse markieren, um mehreren auf einmal ein Signal zu senden |
| ++f10++ / ++q++ | Beenden |

## Beispiele

**`htop` starten:**

```bash
htop
```

```text
    0[||                         2.1%]   Tasks: 48, 112 thr, 87 kthr; 1 running
    1[|                          0.7%]   Load average: 0.08 0.03 0.01
  Mem[||||||||||||||       1.18G/3.82G]   Uptime: 12 days, 03:05:21
  Swp[                        0K/1024M]

    PID USER       PRI  NI  VIRT   RES   SHR S  CPU% MEM%   TIME+  Command
    905 postgres    20   0  216M  160M  147M S   0.7  4.1  2:14.31 postgres
   1310 www-data    20   0  239M 90048 62544 S   0.3  2.3  0:42.07 php-fpm: pool www
```

Oben ein Balken pro CPU-Kern sowie Arbeitsspeicher und Swap. Darunter die Prozessliste
wie bei [`top`](top.md).

**Nur die Prozesse eines Benutzers anzeigen:**

```bash
htop -u www-data
```

```text
    PID USER       PRI  NI  VIRT   RES   SHR S  CPU% MEM%   TIME+  Command
   1310 www-data    20   0  239M 90048 62544 S   0.3  2.3  0:42.07 php-fpm: pool www
    813 www-data    20   0 12968  5876  3912 S   0.0  0.1  0:03.12 nginx: worker process
```

**In der Baumansicht starten:**

```bash
htop -t
```

```text
    PID USER       PRI  NI  VIRT   RES   SHR S  CPU% MEM%   TIME+  Command
    812 root        20   0 11360  1820   920 S   0.0  0.0  0:00.01 nginx: master process
    813 www-data    20   0 12968  5876  3912 S   0.0  0.1  0:03.12 ├─ nginx: worker process
    814 www-data    20   0 12968  5852  3908 S   0.0  0.1  0:03.08 └─ nginx: worker process
```

## Wann brauche ich das?

- Wenn ein Server langsam ist und du auf einen Blick sehen willst, welche Kerne und
  Prozesse beschäftigt sind
- Um Prozesse schnell zu finden, zu filtern und zu beenden, auch mehrere auf einmal
- Um in der Baumansicht den Aufbau von Diensten zu verstehen

!!! tip "Filtern statt suchen"
    ++f4++ und ein Wort wie `php` blenden alles andere aus. Du siehst dann nur die
    Prozesse, die dich interessieren, und der Filter bleibt aktiv, während `htop`
    aktualisiert.

!!! warning "Nicht auf jedem Server"
    `htop` ist auf den meisten Distributionen nicht vorinstalliert und unter RHEL nur im
    EPEL-Repository zu finden. [`top`](top.md) ist immer da.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Standardmäßig installiert | nein | ja (Server) | nein | nein |
| Installieren | `sudo apt install htop` | `sudo apt install htop` | aus EPEL: `sudo dnf install epel-release`, dann `sudo dnf install htop` | `sudo pacman -S htop` |

## Verwandte Befehle

[top](top.md) · [ps](ps.md)
