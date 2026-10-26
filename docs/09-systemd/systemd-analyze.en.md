# systemd-analyze

> Analyzes the boot process and unit files: what made the boot slow, in which order services start, and whether a unit file or a time specification is correct.

![systemd-analyze output](../assets/screenshots/09-systemd/systemd-analyze.png)

## Syntax

```bash
systemd-analyze [OPTION]... [COMMAND] [ARGUMENT]...
```

## Options

| Command | Description |
|---------|-------------|
| *(none)*, `time` | Total boot time, split into kernel, initrd and userspace |
| `blame` | Start time of every unit, slowest first |
| `critical-chain [UNIT]` | The chain of units that the boot or a unit had to wait for |
| `verify FILE` | Check a unit file for errors |
| `calendar EXPRESSION` | Check a time specification for timers and show the next run |
| `security [UNIT]` | Rate the sandboxing settings of services |

## Examples

**Show how long the boot took:**

```bash
systemd-analyze
```

```text
Startup finished in 1.912s (kernel) + 2.604s (initrd) + 5.317s (userspace) = 9.834s
multi-user.target reached after 5.301s in userspace.
```

**Show which units took the longest to start:**

```bash
systemd-analyze blame | head -n 5
```

```text
4.211s postgresql@17-main.service
1.028s networking.service
 498ms php8.4-fpm.service
 351ms apparmor.service
 312ms nginx.service
```

**Show what a service had to wait for:**

```bash
systemd-analyze critical-chain nginx.service
```

```text
The time when unit became active or started is printed after the "@" character.
The time the unit took to start is printed after the "+" character.

nginx.service +312ms
└─network-online.target @3.902s
  └─networking.service @2.871s +1.028s
    └─apparmor.service @2.512s +351ms
      └─local-fs.target @2.498s
```

`@` is the point in time after boot, `+` the time the unit itself needed.

**Check a time specification before you put it into a timer:**

```bash
systemd-analyze calendar "Mon..Fri 03:00"
```

```text
  Original form: Mon..Fri 03:00
Normalized form: Mon..Fri *-*-* 03:00:00
    Next elapse: Tue 2026-10-27 03:00:00 CET
       (in UTC): Tue 2026-10-27 02:00:00 UTC
       From now: 16h left
```

**Check your own unit file:**

```bash
systemd-analyze verify /etc/systemd/system/backup.service
```

```text
backup.service: Command /usr/local/bin/backup.sh is not executable: No such file or directory
```

The script doesn't exist yet, or the path has a typo.

## When do I need it?

- When the server takes long to boot and you want to know which service is to blame
- When a service starts too early, for example before the network is ready
- Before enabling your own unit or timer, to catch errors in advance

!!! tip "`blame` isn't everything"
    Services start in parallel. A unit with a long time in `blame` doesn't necessarily
    delay the boot. `critical-chain` shows what the boot really waited for.

!!! tip "Test timers with `calendar`"
    `systemd-analyze calendar` also accepts `--iterations=5` and then shows the next five
    runs. This lets you check complicated expressions like `*-*-1,15 04:30`.

## Related commands

[systemctl](systemctl.md) · [journalctl](journalctl.md) · [uptime](../01-orientation/uptime.md) · [systemd-run](systemd-run.md)
