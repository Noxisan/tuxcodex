# passwd

> Ändert das Passwort eines Benutzers und kann es sperren, entsperren oder ablaufen lassen.

![passwd output](../assets/screenshots/07-users-groups/passwd.png)

## Syntax

```bash
passwd [OPTION]... [BENUTZER]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Das eigene Passwort ändern |
| `BENUTZER` | Das Passwort eines anderen Benutzers ändern (als `root`) |
| `-S`, `--status` | Passwortstatus anzeigen |
| `-l`, `--lock` | Passwort sperren |
| `-u`, `--unlock` | Passwort entsperren |
| `-e`, `--expire` | Passwortwechsel bei der nächsten Anmeldung erzwingen |
| `-d`, `--delete` | Passwort löschen (Anmeldung ohne Passwort) |

Statusbuchstaben bei `passwd -S`:

| Buchstabe | Bedeutung |
|-----------|-----------|
| `P` | Der Benutzer hat ein nutzbares Passwort |
| `L` | Das Passwort ist gesperrt |
| `NP` | Der Benutzer hat kein Passwort |

## Beispiele

**Das eigene Passwort ändern:**

```bash
passwd
```

```text
Changing password for nox.
Current password:
New password:
Retype new password:
passwd: password updated successfully
```

Was du tippst, wird nicht angezeigt, auch nicht als `*`.

**Das Passwort eines anderen Benutzers setzen:**

```bash
sudo passwd alice
```

```text
New password:
Retype new password:
passwd: password updated successfully
```

Als `root` musst du das alte Passwort nicht kennen.

**Bei der nächsten Anmeldung ein neues Passwort erzwingen:**

```bash
sudo passwd -e alice
```

```text
passwd: password expiry information changed.
```

Meldet sich `alice` das nächste Mal an, fragt das System sofort nach einem neuen Passwort.

**Den Passwortstatus anzeigen:**

```bash
sudo passwd -S alice
```

```text
alice P 2026-10-26 0 99999 7 -1
```

Die Felder: Benutzer, Status, Datum der letzten Änderung, minimales Alter, maximales
Alter, Vorwarnzeit und Inaktivitätszeit in Tagen.

**Tippfehler bei der zweiten Eingabe:**

```bash
passwd
```

```text
Changing password for nox.
Current password:
New password:
Retype new password:
Sorry, passwords do not match.
passwd: Authentication token manipulation error
passwd: password unchanged
```

## Wann brauche ich das?

- Um einem neuen Benutzer ein Startpasswort zu geben, am besten zusammen mit `passwd -e`
- Um das Passwort eines Benutzers zurückzusetzen, der es vergessen hat
- Um ein Konto vorübergehend zu sperren (`-l`) und später wieder zu entsperren (`-u`)
- Um zu prüfen, ob ein Konto überhaupt ein Passwort hat (`-S`)

!!! tip "Startpasswörter"
    Setze ein zufälliges Startpasswort und erzwinge einen Wechsel bei der ersten
    Anmeldung: `sudo passwd alice` und danach `sudo passwd -e alice`. So kennt nur der
    Benutzer selbst das endgültige Passwort.

!!! warning "`-l` hält SSH-Schlüssel nicht auf"
    Ein gesperrtes Passwort blockiert nur Anmeldungen mit Passwort. Wer einen
    SSH-Schlüssel in `~/.ssh/authorized_keys` hat, kann sich weiter anmelden. Wie du ein
    Konto ganz sperrst, steht bei [`usermod`](usermod.md).

!!! danger "Auf Servern nie `passwd -d`"
    `-d` entfernt das Passwort komplett. Je nach Konfiguration kann sich dann jeder ohne
    Passwort als dieser Benutzer anmelden.

## Verwandte Befehle

[usermod](usermod.md) · [adduser](adduser.md) · [chage](chage.md)
