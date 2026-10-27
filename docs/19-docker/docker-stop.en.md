# docker stop

> Stops running containers cleanly: first with SIGTERM, after a grace period with SIGKILL.

![docker-stop output](../assets/screenshots/19-docker/docker-stop.png)

## Syntax

```bash
docker stop [-t SECONDS] CONTAINER...
```

## Options

| Option | Description |
|--------|-------------|
| `CONTAINER` | Name or ID, several are possible |
| `-t`, `--timeout SECONDS` | How long to wait before SIGKILL (default 10) |
| `-s`, `--signal SIGNAL` | Send a different signal instead of SIGTERM |

`docker kill CONTAINER` stops immediately with SIGKILL, without a grace period.

## Examples

**Stop a container:**

```bash
docker stop web
docker ps -a -f name=web --format "{{.Names}}: {{.Status}}"
```

```text
web
web: Exited (0) 1 second ago
```

**Give a database a minute:**

```bash
docker stop -t 60 db
```

```text
db
```

**Stop all running containers:**

```bash
docker stop $(docker ps -q)
```

```text
f1971ec6019c
0d306f9f64bf
```

**Make nginx reload its configuration without stopping:**

```bash
docker kill -s HUP web
```

```text
web
```

## When do I need it?

- Before maintenance, a backup of the data or an update of the host
- To stop a service that is no longer needed
- To stop all containers before a reboot: `docker stop $(docker ps -q)`

!!! tip "Give databases more time"
    Databases need a moment to write their data cleanly. For them, use a longer timeout,
    such as `docker stop -t 60 db`.

!!! warning "Restart policy and stop"
    A container stopped with `docker stop` stays stopped, even with `--restart always`,
    until the Docker service itself restarts. With `unless-stopped`, it stays stopped after
    a reboot too.

## Related commands

[docker start](docker-start.md) · [docker rm](docker-rm.md) · [docker ps](docker-ps.md) · [docker compose](docker-compose.md)
