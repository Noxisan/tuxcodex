# Understanding WireGuard

WireGuard is a VPN built into the Linux kernel. It's small, fast and has very little to
configure: every machine has a key pair, and every connection partner (**peer**) is
known by its public key. There are no certificates, no user names and no handshake
options to get wrong.

## How it fits together

```text
   laptop                                  tuxdex-srv
   10.8.0.2                                10.8.0.1
   wg0 ◄──── encrypted UDP, port 51820 ────► wg0
              over the internet             vpn.example.com (198.51.100.7)
```

| Term | Meaning |
|------|---------|
| **Interface** | The VPN network card, usually `wg0`, with an address in the tunnel network such as `10.8.0.1/24` |
| **Private key** | Secret key of this machine, stays on it |
| **Public key** | Derived from the private key, is entered at the other peers |
| **Peer** | A connection partner, identified by its public key |
| **AllowedIPs** | Which tunnel addresses belong to a peer; on the client also which networks go through the tunnel |
| **Endpoint** | Public address and port of a peer, at least one side needs it |

## What you need to install

WireGuard itself is part of the Linux kernel since version 5.6. You only need the tools:

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Install | `sudo apt install wireguard-tools` | `sudo apt install wireguard-tools` | `sudo dnf install wireguard-tools` | `sudo pacman -S wireguard-tools` |
| Kernel module | included | included | included | included |
| Firewall for the port | `ufw allow 51820/udp` | `ufw allow 51820/udp` | `firewall-cmd --add-port=51820/udp --permanent` | as configured |

Clients exist for Windows, macOS, Android and iOS too; they read the same configuration
format.

## Server: /etc/wireguard/wg0.conf

```text
[Interface]
Address = 10.8.0.1/24
ListenPort = 51820
PrivateKey = <private key of tuxdex-srv>

[Peer]
# laptop of nox
PublicKey = HO2gBkM55TRjnkSr2Nwia5/L/gvPMnYjEGn/tR1B3mo=
AllowedIPs = 10.8.0.2/32
```

## Client: /etc/wireguard/wg0.conf on the laptop

```text
[Interface]
Address = 10.8.0.2/24
PrivateKey = <private key of the laptop>

[Peer]
# tuxdex-srv
PublicKey = uYnlIayVbIBV2lDo84nK2O2R61sblMRycaxu8Y1W1kk=
Endpoint = vpn.example.com:51820
AllowedIPs = 10.8.0.0/24
PersistentKeepalive = 25
```

`AllowedIPs = 10.8.0.0/24` sends only the tunnel network through the VPN. With
`0.0.0.0/0, ::/0`, all traffic of the laptop would go through the server; then the server
needs IP forwarding and NAT.

## Setting it up step by step

| Step | Command |
|------|---------|
| 1. Keys on every machine | `wg genkey \| tee private.key \| wg pubkey > public.key`, see [`wg`](wg.md) |
| 2. Write the configurations | as above, with the public key of the other side |
| 3. Open the port on the server | `sudo ufw allow 51820/udp` |
| 4. Start and enable | `sudo systemctl enable --now wg-quick@wg0`, see [`wg-quick`](wg-quick.md) |
| 5. Check | `sudo wg show`: a `latest handshake` means the tunnel works |

## Admin services only through the VPN

The most useful use of a VPN on servers: SSH, monitoring and admin panels only listen on
the tunnel address or are only allowed from the tunnel network:

```text
$ sudo ufw allow in on wg0 to any port 22 proto tcp
$ sudo ufw delete allow 22/tcp
```

Then SSH can no longer be reached from the internet at all, only through the VPN.

!!! tip "Keep a way back in"
    Before closing SSH to the internet, test the VPN access in a second session and keep
    the console of your hosting provider at hand. A typo in the firewall otherwise locks
    you out.

!!! danger "Private keys stay on their machine"
    Never copy a private key to another machine, a ticket or a repository. Every peer
    creates its own key pair; only public keys are exchanged. The configuration files need
    mode `600`.
