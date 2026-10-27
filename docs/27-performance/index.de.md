---
icon: material/speedometer
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-speedometer:{ .tc-hero-icon }

# Leistung und Kernel

Herausfinden, warum ein Server langsam ist: CPU, Speicher, Platten-I/O und Last über die
Zeit, und den Kernel mit sysctl, Limits und Modulen einstellen.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Die vier Ressourcen, Last richtig lesen, wo der Engpass liegt und was du installieren musst :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Den Engpass finden

<div class="grid cards" markdown>

-   :material-gauge:{ .lg .middle } **[vmstat](vmstat.md)**

    ---

    CPU, Speicher, Swap und I/O auf einen Blick.

-   :material-harddisk:{ .lg .middle } **[iostat](iostat.md)**

    ---

    Wie ausgelastet die Platten sind.

-   :material-harddisk-plus:{ .lg .middle } **[iotop](iotop.md)**

    ---

    Welcher Prozess Platten-I/O verursacht.

-   :material-chart-timeline-variant:{ .lg .middle } **[sar](sar.md)**

    ---

    Statistik für jede Uhrzeit des Tages.

</div>

## Den Kernel einstellen

<div class="grid cards" markdown>

-   :material-tune-variant:{ .lg .middle } **[sysctl](sysctl.md)**

    ---

    Kernel-Parameter im laufenden Betrieb.

-   :material-account-lock-outline:{ .lg .middle } **[ulimit](ulimit.md)**

    ---

    Grenzen wie offene Dateien.

-   :material-puzzle-outline:{ .lg .middle } **[lsmod](lsmod.md)**

    ---

    Geladene Kernelmodule.

-   :material-puzzle-plus-outline:{ .lg .middle } **[modprobe](modprobe.md)**

    ---

    Module laden und sperren.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-monitor-dashboard:{ .lg .middle } **[top](../08-processes/top.md)**

    ---

    Die aktivsten Prozesse live. Behandelt im Kapitel Prozesse.

-   :material-memory:{ .lg .middle } **[free](../08-processes/free.md)**

    ---

    Speicher und Swap auf einen Blick. Behandelt im Kapitel Prozesse.

-   :material-timer-outline:{ .lg .middle } **[uptime](../01-orientation/uptime.md)**

    ---

    Die Last der letzten 1, 5 und 15 Minuten. Behandelt im Kapitel Orientierung.

-   :material-file-search-outline:{ .lg .middle } **[lsof](../08-processes/lsof.md)**

    ---

    Welcher Prozess welche Dateien offen hält, bei `Too many open files`. Behandelt im Kapitel Prozesse.

-   :material-chip:{ .lg .middle } **[dmesg](../15-logs/dmesg.md)**

    ---

    Kernelmeldungen wie OOM-Killer oder Plattenfehler. Behandelt im Kapitel Logs.

</div>
