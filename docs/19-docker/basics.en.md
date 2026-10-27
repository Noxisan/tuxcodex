# Understanding Docker

A container runs a service with everything it needs (libraries, configuration, runtime)
isolated from the rest of the system, but without the overhead of a virtual machine. All
containers share the kernel of the host.

## Image and container

| Term | What it is | Comparable to |
|------|------------|---------------|
| **Image** | Read-only template: a file system plus the command to start | A package or an installation medium |
| **Container** | A running (or stopped) instance of an image, with its own writable layer | A running process |
| **Registry** | Server that stores images, such as Docker Hub or your own registry | A package repository |
| **Volume** | Storage managed by Docker that survives the container | A mounted disk |

From one image you can start as many containers as you like. Deleting a container deletes
everything it wrote, except what lies in a volume.

## Installation

The packages in the distributions are often older and named differently. On servers, the
official repository from Docker is the usual choice. The example server `tuxdex-srv` uses
Docker CE from there, see [docs.docker.com/engine/install](https://docs.docker.com/engine/install/).

```text
$ sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
$ sudo systemctl enable --now docker
$ sudo docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

To work without `sudo`, add your user to the group `docker` and log in again:
`sudo usermod -aG docker nox`.

## Ports and volumes

```text
docker run -d --name web -p 8080:80 -v /srv/www:/usr/share/nginx/html:ro nginx:1.28
                          ─────┬───  ──────────────────┬──────────────────
                               │                       └─ host directory : container directory (read-only)
                               └─ host port : container port
```

| Kind of storage | Example | Use for |
|-----------------|---------|---------|
| Named volume | `-v pgdata:/var/lib/postgresql/data` | Data of databases and services, managed by Docker |
| Bind mount | `-v /srv/www:/usr/share/nginx/html:ro` | Files you edit on the host, such as configuration or a website |

## A Dockerfile

A `Dockerfile` describes how an image is built, step by step:

```text
FROM nginx:1.28
COPY index.html /usr/share/nginx/html/
HEALTHCHECK CMD curl -fs http://localhost/ || exit 1
```

[`docker build`](docker-build.md) turns it into an image.

## A compose.yaml

For services with several containers, a `compose.yaml` describes everything in one file.
`/srv/status/compose.yaml`:

```text
services:
  web:
    image: nginx:1.28
    ports:
      - "8080:80"
    restart: unless-stopped
  db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - dbdata:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  dbdata:
```

[`docker compose up -d`](docker-compose.md) starts both containers, a shared network and the
volume. The containers reach each other by their service names, here `web` and `db`.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package in the distribution | `docker.io` | `docker.io` | none, `podman` instead | `docker` |
| Official Docker repository | yes (`docker-ce`) | yes (`docker-ce`) | yes (`docker-ce`) | no |
| Compose | `docker-compose-plugin` | `docker-compose-plugin` | `docker-compose-plugin` | `docker-compose` |
| Alternative | `podman` | `podman` | `podman` (preferred by Red Hat) | `podman` |

!!! tip "Pin the image version"
    `nginx:1.28` is predictable, `nginx` (meaning `nginx:latest`) can be a new major version
    after the next pull. On servers, always use a version tag.

!!! danger "The group docker is root"
    Anyone in the group `docker` can start a container that mounts `/` from the host and
    thereby gains full root access. Only add trusted admins to this group.
