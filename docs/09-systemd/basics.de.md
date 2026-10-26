# systemd verstehen

systemd ist der erste Prozess unter Debian, Ubuntu, RHEL und Arch: Er läuft mit PID 1,
startet beim Booten alle Dienste, startet sie neu, wenn sie abstürzen, sammelt ihre Logs
und fährt das System sauber herunter. Alles, was systemd verwaltet, heißt **Unit**.

## Unit-Typen

Der Typ ist die Endung des Unit-Namens:

| Typ | Beispiel | Was es ist |
|-----|----------|------------|
| `.service` | `nginx.service` | Ein Dienst oder ein einmaliger Job |
| `.timer` | `logrotate.timer` | Startet einen Dienst zu festen Zeiten, wie ein Cronjob |
| `.socket` | `ssh.socket` | Startet einen Dienst, sobald eine Verbindung ankommt |
| `.target` | `multi-user.target` | Eine Gruppe von Units, ähnlich wie ein Runlevel |
| `.mount` | `srv-data.mount` | Ein eingehängtes Dateisystem |
| `.path` | `systemd-ask-password-wall.path` | Startet einen Dienst, wenn sich eine Datei ändert |

Lässt du die Endung weg, nimmt `systemctl` `.service` an: `systemctl status nginx`
bedeutet `nginx.service`.

## Wo Unit-Dateien liegen

| Verzeichnis | Inhalt |
|-------------|--------|
| `/usr/lib/systemd/system/` | Unit-Dateien aus Paketen. Nicht bearbeiten, Updates überschreiben sie |
| `/etc/systemd/system/` | Eigene Units und Änderungen. Sie haben Vorrang |
| `/run/systemd/system/` | Zur Laufzeit erzeugte Units, nach einem Neustart weg |

!!! tip "Units mit `systemctl edit` ändern"
    `sudo systemctl edit nginx` legt eine Override-Datei in
    `/etc/systemd/system/nginx.service.d/` an. Sie enthält nur deine Änderungen und
    übersteht Paketupdates. `sudo systemctl edit --full nginx` kopiert stattdessen die
    ganze Datei.

## Zustände

Eine Unit hat zwei unabhängige Zustände: ob sie **jetzt** läuft und ob sie **beim Booten**
startet.

| Läuft jetzt | Bedeutung |
|-------------|-----------|
| `active (running)` | Läuft, mit mindestens einem Prozess |
| `active (exited)` | Ist einmal erfolgreich gelaufen und hat keinen Prozess mehr, z. B. ein Firewall-Setup |
| `inactive (dead)` | Läuft nicht |
| `failed` | Mit Fehler beendet, abgestürzt oder abgeschossen |

| Beim Booten | Bedeutung |
|-------------|-----------|
| `enabled` | Startet beim Booten |
| `disabled` | Startet nicht beim Booten, lässt sich aber von Hand starten |
| `static` | Lässt sich nicht aktivieren, wird nur von anderen Units gestartet |
| `masked` | Komplett gesperrt, lässt sich überhaupt nicht starten |

`start` ändert den ersten Zustand, `enable` den zweiten. Ein Dienst, den du nur startest,
ist nach dem nächsten Neustart wieder aus.

## Eine einfache Unit-Datei

`/etc/systemd/system/backup.service`:

```ini
[Unit]
Description=Nightly backup
After=network-online.target

[Service]
Type=oneshot
User=nox
ExecStart=/usr/local/bin/backup.sh

[Install]
WantedBy=multi-user.target
```

| Abschnitt | Zweck |
|-----------|-------|
| `[Unit]` | Beschreibung und Reihenfolge: nach dem Netzwerk starten |
| `[Service]` | Was ausgeführt wird, als welcher Benutzer und wie (`oneshot`: läuft einmal und endet) |
| `[Install]` | Wo `enable` die Unit einhängt: `multi-user.target` ist der normale Bootvorgang |

Nach dem Anlegen oder Ändern einer Unit-Datei führst du `sudo systemctl daemon-reload` aus.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Dienst startet und wird aktiviert, wenn sein Paket installiert wird | ja | ja | nein | nein |
| Typischer nächster Schritt nach der Installation | keiner | keiner | `sudo systemctl enable --now nginx` | `sudo systemctl enable --now nginx` |
