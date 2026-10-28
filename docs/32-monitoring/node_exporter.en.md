# node_exporter

> The Prometheus exporter for Linux servers: offers CPU, memory, disk, file system and network values on port 9100. On Debian and Ubuntu the program is called `prometheus-node-exporter`.

![node_exporter output](../assets/screenshots/32-monitoring/node_exporter.png)

## Syntax

```bash
node_exporter [--web.listen-address=:9100] [--collector.NAME | --no-collector.NAME]
```

## Options

| Option | Description |
|--------|-------------|
| `--web.listen-address=` | Address and port, default `:9100` |
| `--collector.textfile.directory=` | Also read `*.prom` files from this directory |
| `--collector.systemd` | Enable the collector for systemd units (off by default) |
| `--no-collector.NAME` | Switch off a collector, e.g. `--no-collector.wifi` |
| `--collector.disable-defaults` | Start with no collectors, then enable single ones |
| `--web.config.file=` | File with TLS and basic auth settings |

On Debian and Ubuntu the options go into `ARGS="…"` in `/etc/default/prometheus-node-exporter`; then `sudo systemctl restart prometheus-node-exporter`.

## Examples

**A few values straight from the exporter:**

```bash
curl -s localhost:9100/metrics | grep -E '^node_(load1|memory_MemAvailable_bytes|memory_MemTotal_bytes) '
```

```text
node_load1 0.18
node_memory_MemAvailable_bytes 2.61210112e+09
node_memory_MemTotal_bytes 4.11205632e+09
```

**Is the service running:**

```bash
systemctl status prometheus-node-exporter --no-pager | head -3
```

```text
● prometheus-node-exporter.service - Prometheus exporter for machine metrics
     Loaded: loaded (/usr/lib/systemd/system/prometheus-node-exporter.service; enabled; preset: enabled)
     Active: active (running) since Mon 2026-10-26 10:42:17 CET; 2h 11min ago
```

**Free space on the root file system:**

```bash
curl -s localhost:9100/metrics | grep 'node_filesystem_avail_bytes.*mountpoint="/"'
```

```text
node_filesystem_avail_bytes{device="/dev/sda2",device_error="",fstype="ext4",mountpoint="/"} 2.4823209984e+10
```

Values are always in base units: bytes, seconds. `2.48e+10` bytes are about 23 GiB.

**An own value via the textfile collector:**

```bash
echo "backup_last_success_timestamp_seconds $(date +%s)" > /tmp/backup.prom
sudo mv /tmp/backup.prom /var/lib/prometheus/node-exporter/
curl -s localhost:9100/metrics | grep ^backup_
```

```text
backup_last_success_timestamp_seconds 1.793007737e+09
```

An alert rule like `time() - backup_last_success_timestamp_seconds > 86400` then reports a backup that hasn't run for a day.

**Collectors that found nothing:**

```bash
curl -s localhost:9100/metrics | grep '^node_scrape_collector_success.* 0$'
```

```text
node_scrape_collector_success{collector="bonding"} 0
node_scrape_collector_success{collector="fibrechannel"} 0
node_scrape_collector_success{collector="infiniband"} 0
node_scrape_collector_success{collector="tapestats"} 0
node_scrape_collector_success{collector="zfs"} 0
```

`0` isn't an error here: the server simply has no network bonding, no Fibre Channel, no InfiniBand, no tape drive and no ZFS.

## When do I need it?

- On every server that Prometheus should watch
- To check by hand which values a server delivers, before writing a rule
- To feed your own values into Prometheus, such as the time of the last successful backup

!!! tip "Own metrics with the textfile collector"
    A script writes lines like `backup_last_success_timestamp_seconds 1793007737` into a
    `.prom` file in the textfile directory. The node exporter delivers them with every scrape:
    ideal for cron jobs. Write to a temporary file first and rename it, so the exporter never
    reads half a file.

!!! warning "Port 9100 is open to everyone"
    The node exporter has no login by default. Allow the port only from the Prometheus server,
    for example with [`ufw`](../11-network/ufw.md): `sudo ufw allow from 192.0.2.10 to any port 9100 proto tcp`.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `prometheus-node-exporter` | `prometheus-node-exporter` | not in the repositories: release archive or container `prom/node-exporter` | `prometheus-node-exporter` |
| Program and service | `prometheus-node-exporter` | `prometheus-node-exporter` | `node_exporter` | `prometheus-node-exporter` |
| Options in | `/etc/default/prometheus-node-exporter` | `/etc/default/prometheus-node-exporter` | own systemd unit | `/etc/conf.d/prometheus-node-exporter` |

## Related commands

[prometheus](prometheus.md) · [promtool](promtool.md) · [curl](../11-network/curl.md) · [systemctl](../09-systemd/systemctl.md)
