# clamscan

> Durchsucht Dateien und Verzeichnisse mit dem Open-Source-Scanner ClamAV nach Viren und Schadsoftware.

![clamscan output](../assets/screenshots/23-security-scanning/clamscan.png)

## Syntax

```bash
clamscan [OPTIONEN] DATEI|VERZEICHNIS...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-r`, `--recursive` | Auch Unterverzeichnisse durchsuchen |
| `-i`, `--infected` | Nur infizierte Dateien auflisten |
| `--move=VERZEICHNIS` | Infizierte Dateien in ein Quarantäne-Verzeichnis verschieben |
| `--remove` | Infizierte Dateien löschen (vorsichtig) |
| `--exclude-dir=MUSTER` | Verzeichnisse überspringen |
| `-l DATEI` | Ein Log schreiben |

Die Signaturen aktualisiert `freshclam`, unter Debian und Ubuntu automatisch der Dienst `clamav-freshclam`. Für viele Scans ist der Daemon `clamd` mit `clamdscan` deutlich schneller.

## Beispiele

**Ein Upload-Verzeichnis durchsuchen:**

```bash
clamscan -r -i /srv/upload
```

```text
/srv/upload/invoice.pdf.exe: Eicar-Test-Signature FOUND

----------- SCAN SUMMARY -----------
Known viruses: 3628193
Engine version: 1.4.3
Scanned directories: 1
Scanned files: 2
Infected files: 1
Data scanned: 0.00 MB
Data read: 0.00 MB (ratio 0.00:1)
Time: 5.906 sec (0 m 5 s)
Start Date: 2026:10:26 10:42:17
End Date:   2026:10:26 10:42:23
```

Hier ist es die EICAR-Testdatei. Mit `-i` werden saubere Dateien nicht aufgelistet.

**Funde in die Quarantäne verschieben:**

```bash
sudo mkdir -p /var/quarantine
clamscan -r -i --move=/var/quarantine /srv/upload | head -2
```

```text
/srv/upload/invoice.pdf.exe: Eicar-Test-Signature FOUND
/srv/upload/invoice.pdf.exe: moved to '/var/quarantine/invoice.pdf.exe'
```

**Die Aktualisierung der Signaturen prüfen:**

```bash
systemctl is-active clamav-freshclam
sudo tail -2 /var/log/clamav/freshclam.log
```

```text
active
Mon Oct 26 10:12:01 2026 -> daily.cld database is up-to-date (version: 27801, sigs: 2074391, f-level: 90, builder: svc.clamav-publisher)
Mon Oct 26 10:12:01 2026 -> main.cvd database is up-to-date (version: 63, sigs: 3287027, f-level: 90, builder: tomjudge)
```

## Wann brauche ich das?

- Für Upload-Verzeichnisse von Webanwendungen und Dateifreigaben
- Für Mailserver und Server, die Dateien von Windows-Clients verarbeiten
- Als nächtlicher Scan ausgewählter Verzeichnisse

!!! tip "Mit EICAR testen"
    Die EICAR-Testdatei ist eine harmlose Zeichenkette, die jeder Virenscanner erkennt. Damit
    testest du, ob Scan und Alarmierung funktionieren, ganz ohne echte Schadsoftware.

!!! warning "Kein Scan des ganzen Servers"
    Ein vollständiger Scan von `/` dauert lange und liest jede Datei. Auf Linux-Servern ist
    ClamAV vor allem für Dateien sinnvoll, die von außen kommen: Uploads, Mail, Freigaben.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | `sudo apt install clamav` | `sudo apt install clamav` | `sudo dnf install clamav clamav-update` (EPEL) | `sudo pacman -S clamav` |

## Verwandte Befehle

[rkhunter](rkhunter.md) · [chkrootkit](chkrootkit.md) · [find](../02-navigation/find.md)
