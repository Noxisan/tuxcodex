# adduser

> Legt unter Debian Schritt für Schritt einen neuen Benutzer an: Home-Verzeichnis, Gruppe, Passwort und Kontaktdaten in einem Durchgang.

![adduser output](../assets/screenshots/07-users-groups/adduser.png)

## Syntax

```bash
adduser [OPTION]... BENUTZER
adduser BENUTZER GRUPPE
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--disabled-password` | Benutzer ohne Passwort anlegen (Anmeldung nur mit SSH-Schlüssel) |
| `--disabled-login` | Benutzer ganz ohne Anmeldung anlegen |
| `--comment TEXT` | Vollständiger Name oder Beschreibung, ohne Nachfrage |
| `--shell SHELL` | Login-Shell (Standard `/bin/bash`) |
| `--home VERZ` | Home-Verzeichnis (Standard `/home/BENUTZER`) |
| `--ingroup GRUPPE` | Eine vorhandene Gruppe als primäre Gruppe verwenden |
| `--uid ID` | Diese UID verwenden |
| `--system` | Einen Systembenutzer für einen Dienst anlegen (UID unter 1000) |
| `--group` | Mit `--system`: auch eine gleichnamige Gruppe anlegen |
| `--no-create-home` | Kein Home-Verzeichnis anlegen |
| `--verbose` | Jeden Schritt anzeigen |

## Beispiele

**Einen neuen Benutzer interaktiv anlegen:**

```bash
sudo adduser alice
```

```text
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for alice
Enter the new value, or press ENTER for the default
        Full Name []: Alice Example
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] y
```

`adduser` legt die Gruppe `alice` an, das Home-Verzeichnis `/home/alice` mit den Dateien
aus `/etc/skel` und fragt nach Passwort und Kontaktdaten.

**Einen Benutzer nur für SSH-Schlüssel anlegen und jeden Schritt anzeigen:**

```bash
sudo adduser --verbose --disabled-password --comment "Deploy User" deploy
```

```text
info: Adding user `deploy' ...
info: Selecting UID/GID from range 1000 to 59999 ...
info: Adding new group `deploy' (1002) ...
info: Adding new user `deploy' (1002) with group `deploy (1002)' ...
info: Creating home directory `/home/deploy' ...
info: Copying files from `/etc/skel' ...
info: Adding new user `deploy' to supplemental / extra groups `users' ...
info: Adding user `deploy' to group `users' ...
```

**Einen vorhandenen Benutzer einer Gruppe hinzufügen:**

```bash
sudo adduser alice sudo
groups alice
```

```text
alice : alice users sudo
```

**Einen Systembenutzer für einen Dienst anlegen:**

```bash
sudo adduser --system --group --no-create-home --home /nonexistent myapp
getent passwd myapp
```

```text
myapp:x:105:107::/nonexistent:/usr/sbin/nologin
```

Systembenutzer bekommen eine UID unter 1000 und keine Login-Shell.

**Versuchen, einen Benutzer anzulegen, der schon existiert:**

```bash
sudo adduser alice
```

```text
fatal: The user `alice' already exists.
```

## Wann brauche ich das?

- Um Konten für neue Admins oder Teammitglieder auf einem Server anzulegen
- Um einen Benutzer für Deployments oder Backups anzulegen, der sich nur mit
  SSH-Schlüssel anmeldet
- Um einen Systembenutzer für einen eigenen Dienst anzulegen, damit er nicht als `root`
  läuft
- Um einen Benutzer einer Gruppe hinzuzufügen, zum Beispiel `sudo` oder `docker`

!!! tip "`adduser` statt `useradd` unter Debian"
    `adduser` legt standardmäßig das Home-Verzeichnis an, kopiert `/etc/skel` und setzt
    ein Passwort. Bei `useradd` musst du an all das selbst denken. Für Skripte, die auf
    mehreren Distributionen laufen, ist [`useradd`](useradd.md) die portable Wahl.

!!! warning "Neue Gruppen brauchen eine neue Anmeldung"
    Nach `adduser alice sudo` gilt die neue Gruppe erst in neuen Sitzungen von `alice`.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| `adduser` | installiert, empfohlener Weg | nicht vorhanden |
| Alternative | `useradd` | `useradd -m -G wheel alice` und danach `passwd alice` |

## Verwandte Befehle

[groups](groups.md) · [getent](getent.md) · [useradd](useradd.md) · [deluser](deluser.md)
