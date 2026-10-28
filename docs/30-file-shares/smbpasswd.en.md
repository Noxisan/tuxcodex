# smbpasswd

> Manages Samba users: add a Linux user to Samba, set the password, disable or delete the account.

![smbpasswd output](../assets/screenshots/30-file-shares/smbpasswd.png)

## Syntax

```bash
smbpasswd [-a | -x | -d | -e] [USER]
```

## Options

| Option | Description |
|--------|-------------|
| `-a USER` | Add a user to Samba and set the password |
| `USER` | As root: set a new password for the user |
| `-d`, `-e` | Disable or enable the account |
| `-x USER` | Delete the user from Samba |
| `-s` | Read the password from stdin, without a prompt (for scripts) |

Without arguments, a user changes their own Samba password. Samba keeps its own passwords: the Linux password from `passwd` isn't used.

## Examples

**Add a user to Samba:**

```bash
sudo smbpasswd -a nox
```

```text
New SMB password:
Retype new SMB password:
Added user nox.
```

**The user doesn't exist on the system:**

```bash
sudo smbpasswd -a anna
```

```text
New SMB password:
Retype new SMB password:
Failed to add entry for user anna.
```

First `sudo useradd -M -s /usr/sbin/nologin anna`, then `smbpasswd -a` again.

**Reset a forgotten password:**

```bash
sudo smbpasswd nox
```

```text
New SMB password:
Retype new SMB password:
```

**Disable an account and enable it again:**

```bash
sudo smbpasswd -d nox
sudo smbpasswd -e nox
```

```text
Disabled user nox.
Enabled user nox.
```

**All Samba users:**

```bash
sudo pdbedit -L
```

```text
nox:1000:
anna:1001:
```

**Delete a user from Samba:**

```bash
sudo smbpasswd -x anna
```

```text
Deleted user anna.
```

## When do I need it?

- When a new colleague needs access to a share
- When someone forgot the password for the share
- When someone leaves: disable or delete the account

!!! tip "List all Samba users"
    `sudo pdbedit -L` lists all users in the Samba database, `sudo pdbedit -L -v nox`
    shows details such as the account flags.

!!! warning "The Linux user must exist"
    `smbpasswd -a` only works for users that exist on the system. Create them first with
    [`useradd`](../07-users-groups/useradd.md), ideally with `-s /usr/sbin/nologin` if they
    only need the share.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `samba-common-bin` | `samba-common-bin` | `samba-common-tools` | `samba` |

## Related commands

[testparm](testparm.md) · [smbclient](smbclient.md) · [useradd](../07-users-groups/useradd.md) · [passwd](../07-users-groups/passwd.md)
