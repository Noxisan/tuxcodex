# netplan

> Konfiguriert unter Ubuntu das Netzwerk aus YAML-Dateien in `/etc/netplan/`. Netplan erzeugt daraus die Konfiguration für systemd-networkd oder den NetworkManager.

![netplan output](../assets/screenshots/11-network/netplan.png)

## Syntax

```bash
netplan BEFEHL [OPTION]...
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `try` | Die Konfiguration anwenden und nach 120 Sekunden zurückrollen, wenn du nicht bestätigst |
| `apply` | Die Konfiguration sofort anwenden |
| `generate` | Nur prüfen und erzeugen, nicht anwenden |
| `get [SCHLÜSSEL]` | Die zusammengeführte Konfiguration zeigen oder einen Schlüssel wie `ethernets.ens18.addresses` |
| `status` | Aktueller Zustand aller Schnittstellen: Adressen, Routen, DNS |

## Beispiele

**Den aktuellen Zustand des Netzwerks anzeigen:**

```bash
netplan status
```

```text
     Online state: online
    DNS Addresses: 127.0.0.53 (stub)
       DNS Search: example.com

●  2: ens18 ethernet UP (networkd: ens18)
      MAC Address: bc:24:11:5e:3a:7c (Proxmox Server Solutions GmbH)
        Addresses: 192.0.2.10/24
                   2001:db8::10/64
                   fe80::be24:11ff:fe5e:3a7c/64 (link)
    DNS Addresses: 192.0.2.53
                   198.51.100.53
       DNS Search: example.com
           Routes: default via 192.0.2.1 (static)
                   192.0.2.0/24 from 192.0.2.10 (link)
                   2001:db8::/64 metric 256
                   fe80::/64 metric 256

1 inactive interfaces hidden. Use "--all" to show all.
```

**Eine feste Konfiguration:**

```bash
sudo cat /etc/netplan/50-cloud-init.yaml
```

```text
network:
  version: 2
  ethernets:
    ens18:
      addresses:
        - 192.0.2.10/24
        - "2001:db8::10/64"
      routes:
        - to: default
          via: 192.0.2.1
      nameservers:
        addresses: [192.0.2.53, 198.51.100.53]
        search: [example.com]
```

In YAML zählt die Einrückung: immer Leerzeichen, nie Tabs. Mach die Datei nur für root
lesbar: `sudo chmod 600 /etc/netplan/50-cloud-init.yaml`.

**Eine Änderung sicher testen:**

```bash
sudo netplan try
```

```text
Do you want to keep these settings?


Press ENTER before the timeout to accept the new configuration


Changes will revert in 120 seconds
Configuration accepted.
```

Verlierst du die Verbindung, kannst du ++enter++ nicht drücken, und netplan stellt nach
120 Sekunden die alte Konfiguration wieder her.

**Ein Tippfehler in der YAML-Datei:**

```bash
sudo netplan generate
```

```text
/etc/netplan/50-cloud-init.yaml:12:9: Invalid YAML: did not find expected key:
        nameservers:
        ^
```

Zeile 12, Spalte 9: `nameservers` ist um ein Leerzeichen zu weit eingerückt.

**Einen einzelnen Wert lesen:**

```bash
sudo netplan get ethernets.ens18.addresses
```

```text
- "192.0.2.10/24"
- "2001:db8::10/64"
```

## Wann brauche ich das?

- Auf Ubuntu-Servern, um eine feste IP-Adresse, das Gateway oder DNS-Server zu setzen
- Um eine zweite Adresse, ein VLAN oder eine Bridge hinzuzufügen
- Nach dem Klonen einer VM, wenn sich Schnittstellenname oder Adresse ändern müssen

!!! tip "Über SSH immer `try` statt `apply`"
    `netplan try` rollt automatisch zurück, wenn dich die neue Konfiguration aussperrt. Mit
    `apply` bräuchtest du die Konsole des Hosters.

!!! warning "Cloud-Images überschreiben die Datei"
    Auf Cloud-Servern legt cloud-init oft `50-cloud-init.yaml` an und kann sie beim
    nächsten Booten überschreiben. Trag eigene Einstellungen in eine eigene Datei wie
    `60-static.yaml` ein oder schalte die Netzwerkkonfiguration von cloud-init ab.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Netzwerkkonfiguration | ifupdown, netplan nur in Cloud-Images | netplan | NetworkManager | systemd-networkd oder NetworkManager |

## Verwandte Befehle

[ip](ip.md) · [resolvectl](resolvectl.md) · [nmcli](nmcli.md) · [ifup](ifup.md)
