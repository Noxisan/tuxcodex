# Understanding caches and message queues

Many applications need two helpers next to their database: a **cache** that keeps
frequently used data in memory, and a **message broker** that passes jobs between
programs. On Linux servers that's usually **Redis** and **RabbitMQ**.

## Cache or message broker?

| | Redis / Valkey | RabbitMQ |
|---|----------------|----------|
| Job | Key-value store in RAM: cache, sessions, counters, simple queues | Message broker: queues messages until a worker processes them |
| Data | Keys with values, optionally with an expiry time | Messages in queues, confirmed by the consumer |
| If the server restarts | Data from the last snapshot, or none (pure cache) | Durable queues and persistent messages survive |
| Typical use | PHP sessions, page cache, rate limits, Nextcloud file locking | Order processing, mail sending, background jobs |
| Command line | `redis-cli` | `rabbitmqctl` |

## Redis or Valkey?

In 2024 Redis changed its license. The Linux Foundation then started **Valkey**, a fork
of the last open source version. Both speak the same protocol; applications don't notice
the difference. The commands are called `valkey-cli` and `valkey-server` instead of
`redis-cli` and `redis-server`, with the same options.

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Redis | `redis-server` (8.0 in Debian 13) | `redis-server` (7.0 in 24.04) | `redis` (RHEL 9) | no |
| Valkey | `valkey-server` | not in 24.04 | `valkey` (RHEL 10) | `valkey` |
| Service | `redis-server` or `valkey-server` | `redis-server` | `redis` or `valkey` | `valkey` |
| RabbitMQ | `rabbitmq-server` (4.0 in Debian 13) | `rabbitmq-server` | not in the repositories: repository of the RabbitMQ team | `rabbitmq` |

## Ports

| Port | Service |
|------|---------|
| 6379 | Redis / Valkey |
| 5672 | RabbitMQ (AMQP, for applications) |
| 15672 | RabbitMQ web interface and HTTP API (plugin `rabbitmq_management`) |
| 25672, 4369 | RabbitMQ cluster communication and `epmd` (CLI tools) |

## Securing Redis

Redis was built for trusted networks. The important settings in `/etc/redis/redis.conf`:

| Setting | Meaning |
|---------|---------|
| `bind 127.0.0.1 -::1` | Listen only locally (the default on Debian) |
| `protected-mode yes` | Refuse connections from outside as long as no password is set |
| `requirepass …` or ACL users | Password for all clients |
| `maxmemory 512mb` | Upper limit for memory use |
| `maxmemory-policy allkeys-lru` | What happens at the limit: for a cache, delete the least used keys |

With `maxmemory-policy noeviction` (the default) Redis refuses new data when it is full.
That's right for sessions and queues, but wrong for a pure cache.

## Persistence

| Method | How | Data loss on a crash |
|--------|-----|----------------------|
| RDB snapshots | `save 3600 1 300 100 60 10000`: write `dump.rdb` regularly | everything since the last snapshot |
| AOF | `appendonly yes`: log every write | about one second |
| none | `save ""`, `appendonly no` | everything; fine for a pure cache |

## RabbitMQ in five terms

| Term | Meaning |
|------|---------|
| **Virtual host** (vhost) | Separate area with its own queues and rights, like a database per application |
| **Exchange** | Receives messages and distributes them to queues according to rules |
| **Queue** | Holds messages until a consumer fetches and confirms them |
| **Consumer** | The worker process that processes messages |
| **User and permissions** | Per vhost: rights to configure, write and read |

The default user `guest` may only log in from `localhost`. Create your own users with
`rabbitmqctl` and delete `guest` on production systems.

!!! tip "Unix socket for local applications"
    If Redis and the application run on the same server, `unixsocket /run/redis/redis-server.sock`
    plus `port 0` switches off TCP completely. The application connects through the socket file.

!!! warning "Never expose Redis to the internet"
    Open Redis instances are scanned and abused within minutes, for example to write SSH
    keys or crypto miners onto the server. Keep `bind` on `localhost` or allow port 6379
    only for single application servers.
