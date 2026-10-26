# apt-mark

> Setzt unter Debian und Ubuntu Markierungen an Paketen: ein Paket auf seiner aktuellen Version festhalten oder es als manuell oder automatisch installiert markieren.

![apt-mark output](../assets/screenshots/10-packages/apt-mark.png)

## Syntax

```bash
apt-mark BEFEHL [PAKET]...
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `hold PAKET` | Das Paket festhalten: Es wird nicht mehr aktualisiert |
| `unhold PAKET` | Updates wieder erlauben |
| `showhold` | Alle festgehaltenen Pakete auflisten |
| `manual PAKET` | Als manuell installiert markieren: `autoremove` entfernt es nie |
| `auto PAKET` | Als automatisch installiert markieren: `autoremove` entfernt es, wenn nichts es braucht |
| `showmanual` | Alle manuell installierten Pakete auflisten |

## Beispiele

**Ein Paket auf seiner aktuellen Version festhalten:**

```bash
sudo apt-mark hold nginx
```

```text
nginx set on hold.
```

Ab jetzt führt `apt upgrade` `nginx` unter `Not Upgrading` auf und lässt es in Ruhe.

**Alle festgehaltenen Pakete anzeigen:**

```bash
apt-mark showhold
```

```text
nginx
```

**Updates wieder erlauben:**

```bash
sudo apt-mark unhold nginx
```

```text
Canceled hold on nginx.
```

**Ein Paket vor `autoremove` schützen:**

```bash
sudo apt-mark manual libncursesw6
```

```text
libncursesw6 set to manually installed.
```

**Ein Paket später von `autoremove` aufräumen lassen:**

```bash
sudo apt-mark auto htop
```

```text
htop set to automatically installed.
```

Braucht kein manuell installiertes Paket `htop`, entfernt das nächste `apt autoremove` es.

## Wann brauche ich das?

- Wenn ein Update eines Pakets etwas kaputt machen würde, bis du es getestet hast
- Um einen Kernel, eine Datenbank oder PHP auf einer Version zu halten, die deine
  Anwendung braucht
- Zum Aufräumen nach Tests: Testpakete als `auto` markieren, dann `apt autoremove`

!!! tip "Herausfinden, was du installiert hast"
    `apt-mark showmanual` listet alles auf, was gezielt installiert wurde. Das ist eine
    gute Grundlage, um einen Server zu dokumentieren oder einen zweiten gleich
    aufzusetzen.

!!! warning "Festgehaltene Pakete bekommen keine Sicherheitsupdates"
    Ein Paket auf `hold` bleibt auf seiner Version, samt aller Sicherheitslücken. Nutze
    `hold` nur vorübergehend und prüfe regelmäßig `apt-mark showhold`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Ein Paket festhalten | `apt-mark hold` | `apt-mark hold` | `dnf versionlock add` (Plugin) | `IgnorePkg` in `/etc/pacman.conf` |
| Als ausdrücklich installiert markieren | `apt-mark manual` | `apt-mark manual` | `dnf mark install` | `pacman -D --asexplicit` |

## Verwandte Befehle

[apt](apt.md) · [apt-cache](apt-cache.md) · [dpkg](dpkg.md)
