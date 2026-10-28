# elasticsearch-keystore

> Verwaltet den Keystore von Elasticsearch: eine geschützte Datei für geheime Einstellungen wie Passwörter und S3-Schlüssel, die nicht in `elasticsearch.yml` gehören.

![elasticsearch-keystore output](../assets/screenshots/35-search/elasticsearch-keystore.png)

## Syntax

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-keystore list | add [-x] EINSTELLUNG | show EINSTELLUNG | remove EINSTELLUNG
```

## Optionen

| Befehl | Beschreibung |
|--------|--------------|
| `list` | Namen aller gespeicherten Einstellungen |
| `add EINSTELLUNG` | Eine Einstellung hinzufügen; der Wert wird abgefragt |
| `add -x EINSTELLUNG` | Den Wert von stdin lesen (für Skripte) |
| `add-file EINSTELLUNG DATEI` | Den Inhalt einer Datei ablegen, z. B. eine Zugangsdatei |
| `show EINSTELLUNG` | Einen gespeicherten Wert anzeigen |
| `remove EINSTELLUNG` | Eine Einstellung löschen |
| `passwd` | Den Keystore selbst mit einem Passwort schützen |

Die Datei ist `/etc/elasticsearch/elasticsearch.keystore`. Änderungen wirken nach einem Neustart; manche Einstellungen wie S3-Zugangsdaten lassen sich mit `POST /_nodes/reload_secure_settings` neu laden. OpenSearch hat dasselbe Werkzeug als `opensearch-keystore`.

## Beispiele

**Was gespeichert ist:**

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-keystore list
```

```text
keystore.seed
xpack.security.http.ssl.keystore.secure_password
xpack.security.transport.ssl.keystore.secure_password
xpack.security.transport.ssl.truststore.secure_password
```

**S3-Zugangsdaten für Snapshots hinzufügen:**

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add s3.client.default.access_key
sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add s3.client.default.secret_key
```

```text
Enter value for s3.client.default.access_key:
Enter value for s3.client.default.secret_key:
```

**Aus einem Skript, ohne Abfrage:**

```bash
printf '%s' "$S3_KEY" | sudo /usr/share/elasticsearch/bin/elasticsearch-keystore add -x s3.client.default.access_key
sudo /usr/share/elasticsearch/bin/elasticsearch-keystore list | grep s3
```

```text
s3.client.default.access_key
s3.client.default.secret_key
```

**Die neuen Werte ohne Neustart laden:**

```bash
curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic https://localhost:9200/_nodes/reload_secure_settings -X POST -s | jq '._nodes'
```

```text
Enter host password for user 'elastic':
{
  "total": 1,
  "successful": 1,
  "failed": 0
}
```

**Das Passwort des HTTP-Zertifikats:**

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-keystore show xpack.security.http.ssl.keystore.secure_password
```

```text
pV3sKq9TzR2mWx7YbN4c
```

## Wann brauche ich das?

- Um Elasticsearch Zugangsdaten für ein S3-Snapshot-Repository zu geben
- Um die Passwörter der TLS-Keystores nachzuschauen, die die Installation angelegt hat
- Bevor ein Cluster wächst: Jeder Knoten braucht dieselben geheimen Einstellungen

!!! tip "Derselbe Keystore auf jedem Knoten"
    Geheime Einstellungen werden nicht zwischen Knoten kopiert. Leg sie auf jedem Knoten mit
    denselben Werten an und ruf danach einmal `reload_secure_settings` auf.

!!! warning "Kein Tresor"
    Ohne `passwd` ist der Keystore nur verschleiert, und `show` gibt jeden Wert aus. Schütz die
    Datei mit den Rechten `660` und dem Besitzer `root:elasticsearch`, wie das Paket sie setzt.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installation | APT-Paketquelle von Elastic | APT-Paketquelle von Elastic | YUM-Paketquelle von Elastic | AUR oder Container |
| Pfad | `/usr/share/elasticsearch/bin/` | `/usr/share/elasticsearch/bin/` | `/usr/share/elasticsearch/bin/` | je nach Paket |

## Verwandte Befehle

[elasticsearch-reset-password](elasticsearch-reset-password.md) · [elasticsearch-plugin](elasticsearch-plugin.md) · [restic](../28-backup/restic.md) · [chmod](../06-permissions/chmod.md)
