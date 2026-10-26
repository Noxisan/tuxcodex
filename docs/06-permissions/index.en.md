---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-shield-lock-outline:{ .tc-hero-icon }

# Permissions

Who may read, change or run a file? Owners, groups, permission bits, ACLs and
attributes, and how to find out why something says "Permission denied".

</div>

## Basic permissions

<div class="grid cards" markdown>

-   :material-lock-open-variant-outline:{ .lg .middle } **[chmod](chmod.md)**

    ---

    Change permissions as a number or with letters.

</div>

## Understanding permissions

Every file has an owner, a group and three sets of permissions. `ls -l` shows them:

```text
-rwxr-x--- 1 nox www-data 1200 Oct 22 18:40 backup.sh
 └┬┘└┬┘└┬┘     │   │
  │  │  │      │   └ group
  │  │  │      └ owner
  │  │  └ others: no rights
  │  └ group: read and execute
  └ owner: read, write and execute
```

| Right | On a file | On a directory | Value |
|-------|-----------|----------------|-------|
| `r` read | Read the content | List the names of the files in it | 4 |
| `w` write | Change the content | Create, rename and delete files in it | 2 |
| `x` execute | Run it as a program or script | Enter it with `cd` and access files in it | 1 |

The values are added up per group: `rwx` = 4+2+1 = 7, `r-x` = 5, `r--` = 4.
Common combinations:

| Number | Text | Typical use |
|--------|------|-------------|
| `644` | `rw-r--r--` | Normal files, configuration files |
| `600` | `rw-------` | Private files: SSH keys, passwords |
| `640` | `rw-r-----` | Files a service group may read, e.g. TLS keys |
| `755` | `rwxr-xr-x` | Directories, programs and scripts |
| `750` | `rwxr-x---` | Directories only owner and group may enter |
| `700` | `rwx------` | Private directories like `~/.ssh` |

Special permissions:

| Bit | Value | Shown as | Meaning | Example |
|-----|-------|----------|---------|---------|
| SUID | `4000` | `rws` for the owner | A program runs with the rights of its owner | `/usr/bin/passwd` |
| SGID | `2000` | `rws` for the group | New files in a directory get its group | Shared project directories |
| Sticky bit | `1000` | `rwt` for others | Only the owner may delete their files | `/tmp` |

!!! tip "\"Permission denied\" step by step"
    1. Who am I? `id` shows your user and groups.
    2. What does the file allow? `ls -l FILE` shows owner, group and permissions.
    3. Can I reach the file at all? `namei -l /full/path/FILE` shows the permissions of
       every directory on the way. Every directory needs `x`.
    4. Are there ACLs (`+` after the permissions in `ls -l`) or attributes like `i`?

!!! tip "Learning path"
    The commands are sorted from simple to more complex. Work through them in order,
    since later pages build on the earlier ones.
