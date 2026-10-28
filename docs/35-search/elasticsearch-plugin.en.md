# elasticsearch-plugin

> Installs, lists and removes Elasticsearch plugins, for example additional language analyzers.

![elasticsearch-plugin output](../assets/screenshots/35-search/elasticsearch-plugin.png)

## Syntax

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-plugin list | install [--batch] PLUGIN | remove PLUGIN
```

## Options

| Command | Description |
|---------|-------------|
| `list` | Installed plugins |
| `install PLUGIN` | Install an official plugin by name, or from a URL or `file://` path |
| `install --batch` | Don't ask about extra permissions |
| `remove PLUGIN` | Remove a plugin |
| `remove --purge` | Also delete its configuration |

Plugins must have exactly the version of Elasticsearch, and every node needs the same plugins. Changes take effect after `sudo systemctl restart elasticsearch`. OpenSearch: `opensearch-plugin` with the same commands.

## Examples

**Install a plugin:**

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch analysis-icu
```

```text
-> Installing analysis-icu
-> Downloading analysis-icu from elastic
-> Installed analysis-icu
-> Please restart Elasticsearch to activate any plugins installed
```

**Installed plugins:**

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-plugin list
```

```text
analysis-icu
```

**Activate it and check:**

```bash
sudo systemctl restart elasticsearch
curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic https://localhost:9200/_cat/plugins?v
```

```text
Enter host password for user 'elastic':
name       component    version
tuxdex-srv analysis-icu 9.1.0
```

**A typo in the name:**

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-foo
```

```text
ERROR: Unknown plugin analysis-foo, did you mean any of [analysis-nori, analysis-icu]?, with exit code 64
```

**Remove a plugin:**

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-plugin remove analysis-icu
```

```text
-> removing [analysis-icu]...
```

## When do I need it?

- For better search in a language, e.g. `analysis-icu` or `analysis-kuromoji`
- Before an upgrade: which plugins must be upgraded as well?
- To find out why a node doesn't start after an upgrade

!!! tip "Plugins on servers without internet"
    Download the ZIP on another machine and install it with
    `elasticsearch-plugin install file:///tmp/analysis-icu-9.1.0.zip`.

!!! warning "Upgrade plugins together with Elasticsearch"
    After a package upgrade a node with an old plugin version refuses to start. Remove the
    plugin before the upgrade and install it again afterwards, in the new version.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | APT repository of Elastic | APT repository of Elastic | YUM repository of Elastic | AUR or container |
| Path | `/usr/share/elasticsearch/bin/` | `/usr/share/elasticsearch/bin/` | `/usr/share/elasticsearch/bin/` | depends on the package |

## Related commands

[elasticsearch-keystore](elasticsearch-keystore.md) · [elasticsearch-reset-password](elasticsearch-reset-password.md) · [systemctl](../09-systemd/systemctl.md)
