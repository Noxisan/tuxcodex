# lvs

> Listet die logischen Volumes von LVM: die Volumes, auf denen die Dateisysteme liegen, mit Größe und Zustand.

![lvs output](../assets/screenshots/13-disks-storage/lvs.png)

## Syntax

```bash
lvs [OPTION]... [VG | LV]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Alle logischen Volumes |
| `-o FELDER` | Spalten wählen, z. B. `lv_name,lv_size,devices` |
| `-a` | Auch interne Volumes, etwa von Snapshots oder RAID |
| `lvdisplay LV` | Ausführliche Angaben zu einem logischen Volume |

## Beispiele

**Die logischen Volumes anzeigen:**

```bash
sudo lvs
```

```text
  LV     VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lv_srv vg_data -wi-ao---- 30.00g
```

**Anzeigen, auf welcher Platte das Volume liegt:**

```bash
sudo lvs -o lv_name,vg_name,lv_attr,lv_size,devices
```

```text
  LV     VG      Attr       LSize  Devices
  lv_srv vg_data -wi-ao---- 30.00g /dev/sdc(0)
```

**Details eines logischen Volumes:**

```bash
sudo lvdisplay vg_data/lv_srv
```

```text
  --- Logical volume ---
  LV Path                /dev/vg_data/lv_srv
  LV Name                lv_srv
  VG Name                vg_data
  LV UUID                9ciwx5-BCQV-RnST-pBr7-eGxZ-SLBE-Jaz9dm
  LV Write Access        read/write
  LV Creation host, time tuxdex-srv, 2026-09-18 09:41:22 +0200
  LV Status              available
  # open                 1
  LV Size                30.00 GiB
  Current LE             7680
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
```

`LV Path` ist das Gerät, das du formatierst und einhängst, `Current LE` die Anzahl der
Extents zu 4 MiB.

## Wann brauche ich das?

- Um zu sehen, welche logischen Volumes es gibt und wie groß sie sind
- Vor `lvextend`, um die aktuelle Größe zu prüfen
- Um herauszufinden, auf welchen Platten ein Volume liegt

!!! tip "Das Attribut `-wi-ao----`"
    `w` beschreibbar, `i` geerbte Zuteilung, `a` aktiv, `o` offen, also eingehängt oder in
    Benutzung. Ein Volume ohne `o` ist nicht eingehängt.

## Verwandte Befehle

[lvcreate](lvcreate.md) · [lvextend](lvextend.md) · [vgs](vgs.md)
