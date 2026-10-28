---
title: "Datenbanken"
icon: material/database-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-database-outline:{ .tc-hero-icon }

# Datenbanken

PostgreSQL und MariaDB betreiben: verbinden, Benutzer und Datenbanken anlegen, Rechte
vergeben, prüfen, ob der Server lebt, und eine frische Installation absichern.

</div>

[:material-school-outline:{ .tc-basics-icon } **Grundlagen:** PostgreSQL oder MariaDB, Pakete und Pfade je Distribution, wie die Anmeldung funktioniert, Benutzer und Rechte, Zugriff von anderen Rechnern :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## PostgreSQL

<div class="grid cards" markdown>

-   :material-console-line:{ .lg .middle } **[psql](psql.md)**

    ---

    Verbinden, SQL ausführen, Datenbanken und Rollen untersuchen.

-   :material-account-plus-outline:{ .lg .middle } **[createuser](createuser.md)**

    ---

    Eine PostgreSQL-Rolle anlegen.

-   :material-database-plus-outline:{ .lg .middle } **[createdb](createdb.md)**

    ---

    Eine PostgreSQL-Datenbank anlegen.

-   :material-heart-pulse:{ .lg .middle } **[pg_isready](pg_isready.md)**

    ---

    Nimmt der Server Verbindungen an?

-   :material-format-list-bulleted-square:{ .lg .middle } **[pg_lsclusters](pg_lsclusters.md)**

    ---

    Cluster, Versionen und Ports (Debian, Ubuntu).

</div>

## MariaDB

<div class="grid cards" markdown>

-   :material-console-line:{ .lg .middle } **[mariadb](mariadb.md)**

    ---

    Verbinden, SQL ausführen, Benutzer und Rechte verwalten.

-   :material-database-cog-outline:{ .lg .middle } **[mariadb-admin](mariadb-admin.md)**

    ---

    Ping, Status, Prozesse und Variablen.

-   :material-shield-check-outline:{ .lg .middle } **[mariadb-secure-installation](mariadb-secure-installation.md)**

    ---

    Eine frische Installation absichern.

</div>

## Aus anderen Kapiteln

<div class="grid cards" markdown>

-   :material-database-export-outline:{ .lg .middle } **[pg_dump](../28-backup/pg_dump.md)**

    ---

    PostgreSQL-Datenbanken sichern. Behandelt im Kapitel Backup.

-   :material-database-export-outline:{ .lg .middle } **[mysqldump](../28-backup/mysqldump.md)**

    ---

    MariaDB- und MySQL-Datenbanken sichern. Behandelt im Kapitel Backup.

-   :material-lan:{ .lg .middle } **[ss](../11-network/ss.md)**

    ---

    Prüfen, auf welcher Adresse die Datenbank lauscht. Behandelt im Kapitel Netzwerk.

-   :material-shield-lock-outline:{ .lg .middle } **[ufw](../11-network/ufw.md)**

    ---

    Den Datenbank-Port nur für Anwendungsserver öffnen. Behandelt im Kapitel Netzwerk.

</div>
