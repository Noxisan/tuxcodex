# aa-status

> Unter Debian und Ubuntu: zeigt, ob AppArmor aktiv ist, welche Profile geladen sind und welche Prozesse sie schützen.

![aa-status output](../assets/screenshots/25-selinux-apparmor/aa-status.png)

## Syntax

```bash
aa-status [--enabled | --json]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| (keine) | Vollständiger Überblick: Profile und Prozesse je Modus |
| `--enabled` | Nur ein Exit-Code: 0, wenn AppArmor aktiv ist |
| `--json`, `--pretty-json` | Maschinenlesbare Ausgabe |
| `--complaining`, `--enforced` | Nur die Anzahl der Profile in diesem Modus |

Die Profile liegen in `/etc/apparmor.d/`. Ablehnungen erscheinen im Kernel-Log als `apparmor="DENIED"`.

## Beispiele

**Der Überblick:**

```bash
sudo aa-status
```

```text
apparmor module is loaded.
24 profiles are loaded.
21 profiles are in enforce mode.
   /usr/bin/man
   /usr/sbin/chronyd
   /usr/sbin/nginx
   lsb_release
   man_filter
   man_groff
   nvidia_modprobe
   ...
3 profiles are in complain mode.
   /usr/sbin/php-fpm8.4
   ...
0 profiles are in prompt mode.
0 profiles are in kill mode.
0 profiles are in unconfined mode.
3 processes have profiles defined.
3 processes are in enforce mode.
   /usr/sbin/chronyd (598)
   /usr/sbin/nginx (812)
   /usr/sbin/nginx (813)
0 processes are in complain mode.
0 processes are unconfined but have a profile defined.
```

Gekürzt. nginx läuft im Enforce-Modus, sein Profil wird also angewendet; php-fpm protokolliert nur.

**Zeigen, was AppArmor blockiert hat:**

```bash
sudo journalctl -k | grep 'apparmor="DENIED"' | tail -1
```

```text
Oct 26 10:42:17 tuxdex-srv kernel: audit: type=1400 audit(1793094137.412:88): apparmor="DENIED" operation="open" class="file" profile="/usr/sbin/nginx" name="/srv/status/index.html" pid=1384 comm="nginx" requested_mask="r" denied_mask="r" fsuid=33 ouid=0
```

Das nginx-Profil erlaubt `/srv/status/` nicht. Ergänze den Pfad im Profil, siehe [`aa-complain`](aa-complain.md).

**Als Prüfung in einem Skript:**

```bash
sudo aa-status --enabled && echo "AppArmor is active"
```

```text
AppArmor is active
```

## Wann brauche ich das?

- Als erste Prüfung, wenn ein Dienst unter Debian oder Ubuntu „Permission denied“ bekommt
- Um zu sehen, welche Dienste überhaupt durch ein Profil geschützt sind
- Nach dem Ändern eines Profils, um zu bestätigen, dass es im richtigen Modus geladen ist

!!! tip "Ablehnungen finden"
    `sudo journalctl -k | grep apparmor=\"DENIED\"` zeigt, was AppArmor blockiert hat, mit
    Profil, Vorgang und Pfad.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| AppArmor | aktiv | aktiv | nicht verfügbar (stattdessen SELinux) | möglich, Kernel-Parameter `lsm=` nötig |
| Paket | `sudo apt install apparmor-utils` | `apparmor-utils`, vorinstalliert | nicht verfügbar | `sudo pacman -S apparmor` |

## Verwandte Befehle

[aa-complain](aa-complain.md) · [getenforce](getenforce.md) · [journalctl](../09-systemd/journalctl.md)
