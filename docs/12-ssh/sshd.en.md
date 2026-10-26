# sshd

> The SSH server. You rarely start it by hand, but you use it to check its configuration before you reload the service.

![sshd output](../assets/screenshots/12-ssh/sshd.png)

## Syntax

```bash
sshd [OPTION]...
```

The configuration is in `/etc/ssh/sshd_config`. Your own settings belong into a file in `/etc/ssh/sshd_config.d/`, which survives package updates.

## Options

| Option | Description |
|--------|-------------|
| `-t` | Test the configuration, print nothing if it is correct |
| `-T` | Print the effective configuration, all settings in lower case |
| `-T -C user=NAME,host=HOST,addr=IP` | Effective configuration for a specific connection (`Match` blocks) |
| `-d` | Debug mode in the foreground, for one connection |

Important settings:

| Setting | Recommended | Meaning |
|---------|-------------|---------|
| `PermitRootLogin` | `no` | No direct login as root, use `sudo` |
| `PasswordAuthentication` | `no` | Only keys, no passwords |
| `MaxAuthTries` | `3` | Login attempts per connection |
| `AllowUsers` | your users | Only these users may log in |
| `X11Forwarding` | `no` | No graphical programs, not needed on servers |

## Examples

**Show the current effective settings:**

```bash
sudo sshd -T | grep -E "^(port|permitrootlogin|passwordauthentication|pubkeyauthentication|kbdinteractiveauthentication|x11forwarding|maxauthtries) "
```

```text
port 22
maxauthtries 6
permitrootlogin without-password
pubkeyauthentication yes
passwordauthentication yes
kbdinteractiveauthentication no
x11forwarding yes
```

**A hardening file:**

```bash
cat /etc/ssh/sshd_config.d/10-hardening.conf
```

```text
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
MaxAuthTries 3
X11Forwarding no
AllowUsers nox alice
```

On Debian and Ubuntu, files in `sshd_config.d/` are read first, and the **first** value
found for a setting wins. That's why your own file overrides the defaults further down.

**Test the configuration before reloading:**

```bash
sudo sshd -t && echo "config ok"
```

```text
config ok
```

**A typo in the configuration:**

```bash
sudo sshd -t
```

```text
/etc/ssh/sshd_config.d/10-hardening.conf line 1: unsupported option "noo".
```

With this error, `sshd` wouldn't start at all. Fix the line and test again before you
reload the service.

**Reload and check the result:**

```bash
sudo systemctl reload ssh
sudo sshd -T | grep -E "^(port|permitrootlogin|passwordauthentication|pubkeyauthentication|kbdinteractiveauthentication|x11forwarding|maxauthtries) "
```

```text
port 22
maxauthtries 3
permitrootlogin no
pubkeyauthentication yes
passwordauthentication no
kbdinteractiveauthentication no
x11forwarding no
```

## When do I need it?

- When setting up a new server: switch off root and password login
- Before every reload of the SSH service, to rule out typos
- To find out which value really applies when several files set the same option

!!! tip "Reload instead of restart"
    `sudo systemctl reload ssh` reads the configuration again without ending existing
    connections. Your current session stays open even if the new settings are wrong.

!!! danger "Test in a second session"
    After switching off password login, open a **new** SSH session before closing the old
    one. If the new one fails, you can still undo the change in the old session.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Service | `ssh` | `ssh` | `sshd` | `sshd` |
| Reload | `sudo systemctl reload ssh` | `sudo systemctl reload ssh` | `sudo systemctl reload sshd` | `sudo systemctl reload sshd` |

## Related commands

[ssh](ssh.md) · [systemctl](../09-systemd/systemctl.md) · [journalctl](../09-systemd/journalctl.md) · [ssh-keyscan](ssh-keyscan.md) · [fail2ban-client](fail2ban-client.md)
