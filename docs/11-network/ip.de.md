# ip

> Zeigt und ändert Netzwerkschnittstellen, IP-Adressen und Routen. Das zentrale Netzwerkwerkzeug unter Linux, Ersatz für die alten `ifconfig` und `route`.

![ip output](../assets/screenshots/11-network/ip.png)

## Syntax

```bash
ip [OPTION]... OBJEKT [BEFEHL]
```

Objekte lassen sich abkürzen: `ip a` ist `ip address`, `ip r` ist `ip route`.

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `ip address` | Schnittstellen mit ihren IP-Adressen |
| `ip link` | Schnittstellen mit Zustand und MAC-Adresse |
| `ip route` | Routingtabelle samt Standard-Gateway |
| `ip route get ADRESSE` | Welche Route und Absenderadresse genutzt würde |
| `ip neigh` | Nachbartabelle: MAC-Adressen im lokalen Netz (ARP) |
| `-br` | Kurze Ausgabe, eine Zeile pro Schnittstelle |
| `-s` | Statistik dazu: Bytes, Pakete, Fehler |
| `-4`, `-6` | Nur IPv4 oder nur IPv6 |
| `ip address add`, `del` | Eine Adresse hinzufügen oder entfernen (vorübergehend) |
| `ip link set SCHNITTSTELLE up`, `down` | Eine Schnittstelle ein- oder ausschalten |

## Beispiele

**Alle Schnittstellen und Adressen auf einen Blick:**

```bash
ip -br address
```

```text
lo               UNKNOWN        127.0.0.1/8 ::1/128
ens18            UP             192.0.2.10/24 2001:db8::10/64 fe80::be24:11ff:fe5e:3a7c/64
```

**Alle Details einer Schnittstelle anzeigen:**

```bash
ip address show ens18
```

```text
2: ens18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether bc:24:11:5e:3a:7c brd ff:ff:ff:ff:ff:ff
    altname enp0s18
    inet 192.0.2.10/24 brd 192.0.2.255 scope global ens18
       valid_lft forever preferred_lft forever
    inet6 2001:db8::10/64 scope global
       valid_lft forever preferred_lft forever
    inet6 fe80::be24:11ff:fe5e:3a7c/64 scope link
       valid_lft forever preferred_lft forever
```

| Teil | Bedeutung |
|------|-----------|
| `UP,LOWER_UP` | Die Schnittstelle ist an und hat eine Verbindung (Kabel oder virtuell) |
| `link/ether` | MAC-Adresse |
| `inet` | IPv4-Adresse mit Präfixlänge |
| `inet6 ... scope global` | Öffentliche IPv6-Adresse |
| `inet6 ... scope link` | Link-local-IPv6-Adresse, nur im lokalen Netz gültig |

**Routingtabelle und Standard-Gateway anzeigen:**

```bash
ip route
```

```text
default via 192.0.2.1 dev ens18
192.0.2.0/24 dev ens18 proto kernel scope link src 192.0.2.10
```

**Herausfinden, welchen Weg ein Paket nehmen würde:**

```bash
ip route get 198.51.100.23
```

```text
198.51.100.23 via 192.0.2.1 dev ens18 src 192.0.2.10 uid 1000
    cache
```

**Datenverkehr und Fehler einer Schnittstelle anzeigen:**

```bash
ip -s link show ens18
```

```text
2: ens18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether bc:24:11:5e:3a:7c brd ff:ff:ff:ff:ff:ff
    RX:   bytes  packets errors dropped  missed   mcast
    18734523110 21483922      0      12       0       0
    TX:   bytes  packets errors dropped carrier collsns
     9876543210 14522871      0       0       0       0
    altname enp0s18
```

**Vorübergehend eine zweite Adresse hinzufügen:**

```bash
sudo ip address add 192.0.2.11/24 dev ens18
ip -br address show ens18
```

```text
ens18            UP             192.0.2.10/24 192.0.2.11/24 2001:db8::10/64 fe80::be24:11ff:fe5e:3a7c/64
```

## Wann brauche ich das?

- Um die Adressen des Servers herauszufinden und welche Schnittstelle genutzt wird
- Wenn der Server das Internet nicht erreicht: Gibt es eine Standardroute?
- Um eine Schnittstelle auf Fehler und verworfene Pakete zu prüfen
- Um eine zusätzliche Adresse zu testen, bevor du sie in die Konfiguration einträgst

!!! tip "`-br` und `-c` für den schnellen Überblick"
    `ip -br -c a` zeigt eine farbige Zeile pro Schnittstelle. Mehr brauchst du meistens
    nicht.

!!! warning "Änderungen sind vorübergehend"
    Alles, was du mit `ip` änderst, ist nach einem Neustart oder Netzwerk-Neustart weg.
    Dauerhafte Änderungen gehören in die Netzwerkkonfiguration deiner Distribution, siehe
    [Grundlagen](basics.md).

!!! danger "`ip link set ... down` über SSH"
    Schaltest du die Schnittstelle aus, über die du verbunden bist, endet deine
    SSH-Sitzung sofort, und aus der Ferne schaltest du sie nicht wieder ein.

## Verwandte Befehle

[hostname](../01-orientation/hostname.md) · [ping](ping.md) · [ss](ss.md) · [nmcli](nmcli.md)
