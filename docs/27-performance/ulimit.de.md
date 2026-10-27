# ulimit

> Zeigt und setzt die Ressourcengrenzen der Shell und der daraus gestarteten Prozesse, vor allem die Zahl offener Dateien.

![ulimit output](../assets/screenshots/27-performance/ulimit.png)

## Syntax

```bash
ulimit [-a] [-H | -S] [-n | -u | -c | -v] [WERT]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-a` | Alle Grenzen zeigen |
| `-n` | Maximal offene Dateien (Dateideskriptoren) |
| `-u` | Maximale Prozesse des Benutzers |
| `-c` | Maximale Größe von Core-Dumps |
| `-S`, `-H` | Soft Limit (aktuell) oder Hard Limit (Obergrenze für das Soft Limit) |
| `WERT` | Neuer Wert, etwa `65535` oder `unlimited` |

`ulimit` ist ein Shell-Builtin und gilt nur für die aktuelle Shell. Dauerhafte Grenzen für Anmeldungen stehen in `/etc/security/limits.conf`, für Dienste in der systemd-Unit (`LimitNOFILE=`).

## Beispiele

**Alle Grenzen der Shell:**

```bash
ulimit -a
```

```text
real-time non-blocking time  (microseconds, -R) unlimited
core file size              (blocks, -c) 0
data seg size               (kbytes, -d) unlimited
scheduling priority                 (-e) 0
file size                   (blocks, -f) unlimited
pending signals                     (-i) 15419
max locked memory           (kbytes, -l) 501304
max memory size             (kbytes, -m) unlimited
open files                          (-n) 1024
pipe size                (512 bytes, -p) 8
POSIX message queues         (bytes, -q) 819200
real-time priority                  (-r) 0
stack size                  (kbytes, -s) 8192
cpu time                   (seconds, -t) unlimited
max user processes                  (-u) 15419
virtual memory              (kbytes, -v) unlimited
file locks                          (-x) unlimited
```

**Die Grenze eines laufenden Dienstes:**

```bash
grep 'open files' /proc/$(pidof -s nginx)/limits
```

```text
Max open files            1024                 524288               files
```

**Die Grenze für einen Dienst dauerhaft erhöhen:**

```bash
sudo mkdir -p /etc/systemd/system/nginx.service.d
printf '[Service]\nLimitNOFILE=65535\n' | sudo tee /etc/systemd/system/nginx.service.d/limits.conf
sudo systemctl daemon-reload && sudo systemctl restart nginx
grep 'open files' /proc/$(pidof -s nginx)/limits
```

```text
[Service]
LimitNOFILE=65535
Max open files            65535                65535                files
```

**Das Soft Limit in der aktuellen Shell erhöhen:**

```bash
ulimit -n 4096
ulimit -Sn; ulimit -Hn
```

```text
4096
524288
```

## Wann brauche ich das?

- Wenn ein Dienst `Too many open files` protokolliert
- Um die Grenzen eines laufenden Prozesses zu prüfen: `cat /proc/PID/limits`
- Um Core-Dumps zur Fehlersuche bei einem abstürzenden Programm zu erlauben

!!! tip "Dienste: systemd nutzen"
    Grenzen aus `limits.conf` gelten nicht für systemd-Dienste. Setz sie in der Unit, etwa
    mit `sudo systemctl edit nginx` und `[Service]` `LimitNOFILE=65535`, und starte den Dienst
    neu.

## Verwandte Befehle

[sysctl](sysctl.md) · [systemctl](../09-systemd/systemctl.md) · [lsof](../08-processes/lsof.md)
