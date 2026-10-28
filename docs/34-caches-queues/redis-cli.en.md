# redis-cli

> The command line client of Redis and Valkey: run commands, read state and memory, search keys and watch live traffic.

![redis-cli output](../assets/screenshots/34-caches-queues/redis-cli.png)

## Syntax

```bash
redis-cli [-h HOST] [-p PORT] [-n DB] [COMMAND [ARGS]]
```

## Options

| Option | Description |
|--------|-------------|
| `-h HOST`, `-p PORT` | Server and port, default `127.0.0.1:6379` |
| `-s SOCKET` | Connect through a Unix socket |
| `-n DB` | Database number, default `0` |
| `--user`, `--pass` | Log in (better: environment variable `REDISCLI_AUTH`) |
| `--scan --pattern 'P'` | Find keys step by step, without blocking the server |
| `--bigkeys`, `--memkeys` | Find the largest keys |
| `--latency` | Measure the response time continuously |

Important commands: `PING`, `INFO [SECTION]`, `DBSIZE`, `GET`/`SET`, `TTL`, `DEL`, `CONFIG GET`, `MONITOR`, `SLOWLOG GET`. Without a command `redis-cli` starts an interactive shell.

## Examples

**Does Redis answer:**

```bash
redis-cli ping
```

```text
PONG
```

**Memory use and limit:**

```bash
redis-cli INFO memory | grep -E '^(used_memory_human|used_memory_peak_human|maxmemory_human|maxmemory_policy)'
```

```text
used_memory_human:212.47M
used_memory_peak_human:248.03M
maxmemory_human:512.00M
maxmemory_policy:allkeys-lru
```

**How many keys, how many with an expiry time:**

```bash
redis-cli INFO keyspace
```

```text
# Keyspace
db0:keys=48213,expires=47904,avg_ttl=1795341,subexpiry=0
```

**Look at a key and its lifetime:**

```bash
redis-cli GET session:4711
redis-cli TTL session:4711
```

```text
"nox"
(integer) 3512
```

`TTL` gives the remaining seconds. `-1` means no expiry, `-2` that the key doesn't exist.

**Find and delete keys by pattern:**

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

**A password is set:**

```bash
redis-cli ping
REDISCLI_AUTH='secret' redis-cli ping
```

```text
NOAUTH Authentication required.
PONG
```

**Watch live which commands arrive:**

```bash
redis-cli MONITOR
```

```text
OK
1793007737.736306 [0 127.0.0.1:58680] "SET" "session:4712" "anna" "EX" "3600"
1793007737.739543 [0 127.0.0.1:58694] "GET" "session:4711"
```

**Check the persistence:**

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

## When do I need it?

- To check whether Redis answers and how much memory it uses
- To find out why an application doesn't find its sessions or cache entries
- To delete stale keys after a deployment

!!! tip "`--scan` instead of `KEYS *`"
    `KEYS *` goes through all keys at once and blocks Redis meanwhile; with millions of keys
    that takes seconds. `redis-cli --scan --pattern 'cache:*'` does the same in small steps.

!!! warning "`MONITOR` costs performance"
    `MONITOR` shows every command of every client. On a busy server that halves the
    throughput. Use it only briefly and end it with `Ctrl` + `C`.

!!! danger "`FLUSHALL` deletes everything"
    `FLUSHALL` empties all databases of the instance, `FLUSHDB` the current one. There is no
    confirmation and no undo. Many setups rename these commands in `redis.conf` for that reason.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `redis-tools` (or `valkey-tools`) | `redis-tools` | `redis` (RHEL 9), `valkey` (RHEL 10) | `valkey` |
| Command | `redis-cli` (or `valkey-cli`) | `redis-cli` | `redis-cli` or `valkey-cli` | `valkey-cli` |

## Related commands

[redis-benchmark](redis-benchmark.md) · [ss](../11-network/ss.md) · [systemctl](../09-systemd/systemctl.md) · [xargs](../05-text-processing/xargs.md)
