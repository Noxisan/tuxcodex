# SSH verstehen

SSH (Secure Shell) ist die verschlüsselte Verbindung zu einem Server. Sie schützt alles,
was du tippst und siehst, auch Passwörter, und sie trägt Dateiübertragungen mit `scp`,
`sftp` und `rsync` sowie Tunnel für andere Verbindungen.

## Zwei Arten von Schlüsseln

| Schlüssel | Gehört zu | Zweck |
|-----------|-----------|-------|
| **Host-Key** | Dem Server, in `/etc/ssh/ssh_host_*_key` | Beweist dem Client, dass er mit dem richtigen Server spricht |
| **Benutzerschlüssel** | Dir, in `~/.ssh/id_ed25519` | Beweist dem Server, wer du bist, statt eines Passworts |

## Host-Keys und `known_hosts`

Bei der ersten Verbindung zeigt der Client den Fingerprint des Host-Keys an und fragt, ob
du ihm vertraust. Nach `yes` wird der Schlüssel in `~/.ssh/known_hosts` gespeichert. Bei
jeder weiteren Verbindung prüft der Client, ob der Server noch denselben Schlüssel hat.

Ändert sich der Schlüssel, verweigert SSH die Verbindung mit
`WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`. Das passiert nach einer
Neuinstallation des Servers, kann aber auch ein Angriff sein. Entferne den alten Schlüssel
mit `ssh-keygen -R HOST` nur, wenn du weißt, warum er sich geändert hat.

## Anmeldung per Schlüssel

Ein Schlüsselpaar besteht aus zwei Dateien:

| Datei | Inhalt | Wer sie sehen darf |
|-------|--------|--------------------|
| `~/.ssh/id_ed25519` | Privater Schlüssel | Nur du. Nie auf einen Server kopieren |
| `~/.ssh/id_ed25519.pub` | Öffentlicher Schlüssel | Jeder. Er kommt auf die Server |

Der öffentliche Schlüssel kommt auf dem Server in `~/.ssh/authorized_keys`, zum Beispiel
mit `ssh-copy-id`. Bei der Anmeldung prüft der Server damit, dass du den privaten
Schlüssel besitzt, ohne dass dieser je deinen Rechner verlässt.

Schütze den privaten Schlüssel mit einer Passphrase. Mit `ssh-agent` gibst du sie nur
einmal pro Sitzung ein.

## Die Dateien in `~/.ssh` und ihre Rechte

SSH verweigert Schlüssel und Konfigurationsdateien, die andere Benutzer lesen oder ändern
könnten.

| Datei | Rechte | Zweck |
|-------|--------|-------|
| `~/.ssh/` | `700` (`drwx------`) | Das Verzeichnis selbst |
| `id_ed25519` | `600` (`-rw-------`) | Privater Schlüssel |
| `id_ed25519.pub` | `644` (`-rw-r--r--`) | Öffentlicher Schlüssel |
| `authorized_keys` | `600` | Öffentliche Schlüssel, die sich bei diesem Konto anmelden dürfen |
| `known_hosts` | `644` | Host-Keys bekannter Server |
| `config` | `600` | Client-Konfiguration |

## Die Client-Konfiguration `~/.ssh/config`

Statt jedes Mal Benutzer, Port und Schlüssel einzutippen, gibst du jedem Server einen
kurzen Namen:

```text
Host web
    HostName 192.0.2.10
    User nox
    Port 22
    IdentityFile ~/.ssh/id_ed25519

Host db
    HostName 192.0.2.20
    User nox
    ProxyJump web

Host *
    ServerAliveInterval 60
```

Jetzt verbindet `ssh web` mit `nox@192.0.2.10`, und `ssh db` erreicht den Datenbankserver
über `web` als Sprungserver. `ServerAliveInterval` hält untätige Verbindungen offen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket des SSH-Servers | `openssh-server` | `openssh-server` | `openssh-server` | `openssh` |
| Dienstname | `ssh` | `ssh` (seit 22.10 über einen Socket gestartet) | `sshd` | `sshd` |
| Root-Login standardmäßig | nur mit Schlüssel | nur mit Schlüssel | nur mit Schlüssel | nur mit Schlüssel |

!!! tip "Ed25519-Schlüssel nutzen"
    `ssh-keygen -t ed25519` erzeugt kurze, schnelle und sichere Schlüssel. RSA-Schlüssel
    funktionieren weiterhin, sollten aber mindestens 3072 Bit lang sein.

!!! danger "Sperr dich nie aus"
    Bevor du auf einem Server die Passwort-Anmeldung abschaltest, teste die Anmeldung per
    Schlüssel in einer **zweiten** Sitzung. Lass die erste offen, bis die neue
    funktioniert.
