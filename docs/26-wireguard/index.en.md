---
icon: material/vpn
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-vpn:{ .tc-hero-icon }

# VPN with WireGuard

Connecting servers and admin machines through an encrypted tunnel: generating keys,
setting up a server and clients, and reaching admin services only through the VPN.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** How WireGuard works, what to install, a complete server and client setup and the firewall :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Commands

<div class="grid cards" markdown>

-   :material-key-chain-variant:{ .lg .middle } **[wg](wg.md)**

    ---

    Keys, tunnel state and peers.

-   :material-tunnel-outline:{ .lg .middle } **[wg-quick](wg-quick.md)**

    ---

    Bring tunnels up and down, start at boot.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-lan:{ .lg .middle } **[ip](../11-network/ip.md)**

    ---

    `ip address show wg0` and `ip route` show the tunnel interface and its routes. Covered in the chapter Network.

-   :material-wall-fire:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Open UDP port 51820 and allow SSH only through `wg0`. Covered in the chapter Network.

-   :material-console-network:{ .lg .middle } **[ssh](../12-ssh/ssh.md)**

    ---

    Connect to `10.8.0.1` through the tunnel once SSH is closed to the internet. Covered in the chapter SSH.

-   :material-dns-outline:{ .lg .middle } **[resolvectl](../11-network/resolvectl.md)**

    ---

    Check which DNS server applies while the tunnel is up. Covered in the chapter Network.

</div>
