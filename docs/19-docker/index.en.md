---
icon: material/docker
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-docker:{ .tc-hero-icon }

# Docker

Running services in containers: starting and watching containers, building and updating
images, keeping data in volumes and running whole stacks with Docker Compose.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** Images and containers, installation, ports and volumes, a Dockerfile and a compose.yaml :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Running containers

<div class="grid cards" markdown>

-   :material-play-circle-outline:{ .lg .middle } **[docker run](docker-run.md)**

    ---

    Create and start a container.

-   :material-format-list-bulleted:{ .lg .middle } **[docker ps](docker-ps.md)**

    ---

    List running and stopped containers.

-   :material-play:{ .lg .middle } **[docker start](docker-start.md)**

    ---

    Start stopped containers again.

-   :material-stop:{ .lg .middle } **[docker stop](docker-stop.md)**

    ---

    Stop containers cleanly.

-   :material-delete-outline:{ .lg .middle } **[docker rm](docker-rm.md)**

    ---

    Delete containers.

</div>

## Looking inside containers

<div class="grid cards" markdown>

-   :material-text-box-outline:{ .lg .middle } **[docker logs](docker-logs.md)**

    ---

    Show the output of a container.

-   :material-console:{ .lg .middle } **[docker exec](docker-exec.md)**

    ---

    Run a command or shell in a container.

-   :material-magnify:{ .lg .middle } **[docker inspect](docker-inspect.md)**

    ---

    All details as JSON.

-   :material-chart-line:{ .lg .middle } **[docker stats](docker-stats.md)**

    ---

    CPU and memory usage live.

</div>

## Images

<div class="grid cards" markdown>

-   :material-layers-outline:{ .lg .middle } **[docker images](docker-images.md)**

    ---

    List the images on the host.

-   :material-download:{ .lg .middle } **[docker pull](docker-pull.md)**

    ---

    Download an image.

</div>
