# xfs_growfs

> Vergrößert ein XFS-Dateisystem auf die Größe seiner Partition oder seines Volumes, im eingehängten Zustand. XFS lässt sich nicht verkleinern.

![xfs_growfs output](../assets/screenshots/13-disks-storage/xfs_growfs.png)

## Syntax

```bash
xfs_growfs [OPTION]... EINHÄNGEPUNKT
```

Anders als `resize2fs` arbeitet `xfs_growfs` über den **Einhängepunkt**: Das Dateisystem muss eingehängt sein.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Auf die volle Größe des Geräts vergrößern |
| `-D BLÖCKE` | Auf diese Anzahl an Blöcken vergrößern |
| `-n` | Nur die aktuelle Aufteilung zeigen, nichts ändern |

## Beispiele

**Ein XFS-Dateisystem nach `lvextend` vergrößern:**

```bash
sudo xfs_growfs /srv/data
```

```text
meta-data=/dev/mapper/vg_data-lv_srv isize=512    agcount=4, agsize=1966080 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=1
         =                       reflink=1    bigtime=1 inobtcount=1 nrext64=1
data     =                       bsize=4096   blocks=7864320, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1, parent=0
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 7864320 to 13107200
```

Von 30 GiB (7864320 Blöcke zu 4 KiB) auf 50 GiB.

**Das Ergebnis prüfen:**

```bash
df -hT /srv/data
```

```text
Filesystem                 Type  Size  Used Avail Use% Mounted on
/dev/mapper/vg_data-lv_srv xfs    50G  7.2G   43G  15% /srv/data
```

**Ein Dateisystem, das nicht eingehängt ist:**

```bash
sudo xfs_growfs /dev/sdd1
```

```text
xfs_growfs: /dev/sdd1 is not a mounted XFS filesystem
```

`/dev/sdd1` ist nicht eingehängt und enthält ext4. `xfs_growfs` arbeitet nur mit
eingehängten XFS-Dateisystemen.

## Wann brauche ich das?

- Unter RHEL, Rocky und Alma, wo XFS das Standard-Dateisystem ist
- Nach `lvextend` oder nach dem Vergrößern einer Partition
- Wenn ein XFS-Volume vollläuft

!!! tip "`lvextend -r` erledigt das für dich"
    [`lvextend -r`](lvextend.md) vergrößert das logische Volume und ruft `xfs_growfs` selbst auf.

!!! warning "XFS kann nur wachsen"
    Ein XFS-Dateisystem lässt sich nicht verkleinern. Brauchst du den Platz später vielleicht
    für etwas anderes, vergrößere in kleinen Schritten.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| XFS-Werkzeuge installiert | nein, Paket `xfsprogs` | ja | ja | nein, Paket `xfsprogs` |

## Verwandte Befehle

[resize2fs](resize2fs.md) · [lvextend](lvextend.md) · [mkfs](mkfs.md) · [df](df.md)
