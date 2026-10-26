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

-   :material-format-list-numbered:{ .lg .middle } **[nl](nl.md)**

    ---

    Print a file with line numbers.

</div>

## Read page by page

<div class="grid cards" markdown>

-   :material-book-open-page-variant-outline:{ .lg .middle } **[less](less.md)**

    ---

    Scroll, search and follow large files and logs.

</div>

## Beginning and end

<div class="grid cards" markdown>

-   :material-arrow-collapse-up:{ .lg .middle } **[head](head.md)**

    ---

    Show the first lines of a file.

-   :material-arrow-collapse-down:{ .lg .middle } **[tail](tail.md)**

    ---

    Show the last lines of a file and follow logs live.

</div>

## Compressed files

<div class="grid cards" markdown>

-   :material-zip-box-outline:{ .lg .middle } **[zcat](zcat.md)**

    ---

    Print gzip-compressed files without unpacking them.

-   :material-book-open-variant:{ .lg .middle } **[zless](zless.md)**

    ---

    Browse and search compressed files page by page.

</div>

## Binary files

<div class="grid cards" markdown>

-   :material-hexadecimal:{ .lg .middle } **[hexdump](hexdump.md)**

    ---

    Show the bytes of a file in hexadecimal.

-   :material-format-text:{ .lg .middle } **[strings](strings.md)**

    ---

    Pull readable text out of binary files.

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
