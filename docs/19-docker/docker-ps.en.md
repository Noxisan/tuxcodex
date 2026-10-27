# docker ps

> Lists the containers: by default the running ones, with `-a` all of them.

![docker-ps output](../assets/screenshots/19-docker/docker-ps.png)

## Syntax

```bash
docker ps [OPTIONS]
```

## Options

| Option | Description |
|--------|-------------|
| `-a`, `--all` | Also show stopped containers |
| `-q`, `--quiet` | Only the container IDs, for use in scripts |
| `-f`, `--filter FILTER` | Filter, such as `status=exited`, `name=web` or `ancestor=nginx:1.28` |
| `--format TEMPLATE` | Choose the columns, such as `"{{.Names}}\t{{.Status}}"` |
| `-s`, `--size` | Also show the size of each container's writable layer |
| `-n N`, `-l` | Only the last N created containers, or the latest one |

## Examples

**Show the running containers:**

```bash
docker ps
```

```text
CONTAINER ID   IMAGE         COMMAND                  CREATED       STATUS       PORTS                                     NAMES
f1971ec6019c   postgres:17   "docker-entrypoint.s…"   2 hours ago   Up 2 hours   5432/tcp                                  db
0d306f9f64bf   nginx:1.28    "/docker-entrypoint.…"   2 hours ago   Up 2 hours   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web
```

**Also show stopped containers:**

```bash
docker ps -a
```

```text
CONTAINER ID   IMAGE         COMMAND                  CREATED       STATUS                  PORTS                                     NAMES
7b2e91c4d0a3   postgres:17   "docker-entrypoint.s…"   3 days ago    Exited (0) 3 days ago                                             pg-test
f1971ec6019c   postgres:17   "docker-entrypoint.s…"   2 hours ago   Up 2 hours              5432/tcp                                  db
0d306f9f64bf   nginx:1.28    "/docker-entrypoint.…"   2 hours ago   Up 2 hours              0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web
```

**Only name and status:**

```bash
docker ps -a --format "{{.Names}}\t{{.Status}}"
```

```text
pg-test Exited (0) 3 days ago
db      Up 2 hours
web     Up 2 hours
```

**IDs of all stopped containers:**

```bash
docker ps -aq -f status=exited
```

```text
7b2e91c4d0a3
```

## When do I need it?

- To see which containers are running and since when
- To find out which ports a container publishes
- To find containers that stopped or keep restarting

!!! tip "Watch the STATUS column"
    `Restarting (1) 5 seconds ago` means the container keeps crashing. The reason is almost
    always in [`docker logs`](docker-logs.md).

## Related commands

[docker run](docker-run.md) · [docker stats](docker-stats.md) · [docker inspect](docker-inspect.md) · [docker logs](docker-logs.md)
