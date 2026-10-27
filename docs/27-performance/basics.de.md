# Leistung verstehen

„Der Server ist langsam“ hat immer eine Ursache in einer von vier Ressourcen. Die Kunst ist,
herauszufinden, welche an ihrer Grenze ist, statt zu raten.

## Die vier Ressourcen

| Ressource | Anzeichen | Erster Blick | Im Detail |
|-----------|-----------|--------------|-----------|
| **CPU** | Hohe Last, `us` oder `sy` nahe 100 % | [`top`](../08-processes/top.md), [`vmstat`](vmstat.md) | [`sar -u`](sar.md), `mpstat -P ALL` |
| **Speicher** | Swap wird genutzt, `si`/`so` nicht null, OOM-Killer im Log | [`free`](../08-processes/free.md), [`vmstat`](vmstat.md) | [`sar -r`](sar.md), `sar -W` |
| **Platten-I/O** | Hohes `wa` (I/O-Wait), langsame Antworten, obwohl die CPU frei ist | [`vmstat`](vmstat.md), Spalte `wa` | [`iostat -x`](iostat.md), [`iotop`](iotop.md) |
| **Netzwerk** | Timeouts, Neuübertragungen | [`ss -s`](../11-network/ss.md) | `sar -n DEV`, `sar -n TCP,ETCP` |

## Die Last richtig lesen

```text
load average: 3.12, 1.85, 0.97
               │     │     └─ average of the last 15 minutes
               │     └─ last 5 minutes
               └─ last minute
```

Die Last zählt Prozesse, die laufen oder warten, auf die CPU **und** auf die Platte.
Vergleiche sie mit der Zahl der CPU-Kerne (`nproc`): Auf `tuxdex-srv` mit 2 Kernen heißt
eine Last von 2 voll ausgelastet, 3 heißt, Prozesse warten. Hohe Last bei freier CPU deutet
auf Platten-I/O hin.

## Die USE-Methode

Prüfe für jede Ressource drei Dinge:

| | Frage | Beispiel |
|---|-------|----------|
| **U**tilization (Auslastung) | Wie beschäftigt ist sie? | `%util` einer Platte in `iostat` |
| **S**aturation (Sättigung) | Wartet Arbeit? | Warteschlange `r` in `vmstat`, `aqu-sz` in `iostat` |
| **E**rrors (Fehler) | Gibt es Fehler? | `dmesg`, `journalctl -k`, `smartctl` |

## In die Vergangenheit schauen

`top` und `vmstat` zeigen nur das Jetzt. War der Server um 3 Uhr nachts langsam, helfen nur
Daten, die im Hintergrund gesammelt wurden. Das Paket `sysstat` zeichnet alle 10 Minuten
CPU, Speicher, Platten und Netzwerk auf; [`sar`](sar.md) liest das hinterher aus.

## Was du installieren musst

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| vmstat, sysctl | vorinstalliert (`procps`) | vorinstalliert (`procps`) | vorinstalliert (`procps-ng`) | vorinstalliert (`procps-ng`) |
| iostat, sar, mpstat | `sudo apt install sysstat` | `sudo apt install sysstat` | `sudo dnf install sysstat` | `sudo pacman -S sysstat` |
| Sammeln im Hintergrund für sar | `/etc/default/sysstat`: `ENABLED="true"` | `/etc/default/sysstat`: `ENABLED="true"` | `sudo systemctl enable --now sysstat` | `sudo systemctl enable --now sysstat` |
| iotop | `sudo apt install iotop-c` | `sudo apt install iotop-c` | `sudo dnf install iotop` | `sudo pacman -S iotop-c` |
| lsmod, modprobe | vorinstalliert (`kmod`) | vorinstalliert (`kmod`) | vorinstalliert (`kmod`) | vorinstalliert (`kmod`) |

!!! tip "Erst messen, dann optimieren"
    Ändere Kernel-Parameter nur, wenn eine Messung einen Engpass zeigt, und ändere immer nur
    eine Sache. Die meisten Tuning-Anleitungen aus dem Internet sind für andere Kernel und
    andere Lasten geschrieben.

!!! warning "Freier Speicher ist nicht verschwendet"
    Linux nutzt ungenutzten Speicher als Cache (`buff/cache` in `free`). Ein Server mit
    wenig `free`, aber viel `available` ist in Ordnung. Eng wird es erst, wenn `available`
    sinkt und Swap aktiv genutzt wird.
