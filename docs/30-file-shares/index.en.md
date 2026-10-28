---
icon: material/folder-network-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-folder-network-outline:{ .tc-hero-icon }

# File shares

Sharing directories over the network: NFS for Linux clients, Samba for Windows, macOS and
Linux. Exporting, checking the configuration, managing Samba users and testing access.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** NFS or Samba, `/etc/exports` and `smb.conf`, setting up a share step by step, ports and firewall :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## NFS

<div class="grid cards" markdown>

-   :material-folder-arrow-up-outline:{ .lg .middle } **[exportfs](exportfs.md)**

    ---

    Activate and show NFS shares.

-   :material-format-list-bulleted:{ .lg .middle } **[showmount](showmount.md)**

    ---

    Which shares a server offers.

</div>

## Samba

<div class="grid cards" markdown>

-   :material-file-check-outline:{ .lg .middle } **[testparm](testparm.md)**

    ---

    Check the Samba configuration.

-   :material-account-key-outline:{ .lg .middle } **[smbpasswd](smbpasswd.md)**

    ---

    Manage Samba users and passwords.

</div>
