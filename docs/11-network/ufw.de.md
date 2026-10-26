# ufw

> Die unkomplizierte Firewall von Debian und Ubuntu: erlaubt und blockiert Ports mit kurzen, lesbaren Regeln, ohne dass du `nftables`-Regeln von Hand schreiben musst.

![ufw output](../assets/screenshots/11-network/ufw.png)

## Syntax

```bash
ufw [OPTION]... BEFEHL
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `status verbose` | Zustand, Standardrichtlinien und alle Regeln |
| `status numbered` | Regeln mit Nummern, zum Löschen |
| `allow PORT[/PROTO]` | Eingehende Verbindungen auf einem Port erlauben |
| `allow from NETZ to any port PORT` | Einen Port nur für bestimmte Adressen erlauben |
| `deny`, `reject` | Still blockieren oder mit Antwort |
| `limit PORT/tcp` | Erlauben, aber Adressen mit zu vielen Verbindungsversuchen sperren |
| `delete NUMMER` | Eine Regel löschen |
| `enable`, `disable` | Die Firewall ein- oder ausschalten, auch beim Booten |

## Beispiele

**Zustand und alle Regeln anzeigen:**

```bash
sudo ufw status verbose
```

```text
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
80,443/tcp                 ALLOW IN    Anywhere
5432/tcp                   ALLOW IN    192.0.2.0/24
22/tcp (v6)                ALLOW IN    Anywhere (v6)
80,443/tcp (v6)            ALLOW IN    Anywhere (v6)
```

`Default: deny (incoming)` heißt: Alles, was nicht ausdrücklich erlaubt ist, wird
blockiert.

**SSH erlauben, bevor die Firewall eingeschaltet wird:**

```bash
sudo ufw allow 22/tcp
```

```text
Rules updated
Rules updated (v6)
```

Ohne SSH-Regel würde `enable` dich vom Server aussperren.

**Die Firewall einschalten:**

```bash
sudo ufw enable
```

```text
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
```

**Die Datenbank nur aus dem eigenen Netz erlauben:**

```bash
sudo ufw allow from 192.0.2.0/24 to any port 5432 proto tcp
```

```text
Rule added
```

**Eine Regel über ihre Nummer löschen:**

```bash
sudo ufw status numbered
sudo ufw delete 3
```

```text
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    Anywhere
[ 2] 80,443/tcp                 ALLOW IN    Anywhere
[ 3] 5432/tcp                   ALLOW IN    192.0.2.0/24
[ 4] 22/tcp (v6)                ALLOW IN    Anywhere (v6)
[ 5] 80,443/tcp (v6)            ALLOW IN    Anywhere (v6)

Deleting:
 allow from 192.0.2.0/24 to any port 5432 proto tcp
Proceed with operation (y|n)? y
Rule deleted
```

`ufw` löscht die IPv4- und die IPv6-Regel eines Paares getrennt. Prüfe die Nummern nach
jedem Löschen neu, sie verschieben sich.

## Wann brauche ich das?

- Auf jedem Debian- oder Ubuntu-Server, der aus dem Internet erreichbar ist
- Um einen Port für einen neuen Dienst zu öffnen, etwa für einen Webserver
- Um eine Datenbank oder Admin-Oberfläche nur aus bestimmten Netzen erreichbar zu machen

!!! tip "Ratenbegrenzung für SSH"
    `sudo ufw limit 22/tcp` sperrt Adressen, die sich mehr als sechsmal in 30 Sekunden
    verbinden wollen. Das bremst Brute-Force-Angriffe auf SSH deutlich aus.

!!! danger "Zuerst SSH erlauben"
    Führe immer `sudo ufw allow 22/tcp` (oder deinen SSH-Port) vor `ufw enable` aus. Sonst
    blockiert die Firewall deine eigene Sitzung, sobald sie sich neu verbindet.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Firewall-Werkzeug | `ufw` (Paket `ufw`) | `ufw`, installiert, aber inaktiv | `firewall-cmd` | `ufw` oder `nft` |

## Verwandte Befehle

[ss](ss.md) · [nc](nc.md) · [firewall-cmd](firewall-cmd.md)
