---
icon: material/harddisk
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-harddisk:{ .tc-hero-icon }

# Festplatten und Speicher

Herausfinden, welche Platten es gibt und wie voll sie sind, neue Platten partitionieren und
formatieren, dauerhaft einhängen, Dateisysteme vergrößern, mit LVM arbeiten und die Plattengesundheit prüfen.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Blockgeräte, Partitionstabellen, Dateisysteme, `/etc/fstab` und LVM :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Überblick

<div class="grid cards" markdown>

-   :material-view-list:{ .lg .middle } **[lsblk](lsblk.md)**

    ---

    Alle Platten und Partitionen als Baum.

-   :material-barcode:{ .lg .middle } **[blkid](blkid.md)**

    ---

    UUID, Label und Typ von Dateisystemen.

-   :material-folder-search-outline:{ .lg .middle } **[findmnt](findmnt.md)**

    ---

    Eingehängte Dateisysteme, `/etc/fstab` prüfen.

-   :material-chart-pie:{ .lg .middle } **[df](df.md)**

    ---

    Belegter und freier Platz pro Dateisystem.

-   :material-folder-information-outline:{ .lg .middle } **[du](du.md)**

    ---

    Herausfinden, was den Platz belegt.

-   :material-chart-donut:{ .lg .middle } **[ncdu](ncdu.md)**

    ---

    Interaktiver Speicherplatz-Browser.

</div>

## Partitionieren und formatieren

<div class="grid cards" markdown>

-   :material-table-large:{ .lg .middle } **[fdisk](fdisk.md)**

    ---

    Partitionstabellen anzeigen und bearbeiten.

-   :material-view-split-vertical:{ .lg .middle } **[parted](parted.md)**

    ---

    In einer Befehlszeile partitionieren.

-   :material-eraser:{ .lg .middle } **[mkfs](mkfs.md)**

    ---

    Ein Dateisystem anlegen.

-   :material-swap-horizontal-bold:{ .lg .middle } **[mkswap](mkswap.md)**

    ---

    Swap vorbereiten.

-   :material-swap-vertical:{ .lg .middle } **[swapon](swapon.md)**

    ---

    Swap aktivieren und anzeigen.

</div>

## Einhängen

<div class="grid cards" markdown>

-   :material-link-variant:{ .lg .middle } **[mount](mount.md)**

    ---

    Dateisysteme einhängen.

-   :material-link-variant-off:{ .lg .middle } **[umount](umount.md)**

    ---

    Dateisysteme aushängen.

</div>

## Prüfen und vergrößern

<div class="grid cards" markdown>

-   :material-stethoscope:{ .lg .middle } **[fsck](fsck.md)**

    ---

    Dateisysteme prüfen und reparieren.

-   :material-arrow-expand-horizontal:{ .lg .middle } **[resize2fs](resize2fs.md)**

    ---

    ext4 vergrößern oder verkleinern.

-   :material-arrow-expand-all:{ .lg .middle } **[xfs_growfs](xfs_growfs.md)**

    ---

    XFS vergrößern.

</div>

## LVM

<div class="grid cards" markdown>

-   :material-harddisk:{ .lg .middle } **[pvs](pvs.md)**

    ---

    Physische Volumes von LVM.

-   :material-database:{ .lg .middle } **[vgs](vgs.md)**

    ---

    Volume Groups von LVM.

-   :material-layers-outline:{ .lg .middle } **[lvs](lvs.md)**

    ---

    Logische Volumes von LVM.

-   :material-layers-plus:{ .lg .middle } **[lvcreate](lvcreate.md)**

    ---

    Ein logisches Volume anlegen.

-   :material-arrow-expand-vertical:{ .lg .middle } **[lvextend](lvextend.md)**

    ---

    Ein Volume samt Dateisystem vergrößern.

</div>

## RAID

<div class="grid cards" markdown>

-   :material-harddisk-plus:{ .lg .middle } **[mdadm](mdadm.md)**

    ---

    Platten per Software-RAID spiegeln.

</div>

## Gesundheit

<div class="grid cards" markdown>

-   :material-heart-pulse:{ .lg .middle } **[smartctl](smartctl.md)**

    ---

    Die Gesundheit von Platten prüfen.

</div>
