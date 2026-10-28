---
title: "Performance and kernel"
icon: material/speedometer
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-speedometer:{ .tc-hero-icon }

# Performance and kernel

Finding out why a server is slow: CPU, memory, disk I/O and load over time, and tuning
the kernel with sysctl, limits and modules.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** The four resources, reading load, where the bottleneck is, and what to install :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Finding the bottleneck

<div class="grid cards" markdown>

-   :material-gauge:{ .lg .middle } **[vmstat](vmstat.md)**

    ---

    CPU, memory, swap and I/O at a glance.

-   :material-harddisk:{ .lg .middle } **[iostat](iostat.md)**

    ---

    How busy the disks are.

-   :material-harddisk-plus:{ .lg .middle } **[iotop](iotop.md)**

    ---

    Which process causes disk I/O.

-   :material-chart-timeline-variant:{ .lg .middle } **[sar](sar.md)**

    ---

    Statistics for any time of the day.

</div>

## Tuning the kernel

<div class="grid cards" markdown>

-   :material-tune-variant:{ .lg .middle } **[sysctl](sysctl.md)**

    ---

    Kernel parameters at runtime.

-   :material-account-lock-outline:{ .lg .middle } **[ulimit](ulimit.md)**

    ---

    Limits such as open files.

-   :material-puzzle-outline:{ .lg .middle } **[lsmod](lsmod.md)**

    ---

    Loaded kernel modules.

-   :material-puzzle-plus-outline:{ .lg .middle } **[modprobe](modprobe.md)**

    ---

    Load and block modules.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-monitor-dashboard:{ .lg .middle } **[top](../08-processes/top.md)**

    ---

    The busiest processes live. Covered in the chapter Processes.

-   :material-memory:{ .lg .middle } **[free](../08-processes/free.md)**

    ---

    Memory and swap at a glance. Covered in the chapter Processes.

-   :material-timer-outline:{ .lg .middle } **[uptime](../01-orientation/uptime.md)**

    ---

    The load average of the last 1, 5 and 15 minutes. Covered in the chapter Orientation.

-   :material-file-search-outline:{ .lg .middle } **[lsof](../08-processes/lsof.md)**

    ---

    Which process holds which files open, for `Too many open files`. Covered in the chapter Processes.

-   :material-chip:{ .lg .middle } **[dmesg](../15-logs/dmesg.md)**

    ---

    Kernel messages such as the OOM killer or disk errors. Covered in the chapter Logs.

</div>
