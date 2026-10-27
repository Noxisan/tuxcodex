# resize2fs

> Vergrößert oder verkleinert ein ext4-Dateisystem. Vergrößern klappt sogar, während es eingehängt ist und benutzt wird.

![resize2fs output](../assets/screenshots/13-disks-storage/resize2fs.png)

## Syntax

```bash
resize2fs [OPTION]... GERÄT [GRÖSSE]
```

Zuerst muss die Partition oder das logische Volume vergrößert werden. `resize2fs` passt nur das Dateisystem daran an.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine Größe)* | Das Dateisystem auf die Größe der Partition oder des Volumes vergrößern |
| `GRÖSSE` | Neue Größe, z. B. `40G`, zum Verkleinern |
| `-P` | Die Mindestgröße zeigen, auf die sich das Dateisystem verkleinern lässt |
| `-p` | Fortschritt zeigen |

## Beispiele

**Die Partition vergrößern, nachdem die Platte auf 150 GB vergrößert wurde:**

```bash
sudo growpart /dev/sdb 1
```

```text
CHANGED: partition=1 start=2048 old: size=209713119 end=209715166 new: size=314570719 end=314572766
```

`growpart` kommt aus dem Paket `cloud-guest-utils` (Debian, Ubuntu) oder
`cloud-utils-growpart` (RHEL). Achte auf das Leerzeichen zwischen Platte und
Partitionsnummer.

**Das Dateisystem im laufenden Betrieb vergrößern:**

```bash
sudo resize2fs /dev/sdb1
```

```text
resize2fs 1.47.2 (1-Jan-2025)
Filesystem at /dev/sdb1 is mounted on /mnt/backup; on-line resizing required
old_desc_blocks = 13, new_desc_blocks = 19
The filesystem on /dev/sdb1 is now 39321339 (4k) blocks long.
```

**Das Ergebnis prüfen:**

```bash
df -h /mnt/backup
```

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb1       147G   32G  109G  23% /mnt/backup
```

**Herausfinden, wie klein es werden könnte:**

```bash
sudo resize2fs -P /dev/sdd1
```

```text
resize2fs 1.47.2 (1-Jan-2025)
Estimated minimum size of the filesystem: 712355
```

Der Wert ist in Blöcken zu 4 KiB angegeben, also etwa 2,7 GiB.

## Wann brauche ich das?

- Nachdem der Hoster eine virtuelle Platte vergrößert hat
- Nach `lvextend`, wenn du dessen Option `-r` nicht genutzt hast
- Um ein Dateisystem vor dem Verkleinern der Partition zu verkleinern (ausgehängt)

!!! tip "Die Reihenfolge ist entscheidend"
    Vergrößern: erst die Partition oder das Volume, dann das Dateisystem. Verkleinern: erst
    das Dateisystem, dann die Partition. Die falsche Reihenfolge kostet Daten.

!!! warning "Verkleinern nur ausgehängt"
    ext4 lässt sich nur verkleinern, wenn es nicht eingehängt ist, und erst nach
    `e2fsck -f`. Deshalb geht das beim Root-Dateisystem nur aus einem Rettungssystem.

## Verwandte Befehle

[lvextend](lvextend.md) · [xfs_growfs](xfs_growfs.md) · [parted](parted.md) · [df](df.md)
