---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-folder-outline:{ .tc-hero-icon }

# Navigation

Moving around the file system: where am I, what is in here, and where is the file I'm
looking for?

</div>

## Where am I, and where can I go?

<div class="grid cards" markdown>

-   :material-folder-marker-outline:{ .lg .middle } **[pwd](pwd.md)**

    ---

    Show the directory you are currently in.

-   :material-folder-arrow-right-outline:{ .lg .middle } **[cd](cd.md)**

    ---

    Change the current directory.

-   :material-layers-plus:{ .lg .middle } **[pushd](pushd.md)**

    ---

    Change directory and remember the previous one on a stack.

-   :material-layers-minus:{ .lg .middle } **[popd](popd.md)**

    ---

    Jump back to the previous directory on the stack.

</div>

## What is in here?

<div class="grid cards" markdown>

-   :material-view-list-outline:{ .lg .middle } **[ls](ls.md)**

    ---

    List directory contents with permissions, owner, size and date.

-   :material-file-tree-outline:{ .lg .middle } **[tree](tree.md)**

    ---

    Show a directory and its subdirectories as a tree.

</div>

## Where is it?

<div class="grid cards" markdown>

-   :material-file-search-outline:{ .lg .middle } **[find](find.md)**

    ---

    Search files by name, type, size, age or owner.

</div>

## The most important directories on a Debian server

| Directory | Contents |
|-----------|----------|
| `/` | Root of the file system, everything starts here |
| `/etc` | Configuration files of the system and all services |
| `/home` | Home directories of the users (`/home/nox`) |
| `/root` | Home directory of the `root` user |
| `/var/log` | Log files |
| `/var/lib` | Data of programs and services (databases, Docker, package lists) |
| `/var/www` | Web content (default for Apache and nginx on Debian) |
| `/srv` | Data that the server provides (websites, FTP, Git repositories) |
| `/opt` | Additional software that is not installed via `apt` |
| `/usr/local` | Software and scripts you installed yourself |
| `/usr/bin` | Programs (`/bin` is a link to it) |
| `/tmp` | Temporary files; since Debian 13 kept in RAM and emptied on every reboot |
| `/boot` | Kernel and boot loader |
| `/proc`, `/sys` | Virtual file systems with live information from the kernel |
| `/dev` | Devices (disks, terminals) |
| `/mnt`, `/media` | Mount points for additional drives |

!!! tip "Learning path"
    The commands are sorted from simple to more complex. Work through them in order,
    since later pages build on the earlier ones.
