# mkswap

> Bereitet eine Partition oder eine Datei als Swap vor, den Bereich, den Linux nutzt, wenn der Arbeitsspeicher knapp wird.

![mkswap output](../assets/screenshots/13-disks-storage/mkswap.png)

## Syntax

```bash
mkswap [OPTION]... GERÄT | DATEI
```

Nach `mkswap` ist der Swap bereit, aber noch nicht in Benutzung. [`swapon`](swapon.md) aktiviert ihn.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-L LABEL` | Dem Swap-Bereich einen Namen geben |
| `-U UUID` | Eine bestimmte UUID setzen |
| `--file DATEI -s GRÖSSE` | Die Swap-Datei in einem Schritt anlegen und vorbereiten (neueres util-linux) |

## Beispiele

**Eine Swap-Datei mit 2 GiB anlegen:**

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
```

```text
Setting up swapspace version 1, size = 2 GiB (2147479552 bytes)
no label, UUID=6f1d3a8c-2e5b-4c97-8a40-b3e9d7f2c516
```

**Eine Swap-Partition mit Label vorbereiten:**

```bash
sudo mkswap -L swap /dev/sda3
```

```text
mkswap: /dev/sda3: warning: wiping old swap signature.
Setting up swapspace version 1, size = 1024 MiB (1073737728 bytes)
LABEL=swap, UUID=8e2b6d4f-1a3c-4f5e-b7d9-0c2e4a6f8b31
```

**Die Swap-Datei dauerhaft machen:**

```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

```text
/swapfile none swap sw 0 0
```

## Wann brauche ich das?

- Wenn ein Server zu wenig Arbeitsspeicher und gar keinen Swap hat
- Um einem Cloud-Server eine Swap-Datei zu geben, ohne Partitionen zu ändern
- Nach dem Austausch oder der Größenänderung der Swap-Partition

!!! tip "Swap-Datei statt Partition"
    Eine Swap-Datei lässt sich jederzeit anlegen, vergrößern und entfernen, ohne die
    Partitionen anzufassen. Für die meisten Server ist das die flexiblere Wahl.

!!! warning "Rechte der Swap-Datei"
    Eine Swap-Datei darf nur für root lesbar sein (`chmod 600`). Sonst könnten andere
    Benutzer Speicherinhalte lesen, `mkswap` warnt vor unsicheren Rechten.

## Verwandte Befehle

[swapon](swapon.md) · [free](../08-processes/free.md) · [mkfs](mkfs.md)
