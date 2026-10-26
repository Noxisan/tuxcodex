# unattended-upgrade

> Installiert unter Debian und Ubuntu Sicherheitsupdates automatisch, jeden Tag, ohne dass sich jemand anmelden muss.

![unattended-upgrade output](../assets/screenshots/10-packages/unattended-upgrade.png)

## Syntax

```bash
unattended-upgrade [OPTION]...
```

Normalerweise startest du es nicht von Hand: Der systemd-Timer `apt-daily-upgrade.timer`
ruft es einmal am Tag auf. Das Paket heißt `unattended-upgrades`.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--dry-run` | Nur anzeigen, was aktualisiert würde |
| `-v`, `--verbose` | Mehr Details anzeigen |
| `-d`, `--debug` | Alles anzeigen, zur Fehlersuche |

Wichtige Dateien:

| Datei | Zweck |
|-------|-------|
| `/etc/apt/apt.conf.d/20auto-upgrades` | Schaltet das tägliche Update ein oder aus |
| `/etc/apt/apt.conf.d/50unattended-upgrades` | Welche Quellen erlaubt sind, automatischer Neustart, Mail |
| `/var/log/unattended-upgrades/` | Protokoll jedes Laufs |

## Beispiele

**Testen, was aktualisiert würde:**

```bash
sudo unattended-upgrade --dry-run --verbose
```

```text
Starting unattended upgrades script
Allowed origins are: origin=Debian,codename=trixie,label=Debian, origin=Debian,codename=trixie,label=Debian-Security, origin=Debian,codename=trixie-security,label=Debian-Security
Initial blacklist:
Initial whitelist (not strict):
Option --dry-run given, *not* performing real actions
Packages that will be upgraded: nginx nginx-common
Writing dpkg log to /var/log/unattended-upgrades/unattended-upgrades-dpkg.log
All upgrades installed
```

Trotz `All upgrades installed` wurde nichts geändert: `--dry-run` simuliert nur.

**Prüfen, ob automatische Updates eingeschaltet sind:**

```bash
cat /etc/apt/apt.conf.d/20auto-upgrades
```

```text
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
```

`"1"` heißt: jeden Tag. Fehlt die Datei oder steht dort `"0"`, wird nichts automatisch
aktualisiert.

**Herausfinden, wann es läuft:**

```bash
systemctl list-timers "apt-daily*"
```

```text
NEXT                        LEFT LAST                        PASSED       UNIT                    ACTIVATES
Mon 2026-10-26 18:07:44 CET   7h Mon 2026-10-26 07:12:30 CET 3h 29min ago apt-daily.timer         apt-daily.service
Tue 2026-10-27 06:31:07 CET  19h Mon 2026-10-26 06:24:09 CET 4h 18min ago apt-daily-upgrade.timer apt-daily-upgrade.service
```

`apt-daily` lädt die Paketlisten, `apt-daily-upgrade` installiert die Updates.

**Nachsehen, was letzte Nacht installiert wurde:**

```bash
tail -n 4 /var/log/unattended-upgrades/unattended-upgrades.log
```

```text
2026-10-26 06:24:09,942 INFO Initial whitelist (not strict):
2026-10-26 06:24:11,226 INFO Packages that will be upgraded: nginx nginx-common
2026-10-26 06:24:11,226 INFO Writing dpkg log to /var/log/unattended-upgrades/unattended-upgrades-dpkg.log
2026-10-26 06:24:13,324 INFO All upgrades installed
```

## Wann brauche ich das?

- Auf jedem Debian- oder Ubuntu-Server, der aus dem Internet erreichbar ist
- Damit Sicherheitsupdates innerhalb eines Tages ankommen, auch im Urlaub
- Nach einem Update-Problem: Das Protokoll zeigt, was wann installiert wurde

!!! tip "Einschalten"
    `sudo apt install unattended-upgrades`, dann
    `sudo dpkg-reconfigure -plow unattended-upgrades` und mit `Yes` antworten. Das legt
    `20auto-upgrades` mit den richtigen Werten an.

!!! tip "Automatisch neu starten"
    Kernel-Updates wirken erst nach einem Neustart. In `50unattended-upgrades` starten
    `Unattended-Upgrade::Automatic-Reboot "true";` und
    `Unattended-Upgrade::Automatic-Reboot-Time "04:00";` den Server bei Bedarf nachts
    neu.

!!! warning "Dienste behalten die alte Version"
    Ein laufender Dienst nutzt die alte Bibliothek weiter, bis er neu gestartet wird.
    Prüfe mit [`needrestart`](needrestart.md), welche Dienste nach einem Update einen
    Neustart brauchen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Automatische Sicherheitsupdates | `unattended-upgrades`, auf minimalen Systemen oft nicht installiert | `unattended-upgrades`, installiert und aktiv | `dnf-automatic` mit `dnf-automatic.timer` | nicht vorgesehen, von Hand mit `pacman -Syu` aktualisieren |

## Verwandte Befehle

[apt](apt.md) · [apt-mark](apt-mark.md) · [systemctl](../09-systemd/systemctl.md) · [journalctl](../09-systemd/journalctl.md) · [needrestart](needrestart.md)
