---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-cog-sync-outline:{ .tc-hero-icon }

# systemd and services

Starting, stopping and monitoring services, reading their logs, running jobs on a schedule, and
restarting or shutting down the server cleanly.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Units, unit files and their states :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Manage services

<div class="grid cards" markdown>

-   :material-cog-play-outline:{ .lg .middle } **[systemctl](systemctl.md)**

    ---

    Start, stop, enable and check services.

</div>

## Logs and analysis

<div class="grid cards" markdown>

-   :material-text-box-search-outline:{ .lg .middle } **[journalctl](journalctl.md)**

    ---

    Read and filter the logs of services and the system.

-   :material-chart-timeline:{ .lg .middle } **[systemd-analyze](systemd-analyze.md)**

    ---

    Analyze boot time and check unit files.

</div>

## Run and schedule

<div class="grid cards" markdown>

-   :material-rocket-launch-outline:{ .lg .middle } **[systemd-run](systemd-run.md)**

    ---

    Run a command as a temporary unit.

</div>

## System settings

<div class="grid cards" markdown>

-   :material-cog-outline:{ .lg .middle } **[hostnamectl](../01-orientation/hostnamectl.md)**

    ---

    Show system information and set the host name. Covered in the chapter Orientation.

-   :material-web-clock:{ .lg .middle } **[timedatectl](../01-orientation/timedatectl.md)**

    ---

    Show and set time zone and time synchronization. Covered in the chapter Orientation.

-   :material-keyboard-outline:{ .lg .middle } **[localectl](localectl.md)**

    ---

    Show and set system language and keyboard layout.

</div>

## Sessions and power

<div class="grid cards" markdown>

-   :material-account-multiple-check-outline:{ .lg .middle } **[loginctl](loginctl.md)**

    ---

    Show and end login sessions.

</div>
