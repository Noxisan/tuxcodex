---
icon: material/docker
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-docker:{ .tc-hero-icon }

# Docker

Dienste in Containern betreiben: Container starten und beobachten, Images bauen und
aktualisieren, Daten in Volumes ablegen und ganze Stacks mit Docker Compose betreiben.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** Images und Container, Installation, Ports und Volumes, ein Dockerfile und eine compose.yaml :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## Container betreiben

<div class="grid cards" markdown>

-   :material-play-circle-outline:{ .lg .middle } **[docker run](docker-run.md)**

    ---

    Einen Container anlegen und starten.

-   :material-format-list-bulleted:{ .lg .middle } **[docker ps](docker-ps.md)**

    ---

    Laufende und gestoppte Container auflisten.

-   :material-play:{ .lg .middle } **[docker start](docker-start.md)**

    ---

    Gestoppte Container wieder starten.

-   :material-stop:{ .lg .middle } **[docker stop](docker-stop.md)**

    ---

    Container sauber stoppen.

-   :material-delete-outline:{ .lg .middle } **[docker rm](docker-rm.md)**

    ---

    Container löschen.

</div>

## In Container hineinschauen

<div class="grid cards" markdown>

-   :material-text-box-outline:{ .lg .middle } **[docker logs](docker-logs.md)**

    ---

    Die Ausgabe eines Containers zeigen.

-   :material-console:{ .lg .middle } **[docker exec](docker-exec.md)**

    ---

    Einen Befehl oder eine Shell im Container ausführen.

-   :material-magnify:{ .lg .middle } **[docker inspect](docker-inspect.md)**

    ---

    Alle Details als JSON.

-   :material-chart-line:{ .lg .middle } **[docker stats](docker-stats.md)**

    ---

    CPU- und Speicherauslastung live.

</div>

## Images

<div class="grid cards" markdown>

-   :material-layers-outline:{ .lg .middle } **[docker images](docker-images.md)**

    ---

    Die Images auf dem Host auflisten.

-   :material-download:{ .lg .middle } **[docker pull](docker-pull.md)**

    ---

    Ein Image herunterladen.

-   :material-hammer-wrench:{ .lg .middle } **[docker build](docker-build.md)**

    ---

    Ein Image aus einem Dockerfile bauen.

-   :material-upload:{ .lg .middle } **[docker push](docker-push.md)**

    ---

    Ein Image in eine Registry hochladen.

-   :material-layers-remove:{ .lg .middle } **[docker rmi](docker-rmi.md)**

    ---

    Images löschen.

</div>

## Daten und Netzwerk

<div class="grid cards" markdown>

-   :material-database-outline:{ .lg .middle } **[docker volume](docker-volume.md)**

    ---

    Speicher, der den Container überlebt.

-   :material-lan:{ .lg .middle } **[docker network](docker-network.md)**

    ---

    Netzwerke zwischen Containern.

</div>

## Stacks und Aufräumen

<div class="grid cards" markdown>

-   :material-file-cog-outline:{ .lg .middle } **[docker compose](docker-compose.md)**

    ---

    Mehrere Container aus einer compose.yaml betreiben.

</div>
