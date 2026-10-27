# restorecon

> On RHEL, Rocky and Alma: resets the SELinux labels of files to what the rules say they should be.

![restorecon output](../assets/screenshots/25-selinux-apparmor/restorecon.png)

## Syntax

```bash
restorecon [-R] [-v] [-n] PATH...
```

## Options

| Option | Description |
|--------|-------------|
| `-R` | Recursively, including all files below |
| `-v` | Show every changed label |
| `-n` | Only show what would change |
| `-F` | Also reset the user and role parts of the label |

`ls -Z` shows the label of a file, `matchpathcon PATH` the label it should have.

## Examples

**Apply the labels to a directory:**

```bash
sudo restorecon -Rv /srv/status
```

```text
Relabeled /srv/status from unconfined_u:object_r:var_t:s0 to unconfined_u:object_r:httpd_sys_content_t:s0
Relabeled /srv/status/index.html from unconfined_u:object_r:var_t:s0 to unconfined_u:object_r:httpd_sys_content_t:s0
```

**Wrong label after mv:**

```bash
mv ~/index.html /var/www/html/
ls -Z /var/www/html/index.html
matchpathcon /var/www/html/index.html
```

```text
unconfined_u:object_r:user_home_t:s0 /var/www/html/index.html
/var/www/html/index.html  system_u:object_r:httpd_sys_content_t:s0
```

The file still has the label of the home directory (`user_home_t`), nginx may not read it. `sudo restorecon -v /var/www/html/index.html` fixes it.

**Only show what would change:**

```bash
sudo restorecon -Rnv /var/www
```

```text
Would relabel /var/www/html/index.html from unconfined_u:object_r:user_home_t:s0 to unconfined_u:object_r:httpd_sys_content_t:s0
```

## When do I need it?

- After `semanage fcontext`, to apply new rules to existing files
- After moving files with `mv`: they keep their old label from the source directory
- When a service suddenly can't read its files after a restore from backup

!!! tip "cp instead of mv"
    `cp` creates files with the label of the target directory, `mv` keeps the old label. That's
    why files moved from your home directory to `/var/www` often don't work. `restorecon`
    repairs it.

!!! warning "Relabel the whole system"
    After SELinux was disabled, `touch /.autorelabel` and a reboot relabel the whole file
    system. That can take a long time on large disks; plan a maintenance window.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| SELinux | not active (AppArmor instead) | not active (AppArmor instead) | active, `enforcing` | not active |
| Package | `selinux-utils` (only if SELinux is set up) | `selinux-utils` (only if SELinux is set up) | `libselinux-utils`, preinstalled | not in the official repositories |

## Related commands

[semanage](semanage.md) · [audit2allow](audit2allow.md) · [ls](../02-navigation/ls.md) · [mv](../03-files/mv.md)
