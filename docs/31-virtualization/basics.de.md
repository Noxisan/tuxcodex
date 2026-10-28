# Virtualisierung verstehen

Eine virtuelle Maschine (VM) ist ein vollständiger Rechner in Software: mit eigenem Kernel,
eigenen Platten und eigener Netzwerkkarte. Unter Linux arbeiten dafür drei Teile zusammen:

| Teil | Aufgabe |
|------|---------|
| **KVM** | Kernelmodul, das die Virtualisierungsfunktionen der CPU nutzt (Intel VT-x, AMD-V) |
| **QEMU** | Bildet die Hardware der VM nach: Platten, Netzwerkkarte, Grafik |
| **libvirt** | Verwaltet VMs, Netzwerke und Speicher; [`virsh`](virsh.md), `virt-install` und virt-manager sprechen mit ihm |

Container wie [Docker](../19-docker/index.md) teilen sich den Kernel des Hosts. Eine VM hat
einen eigenen: Darin läuft auch eine andere Distribution, ein anderer Kernel oder Windows.

## Den Host prüfen

```text
$ grep -cE 'vmx|svm' /proc/cpuinfo        # > 0: Die CPU kann virtualisieren
2
$ ls /dev/kvm                              # vorhanden: KVM ist nutzbar
/dev/kvm
$ sudo virt-host-validate qemu | head -3
  QEMU: Checking for hardware virtualization                                 : PASS
  QEMU: Checking if device '/dev/kvm' exists                                 : PASS
  QEMU: Checking if device '/dev/kvm' is accessible                          : PASS
```

Ist die Zahl `0`, ist die Virtualisierung im BIOS bzw. UEFI ausgeschaltet, oder der Host ist
selbst eine VM ohne verschachtelte Virtualisierung (Nested Virtualization).

## Pakete und Dienste

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| QEMU/KVM | `qemu-system-x86` | `qemu-kvm` | `qemu-kvm` | `qemu-base` |
| libvirt | `libvirt-daemon-system` | `libvirt-daemon-system` | `libvirt` | `libvirt`, `dnsmasq` |
| Werkzeuge | `virtinst`, `qemu-utils` | `virtinst`, `qemu-utils` | `virt-install` | `virt-install` |
| Dienst | `libvirtd` | `libvirtd` | `virtqemud` (ein Daemon pro Treiber) | `libvirtd` |
| VMs ohne `sudo` | Gruppe `libvirt` | Gruppe `libvirt` | Gruppe `libvirt` | Gruppe `libvirt` |

!!! tip "`qemu:///system` und `qemu:///session`"
    Als normaler Benutzer verbindet sich `virsh` mit deiner privaten Sitzung und sieht die
    VMs des Systems nicht. Nimm `sudo virsh` oder tritt der Gruppe `libvirt` bei und setz
    `export LIBVIRT_DEFAULT_URI=qemu:///system`.

## Wo die Dateien liegen

| Was | Pfad |
|-----|------|
| VM-Definitionen (XML) | `/etc/libvirt/qemu/*.xml`, nur mit `virsh edit` ändern |
| Plattenabbilder | `/var/lib/libvirt/images/` |
| Logs pro VM | `/var/log/libvirt/qemu/NAME.log` |

## Netzwerke und Bridges

| Art | So funktioniert es | Gut für |
|-----|--------------------|---------|
| NAT (`default`) | VMs bekommen Adressen aus `192.168.122.0/24` und gehen über den Host nach draußen | Tests, VMs, die nur hinaus müssen |
| Bridge (`br0`) | Die VMs hängen im selben Netz wie der Host und bekommen Adressen von dort | Server, die aus dem Netz erreichbar sein müssen |

Eine Bridge unter Debian mit `/etc/network/interfaces` (die physische Karte `ens18` wird Teil
von `br0`, Paket `bridge-utils`):

```text
auto br0
iface br0 inet static
    address 192.0.2.10/24
    gateway 192.0.2.1
    bridge_ports ens18
    bridge_stp off
```

Unter Ubuntu kommt dasselbe in eine [Netplan](../11-network/netplan.md)-Datei unter
`bridges:`, unter RHEL legst du sie mit [`nmcli`](../11-network/nmcli.md) an. VMs nutzen die
Bridge mit `virt-install --network bridge=br0`.

!!! warning "Eine Bridge über die Konsole einrichten"
    Die IP des Hosts wandert von der Netzwerkkarte auf die Bridge. Ein Fehler trennt die
    SSH-Verbindung. Halte eine Konsole bereit (IPMI, iDRAC, den Hypervisor), bevor du
    etwas änderst.

## Proxmox VE

Proxmox VE ist eine auf Debian basierende Distribution für Virtualisierungsserver mit
Weboberfläche. Darunter arbeiten dieselben KVM und QEMU, aber nicht libvirt: Proxmox hat
eigene Werkzeuge wie `qm` für VMs und `pct` für LXC-Container. Die Plattenabbilder sind
dieselben, deshalb funktioniert [`qemu-img`](qemu-img.md) auch dort.

!!! tip "Snapshots sind kein Backup"
    Ein Snapshot liegt im selben Abbild auf derselben Platte. Fällt die Platte aus, ist auch
    der Snapshot weg. Sichere VMs als Dateien, siehe das Kapitel [Backup](../28-backup/index.md).
