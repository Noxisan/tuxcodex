# showmount

> Fragt einen NFS-Server, welche Verzeichnisse er freigibt und, mit Einschränkungen, welche Clients sie eingehängt haben.

![showmount output](../assets/screenshots/30-file-shares/showmount.png)

## Syntax

```bash
showmount [-e | -a | -d] [SERVER]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-e` | Die Freigaben des Servers auflisten |
| `-a` | Clients und die von ihnen eingehängten Verzeichnisse zeigen |
| `-d` | Nur die Verzeichnisse zeigen, die Clients eingehängt haben |
| `--no-headers` | Die Überschriftszeile weglassen |

Ohne Server fragt `showmount` den eigenen Rechner. Es spricht mit `mountd` von NFSv3: Ein Server, der nur NFSv4 anbietet oder Port 111 sperrt, antwortet nicht.

## Beispiele

**Die Freigaben eines Servers:**

```bash
showmount -e 192.0.2.10
```

```text
Export list for 192.0.2.10:
/srv/nfs/iso    *
/srv/nfs/backup 192.0.2.0/24
```

**Die eigenen Freigaben auf dem Server prüfen:**

```bash
showmount -e
```

```text
Export list for tuxdex-srv:
/srv/nfs/iso    *
/srv/nfs/backup 192.0.2.0/24
```

**Welche Clients etwas eingehängt haben:**

```bash
showmount -a
```

```text
All mount points on tuxdex-srv:
192.0.2.21:/srv/nfs/backup
192.0.2.22:/srv/nfs/backup
```

**Die Firewall blockiert die Anfrage:**

```bash
showmount -e 192.0.2.30
```

```text
clnt_create: RPC: Port mapper failure - Unable to receive: errno 113 (No route to host)
```

Port 111 ist gesperrt. Unter RHEL öffnest du ihn mit `sudo firewall-cmd --permanent --add-service={rpc-bind,mountd}` plus `--reload`, oder du hängst direkt per NFSv4 ein: Das braucht nur Port 2049.

## Wann brauche ich das?

- Auf einem Client vor dem Einhängen: Was bietet der Server an?
- Um nach `exportfs -ra` zu prüfen, ob eine Freigabe von außen sichtbar ist
- Wenn ein Mount scheitert: Liegt es an der Freigabe, am Netz oder an der Firewall?

!!! warning "`-a` ist nicht zuverlässig"
    Die Liste der eingehängten Clients führt `mountd`, und sie wird nicht bereinigt, wenn ein
    Client ohne Aushängen herunterfährt. NFSv4-Clients tauchen gar nicht auf. Einen aktuellen
    Überblick gibt `ss -tn sport = :2049` auf dem Server.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `nfs-common` | `nfs-common` | `nfs-utils` | `nfs-utils` |

## Verwandte Befehle

[exportfs](exportfs.md) · [mount](../13-disks-storage/mount.md) · [ss](../11-network/ss.md) · [firewall-cmd](../11-network/firewall-cmd.md)
