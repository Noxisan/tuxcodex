# Understanding monitoring

Monitoring answers two questions: *How are my servers doing right now?* and *Does someone
get told when something breaks?* **Prometheus** is the most common open source answer on
Linux servers.

## How Prometheus works

```text
 web01, db01, tuxdex-srv          tuxdex-srv                         tuxdex-srv
┌──────────────────────┐  pull   ┌──────────────────────┐  alerts  ┌──────────────┐  mail
│ node_exporter :9100  │ ──────> │ Prometheus :9090     │ ───────> │ Alertmanager │ ─────> admin
│ /metrics             │         │ stores time series,  │          │ :9093        │
└──────────────────────┘         │ evaluates rules      │          └──────────────┘
                                 └──────────────────────┘
                                            │
                                            └──> Grafana (dashboards, optional)
```

| Part | Job |
|------|-----|
| **Exporter** | Offers metrics as text on an HTTP page `/metrics`. The node exporter covers the server itself: CPU, RAM, disks, network |
| **Prometheus** | Fetches (*scrapes*) all targets every 15 seconds, stores the values and evaluates alert rules |
| **Alertmanager** | Receives firing alerts, groups them, silences them on request and sends mails or chat messages |
| **Grafana** | Draws dashboards from the data in Prometheus; not part of Prometheus itself |

## Packages, services and ports

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Prometheus | `prometheus` | `prometheus` | not in the repositories | `prometheus` |
| Node exporter | `prometheus-node-exporter` | `prometheus-node-exporter` | not in the repositories | `prometheus-node-exporter` |
| Alertmanager | `prometheus-alertmanager` | `prometheus-alertmanager` | not in the repositories | `alertmanager` |
| Started after install | yes | yes | see below | no: `systemctl enable --now` |

On RHEL, use the release archives from prometheus.io with your own systemd units, or the
container images `prom/prometheus`, `prom/node-exporter` and `prom/alertmanager`.

| Port | Service |
|------|---------|
| 9090 | Prometheus (web interface and API) |
| 9093 | Alertmanager |
| 9100 | Node exporter |

## A scrape configuration

`/etc/prometheus/prometheus.yml` (shortened):

```text
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['localhost:9093']

rule_files:
  - /etc/prometheus/rules/*.yml

scrape_configs:
  - job_name: node
    static_configs:
      - targets: ['localhost:9100', '192.0.2.21:9100', '192.0.2.22:9100']
```

After a change: `promtool check config`, then `sudo systemctl reload prometheus`.

## PromQL in five queries

| Query | Result |
|-------|--------|
| `up` | `1` for every reachable target, `0` for the others |
| `up == 0` | Only the targets that are down |
| `node_load1` | Load average of the last minute, per server |
| `100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)` | RAM usage in percent |
| `rate(node_network_receive_bytes_total[5m])` | Received bytes per second, averaged over 5 minutes |

You can type them into the web interface on port 9090 or run them with
`promtool query instant`.

## An alert rule

`/etc/prometheus/rules/node.yml`:

```text
groups:
  - name: node
    rules:
      - alert: InstanceDown
        expr: up == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "{{ $labels.instance }} is down"
```

`for: 2m` means the condition must be true for two minutes before the alert *fires*. That
avoids mails for a short hiccup. The Alertmanager then decides who gets told; see
`amtool`.

!!! tip "Monitor the monitoring"
    If the Prometheus server itself fails, no alert arrives. A simple external check (a
    second Prometheus, an uptime service or a cron job with [`curl`](../11-network/curl.md)
    on `/-/healthy`) closes that gap.

!!! warning "Don't expose the ports"
    The metrics reveal a lot about your servers: versions, mount points, services.
    Allow ports 9100 and 9090 only from the Prometheus server and your admin network.
