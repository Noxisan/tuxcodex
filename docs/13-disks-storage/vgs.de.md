# vgs

> Listet die Volume Groups von LVM: die Speicherpools, aus denen logische Volumes entnommen werden. `vgcreate` legt eine an, `vgextend` fügt ihr Platten hinzu.

![vgs output](../assets/screenshots/13-disks-storage/vgs.png)

## Syntax

```bash
vgs [OPTION]... [VG]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Alle Volume Groups mit Größe und freiem Platz |
| `vgcreate VG PV...` | Eine Volume Group aus physischen Volumes anlegen |
| `vgextend VG PV` | Einer Volume Group ein physisches Volume hinzufügen |
| `vgdisplay VG` | Ausführliche Angaben zu einer Volume Group |

## Beispiele

**Die Volume Groups anzeigen:**

```bash
sudo vgs
```

```text
  VG      #PV #LV #SN Attr   VSize   VFree
  vg_data   1   1   0 wz--n- <50.00g <20.00g
```

**Der Volume Group eine neue Platte hinzufügen:**

```bash
sudo vgextend vg_data /dev/sdd
sudo vgs
```

```text
  Volume group "vg_data" successfully extended
  VG      #PV #LV #SN Attr   VSize  VFree
  vg_data   2   1   0 wz--n- 99.99g 69.99g
```

Die Gruppe hat jetzt zwei Platten und fast 70 GiB frei.

**Eine neue Volume Group anlegen:**

```bash
sudo vgcreate vg_backup /dev/sde
```

```text
  Volume group "vg_backup" successfully created
```

## Wann brauche ich das?

- Um zu sehen, wie viel Platz für neue oder größere logische Volumes übrig ist
- Wenn `lvextend` zu wenig freien Platz meldet: die Gruppe um eine neue Platte erweitern
- Beim Einrichten von LVM auf einem neuen Server

!!! tip "Die Spalten"
    `#PV` physische Volumes, `#LV` logische Volumes, `#SN` Snapshots, `VFree` Platz, der noch
    keinem logischen Volume zugeteilt ist.

## Verwandte Befehle

[pvs](pvs.md) · [lvs](lvs.md) · [lvcreate](lvcreate.md) · [lvextend](lvextend.md)
