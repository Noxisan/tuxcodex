# getenforce

> Unter RHEL, Rocky und Alma: zeigt, ob SELinux erzwingt, nur protokolliert oder ausgeschaltet ist.

![getenforce output](../assets/screenshots/25-selinux-apparmor/getenforce.png)

## Syntax

```bash
getenforce
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| (keine) | Den aktuellen Modus ausgeben: `Enforcing`, `Permissive` oder `Disabled` |

| Modus | Bedeutung |
|-------|-----------|
| `Enforcing` | Regeln werden angewendet: Verbotene Zugriffe werden blockiert und protokolliert |
| `Permissive` | Regeln werden nur geprüft: Verbotene Zugriffe werden protokolliert, aber erlaubt |
| `Disabled` | SELinux ist vollständig ausgeschaltet |

## Beispiele

**Den Modus prüfen:**

```bash
getenforce
```

```text
Enforcing
```

**Nach einem vorübergehenden Wechsel auf permissive:**

```bash
sudo setenforce 0
getenforce
```

```text
Permissive
```

**Als Prüfung in einem Skript:**

```bash
[ "$(getenforce)" = "Enforcing" ] || echo "WARNING: SELinux is not enforcing on $(hostname)"
```

```text
WARNING: SELinux is not enforcing on tuxdex-srv
```

## Wann brauche ich das?

- Als erste Prüfung, wenn ein Dienst unter RHEL „Permission denied“ bekommt
- In Skripten und im Monitoring, um sicherzugehen, dass SELinux nicht abgeschaltet wurde
- Nach einem Neustart, um den Modus aus `/etc/selinux/config` zu bestätigen

!!! tip "Details mit sestatus"
    `getenforce` zeigt nur den Modus. [`sestatus`](sestatus.md) zeigt außerdem die
    Richtlinie und den Modus, der nach dem nächsten Neustart gilt.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| SELinux | nicht aktiv (stattdessen AppArmor) | nicht aktiv (stattdessen AppArmor) | aktiv, `enforcing` | nicht aktiv |
| Paket | `selinux-utils` (nur wenn SELinux eingerichtet ist) | `selinux-utils` (nur wenn SELinux eingerichtet ist) | `libselinux-utils`, vorinstalliert | nicht in den offiziellen Repositorys |

## Verwandte Befehle

[setenforce](setenforce.md) · [sestatus](sestatus.md) · [aa-status](aa-status.md)
