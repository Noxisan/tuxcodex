# virt-clone

> Kopiert eine vorhandene virtuelle Maschine: Definition und Plattenabbilder, mit neuem Namen, neuer MAC-Adresse und neuer UUID.

![virt-clone output](../assets/screenshots/31-virtualization/virt-clone.png)

## Syntax

```bash
virt-clone --original VM --name NEU --auto-clone
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--original VM` | Die zu kopierende VM; sie muss ausgeschaltet sein |
| `--name NEU` | Name der Kopie |
| `--auto-clone` | Dateinamen für die neuen Abbilder automatisch wählen |
| `--file PFAD` | Pfad für das neue Abbild, einmal pro Platte |
| `--mac MAC` | Eine feste MAC-Adresse statt einer zufälligen setzen |
| `--preserve-data` | Nur die Definition anlegen, die Abbilder nicht kopieren |

`virt-clone` kopiert die Hardware. Innen ist der Klon identisch: gleicher Hostname, gleiche SSH-Hostschlüssel, gleiche `/etc/machine-id`.

## Beispiele

**Eine ausgeschaltete VM klonen:**

```bash
sudo virt-clone --original web01 --name web02 --auto-clone
```

```text
Allocating 'web02.qcow2'                                    | 2.3 GB  00:00:06 ...

Clone 'web02' created successfully.
```

**Das Original läuft noch:**

```bash
sudo virt-clone --original db01 --name db02 --auto-clone
```

```text
ERROR    Domain to clone must be shutoff.
```

Fahr sie vorher mit `sudo virsh shutdown db01` herunter, klone sie und starte sie wieder.

**Den Pfad des neuen Abbilds selbst wählen:**

```bash
sudo virt-clone --original web01 --name web03 --file /srv/vms/web03.qcow2
```

```text
Allocating 'web03.qcow2'                                    | 2.3 GB  00:00:07 ...

Clone 'web03' created successfully.
```

**Dem Klon eine eigene Identität geben und ihn starten:**

```bash
sudo virt-sysprep -d web02 --hostname web02 >/dev/null
sudo virsh start web02
```

```text
Domain 'web02' started
```

## Wann brauche ich das?

- Um vor einem riskanten Versuch eine Testkopie einer Server-VM zu machen
- Um aus einer vorbereiteten Vorlage mehrere gleiche VMs zu erzeugen

!!! tip "Den Klon mit `virt-sysprep` vorbereiten"
    `sudo virt-sysprep -d web02 --hostname web02` (Paket `guestfs-tools`) setzt im
    ausgeschalteten Klon Machine-ID, SSH-Hostschlüssel, Logs und Hostnamen zurück. Danach ist
    die Kopie ein eigener Rechner.

!!! warning "Zwei Rechner mit derselben Identität"
    Ohne `virt-sysprep` haben beide VMs dieselbe `machine-id`. DHCP-Server können ihnen
    dieselbe Adresse geben, und SSH-Clients sehen auf zwei Servern denselben Hostschlüssel.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `virtinst` | `virtinst` | `virt-install` | `virt-install` |

## Verwandte Befehle

[virsh](virsh.md) · [virt-install](virt-install.md) · [qemu-img](qemu-img.md) · [hostnamectl](../01-orientation/hostnamectl.md)
