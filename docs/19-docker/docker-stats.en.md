# docker stats

> Shows CPU, memory, network and disk usage of the running containers live.

![docker-stats output](../assets/screenshots/19-docker/docker-stats.png)

## Syntax

```bash
docker stats [OPTIONS] [CONTAINER...]
```

## Options

| Option | Description |
|--------|-------------|
| `CONTAINER` | Only these containers, otherwise all running ones |
| `--no-stream` | Show the values once and exit, instead of updating them |
| `-a`, `--all` | Also list stopped containers |
| `--format TEMPLATE` | Choose the columns, such as `"{{.Name}}\t{{.MemUsage}}"` |

## Examples

**Usage of all running containers:**

```bash
docker stats --no-stream
```

```text
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS
f1971ec6019c   db        0.02%     38.71MiB / 3.82GiB    0.99%     1.42MB / 2.17MB   12.3MB / 81.6MB   7
0d306f9f64bf   web       0.00%     4.836MiB / 3.82GiB    0.12%     3.86MB / 41.2MB   1.02MB / 8.19kB   3
```

**Only name, CPU and memory:**

```bash
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

```text
NAME      CPU %     MEM USAGE / LIMIT
db        0.02%     38.71MiB / 3.82GiB
web       0.00%     4.836MiB / 3.82GiB
```

**A container with a memory limit:**

```bash
docker stats --no-stream web
```

```text
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O           BLOCK I/O         PIDS
0d306f9f64bf   web       0.00%     4.84MiB / 256MiB    1.89%     3.86MB / 41.2MB   1.02MB / 8.19kB   3
```

## When do I need it?

- When the server is slow and you want to know which container is responsible
- To check whether a memory limit is set high enough
- To get a quick overview of the load without a monitoring system

!!! tip "Limit memory"
    A container may use all the memory of the host by default. Limit it with
    `docker run -m 512m` or `mem_limit: 512m` in the `compose.yaml`; the LIMIT column then
    shows the value.

## Related commands

[docker ps](docker-ps.md) · [docker inspect](docker-inspect.md) · [top](../08-processes/top.md) · [docker system](docker-system.md)
