---
title: "VPN mit WireGuard"
icon: material/vpn
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-vpn:{ .tc-hero-icon }

# VPN mit WireGuard

Server und Admin-Rechner über einen verschlüsselten Tunnel verbinden: Schlüssel erzeugen,
Server und Clients einrichten und Admin-Dienste nur noch über das VPN erreichbar machen.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Wie WireGuard funktioniert, was du installieren musst, eine vollständige Einrichtung von Server und Client und die Firewall :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Befehle

<div class="grid cards" markdown>

-   :material-key-chain-variant:{ .lg .middle } **[wg](wg.md)**

    ---

    Schlüssel, Tunnelzustand und Peers.

-   :material-tunnel-outline:{ .lg .middle } **[wg-quick](wg-quick.md)**

    ---

    Tunnel auf- und abbauen, beim Start hochfahren.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-lan:{ .lg .middle } **[ip](../11-network/ip.md)**

    ---

    `ip address show wg0` und `ip route` zeigen das Tunnel-Interface und seine Routen. Behandelt im Kapitel Netzwerk.

-   :material-wall-fire:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    UDP-Port 51820 öffnen und SSH nur über `wg0` erlauben. Behandelt im Kapitel Netzwerk.

-   :material-console-network:{ .lg .middle } **[ssh](../12-ssh/ssh.md)**

    ---

    Über den Tunnel zu `10.8.0.1` verbinden, sobald SSH zum Internet geschlossen ist. Behandelt im Kapitel SSH.

-   :material-dns-outline:{ .lg .middle } **[resolvectl](../11-network/resolvectl.md)**

    ---

    Prüfen, welcher DNS-Server gilt, während der Tunnel steht. Behandelt im Kapitel Netzwerk.

</div>
