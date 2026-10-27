# lnav

> Der Log-Datei-Navigator: führt mehrere Logdateien zu einer Zeitleiste zusammen, hebt Fehler hervor, filtert und beantwortet sogar SQL-Abfragen über Logs.

![lnav output](../assets/screenshots/15-logs/lnav.png)

## Syntax

```bash
lnav [OPTION]... [DATEI | VERZEICHNIS]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `DATEI...`, `VERZEICHNIS` | Diese Logs öffnen, auch komprimierte `.gz`-Dateien |
| `-r` | Verzeichnisse rekursiv öffnen |
| `-t` | Zeilen von der Standardeingabe mit Zeitstempel versehen |
| `-n` | Ohne Oberfläche, z. B. mit `-c` für Skripte |
| `-c BEFEHL` | Einen Befehl ausführen, etwa einen Filter oder eine SQL-Abfrage |

Tasten in `lnav`: ++e++ / ++shift+e++ nächster und vorheriger Fehler, ++w++ nächste Warnung, ++slash++ suchen, `:filter-in MUSTER` nur passende Zeilen zeigen, `;` SQL-Abfrage, ++q++ beenden.

## Beispiele

**Mehrere Logs in einer Zeitleiste öffnen:**

```bash
journalctl -o short-iso --since today > /tmp/today.log
sudo lnav /var/log/nginx/ /tmp/today.log
```

```text
2026-10-26T10:31:02 tuxcodex-srv sshd-session[3301]: Failed password for invalid user admin from 198.51.100.66
2026-10-26T10:31:05 tuxcodex-srv sshd-session[3301]: Failed password for invalid user admin from 198.51.100.66
2026-10-26T10:41:58 198.51.100.23 - - "GET /shop/cart HTTP/2.0" 200 4812 "-" "Mozilla/5.0"
2026-10-26T10:42:03 198.51.100.23 - - "POST /shop/checkout HTTP/2.0" 502 166 "-" "Mozilla/5.0"
2026/10/26 10:42:03 [error] 813#813: *4412 connect() to unix:/run/php/php8.4-fpm.sock failed (11: Resource temporarily unavailable)
2026-10-26T10:42:17 tuxcodex-srv backup[4421]: Backup of /srv/www finished, 48 MiB
 L1,284 100%                                   ?:View Help
 Files :: Text Filters ::                                            Press TAB to edit
```

Der Checkout scheitert mit `502`, weil PHP-FPM keine weiteren Verbindungen annimmt. Beide
Zeilen stehen nebeneinander, obwohl sie aus zwei Dateien stammen.

**In lnav: mit `:filter-in` nur passende Zeilen zeigen:**

```bash
:filter-in " 502 "
```

```text
2026-10-26T10:42:03 198.51.100.23 - - "POST /shop/checkout HTTP/2.0" 502 166 "-" "Mozilla/5.0"
2026-10-26T10:42:09 192.0.2.45 - - "POST /shop/checkout HTTP/2.0" 502 166 "-" "Mozilla/5.0"
 L41 100%                                      ?:View Help
 Files :: Text Filters ::                                            Press TAB to edit
```

**In lnav: Serverfehler pro Client mit SQL zählen:**

```bash
;SELECT c_ip, count(*) AS hits FROM access_log WHERE sc_status >= 500 GROUP BY c_ip ORDER BY hits DESC
```

```text
 c_ip           hits
198.51.100.23     14
192.0.2.45         3
```

## Wann brauche ich das?

- Wenn ein Problem mehrere Dienste betrifft und du ihre Logs in einer Zeitleiste sehen willst
- Um schnell durch Fehler und Warnungen zu springen
- Um Webserver-Logs mit SQL auszuwerten, ohne sie vorher zu exportieren

!!! tip "Ein ganzes Verzeichnis öffnen"
    `lnav /var/log/nginx` öffnet alle Dateien, auch rotierte und komprimierte, und sortiert sie
    nach Zeit.

!!! tip "Auch das Journal"
    `journalctl -o short-iso -f | lnav` zeigt das Journal in lnav, mit Hervorhebung und
    Fehlersprüngen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `lnav` | `lnav` | aus EPEL | `lnav` |

## Verwandte Befehle

[less](../04-viewing-files/less.md) · [goaccess](goaccess.md) · [journalctl](../09-systemd/journalctl.md)
