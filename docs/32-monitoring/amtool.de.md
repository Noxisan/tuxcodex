# amtool

> Die Kommandozeile für den Alertmanager von Prometheus: seine Konfiguration prüfen, aktive Alarme zeigen und sie während Wartungen stummschalten.

![amtool output](../assets/screenshots/32-monitoring/amtool.png)

## Syntax

```bash
amtool [--alertmanager.url=URL] check-config | alert query | silence add | silence query | silence expire
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `check-config DATEI` | `alertmanager.yml` prüfen |
| `alert query [MATCHER]` | Aktive Alarme zeigen, z. B. `alertname=InstanceDown` |
| `silence add MATCHER --duration=2h --comment=…` | Passende Alarme für eine Weile stummschalten |
| `silence query` | Aktive Stummschaltungen auflisten (`-q`: nur IDs) |
| `silence expire ID` | Eine Stummschaltung vorzeitig beenden |
| `config routes` | Den Routing-Baum zeigen: wer welchen Alarm bekommt |
| `--alertmanager.url=` | Adresse des Alertmanagers, z. B. `http://localhost:9093` |

Trag die Adresse in `~/.config/amtool/config.yml` ein (`alertmanager.url: http://localhost:9093`), dann kannst du `--alertmanager.url` weglassen.

## Beispiele

**Die Konfiguration prüfen:**

```bash
amtool check-config /etc/prometheus/alertmanager.yml
```

```text
Checking '/etc/prometheus/alertmanager.yml'  SUCCESS
Found:
 - global config
 - route
 - 0 inhibit rules
 - 1 receivers
 - 0 templates

```

**Aktive Alarme:**

```bash
amtool --alertmanager.url=http://localhost:9093 alert query
```

```text
Alertname     Starts At                Summary                  State
InstanceDown  2026-10-26 09:38:05 UTC  192.0.2.21:9100 is down  active
```

**Einen Server für zwei Stunden Wartung stummschalten:**

```bash
amtool --alertmanager.url=http://localhost:9093 silence add instance=192.0.2.21:9100 \
  --duration=2h --comment="Kernel update" --author=nox
```

```text
10e4013c-0d68-430c-b174-6ffc507daab7
```

Die Ausgabe ist die ID der Stummschaltung. Solange sie läuft, haben Alarme für `192.0.2.21:9100` den Zustand `suppressed` und verschicken keine Mails.

**Die aktiven Stummschaltungen auflisten:**

```bash
amtool --alertmanager.url=http://localhost:9093 silence query
```

```text
ID                                    Matchers                    Ends At                  Created By  Comment
10e4013c-0d68-430c-b174-6ffc507daab7  instance="192.0.2.21:9100"  2026-10-26 11:42:17 UTC  nox         Kernel update
```

**Nach der Wartung alle Stummschaltungen beenden:**

```bash
amtool --alertmanager.url=http://localhost:9093 silence expire $(amtool --alertmanager.url=http://localhost:9093 silence query -q)
echo $?
```

```text
0
```

**Wer die Alarme bekommt:**

```bash
amtool --alertmanager.url=http://localhost:9093 config routes
```

```text
Routing tree:
.
└── default-route  receiver: admin
```

## Wann brauche ich das?

- Vor einer geplanten Wartung, damit ein Neustart niemanden weckt
- Um nach einer Änderung an `alertmanager.yml` zu prüfen, ob die Datei gültig ist
- Um ohne Weboberfläche zu sehen, welche Alarme aktiv sind

!!! tip "Vorher stummschalten, nicht hinterher"
    Setz die Stummschaltung, bevor die Wartung beginnt: `amtool silence add instance=~"web01.*"
    --duration=1h --comment="Kernel-Update"`. Danach beendet `silence expire` sie, damit spätere
    Probleme wieder gemeldet werden.

!!! warning "Stummschaltungen verdecken echte Probleme"
    Eine Stummschaltung mit breitem Matcher (`severity=critical`) oder langer Dauer verschluckt
    auch Alarme, die mit der Wartung nichts zu tun haben. Halte den Matcher eng und die Dauer
    kurz.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `prometheus-alertmanager` | `prometheus-alertmanager` | nicht in den Paketquellen: Release-Archiv oder Container `prom/alertmanager` | `alertmanager` |
| Alertmanager-Dienst | `prometheus-alertmanager` | `prometheus-alertmanager` | eigene systemd-Unit | `alertmanager` |
| Konfiguration | `/etc/prometheus/alertmanager.yml` | `/etc/prometheus/alertmanager.yml` | je nach Einrichtung | `/etc/alertmanager/alertmanager.yml` |

## Verwandte Befehle

[promtool](promtool.md) · [prometheus](prometheus.md) · [node_exporter](node_exporter.md) · [curl](../11-network/curl.md)
