---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-cog-sync-outline:{ .tc-hero-icon }

# systemd und Dienste

Dienste starten, stoppen und überwachen, ihre Logs lesen, Jobs zeitgesteuert ausführen und
den Server sauber neu starten oder herunterfahren.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Units, Unit-Dateien und ihre Zustände :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Dienste verwalten

<div class="grid cards" markdown>

-   :material-cog-play-outline:{ .lg .middle } **[systemctl](systemctl.md)**

    ---

    Dienste starten, stoppen, aktivieren und prüfen.

</div>

## Logs und Analyse

<div class="grid cards" markdown>

-   :material-text-box-search-outline:{ .lg .middle } **[journalctl](journalctl.md)**

    ---

    Logs von Diensten und System lesen und filtern.

-   :material-chart-timeline:{ .lg .middle } **[systemd-analyze](systemd-analyze.md)**

    ---

    Bootzeit analysieren und Unit-Dateien prüfen.

</div>

## Starten und planen

<div class="grid cards" markdown>

-   :material-rocket-launch-outline:{ .lg .middle } **[systemd-run](systemd-run.md)**

    ---

    Einen Befehl als vorübergehende Unit ausführen.

</div>

## Systemeinstellungen

<div class="grid cards" markdown>

-   :material-cog-outline:{ .lg .middle } **[hostnamectl](../01-orientation/hostnamectl.md)**

    ---

    Systeminfos anzeigen und den Hostnamen setzen. Behandelt im Kapitel Orientierung.

-   :material-web-clock:{ .lg .middle } **[timedatectl](../01-orientation/timedatectl.md)**

    ---

    Zeitzone und Zeitsynchronisation anzeigen und setzen. Behandelt im Kapitel Orientierung.

-   :material-keyboard-outline:{ .lg .middle } **[localectl](localectl.md)**

    ---

    Systemsprache und Tastaturlayout anzeigen und setzen.

</div>

## Sitzungen und Neustart

<div class="grid cards" markdown>

-   :material-account-multiple-check-outline:{ .lg .middle } **[loginctl](loginctl.md)**

    ---

    Anmeldesitzungen anzeigen und beenden.

</div>
