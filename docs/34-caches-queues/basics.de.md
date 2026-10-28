# Caches und Message Queues verstehen

Viele Anwendungen brauchen neben ihrer Datenbank zwei Helfer: einen **Cache**, der häufig
genutzte Daten im Arbeitsspeicher hält, und einen **Message Broker**, der Aufträge zwischen
Programmen weiterreicht. Auf Linux-Servern sind das meist **Redis** und **RabbitMQ**.

## Cache oder Message Broker?

| | Redis / Valkey | RabbitMQ |
|---|----------------|----------|
| Aufgabe | Schlüssel-Wert-Speicher im RAM: Cache, Sitzungen, Zähler, einfache Queues | Message Broker: hält Nachrichten in Queues, bis ein Worker sie abarbeitet |
| Daten | Schlüssel mit Werten, auf Wunsch mit Ablaufzeit | Nachrichten in Queues, vom Empfänger bestätigt |
| Nach einem Neustart | Daten aus dem letzten Snapshot oder keine (reiner Cache) | Dauerhafte Queues und persistente Nachrichten überleben |
| Typischer Einsatz | PHP-Sitzungen, Seiten-Cache, Rate Limits, Datei-Sperren in Nextcloud | Bestellverarbeitung, Mailversand, Hintergrundjobs |
| Kommandozeile | `redis-cli` | `rabbitmqctl` |

## Redis oder Valkey?

2024 hat Redis seine Lizenz geändert. Die Linux Foundation hat daraufhin **Valkey**
gestartet, einen Fork der letzten Open-Source-Version. Beide sprechen dasselbe Protokoll;
Anwendungen merken keinen Unterschied. Die Befehle heißen `valkey-cli` und `valkey-server`
statt `redis-cli` und `redis-server`, mit denselben Optionen.

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Redis | `redis-server` (8.0 in Debian 13) | `redis-server` (7.0 in 24.04) | `redis` (RHEL 9) | nein |
| Valkey | `valkey-server` | nicht in 24.04 | `valkey` (RHEL 10) | `valkey` |
| Dienst | `redis-server` oder `valkey-server` | `redis-server` | `redis` oder `valkey` | `valkey` |
| RabbitMQ | `rabbitmq-server` (4.0 in Debian 13) | `rabbitmq-server` | nicht in den Paketquellen: Paketquelle des RabbitMQ-Teams | `rabbitmq` |

## Ports

| Port | Dienst |
|------|--------|
| 6379 | Redis / Valkey |
| 5672 | RabbitMQ (AMQP, für Anwendungen) |
| 15672 | Weboberfläche und HTTP-API von RabbitMQ (Plugin `rabbitmq_management`) |
| 25672, 4369 | Cluster-Kommunikation von RabbitMQ und `epmd` (Kommandozeilenwerkzeuge) |

## Redis absichern

Redis wurde für vertrauenswürdige Netze gebaut. Die wichtigen Einstellungen in
`/etc/redis/redis.conf`:

| Einstellung | Bedeutung |
|-------------|-----------|
| `bind 127.0.0.1 -::1` | Nur lokal lauschen (Standard unter Debian) |
| `protected-mode yes` | Verbindungen von außen ablehnen, solange kein Passwort gesetzt ist |
| `requirepass …` oder ACL-Benutzer | Passwort für alle Clients |
| `maxmemory 512mb` | Obergrenze für den Speicherverbrauch |
| `maxmemory-policy allkeys-lru` | Was an der Grenze passiert: für einen Cache die am wenigsten genutzten Schlüssel löschen |

Mit `maxmemory-policy noeviction` (dem Standard) nimmt Redis keine neuen Daten mehr an,
wenn es voll ist. Für Sitzungen und Queues ist das richtig, für einen reinen Cache falsch.

## Persistenz

| Verfahren | Wie | Datenverlust bei einem Absturz |
|-----------|-----|--------------------------------|
| RDB-Snapshots | `save 3600 1 300 100 60 10000`: regelmäßig `dump.rdb` schreiben | alles seit dem letzten Snapshot |
| AOF | `appendonly yes`: jeden Schreibvorgang protokollieren | etwa eine Sekunde |
| keine | `save ""`, `appendonly no` | alles; für einen reinen Cache in Ordnung |

## RabbitMQ in fünf Begriffen

| Begriff | Bedeutung |
|---------|-----------|
| **Virtual Host** (vhost) | Getrennter Bereich mit eigenen Queues und Rechten, wie eine Datenbank pro Anwendung |
| **Exchange** | Nimmt Nachrichten an und verteilt sie nach Regeln auf Queues |
| **Queue** | Hält Nachrichten, bis ein Consumer sie abholt und bestätigt |
| **Consumer** | Der Worker-Prozess, der Nachrichten verarbeitet |
| **Benutzer und Rechte** | Pro vhost: Rechte zum Konfigurieren, Schreiben und Lesen |

Der Standardbenutzer `guest` darf sich nur von `localhost` aus anmelden. Leg mit
`rabbitmqctl` eigene Benutzer an und lösch `guest` auf Produktivsystemen.

!!! tip "Unix-Socket für lokale Anwendungen"
    Laufen Redis und Anwendung auf demselben Server, schaltet `unixsocket /run/redis/redis-server.sock`
    plus `port 0` TCP ganz ab. Die Anwendung verbindet sich über die Socket-Datei.

!!! warning "Redis nie offen ins Internet stellen"
    Offene Redis-Instanzen werden innerhalb von Minuten gefunden und missbraucht, etwa um
    SSH-Schlüssel oder Krypto-Miner auf den Server zu schreiben. Lass `bind` auf `localhost`
    oder erlaube Port 6379 nur für einzelne Anwendungsserver.
