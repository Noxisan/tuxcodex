# loginctl

> Zeigt und steuert Anmeldesitzungen: wer über welche Sitzung angemeldet ist, und beendet Sitzungen oder alle Prozesse eines Benutzers.

![loginctl output](../assets/screenshots/09-systemd/loginctl.png)

## Syntax

```bash
loginctl [OPTION]... [BEFEHL] [ARGUMENT]...
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| *(keiner)*, `list-sessions` | Alle Sitzungen auflisten |
| `list-users` | Alle angemeldeten Benutzer auflisten |
| `session-status ID` | Details und Prozesse einer Sitzung |
| `terminate-session ID` | Eine Sitzung mit allen ihren Prozessen beenden |
| `terminate-user BENUTZER` | Alle Sitzungen und Prozesse eines Benutzers beenden |
| `enable-linger BENUTZER` | Die Dienste des Benutzers nach dem Abmelden weiterlaufen lassen |
| `show-user BENUTZER -p EIGENSCHAFT` | Eine einzelne Eigenschaft ausgeben, z. B. `Linger` |

## Beispiele

**Alle Sitzungen anzeigen:**

```bash
loginctl
```

```text
SESSION  UID USER  SEAT LEADER CLASS   TTY   IDLE SINCE
      4 1000 nox   -    2190   user    pts/0 no   -
      5 1000 nox   -    2195   manager -     no   -
     12 1001 alice -    3118   user    pts/1 no   -
     13 1001 alice -    3122   manager -     no   -

4 sessions listed.
```

`user`-Sitzungen sind die SSH-Anmeldungen. Die `manager`-Sitzungen gehören zum eigenen
Dienstmanager des Benutzers, den systemd für jeden angemeldeten Benutzer startet.

**Die angemeldeten Benutzer auflisten:**

```bash
loginctl list-users
```

```text
 UID USER  LINGER STATE
1000 nox   no     active
1001 alice no     active

2 users listed.
```

**Einen Benutzer vollständig abmelden:**

```bash
sudo loginctl terminate-user alice
loginctl list-users
```

```text
 UID USER LINGER STATE
1000 nox  no     active

1 users listed.
```

Alle Prozesse von `alice` werden beendet, auch Programme, die im Hintergrund gestartet
wurden.

**Die Dienste eines Benutzers nach dem Abmelden weiterlaufen lassen:**

```bash
sudo loginctl enable-linger nox
loginctl show-user nox -p Linger
```

```text
Linger=yes
```

## Wann brauche ich das?

- Um zu sehen, wer angemeldet ist und über welche Sitzung
- Um einen Benutzer, dessen Konto du gesperrt hast, samt aller Hintergrundprozesse abzumelden
- Um eigene Benutzerdienste oder Timer (`systemctl --user`) ohne Anmeldung laufen zu lassen

!!! tip "Sitzungen sauber beenden"
    `terminate-user` ist gründlicher als `pkill -u`: systemd kennt jeden Prozess einer
    Sitzung, auch solche, die die Shell längst verlassen haben.

!!! warning "Hintergrundjobs enden beim Abmelden"
    Je nach Einstellung `KillUserProcesses=` in `/etc/systemd/logind.conf` beendet
    systemd beim Abmelden alle Prozesse einer Sitzung, sogar mit `nohup` gestartete Jobs.
    Für Jobs, die weiterlaufen müssen, nimm `systemd-run` oder `enable-linger`.

## Verwandte Befehle

[who](../01-orientation/who.md) · [w](../01-orientation/w.md) · [pkill](../08-processes/pkill.md) · [systemd-run](systemd-run.md) · [shutdown](shutdown.md)
