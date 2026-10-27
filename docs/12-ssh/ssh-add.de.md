# ssh-add

> Lädt SSH-Schlüssel in den laufenden `ssh-agent`, listet die geladenen Schlüssel auf und entfernt sie wieder.

![ssh-add output](../assets/screenshots/12-ssh/ssh-add.png)

## Syntax

```bash
ssh-add [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Die Standardschlüssel hinzufügen (`~/.ssh/id_ed25519` und andere) |
| `DATEI` | Diesen Schlüssel hinzufügen |
| `-l` | Die Fingerprints der geladenen Schlüssel auflisten |
| `-L` | Die geladenen öffentlichen Schlüssel vollständig auflisten |
| `-t ZEIT` | Den Schlüssel nach `ZEIT` automatisch entfernen, z. B. `1h` |
| `-d DATEI` | Einen einzelnen Schlüssel entfernen |
| `-D` | Alle Schlüssel entfernen |

## Beispiele

**Den Standardschlüssel hinzufügen:**

```bash
ssh-add
```

```text
Enter passphrase for /home/nox/.ssh/id_ed25519:
Identity added: /home/nox/.ssh/id_ed25519 (nox@tuxdex-srv)
```

Ab jetzt nutzt `ssh` den Schlüssel, ohne erneut nach der Passphrase zu fragen.

**Einen Schlüssel nur für eine Stunde hinzufügen:**

```bash
ssh-add -t 1h
```

```text
Enter passphrase for /home/nox/.ssh/id_ed25519:
Identity added: /home/nox/.ssh/id_ed25519 (nox@tuxdex-srv)
Lifetime set to 3600 seconds
```

**Die geladenen Schlüssel anzeigen:**

```bash
ssh-add -l
```

```text
256 SHA256:MH9iiNBiK1fYLz4X57tGWkD2uYd7TpgABke1SUynK1k nox@tuxdex-srv (ED25519)
```

**Den öffentlichen Schlüssel eines geladenen Schlüssels anzeigen:**

```bash
ssh-add -L
```

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAWZDtTcIe235G0EzeAQj/BESDJnWT39gRghXyiMZZal nox@tuxdex-srv
```

**Einen Schlüssel entfernen:**

```bash
ssh-add -d ~/.ssh/id_ed25519
```

```text
Identity removed: /home/nox/.ssh/id_ed25519 ED25519 (nox@tuxdex-srv)
```

**Der Agent ist leer:**

```bash
ssh-add -l
```

```text
The agent has no identities.
```

## Wann brauche ich das?

- Zu Beginn einer Arbeitssitzung, um deinen Schlüssel einmal zu entsperren
- Um zu prüfen, welchen Schlüssel der Agent anbietet, wenn eine Anmeldung scheitert
- Vor einer Pause, um mit `-D` alle Schlüssel aus dem Agenten zu entfernen

!!! tip "Schlüssel automatisch laden"
    Mit `AddKeysToAgent yes` in `~/.ssh/config` fügt `ssh` den Schlüssel bei der ersten
    Nutzung dem Agenten hinzu. Du musst `ssh-add` nicht von Hand aufrufen.

!!! warning "Zu viele Schlüssel"
    Der Agent bietet jeden geladenen Schlüssel nacheinander an. Server erlauben oft nur
    sechs Versuche, mit vielen Schlüsseln siehst du dann `Too many authentication failures`.
    Nutze `IdentitiesOnly yes` und `IdentityFile` pro Host in `~/.ssh/config`.

## Verwandte Befehle

[ssh-agent](ssh-agent.md) · [ssh-keygen](ssh-keygen.md) · [ssh](ssh.md)
