---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-account-multiple-outline:{ .tc-hero-icon }

# Users and groups

Creating, changing and deleting users and groups, managing passwords and working with
root rights through `sudo` and `su`.

</div>

## Look up users and groups

<div class="grid cards" markdown>

-   :material-account-group:{ .lg .middle } **[groups](groups.md)**

    ---

    Show the groups a user belongs to.

-   :material-account-search-outline:{ .lg .middle } **[getent](getent.md)**

    ---

    Look up users, groups, hosts and services.

</div>

## Manage users

<div class="grid cards" markdown>

-   :material-account-plus-outline:{ .lg .middle } **[adduser](adduser.md)**

    ---

    Create a new user step by step (Debian).

-   :material-account-plus:{ .lg .middle } **[useradd](useradd.md)**

    ---

    Create a user in one command, for scripts and every distribution.

-   :material-account-edit-outline:{ .lg .middle } **[usermod](usermod.md)**

    ---

    Change groups, shell, name or lock of a user.

-   :material-form-textbox-password:{ .lg .middle } **[passwd](passwd.md)**

    ---

    Set, lock, unlock or expire a password.

-   :material-calendar-clock-outline:{ .lg .middle } **[chage](chage.md)**

    ---

    Set password ageing and account expiry.

-   :material-account-minus-outline:{ .lg .middle } **[deluser](deluser.md)**

    ---

    Delete a user or remove it from a group (Debian).

-   :material-account-remove-outline:{ .lg .middle } **[userdel](userdel.md)**

    ---

    Delete a user account on every distribution.

</div>

## Manage groups

<div class="grid cards" markdown>

-   :material-account-multiple-plus-outline:{ .lg .middle } **[addgroup](addgroup.md)**

    ---

    Create a group or add a user to it (Debian).

-   :material-account-multiple-plus:{ .lg .middle } **[groupadd](groupadd.md)**

    ---

    Create a group on every distribution.

</div>

## The important files

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
| `/etc/adduser.conf` | Defaults for `adduser` and `addgroup` on Debian |

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
| `1000` to `59999` | Normal users, created with `adduser` |
| `65534` | `nobody`, a user without any rights |

!!! tip "Never edit the files directly"
    Use the commands of this chapter instead of editing `/etc/passwd`, `/etc/shadow` or
    `/etc/group` with an editor. They lock the files and keep all of them consistent. If
    you really have to, use `vipw` and `vigr`.

!!! tip "Learning path"
    The commands are sorted from simple to more complex. Work through them in order,
    since later pages build on the earlier ones.
