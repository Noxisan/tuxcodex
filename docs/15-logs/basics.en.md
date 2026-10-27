# Understanding logs

Logs are the memory of a server: what services did, which errors occurred, who logged
in. Linux has two places for them: the **systemd journal** and classic text files in
**`/var/log`**.

## Journal or text file?

| Source | Where | Read with |
|--------|-------|-----------|
| systemd journal | Binary files in `/var/log/journal/` | [`journalctl`](../09-systemd/journalctl.md) |
| rsyslog | Text files like `/var/log/syslog` or `/var/log/messages` | `less`, `tail`, `grep` |
| Applications | Own files, e.g. `/var/log/nginx/`, `/var/log/postgresql/` | `less`, `tail`, `grep` |

Almost all system services log to the journal. Whether rsyslog also writes text files
depends on the distribution:

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| rsyslog installed | no | yes | yes | no |
| General system log | journal only | `/var/log/syslog` | `/var/log/messages` | journal only |
| Logins and `sudo` | journal only | `/var/log/auth.log` | `/var/log/secure` | journal only |
| Package manager | `/var/log/apt/history.log`, `/var/log/dpkg.log` | `/var/log/apt/history.log`, `/var/log/dpkg.log` | `/var/log/dnf.log` | `/var/log/pacman.log` |
| Kernel | journal, `dmesg` | `/var/log/kern.log`, `dmesg` | journal, `dmesg` | journal, `dmesg` |

## Log levels

Every message has a priority. `journalctl -p` and many tools filter by it:

| Level | Name | Meaning |
|-------|------|---------|
| 0 | `emerg` | The system is unusable |
| 1 | `alert` | Action must be taken immediately |
| 2 | `crit` | Critical condition, e.g. hardware failure |
| 3 | `err` | Error |
| 4 | `warning` | Warning |
| 5 | `notice` | Normal, but significant |
| 6 | `info` | Information |
| 7 | `debug` | Debug messages |

`journalctl -p warning` shows levels 0 to 4, everything from warnings upwards.

## Log rotation

Log files grow endlessly. **logrotate** runs once a day and, according to its rules in
`/etc/logrotate.d/`, renames the current file (`access.log` becomes `access.log.1`),
compresses older ones (`access.log.2.gz`) and deletes the oldest. The journal limits its
size itself, see `SystemMaxUse=` in `/etc/systemd/journald.conf`.

## Failed logins

Without `/var/log/auth.log` and without `lastb` (no longer available on Debian 13), the
journal shows failed SSH logins:

```text
$ journalctl -u ssh --since today | grep "Failed password"
Oct 26 09:58:02 tuxcodex-srv sshd-session[2187]: Failed password for nox from 192.0.2.45 port 51720 ssh2
Oct 26 10:31:02 tuxcodex-srv sshd-session[3301]: Failed password for invalid user admin from 198.51.100.66 port 40218 ssh2
Oct 26 10:31:05 tuxcodex-srv sshd-session[3301]: Failed password for invalid user admin from 198.51.100.66 port 40218 ssh2
```

`invalid user` means: the account doesn't exist, typical for automated attacks. Tools
like [`fail2ban-client`](../12-ssh/fail2ban-client.md) and [`faillock`](faillock.md)
react to such attempts.

!!! tip "Look at the time first"
    When something went wrong, note the time and look at all logs around it:
    `journalctl --since "10:25" --until "10:35"` shows every service in that window.

!!! warning "Logs contain personal data"
    IP addresses, user names and URLs in logs are personal data. Keep them only as long
    as you need them, and protect access: on Debian and Ubuntu, only the group `adm` may
    read most of `/var/log`.
