# ssh

> Meldet sich über eine verschlüsselte Verbindung an einem entfernten Server an, führt dort Befehle aus und tunnelt andere Verbindungen hindurch.

![ssh output](../assets/screenshots/12-ssh/ssh.png)

## Syntax

```bash
ssh [OPTION]... [BENUTZER@]HOST [BEFEHL]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-p PORT` | Mit einem anderen Port als `22` verbinden |
| `-i DATEI` | Diesen privaten Schlüssel nutzen |
| `-J HOST` | Über einen Sprungserver verbinden |
| `-L LPORT:HOST:PORT` | Lokaler Tunnel: `LPORT` auf deinem Rechner führt zu `HOST:PORT`, vom Server aus gesehen |
| `-R RPORT:HOST:PORT` | Entfernter Tunnel: Ein Port auf dem Server führt zurück auf deine Seite |
| `-D PORT` | Dynamischer Tunnel: ein SOCKS-Proxy über den Server |
| `-N`, `-f` | Kein entfernter Befehl, in den Hintergrund gehen (für Tunnel) |
| `-t` | Ein Terminal erzwingen, z. B. für `sudo` in einem entfernten Befehl |
| `-v` | Debug-Ausgabe zeigen, um Anmeldeprobleme zu finden |

## Beispiele

**Zum ersten Mal mit einem Server verbinden:**

```bash
ssh nox@192.0.2.10
```

```text
The authenticity of host '192.0.2.10 (192.0.2.10)' can't be established.
ED25519 key fingerprint is SHA256:7awcmzPpIyIq2FLg8thedrrsPVr3eAEl4Q7s7ZBpAdE.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.0.2.10' (ED25519) to the list of known hosts.
nox@192.0.2.10's password:
Linux tuxcodex-srv 6.12.48+deb13-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.12.48-1 (2025-09-20) x86_64

Last login: Mon Oct 26 09:12:44 2026 from 192.0.2.45
```

Vergleiche den Fingerprint mit dem, den dir der Serveradmin oder die Konsole des Hosters
zeigt, bevor du mit `yes` antwortest.

**Einen einzelnen Befehl auf dem Server ausführen:**

```bash
ssh nox@192.0.2.10 uptime
```

```text
 10:42:17 up 12 days,  3:05,  2 users,  load average: 0.08, 0.03, 0.01
```

Mit einem Host aus `~/.ssh/config` (siehe [Grundlagen](basics.md)) reicht `web` statt
`nox@192.0.2.10`.

**Eine Datenbank erreichen, die nur auf dem Server selbst lauscht:**

```bash
ssh -f -N -L 5433:127.0.0.1:5432 nox@192.0.2.10
ss -tln | grep 5433
```

```text
LISTEN 0      128        127.0.0.1:5433      0.0.0.0:*
```

Port `5433` auf deinem Rechner führt jetzt zu `127.0.0.1:5432` auf dem Server. Dein
Datenbankwerkzeug verbindet sich mit `localhost:5433`, die Datenbank selbst bleibt nach
außen geschlossen.

**Über einen Sprungserver verbinden:**

```bash
ssh -J nox@192.0.2.10 nox@192.0.2.20 hostname
```

```text
tuxcodex-db
```

Der Datenbankserver `192.0.2.20` ist von außen nicht erreichbar. `-J` verbindet in einem
Schritt über `192.0.2.10`.

**Der Host-Key hat sich geändert:**

```bash
ssh nox@192.0.2.10
```

```text
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:3qrz2WaaPN7BZOUbSTXHRndWQcm8gTxZgtaniXKLSGs.
Please contact your system administrator.
Add correct host key in /home/nox/.ssh/known_hosts to get rid of this message.
Offending ED25519 key in /home/nox/.ssh/known_hosts:3
  remove with:
  ssh-keygen -f '/home/nox/.ssh/known_hosts' -R '192.0.2.10'
Host key for 192.0.2.10 has changed and you have requested strict checking.
Host key verification failed.
```

SSH verweigert die Verbindung. Wurde der Server neu installiert, entferne den alten
Schlüssel mit dem angezeigten Befehl und verbinde dich neu. Wenn nicht, finde erst heraus,
warum.

## Wann brauche ich das?

- Für jede Verwaltungsaufgabe auf einem entfernten Server
- Um Dienste zu erreichen, die nur auf dem Server selbst erreichbar sind, etwa Datenbanken
- Um Server in einem internen Netz über einen Sprungserver zu erreichen

!!! tip "Anmeldeprobleme untersuchen"
    `ssh -v nox@192.0.2.10` zeigt, welche Schlüssel angeboten werden und welche Methoden der
    Server akzeptiert. Die Zeilen `Offering public key` und
    `Authentications that can continue` verraten meist das Problem.

!!! warning "Eine eingefrorene Sitzung verlassen"
    Hängt die Verbindung, tippe ++enter++, dann `~.` (Tilde, Punkt). SSH beendet die Sitzung
    sofort, auch wenn der Server nicht mehr antwortet.

## Verwandte Befehle

[ssh-keygen](ssh-keygen.md) · [ssh-copy-id](ssh-copy-id.md) · [scp](scp.md) · [sshd](sshd.md) · [ssh-keygen](ssh-keygen.md)
