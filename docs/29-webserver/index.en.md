---
title: "Web servers"
icon: material/web
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-web:{ .tc-hero-icon }

# Web servers

Running nginx and Apache: testing and reloading the configuration, enabling sites and
modules, protecting areas with passwords, reverse proxies and load tests.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Where the configuration lives on each distribution, server blocks and virtual hosts, reverse proxy and TLS :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## nginx

<div class="grid cards" markdown>

-   :material-server-network-outline:{ .lg .middle } **[nginx](nginx.md)**

    ---

    Test, reload and inspect the configuration.

</div>

## Apache

<div class="grid cards" markdown>

-   :material-feather:{ .lg .middle } **[apachectl](apachectl.md)**

    ---

    Test and reload Apache, list virtual hosts.

-   :material-toggle-switch-outline:{ .lg .middle } **[a2ensite](a2ensite.md)**

    ---

    Enable and disable sites.

-   :material-puzzle-check-outline:{ .lg .middle } **[a2enmod](a2enmod.md)**

    ---

    Enable and disable modules.

</div>

## Tools

<div class="grid cards" markdown>

-   :material-account-key-outline:{ .lg .middle } **[htpasswd](htpasswd.md)**

    ---

    Password protection for areas.

-   :material-speedometer-medium:{ .lg .middle } **[ab](ab.md)**

    ---

    Load tests against your own server.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-certificate-outline:{ .lg .middle } **[certbot](../24-certificates/certbot.md)**

    ---

    HTTPS with Let's Encrypt for nginx and Apache. Covered in the chapter Certificates.

-   :material-web-check:{ .lg .middle } **[curl](../11-network/curl.md)**

    ---

    Test responses, headers and redirects. Covered in the chapter Network.

-   :material-chart-bar:{ .lg .middle } **[goaccess](../15-logs/goaccess.md)**

    ---

    Evaluate the access logs. Covered in the chapter Logs.

-   :material-rotate-right:{ .lg .middle } **[logrotate](../15-logs/logrotate.md)**

    ---

    Keep the logs of the web server small. Covered in the chapter Logs.

</div>
