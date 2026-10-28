---
title: "Caches and message queues"
icon: material/lightning-bolt-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-lightning-bolt-outline:{ .tc-hero-icon }

# Caches and message queues

Running Redis (or Valkey) as a fast cache and RabbitMQ as a message broker: checking state
and memory, measuring speed, managing users and queues, and finding problems.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Cache or message broker, Redis and Valkey, ports, securing Redis, persistence and memory limits, RabbitMQ concepts :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Redis / Valkey

<div class="grid cards" markdown>

-   :material-console-line:{ .lg .middle } **[redis-cli](redis-cli.md)**

    ---

    State, memory, keys and live traffic.

-   :material-speedometer:{ .lg .middle } **[redis-benchmark](redis-benchmark.md)**

    ---

    Measure requests per second and latency.

</div>

## RabbitMQ

<div class="grid cards" markdown>

-   :material-tray-full:{ .lg .middle } **[rabbitmqctl](rabbitmqctl.md)**

    ---

    Users, vhosts, permissions and queues.

-   :material-puzzle-outline:{ .lg .middle } **[rabbitmq-plugins](rabbitmq-plugins.md)**

    ---

    Enable the web interface and other plugins.

-   :material-stethoscope:{ .lg .middle } **[rabbitmq-diagnostics](rabbitmq-diagnostics.md)**

    ---

    Health checks, alarms, ports and memory.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-gauge:{ .lg .middle } **[node_exporter](../32-monitoring/node_exporter.md)**

    ---

    Watch Redis and RabbitMQ in Prometheus. Covered in the chapter Monitoring.

-   :material-lan:{ .lg .middle } **[ss](../11-network/ss.md)**

    ---

    Check on which address Redis and RabbitMQ listen. Covered in the chapter Network.

-   :material-shield-lock-outline:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Open the ports only for application servers. Covered in the chapter Network.

</div>
