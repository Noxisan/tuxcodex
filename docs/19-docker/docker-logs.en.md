# docker logs

> Shows the output of a container: everything the service writes to stdout and stderr.

![docker-logs output](../assets/screenshots/19-docker/docker-logs.png)

## Syntax

```bash
docker logs [OPTIONS] CONTAINER
```

## Options

| Option | Description |
|--------|-------------|
| `-f`, `--follow` | Keep showing new lines, like `tail -f` |
| `-n N`, `--tail N` | Only the last N lines |
| `--since TIME` | Only lines since a time, such as `10m`, `2h` or `2026-10-26T09:00` |
| `--until TIME` | Only lines up to a time |
| `-t`, `--timestamps` | Show a timestamp for every line |

## Examples

**The last lines of a container:**

```bash
docker logs --tail 4 web
```

```text
2026/10/26 09:41:52 [notice] 1#1: start worker process 29
2026/10/26 09:41:52 [notice] 1#1: start worker process 30
198.51.100.23 - - [26/Oct/2026:09:42:10 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0" "-"
198.51.100.23 - - [26/Oct/2026:09:42:10 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://tuxdex-srv:8080/" "Mozilla/5.0 (X11; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0" "-"
```

**Follow new lines live:**

```bash
docker logs -f --tail 0 web
```

```text
198.51.100.23 - - [26/Oct/2026:09:42:31 +0000] "GET /status HTTP/1.1" 404 153 "-" "curl/8.14.1" "-"
^C
```

End with ++ctrl+c++; the container keeps running.

**Find out why a container doesn't start:**

```bash
docker logs pg-new
```

```text
Error: Database is uninitialized and superuser password is not specified.
       You must specify POSTGRES_PASSWORD to a non-empty value for the
       superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".
```

**Only the last hour, with timestamps:**

```bash
docker logs -t --since 1h db
```

```text
2026-10-26T09:12:04.517802311Z 2026-10-26 09:12:04.517 UTC [27] LOG:  checkpoint starting: time
2026-10-26T09:12:09.183224019Z 2026-10-26 09:12:09.183 UTC [27] LOG:  checkpoint complete: wrote 47 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=4.611 s, sync=0.021 s, total=4.666 s
```

## When do I need it?

- When a container doesn't start or keeps restarting
- To watch the access log of a web server while testing
- To check what happened during the night

!!! tip "Logs only where the service writes them"
    `docker logs` only shows what the process writes to stdout and stderr. Most official
    images are set up that way. Services that write to files inside the container need a
    volume for their logs.

!!! warning "Logs grow without limit"
    By default, Docker keeps the logs of a container in a JSON file without any size limit.
    Limit them in `/etc/docker/daemon.json` with
    `"log-opts": {"max-size": "10m", "max-file": "3"}` and restart Docker.

## Related commands

[docker ps](docker-ps.md) · [docker exec](docker-exec.md) · [docker compose](docker-compose.md) · [journalctl](../09-systemd/journalctl.md)
