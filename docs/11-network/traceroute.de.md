# traceroute

> Zeigt den Weg, den Pakete zu einem Host nehmen, Router für Router, und wie lange jeder Schritt dauert.

![traceroute output](../assets/screenshots/11-network/traceroute.png)

## Syntax

```bash
traceroute [OPTION]... HOST
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n` | Routernamen nicht auflösen, nur Adressen zeigen (schneller) |
| `-m ANZAHL` | Höchstzahl an Sprüngen, Standard `30` |
| `-q ANZAHL` | Messungen pro Sprung, Standard `3` |
| `-T -p PORT` | TCP zu diesem Port statt UDP nutzen, kommt durch viele Firewalls |
| `-I` | ICMP wie `ping` nutzen |
| `-4`, `-6` | IPv4 oder IPv6 erzwingen |

## Beispiele

**Den Weg zu einem Host anzeigen:**

```bash
traceroute example.com
```

```text
traceroute to example.com (198.51.100.7), 30 hops max, 60 byte packets
 1  _gateway (192.0.2.1)  0.312 ms  0.287 ms  0.301 ms
 2  core1.isp.example.net (198.51.100.1)  1.104 ms  1.092 ms  1.123 ms
 3  * * *
 4  ix1.fra.example.net (198.51.100.65)  4.871 ms  4.902 ms  4.855 ms
 5  edge2.example.net (198.51.100.129)  11.402 ms  11.388 ms  11.421 ms
 6  example.com (198.51.100.7)  11.618 ms  11.703 ms  11.592 ms
```

Jede Zeile ist ein Router. Die drei Zeiten sind drei Messungen. `* * *` heißt: Dieser
Router antwortet nicht, was normal ist, solange die folgenden Sprünge funktionieren.

**Schneller, ohne Namensauflösung:**

```bash
traceroute -n example.com
```

```text
traceroute to example.com (198.51.100.7), 30 hops max, 60 byte packets
 1  192.0.2.1  0.298 ms  0.276 ms  0.290 ms
 2  198.51.100.1  1.098 ms  1.101 ms  1.087 ms
 3  * * *
 4  198.51.100.65  4.866 ms  4.893 ms  4.849 ms
 5  198.51.100.129  11.395 ms  11.384 ms  11.410 ms
 6  198.51.100.7  11.602 ms  11.698 ms  11.587 ms
```

**Den Weg zu einem Webserver durch Firewalls testen:**

```bash
sudo traceroute -T -p 443 example.com
```

```text
traceroute to example.com (198.51.100.7), 30 hops max, 60 byte packets
 1  _gateway (192.0.2.1)  0.305 ms  0.281 ms  0.296 ms
 2  core1.isp.example.net (198.51.100.1)  1.110 ms  1.097 ms  1.119 ms
 3  ix1.fra.example.net (198.51.100.65)  4.880 ms  4.871 ms  4.902 ms
 4  edge2.example.net (198.51.100.129)  11.398 ms  11.405 ms  11.391 ms
 5  example.com (198.51.100.7)  11.612 ms  11.701 ms  11.590 ms
```

**Der Weg endet irgendwo:**

```bash
traceroute -n -m 8 198.51.100.200
```

```text
traceroute to 198.51.100.200 (198.51.100.200), 8 hops max, 60 byte packets
 1  192.0.2.1  0.301 ms  0.284 ms  0.292 ms
 2  198.51.100.1  1.101 ms  1.096 ms  1.090 ms
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  * * *
```

Ab Sprung 3 antwortet nichts mehr: Die Pakete gehen hinter `198.51.100.1` verloren, etwa
an einer Firewall oder einer kaputten Route.

## Wann brauche ich das?

- Wenn ein Host nicht erreichbar ist: Bis zu welchem Router kommen die Pakete?
- Wenn eine Verbindung langsam ist: An welchem Sprung springt die Zeit nach oben?
- Um deinem Hoster oder Provider zu zeigen, wo genau ein Problem auftritt

!!! tip "`mtr` für eine längere Messung"
    `traceroute` zeigt eine einzelne Momentaufnahme. [`mtr`](mtr.md) wiederholt die
    Messung fortlaufend und zeigt den Paketverlust pro Sprung.

!!! warning "Nicht vorinstalliert"
    Installiere das Paket `traceroute` mit dem Paketmanager deiner Distribution.
    `tracepath` erledigt Ähnliches und ist oft schon da, siehe Tabelle unten.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| `traceroute` | Paket `traceroute` | Paket `traceroute` | Paket `traceroute` | Paket `traceroute` |
| `tracepath` | Paket `iputils-tracepath` | Paket `iputils-tracepath` | Teil von `iputils` | Teil von `iputils` |

## Verwandte Befehle

[ping](ping.md) · [mtr](mtr.md) · [ip](ip.md)
