# Zeitsteuerung verstehen

Linux hat zwei Systeme für wiederkehrende Jobs: das klassische **cron** und
**systemd-Timer**. Für einen Job, der nur einmal läuft, gibt es **at**.

## Die cron-Syntax

Jede cron-Zeile hat fünf Zeitfelder, gefolgt vom Befehl:

```text
┌───────────── Minute        0-59
│ ┌─────────── Stunde        0-23
│ │ ┌───────── Tag im Monat  1-31
│ │ │ ┌─────── Monat         1-12
│ │ │ │ ┌───── Wochentag     0-7 (0 und 7 sind Sonntag)
│ │ │ │ │
* * * * * befehl
```

| Ausdruck | Bedeutung |
|----------|-----------|
| `*/5 * * * *` | Alle 5 Minuten |
| `0 * * * *` | Zu jeder vollen Stunde |
| `30 3 * * *` | Jeden Tag um 03:30 |
| `0 3 * * 1-5` | Montag bis Freitag um 03:00 |
| `0 22 * * 0` | Jeden Sonntag um 22:00 |
| `0 4 1 * *` | Am Ersten jedes Monats um 04:00 |
| `@reboot` | Einmal nach jedem Booten |

[crontab.guru](https://crontab.guru) erklärt jeden Ausdruck in Klartext (auf Englisch).

## Wo Cronjobs liegen

| Ort | Für | Format |
|-----|-----|--------|
| `crontab -e` | Jobs eines einzelnen Benutzers | Fünf Zeitfelder und Befehl |
| `/etc/crontab` | Systemjobs | Fünf Zeitfelder, **Benutzer**, Befehl |
| `/etc/cron.d/` | Systemjobs von Paketen und Admins, eine Datei pro Job | wie `/etc/crontab` |
| `/etc/cron.hourly/`, `daily/`, `weekly/`, `monthly/` | Skripte, die einfach einmal pro Zeitraum laufen | Ausführbare Skripte, keine Zeitfelder |

Eine Beispieldatei `/etc/cron.d/backup`:

```text
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MAILTO=admin@example.com

30 3 * * * root /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```

## systemd-Timer

Ein Timer besteht aus zwei Units: einem `.service`, der die Arbeit macht, und einem
`.timer`, der sagt, wann. `/etc/systemd/system/backup.timer`:

```text
[Unit]
Description=Nightly backup

[Timer]
OnCalendar=*-*-* 03:30:00
Persistent=true
RandomizedDelaySec=10min

[Install]
WantedBy=timers.target
```

Zusammen mit dem `backup.service` aus den Grundlagen des Kapitels
[systemd](../09-systemd/basics.md) aktiviert `sudo systemctl enable --now backup.timer` ihn,
und `systemctl list-timers` zeigt den nächsten Lauf.

## cron oder systemd-Timer?

| | cron | systemd-Timer |
|---|------|---------------|
| Einrichten | Eine Zeile | Zwei Unit-Dateien |
| Ausgabe und Fehler | Per Mail oder verloren | Im Journal: `journalctl -u backup` |
| Verpasste Läufe (Server war aus) | Nur mit anacron | `Persistent=true` |
| Ressourcengrenzen, Abhängigkeiten | Nein | Wie bei jedem systemd-Dienst |
| Einen Job zum Testen sofort ausführen | Den Befehl von Hand starten | `systemctl start backup.service` |

Für neue Jobs auf Servern sind Timer die bessere Wahl. cron ist einfacher und weiterhin
überall vorhanden.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| cron installiert | ja, Paket `cron` | ja, Paket `cron` | ja, Paket `cronie` | nein, Paket `cronie` |
| Dienst | `cron` | `cron` | `crond` | `cronie` |
| `at` installiert | nein, Paket `at` | nein, Paket `at` | nein, Paket `at` | nein, Paket `at` |
| Tägliche Jobs ausgeführt von | cron, anacron falls installiert | cron, anacron falls installiert | anacron (`cronie-anacron`) | anacron (Teil von `cronie`) |

!!! tip "Absolute Pfade und eine vollständige Umgebung"
    cron führt Jobs mit einer minimalen Umgebung aus: kurzer `PATH`, keine Aliase, keine
    Variablen aus deiner Login-Shell. Nutze in Cronjobs absolute Pfade oder setze `PATH`
    oben in der Crontab.

!!! warning "Die Ausgabe landet irgendwo"
    Ohne Umleitung schickt cron die Ausgabe eines Jobs per Mail an den Benutzer. Ohne
    Mailsystem geht sie verloren. Leite sie in eine Logdatei um oder schick sie mit `logger`
    oder `systemd-cat` ins Journal.
