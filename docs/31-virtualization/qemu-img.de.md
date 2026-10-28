# qemu-img

> Legt Plattenabbilder virtueller Maschinen an, untersucht, vergrößert und wandelt sie um, zum Beispiel `qcow2`, `raw` oder `vmdk`.

![qemu-img output](../assets/screenshots/31-virtualization/qemu-img.png)

## Syntax

```bash
qemu-img info | create | resize | convert | check | snapshot [OPTIONEN] DATEI
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `info DATEI` | Format, virtuelle Größe und echter Platzbedarf eines Abbilds |
| `info -U DATEI` | Ein Abbild lesen, das eine laufende VM nutzt |
| `create -f qcow2 DATEI GRÖSSE` | Ein neues, leeres Abbild anlegen |
| `create -b BASIS -F qcow2` | Ein Overlay anlegen, das nur Änderungen an `BASIS` speichert |
| `resize DATEI +10G` | Ein Abbild vergrößern (`--shrink` zum Verkleinern) |
| `convert -f EIN -O AUS -p` | Zwischen Formaten umwandeln, mit Fortschritt |
| `check DATEI` | Ein `qcow2`-Abbild auf Fehler prüfen |
| `snapshot -l`, `-c NAME` | Interne Snapshots auflisten oder anlegen |

`qcow2` belegt nur so viel Platz, wie tatsächlich geschrieben wurde, und kann Snapshots. `raw` ist eine schlichte Byte-für-Byte-Kopie einer Platte.

## Beispiele

**Das Abbild einer ausgeschalteten VM untersuchen:**

```bash
sudo qemu-img info /var/lib/libvirt/images/test.qcow2
```

```text
image: /var/lib/libvirt/images/test.qcow2
file format: qcow2
virtual size: 10 GiB (10737418240 bytes)
disk size: 1.84 GiB
cluster_size: 65536
Format specific information:
    compat: 1.1
    compression type: zlib
    lazy refcounts: false
    refcount bits: 16
    corrupt: false
    extended l2: false
Child node '/file':
    filename: /var/lib/libvirt/images/test.qcow2
    protocol type: file
    file length: 10 GiB (10739318784 bytes)
    disk size: 1.84 GiB
```

**Die VM läuft:**

```bash
sudo qemu-img info /var/lib/libvirt/images/web01.qcow2
```

```text
qemu-img: Could not open '/var/lib/libvirt/images/web01.qcow2': Failed to get shared "write" lock
Is another process using the image [/var/lib/libvirt/images/web01.qcow2]?
```

Zum Lesen ist `qemu-img info -U` in Ordnung. Für alles, was schreibt, fährst du die VM herunter.

**Ein neues Abbild anlegen:**

```bash
sudo qemu-img create -f qcow2 /var/lib/libvirt/images/data01.qcow2 20G
```

```text
Formatting '/var/lib/libvirt/images/data01.qcow2', fmt=qcow2 cluster_size=65536 extended_l2=off compression_type=zlib size=21474836480 lazy_refcounts=off refcount_bits=16
```

**Einer VM 10 GB mehr geben:**

```bash
sudo virsh shutdown test
sudo qemu-img resize /var/lib/libvirt/images/test.qcow2 +10G
```

```text
Domain 'test' is being shutdown

Image resized.
```

**Verkleinern ist abgesichert:**

```bash
sudo qemu-img resize /var/lib/libvirt/images/test.qcow2 5G
```

```text
qemu-img: Use the --shrink option to perform a shrink operation.
qemu-img: warning: Shrinking an image will delete all data beyond the shrunken image's end. Before performing such an operation, make sure there is no important data there.
```

**Eine VMware-Platte umwandeln:**

```bash
sudo qemu-img convert -p -f vmdk -O qcow2 legacy-app.vmdk /var/lib/libvirt/images/legacy-app.qcow2
```

```text
    (100.00/100%)
```

**Test-VMs aus einem Basisabbild (Overlay):**

```bash
cd /var/lib/libvirt/images
sudo qemu-img create -f qcow2 -b debian-13-base.qcow2 -F qcow2 test2.qcow2
```

```text
Formatting 'test2.qcow2', fmt=qcow2 cluster_size=65536 extended_l2=off compression_type=zlib size=21474836480 backing_file=debian-13-base.qcow2 backing_fmt=qcow2 lazy_refcounts=off refcount_bits=16
```

`test2.qcow2` ist anfangs winzig und speichert nur, was die VM ändert. Das Basisabbild darf danach nicht mehr verändert werden.

**Ein Abbild auf Fehler prüfen:**

```bash
sudo qemu-img check /var/lib/libvirt/images/test.qcow2
```

```text
No errors were found on the image.
30148/327680 = 9.20% allocated, 2.31% fragmented, 0.00% compressed clusters
Image end offset: 1977745408
```

## Wann brauche ich das?

- Um zu prüfen, wie groß ein Abbild wirklich ist und ob es eine Basisdatei hat
- Um einer VM mehr Plattenplatz zu geben
- Um VMs von VMware oder Hyper-V (`vmdk`, `vhdx`) nach KVM umzuziehen

!!! tip "Nach `resize` in der VM"
    Das Abbild ist größer, Partition und Dateisystem noch nicht. Führe in der VM
    `sudo growpart /dev/vda 1` und [`resize2fs`](../13-disks-storage/resize2fs.md) bzw.
    [`xfs_growfs`](../13-disks-storage/xfs_growfs.md) aus.

!!! danger "Nie ein Abbild ändern, während die VM läuft"
    `resize`, `convert` in dieselbe Datei, `snapshot -c` oder `check -r` bei laufender VM
    zerstören das Abbild. Fahr die VM vorher herunter; `qemu-img` verweigert sich zum
    Schutz mit einem Lock-Fehler.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `qemu-utils` | `qemu-utils` | `qemu-img` | `qemu-img` |

## Verwandte Befehle

[virsh](virsh.md) · [virt-install](virt-install.md) · [resize2fs](../13-disks-storage/resize2fs.md) · [du](../13-disks-storage/du.md)
