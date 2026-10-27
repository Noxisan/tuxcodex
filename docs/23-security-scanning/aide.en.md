# aide

> Saves checksums and attributes of important files in a database and later reports every file that was added, removed or changed.

![aide output](../assets/screenshots/23-security-scanning/aide.png)

## Syntax

```bash
aide --init | --check | --update [--config FILE]
```

## Options

| Option | Description |
|--------|-------------|
| `--init` | Create a new database (`aide.db.new`) |
| `--check` | Compare the files with the database |
| `--update` | Check and write a new database with the current state |
| `--config FILE` | Configuration, on Debian `/etc/aide/aide.conf` |
| `--limit PATH` | Only check this path |

On Debian and Ubuntu, `aideinit` creates the first database and `/etc/cron.daily/dailyaidecheck` checks every day. After `--init`, copy `aide.db.new` to `aide.db`.

## Examples

**Create the database:**

```bash
sudo aide --init --config /etc/aide/aide.conf | head -6
sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db
```

```text
Start timestamp: 2026-10-26 10:42:17 +0100 (AIDE 0.19.1)
AIDE successfully initialized database.
New AIDE database written to /var/lib/aide/aide.db.new
Ignored e2fs attributes: EINV

Number of entries:      20077
```

**Check the system:**

```bash
sudo aide --check --config /etc/aide/aide.conf | head -24
```

```text
Start timestamp: 2026-10-27 03:15:02 +0100 (AIDE 0.19.1)
AIDE found differences between database and filesystem!!
Ignored e2fs attributes: EINV

Summary:
  Total number of entries:      20078
  Added entries:                1
  Removed entries:              0
  Changed entries:              2

---------------------------------------------------
Added entries:
---------------------------------------------------

f++++++++++++++++++: /usr/local/bin/sysupdate

---------------------------------------------------
Changed entries:
---------------------------------------------------

f >.... mc..H.. .  : /etc/ssh/ssh_config
d >.... mc.. .. .  : /usr/local/bin
```

A new program in `/usr/local/bin` that nobody installed, and a changed SSH configuration: exactly what AIDE is for. `cat /usr/local/bin/sysupdate` shows what it does.

**The details of a changed file:**

```bash
sudo aide --check --config /etc/aide/aide.conf | grep -A6 '^File: /etc/ssh/ssh_config'
```

```text
File: /etc/ssh/ssh_config
 Size      : 1650                             | 1670
 Mtime     : 2026-08-13 10:00:00 +0200        | 2026-10-27 01:12:44 +0100
 Ctime     : 2026-08-13 10:00:00 +0200        | 2026-10-27 01:12:44 +0100
 SHA256    : RMkYV/NLHsaOJG68utZsS5OAtBw0kMcZ | zm2eKuUrRACjhxL0sGrltdYuiGeT8gW4
             vf1mlrp7QLU=                     | xMN9K5VYv90=
```

## When do I need it?

- To notice when someone changes system programs or configuration files
- For compliance requirements such as PCI DSS that demand file integrity monitoring
- After an incident, to see exactly which files were changed

!!! tip "Keep a copy of the database elsewhere"
    An attacker with root rights can also update the AIDE database. Copy `aide.db` to
    another machine or read-only media after every update.

!!! warning "After updates: --update"
    Every package update changes files that AIDE watches. Run `aide --update` after
    updates, check the report, and take over the new database. Otherwise the real changes
    disappear in the noise.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Install | `sudo apt install aide` | `sudo apt install aide` | `sudo dnf install aide` | AUR |

## Related commands

[debsums](debsums.md) · [rkhunter](rkhunter.md) · [lynis](lynis.md) · [sha256sum](../14-archives/sha256sum.md)
