# su

> Wechselt im aktuellen Terminal zu einem anderen Benutzer, standardmäßig zu `root`.

![su output](../assets/screenshots/07-users-groups/su.png)

## Syntax

```bash
su [OPTION]... [-] [BENUTZER]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-`, `-l`, `--login` | Login-Shell starten: Umgebung, `$PATH` und Verzeichnis des Zielbenutzers |
| `-c BEFEHL` | Nur einen einzelnen Befehl als anderer Benutzer ausführen |
| `-s SHELL`, `--shell` | Diese Shell statt der Login-Shell des Benutzers verwenden |
| `-p`, `--preserve-environment` | Die aktuelle Umgebung behalten |

Ohne `-` bleibst du in deinem Verzeichnis und behältst den Großteil deiner Umgebung. Mit
`-` ist es wie eine frische Anmeldung als der andere Benutzer.

## Beispiele

**Mit dem Root-Passwort zu `root` werden:**

```bash
su -
whoami
```

```text
Password:
root
```

**Zu einem anderen Benutzer wechseln:**

```bash
su - alice
pwd
```

```text
Password:
/home/alice
```

Du brauchst das Passwort von `alice`, nicht dein eigenes.

**Einen einzelnen Befehl als `root` ausführen:**

```bash
su -c 'systemctl restart nginx'
```

```text
Password:
```

**Als Dienstbenutzer ohne Login-Shell arbeiten:**

```bash
sudo su - www-data
sudo su - www-data -s /bin/bash -c 'whoami'
```

```text
This account is currently not available.
www-data
```

`www-data` hat die Shell `/usr/sbin/nologin`. Mit `-s /bin/bash` kannst du trotzdem
Befehle als dieser Benutzer ausführen.

**Falsches Passwort:**

```bash
su -
```

```text
Password:
su: Authentication failure
```

## Wann brauche ich das?

- Auf Servern, auf denen `root` ein Passwort hat und `sudo` nicht installiert ist
- Um etwas mit den Rechten und der Umgebung eines anderen Benutzers zu testen, etwa eines
  Deploy-Benutzers
- Um Befehle als Dienstbenutzer auszuführen, der sich normalerweise nicht anmelden kann

!!! tip "Immer `su -` nehmen"
    Ein einfaches `su` behält deine Umgebung, auch deinen `$PATH`. Befehle aus `/usr/sbin`
    werden dann eventuell nicht gefunden, und Einstellungen deines Benutzers rutschen in
    die Root-Shell. `su -` gibt dir eine saubere Login-Umgebung.

!!! warning "`su` braucht das Passwort des Zielbenutzers"
    Mit `su` braucht jeder, der `root` werden will, das Root-Passwort. Mit `sudo` nutzt
    jeder sein eigenes Passwort, und jeder Befehl wird protokolliert. Auf Servern mit
    mehreren Admins ist `sudo` die bessere Wahl.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Root-Passwort | bei der Installation gesetzt oder leer gelassen (dann gesperrt) | gesperrt | bei der Installation gesetzt oder gesperrt | vom Admin gesetzt |
| `sudo` installiert | wenn das Root-Passwort leer blieb | ja | ja | nein |

Hat `root` kein Passwort, nimm `sudo -i` statt `su -`.

## Verwandte Befehle

[whoami](../01-orientation/whoami.md) · [id](../01-orientation/id.md) · [sudo](sudo.md)
