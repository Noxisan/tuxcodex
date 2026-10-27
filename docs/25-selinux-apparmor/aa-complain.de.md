# aa-complain

> Unter Debian und Ubuntu: schaltet AppArmor-Profile in den Complain-Modus (nur protokollieren) oder zurück in den Enforce-Modus.

![aa-complain output](../assets/screenshots/25-selinux-apparmor/aa-complain.png)

## Syntax

```bash
aa-complain PROFIL|PROGRAMM...
aa-enforce PROFIL|PROGRAMM...
aa-disable PROFIL...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `aa-complain` | Verstöße nur protokollieren, nicht blockieren |
| `aa-enforce` | Das Profil wieder anwenden |
| `aa-disable` | Das Profil vollständig entladen |
| `aa-logprof` | Die protokollierten Verstöße durchgehen und interaktiv ins Profil übernehmen |
| `apparmor_parser -r DATEI` | Ein Profil nach dem Bearbeiten neu laden |

Kleine Ergänzungen gehören nach `/etc/apparmor.d/local/` (etwa `local/usr.sbin.nginx`), damit Paket-Updates sie nicht überschreiben.

## Beispiele

**nginx für einen Test in den Complain-Modus setzen:**

```bash
sudo aa-complain /usr/sbin/nginx
```

```text
Setting /usr/sbin/nginx to complain mode.
```

**Ein Verzeichnis erlauben und zurückschalten:**

```bash
echo '/srv/status/** r,' | sudo tee -a /etc/apparmor.d/local/usr.sbin.nginx
sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx
sudo aa-enforce /usr/sbin/nginx
```

```text
/srv/status/** r,
Setting /usr/sbin/nginx to enforce mode.
```

**Den Modus danach prüfen:**

```bash
sudo aa-status | grep -A1 'complain mode'
```

```text
1 profiles are in complain mode.
   /usr/sbin/php-fpm8.4
```

## Wann brauche ich das?

- Um zu testen, ob AppArmor einen Fehler verursacht, ohne es für alles abzuschalten
- Um zu lernen, was ein Programm braucht: Complain-Modus, benutzen, dann `aa-logprof`
- Um nach dem Anpassen des Profils wieder in den Enforce-Modus zu schalten

!!! tip "Lokale Ergänzungen statt Profil bearbeiten"
    Eine Zeile wie `/srv/status/** r,` in `/etc/apparmor.d/local/usr.sbin.nginx` plus
    `sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx` erlaubt nginx das Lesen des neuen
    Verzeichnisses und übersteht Updates.

!!! warning "Der Complain-Modus schützt nichts"
    Im Complain-Modus schreibt das Profil nur Logeinträge. Schalte mit `aa-enforce` zurück,
    sobald der Test vorbei ist.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| AppArmor | aktiv | aktiv | nicht verfügbar (stattdessen SELinux) | möglich, Kernel-Parameter `lsm=` nötig |
| Paket | `sudo apt install apparmor-utils` | `apparmor-utils`, vorinstalliert | nicht verfügbar | `sudo pacman -S apparmor` |

## Verwandte Befehle

[aa-status](aa-status.md) · [setenforce](setenforce.md) · [systemctl](../09-systemd/systemctl.md)
