---
title: "Dateifreigaben"
icon: material/folder-network-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-folder-network-outline:{ .tc-hero-icon }

# Dateifreigaben

Verzeichnisse im Netzwerk freigeben: NFS für Linux-Clients, Samba für Windows, macOS und
Linux. Freigaben exportieren, die Konfiguration prüfen, Samba-Benutzer verwalten und den
Zugriff testen.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** NFS oder Samba, `/etc/exports` und `smb.conf`, eine Freigabe Schritt für Schritt einrichten, Ports und Firewall :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## NFS

<div class="grid cards" markdown>

-   :material-folder-arrow-up-outline:{ .lg .middle } **[exportfs](exportfs.md)**

    ---

    NFS-Freigaben aktivieren und anzeigen.

-   :material-format-list-bulleted:{ .lg .middle } **[showmount](showmount.md)**

    ---

    Welche Freigaben ein Server anbietet.

</div>

## Samba

<div class="grid cards" markdown>

-   :material-file-check-outline:{ .lg .middle } **[testparm](testparm.md)**

    ---

    Die Samba-Konfiguration prüfen.

-   :material-account-key-outline:{ .lg .middle } **[smbpasswd](smbpasswd.md)**

    ---

    Samba-Benutzer und Passwörter verwalten.

-   :material-console-network-outline:{ .lg .middle } **[smbclient](smbclient.md)**

    ---

    SMB-Freigaben testen und nutzen.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-link-variant:{ .lg .middle } **[mount](../13-disks-storage/mount.md)**

    ---

    NFS- und SMB-Freigaben auf einem Client einhängen. Behandelt im Kapitel Datenträger.

-   :material-account-multiple-outline:{ .lg .middle } **[useradd](../07-users-groups/useradd.md)**

    ---

    Benutzer für Samba anlegen. Behandelt im Kapitel Benutzer & Gruppen.

-   :material-shield-lock-outline:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Die Ports nur fürs eigene Netz öffnen. Behandelt im Kapitel Netzwerk.

-   :material-shield-lock-outline:{ .lg .middle } **[firewall-cmd](../11-network/firewall-cmd.md)**

    ---

    Die Dienste nfs und samba unter RHEL erlauben. Behandelt im Kapitel Netzwerk.

</div>
