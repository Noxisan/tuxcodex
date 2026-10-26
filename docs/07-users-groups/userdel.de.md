# userdel

> Löscht ein Benutzerkonto, auf Wunsch samt Home-Verzeichnis und Mail-Spool, auf jeder Distribution.

![userdel output](../assets/screenshots/07-users-groups/userdel.png)

## Syntax

```bash
userdel [OPTION]... BENUTZER
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-r`, `--remove` | Auch das Home-Verzeichnis und den Mail-Spool löschen |
| `-f`, `--force` | Auch löschen, wenn der Benutzer noch angemeldet ist (gefährlich) |

## Beispiele

**Einen Benutzer löschen:**

```bash
sudo userdel carol
getent passwd carol
echo $?
```

```text
2
```

Das Konto ist weg, `getent` findet nichts mehr.

**Einen Benutzer mit Home-Verzeichnis löschen:**

```bash
sudo userdel -r bob
```

```text
userdel: bob mail spool (/var/mail/bob) not found
```

Die Meldung ist harmlos: `bob` hatte einfach nie einen Mail-Spool. Das Home-Verzeichnis
wurde gelöscht.

**Was ohne `-r` übrig bleibt:**

```bash
sudo userdel dave
stat -c '%U:%G %n' /home/dave
```

```text
UNKNOWN:UNKNOWN /home/dave
```

Das Home-Verzeichnis existiert noch, gehört aber einer UID, die keinen Namen mehr hat.

**Versuchen, einen angemeldeten Benutzer zu löschen:**

```bash
sudo userdel alice
```

```text
userdel: user alice is currently used by process 2345
```

## Wann brauche ich das?

- Um Konten in Skripten oder auf Distributionen ohne `deluser` zu löschen
- Um aufzuräumen, wenn eine Person oder ein Dienst endgültig weg ist
- In Ansible oder anderer Automatisierung, wo das Modul `user` im Hintergrund `userdel`
  nutzt

!!! tip "Erst laufende Prozesse beenden"
    Finde die Prozesse des Benutzers mit `ps -u alice` und beende sie, oder nimm
    `sudo pkill -u alice`. Danach funktioniert `userdel` ohne `-f`.

!!! warning "Verwaiste Dateien"
    Dateien eines gelöschten Benutzers bleiben überall außerhalb des Home-Verzeichnisses
    liegen. Bekommt später ein neuer Benutzer dieselbe UID, gehören ihm plötzlich diese
    Dateien. Finde sie vor dem Löschen mit `sudo find / -xdev -user alice`.

!!! danger "`-f`, während der Benutzer arbeitet"
    `userdel -f` löscht das Konto, auch während Prozesse des Benutzers laufen. Sie laufen
    unter einer UID ohne Namen weiter, was Fehler schwer nachvollziehbar macht.

## Verwandte Befehle

[deluser](deluser.md) · [useradd](useradd.md)
