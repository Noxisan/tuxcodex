# semanage

> Unter RHEL, Rocky und Alma: ändert die SELinux-Konfiguration dauerhaft: Datei-Labels, erlaubte Ports, Booleans und Permissive-Domänen.

![semanage output](../assets/screenshots/25-selinux-apparmor/semanage.png)

## Syntax

```bash
semanage fcontext | port | boolean | permissive  -l | -a | -d | -m [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `fcontext -a -t TYP 'PFAD(/.*)?'` | Regel, welches Label Dateien unterhalb eines Pfades bekommen |
| `fcontext -l [-C]` | Die Regeln auflisten; `-C` nur die eigenen |
| `port -a -t TYP -p tcp PORT` | Einem Diensttyp einen weiteren Port erlauben |
| `port -l` | Auflisten, welche Ports zu welchem Typ gehören |
| `boolean -l` | Booleans mit Zustand und Beschreibung |
| `permissive -a DOMÄNE` | Eine einzelne Domäne auf permissive setzen |
| `-d` | Eine eigene Regel wieder löschen |

`semanage fcontext` ändert nur die Regeln. Ihr neues Label bekommen die Dateien erst, wenn du [`restorecon`](restorecon.md) ausführst.

## Beispiele

**nginx ein neues Verzeichnis ausliefern lassen:**

```bash
sudo semanage fcontext -a -t httpd_sys_content_t '/srv/status(/.*)?'
sudo semanage fcontext -l -C
```

```text
SELinux fcontext                                   type               Context

/srv/status(/.*)?                                  all files          system_u:object_r:httpd_sys_content_t:s0
```

Danach wendest du die Regel mit `sudo restorecon -Rv /srv/status` auf die vorhandenen Dateien an.

**Die Ports zeigen, die der Webserver nutzen darf:**

```bash
sudo semanage port -l | grep -E '^http_port_t'
```

```text
http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
http_port_t                    udp      80, 443
```

**Einen zusätzlichen Port erlauben:**

```bash
sudo semanage port -a -t http_port_t -p tcp 8090
sudo semanage port -l -C
```

```text
SELinux Port Type              Proto    Port Number

http_port_t                    tcp      8090
```

**Der Port gehört schon zu einem anderen Typ:**

```bash
sudo semanage port -a -t http_port_t -p tcp 8081
```

```text
Port tcp/8081 already defined, modifying instead
```

Port 8081 ist als `transproxy_port_t` definiert; semanage ordnet ihn um, statt ihn hinzuzufügen.

## Wann brauche ich das?

- Wenn ein Dienst Dateien aus einem ungewöhnlichen Verzeichnis ausliefert, etwa `/srv/status`
- Wenn ein Dienst auf einem Port lauschen soll, der nicht sein Standard ist
- Um zu sehen, welche eigenen SELinux-Änderungen auf einem Server gemacht wurden (`-l -C`)

!!! tip "Erst die bestehenden Regeln ansehen"
    `semanage fcontext -l | grep /var/www` zeigt, wie die Standardverzeichnisse gelabelt
    sind. Übernimm den Typ von dort für dein eigenes Verzeichnis.

!!! warning "chcon hält nicht"
    `chcon -t httpd_sys_content_t DATEI` ändert ein Label direkt, aber das nächste Relabel
    oder `restorecon` setzt es zurück. Für dauerhafte Änderungen immer
    `semanage fcontext` nehmen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| SELinux | nicht aktiv (stattdessen AppArmor) | nicht aktiv (stattdessen AppArmor) | aktiv, `enforcing` | nicht aktiv |
| Paket | `policycoreutils-python-utils` (nur wenn SELinux eingerichtet ist) | `policycoreutils-python-utils` (nur wenn SELinux eingerichtet ist) | `sudo dnf install policycoreutils-python-utils` | nicht in den offiziellen Repositorys |

## Verwandte Befehle

[restorecon](restorecon.md) · [setsebool](setsebool.md) · [audit2allow](audit2allow.md) · [ls](../02-navigation/ls.md)
