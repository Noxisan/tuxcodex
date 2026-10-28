# Understanding search servers

Shops, wikis, log platforms and many applications use a search server to find text in
millions of documents within milliseconds. The two common ones are **Elasticsearch** and
**OpenSearch**.

## Elasticsearch or OpenSearch?

In 2021 Elastic changed the license of Elasticsearch. Amazon then forked the last open
source version as **OpenSearch**. Both work the same way and share most of the REST API.

| | Elasticsearch | OpenSearch |
|---|---------------|------------|
| Maintained by | Elastic | OpenSearch Software Foundation (Linux Foundation) |
| Web interface | Kibana | OpenSearch Dashboards |
| Security | built in, active by default since version 8 | security plugin, active by default |
| Admin user | `elastic` | `admin` |
| Tools in `bin/` | `elasticsearch-reset-password`, `elasticsearch-keystore`, `elasticsearch-plugin` | `opensearch-keystore`, `opensearch-plugin`; users in the security plugin |

## Installation and paths

Neither is in the repositories of the distributions. Use the package repository of the
vendor, or a container image.

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Elasticsearch | APT repository of Elastic | APT repository of Elastic | YUM repository of Elastic | AUR or container |
| OpenSearch | APT repository of OpenSearch | APT repository of OpenSearch | YUM repository of OpenSearch | AUR or container |

| What | Elasticsearch (package) | OpenSearch (package) |
|------|-------------------------|----------------------|
| Programs | `/usr/share/elasticsearch/bin/` | `/usr/share/opensearch/bin/` |
| Configuration | `/etc/elasticsearch/elasticsearch.yml` | `/etc/opensearch/opensearch.yml` |
| Heap size | `/etc/elasticsearch/jvm.options.d/*.options` | `/etc/opensearch/jvm.options` |
| Data and logs | `/var/lib/elasticsearch/`, `/var/log/elasticsearch/` | `/var/lib/opensearch/`, `/var/log/opensearch/` |
| Service | `elasticsearch` | `opensearch` |

The programs aren't in the `PATH`. Call them with the full path, for example
`sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password`.

| Port | Use |
|------|-----|
| 9200 | REST API over HTTPS, for applications and admins |
| 9300 | Communication between the nodes of a cluster |

## The REST API with curl

Almost all administration runs over HTTP. With the package installation, Elasticsearch
creates its own CA; `curl` needs its certificate:

```text
$ curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic https://localhost:9200/_cluster/health?pretty
```

| Request | Answer |
|---------|--------|
| `GET /` | Name, version, cluster name |
| `GET /_cluster/health?pretty` | State of the cluster: green, yellow or red |
| `GET /_cat/indices?v` | All indices with document count and size |
| `GET /_cat/shards?v` | Every shard with state and node |
| `GET /_cat/nodes?v` | Nodes with heap, RAM, CPU and load |
| `GET /_cat/allocation?v` | Disk usage per node |
| `GET /_cluster/allocation/explain?pretty` | Why a shard isn't assigned |
| `PUT /INDEX/_settings` | Change settings, e.g. the number of replicas |
| `DELETE /INDEX` | Delete an index |

`?v` adds column headings to the `_cat` APIs, `?pretty` formats JSON.

## Green, yellow, red

| State | Meaning | Typical cause |
|-------|---------|---------------|
| **green** | All primary shards and replicas are assigned | |
| **yellow** | All data is available, but some replicas are missing | A single node: replicas can't be on the same node as their primary |
| **red** | At least one primary shard is missing: data is unavailable | Node failed, disk full, broken index |

On a single server, yellow is normal. Set `"number_of_replicas": 0` for your indices, then
the cluster becomes green.

## Memory and system settings

| Setting | Recommendation |
|---------|----------------|
| Heap (`-Xms`, `-Xmx`) | Half of the RAM at most, never more than about 31 GB; both values equal |
| `vm.max_map_count` | At least `262144`, set with [`sysctl`](../27-performance/sysctl.md); the packages set it themselves |
| Swap | Off, or `bootstrap.memory_lock: true` |
| Free disk | Above 15 %: from 85 % no new shards, from 95 % indices become read only |

!!! tip "Snapshots instead of file copies"
    Back up indices with the snapshot API into a repository (`path.repo` in the
    configuration, or S3). Copying `/var/lib/elasticsearch` while the service runs gives
    an inconsistent backup.

!!! warning "Don't expose port 9200"
    Old Elasticsearch versions without a password are a classic data leak. Even with
    security enabled, allow port 9200 only for application servers.
