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

[:material-school-outline:{ .tc-basics-icon } **Basics:** Owner, group, rwx and octal notation explained :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Basic permissions

<div class="grid cards" markdown>

-   :material-lock-open-variant-outline:{ .lg .middle } **[chmod](chmod.md)**

    ---

    Change permissions as a number or with letters.

-   :material-account-key-outline:{ .lg .middle } **[chown](chown.md)**

    ---

    Change owner and group of files.

-   :material-account-group-outline:{ .lg .middle } **[chgrp](chgrp.md)**

    ---

    Change only the group of files.

-   :material-shield-account-outline:{ .lg .middle } **[umask](umask.md)**

    ---

    Set the default permissions for new files.

</div>

## Troubleshooting

<div class="grid cards" markdown>

-   :material-folder-search-outline:{ .lg .middle } **[namei](namei.md)**

    ---

    Show the permissions of every directory along a path.

</div>

## Access control lists (ACLs)

<div class="grid cards" markdown>

-   :material-playlist-check:{ .lg .middle } **[getfacl](getfacl.md)**

    ---

    Show additional permissions for single users and groups.

-   :material-playlist-edit:{ .lg .middle } **[setfacl](setfacl.md)**

    ---

    Give single users or groups additional permissions.

</div>

## File attributes

<div class="grid cards" markdown>

-   :material-tag-search-outline:{ .lg .middle } **[lsattr](lsattr.md)**

    ---

    Show special attributes like immutable or append only.

-   :material-tag-edit-outline:{ .lg .middle } **[chattr](chattr.md)**

    ---

    Protect files with attributes like immutable.

</div>
