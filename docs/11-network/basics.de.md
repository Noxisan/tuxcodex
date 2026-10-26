# Netzwerke verstehen

Ein Server braucht vier Dinge, um mit der Welt zu sprechen: eine **IP-Adresse**, ein
**Subnetz**, das sagt, welche Adressen lokal sind, ein **Gateway** für alles andere und
einen **DNS-Server**, der Namen in Adressen übersetzt. Programme sprechen dann über
**Ports** miteinander.

## IP-Adressen und Subnetze

Eine Adresse wie `192.0.2.10/24` besteht aus der Adresse und der Präfixlänge. `/24`
heißt: Die ersten 24 Bit sind das Netz, also liegen alle Adressen von `192.0.2.0` bis
`192.0.2.255` im selben Subnetz und sind direkt erreichbar.

| Schreibweise | Netzmaske | Adressen | Typischer Einsatz |
|--------------|-----------|----------|-------------------|
| `/32` | `255.255.255.255` | 1 | Ein einzelner Host, z. B. in Firewall-Regeln |
| `/24` | `255.255.255.0` | 256 | Ein typisches LAN oder Servernetz |
| `/16` | `255.255.0.0` | 65.536 | Große interne Netze |
| `/8` | `255.0.0.0` | 16,7 Millionen | `10.0.0.0/8`, sehr große Netze |

Besondere Bereiche:

| Bereich | Bedeutung |
|---------|-----------|
| `127.0.0.0/8`, `::1` | Loopback: die Maschine selbst (`localhost`) |
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | Private Netze, werden im Internet nicht geroutet |
| `169.254.0.0/16`, `fe80::/10` | Link-local: nur im lokalen Netzsegment gültig |
| `0.0.0.0`, `::` | „Alle Adressen“: Ein Dienst, der hier lauscht, ist auf jeder Schnittstelle erreichbar |

IPv6-Adressen wie `2001:db8::10/64` funktionieren genauso, nur länger. `::` ersetzt eine
Folge von Nullen.

## Gateway und Routen

Alles außerhalb des eigenen Subnetzes geht an das **Standard-Gateway**, meist den Router
des Netzes, zum Beispiel `192.0.2.1`. `ip route` zeigt die Routen; die Zeile
`default via 192.0.2.1` ist das Gateway.

## Ports

Die IP-Adresse findet die Maschine, der **Port** das Programm darauf. Ein Webserver
lauscht auf Port 80 und 443, der SSH-Server auf Port 22.

| Port | Protokoll | Dienst |
|------|-----------|--------|
| 22 | TCP | SSH |
| 25 | TCP | SMTP (Mail zwischen Servern) |
| 53 | UDP, TCP | DNS |
| 80 | TCP | HTTP |
| 123 | UDP | NTP (Zeit) |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL, MariaDB |
| 5432 | TCP | PostgreSQL |

**TCP** baut eine Verbindung auf und sorgt dafür, dass alles ankommt. **UDP** schickt
einzelne Pakete ohne Verbindung, etwa für DNS und die Zeitsynchronisation.

## Namensauflösung

Sucht ein Programm einen Namen wie `example.com`, prüft Linux die Quellen in der
Reihenfolge aus `/etc/nsswitch.conf`, meist:

1. `/etc/hosts`: feste Einträge auf dieser Maschine
2. DNS: die Server aus `/etc/resolv.conf` oder der lokale Resolver von `systemd-resolved`

`getent hosts example.com` zeigt das Ergebnis genau so, wie Programme es sehen, samt
`/etc/hosts`. `dig` und `host` fragen direkt den DNS.

## Wo die Netzwerkkonfiguration liegt

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Konfiguriert mit | ifupdown | netplan | NetworkManager | systemd-networkd (oder NetworkManager) |
| Konfigurationsdateien | `/etc/network/interfaces` | `/etc/netplan/*.yaml` | `/etc/NetworkManager/system-connections/` | `/etc/systemd/network/*.network` |
| Werkzeug | `ifup`, `ifdown` | `netplan` | `nmcli` | `networkctl` |
| DNS-Resolver | direkt `/etc/resolv.conf` | `systemd-resolved` (`127.0.0.53`) | NetworkManager schreibt `/etc/resolv.conf` | je nach Einrichtung |
| Firewall nach der Installation aktiv | keine | `ufw` installiert, inaktiv | `firewalld` aktiv | keine |

!!! tip "`ip` funktioniert überall"
    Wie die Konfiguration gespeichert wird, unterscheidet sich zwischen den
    Distributionen. Die Befehle, die den aktuellen Zustand zeigen, `ip`, `ss`, `ping` und
    `dig`, sind überall gleich.

!!! warning "Änderungen aus der Ferne"
    Eine falsche Netzwerk- oder Firewall-Änderung an einem Server, den du per SSH
    erreichst, kann dich aussperren. Sorge für eine Konsole deines Hosters, bevor du die
    Netzwerkkonfiguration änderst.
