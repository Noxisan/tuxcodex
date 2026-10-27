# aa-complain

> On Debian and Ubuntu: switches AppArmor profiles to complain mode (only log) or back to enforce mode.

![aa-complain output](../assets/screenshots/25-selinux-apparmor/aa-complain.png)

## Syntax

```bash
aa-complain PROFILE|PROGRAM...
aa-enforce PROFILE|PROGRAM...
aa-disable PROFILE...
```

## Options

| Option | Description |
|--------|-------------|
| `aa-complain` | Only log violations, don't block |
| `aa-enforce` | Apply the profile again |
| `aa-disable` | Unload the profile completely |
| `aa-logprof` | Go through the logged violations and add them to the profile interactively |
| `apparmor_parser -r FILE` | Reload a profile after editing it |

Small additions belong in `/etc/apparmor.d/local/` (for example `local/usr.sbin.nginx`), so package updates don't overwrite them.

## Examples

**Put nginx into complain mode for a test:**

```bash
sudo aa-complain /usr/sbin/nginx
```

```text
Setting /usr/sbin/nginx to complain mode.
```

**Allow a directory and switch back:**

```bash
echo '/srv/status/** r,' | sudo tee -a /etc/apparmor.d/local/usr.sbin.nginx
sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx
sudo aa-enforce /usr/sbin/nginx
```

```text
/srv/status/** r,
Setting /usr/sbin/nginx to enforce mode.
```

**Check the mode afterwards:**

```bash
sudo aa-status | grep -A1 'complain mode'
```

```text
1 profiles are in complain mode.
   /usr/sbin/php-fpm8.4
```

## When do I need it?

- To test whether AppArmor causes an error, without switching it off for everything
- To learn what a program needs: complain mode, use it, then `aa-logprof`
- To switch back to enforce mode after the profile was adjusted

!!! tip "Local additions instead of editing the profile"
    A line like `/srv/status/** r,` in `/etc/apparmor.d/local/usr.sbin.nginx` plus
    `sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx` allows nginx to read the new
    directory and survives updates.

!!! warning "Complain mode protects nothing"
    In complain mode, the profile only writes log entries. Switch back with `aa-enforce` as
    soon as the test is done.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| AppArmor | active | active | not available (SELinux instead) | possible, kernel parameter `lsm=` needed |
| Package | `sudo apt install apparmor-utils` | `apparmor-utils`, preinstalled | not available | `sudo pacman -S apparmor` |

## Related commands

[aa-status](aa-status.md) · [setenforce](setenforce.md) · [systemctl](../09-systemd/systemctl.md)
