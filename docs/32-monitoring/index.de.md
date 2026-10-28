---
icon: material/monitor-dashboard
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-monitor-dashboard:{ .tc-hero-icon }

# Monitoring

Server mit Prometheus überwachen: Metriken mit dem Node Exporter sammeln, Konfiguration und
Alarmregeln prüfen, Daten abfragen und Alarme im Alertmanager bearbeiten.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Wie Prometheus arbeitet, Ports und Pakete, eine Scrape-Konfiguration, PromQL, Alarmregeln und Alertmanager :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Prometheus

<div class="grid cards" markdown>

-   :material-gauge:{ .lg .middle } **[node_exporter](node_exporter.md)**

    ---

    Metriken eines Linux-Servers auf Port 9100.

-   :material-chart-line:{ .lg .middle } **[prometheus](prometheus.md)**

    ---

    Metriken sammeln, speichern und auswerten.

</div>

## Werkzeuge

<div class="grid cards" markdown>

-   :material-file-check-outline:{ .lg .middle } **[promtool](promtool.md)**

    ---

    Konfiguration und Regeln prüfen, Abfragen ausführen.

-   :material-bell-off-outline:{ .lg .middle } **[amtool](amtool.md)**

    ---

    Alarme zeigen und stummschalten.

</div>
