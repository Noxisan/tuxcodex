# faillock

> Shows failed login attempts per user and unlocks accounts that were locked after too many wrong passwords.

![faillock output](../assets/screenshots/15-logs/faillock.png)

## Syntax

```bash
faillock [--user USER] [--reset]
```

`faillock` belongs to the PAM module `pam_faillock`. It only counts and locks if that module is enabled in the PAM configuration, see the table.

## Options

| Option | Description |
|--------|-------------|
| *(none)* | Failed attempts of all users |
| `--user USER` | Only this user |
| `--reset` | Delete the failed attempts and unlock the account |

## Examples

**Show the failed attempts of a user:**

```bash
sudo faillock --user alice
```

```text
alice:
When                Type  Source                                           Valid
2026-10-26 10:31:02 RHOST 198.51.100.66                                        V
2026-10-26 10:31:05 RHOST 198.51.100.66                                        V
2026-10-26 10:31:09 RHOST 198.51.100.66                                        V
```

Three attempts from the same address within seconds, `V` marks them as valid for the count.
With `deny = 3`, the account is now locked.

**Unlock the account:**

```bash
sudo faillock --user alice --reset
sudo faillock --user alice
```

```text
alice:
When                Type  Source                                           Valid
```

**Check the limits:**

```bash
grep -v '^#' /etc/security/faillock.conf | grep .
```

```text
deny = 3
unlock_time = 600
fail_interval = 900
```

Three failed attempts within 15 minutes lock the account for 10 minutes.

## When do I need it?

- When a user can't log in anymore after mistyping the password several times
- To see from where someone tried to log in to an account
- To unlock an account after checking that the attempts were harmless

!!! tip "Settings in `faillock.conf`"
    How many attempts lead to a lock and how long it lasts is set in
    `/etc/security/faillock.conf`.

!!! warning "Only local and PAM logins"
    Failed SSH logins with keys or of non-existing users don't appear here. For SSH attacks,
    look at the journal and use [`fail2ban-client`](../12-ssh/fail2ban-client.md).

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| `pam_faillock` active by default | no | no | no, `sudo authselect enable-feature with-faillock` | yes |

## Related commands

[passwd](../07-users-groups/passwd.md) · [fail2ban-client](../12-ssh/fail2ban-client.md) · [last](../01-orientation/last.md)
