# hostname

> Zeigt den Namen der Maschine an, auf der du gerade bist – oder setzt ihn vorübergehend.

## Syntax

```bash
hostname [OPTION]... [NAME]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-s`, `--short` | Kurzen Hostnamen ausgeben (bis zum ersten Punkt) |
| `-f`, `--fqdn`, `--long` | Vollständigen Domainnamen (FQDN) ausgeben |
| `-d`, `--domain` | DNS-Domainnamen ausgeben |
| `-I`, `--all-ip-addresses` | Alle konfigurierten IP-Adressen ausgeben (ohne Loopback und IPv6-Link-Local) |
| `-i`, `--ip-address` | Die Adresse(n) ausgeben, zu der der Hostname aufgelöst wird |
| `-A`, `--all-fqdns` | Die FQDNs aller konfigurierten Adressen ausgeben |
| `-F`, `--file DATEI` | Den zu setzenden Hostnamen aus `DATEI` lesen |

## Beispiele

**Den Hostnamen anzeigen:**

```bash
hostname
```

```text
tuxcodex-srv
```

**Den vollständigen Domainnamen anzeigen:**

```bash
hostname -f
```

```text
tuxcodex-srv.example.com
```

**Alle IP-Adressen des Servers anzeigen:**

```bash
hostname -I
```

```text
192.0.2.10 2001:db8::10
```

**Die Adresse anzeigen, zu der der Hostname aufgelöst wird:**

```bash
hostname -i
```

```text
127.0.1.1
```

**Den Hostnamen bis zum nächsten Neustart ändern:**

```bash
sudo hostname test-srv
hostname
```

```text
test-srv
```

<!-- SCREENSHOT: assets/screenshots/01-orientation/hostname.png -->

## Wann brauche ich das?

- Um sicherzugehen, dass du auf dem richtigen Server bist, bevor du etwas änderst
- Um mit `hostname -I` schnell die IP-Adressen des Servers zu sehen, ohne dich durch die
  Ausgabe von `ip address` zu lesen
- Um zu prüfen, ob der FQDN stimmt – darauf verlassen sich Mailserver, Zertifikate und
  manche Monitoring-Agenten
- In Skripten und Logmeldungen, die den Maschinennamen enthalten sollen

!!! tip "Schnell die IP herausfinden"
    `hostname -I` ist der schnellste Weg zu den Adressen eines Servers – etwa wenn du an
    der Konsole sitzt und die IP für SSH brauchst.

!!! warning "`-i` zeigt unter Debian `127.0.1.1`"
    `hostname -i` löst nur den Hostnamen auf, und Debian trägt ihn in `/etc/hosts` mit
    `127.0.1.1` ein. Für die echten Adressen nimm `hostname -I`.

!!! warning "Änderungen sind nicht dauerhaft"
    `hostname NAME` ändert den Namen nur bis zum nächsten Neustart. Dauerhaft änderst du
    ihn mit `hostnamectl hostname NAME` – und passt zusätzlich den Eintrag in
    `/etc/hosts` an.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| Paket | `hostname` (immer installiert) | `inetutils` (nicht immer installiert) |
| `-I`, `-A` | vorhanden | nicht vorhanden |

Auf minimalen Arch-Systemen fehlt `hostname` unter Umständen. Nimm dann `hostnamectl`
oder `cat /etc/hostname` und für die IP-Adressen `ip -brief address`.

## Verwandte Befehle

[hostnamectl](hostnamectl.md) · [whoami](whoami.md) · [id](id.md)
