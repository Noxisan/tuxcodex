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

-   :material-link-variant-off:{ .lg .middle } **[umount](umount.md)**

    ---

    Unmount file systems.

</div>

## Check and grow

<div class="grid cards" markdown>

-   :material-stethoscope:{ .lg .middle } **[fsck](fsck.md)**

    ---

    Check and repair file systems.

-   :material-arrow-expand-horizontal:{ .lg .middle } **[resize2fs](resize2fs.md)**

    ---

    Grow or shrink ext4.

-   :material-arrow-expand-all:{ .lg .middle } **[xfs_growfs](xfs_growfs.md)**

    ---

    Grow XFS.

</div>

## LVM

<div class="grid cards" markdown>

-   :material-harddisk:{ .lg .middle } **[pvs](pvs.md)**

    ---

    Physical volumes of LVM.

-   :material-database:{ .lg .middle } **[vgs](vgs.md)**

    ---

    Volume groups of LVM.

-   :material-layers-outline:{ .lg .middle } **[lvs](lvs.md)**

    ---

    Logical volumes of LVM.

-   :material-layers-plus:{ .lg .middle } **[lvcreate](lvcreate.md)**

    ---

    Create a logical volume.

-   :material-arrow-expand-vertical:{ .lg .middle } **[lvextend](lvextend.md)**

    ---

    Grow a volume and its file system.

</div>

## Health

<div class="grid cards" markdown>

</div>
