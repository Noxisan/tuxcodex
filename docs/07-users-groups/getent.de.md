# getent

> Schlägt Einträge in den Systemdatenbanken nach: Benutzer, Gruppen, Hosts und Dienste, aus lokalen Dateien und aus Verzeichnisdiensten wie LDAP.

![getent output](../assets/screenshots/07-users-groups/getent.png)

## Syntax

```bash
getent [OPTION]... DATENBANK [SCHLÜSSEL]...
```

## Optionen

| Datenbank | Inhalt |
|-----------|--------|
| `passwd` | Benutzerkonten |
| `group` | Gruppen und ihre Mitglieder |
| `shadow` | Passwortdaten (nur als `root`) |
| `hosts` | Hostnamen und IP-Adressen |
| `services` | Netzwerkdienste und ihre Ports |

| Option | Beschreibung |
|--------|--------------|
| `-s QUELLE`, `--service=QUELLE` | Nur eine bestimmte Quelle fragen, z. B. `files` oder `ldap` |

Ohne Schlüssel listet `getent` alle Einträge der Datenbank. Der Exit-Status ist `0`, wenn
etwas gefunden wurde, und `2`, wenn nicht.

## Beispiele

**Einen Benutzer nachschlagen:**

```bash
getent passwd nox
```

```text
nox:x:1000:1000:Nox,,,:/home/nox:/bin/bash
```

**Den Benutzer zu einer UID finden:**

```bash
getent passwd 33
```

```text
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

**Die Mitglieder einer Gruppe anzeigen:**

```bash
getent group sudo
```

```text
sudo:x:27:nox
```

**Prüfen, ob ein Benutzer existiert:**

```bash
getent passwd ghost
echo $?
```

```text
2
```

**Einen Hostnamen so auflösen wie das System:**

```bash
getent hosts tuxcodex-srv
```

```text
127.0.1.1       tuxcodex-srv.example.com tuxcodex-srv
```

**Den Port eines Dienstes finden:**

```bash
getent services ssh
```

```text
ssh                   22/tcp
```

**Die Passwortdaten eines Benutzers anzeigen:**

```bash
sudo getent shadow nox
```

```text
nox:$y$j9T$ExampleSaltOnly$ExampleHashOnlyNotARealPasswordHash:20752:0:99999:7:::
```

Die Felder nach dem Hash: letzte Änderung (Tage seit 1970), minimales und maximales Alter
und Vorwarnzeit.

## Wann brauche ich das?

- Um in Skripten zu prüfen, ob ein Benutzer oder eine Gruppe existiert, bevor du sie anlegst
- Auf Servern mit LDAP, Active Directory oder SSSD, wo Benutzer nicht in `/etc/passwd`
  stehen: `getent` fragt alle eingerichteten Quellen
- Um die Namensauflösung so zu testen, wie Programme sie sehen, inklusive `/etc/hosts`

!!! tip "`getent` statt `grep /etc/passwd`"
    `grep nox /etc/passwd` findet nur lokale Benutzer und trifft `nox` auch in anderen
    Namen. `getent passwd nox` sucht genau nach diesem Namen in allen Quellen.

!!! tip "Die Gruppe zu einer GID finden"
    `getent group 1001` zeigt, welche Gruppe die GID 1001 hat, etwa wenn `ls -l` eine Zahl
    statt eines Gruppennamens zeigt.

## Verwandte Befehle

[groups](groups.md) · [id](../01-orientation/id.md)
