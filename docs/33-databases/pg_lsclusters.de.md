# pg_lsclusters

> Listet alle PostgreSQL-Cluster auf dem Server mit Version, Port, Zustand und Datenverzeichnis. Nur unter Debian und Ubuntu.

![pg_lsclusters output](../assets/screenshots/33-databases/pg_lsclusters.png)

## Syntax

```bash
pg_lsclusters [-h] [--json]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-h` | Keine Überschriftszeile |
| `--json` | Ausgabe als JSON |

Verwandte Werkzeuge aus demselben Paket: `pg_ctlcluster 17 main start|stop|restart|reload`, `pg_createcluster`, `pg_dropcluster` und `pg_upgradecluster` für Versionssprünge. Die systemd-Unit eines Clusters heißt `postgresql@17-main`.

## Beispiele

**Alle Cluster auf dem Server:**

```bash
pg_lsclusters
```

```text
Ver Cluster Port Status Owner    Data directory              Log file
17  main    5432 online postgres /var/lib/postgresql/17/main /var/log/postgresql/postgresql-17-main.log
```

**Nach einem Distributions-Upgrade von Debian 12:**

```bash
pg_lsclusters
```

```text
Ver Cluster Port Status Owner    Data directory              Log file
15  main    5432 online postgres /var/lib/postgresql/15/main /var/log/postgresql/postgresql-15-main.log
17  main    5433 online postgres /var/lib/postgresql/17/main /var/log/postgresql/postgresql-17-main.log
```

Die Daten liegen noch in Version 15 auf Port 5432. Der leere 17er-Cluster steht `pg_upgradecluster` im Weg: Entferne ihn vorher mit `sudo pg_dropcluster 17 main --stop`.

**Einen Cluster stoppen und prüfen:**

```bash
sudo pg_ctlcluster 17 main stop
pg_lsclusters -h
```

```text
17  main    5432 down   postgres /var/lib/postgresql/17/main /var/log/postgresql/postgresql-17-main.log
```

## Wann brauche ich das?

- Um zu sehen, welche PostgreSQL-Versionen auf einem Server laufen und auf welchem Port
- Vor und nach einem Versionssprung, z. B. von 16 auf 17
- Wenn `psql` keine Verbindung bekommt: Läuft der Cluster überhaupt?

!!! tip "Versionssprung unter Debian"
    Nach einem Distributions-Upgrade läuft der alte Cluster weiter. `sudo pg_upgradecluster 16 main`
    kopiert ihn auf die neue Version; prüf die Anwendung und lösch den alten danach mit
    `sudo pg_dropcluster 16 main`.

!!! warning "Zwei Cluster, zwei Ports"
    Wurde die neue Version installiert, während die alte noch läuft, bekommt der neue Cluster
    Port 5433. Anwendungen sprechen weiter mit dem alten auf 5432, bis du die Ports tauschst.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Vorhanden | ja (`postgresql-common`) | ja (`postgresql-common`) | nein: `systemctl status postgresql` | nein: `systemctl status postgresql` |

## Verwandte Befehle

[pg_isready](pg_isready.md) · [psql](psql.md) · [systemctl](../09-systemd/systemctl.md) · [apt](../10-packages/apt.md)
