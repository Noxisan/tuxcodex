---
icon: material/monitor-multiple
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-monitor-multiple:{ .tc-hero-icon }

# Virtualisierung

Virtuelle Maschinen mit KVM und libvirt betreiben: VMs installieren, starten und stoppen,
mit Plattenabbildern arbeiten, klonen und Snapshots anlegen.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** KVM, QEMU und libvirt, den Host prüfen, Netzwerke und Bridges, wo die Dateien liegen, Proxmox :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Virtuelle Maschinen

<div class="grid cards" markdown>

-   :material-console:{ .lg .middle } **[virsh](virsh.md)**

    ---

    VMs auflisten, starten, stoppen und untersuchen.

-   :material-disc:{ .lg .middle } **[virt-install](virt-install.md)**

    ---

    Eine neue VM anlegen und installieren.

</div>

## Platten und Kopien

<div class="grid cards" markdown>

-   :material-harddisk:{ .lg .middle } **[qemu-img](qemu-img.md)**

    ---

    Plattenabbilder anlegen, untersuchen und umwandeln.

-   :material-content-copy:{ .lg .middle } **[virt-clone](virt-clone.md)**

    ---

    Eine VM mit neuer Identität kopieren.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-docker:{ .lg .middle } **[docker run](../19-docker/docker-run.md)**

    ---

    Container statt VMs, wenn der Kernel des Hosts reicht. Behandelt im Kapitel Docker.

-   :material-lan:{ .lg .middle } **[ip](../11-network/ip.md)**

    ---

    Bridges und Schnittstellen auf dem Host prüfen. Behandelt im Kapitel Netzwerk.

-   :material-chart-pie:{ .lg .middle } **[df](../13-disks-storage/df.md)**

    ---

    Den Platz für Plattenabbilder im Blick behalten. Behandelt im Kapitel Datenträger.

</div>
