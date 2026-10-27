# sestatus

> Unter RHEL, Rocky und Alma: zeigt den vollständigen SELinux-Status: Modus, Richtlinie, eingestellten Modus und Booleans.

![sestatus output](../assets/screenshots/25-selinux-apparmor/sestatus.png)

## Syntax

```bash
sestatus [-v] [-b]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| (keine) | Status, Modus, Richtlinie und der Modus aus der Konfigurationsdatei |
| `-b` | Auch alle Booleans mit ihrem Zustand auflisten |
| `-v` | Auch die Kontexte wichtiger Dateien und Prozesse zeigen |

## Beispiele

**Der vollständige Status:**

```bash
sestatus
```

```text
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      35
```

**Jemand hat auf permissive umgestellt:**

```bash
sestatus | grep -i mode
```

```text
Current mode:                   permissive
Mode from config file:          enforcing
```

**Die Booleans für den Webserver:**

```bash
sestatus -b | grep -E 'httpd_can_network_connect |httpd_enable_homedirs'
```

```text
httpd_can_network_connect                  off
httpd_enable_homedirs                      off
```

## Wann brauche ich das?

- Um auf einen Blick zu sehen, ob aktueller und eingestellter Modus übereinstimmen
- Um zu prüfen, welche Richtlinie geladen ist (meist `targeted`)
- Beim Dokumentieren des Zustands eines Servers

!!! warning "Aktueller Modus und Konfiguration weichen ab"
    `Current mode: permissive` und `Mode from config file: enforcing` heißt, jemand hat
    `setenforce 0` ausgeführt. Nach dem nächsten Neustart blockiert SELinux wieder, also
    behebe die Ursache vorher.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| SELinux | nicht aktiv (stattdessen AppArmor) | nicht aktiv (stattdessen AppArmor) | aktiv, `enforcing` | nicht aktiv |
| Paket | `selinux-utils` (nur wenn SELinux eingerichtet ist) | `selinux-utils` (nur wenn SELinux eingerichtet ist) | `libselinux-utils`, vorinstalliert | nicht in den offiziellen Repositorys |

## Verwandte Befehle

[getenforce](getenforce.md) · [setenforce](setenforce.md) · [setsebool](setsebool.md)
