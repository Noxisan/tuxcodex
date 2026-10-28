# Monitoring verstehen

Monitoring beantwortet zwei Fragen: *Wie geht es meinen Servern gerade?* und *Erfährt
jemand davon, wenn etwas kaputtgeht?* **Prometheus** ist dafür auf Linux-Servern die
verbreitetste Open-Source-Lösung.

## Wie Prometheus arbeitet

```text
 web01, db01, tuxdex-srv          tuxdex-srv                         tuxdex-srv
┌──────────────────────┐  holt   ┌──────────────────────┐  Alarme  ┌──────────────┐  Mail
│ node_exporter :9100  │ ──────> │ Prometheus :9090     │ ───────> │ Alertmanager │ ─────> Admin
│ /metrics             │         │ speichert Zeitreihen,│          │ :9093        │
└──────────────────────┘         │ wertet Regeln aus    │          └──────────────┘
                                 └──────────────────────┘
                                            │
                                            └──> Grafana (Dashboards, optional)
```

| Teil | Aufgabe |
|------|---------|
| **Exporter** | Bietet Metriken als Text auf einer HTTP-Seite `/metrics` an. Der Node Exporter deckt den Server selbst ab: CPU, RAM, Platten, Netzwerk |
| **Prometheus** | Holt alle 15 Sekunden die Werte aller Ziele ab (*Scrape*), speichert sie und wertet Alarmregeln aus |
| **Alertmanager** | Nimmt ausgelöste Alarme an, fasst sie zusammen, schaltet sie auf Wunsch stumm und verschickt Mails oder Chatnachrichten |
| **Grafana** | Zeichnet Dashboards aus den Daten in Prometheus; gehört nicht zu Prometheus selbst |

## Pakete, Dienste und Ports

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Prometheus | `prometheus` | `prometheus` | nicht in den Paketquellen | `prometheus` |
| Node Exporter | `prometheus-node-exporter` | `prometheus-node-exporter` | nicht in den Paketquellen | `prometheus-node-exporter` |
| Alertmanager | `prometheus-alertmanager` | `prometheus-alertmanager` | nicht in den Paketquellen | `alertmanager` |
| Nach der Installation gestartet | ja | ja | siehe unten | nein: `systemctl enable --now` |

Unter RHEL nimmst du die Release-Archive von prometheus.io mit eigenen systemd-Units oder die
Container-Images `prom/prometheus`, `prom/node-exporter` und `prom/alertmanager`.

| Port | Dienst |
|------|--------|
| 9090 | Prometheus (Weboberfläche und API) |
| 9093 | Alertmanager |
| 9100 | Node Exporter |

## Eine Scrape-Konfiguration

`/etc/prometheus/prometheus.yml` (gekürzt):

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

Nach einer Änderung: `promtool check config`, dann `sudo systemctl reload prometheus`.

## PromQL in fünf Abfragen

| Abfrage | Ergebnis |
|---------|----------|
| `up` | `1` für jedes erreichbare Ziel, `0` für die anderen |
| `up == 0` | Nur die Ziele, die nicht erreichbar sind |
| `node_load1` | Load Average der letzten Minute, pro Server |
| `100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)` | RAM-Auslastung in Prozent |
| `rate(node_network_receive_bytes_total[5m])` | Empfangene Bytes pro Sekunde, gemittelt über 5 Minuten |

Du gibst sie in der Weboberfläche auf Port 9090 ein oder führst sie mit
`promtool query instant` aus.

## Eine Alarmregel

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

`for: 2m` heißt: Die Bedingung muss zwei Minuten lang zutreffen, bevor der Alarm *auslöst*
(firing). Das verhindert Mails wegen eines kurzen Aussetzers. Wer benachrichtigt wird,
entscheidet danach der Alertmanager; siehe `amtool`.

!!! tip "Das Monitoring überwachen"
    Fällt der Prometheus-Server selbst aus, kommt kein Alarm. Eine einfache Prüfung von
    außen (ein zweites Prometheus, ein Uptime-Dienst oder ein Cronjob mit
    [`curl`](../11-network/curl.md) auf `/-/healthy`) schließt diese Lücke.

!!! warning "Die Ports nicht offen ins Netz stellen"
    Die Metriken verraten viel über deine Server: Versionen, Einhängepunkte, Dienste. Erlaube
    die Ports 9100 und 9090 nur vom Prometheus-Server und aus deinem Admin-Netz.
