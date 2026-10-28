# Suchserver verstehen

Shops, Wikis, Log-Plattformen und viele Anwendungen nutzen einen Suchserver, um Text in
Millionen von Dokumenten in Millisekunden zu finden. Die beiden verbreiteten sind
**Elasticsearch** und **OpenSearch**.

## Elasticsearch oder OpenSearch?

2021 hat Elastic die Lizenz von Elasticsearch geändert. Amazon hat daraufhin die letzte
Open-Source-Version als **OpenSearch** abgespalten. Beide arbeiten gleich und teilen den
größten Teil der REST-API.

| | Elasticsearch | OpenSearch |
|---|---------------|------------|
| Gepflegt von | Elastic | OpenSearch Software Foundation (Linux Foundation) |
| Weboberfläche | Kibana | OpenSearch Dashboards |
| Sicherheit | eingebaut, seit Version 8 standardmäßig aktiv | Security-Plugin, standardmäßig aktiv |
| Admin-Benutzer | `elastic` | `admin` |
| Werkzeuge in `bin/` | `elasticsearch-reset-password`, `elasticsearch-keystore`, `elasticsearch-plugin` | `opensearch-keystore`, `opensearch-plugin`; Benutzer im Security-Plugin |

## Installation und Pfade

Keiner von beiden steckt in den Paketquellen der Distributionen. Nimm die Paketquelle des
Herstellers oder ein Container-Image.

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Elasticsearch | APT-Paketquelle von Elastic | APT-Paketquelle von Elastic | YUM-Paketquelle von Elastic | AUR oder Container |
| OpenSearch | APT-Paketquelle von OpenSearch | APT-Paketquelle von OpenSearch | YUM-Paketquelle von OpenSearch | AUR oder Container |

| Was | Elasticsearch (Paket) | OpenSearch (Paket) |
|-----|-----------------------|--------------------|
| Programme | `/usr/share/elasticsearch/bin/` | `/usr/share/opensearch/bin/` |
| Konfiguration | `/etc/elasticsearch/elasticsearch.yml` | `/etc/opensearch/opensearch.yml` |
| Heap-Größe | `/etc/elasticsearch/jvm.options.d/*.options` | `/etc/opensearch/jvm.options` |
| Daten und Logs | `/var/lib/elasticsearch/`, `/var/log/elasticsearch/` | `/var/lib/opensearch/`, `/var/log/opensearch/` |
| Dienst | `elasticsearch` | `opensearch` |

Die Programme liegen nicht im `PATH`. Ruf sie mit vollem Pfad auf, etwa
`sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password`.

| Port | Zweck |
|------|-------|
| 9200 | REST-API über HTTPS, für Anwendungen und Admins |
| 9300 | Kommunikation zwischen den Knoten eines Clusters |

## Die REST-API mit curl

Fast die ganze Verwaltung läuft über HTTP. Bei der Paketinstallation legt Elasticsearch eine
eigene CA an; `curl` braucht deren Zertifikat:

```text
$ curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic https://localhost:9200/_cluster/health?pretty
```

| Anfrage | Antwort |
|---------|---------|
| `GET /` | Name, Version, Clustername |
| `GET /_cluster/health?pretty` | Zustand des Clusters: grün, gelb oder rot |
| `GET /_cat/indices?v` | Alle Indizes mit Dokumentanzahl und Größe |
| `GET /_cat/shards?v` | Jeder Shard mit Zustand und Knoten |
| `GET /_cat/nodes?v` | Knoten mit Heap, RAM, CPU und Last |
| `GET /_cat/allocation?v` | Plattenbelegung pro Knoten |
| `GET /_cluster/allocation/explain?pretty` | Warum ein Shard nicht zugewiesen ist |
| `PUT /INDEX/_settings` | Einstellungen ändern, z. B. die Zahl der Replikate |
| `DELETE /INDEX` | Einen Index löschen |

`?v` ergänzt bei den `_cat`-APIs Spaltenüberschriften, `?pretty` formatiert JSON.

## Grün, gelb, rot

| Zustand | Bedeutung | Typische Ursache |
|---------|-----------|------------------|
| **green** | Alle Primär-Shards und Replikate sind zugewiesen | |
| **yellow** | Alle Daten sind da, aber einige Replikate fehlen | Ein einzelner Knoten: Replikate dürfen nicht auf demselben Knoten liegen wie ihr Primär-Shard |
| **red** | Mindestens ein Primär-Shard fehlt: Daten sind nicht verfügbar | Knoten ausgefallen, Platte voll, kaputter Index |

Auf einem einzelnen Server ist gelb normal. Setz für deine Indizes `"number_of_replicas": 0`,
dann wird der Cluster grün.

## Speicher und Systemeinstellungen

| Einstellung | Empfehlung |
|-------------|------------|
| Heap (`-Xms`, `-Xmx`) | Höchstens die Hälfte des RAM, nie mehr als etwa 31 GB; beide Werte gleich |
| `vm.max_map_count` | Mindestens `262144`, gesetzt mit [`sysctl`](../27-performance/sysctl.md); die Pakete setzen es selbst |
| Swap | Aus oder `bootstrap.memory_lock: true` |
| Freier Plattenplatz | Über 15 %: ab 85 % keine neuen Shards, ab 95 % werden Indizes schreibgeschützt |

!!! tip "Snapshots statt Dateikopien"
    Sichere Indizes mit der Snapshot-API in ein Repository (`path.repo` in der Konfiguration
    oder S3). Eine Kopie von `/var/lib/elasticsearch` bei laufendem Dienst ergibt ein
    inkonsistentes Backup.

!!! warning "Port 9200 nicht offen ins Netz stellen"
    Alte Elasticsearch-Versionen ohne Passwort sind ein klassisches Datenleck. Auch mit
    aktiver Sicherheit erlaubst du Port 9200 nur für die Anwendungsserver.
