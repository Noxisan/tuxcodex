# sysctl

> Reads and changes kernel parameters at runtime, such as IP forwarding, swappiness or network buffers.

![sysctl output](../assets/screenshots/27-performance/sysctl.png)

## Syntax

```bash
sysctl [-a] [NAME...]
sysctl -w NAME=VALUE
sysctl --system
```

## Options

| Option | Description |
|--------|-------------|
| `NAME` | Show a parameter, such as `vm.swappiness` |
| `-a` | Show all parameters |
| `-w NAME=VALUE` | Change a parameter until the next reboot |
| `--system` | Load all files from `/etc/sysctl.d/` and the other configuration directories |
| `-p FILE` | Load a single file |

Parameters an admin often touches:

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `net.ipv4.ip_forward` | `0` | `1` lets the server route packets, for a VPN gateway or a router |
| `vm.swappiness` | `60` | Lower values keep more in RAM before swapping |
| `fs.file-max` | very high | Maximum open files on the whole system |
| `net.core.somaxconn` | `4096` | Maximum queue of waiting connections per socket |
| `kernel.panic` | `0` | Seconds until an automatic reboot after a kernel panic |

## Examples

**Read some parameters:**

```bash
sysctl vm.swappiness net.ipv4.ip_forward net.core.somaxconn
```

```text
vm.swappiness = 60
net.ipv4.ip_forward = 0
net.core.somaxconn = 4096
```

**Enable IP forwarding for a VPN gateway, permanently:**

```bash
echo 'net.ipv4.ip_forward = 1' | sudo tee /etc/sysctl.d/90-tuxdex.conf
sudo sysctl --system | tail -3
```

```text
net.ipv4.ip_forward = 1
* Applying /etc/sysctl.d/90-tuxdex.conf ...
net.ipv4.ip_forward = 1
* Applying /etc/sysctl.conf ...
```

**Change a value only for a test:**

```bash
sudo sysctl -w vm.swappiness=10
```

```text
vm.swappiness = 10
```

**Search all parameters:**

```bash
sudo sysctl -a 2>/dev/null | grep -E '^net.ipv4.tcp_(keepalive_time|fin_timeout|syncookies)'
```

```text
net.ipv4.tcp_fin_timeout = 60
net.ipv4.tcp_keepalive_time = 7200
net.ipv4.tcp_syncookies = 1
```

## When do I need it?

- To turn a server into a VPN gateway or router (`ip_forward`)
- To adapt the kernel to a workload, for example a database or many connections
- To check what a hardening guide or a tool has changed

!!! tip "Permanent in /etc/sysctl.d/"
    Write own settings into a file like `/etc/sysctl.d/90-tuxdex.conf` and load it with
    `sudo sysctl --system`. That way it's clear which values you changed, and they survive
    the reboot.

!!! warning "One change at a time"
    Copied tuning blocks with dozens of values make it impossible to know which one helped
    or hurt. Change one parameter, measure, then decide.

## Related commands

[ulimit](ulimit.md) · [modprobe](modprobe.md) · [wg-quick](../26-wireguard/wg-quick.md)
