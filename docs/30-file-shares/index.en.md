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

-   :material-console-network-outline:{ .lg .middle } **[smbclient](smbclient.md)**

    ---

    Test and use SMB shares.

</div>

## From other chapters

<div class="grid cards" markdown>

-   :material-link-variant:{ .lg .middle } **[mount](../13-disks-storage/mount.md)**

    ---

    Mount NFS and SMB shares on a client. Covered in the chapter Storage.

-   :material-account-multiple-outline:{ .lg .middle } **[useradd](../07-users-groups/useradd.md)**

    ---

    Create users for Samba. Covered in the chapter Users & groups.

-   :material-shield-lock-outline:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Open the ports for your own network only. Covered in the chapter Network.

-   :material-shield-lock-outline:{ .lg .middle } **[firewall-cmd](../11-network/firewall-cmd.md)**

    ---

    Allow the services nfs and samba on RHEL. Covered in the chapter Network.

</div>
