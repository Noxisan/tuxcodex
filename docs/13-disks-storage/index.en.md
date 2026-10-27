---
icon: material/harddisk
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-harddisk:{ .tc-hero-icon }

# Disks and storage

Finding out which disks there are and how full they are, partitioning and formatting new disks,
mounting them permanently, growing file systems, working with LVM and checking disk health.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Block devices, partition tables, file systems, `/etc/fstab` and LVM :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Overview

<div class="grid cards" markdown>

-   :material-view-list:{ .lg .middle } **[lsblk](lsblk.md)**

    ---

    All disks and partitions as a tree.

-   :material-barcode:{ .lg .middle } **[blkid](blkid.md)**

    ---

    UUID, label and type of file systems.

-   :material-folder-search-outline:{ .lg .middle } **[findmnt](findmnt.md)**

    ---

    Mounted file systems, check `/etc/fstab`.

-   :material-chart-pie:{ .lg .middle } **[df](df.md)**

    ---

    Used and free space per file system.

-   :material-folder-information-outline:{ .lg .middle } **[du](du.md)**

    ---

    Find out what takes up the space.

-   :material-chart-donut:{ .lg .middle } **[ncdu](ncdu.md)**

    ---

    Interactive disk usage browser.

</div>

## Partition and format

<div class="grid cards" markdown>

-   :material-table-large:{ .lg .middle } **[fdisk](fdisk.md)**

    ---

    Show and edit partition tables.

-   :material-view-split-vertical:{ .lg .middle } **[parted](parted.md)**

    ---

    Partition in one command line.

-   :material-eraser:{ .lg .middle } **[mkfs](mkfs.md)**

    ---

    Create a file system.

-   :material-swap-horizontal-bold:{ .lg .middle } **[mkswap](mkswap.md)**

    ---

    Prepare swap space.

-   :material-swap-vertical:{ .lg .middle } **[swapon](swapon.md)**

    ---

    Activate and show swap.

</div>

## Mount

<div class="grid cards" markdown>

-   :material-link-variant:{ .lg .middle } **[mount](mount.md)**

    ---

    Mount file systems.

</div>

## Check and grow

<div class="grid cards" markdown>

</div>

## LVM

<div class="grid cards" markdown>

</div>

## Health

<div class="grid cards" markdown>

</div>
