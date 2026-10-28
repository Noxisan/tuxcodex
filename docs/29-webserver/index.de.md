---
title: "Webserver"
icon: material/web
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-web:{ .tc-hero-icon }

# Webserver

nginx und Apache betreiben: Konfiguration testen und neu laden, Seiten und Module
aktivieren, Bereiche mit Passwörtern schützen, Reverse Proxys und Lasttests.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Wo die Konfiguration je Distribution liegt, Server-Blöcke und Virtual Hosts, Reverse Proxy und TLS :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## nginx

<div class="grid cards" markdown>

-   :material-server-network-outline:{ .lg .middle } **[nginx](nginx.md)**

    ---

    Konfiguration testen, neu laden und durchsuchen.

</div>

## Apache

<div class="grid cards" markdown>

-   :material-feather:{ .lg .middle } **[apachectl](apachectl.md)**

    ---

    Apache testen und neu laden, Virtual Hosts zeigen.

-   :material-toggle-switch-outline:{ .lg .middle } **[a2ensite](a2ensite.md)**

    ---

    Seiten aktivieren und deaktivieren.

-   :material-puzzle-check-outline:{ .lg .middle } **[a2enmod](a2enmod.md)**

    ---

    Module aktivieren und deaktivieren.

</div>

## Werkzeuge

<div class="grid cards" markdown>

-   :material-account-key-outline:{ .lg .middle } **[htpasswd](htpasswd.md)**

    ---

    Passwortschutz für Bereiche.

-   :material-speedometer-medium:{ .lg .middle } **[ab](ab.md)**

    ---

    Lasttests gegen den eigenen Server.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-certificate-outline:{ .lg .middle } **[certbot](../24-certificates/certbot.md)**

    ---

    HTTPS mit Let's Encrypt für nginx und Apache. Behandelt im Kapitel Zertifikate.

-   :material-web-check:{ .lg .middle } **[curl](../11-network/curl.md)**

    ---

    Antworten, Header und Weiterleitungen testen. Behandelt im Kapitel Netzwerk.

-   :material-chart-bar:{ .lg .middle } **[goaccess](../15-logs/goaccess.md)**

    ---

    Die Zugriffslogs auswerten. Behandelt im Kapitel Logs.

-   :material-rotate-right:{ .lg .middle } **[logrotate](../15-logs/logrotate.md)**

    ---

    Die Logs des Webservers klein halten. Behandelt im Kapitel Logs.

</div>
