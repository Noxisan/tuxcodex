# Logs verstehen

Logs sind das Gedächtnis eines Servers: was Dienste getan haben, welche Fehler auftraten,
wer sich angemeldet hat. Linux hat dafür zwei Orte: das **systemd-Journal** und klassische
Textdateien in **`/var/log`**.

## Journal oder Textdatei?

| Quelle | Wo | Lesen mit |
|--------|----|-----------|
| systemd-Journal | Binärdateien in `/var/log/journal/` | [`journalctl`](../09-systemd/journalctl.md) |
| rsyslog | Textdateien wie `/var/log/syslog` oder `/var/log/messages` | `less`, `tail`, `grep` |
| Anwendungen | Eigene Dateien, z. B. `/var/log/nginx/`, `/var/log/postgresql/` | `less`, `tail`, `grep` |

Fast alle Systemdienste schreiben ins Journal. Ob rsyslog zusätzlich Textdateien schreibt,
hängt von der Distribution ab:

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| rsyslog installiert | nein | ja | ja | nein |
| Allgemeines Systemlog | nur Journal | `/var/log/syslog` | `/var/log/messages` | nur Journal |
| Anmeldungen und `sudo` | nur Journal | `/var/log/auth.log` | `/var/log/secure` | nur Journal |
| Paketmanager | `/var/log/apt/history.log`, `/var/log/dpkg.log` | `/var/log/apt/history.log`, `/var/log/dpkg.log` | `/var/log/dnf.log` | `/var/log/pacman.log` |
| Kernel | Journal, `dmesg` | `/var/log/kern.log`, `dmesg` | Journal, `dmesg` | Journal, `dmesg` |

## Log-Level

Jede Meldung hat eine Priorität. `journalctl -p` und viele Werkzeuge filtern danach:

| Level | Name | Bedeutung |
|-------|------|-----------|
| 0 | `emerg` | Das System ist unbenutzbar |
| 1 | `alert` | Es muss sofort gehandelt werden |
| 2 | `crit` | Kritischer Zustand, z. B. Hardwareausfall |
| 3 | `err` | Fehler |
| 4 | `warning` | Warnung |
| 5 | `notice` | Normal, aber bemerkenswert |
| 6 | `info` | Information |
| 7 | `debug` | Debug-Meldungen |

`journalctl -p warning` zeigt die Level 0 bis 4, also alles ab Warnungen aufwärts.

## Logrotation

Logdateien wachsen endlos. **logrotate** läuft einmal am Tag und benennt nach seinen Regeln
in `/etc/logrotate.d/` die aktuelle Datei um (`access.log` wird zu `access.log.1`),
komprimiert ältere (`access.log.2.gz`) und löscht die ältesten. Das Journal begrenzt seine
Größe selbst, siehe `SystemMaxUse=` in `/etc/systemd/journald.conf`.

## Fehlgeschlagene Anmeldungen

Ohne `/var/log/auth.log` und ohne `lastb` (unter Debian 13 nicht mehr verfügbar) zeigt das
Journal fehlgeschlagene SSH-Anmeldungen:

```text
$ journalctl -u ssh --since today | grep "Failed password"
Oct 26 09:58:02 tuxcodex-srv sshd-session[2187]: Failed password for nox from 192.0.2.45 port 51720 ssh2
Oct 26 10:31:02 tuxcodex-srv sshd-session[3301]: Failed password for invalid user admin from 198.51.100.66 port 40218 ssh2
Oct 26 10:31:05 tuxcodex-srv sshd-session[3301]: Failed password for invalid user admin from 198.51.100.66 port 40218 ssh2
```

`invalid user` heißt: Das Konto gibt es nicht, typisch für automatische Angriffe. Werkzeuge
wie [`fail2ban-client`](../12-ssh/fail2ban-client.md) und [`faillock`](faillock.md)
reagieren auf solche Versuche.

!!! tip "Zuerst die Uhrzeit"
    Ist etwas schiefgegangen, notiere die Uhrzeit und schau dir alle Logs rund um diesen
    Zeitpunkt an: `journalctl --since "10:25" --until "10:35"` zeigt jeden Dienst in diesem
    Zeitfenster.

!!! warning "Logs enthalten personenbezogene Daten"
    IP-Adressen, Benutzernamen und URLs in Logs sind personenbezogene Daten. Bewahre sie nur
    so lange auf, wie du sie brauchst, und schütze den Zugriff: Unter Debian und Ubuntu darf
    nur die Gruppe `adm` den größten Teil von `/var/log` lesen.
