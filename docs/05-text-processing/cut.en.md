# cut

> Cuts columns or character ranges out of each line.

![cut output](../assets/screenshots/05-text-processing/cut.png)

## Syntax

```bash
cut OPTION... [FILE]...
```

## Options

| Option | Description |
|--------|-------------|
| `-d CHAR`, `--delimiter=CHAR` | Column separator (default: tab) |
| `-f LIST`, `--fields=LIST` | Columns to keep: `1`, `1,3`, `2-4`, `3-` |
| `-c LIST`, `--characters=LIST` | Character positions to keep: `1-10`, `5-` |
| `--complement` | Keep everything **except** the selected columns |
| `--output-delimiter=TEXT` | Separator between columns in the output |

## Examples

**Show all user names:**

```bash
cut -d: -f1 /etc/passwd | head -n 3
```

```text
root
daemon
bin
```

**Show user name and login shell:**

```bash
cut -d: -f1,7 /etc/passwd | grep bash
```

```text
root:/bin/bash
nox:/bin/bash
```

**Take columns from a CSV file:**

```bash
cut -d, -f2,3 users.csv
```

```text
name,email
nox,nox@example.com
alice,alice@example.com
bob,bob@example.com
```

**Show only the IP addresses of a log:**

```bash
cut -d' ' -f1 /var/log/nginx/access.log | head -n 3
```

```text
192.0.2.10
192.0.2.10
198.51.100.23
```

**Cut out the time stamp by character position:**

```bash
cut -c1-19 deploy.log
```

```text
2026-10-26 10:40:01
2026-10-26 10:40:12
2026-10-26 10:40:15
```

**Show only the paths from the output of `du`:**

```bash
du -sh /srv/* | cut -f2
```

```text
/srv/README
/srv/backup
/srv/logs
/srv/www
```

`du` separates its columns with a tab, which is the default separator of `cut`.

## When do I need it?

- To get single columns from `/etc/passwd`, CSV exports or the output of other commands
- To extract IP addresses, status codes or time stamps from logs for further processing
- In scripts that need one value from a line

!!! tip "Several spaces in a row: use `awk`"
    `cut -d' '` treats every single space as a separator. If columns are aligned with
    several spaces, the counting gets mixed up. `awk` handles this correctly.

!!! warning "CSV files with commas in values"
    A value like `"Smith, John"` contains a comma, and `cut -d,` splits it in two. For
    real CSV data with quotes, use a tool that understands CSV.

## Related commands

[sort](sort.md) · [uniq](uniq.md) · [tr](tr.md) · [column](column.md)
