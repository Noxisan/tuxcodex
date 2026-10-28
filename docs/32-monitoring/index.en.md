---
title: "Monitoring"
icon: material/monitor-dashboard
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-monitor-dashboard:{ .tc-hero-icon }

# Monitoring

Watching servers with Prometheus: collecting metrics with the node exporter, checking
configuration and alert rules, querying data and handling alerts in the Alertmanager.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** How Prometheus works, ports and packages, a scrape configuration, PromQL, alert rules and Alertmanager :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Prometheus

<div class="grid cards" markdown>

-   :material-gauge:{ .lg .middle } **[node_exporter](node_exporter.md)**

    ---

    Metrics of a Linux server on port 9100.

-   :material-chart-line:{ .lg .middle } **[prometheus](prometheus.md)**

    ---

    Collect, store and evaluate metrics.

</div>

## Tools

<div class="grid cards" markdown>

-   :material-file-check-outline:{ .lg .middle } **[promtool](promtool.md)**

    ---

    Check configuration and rules, run queries.

-   :material-bell-off-outline:{ .lg .middle } **[amtool](amtool.md)**

    ---

    Show alerts and silence them.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-chart-line:{ .lg .middle } **[sar](../27-performance/sar.md)**

    ---

    Performance history on a single server. Covered in the chapter Performance.

-   :material-web-check:{ .lg .middle } **[curl](../11-network/curl.md)**

    ---

    Query the metrics and the API by hand. Covered in the chapter Network.

-   :material-code-json:{ .lg .middle } **[jq](../05-text-processing/jq.md)**

    ---

    Filter the JSON answers of the API. Covered in the chapter Text processing.

-   :material-shield-lock-outline:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Allow the exporter ports only for Prometheus. Covered in the chapter Network.

</div>
