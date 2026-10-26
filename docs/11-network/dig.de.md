# dig

> Fragt DNS-Server direkt und zeigt ihre vollständige Antwort: welche Adresse ein Name hat, welcher Mailserver zuständig ist und welcher DNS-Server geantwortet hat.

![dig output](../assets/screenshots/11-network/dig.png)

## Syntax

```bash
dig [@SERVER] NAME [TYP] [+OPTION]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `TYP` | Eintragstyp: `A` (Standard), `AAAA`, `MX`, `TXT`, `NS`, `CNAME`, `SOA` |
| `@SERVER` | Diesen DNS-Server statt des eingestellten fragen |
| `+short` | Nur die Antwort ausgeben |
| `-x ADRESSE` | Rückwärtssuche: welcher Name zu einer IP-Adresse gehört |
| `+trace` | Die Auflösung von den Root-Servern abwärts verfolgen |
| `+noall +answer` | Nur den Antwortteil im vollen Format ausgeben |

## Beispiele

**Die Adresse eines Namens nachschlagen:**

```bash
dig example.com
```

```text
; <<>> DiG 9.20.30-1~deb13u1-Debian <<>> example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59767
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            3600    IN      A       198.51.100.7

;; Query time: 12 msec
;; SERVER: 192.0.2.53#53(192.0.2.53) (UDP)
;; WHEN: Mon Oct 26 10:42:17 CET 2026
;; MSG SIZE  rcvd: 56
```

| Teil | Bedeutung |
|------|-----------|
| `status: NOERROR` | Der Name existiert. `NXDOMAIN` heißt: Er existiert nicht |
| `ANSWER SECTION` | Die Antwort: Name, TTL in Sekunden, Klasse, Typ, Wert |
| `SERVER` | Der DNS-Server, der geantwortet hat |
| `Query time` | Wie lange die Antwort gedauert hat |

**Nur die Antwort, für Skripte:**

```bash
dig +short example.com AAAA
```

```text
2001:db8:1::7
```

**Den Mailserver einer Domain finden:**

```bash
dig +short example.com MX
```

```text
10 mail.example.com.
```

**Einen bestimmten DNS-Server fragen:**

```bash
dig @198.51.100.53 example.com +noall +answer
```

```text
example.com.            3600    IN      A       198.51.100.7
```

Geben zwei DNS-Server unterschiedliche Antworten, ist eine Änderung noch nicht überall
angekommen, oder ein Server ist falsch eingerichtet.

**Den Namen zu einer IP-Adresse finden:**

```bash
dig +short -x 198.51.100.7
```

```text
example.com.
```

**Ein Name, den es nicht gibt:**

```bash
dig nosuch.example.com | grep status
```

```text
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 40112
```

## Wann brauche ich das?

- Nach der Änderung eines DNS-Eintrags: Ist die Änderung angekommen?
- Wenn Mail nicht ankommt: Stimmen die `MX`- und `TXT`-Einträge (SPF)?
- Wenn ein Name auf verschiedenen Servern unterschiedlich aufgelöst wird

!!! tip "Auf die TTL achten"
    Die Zahl nach dem Namen ist die TTL: wie viele Sekunden ein DNS-Server die Antwort
    zwischenspeichern darf. Nach einer Änderung können alte Antworten so lange bestehen
    bleiben.

!!! warning "`dig` ignoriert `/etc/hosts`"
    `dig` fragt immer den DNS. Einträge aus `/etc/hosts` tauchen nicht auf. Was Programme
    wirklich nutzen, zeigt `getent hosts example.com`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `bind9-dnsutils` | `bind9-dnsutils` (installiert) | `bind-utils` | `bind` |

## Verwandte Befehle

[host](host.md) · [resolvectl](resolvectl.md) · [getent](../07-users-groups/getent.md) · [ping](ping.md)
