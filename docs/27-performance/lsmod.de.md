# lsmod

> Listet die gerade geladenen Kernelmodule mit ihrer Größe und den Modulen auf, die sie nutzen.

![lsmod output](../assets/screenshots/27-performance/lsmod.png)

## Syntax

```bash
lsmod
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| (keine) | Alle geladenen Module: Name, Größe, Zahl der Nutzer und die Module, die sie nutzen |

`modinfo NAME` zeigt Details zu einem Modul: Beschreibung, Datei, Parameter und Version.

## Beispiele

**Prüfen, ob das WireGuard-Modul geladen ist:**

```bash
lsmod | grep -E '^Module|wireguard'
```

```text
Module                  Size  Used by
wireguard             118784  0
libchacha20poly1305    16384  1 wireguard
curve25519_x86_64      36864  1 wireguard
libcurve25519_generic    45056  2 curve25519_x86_64,wireguard
ip6_udp_tunnel         16384  1 wireguard
udp_tunnel             32768  1 wireguard
```

**Details zu einem Modul:**

```bash
modinfo wireguard | head -6
```

```text
filename:       /lib/modules/6.12.48+deb13-amd64/kernel/drivers/net/wireguard/wireguard.ko.xz
intree:         Y
alias:          net-pf-16-proto-16-family-wireguard
alias:          rtnl-link-wireguard
version:        1.0.0
author:         Jason A. Donenfeld <Jason@zx2c4.com>
```

**Der Treiber der Netzwerkkarte:**

```bash
lspci -k | grep -A2 Ethernet
```

```text
00:12.0 Ethernet controller: Red Hat, Inc. Virtio 1.0 network device (rev 01)
        Subsystem: Red Hat, Inc. Device 1100
        Kernel driver in use: virtio_net
```

## Wann brauche ich das?

- Um zu prüfen, ob ein Treiber geladen ist, etwa für eine Netzwerkkarte oder WireGuard
- Um herauszufinden, welches Modul zu einer Hardware gehört (zusammen mit `lspci -k`)
- Bevor du ein Modul entlädst, um zu sehen, was es noch nutzt

!!! tip "Welchen Treiber nutzt ein Gerät?"
    `lspci -k` zeigt für jedes PCI-Gerät die Zeile `Kernel driver in use`, damit weißt du,
    welches Modul du in `lsmod` suchst.

## Verwandte Befehle

[modprobe](modprobe.md) · [dmesg](../15-logs/dmesg.md) · [wg](../26-wireguard/wg.md)
