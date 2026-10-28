# Understanding databases

Most applications keep their data in a relational database. On Linux servers two of them
are everywhere: **PostgreSQL** and **MariaDB** (the community fork of MySQL; both use the
same commands and protocol).

## PostgreSQL or MariaDB?

| | PostgreSQL | MariaDB / MySQL |
|---|------------|-----------------|
| Client | `psql` | `mariadb` (also available as `mysql`) |
| Port | 5432 | 3306 |
| Admin account | Linux user `postgres` | MariaDB user `root`, as Linux `root` |
| Typical use | Applications with complex data, GIS, many current frameworks | Classic web hosting, WordPress, Nextcloud, many PHP applications |
| Backup | [`pg_dump`](../28-backup/pg_dump.md) | [`mysqldump`](../28-backup/mysqldump.md) |

## Packages and paths

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| PostgreSQL package | `postgresql` (17 in Debian 13) | `postgresql` (16 in 24.04) | `postgresql-server` | `postgresql` |
| First database cluster | created and started on install | created and started on install | `sudo postgresql-setup --initdb`, then enable | `sudo -u postgres initdb -D /var/lib/postgres/data`, then enable |
| PostgreSQL configuration | `/etc/postgresql/17/main/` | `/etc/postgresql/16/main/` | `/var/lib/pgsql/data/` | `/var/lib/postgres/data/` |
| MariaDB package | `mariadb-server` (11.8 in Debian 13) | `mariadb-server` (10.11 in 24.04) | `mariadb-server` | `mariadb` |
| First start | automatic on install | automatic on install | `systemctl enable --now mariadb` | `sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql`, then enable |
| MariaDB configuration | `/etc/mysql/mariadb.conf.d/50-server.cnf` | `/etc/mysql/mariadb.conf.d/50-server.cnf` | `/etc/my.cnf.d/mariadb-server.cnf` | `/etc/my.cnf.d/server.cnf` |

The services are called `postgresql` and `mariadb` everywhere. On Debian and Ubuntu,
PostgreSQL runs as *clusters* such as `17/main`; `pg_lsclusters` lists them.

## How login works

Both servers trust the **Linux user** for local connections over the socket, so the
admin needs no database password:

| | Local admin login | How |
|---|-------------------|-----|
| PostgreSQL | `sudo -u postgres psql` | Method `peer`: the Linux user must have the same name as the database role |
| MariaDB | `sudo mariadb` | Plugin `unix_socket`: Linux `root` is MariaDB `root` |

Applications usually connect over TCP (`-h localhost`) with a **password**. In PostgreSQL
the file `pg_hba.conf` decides which method applies for which connection:

```text
# TYPE  DATABASE  USER  ADDRESS        METHOD
local   all       all                  peer
host    all       all   127.0.0.1/32   scram-sha-256
host    shop      app   192.0.2.0/24   scram-sha-256
```

The rules are read top to bottom; the first matching line wins.

## Users, databases and rights

One application, one database, one user with rights only on that database:

```text
# PostgreSQL
$ sudo -u postgres createuser --pwprompt app
$ sudo -u postgres createdb -O app shop

# MariaDB
$ sudo mariadb
MariaDB [(none)]> CREATE DATABASE wiki CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
MariaDB [(none)]> CREATE USER 'wiki'@'localhost' IDENTIFIED BY 'secret';
MariaDB [(none)]> GRANT ALL PRIVILEGES ON wiki.* TO 'wiki'@'localhost';
```

In MariaDB a user always consists of name **and host**: `'wiki'@'localhost'` and
`'wiki'@'192.0.2.%'` are two different users with their own passwords and rights.

## Access from other machines

By default both servers only listen on `localhost`. For access from the network:

| | Setting | Additionally |
|---|---------|--------------|
| PostgreSQL | `listen_addresses = '*'` in `postgresql.conf` | a `host` line in `pg_hba.conf`, then `systemctl reload postgresql` |
| MariaDB | `bind-address = 0.0.0.0` in the server configuration | a user with a matching host like `'report'@'192.0.2.%'` |

After `listen_addresses` or `bind-address` the service needs a restart. Check the result with
[`ss -tlnp`](../11-network/ss.md).

!!! tip "Keep the database next to the application"
    If the application runs on the same server, leave the database on `localhost`. Then
    the port isn't reachable from outside at all, and you need no firewall rule.

!!! warning "Open ports only for single addresses"
    Ports 5432 and 3306 must never be reachable from the internet. Allow them in the firewall
    only for the application servers, e.g. with
    [`ufw`](../11-network/ufw.md): `sudo ufw allow from 192.0.2.21 to any port 5432 proto tcp`.
