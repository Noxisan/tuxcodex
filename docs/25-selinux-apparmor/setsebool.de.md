# setsebool

> Unter RHEL, Rocky und Alma: schaltet SELinux-Booleans, fertige Ausnahmen für häufige Bedürfnisse.

![setsebool output](../assets/screenshots/25-selinux-apparmor/setsebool.png)

## Syntax

```bash
setsebool [-P] BOOLEAN on|off
getsebool -a | BOOLEAN
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-P` | Dauerhaft, auch nach einem Neustart (ohne nur bis zum nächsten Neustart) |
| `on`, `off` | Ein- oder ausschalten (auch `1`, `0`) |
| `getsebool -a` | Alle Booleans mit ihrem Zustand auflisten |
| `getsebool BOOLEAN` | Zustand eines einzelnen Booleans |

Häufige Booleans für Server:

| Boolean | Erlaubt |
|---------|---------|
| `httpd_can_network_connect` | Webserver verbindet sich mit anderen Servern, etwa als Reverse Proxy |
| `httpd_can_network_connect_db` | Webserver verbindet sich mit einer Datenbank im Netz |
| `httpd_can_sendmail` | Webanwendungen verschicken Mails |
| `httpd_enable_homedirs` | Webserver liefert `~/public_html` aus |
| `samba_enable_home_dirs` | Samba gibt Home-Verzeichnisse frei |

## Beispiele

**nginx als Reverse Proxy arbeiten lassen:**

```bash
sudo setsebool -P httpd_can_network_connect on
getsebool httpd_can_network_connect
```

```text
httpd_can_network_connect --> on
```

**Alle eingeschalteten Booleans für den Webserver:**

```bash
getsebool -a | grep '^httpd' | grep 'on$'
```

```text
httpd_builtin_scripting --> on
httpd_can_network_connect --> on
httpd_enable_cgi --> on
httpd_graceful_shutdown --> on
```

**Booleans mit Beschreibung und Standardwert:**

```bash
sudo semanage boolean -l | grep -E '^httpd_can_network_connect |^httpd_enable_homedirs'
```

```text
httpd_can_network_connect      (on   ,  off)  Allow httpd to can network connect
httpd_enable_homedirs          (off  ,  off)  Allow httpd to enable homedirs
```

Der erste Wert ist der aktuelle Zustand, der zweite der Standard der Richtlinie.

## Wann brauche ich das?

- Wenn nginx als Reverse Proxy `502 Bad Gateway` liefert und das Log `Permission denied` beim Verbinden zeigt
- Wenn eine Webanwendung die Datenbank nicht erreicht oder keine Mails verschicken kann
- Immer dann, wenn `audit2why` ein Boolean als Lösung nennt

!!! tip "Das richtige Boolean finden"
    `semanage boolean -l | grep httpd` listet alle Booleans für Webserver mit Beschreibung.
    `audit2why` nennt oft genau das richtige.

!!! warning "Ohne -P ist es nach dem Neustart weg"
    `setsebool` ohne `-P` ändert nur den laufenden Zustand. Der Dienst funktioniert, und nach
    dem nächsten Neustart scheitert er wieder.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| SELinux | nicht aktiv (stattdessen AppArmor) | nicht aktiv (stattdessen AppArmor) | aktiv, `enforcing` | nicht aktiv |
| Paket | `selinux-utils` (nur wenn SELinux eingerichtet ist) | `selinux-utils` (nur wenn SELinux eingerichtet ist) | `libselinux-utils`, vorinstalliert | nicht in den offiziellen Repositorys |

## Verwandte Befehle

[semanage](semanage.md) · [audit2allow](audit2allow.md) · [sestatus](sestatus.md)
