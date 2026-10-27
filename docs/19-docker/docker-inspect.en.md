# docker inspect

> Shows all details of a container, image, volume or network as JSON.

![docker-inspect output](../assets/screenshots/19-docker/docker-inspect.png)

## Syntax

```bash
docker inspect [-f TEMPLATE] NAME...
```

## Options

| Option | Description |
|--------|-------------|
| `NAME` | Container, image, volume or network |
| `-f`, `--format TEMPLATE` | Only show selected values, such as `"{{.State.Status}}"` |
| `--type TYPE` | Only search this type: `container`, `image`, `volume`, `network` |
| `-s`, `--size` | Also show the size (containers) |

## Examples

**Status and restart policy:**

```bash
docker inspect -f "{{.State.Status}}, restart: {{.HostConfig.RestartPolicy.Name}}" web
```

```text
running, restart: unless-stopped
```

**Where the data lies:**

```bash
docker inspect -f "{{json .Mounts}}" db
```

```text
[{"Type":"volume","Name":"pgdata","Source":"/var/lib/docker/volumes/pgdata/_data","Destination":"/var/lib/postgresql/data","Driver":"local","Mode":"z","RW":true,"Propagation":""}]
```

**IP address in each network:**

```bash
docker inspect -f "{{range $n, $c := .NetworkSettings.Networks}}{{$n}}: {{$c.IPAddress}} {{end}}" db
```

```text
backend: 172.19.0.2 bridge: 172.17.0.3
```

**The beginning of the full output:**

```bash
docker inspect db | head -20
```

```text
[
    {
        "Id": "f1971ec6019cd6b63bec27e35dd69ceae4e9504716d98e74ba691b6989040cae",
        "Created": "2026-10-26T07:41:05.713664518Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "postgres"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1077,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2026-10-26T07:41:06.299818118Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
```

## When do I need it?

- To find out where the data of a container is stored
- To check the IP address, the restart policy or the environment variables of a container
- To read single values in scripts and monitoring checks

!!! tip "With jq it's easier to read"
    `docker inspect web | jq '.[0].NetworkSettings.Networks'` picks out a part of the JSON
    without templates.

!!! warning "Passwords in plain text"
    `docker inspect` shows all environment variables, including passwords like
    `POSTGRES_PASSWORD`. Be careful when sharing the output. For sensitive values, use
    secrets or files instead of environment variables.

## Related commands

[docker ps](docker-ps.md) · [docker volume](docker-volume.md) · [docker network](docker-network.md) · [jq](../05-text-processing/jq.md)
