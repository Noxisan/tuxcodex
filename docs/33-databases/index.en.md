---
title: "Databases"
icon: material/database-outline
hide:
  - toc
---

<div class="tc-hero tc-hero--chapter" markdown>

:material-database-outline:{ .tc-hero-icon }

# Databases

Running PostgreSQL and MariaDB: connecting, creating users and databases, granting
rights, checking whether the server is alive and securing a fresh installation.

</div>

[:material-school-outline:{ .tc-basics-icon } **Basics:** PostgreSQL or MariaDB, packages and paths per distribution, how login works, users and rights, access from other machines :material-arrow-right:{ .tc-basics-arrow }](basics.md){ .tc-basics }

## PostgreSQL

<div class="grid cards" markdown>

-   :material-console-line:{ .lg .middle } **[psql](psql.md)**

    ---

    Connect, run SQL, inspect databases and roles.

-   :material-account-plus-outline:{ .lg .middle } **[createuser](createuser.md)**

    ---

    Create a PostgreSQL role.

-   :material-database-plus-outline:{ .lg .middle } **[createdb](createdb.md)**

    ---

    Create a PostgreSQL database.

-   :material-heart-pulse:{ .lg .middle } **[pg_isready](pg_isready.md)**

    ---

    Does the server accept connections?

-   :material-format-list-bulleted-square:{ .lg .middle } **[pg_lsclusters](pg_lsclusters.md)**

    ---

    Clusters, versions and ports (Debian, Ubuntu).

</div>

## MariaDB

<div class="grid cards" markdown>

-   :material-console-line:{ .lg .middle } **[mariadb](mariadb.md)**

    ---

    Connect, run SQL, manage users and rights.

-   :material-database-cog-outline:{ .lg .middle } **[mariadb-admin](mariadb-admin.md)**

    ---

    Ping, status, processes and variables.

-   :material-shield-check-outline:{ .lg .middle } **[mariadb-secure-installation](mariadb-secure-installation.md)**

    ---

    Secure a fresh installation.

</div>
