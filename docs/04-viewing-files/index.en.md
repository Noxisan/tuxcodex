---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-text-box-search-outline:{ .tc-hero-icon }

# Viewing files

Reading configuration files, logs and other files without changing them, from short
text files to compressed logs and binary files.

</div>

## Show the whole file

<div class="grid cards" markdown>

-   :material-text-box-outline:{ .lg .middle } **[cat](cat.md)**

    ---

    Print files and join them together.

-   :material-sort-reverse-variant:{ .lg .middle } **[tac](tac.md)**

    ---

    Print a file backwards, last line first.

</div>

## Reading logs

| Task | Command |
|------|---------|
| Follow a log live while you test | `tail -f /var/log/nginx/error.log` |
| Show the last 50 lines | `tail -n 50 /var/log/nginx/error.log` |
| Browse and search a large log | `less /var/log/nginx/access.log`, then `/` to search |
| Read a rotated, compressed log | `zless /var/log/nginx/access.log.2.gz` |
| Show the newest lines first | `tac /var/log/nginx/access.log | less` |

!!! tip "Logs of systemd services"
    Many services on Debian don't write their own log files, but log to the systemd
    journal. You read those with `journalctl`, which is covered in the chapter on logs.

!!! tip "Learning path"
    The commands are sorted from simple to more complex. Work through them in order,
    since later pages build on the earlier ones.
