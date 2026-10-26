---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-text-search:{ .tc-hero-icon }

# Text processing

Searching, filtering, sorting, counting and changing text, the everyday tools for logs,
configuration files and the output of other commands.

</div>

## Count and sort

<div class="grid cards" markdown>

-   :material-counter:{ .lg .middle } **[wc](wc.md)**

    ---

    Count lines, words and bytes.

-   :material-sort-alphabetical-ascending:{ .lg .middle } **[sort](sort.md)**

    ---

    Sort lines alphabetically, numerically or by column.

</div>

## Combining commands with pipes

The real strength of these tools comes from combining them. Each command does one thing,
and you connect them into a chain:

| Symbol | Meaning | Example |
|--------|---------|---------|
| `|` | Pass the output of one command to the next | `grep 404 access.log | wc -l` |
| `>` | Write the output to a file, overwriting it | `sort names.txt > sorted.txt` |
| `>>` | Append the output to a file | `date >> run.log` |
| `2>` | Write error messages to a file | `find / -name x 2> errors.txt` |
| `2>&1` | Send error messages to the same place as the output | `./backup.sh > backup.log 2>&1` |

A classic from everyday admin work, the IP addresses with the most requests:

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head
```

```text
      4 198.51.100.23
      2 192.0.2.77
      2 192.0.2.10
      1 192.0.2.55
```

`awk` takes the first column (the IP), `sort` groups identical addresses, `uniq -c`
counts them, `sort -rn` puts the highest number on top and `head` keeps the top 10.

!!! tip "Learning path"
    The commands are sorted from simple to more complex. Work through them in order,
    since later pages build on the earlier ones.
