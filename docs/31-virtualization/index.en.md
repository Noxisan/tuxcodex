---
title: "Virtualization"
icon: material/monitor-multiple
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-monitor-multiple:{ .tc-hero-icon }

# Virtualization

Running virtual machines with KVM and libvirt: installing, starting and stopping VMs,
working with disk images, cloning and snapshots.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** KVM, QEMU and libvirt, checking the host, networks and bridges, where the files live, Proxmox :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Virtual machines

<div class="grid cards" markdown>

-   :material-console:{ .lg .middle } **[virsh](virsh.md)**

    ---

    List, start, stop and inspect VMs.

-   :material-disc:{ .lg .middle } **[virt-install](virt-install.md)**

    ---

    Create a new VM and install it.

</div>

## Disks and copies

<div class="grid cards" markdown>

-   :material-harddisk:{ .lg .middle } **[qemu-img](qemu-img.md)**

    ---

    Create, inspect and convert disk images.

-   :material-content-copy:{ .lg .middle } **[virt-clone](virt-clone.md)**

    ---

    Copy a VM with new identity.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-docker:{ .lg .middle } **[docker run](../19-docker/docker-run.md)**

    ---

    Containers instead of VMs, when the host kernel is enough. Covered in the chapter Docker.

-   :material-lan:{ .lg .middle } **[ip](../11-network/ip.md)**

    ---

    Check bridges and interfaces on the host. Covered in the chapter Network.

-   :material-chart-pie:{ .lg .middle } **[df](../13-disks-storage/df.md)**

    ---

    Watch the space for disk images. Covered in the chapter Storage.

</div>
