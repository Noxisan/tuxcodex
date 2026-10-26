# Die wichtigen Dateien

| Datei | Inhalt |
|-------|--------|
| `/etc/passwd` | Alle Benutzerkonten: Name, UID, GID, Home-Verzeichnis, Shell |
| `/etc/shadow` | Passwort-Hashes und Passwort-Ablauf, nur für `root` lesbar |
| `/etc/group` | Alle Gruppen und ihre zusätzlichen Mitglieder |
| `/etc/gshadow` | Gruppenpasswörter und Gruppenverwalter |
| `/etc/sudoers` | Wer `sudo` wofür benutzen darf, nur mit `visudo` bearbeiten |
| `/etc/sudoers.d/` | Zusätzliche `sudo`-Regeln als eigene Dateien |
| `/etc/skel/` | Vorlagen, die in jedes neue Home-Verzeichnis kopiert werden |
| `/etc/login.defs` | Standardwerte: UID-Bereiche, Passwort-Ablauf, `umask` |
| `/etc/adduser.conf` | Standardwerte für `adduser` und `addgroup` unter Debian und Ubuntu |

Eine Zeile aus `/etc/passwd`, Feld für Feld:

```text
nox:x:1000:1000:Nox,,,:/home/nox:/bin/bash
 │  │  │    │     │       │         └ Login-Shell
 │  │  │    │     │       └ Home-Verzeichnis
 │  │  │    │     └ vollständiger Name und Kontaktdaten (GECOS)
 │  │  │    └ GID der primären Gruppe
 │  │  └ UID
 │  └ x = das Passwort steht in /etc/shadow
 └ Benutzername
```

| UID-Bereich | Bedeutung |
|-------------|-----------|
| `0` | `root` |
| `1` bis `999` | Systembenutzer für Dienste, wie `www-data` (33) oder `sshd` |
| ab `1000` | Normale Benutzer (bis `59999` unter Debian und Ubuntu, `60000` unter RHEL und Arch) |
| `65534` | `nobody`, ein Benutzer ganz ohne Rechte |

!!! tip "Die Dateien nie direkt bearbeiten"
    Nimm die Befehle aus diesem Kapitel, statt `/etc/passwd`, `/etc/shadow` oder
    `/etc/group` mit einem Editor zu bearbeiten. Sie sperren die Dateien und halten alle
    zueinander stimmig. Wenn es wirklich sein muss, nimm `vipw` und `vigr`.
