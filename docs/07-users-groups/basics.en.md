# The important files

| File | Contents |
|------|----------|
| `/etc/passwd` | All user accounts: name, UID, GID, home directory, shell |
| `/etc/shadow` | Password hashes and password ageing, only readable by `root` |
| `/etc/group` | All groups and their additional members |
| `/etc/gshadow` | Group passwords and group administrators |
| `/etc/sudoers` | Who may use `sudo` for what, only edit with `visudo` |
| `/etc/sudoers.d/` | Additional `sudo` rules as separate files |
| `/etc/skel/` | Template files that are copied into every new home directory |
| `/etc/login.defs` | Defaults: UID ranges, password ageing, `umask` |
| `/etc/adduser.conf` | Defaults for `adduser` and `addgroup` on Debian and Ubuntu |

A line in `/etc/passwd`, field by field:

```text
nox:x:1000:1000:Nox,,,:/home/nox:/bin/bash
 │  │  │    │     │       │         └ login shell
 │  │  │    │     │       └ home directory
 │  │  │    │     └ full name and contact details (GECOS)
 │  │  │    └ GID of the primary group
 │  │  └ UID
 │  └ x = the password is in /etc/shadow
 └ user name
```

| UID range | Meaning |
|-----------|---------|
| `0` | `root` |
| `1` to `999` | System users for services, like `www-data` (33) or `sshd` |
| `1000` and above | Normal users (up to `59999` on Debian and Ubuntu, `60000` on RHEL and Arch) |
| `65534` | `nobody`, a user without any rights |

!!! tip "Never edit the files directly"
    Use the commands of this chapter instead of editing `/etc/passwd`, `/etc/shadow` or
    `/etc/group` with an editor. They lock the files and keep all of them consistent. If
    you really have to, use `vipw` and `vigr`.
