# nikto

> Prüft einen Webserver auf bekannte Probleme: fehlende Sicherheits-Header, gefährliche Dateien, veraltete Software.

![nikto output](../assets/screenshots/23-security-scanning/nikto.png)

## Syntax

```bash
nikto -h URL [OPTIONEN]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-h URL` | Ziel, etwa `http://web01` oder `https://status.example.com` |
| `-p PORT` | Port, falls nicht in der URL |
| `-ssl` | HTTPS erzwingen |
| `-Tuning X` | Nur bestimmte Testgruppen, etwa `1` (interessante Dateien) oder `x` zum Ausschließen |
| `-o DATEI -Format htm` | Den Bericht speichern, auch als `csv`, `txt` oder `xml` |
| `-useragent TEXT` | Ein anderer User-Agent |

## Beispiele

**Einen Webserver prüfen:**

```bash
nikto -h http://web01
```

```text
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          192.0.2.21
+ Target Hostname:    web01
+ Target Port:        80
+ Start Time:         2026-10-26 10:42:17 (GMT1)
---------------------------------------------------------------------------
+ Server: nginx
+ Server leaks inodes via ETags, header found with file /, fields: 0x6ae09481 0x267
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 6544 items checked: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2026-10-26 10:42:20 (GMT1) (3 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

**Den Bericht als HTML speichern:**

```bash
nikto -h https://status.example.com -o nikto-status.html -Format htm | tail -3
```

```text
+ 6544 items checked: 0 error(s) and 1 item(s) reported on remote host
+ End Time:           2026-10-26 10:44:51 (GMT1) (6 seconds)
---------------------------------------------------------------------------
```

**Nach dem Ergänzen des Headers in nginx:**

```bash
grep add_header /etc/nginx/conf.d/status.conf
nikto -h http://web01 | grep -c X-Frame-Options
```

```text
    add_header X-Frame-Options "SAMEORIGIN" always;
0
```

## Wann brauche ich das?

- Nach dem Einrichten eines Webservers, um vergessene Standards und fehlende Header zu finden
- Bevor eine neue Webanwendung online geht
- Um zu prüfen, dass Backup-Dateien oder Admin-Seiten von außen nicht erreichbar sind

!!! tip "Fehlende Header sind schnell ergänzt"
    Header wie `X-Frame-Options` und `Content-Security-Policy` ergänzt du in der
    nginx-Konfiguration mit `add_header`. Starte nikto danach noch einmal zur Kontrolle.

!!! warning "Laut und sichtbar"
    nikto schickt Tausende Anfragen und versucht nicht, sich zu verstecken. Das füllt das
    Zugriffslog und löst Einbruchserkennung und fail2ban aus. Nutze es nur gegen eigene
    Server.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install nikto` (Repository-Bereich `non-free`) | `sudo apt install nikto` (multiverse) | von GitHub (`sullo/nikto`) | `sudo pacman -S nikto` |
| Version | alt, 2.1.5 | alt, 2.1.5 | aktuell aus Git | aktuell |

## Verwandte Befehle

[nmap](nmap.md) · [curl](../11-network/curl.md) · [fail2ban-client](../12-ssh/fail2ban-client.md)
