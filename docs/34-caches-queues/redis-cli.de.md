# redis-cli

> Der Kommandozeilen-Client von Redis und Valkey: Befehle ausführen, Zustand und Speicher lesen, Schlüssel suchen und den Verkehr live verfolgen.

![redis-cli output](../assets/screenshots/34-caches-queues/redis-cli.png)

## Syntax

```bash
redis-cli [-h HOST] [-p PORT] [-n DB] [BEFEHL [ARGUMENTE]]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-h HOST`, `-p PORT` | Server und Port, Standard `127.0.0.1:6379` |
| `-s SOCKET` | Über einen Unix-Socket verbinden |
| `-n DB` | Nummer der Datenbank, Standard `0` |
| `--user`, `--pass` | Anmelden (besser: Umgebungsvariable `REDISCLI_AUTH`) |
| `--scan --pattern 'M'` | Schlüssel schrittweise suchen, ohne den Server zu blockieren |
| `--bigkeys`, `--memkeys` | Die größten Schlüssel finden |
| `--latency` | Die Antwortzeit laufend messen |

Wichtige Befehle: `PING`, `INFO [ABSCHNITT]`, `DBSIZE`, `GET`/`SET`, `TTL`, `DEL`, `CONFIG GET`, `MONITOR`, `SLOWLOG GET`. Ohne Befehl startet `redis-cli` eine interaktive Shell.

## Beispiele

**Antwortet Redis:**

```bash
redis-cli ping
```

```text
PONG
```

**Speicherverbrauch und Grenze:**

```bash
redis-cli INFO memory | grep -E '^(used_memory_human|used_memory_peak_human|maxmemory_human|maxmemory_policy)'
```

```text
used_memory_human:212.47M
used_memory_peak_human:248.03M
maxmemory_human:512.00M
maxmemory_policy:allkeys-lru
```

**Wie viele Schlüssel, wie viele mit Ablaufzeit:**

```bash
redis-cli INFO keyspace
```

```text
# Keyspace
db0:keys=48213,expires=47904,avg_ttl=1795341,subexpiry=0
```

**Einen Schlüssel und seine Lebensdauer ansehen:**

```bash
redis-cli GET session:4711
redis-cli TTL session:4711
```

```text
"nox"
(integer) 3512
```

`TTL` nennt die verbleibenden Sekunden. `-1` heißt keine Ablaufzeit, `-2`, dass es den Schlüssel nicht gibt.

**Schlüssel nach Muster finden und löschen:**

```bash
redis-cli --scan --pattern 'cache:page:*' | head -3
redis-cli --scan --pattern 'cache:page:*' | xargs redis-cli DEL
```

```text
cache:page:35
cache:page:14
cache:page:26
(integer) 50
```

**Ein Passwort ist gesetzt:**

```bash
redis-cli ping
REDISCLI_AUTH='secret' redis-cli ping
```

```text
NOAUTH Authentication required.
PONG
```

**Live verfolgen, welche Befehle ankommen:**

```bash
redis-cli MONITOR
```

```text
OK
1793007737.736306 [0 127.0.0.1:58680] "SET" "session:4712" "anna" "EX" "3600"
1793007737.739543 [0 127.0.0.1:58694] "GET" "session:4711"
```

**Die Persistenz prüfen:**

```bash
redis-cli INFO persistence | grep -E '^(rdb_last_bgsave_status|rdb_changes_since_last_save|aof_enabled)'
redis-cli CONFIG GET save
```

```text
rdb_changes_since_last_save:52
rdb_last_bgsave_status:ok
aof_enabled:0
1) "save"
2) "3600 1 300 100 60 10000"
```

## Wann brauche ich das?

- Um zu prüfen, ob Redis antwortet und wie viel Speicher es belegt
- Um herauszufinden, warum eine Anwendung ihre Sitzungen oder Cache-Einträge nicht findet
- Um nach einem Deployment veraltete Schlüssel zu löschen

!!! tip "`--scan` statt `KEYS *`"
    `KEYS *` geht alle Schlüssel auf einmal durch und blockiert Redis währenddessen; bei
    Millionen Schlüsseln dauert das Sekunden. `redis-cli --scan --pattern 'cache:*'` macht
    dasselbe in kleinen Schritten.

!!! warning "`MONITOR` kostet Leistung"
    `MONITOR` zeigt jeden Befehl jedes Clients. Auf einem ausgelasteten Server halbiert das den
    Durchsatz. Nutze es nur kurz und beende es mit `Strg` + `C`.

!!! danger "`FLUSHALL` löscht alles"
    `FLUSHALL` leert alle Datenbanken der Instanz, `FLUSHDB` die aktuelle. Es gibt keine
    Rückfrage und kein Zurück. Viele Setups benennen diese Befehle deshalb in `redis.conf` um.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `redis-tools` (oder `valkey-tools`) | `redis-tools` | `redis` (RHEL 9), `valkey` (RHEL 10) | `valkey` |
| Befehl | `redis-cli` (oder `valkey-cli`) | `redis-cli` | `redis-cli` oder `valkey-cli` | `valkey-cli` |

## Verwandte Befehle

[redis-benchmark](redis-benchmark.md) · [ss](../11-network/ss.md) · [systemctl](../09-systemd/systemctl.md) · [xargs](../05-text-processing/xargs.md)
