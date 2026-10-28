---
title: "Caches und Message Queues"
icon: material/lightning-bolt-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-lightning-bolt-outline:{ .tc-hero-icon }

# Caches und Message Queues

Redis (oder Valkey) als schnellen Cache und RabbitMQ als Message Broker betreiben: Zustand
und Speicher prüfen, Geschwindigkeit messen, Benutzer und Queues verwalten und Probleme
finden.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Cache oder Message Broker, Redis und Valkey, Ports, Redis absichern, Persistenz und Speichergrenzen, Begriffe von RabbitMQ :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Redis / Valkey

<div class="grid cards" markdown>

-   :material-console-line:{ .lg .middle } **[redis-cli](redis-cli.md)**

    ---

    Zustand, Speicher, Schlüssel und Live-Verkehr.

-   :material-speedometer:{ .lg .middle } **[redis-benchmark](redis-benchmark.md)**

    ---

    Anfragen pro Sekunde und Latenz messen.

</div>

## RabbitMQ

<div class="grid cards" markdown>

-   :material-tray-full:{ .lg .middle } **[rabbitmqctl](rabbitmqctl.md)**

    ---

    Benutzer, vhosts, Rechte und Queues.

-   :material-puzzle-outline:{ .lg .middle } **[rabbitmq-plugins](rabbitmq-plugins.md)**

    ---

    Weboberfläche und andere Plugins einschalten.

-   :material-stethoscope:{ .lg .middle } **[rabbitmq-diagnostics](rabbitmq-diagnostics.md)**

    ---

    Health Checks, Alarme, Ports und Speicher.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-gauge:{ .lg .middle } **[node_exporter](../32-monitoring/node_exporter.md)**

    ---

    Redis und RabbitMQ in Prometheus überwachen. Behandelt im Kapitel Monitoring.

-   :material-lan:{ .lg .middle } **[ss](../11-network/ss.md)**

    ---

    Prüfen, auf welcher Adresse Redis und RabbitMQ lauschen. Behandelt im Kapitel Netzwerk.

-   :material-shield-lock-outline:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Die Ports nur für Anwendungsserver öffnen. Behandelt im Kapitel Netzwerk.

</div>
