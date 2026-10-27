# systemctl

> Steuert systemd: startet, stoppt und startet Dienste neu, aktiviert sie beim Booten und zeigt ihren Zustand.

![systemctl output](../assets/screenshots/09-systemd/systemctl.png)

## Syntax

```bash
systemctl [OPTION]... BEFEHL [UNIT]...
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `status UNIT` | Zustand, Haupt-PID, Speicher und die letzten Logzeilen |
| `start`, `stop` | Eine Unit jetzt starten oder stoppen |
| `restart` | Stoppen und neu starten |
| `reload` | Konfiguration neu laden, ohne zu stoppen, wenn der Dienst das kann |
| `enable`, `disable` | Die Unit beim Booten starten oder nicht |
| `enable --now` | Aktivieren und starten in einem Schritt (auch `disable --now`) |
| `is-active`, `is-enabled` | Nur den Zustand ausgeben, für Skripte |
| `list-units` | Geladene Units auflisten, z. B. mit `--type=service --state=running` |
| `--failed` | Nur fehlgeschlagene Units zeigen |
| `cat UNIT` | Die Unit-Datei mit allen Overrides anzeigen |
| `edit UNIT` | Eine Override-Datei für die Unit anlegen |
| `daemon-reload` | Geänderte Unit-Dateien neu einlesen |
| `mask`, `unmask` | Eine Unit komplett sperren oder wieder freigeben |

Ändernde Befehle (`start`, `enable`, `edit`, …) brauchen `sudo`. Units und ihre Zustände
erklären die [Grundlagen](basics.md).

## Beispiele

**Den Zustand eines Dienstes anzeigen:**

```bash
systemctl status nginx
```

```text
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-10-14 07:37:21 CEST; 1 week 5 days ago
       Docs: man:nginx(8)
   Main PID: 812 (nginx)
      Tasks: 3 (limit: 4601)
     Memory: 7.8M (peak: 9.1M)
        CPU: 1.284s
     CGroup: /system.slice/nginx.service
             ├─812 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─813 "nginx: worker process"
             └─814 "nginx: worker process"

Oct 14 07:37:21 tuxdex-srv systemd[1]: Starting nginx.service - A high performance web server and a reverse proxy server...
Oct 14 07:37:21 tuxdex-srv systemd[1]: Started nginx.service - A high performance web server and a reverse proxy server.
```

| Zeile | Bedeutung |
|-------|-----------|
| `Loaded` | Pfad der Unit-Datei, `enabled` beim Booten und die Vorgabe der Distribution (`preset`) |
| `Active` | Läuft jetzt, und seit wann |
| `Main PID` | Der Hauptprozess, an den sich `kill` und `reload` wenden |
| `CGroup` | Alle Prozesse des Dienstes |

**Nach einer Änderung die Konfiguration neu laden:**

```bash
sudo nginx -t && sudo systemctl reload nginx && systemctl is-active nginx
```

```text
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
active
```

`nginx -t` prüft vorher die Konfiguration. Ist ein Fehler darin, unterbleibt das Neuladen,
und der laufende Dienst bleibt unberührt.

**Einen eigenen Timer beim Booten aktivieren und sofort starten:**

```bash
sudo systemctl enable --now backup.timer
```

```text
Created symlink '/etc/systemd/system/timers.target.wants/backup.timer' → '/etc/systemd/system/backup.timer'.
```

**Fehlgeschlagene Units finden:**

```bash
systemctl --failed
```

```text
  UNIT           LOAD   ACTIVE SUB    DESCRIPTION
● backup.service loaded failed failed Nightly backup

Legend: LOAD   → Reflects whether the unit definition was properly loaded.
        ACTIVE → The high-level unit activation state, i.e. generalization of SUB.
        SUB    → The low-level unit activation state, values depend on unit type.

1 loaded units listed.
```

Den Grund findest du mit `systemctl status backup` und [`journalctl -u backup`](journalctl.md).

**Alle laufenden Dienste auflisten:**

```bash
systemctl list-units --type=service --state=running --no-legend
```

```text
  cron.service               loaded active running Regular background program processing daemon
  nginx.service              loaded active running A high performance web server and a reverse proxy server
  php8.4-fpm.service         loaded active running The PHP 8.4 FastCGI Process Manager
  postgresql@17-main.service loaded active running PostgreSQL Cluster 17-main
  ssh.service                loaded active running OpenBSD Secure Shell server
  systemd-journald.service   loaded active running Journal Service
  systemd-logind.service     loaded active running User Login Management
  systemd-timesyncd.service  loaded active running Network Time Synchronization
```

**Im Skript prüfen, ob ein Dienst aktiviert ist:**

```bash
systemctl is-enabled nginx
```

```text
enabled
```

## Wann brauche ich das?

- Nach einer Konfigurationsänderung: den Dienst neu laden oder neu starten
- Nach der Installation eines Dienstes: ihn beim Booten aktivieren und starten
- Wenn etwas nicht funktioniert: Läuft der Dienst, ist er fehlgeschlagen, und seit wann?
- Vor Wartungsarbeiten: Dienste sauber stoppen, statt ihre Prozesse abzuschießen

!!! tip "`reload` vor `restart`"
    `reload` lässt den Dienst laufen und offene Verbindungen bestehen. Nimm `restart`
    nur, wenn der Dienst kein `reload` kennt oder eine Änderung einen echten Neustart
    braucht.

!!! tip "`status` schneidet ab"
    In einem schmalen Terminal kürzt `status` lange Zeilen. Mit `--no-pager -l` siehst du
    sie vollständig, etwa um eine Fehlermeldung zu kopieren.

!!! warning "`enable` startet nicht, `start` aktiviert nicht"
    Ein Dienst, den du nur mit `start` startest, ist nach dem nächsten Neustart wieder aus.
    Einer, den du nur mit `enable` aktivierst, läuft erst nach dem nächsten Neustart.
    `enable --now` erledigt beides.

!!! danger "`ssh` über SSH stoppen"
    `sudo systemctl stop ssh` beendet deine laufende Sitzung nicht, aber danach kann sich
    niemand mehr anmelden, auch du nicht nach einem Verbindungsabbruch. Nimm `restart`
    und halte beim Testen eine zweite Sitzung offen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Dienst startet und wird aktiviert, wenn sein Paket installiert wird | ja | ja | nein | nein |
| Dienst des SSH-Servers | `ssh` | `ssh` | `sshd` | `sshd` |
| Dienst des Apache-Webservers | `apache2` | `apache2` | `httpd` | `httpd` |

## Verwandte Befehle

[kill](../08-processes/kill.md) · [ps](../08-processes/ps.md) · [journalctl](journalctl.md)
