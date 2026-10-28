# Understanding virtualization

A virtual machine (VM) is a complete computer in software: with its own kernel, its own
disks and its own network card. On Linux, three parts work together:

| Part | Job |
|------|-----|
| **KVM** | Kernel module that uses the virtualization features of the CPU (Intel VT-x, AMD-V) |
| **QEMU** | Emulates the hardware of the VM: disks, network card, graphics |
| **libvirt** | Manages VMs, networks and storage; `virsh`, `virt-install` and virt-manager talk to it |

Containers like [Docker](../19-docker/index.md) share the kernel of the host. A VM has its
own: you can run another distribution, another kernel or Windows.

## Checking the host

```text
$ grep -cE 'vmx|svm' /proc/cpuinfo        # > 0: the CPU supports virtualization
2
$ ls /dev/kvm                              # exists: KVM is usable
/dev/kvm
$ sudo virt-host-validate qemu | head -3
  QEMU: Checking for hardware virtualization                                 : PASS
  QEMU: Checking if device '/dev/kvm' exists                                 : PASS
  QEMU: Checking if device '/dev/kvm' is accessible                          : PASS
```

If the count is `0`, virtualization is switched off in the BIOS or UEFI, or the host is
itself a VM without nested virtualization.

## Packages and services

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| QEMU/KVM | `qemu-system-x86` | `qemu-kvm` | `qemu-kvm` | `qemu-base` |
| libvirt | `libvirt-daemon-system` | `libvirt-daemon-system` | `libvirt` | `libvirt`, `dnsmasq` |
| Tools | `virtinst`, `qemu-utils` | `virtinst`, `qemu-utils` | `virt-install` | `virt-install` |
| Service | `libvirtd` | `libvirtd` | `virtqemud` (one daemon per driver) | `libvirtd` |
| VMs without `sudo` | group `libvirt` | group `libvirt` | group `libvirt` | group `libvirt` |

!!! tip "`qemu:///system` and `qemu:///session`"
    As a normal user, `virsh` connects to your private session and doesn't see the VMs of
    the system. Use `sudo virsh`, or join the group `libvirt` and set
    `export LIBVIRT_DEFAULT_URI=qemu:///system`.

## Where the files live

| What | Path |
|------|------|
| VM definitions (XML) | `/etc/libvirt/qemu/*.xml`, change them only with `virsh edit` |
| Disk images | `/var/lib/libvirt/images/` |
| Logs per VM | `/var/log/libvirt/qemu/NAME.log` |

## Networks and bridges

| Type | How it works | Good for |
|------|--------------|----------|
| NAT (`default`) | VMs get addresses from `192.168.122.0/24` and reach the outside through the host | Tests, VMs that only need to go out |
| Bridge (`br0`) | The VMs sit in the same network as the host and get addresses from there | Servers that must be reachable from the network |

A bridge on Debian with `/etc/network/interfaces` (the physical card `ens18` becomes part of
`br0`, package `bridge-utils`):

```text
auto br0
iface br0 inet static
    address 192.0.2.10/24
    gateway 192.0.2.1
    bridge_ports ens18
    bridge_stp off
```

On Ubuntu the same goes into a [Netplan](../11-network/netplan.md) file under `bridges:`, on
RHEL you create it with [`nmcli`](../11-network/nmcli.md). VMs use the bridge with
`virt-install --network bridge=br0`.

!!! warning "Set up a bridge from the console"
    The host's IP moves from the network card to the bridge. A mistake cuts the SSH
    connection. Have a console ready (IPMI, iDRAC, the hypervisor) before you change it.

## Proxmox VE

Proxmox VE is a Debian-based distribution for virtualization servers with a web interface.
Underneath it uses the same KVM and QEMU, but not libvirt: it has its own tools such as
`qm` for VMs and `pct` for LXC containers. The disk images are the same, so
`qemu-img` works there as well.

!!! tip "Snapshots are no backup"
    A snapshot lives in the same image on the same disk. If the disk fails, the snapshot is
    gone too. Back up VMs as files, see the chapter [Backup](../28-backup/index.md).
