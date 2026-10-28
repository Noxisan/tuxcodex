# Understanding file shares

A file share makes a directory of the server available to other machines over the network.
On Linux there are two common ways: **NFS** and **Samba** (SMB, the protocol of Windows
shares).

## NFS or Samba?

| | NFS | Samba (SMB) |
|---|-----|-------------|
| Clients | Linux and other Unix systems | Windows, macOS, Linux |
| Users | By user ID: the IDs on client and server must match | Own Samba users with a password |
| Configuration | `/etc/exports` | `/etc/samba/smb.conf` |
| Port | 2049/tcp (NFSv4) | 445/tcp |
| Typical use | Shared data between Linux servers, backups, container volumes | Team shares, office files |

## Packages and services

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| NFS server | `nfs-kernel-server` | `nfs-kernel-server` | `nfs-utils` | `nfs-utils` |
| NFS service | `nfs-server` | `nfs-server` | `nfs-server` | `nfs-server` |
| NFS client | `nfs-common` | `nfs-common` | `nfs-utils` | `nfs-utils` |
| Samba server | `samba` | `samba` | `samba` | `samba` |
| Samba service | `smbd` | `smbd` | `smb` | `smb` |
| Samba client | `smbclient`, `cifs-utils` | `smbclient`, `cifs-utils` | `samba-client`, `cifs-utils` | `smbclient`, `cifs-utils` |
| Samba configuration | preinstalled `smb.conf` | preinstalled `smb.conf` | preinstalled `smb.conf` | none: copy `smb.conf.default` |

## An NFS share

`/etc/exports` has one line per directory: the path, then the clients with their options in
parentheses, without a space in between.

```text
/srv/nfs/backup   192.0.2.0/24(rw,sync,no_subtree_check)
/srv/nfs/iso      *(ro,no_subtree_check)
```

| Option | Meaning |
|--------|---------|
| `rw`, `ro` | Read and write, or read only |
| `sync` | Write to disk before answering (safe, the default) |
| `no_subtree_check` | No check of the path for every request, recommended |
| `root_squash` | `root` on the client becomes `nobody` on the server (the default) |
| `no_root_squash` | `root` on the client stays `root`: only for trusted machines |

The steps on the server and on a client:

```text
$ sudo mkdir -p /srv/nfs/backup
$ sudoedit /etc/exports                      # add the line
$ sudo exportfs -ra                          # activate
$ sudo exportfs -v                           # check

client$ showmount -e 192.0.2.10              # what does the server export?
client$ sudo mount -t nfs 192.0.2.10:/srv/nfs/backup /mnt/backup
```

In `/etc/fstab` on the client:
`192.0.2.10:/srv/nfs/backup  /mnt/backup  nfs  defaults,_netdev  0  0`

## A Samba share

A section at the end of `/etc/samba/smb.conf`. The name in brackets is the share name:

```text
[team]
   path = /srv/share/team
   valid users = @team
   read only = no
   create mask = 0660
   directory mask = 0770
```

The steps:

```text
$ sudo mkdir -p /srv/share/team
$ sudo chgrp team /srv/share/team && sudo chmod 2770 /srv/share/team
$ sudoedit /etc/samba/smb.conf               # add the section
$ testparm -s                                # check
$ sudo smbpasswd -a nox                      # Samba password for an existing user
$ sudo systemctl reload smbd
$ smbclient //localhost/team -U nox -c ls    # test
```

Windows connects with `\\192.0.2.10\team`, Linux mounts with
`sudo mount -t cifs //192.0.2.10/team /mnt/team -o username=nox`.

## Ports and firewall

| Service | Port |
|---------|------|
| NFSv4 | 2049/tcp |
| NFSv3 (additionally) | 111/tcp+udp (rpcbind), `mountd` on a changing port |
| Samba | 445/tcp |

With [`ufw`](../11-network/ufw.md): `sudo ufw allow from 192.0.2.0/24 to any port 2049 proto tcp`.
With [`firewall-cmd`](../11-network/firewall-cmd.md): `--add-service=nfs` or `--add-service=samba`.

!!! tip "Same user IDs for NFS"
    NFS checks permissions by numbers. If `nox` has ID 1000 on the server and 1001 on the
    client, files belong to someone else. Give users the same IDs everywhere, see
    [`id`](../01-orientation/id.md).

!!! warning "Never share to the internet"
    Neither NFS nor SMB belongs on a public interface. Allow the ports only from your own
    network, or use a VPN like [WireGuard](../26-wireguard/index.md).
