# date

> Shows the current date and time in any format, and calculates other points in time.

## Syntax

```bash
date [OPTION]... [+FORMAT]
```

## Options

| Option | Description |
|--------|-------------|
| `+FORMAT` | Print the date in your own format (see below) |
| `-d`, `--date=STRING` | Show the date described by `STRING` instead of now (`yesterday`, `+30 days`, `@1793007737`) |
| `-u`, `--utc` | Show the time in UTC |
| `-I[FMT]`, `--iso-8601[=FMT]` | ISO 8601 format; `FMT` is `date`, `hours`, `minutes`, `seconds` or `ns` |
| `-R`, `--rfc-email` | Format used in e-mail headers (`Mon, 26 Oct 2026 10:42:17 +0100`) |
| `-r`, `--reference=FILE` | Show the last modification time of `FILE` |
| `-s`, `--set=STRING` | Set the system time (root only) |

The most important format specifiers:

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `%Y` / `%m` / `%d` | Year / month / day | `2026` / `10` / `26` |
| `%H` / `%M` / `%S` | Hour / minute / second | `10` / `42` / `17` |
| `%F` | Date, same as `%Y-%m-%d` | `2026-10-26` |
| `%T` | Time, same as `%H:%M:%S` | `10:42:17` |
| `%a` / `%A` | Weekday, short / long | `Mon` / `Monday` |
| `%Z` / `%z` | Time zone name / offset | `CET` / `+0100` |
| `%s` | Seconds since 1970-01-01 UTC (Unix time) | `1793007737` |

## Examples

**Show the current date and time:**

```bash
date
```

```text
Mon Oct 26 10:42:17 CET 2026
```

**Show the time in UTC:**

```bash
date -u
```

```text
Mon Oct 26 09:42:17 UTC 2026
```

**Use a date in a file name:**

```bash
echo "backup-$(date +%F).tar.gz"
```

```text
backup-2026-10-26.tar.gz
```

**Create a timestamp for log messages:**

```bash
date '+%F %T'
```

```text
2026-10-26 10:42:17
```

**Calculate a date in the past or future:**

```bash
date -d yesterday +%F
date -d '+30 days'
```

```text
2026-10-25
Wed Nov 25 10:42:17 CET 2026
```

**Convert a Unix timestamp into a readable date:**

```bash
date -d @1793007737
```

```text
Mon Oct 26 10:42:17 CET 2026
```

![date output](../assets/screenshots/01-orientation/date.png)

## When do I need it?

- To check the server's time and time zone before you compare log entries
- For file names of backups and exports (`backup-2026-10-26.tar.gz`), which sort
  correctly when you use `%F`
- For timestamps in your own scripts and log messages
- To convert Unix timestamps from logs, databases or APIs into a readable date
- To calculate dates, for example "delete everything older than 30 days"

!!! tip "Use `%F` for file names"
    `%F` (`2026-10-26`) sorts correctly with `ls` and does not contain spaces or
    colons. Formats like `26.10.2026` end up in the wrong order.

!!! warning "Escape `%` in crontab"
    In a crontab, `%` has a special meaning and starts a new line. Write `\%` there:
    `tar -czf /backup/etc-$(date +\%F).tar.gz /etc`

!!! warning "Don't set the time with `date -s`"
    On servers, the time is kept correct by NTP. Use `timedatectl`
    to set time zone and synchronization instead of changing the clock by hand.

## Related commands

[uptime](uptime.md)
