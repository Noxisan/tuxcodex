# Understanding networks

A server needs four things to talk to the world: an **IP address**, a **subnet** that
says which addresses are local, a **gateway** for everything else, and a **DNS server**
that turns names into addresses. Programs then talk to each other through **ports**.

## IP addresses and subnets

An address like `192.0.2.10/24` consists of the address and the prefix length. `/24`
means: the first 24 bits are the network, so all addresses from `192.0.2.0` to
`192.0.2.255` are in the same subnet and can be reached directly.

| Notation | Netmask | Addresses | Typical use |
|----------|---------|-----------|-------------|
| `/32` | `255.255.255.255` | 1 | A single host, e.g. in firewall rules |
| `/24` | `255.255.255.0` | 256 | A typical LAN or server network |
| `/16` | `255.255.0.0` | 65,536 | Large internal networks |
| `/8` | `255.0.0.0` | 16.7 million | `10.0.0.0/8`, very large networks |

Special ranges:

| Range | Meaning |
|-------|---------|
| `127.0.0.0/8`, `::1` | Loopback: the machine itself (`localhost`) |
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | Private networks, not routed on the internet |
| `169.254.0.0/16`, `fe80::/10` | Link-local: only valid on the local network segment |
| `0.0.0.0`, `::` | "All addresses": a service listening here is reachable on every interface |

IPv6 addresses like `2001:db8::10/64` work the same way, just longer. `::` replaces a run
of zeros.

## Gateway and routes

Everything outside the own subnet goes to the **default gateway**, usually the router of
the network, for example `192.0.2.1`. `ip route` shows the routes; the line
`default via 192.0.2.1` is the gateway.

## Ports

An IP address finds the machine, the **port** finds the program on it. A web server
listens on port 80 and 443, the SSH server on port 22.

| Port | Protocol | Service |
|------|----------|---------|
| 22 | TCP | SSH |
| 25 | TCP | SMTP (mail between servers) |
| 53 | UDP, TCP | DNS |
| 80 | TCP | HTTP |
| 123 | UDP | NTP (time) |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL, MariaDB |
| 5432 | TCP | PostgreSQL |

**TCP** establishes a connection and makes sure everything arrives. **UDP** sends single
packets without a connection, for example for DNS and time synchronisation.

## Name resolution

When a program looks up a name like `example.com`, Linux checks the sources in the order
given in `/etc/nsswitch.conf`, usually:

1. `/etc/hosts`: fixed entries on this machine
2. DNS: the servers in `/etc/resolv.conf`, or the local resolver of `systemd-resolved`

`getent hosts example.com` shows the result exactly as programs see it, including
`/etc/hosts`. `dig` and `host` ask DNS directly.

## Where the network configuration is

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Configured with | ifupdown | netplan | NetworkManager | systemd-networkd (or NetworkManager) |
| Configuration files | `/etc/network/interfaces` | `/etc/netplan/*.yaml` | `/etc/NetworkManager/system-connections/` | `/etc/systemd/network/*.network` |
| Tool | `ifup`, `ifdown` | `netplan` | `nmcli` | `networkctl` |
| DNS resolver | `/etc/resolv.conf` directly | `systemd-resolved` (`127.0.0.53`) | NetworkManager writes `/etc/resolv.conf` | depends on the setup |
| Firewall active after installation | none | `ufw` installed, inactive | `firewalld` active | none |

!!! tip "`ip` works everywhere"
    How the configuration is stored differs between distributions. The commands to
    look at the current state, `ip`, `ss`, `ping` and `dig`, are the same everywhere.

!!! warning "Remote changes"
    A wrong network or firewall change on a server you reach via SSH can lock you out.
    Make sure you have a console from your hosting provider before you change the
    network configuration.
