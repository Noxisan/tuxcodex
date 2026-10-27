# Understanding performance

"The server is slow" always has a cause in one of four resources. The art is to find out
which one is at its limit, instead of guessing.

## The four resources

| Resource | Symptom | First look | In detail |
|----------|---------|------------|-----------|
| **CPU** | High load, `us` or `sy` near 100 % | [`top`](../08-processes/top.md), [`vmstat`](vmstat.md) | [`sar -u`](sar.md), `mpstat -P ALL` |
| **Memory** | Swap is used, `si`/`so` not zero, OOM killer in the log | [`free`](../08-processes/free.md), [`vmstat`](vmstat.md) | [`sar -r`](sar.md), `sar -W` |
| **Disk I/O** | High `wa` (I/O wait), slow responses although CPU is idle | [`vmstat`](vmstat.md) column `wa` | [`iostat -x`](iostat.md), [`iotop`](iotop.md) |
| **Network** | Timeouts, retransmissions | [`ss -s`](../11-network/ss.md) | `sar -n DEV`, `sar -n TCP,ETCP` |

## Reading the load correctly

```text
load average: 3.12, 1.85, 0.97
               │     │     └─ average of the last 15 minutes
               │     └─ last 5 minutes
               └─ last minute
```

The load counts processes that run or wait, for CPU **and** for disk. Compare it with the
number of CPU cores (`nproc`): on `tuxdex-srv` with 2 cores, a load of 2 means fully
busy, 3 means processes are waiting. A high load with an idle CPU points to disk I/O.

## The USE method

For every resource, check three things:

| | Question | Example |
|---|----------|---------|
| **U**tilization | How busy is it? | `%util` of a disk in `iostat` |
| **S**aturation | Is work waiting? | Run queue `r` in `vmstat`, `aqu-sz` in `iostat` |
| **E**rrors | Are there errors? | `dmesg`, `journalctl -k`, `smartctl` |

## Looking back in time

`top` and `vmstat` only show now. When the server was slow at 3 at night, only data
collected in the background helps. The package `sysstat` records CPU, memory, disk and
network every 10 minutes; [`sar`](sar.md) reads it afterwards.

## What you need to install

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| vmstat, sysctl | preinstalled (`procps`) | preinstalled (`procps`) | preinstalled (`procps-ng`) | preinstalled (`procps-ng`) |
| iostat, sar, mpstat | `sudo apt install sysstat` | `sudo apt install sysstat` | `sudo dnf install sysstat` | `sudo pacman -S sysstat` |
| Background collection for sar | `/etc/default/sysstat`: `ENABLED="true"` | `/etc/default/sysstat`: `ENABLED="true"` | `sudo systemctl enable --now sysstat` | `sudo systemctl enable --now sysstat` |
| iotop | `sudo apt install iotop-c` | `sudo apt install iotop-c` | `sudo dnf install iotop` | `sudo pacman -S iotop-c` |
| lsmod, modprobe | preinstalled (`kmod`) | preinstalled (`kmod`) | preinstalled (`kmod`) | preinstalled (`kmod`) |

!!! tip "Measure before you tune"
    Change kernel parameters only when a measurement shows a bottleneck, and change one
    thing at a time. Most tuning guides from the internet were written for other kernels
    and other workloads.

!!! warning "Free memory isn't wasted"
    Linux uses unused memory as cache (`buff/cache` in `free`). A server with little
    `free` but much `available` memory is fine. It only gets tight when `available` drops
    and swap is used actively.
