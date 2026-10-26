# host

> Schlägt Namen und Adressen im DNS nach und gibt die Antwort in kurzer, lesbarer Form aus.

![host output](../assets/screenshots/11-network/host.png)

## Syntax

```bash
host [OPTION]... NAME [SERVER]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-t TYP` | Nur diesen Eintragstyp: `A`, `AAAA`, `MX`, `TXT`, `NS`, `SOA` |
| `-a` | Alle Einträge, ausführlich wie bei `dig` |
| `-4`, `-6` | Den DNS-Server über IPv4 oder IPv6 fragen |
| `SERVER` | Diesen DNS-Server statt des eingestellten fragen |

## Beispiele

**Einen Namen nachschlagen:**

```bash
host example.com
```

```text
example.com has address 198.51.100.7
example.com has IPv6 address 2001:db8:1::7
example.com mail is handled by 10 mail.example.com.
```

Ohne Typ zeigt `host` IPv4- und IPv6-Adressen und den Mailserver auf einmal.

**Den Namen zu einer IP-Adresse finden:**

```bash
host 192.0.2.10
```

```text
10.2.0.192.in-addr.arpa domain name pointer tuxcodex-srv.example.com.
```

**Die TXT-Einträge anzeigen, etwa für SPF:**

```bash
host -t TXT example.com
```

```text
example.com descriptive text "v=spf1 mx -all"
```

**Einen bestimmten DNS-Server fragen:**

```bash
host example.com 198.51.100.53
```

```text
Using domain server:
Name: 198.51.100.53
Address: 198.51.100.53#53
Aliases:

example.com has address 198.51.100.7
example.com has IPv6 address 2001:db8:1::7
example.com mail is handled by 10 mail.example.com.
```

**Ein Name, den es nicht gibt:**

```bash
host nosuch.example.com
```

```text
Host nosuch.example.com not found: 3(NXDOMAIN)
```

## Wann brauche ich das?

- Für einen schnellen Test, ob ein Name aufgelöst wird und zu welcher Adresse
- Um den Rückwärtseintrag (PTR) eines Mailservers zu prüfen, den viele Empfänger verlangen
- Wenn `dig` dir mehr Details liefert, als du brauchst

!!! tip "PTR-Einträge für Mailserver"
    Mailserver ohne passenden Rückwärtseintrag werden oft als Spam abgelehnt. `host` mit
    der IP-Adresse des Servers muss seinen Hostnamen liefern, und dieser Name muss wieder
    auf dieselbe Adresse zeigen.

!!! warning "Auch `host` ignoriert `/etc/hosts`"
    Wie `dig` fragt `host` nur den DNS. Mit `getent hosts NAME` siehst du das Ergebnis
    samt `/etc/hosts`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `bind9-host` | `bind9-host` (installiert) | `bind-utils` | `bind` |

## Verwandte Befehle

[dig](dig.md) · [resolvectl](resolvectl.md) · [getent](../07-users-groups/getent.md)
