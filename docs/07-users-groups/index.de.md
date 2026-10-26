---
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-account-multiple-outline:{ .tc-hero-icon }

# Benutzer und Gruppen

Benutzer und Gruppen anlegen, ändern und löschen, Passwörter verwalten und mit
Root-Rechten über `sudo` und `su` arbeiten.

</div>

## Benutzer und Gruppen nachschlagen

<div class="grid cards" markdown>

-   :material-account-group:{ .lg .middle } **[groups](groups.md)**

    ---

    Zeigt die Gruppen eines Benutzers.

-   :material-account-search-outline:{ .lg .middle } **[getent](getent.md)**

    ---

    Schlägt Benutzer, Gruppen, Hosts und Dienste nach.

</div>

## Benutzer verwalten

<div class="grid cards" markdown>

-   :material-account-plus-outline:{ .lg .middle } **[adduser](adduser.md)**

    ---

    Legt Schritt für Schritt einen neuen Benutzer an (Debian).

-   :material-account-plus:{ .lg .middle } **[useradd](useradd.md)**

    ---

    Legt einen Benutzer in einem Befehl an, für Skripte und jede Distribution.

-   :material-account-edit-outline:{ .lg .middle } **[usermod](usermod.md)**

    ---

    Ändert Gruppen, Shell, Name oder Sperre eines Benutzers.

-   :material-form-textbox-password:{ .lg .middle } **[passwd](passwd.md)**

    ---

    Setzt, sperrt, entsperrt oder erneuert ein Passwort.

-   :material-calendar-clock-outline:{ .lg .middle } **[chage](chage.md)**

    ---

    Legt Passwort- und Kontoablauf fest.

-   :material-account-minus-outline:{ .lg .middle } **[deluser](deluser.md)**

    ---

    Löscht einen Benutzer oder entfernt ihn aus einer Gruppe (Debian).

-   :material-account-remove-outline:{ .lg .middle } **[userdel](userdel.md)**

    ---

    Löscht ein Benutzerkonto auf jeder Distribution.

</div>

## Gruppen verwalten

<div class="grid cards" markdown>

-   :material-account-multiple-plus-outline:{ .lg .middle } **[addgroup](addgroup.md)**

    ---

    Legt eine Gruppe an oder fügt ihr einen Benutzer hinzu (Debian).

-   :material-account-multiple-plus:{ .lg .middle } **[groupadd](groupadd.md)**

    ---

    Legt eine Gruppe auf jeder Distribution an.

</div>

## Die wichtigen Dateien

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
| `/etc/adduser.conf` | Standardwerte für `adduser` und `addgroup` unter Debian |

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
| `1000` bis `59999` | Normale Benutzer, angelegt mit `adduser` |
| `65534` | `nobody`, ein Benutzer ganz ohne Rechte |

!!! tip "Die Dateien nie direkt bearbeiten"
    Nimm die Befehle aus diesem Kapitel, statt `/etc/passwd`, `/etc/shadow` oder
    `/etc/group` mit einem Editor zu bearbeiten. Sie sperren die Dateien und halten alle
    zueinander stimmig. Wenn es wirklich sein muss, nimm `vipw` und `vigr`.

!!! tip "Lernpfad"
    Die Befehle sind von einfach nach komplexer sortiert. Arbeite sie der Reihe nach
    durch. Spätere Seiten bauen auf den früheren auf.
