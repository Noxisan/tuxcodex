# virsh

> Die Kommandozeile für libvirt: virtuelle Maschinen auflisten, starten, stoppen und untersuchen, ihre Konsole öffnen und Snapshots anlegen.

![virsh output](../assets/screenshots/31-virtualization/virsh.png)

## Syntax

```bash
virsh BEFEHL [VM] [OPTIONEN]
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `list --all` | Alle VMs, auch die ausgeschalteten |
| `start`, `shutdown`, `reboot` | Eine VM starten, sauber herunterfahren, neu starten |
| `destroy` | Eine VM hart ausschalten, wie Stecker ziehen |
| `autostart` | Die VM mit dem Host starten (`--disable` macht es rückgängig) |
| `dominfo`, `domifaddr` | Details einer VM oder ihre IP-Adressen |
| `console` | Serielle Konsole der VM, verlassen mit `Strg` + `]` |
| `edit` | Die XML-Definition einer VM bearbeiten |
| `snapshot-create-as`, `snapshot-list`, `snapshot-revert` | Snapshots anlegen, auflisten und zurückspielen |
| `undefine` | Eine VM aus libvirt entfernen |

Führe `virsh` als root aus (`sudo virsh`) oder als Mitglied der Gruppe `libvirt` mit `LIBVIRT_DEFAULT_URI=qemu:///system`; sonst siehst du nur deine privaten VMs.

## Beispiele

**Alle VMs auf dem Host:**

```bash
sudo virsh list --all
```

```text
 Id   Name    State
-------------------------
 1    web01   running
 2    db01    running
 -    test    shut off
```

**Eine VM starten und ab jetzt mit dem Host starten:**

```bash
sudo virsh start test
sudo virsh autostart test
```

```text
Domain 'test' started

Domain 'test' marked as autostarted
```

**Details einer VM:**

```bash
sudo virsh dominfo web01
```

```text
Id:             1
Name:           web01
UUID:           6c1f0e5a-3b2d-4f8e-9a71-2d5c8b4e7f10
OS Type:        hvm
State:          running
CPU(s):         1
CPU time:       842.3s
Max memory:     1048576 KiB
Used memory:    1048576 KiB
Persistent:     yes
Autostart:      enable
Managed save:   no
Security model: apparmor
Security DOI:   0
Security label: libvirt-6c1f0e5a-3b2d-4f8e-9a71-2d5c8b4e7f10 (enforcing)
```

**Welche IP-Adresse eine VM bekommen hat:**

```bash
sudo virsh domifaddr web01
```

```text
 Name       MAC address          Protocol     Address
-------------------------------------------------------------------------------
 vnet0      52:54:00:3a:7c:21    ipv4         192.168.122.53/24
```

Das klappt für VMs im NAT-Netz `default`. Für VMs an einer Bridge hängst du `--source agent` an; dafür braucht die VM den `qemu-guest-agent`.

**Über die serielle Konsole in die VM:**

```bash
sudo virsh console web01
```

```text
Connected to domain 'web01'
Escape character is ^] (Ctrl + ])

web01 login:
```

**Ein Snapshot vor einem Upgrade:**

```bash
sudo virsh snapshot-create-as web01 before-upgrade
sudo virsh snapshot-list web01
```

```text
Domain snapshot before-upgrade created
 Name             Creation Time               State
---------------------------------------------------------
 before-upgrade   2026-10-26 10:42:17 +0100   running
```

Geht das Upgrade schief: `sudo virsh snapshot-revert web01 before-upgrade`. Lösch den Snapshot danach mit `snapshot-delete`, damit das Abbild nicht weiter wächst.

**Eine VM sauber herunterfahren:**

```bash
sudo virsh shutdown test
```

```text
Domain 'test' is being shutdown
```

## Wann brauche ich das?

- Um zu sehen, welche VMs auf einem Host laufen, und sie zu starten oder zu stoppen
- Damit VMs nach einem Neustart des Hosts wieder anlaufen
- Um vor einem Upgrade in der VM einen Snapshot anzulegen
- Um über die Konsole in eine VM zu kommen, deren Netzwerk nicht funktioniert

!!! tip "VMs mit dem Host herunterfahren"
    Unter Debian und Ubuntu fährt der Dienst `libvirt-guests` laufende VMs herunter oder
    hält sie an, wenn der Host neu startet. Setz `ON_SHUTDOWN=shutdown` in
    `/etc/default/libvirt-guests`.

!!! warning "`shutdown` braucht den Gast"
    `virsh shutdown` schickt ein ACPI-Signal. Ignoriert der Gast es (kein `acpid`, hängendes
    System), passiert nichts. Erst dann nimmst du `virsh destroy`.

!!! danger "`undefine --remove-all-storage`"
    Das entfernt die VM und löscht ihre Plattenabbilder. Es gibt kein Zurück. Ohne die Option
    bleiben die Abbilder in `/var/lib/libvirt/images/` liegen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `libvirt-clients` | `libvirt-clients` | `libvirt-client` | `libvirt` |
| Daemon | `libvirtd` | `libvirtd` | `virtqemud` | `libvirtd` |
| Sicherheitslabel | AppArmor | AppArmor | SELinux | keins |

## Verwandte Befehle

[virt-install](virt-install.md) · [virt-clone](virt-clone.md) · [qemu-img](qemu-img.md) · [systemctl](../09-systemd/systemctl.md)
