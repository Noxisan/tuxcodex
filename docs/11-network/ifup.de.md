# ifup

> Fährt unter Debian Netzwerkschnittstellen nach `/etc/network/interfaces` hoch und herunter. `ifdown` ist das Gegenstück.

![ifup output](../assets/screenshots/11-network/ifup.png)

## Syntax

```bash
ifup [OPTION]... SCHNITTSTELLE
ifdown [OPTION]... SCHNITTSTELLE
```

Beide gehören zum Paket `ifupdown`, das Debian auf Servern nutzt. Ohne `-v` geben sie nichts aus, wenn alles klappt.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `ifup GERÄT` | Eine Schnittstelle wie konfiguriert hochfahren |
| `ifdown GERÄT` | Eine Schnittstelle herunterfahren |
| `-a` | Alle mit `auto` markierten Schnittstellen |
| `-v` | Jeden ausgeführten Befehl zeigen |
| `--no-act` | Nur zeigen, was passieren würde |
| `ifquery GERÄT` | Die Konfiguration einer Schnittstelle zeigen |
| `ifquery --state` | Zeigen, welche Schnittstellen ifupdown für aktiv hält |

## Beispiele

**Die Konfiguration des Beispielservers:**

```bash
cat /etc/network/interfaces
```

```text
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens18
iface ens18 inet static
        address 192.0.2.10/24
        gateway 192.0.2.1

iface ens18 inet6 static
        address 2001:db8::10/64
        gateway 2001:db8::1
```

`allow-hotplug` fährt die Schnittstelle hoch, sobald sie auftaucht, `auto` beim Booten.
Die Einstellungen unter `iface` sind mit einem Tab eingerückt.

**Einen Block für eine zweite Schnittstelle eintragen:**

```bash
tail -n 3 /etc/network/interfaces
```

```text
auto ens19
iface ens19 inet static
        address 198.51.100.10/24
```

**Die neue Schnittstelle hochfahren:**

```bash
sudo ifup -v ens19
```

```text
ifup: configuring interface ens19=ens19 (inet)
run-parts --exit-on-error --verbose /etc/network/if-pre-up.d
ip addr add 198.51.100.10/255.255.255.0 broadcast 198.51.100.255          dev ens19 label ens19
ip link set dev ens19   up
run-parts --exit-on-error --verbose /etc/network/if-up.d
```

`-v` zeigt die `ip`-Befehle, die `ifup` ausführt. Ohne die Option wird nichts
ausgegeben.

**Anzeigen, was ifupdown aus der Konfiguration liest:**

```bash
ifquery ens18
```

```text
address: 192.0.2.10
gateway: 192.0.2.1
broadcast: 192.0.2.255
netmask: 255.255.255.0
```

**Welche Schnittstellen laut ifupdown aktiv sind:**

```bash
ifquery --state
```

```text
lo=lo
ens18=ens18
ens19=ens19
```

**Die Adresse ist schon gesetzt:**

```bash
sudo ifup ens19
```

```text
Error: ipv4: Address already assigned.
ifup: failed to bring up ens19
```

Jemand hat die Adresse schon von Hand mit `ip` gesetzt. Entferne sie mit
`sudo ip address del 198.51.100.10/24 dev ens19` und führe `ifup` erneut aus.

## Wann brauche ich das?

- Unter Debian, um eine geänderte oder neue Schnittstelle ohne Neustart zu aktivieren
- Um mit `ifquery` zu prüfen, was die Konfiguration wirklich enthält
- Nach einer Netzwerkänderung, zusammen mit `ip`, um das Ergebnis zu prüfen

!!! tip "Das Netzwerk neu starten, ohne SSH zu verlieren"
    `sudo systemctl restart networking` fährt alle Schnittstellen herunter und wieder
    hoch. Über SSH führst du das in einem Befehl oder mit `nohup` aus, damit die Sitzung
    nicht mittendrin endet.

!!! danger "`ifdown` auf der SSH-Schnittstelle"
    `sudo ifdown ens18` beendet deine SSH-Sitzung sofort, und die Schnittstelle bleibt
    unten. Ändere die Hauptschnittstelle nur mit Zugriff auf die Konsole des Hosters.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Verfügbar | ja, Standard auf Servern | Paket `ifupdown`, standardmäßig nicht genutzt | nein, `nmcli` nutzen | nein, `networkctl` nutzen |

## Verwandte Befehle

[ip](ip.md) · [nmcli](nmcli.md) · [netplan](netplan.md)
