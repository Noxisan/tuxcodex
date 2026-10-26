---
icon: material/lan
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-lan:{ .tc-hero-icon }

# Network

Finding out addresses and routes, testing connections and name resolution, downloading files,
configuring interfaces and the firewall, and looking at the traffic itself.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** IP addresses, subnets, ports, DNS and where each distribution keeps its network configuration :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Addresses and routes

<div class="grid cards" markdown>

-   :material-ip-network-outline:{ .lg .middle } **[ip](ip.md)**

    ---

    Interfaces, addresses and routes.

</div>

## Check connections

<div class="grid cards" markdown>

-   :material-radar:{ .lg .middle } **[ping](ping.md)**

    ---

    Test whether a host answers.

-   :material-map-marker-path:{ .lg .middle } **[traceroute](traceroute.md)**

    ---

    Show the route to a host, hop by hop.

-   :material-chart-timeline-variant:{ .lg .middle } **[mtr](mtr.md)**

    ---

    Measure loss and latency per hop.

-   :material-lan-connect:{ .lg .middle } **[ss](ss.md)**

    ---

    Listening ports and open connections.

-   :material-swap-horizontal:{ .lg .middle } **[nc](nc.md)**

    ---

    Test ports and talk to services by hand.

</div>

## DNS

<div class="grid cards" markdown>

-   :material-dns-outline:{ .lg .middle } **[dig](dig.md)**

    ---

    Ask DNS servers directly.

-   :material-dns:{ .lg .middle } **[host](host.md)**

    ---

    Short DNS lookups.

-   :material-server-network:{ .lg .middle } **[resolvectl](resolvectl.md)**

    ---

    The local resolver of systemd.

</div>

## HTTP and downloads

<div class="grid cards" markdown>

-   :material-web:{ .lg .middle } **[curl](curl.md)**

    ---

    Test websites, APIs and certificates.

-   :material-download-network-outline:{ .lg .middle } **[wget](wget.md)**

    ---

    Download files, resume downloads.

</div>

## Configure the network

<div class="grid cards" markdown>

-   :material-network-outline:{ .lg .middle } **[nmcli](nmcli.md)**

    ---

    NetworkManager on RHEL, Rocky and Alma.

-   :material-file-cog-outline:{ .lg .middle } **[netplan](netplan.md)**

    ---

    Network configuration on Ubuntu.

-   :material-ethernet:{ .lg .middle } **[ifup](ifup.md)**

    ---

    Bring interfaces up and down on Debian.

</div>

## Firewall

<div class="grid cards" markdown>

-   :material-wall:{ .lg .middle } **[ufw](ufw.md)**

    ---

    Simple firewall of Debian and Ubuntu.

-   :material-wall-fire:{ .lg .middle } **[firewall-cmd](firewall-cmd.md)**

    ---

    firewalld on RHEL, Rocky and Alma.

-   :material-filter-outline:{ .lg .middle } **[nft](nft.md)**

    ---

    The packet filter in the kernel.

</div>

## Capture traffic

<div class="grid cards" markdown>

-   :material-waveform:{ .lg .middle } **[tcpdump](tcpdump.md)**

    ---

    Record and inspect network packets.

</div>
