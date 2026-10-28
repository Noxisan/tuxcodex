# redis-benchmark

> Misst, wie viele Anfragen pro Sekunde ein Redis- oder Valkey-Server schafft und mit welcher Latenz.

![redis-benchmark output](../assets/screenshots/34-caches-queues/redis-benchmark.png)

## Syntax

```bash
redis-benchmark [-h HOST] [-p PORT] [-n ANFRAGEN] [-c CLIENTS] [-d BYTES] [-t TESTS] [-q]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n N` | Anzahl der Anfragen pro Test, Standard 100000 |
| `-c N` | Parallele Clients, Standard 50 |
| `-d BYTES` | Größe der Werte für `SET` und `GET`, Standard 3 |
| `-t TESTS` | Nur diese Tests, z. B. `set,get,incr,lpush` |
| `-P N` | Pipeline: N Befehle auf einmal schicken |
| `-q` | Nur eine Ergebniszeile pro Test |
| `--csv` | Ausgabe als CSV |

Die Tests schreiben Schlüssel wie `key:__rand_int__` in die Datenbank. Lass sie gegen eine Testinstanz oder eine leere Datenbanknummer laufen (`--dbnum 15`).

## Beispiele

**Ein schneller Überblick:**

```bash
redis-benchmark -q -n 20000 -t set,get,incr,lpush --dbnum 15
```

```text
SET: 47732.70 requests per second, p50=0.511 msec
GET: 49504.95 requests per second, p50=0.495 msec
INCR: 50000.00 requests per second, p50=0.487 msec
LPUSH: 48543.69 requests per second, p50=0.503 msec
```

**GET mit 1-KB-Werten und der Verteilung der Latenz:**

```bash
redis-benchmark -n 10000 -t get -c 50 -d 1024 --dbnum 15 | tail -6
```

```text
Summary:
  throughput summary: 45454.55 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.561     0.152     0.527     0.791     1.247     3.519
```

**Schneller mit Pipeline:**

```bash
redis-benchmark -q -n 100000 -t get -P 16 --dbnum 15
```

```text
GET: 409836.06 requests per second, p50=1.623 msec
```

Mit 16 Befehlen pro Hin- und Rückweg steigt der Durchsatz etwa auf das Achtfache. Anwendungen erreichen denselben Effekt mit Pipelining in ihrer Redis-Bibliothek.

**Der Server ist nicht erreichbar:**

```bash
redis-benchmark -q -h 192.0.2.22 -n 1000 -t ping
```

```text
Could not connect to Redis at 192.0.2.22:6379: Connection refused
```

## Wann brauche ich das?

- Um zu prüfen, ob ein neuer Server oder eine neue Konfiguration schnell genug ist
- Um Redis über TCP mit einem Unix-Socket oder Redis mit Valkey zu vergleichen
- Um zu erkennen, ob eine Verlangsamung an Redis oder am Netz liegt

!!! tip "Vom Anwendungsserver aus messen"
    Lass den Benchmark einmal auf dem Redis-Server und einmal vom Anwendungsserver aus laufen.
    Weichen die Zahlen stark ab, ist das Netz der Engpass, nicht Redis.

!!! warning "Nicht auf einer Produktivinstanz"
    Der Benchmark erzeugt Last und schreibt eigene Schlüssel. Auf einem Produktivserver bremst
    das die Anwendung und kann echte Cache-Einträge aus dem Speicher drängen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `redis-tools` (oder `valkey-tools`) | `redis-tools` | `redis` (RHEL 9), `valkey` (RHEL 10) | `valkey` |
| Befehl | `redis-cli` (oder `valkey-cli`) | `redis-cli` | `redis-cli` oder `valkey-cli` | `valkey-cli` |

## Verwandte Befehle

[redis-cli](redis-cli.md) · [ab](../29-webserver/ab.md) · [ping](../11-network/ping.md)
