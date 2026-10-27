# Understanding SELinux and AppArmor

Normal Linux permissions (owner, group, `rwx`) are **discretionary**: the owner of a file
decides. SELinux and AppArmor add **mandatory** rules on top that even root can't simply
ignore. If nginx is taken over, it can still only touch what the policy allows for nginx,
not `/etc/shadow` and not your SSH keys.

## Two systems, one goal

| | SELinux | AppArmor |
|---|---------|----------|
| Principle | Every file, process and port has a **label** (context); the policy says which labels may access which | Every program has a **profile** with the paths it may use |
| Active by default on | RHEL, Rocky, Alma, Fedora | Debian, Ubuntu, SUSE |
| Strength | Very fine-grained, covers the whole system | Easier to read and write |
| Typical problem | Files with the wrong label, for example after `mv` | A program uses a path that isn't in its profile |

## Which distribution uses what

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Active by default | AppArmor | AppArmor | SELinux (enforcing) | none |
| Tools | `apparmor-utils` | `apparmor-utils` (preinstalled) | `policycoreutils` (preinstalled), `policycoreutils-python-utils` for `semanage` and `audit2allow` | AppArmor possible: package `apparmor` plus kernel parameter `lsm=` |
| Denials are logged in | `journalctl -k`, `/var/log/kern.log` | `journalctl -k`, `/var/log/kern.log` | `/var/log/audit/audit.log` | `journalctl -k` |

## SELinux in three terms

```text
system_u:object_r:httpd_sys_content_t:s0
   │         │            │            └─ level (MLS, rarely relevant)
   │         │            └─ type: this is what the rules are about
   │         └─ role
   └─ user
```

| Term | Example | Meaning |
|------|---------|---------|
| **Type** of a file | `httpd_sys_content_t` | Web content that the web server may read |
| **Domain** of a process | `httpd_t` | nginx and Apache run in this domain |
| **Boolean** | `httpd_can_network_connect` | A switch for a common exception, such as "web server may connect to other servers" |

`ls -Z` shows the label of files, `ps -eZ` that of processes.

## From a denial to a fix

```text
"Permission denied" in the service log, although chmod/chown are right
   │
   ├─ 1. Is it SELinux/AppArmor?    getenforce · aa-status · ausearch -m AVC
   ├─ 2. What exactly was denied?   ausearch -m AVC -ts recent · audit2why
   └─ 3. Fix it in this order:
          a) wrong file label   → semanage fcontext + restorecon
          b) unusual port       → semanage port
          c) known exception    → setsebool -P
          d) only if nothing fits → audit2allow -M (own policy module)
```

The quick test: `setenforce 0` (SELinux) or `aa-complain` (AppArmor). If the problem is
gone, it was the access control. Switch it back on right away and fix it properly.

!!! tip "Read the denial before you act"
    `audit2why` explains each SELinux denial in plain words and often names the boolean
    that fixes it. That's usually a one-line solution.

!!! danger "Don't switch it off permanently"
    `SELINUX=disabled` or removing AppArmor makes the error go away, and with it the
    protection that limits the damage of a hacked service. On RHEL, re-enabling SELinux
    later requires relabeling the whole file system.
