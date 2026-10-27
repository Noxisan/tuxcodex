---
icon: material/text-box-multiple-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-text-box-multiple-outline:{ .tc-hero-icon }

# Logs

Finding out where a server writes its logs, reading kernel messages, writing your own log entries,
keeping log files small, tracking failed logins and audit events, and analysing logs quickly.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Where logs are kept, log levels and log rotation :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Kernel and system

<div class="grid cards" markdown>

-   :material-chip:{ .lg .middle } **[dmesg](dmesg.md)**

    ---

    Kernel messages: hardware, drivers, OOM killer.

-   :material-pencil-plus-outline:{ .lg .middle } **[logger](logger.md)**

    ---

    Write your own messages into the log.

</div>

## Manage log files

<div class="grid cards" markdown>

</div>

## Logins

<div class="grid cards" markdown>

</div>

## Audit

<div class="grid cards" markdown>

</div>

## Analyse

<div class="grid cards" markdown>

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-text-box-search-outline:{ .lg .middle } **[journalctl](../09-systemd/journalctl.md)**

    ---

    Read the systemd journal. Covered in the chapter systemd.

-   :material-arrow-collapse-down:{ .lg .middle } **[tail](../04-viewing-files/tail.md)**

    ---

    Follow log files live with `tail -f`. Covered in the chapter Viewing files.

-   :material-book-open-page-variant-outline:{ .lg .middle } **[less](../04-viewing-files/less.md)**

    ---

    Browse and search large log files. Covered in the chapter Viewing files.

-   :material-text-box-search-outline:{ .lg .middle } **[grep](../05-text-processing/grep.md)**

    ---

    Filter log lines by a pattern. Covered in the chapter Text processing.

-   :material-history:{ .lg .middle } **[last](../01-orientation/last.md)**

    ---

    Show the login history. Covered in the chapter Orientation.

</div>
