# Understanding scheduling

Linux has two systems for recurring jobs: the classic **cron** and **systemd timers**.
For a job that runs only once, there is **at**.

## The cron syntax

Every cron line has five time fields, followed by the command:

```text
┌───────────── minute        0-59
│ ┌─────────── hour          0-23
│ │ ┌───────── day of month  1-31
│ │ │ ┌─────── month         1-12
│ │ │ │ ┌───── day of week   0-7 (0 and 7 are Sunday)
│ │ │ │ │
* * * * * command
```

| Expression | Meaning |
|------------|---------|
| `*/5 * * * *` | Every 5 minutes |
| `0 * * * *` | Every full hour |
| `30 3 * * *` | Every day at 03:30 |
| `0 3 * * 1-5` | Monday to Friday at 03:00 |
| `0 22 * * 0` | Every Sunday at 22:00 |
| `0 4 1 * *` | On the first of every month at 04:00 |
| `@reboot` | Once after every boot |

[crontab.guru](https://crontab.guru) explains any expression in plain English.

## Where cron jobs live

| Place | For | Format |
|-------|-----|--------|
| `crontab -e` | Jobs of a single user | Five time fields and command |
| `/etc/crontab` | System jobs | Five time fields, **user**, command |
| `/etc/cron.d/` | System jobs of packages and admins, one file per job | like `/etc/crontab` |
| `/etc/cron.hourly/`, `daily/`, `weekly/`, `monthly/` | Scripts that simply run once per period | Executable scripts, no time fields |

An example file `/etc/cron.d/backup`:

```text
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MAILTO=admin@example.com

30 3 * * * root /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```

## systemd timers

A timer consists of two units: a `.service` that does the work and a `.timer` that says
when. `/etc/systemd/system/backup.timer`:

```text
[Unit]
Description=Nightly backup

[Timer]
OnCalendar=*-*-* 03:30:00
Persistent=true
RandomizedDelaySec=10min

[Install]
WantedBy=timers.target
```

Together with the `backup.service` from the basics of the chapter
[systemd](../09-systemd/basics.md), `sudo systemctl enable --now backup.timer` activates
it, and `systemctl list-timers` shows the next run.

## cron or systemd timer?

| | cron | systemd timer |
|---|------|---------------|
| Set up | One line | Two unit files |
| Output and errors | By mail, or lost | In the journal: `journalctl -u backup` |
| Missed runs (server was off) | Only with anacron | `Persistent=true` |
| Resource limits, dependencies | No | Like every systemd service |
| Run a job right now for a test | Run the command by hand | `systemctl start backup.service` |

For new jobs on servers, timers are the better choice. cron is simpler and still everywhere.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| cron installed | yes, package `cron` | yes, package `cron` | yes, package `cronie` | no, package `cronie` |
| Service | `cron` | `cron` | `crond` | `cronie` |
| `at` installed | no, package `at` | no, package `at` | no, package `at` | no, package `at` |
| Daily jobs run by | cron, anacron if installed | cron, anacron if installed | anacron (`cronie-anacron`) | anacron (part of `cronie`) |

!!! tip "Absolute paths and a full environment"
    cron runs jobs with a minimal environment: a short `PATH`, no aliases, no variables
    from your login shell. Use absolute paths in cron jobs, or set `PATH` at the top of
    the crontab.

!!! warning "Output goes somewhere"
    Without redirection, cron sends the output of a job by mail to the user. Without a
    mail system, it is lost. Redirect it into a log file, or use `logger` or
    `systemd-cat` to send it to the journal.
