# exportfs

> Aktiviert die NFS-Freigaben aus `/etc/exports` und zeigt, was der Server gerade freigibt.

![exportfs output](../assets/screenshots/30-file-shares/exportfs.png)

## Syntax

```bash
exportfs [-r | -a | -u] [-v] [-o OPTIONEN] [CLIENT:/PFAD]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-r` | Neu exportieren: `/etc/exports` übernehmen, entfernt auch dort gelöschte Freigaben |
| `-a` | Alle Verzeichnisse freigeben (oder mit `-u` alle Freigaben beenden) |
| `-v` | Die Freigaben mit allen Optionen zeigen, auch den Standardwerten |
| `-s` | Die Freigaben im Format von `/etc/exports` zeigen |
| `-o OPTIONEN` | Ein Verzeichnis vorübergehend freigeben, ohne `/etc/exports` |
| `-u CLIENT:/PFAD` | Eine Freigabe beenden |

`exportfs` gehört zum Paket des NFS-Servers und ändert die Freigabetabelle des Kernels. Mit `-o` angelegte Freigaben verschwinden beim nächsten `exportfs -ra` oder Neustart.

## Beispiele

**Die aktuellen Freigaben mit allen Optionen zeigen:**

```bash
sudo exportfs -v
```

```text
/srv/nfs/backup
                192.0.2.0/24(sync,wdelay,hide,no_subtree_check,sec=sys,rw,secure,root_squash,no_all_squash)
/srv/nfs/iso      <world>(sync,wdelay,hide,no_subtree_check,sec=sys,ro,secure,root_squash,no_all_squash)
```

**Ein geändertes `/etc/exports` übernehmen:**

```bash
sudo exportfs -ra && sudo exportfs -s
```

```text
/srv/nfs/backup  192.0.2.0/24(sync,wdelay,hide,no_subtree_check,sec=sys,rw,secure,root_squash,no_all_squash)
/srv/nfs/iso  *(sync,wdelay,hide,no_subtree_check,sec=sys,ro,secure,root_squash,no_all_squash)
```

**Eine Warnung wegen einer fehlenden Option:**

```bash
sudo exportfs -ra
```

```text
exportfs: /etc/exports [3]: Neither 'subtree_check' or 'no_subtree_check' specified for export "198.51.100.23:/srv/nfs/web".
  Assuming default behaviour ('no_subtree_check').
  NOTE: this default has changed since nfs-utils version 1.0.x
```

Die Freigabe funktioniert trotzdem. Ergänz `no_subtree_check` in Zeile 3, dann ist die Warnung weg.

**Ein Verzeichnis vorübergehend freigeben und wieder beenden:**

```bash
sudo exportfs -o ro,no_subtree_check 198.51.100.23:/srv/migration
sudo exportfs | grep migration
sudo exportfs -u 198.51.100.23:/srv/migration
```

```text
/srv/migration    198.51.100.23
```

## Wann brauche ich das?

- Nach jeder Änderung an `/etc/exports`: `sudo exportfs -ra`
- Um zu prüfen, welche Optionen eine Freigabe wirklich hat, auch Standardwerte wie `root_squash`
- Um ein Verzeichnis kurzzeitig freizugeben, etwa für eine Migration

!!! tip "Kein Neustart nötig"
    `sudo exportfs -ra` übernimmt die Änderungen, während der NFS-Server weiterläuft. Clients,
    die die Freigabe eingehängt haben, arbeiten einfach weiter.

!!! warning "Kein Leerzeichen vor der Klammer"
    `/srv/nfs/backup 192.0.2.0/24(rw)` gibt dem Netz Lese- und Schreibzugriff.
    `/srv/nfs/backup 192.0.2.0/24 (rw)` gibt dem Netz nur Lesezugriff und **allen** Lese- und
    Schreibzugriff: Die Optionen gehören dann zum Client `*`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `nfs-kernel-server` | `nfs-kernel-server` | `nfs-utils` | `nfs-utils` |
| Dienst nach der Installation gestartet | ja | ja | nein: `systemctl enable --now nfs-server` | nein: `systemctl enable --now nfs-server` |
| Firewall | Port in `ufw` öffnen, falls aktiv | Port in `ufw` öffnen, falls aktiv | `firewall-cmd --add-service=nfs --permanent` | je nach Einrichtung |

## Verwandte Befehle

[showmount](showmount.md) · [mount](../13-disks-storage/mount.md) · [systemctl](../09-systemd/systemctl.md) · [smbclient](smbclient.md)
