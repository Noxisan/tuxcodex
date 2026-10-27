---
icon: material/calendar-clock
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-calendar-clock:{ .tc-hero-icon }

# Zeitgesteuerte Aufgaben

Jobs regelmäßig mit cron und systemd-Timern ausführen, einmalig zu einer festen Zeit mit `at`,
verpasste Jobs nachholen und dafür sorgen, dass ein Job nie doppelt gleichzeitig läuft.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** cron-Syntax, wo Cronjobs liegen und systemd-Timer im Vergleich :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## cron

<div class="grid cards" markdown>

-   :material-calendar-edit:{ .lg .middle } **[crontab](crontab.md)**

    ---

    Die Cronjobs eines Benutzers zeigen und bearbeiten.

-   :material-folder-play-outline:{ .lg .middle } **[run-parts](run-parts.md)**

    ---

    Alle Skripte in einem Verzeichnis ausführen.

-   :material-calendar-refresh-outline:{ .lg .middle } **[anacron](anacron.md)**

    ---

    Verpasste tägliche Jobs nachholen.

</div>

## Einmalige Jobs

<div class="grid cards" markdown>

-   :material-clock-plus-outline:{ .lg .middle } **[at](at.md)**

    ---

    Einen Befehl einmal zu einer Zeit ausführen.

-   :material-format-list-bulleted:{ .lg .middle } **[atq](atq.md)**

    ---

    Wartende at-Jobs auflisten.

-   :material-clock-remove-outline:{ .lg .middle } **[atrm](atrm.md)**

    ---

    Wartende at-Jobs entfernen.

-   :material-tray-full:{ .lg .middle } **[batch](batch.md)**

    ---

    Einen Job bei niedriger Last ausführen.

</div>

## Überschneidungen vermeiden

<div class="grid cards" markdown>

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-cog-play-outline:{ .lg .middle } **[systemctl](../09-systemd/systemctl.md)**

    ---

    `systemctl list-timers` zeigt alle systemd-Timer. Behandelt im Kapitel systemd.

-   :material-rocket-launch-outline:{ .lg .middle } **[systemd-run](../09-systemd/systemd-run.md)**

    ---

    Einen Befehl einmalig später als vorübergehenden Timer ausführen. Behandelt im Kapitel systemd.

-   :material-chart-timeline:{ .lg .middle } **[systemd-analyze](../09-systemd/systemd-analyze.md)**

    ---

    Timer-Ausdrücke mit `systemd-analyze calendar` prüfen. Behandelt im Kapitel systemd.

</div>
