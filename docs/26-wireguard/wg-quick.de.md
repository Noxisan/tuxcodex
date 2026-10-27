# wg-quick

> Baut einen WireGuard-Tunnel aus einer Konfigurationsdatei auf oder ab, mit Adressen, Routen und DNS.

![wg-quick output](../assets/screenshots/26-wireguard/wg-quick.png)

## Syntax

```bash
wg-quick up | down | save | strip INTERFACE
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `up wg0` | `/etc/wireguard/wg0.conf` lesen, das Interface anlegen, Adressen und Routen setzen |
| `down wg0` | Das Interface und seine Routen wieder entfernen |
| `save wg0` | Den laufenden Zustand (etwa mit `wg set` hinzugefügte Peers) in die Datei schreiben |
| `strip wg0` | Nur den Teil der Datei ausgeben, den `wg` selbst versteht |
| `systemctl enable --now wg-quick@wg0` | Den Tunnel jetzt und bei jedem Start hochfahren |

Neben den `wg`-Einstellungen versteht der Abschnitt `[Interface]` auch `Address`, `DNS`, `MTU`, `PostUp` und `PostDown`, etwa für NAT-Regeln.

## Beispiele

**Den Tunnel hochfahren:**

```bash
sudo wg-quick up wg0
```

```text
[#] ip link add wg0 type wireguard
[#] wg setconf wg0 /dev/fd/63
[#] ip -4 address add 10.8.0.1/24 dev wg0
[#] ip link set mtu 1420 up dev wg0
```

`wg-quick` zeigt jeden Befehl, den es ausführt. Die Konfiguration steht in den [Grundlagen](basics.md).

**Bei jedem Start hochfahren:**

```bash
sudo systemctl enable --now wg-quick@wg0
ip -br address show wg0
```

```text
Created symlink '/etc/systemd/system/multi-user.target.wants/wg-quick@wg0.service' → '/usr/lib/systemd/system/wg-quick@.service'.
wg0              UNKNOWN        10.8.0.1/24
```

**Den Tunnel vom Laptop aus testen:**

```bash
ping -c 3 10.8.0.1
```

```text
PING 10.8.0.1 (10.8.0.1) 56(84) bytes of data.
64 bytes from 10.8.0.1: icmp_seq=1 ttl=64 time=18.4 ms
64 bytes from 10.8.0.1: icmp_seq=2 ttl=64 time=18.1 ms
64 bytes from 10.8.0.1: icmp_seq=3 ttl=64 time=18.3 ms

--- 10.8.0.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 18.112/18.267/18.402/0.119 ms
```

**Im Betrieb hinzugefügte Peers speichern:**

```bash
sudo wg-quick save wg0
sudo grep -c '^\[Peer\]' /etc/wireguard/wg0.conf
```

```text
2
```

**Den Tunnel herunterfahren:**

```bash
sudo wg-quick down wg0
```

```text
[#] ip link delete dev wg0
```

## Wann brauche ich das?

- Um einen Tunnel für einen Test von Hand zu starten
- Um das VPN mit systemd automatisch beim Start hochzufahren
- Um Peers zu speichern, die im laufenden System hinzugefügt wurden

!!! tip "Nach Änderungen neu starten"
    Nach dem Bearbeiten der `wg0.conf` übernimmt `sudo systemctl restart wg-quick@wg0`
    sie. Um Peers zu ändern, ohne Verbindungen zu unterbrechen, nimm
    `sudo wg syncconf wg0 <(wg-quick strip wg0)`.

!!! warning "DNS = braucht resolvconf"
    Eine Zeile `DNS =` in der Client-Konfiguration braucht `resolvconf` oder
    `systemd-resolved`. Ohne scheitert `wg-quick up` mit `resolvconf: command not found`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install wireguard-tools` | `sudo apt install wireguard-tools` | `sudo dnf install wireguard-tools` | `sudo pacman -S wireguard-tools` |

## Verwandte Befehle

[wg](wg.md) · [systemctl](../09-systemd/systemctl.md) · [ip](../11-network/ip.md) · [resolvectl](../11-network/resolvectl.md)
