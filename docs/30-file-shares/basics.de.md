# Dateifreigaben verstehen

Eine Freigabe stellt ein Verzeichnis des Servers anderen Rechnern im Netzwerk zur Verfügung.
Unter Linux gibt es dafür zwei gängige Wege: **NFS** und **Samba** (SMB, das Protokoll der
Windows-Freigaben).

## NFS oder Samba?

| | NFS | Samba (SMB) |
|---|-----|-------------|
| Clients | Linux und andere Unix-Systeme | Windows, macOS, Linux |
| Benutzer | Über die Benutzer-ID: Die IDs auf Client und Server müssen passen | Eigene Samba-Benutzer mit Passwort |
| Konfiguration | `/etc/exports` | `/etc/samba/smb.conf` |
| Port | 2049/tcp (NFSv4) | 445/tcp |
| Typischer Einsatz | Gemeinsame Daten zwischen Linux-Servern, Backups, Container-Volumes | Team-Freigaben, Office-Dateien |

## Pakete und Dienste

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| NFS-Server | `nfs-kernel-server` | `nfs-kernel-server` | `nfs-utils` | `nfs-utils` |
| NFS-Dienst | `nfs-server` | `nfs-server` | `nfs-server` | `nfs-server` |
| NFS-Client | `nfs-common` | `nfs-common` | `nfs-utils` | `nfs-utils` |
| Samba-Server | `samba` | `samba` | `samba` | `samba` |
| Samba-Dienst | `smbd` | `smbd` | `smb` | `smb` |
| Samba-Client | `smbclient`, `cifs-utils` | `smbclient`, `cifs-utils` | `samba-client`, `cifs-utils` | `smbclient`, `cifs-utils` |
| Samba-Konfiguration | `smb.conf` vorinstalliert | `smb.conf` vorinstalliert | `smb.conf` vorinstalliert | keine: `smb.conf.default` kopieren |

## Eine NFS-Freigabe

In `/etc/exports` steht pro Verzeichnis eine Zeile: der Pfad, dann die Clients mit ihren
Optionen in Klammern, ohne Leerzeichen dazwischen.

```text
/srv/nfs/backup   192.0.2.0/24(rw,sync,no_subtree_check)
/srv/nfs/iso      *(ro,no_subtree_check)
```

| Option | Bedeutung |
|--------|-----------|
| `rw`, `ro` | Lesen und schreiben oder nur lesen |
| `sync` | Erst auf die Platte schreiben, dann antworten (sicher, der Standard) |
| `no_subtree_check` | Keine Prüfung des Pfads bei jeder Anfrage, empfohlen |
| `root_squash` | `root` auf dem Client wird auf dem Server zu `nobody` (der Standard) |
| `no_root_squash` | `root` auf dem Client bleibt `root`: nur für vertrauenswürdige Rechner |

Die Schritte auf dem Server und auf einem Client:

```text
$ sudo mkdir -p /srv/nfs/backup
$ sudoedit /etc/exports                      # Zeile eintragen
$ sudo exportfs -ra                          # aktivieren
$ sudo exportfs -v                           # prüfen

client$ showmount -e 192.0.2.10              # Was gibt der Server frei?
client$ sudo mount -t nfs 192.0.2.10:/srv/nfs/backup /mnt/backup
```

In `/etc/fstab` auf dem Client:
`192.0.2.10:/srv/nfs/backup  /mnt/backup  nfs  defaults,_netdev  0  0`

## Eine Samba-Freigabe

Ein Abschnitt am Ende von `/etc/samba/smb.conf`. Der Name in eckigen Klammern ist der Name
der Freigabe:

```text
[team]
   path = /srv/share/team
   valid users = @team
   read only = no
   create mask = 0660
   directory mask = 0770
```

Die Schritte:

```text
$ sudo mkdir -p /srv/share/team
$ sudo chgrp team /srv/share/team && sudo chmod 2770 /srv/share/team
$ sudoedit /etc/samba/smb.conf               # Abschnitt eintragen
$ testparm -s                                # prüfen
$ sudo smbpasswd -a nox                      # Samba-Passwort für einen vorhandenen Benutzer
$ sudo systemctl reload smbd
$ smbclient //localhost/team -U nox -c ls    # testen
```

Windows verbindet sich mit `\\192.0.2.10\team`, Linux hängt die Freigabe mit
`sudo mount -t cifs //192.0.2.10/team /mnt/team -o username=nox` ein.

## Ports und Firewall

| Dienst | Port |
|--------|------|
| NFSv4 | 2049/tcp |
| NFSv3 (zusätzlich) | 111/tcp+udp (rpcbind), `mountd` auf wechselndem Port |
| Samba | 445/tcp |

Mit [`ufw`](../11-network/ufw.md): `sudo ufw allow from 192.0.2.0/24 to any port 2049 proto tcp`.
Mit [`firewall-cmd`](../11-network/firewall-cmd.md): `--add-service=nfs` oder `--add-service=samba`.

!!! tip "Gleiche Benutzer-IDs für NFS"
    NFS prüft Rechte anhand von Zahlen. Hat `nox` auf dem Server die ID 1000 und auf dem
    Client 1001, gehören die Dateien plötzlich jemand anderem. Gib Benutzern überall
    dieselben IDs, siehe [`id`](../01-orientation/id.md).

!!! warning "Nie ins Internet freigeben"
    Weder NFS noch SMB gehören auf eine öffentliche Schnittstelle. Erlaube die Ports nur aus
    dem eigenen Netz oder nutze ein VPN wie [WireGuard](../26-wireguard/index.md).
