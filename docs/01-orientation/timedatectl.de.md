# timedatectl

> Zeigt und setzt die Zeitzone und die Zeitsynchronisation (NTP) des Systems.

## Syntax

```bash
timedatectl [OPTION]... [BEFEHL]
```

## Optionen

| Option / Befehl | Beschreibung |
|-----------------|--------------|
| `status` | Uhrzeit, Zeitzone und Synchronisationsstatus anzeigen (Standard ohne Befehl) |
| `set-timezone ZONE` | Zeitzone setzen, z. B. `Europe/Berlin` oder `UTC` |
| `list-timezones` | Alle verfügbaren Zeitzonen auflisten |
| `set-ntp BOOL` | Zeitsynchronisation übers Netz ein- (`true`) oder ausschalten (`false`) |
| `timesync-status` | Details von `systemd-timesyncd` anzeigen (Server, Abweichung, Abfrageintervall) |
| `set-time ZEIT` | Uhrzeit von Hand setzen (nur bei ausgeschaltetem NTP möglich) |
| `show` | Alle Einstellungen als `Name=Wert`-Paare anzeigen, für Skripte |
| `-p`, `--property=NAME` | Mit `show`: nur die Eigenschaft `NAME` ausgeben |
| `--value` | Mit `show`: nur den Wert ausgeben, ohne `NAME=` |

## Beispiele

**Uhrzeit, Zeitzone und Synchronisationsstatus anzeigen:**

```bash
timedatectl
```

```text
               Local time: Mon 2026-10-26 10:42:17 CET
           Universal time: Mon 2026-10-26 09:42:17 UTC
                 RTC time: Mon 2026-10-26 09:42:17
                Time zone: Europe/Berlin (CET, +0100)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

**Eine Zeitzone finden:**

```bash
timedatectl list-timezones | grep Berlin
```

```text
Europe/Berlin
```

**Die Zeitzone setzen:**

```bash
sudo timedatectl set-timezone Europe/Berlin
timedatectl | grep 'Time zone'
```

```text
                Time zone: Europe/Berlin (CET, +0100)
```

**Zeitsynchronisation einschalten und prüfen:**

```bash
sudo timedatectl set-ntp true
timedatectl | grep -E 'synchronized|NTP'
```

```text
System clock synchronized: yes
              NTP service: active
```

**Details der Zeitsynchronisation anzeigen:**

```bash
timedatectl timesync-status
```

```text
       Server: 192.0.2.123 (0.debian.pool.ntp.org)
Poll interval: 34min 8s (min: 32s; max 34min 8s)
         Leap: normal
      Version: 4
      Stratum: 2
    Reference: C0000201
    Precision: 1us (-25)
Root distance: 23.588ms (max: 5s)
       Offset: -312us
        Delay: 14.207ms
       Jitter: 1.104ms
 Packet count: 42
    Frequency: +3.512ppm
```

**Nur die Zeitzone auslesen (für Skripte):**

```bash
timedatectl show --property=Timezone --value
```

```text
Europe/Berlin
```

![timedatectl output](../assets/screenshots/01-orientation/timedatectl.png)

## Wann brauche ich das?

- Nach der Installation eines Servers: richtige Zeitzone setzen und prüfen, ob NTP läuft
- Wenn Zeiten in Logs falsch aussehen oder Einträge zweier Server nicht zusammenpassen
- Wenn TLS-Verbindungen, Kerberos oder 2FA-Codes scheitern – eine falsche Uhr ist eine
  häufige Ursache
- Um zu prüfen, ob die Zeitsynchronisation funktioniert (`System clock synchronized: yes`)

!!! tip "UTC auf Servern"
    Viele Admins stellen Server auf `UTC` (`sudo timedatectl set-timezone UTC`). Dann
    lassen sich Logs von Servern an verschiedenen Standorten direkt vergleichen, und es
    gibt keine Sprünge bei der Zeitumstellung.

!!! warning "`System clock synchronized: no`"
    Ist die Uhr nicht synchronisiert, schau auf `NTP service`. Bei `inactive` schaltest
    du sie mit `sudo timedatectl set-ntp true` ein. Bei `n/a` ist kein NTP-Client
    installiert (siehe unten). Prüfe außerdem, ob die Firewall ausgehend UDP-Port 123
    erlaubt.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| NTP-Client | eigenes Paket `systemd-timesyncd` (oder `chrony`) | `systemd-timesyncd` gehört zu `systemd` |
| Aktiviert | automatisch, sobald installiert | nein – einschalten mit `sudo timedatectl set-ntp true` |

Zeigt `timedatectl` unter Debian `NTP service: n/a`, installiere den Client:

```bash
sudo apt install systemd-timesyncd
```

## Verwandte Befehle

[date](date.md) · [hostnamectl](hostnamectl.md)
