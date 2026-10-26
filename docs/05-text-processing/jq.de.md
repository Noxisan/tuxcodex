# jq

> Liest, filtert und formatiert JSON-Daten, zum Beispiel aus APIs, Docker oder Konfigurationsdateien.

![jq output](../assets/screenshots/05-text-processing/jq.png)

## Syntax

```bash
jq [OPTION]... FILTER [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-r`, `--raw-output` | Zeichenketten ohne Anführungszeichen ausgeben (für Skripte und Weiterverarbeitung) |
| `-c`, `--compact-output` | Jedes Ergebnis in einer einzigen Zeile ausgeben |
| `-e`, `--exit-status` | Exit-Status `1`, wenn das Ergebnis `false` oder `null` ist |
| `--arg NAME WERT` | Einen Wert aus der Shell als `$NAME` an den Filter übergeben |

Die wichtigsten Filter:

| Filter | Bedeutung |
|--------|-----------|
| `.` | Die ganze Eingabe, schön formatiert |
| `.key` | Der Wert von `key` |
| `.list[]` | Jedes Element einer Liste |
| `.list[0]` | Das erste Element einer Liste |
| `A | B` | Das Ergebnis von `A` an `B` weitergeben |
| `select(BEDINGUNG)` | Nur Elemente behalten, die die Bedingung erfüllen |
| `length` | Anzahl der Elemente |
| `keys` | Alle Schlüssel eines Objekts |
| `"\(.a): \(.b)"` | Einen Text aus Werten zusammenbauen |

## Beispiele

**JSON lesbar formatieren:**

```bash
jq . status.json
```

```text
{
  "server": "tuxcodex-srv",
  "uptime_days": 12,
  "services": [
    {
      "name": "nginx",
      "active": true,
      "port": 80
    },
    {
      "name": "postgresql",
      "active": true,
      "port": 5432
    },
    {
      "name": "redis",
      "active": false,
      "port": 6379
    }
  ]
}
```

**Einen einzelnen Wert auslesen:**

```bash
jq -r '.server' status.json
```

```text
tuxcodex-srv
```

Ohne `-r` wäre das Ergebnis `"tuxcodex-srv"` mit Anführungszeichen.

**Einen Wert aus jedem Element einer Liste holen:**

```bash
jq -r '.services[].name' status.json
```

```text
nginx
postgresql
redis
```

**Nach einer Bedingung filtern:**

```bash
jq -r '.services[] | select(.active == false) | .name' status.json
```

```text
redis
```

**Eine eigene Ausgabe zusammenbauen:**

```bash
jq -r '.services[] | "\(.name): \(.port)"' status.json
```

```text
nginx: 80
postgresql: 5432
redis: 6379
```

**Elemente zählen:**

```bash
jq '.services | length' status.json
```

```text
3
```

**Einen Syntaxfehler in einer JSON-Datei finden:**

```bash
jq . broken.json
```

```text
jq: parse error: Expected another key-value pair at line 1, column 8
```

## Wann brauche ich das?

- Um die Antworten von REST-APIs zu lesen: `curl -s https://api.example.com/status | jq .`
- Um einzelne Werte aus `docker inspect`, `kubectl get -o json` oder Cloud-CLIs zu holen
- Um JSON-Konfigurationsdateien auf Syntaxfehler zu prüfen, bevor ein Dienst sie lädt
- In Skripten, die auf Werte in JSON-Daten reagieren sollen

!!! tip "JSON vor einem Neustart prüfen"
    `jq . config.json > /dev/null && echo OK` gibt nur dann `OK` aus, wenn die Datei
    gültiges JSON ist. Führe das aus, bevor du einen Dienst neu startest, der diese Datei
    liest.

!!! warning "Nicht standardmäßig installiert"
    `jq` ist auf den meisten Distributionen nicht vorinstalliert. Das Paket heißt überall
    `jq`, siehe die Tabelle unten.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Installieren | `sudo apt install jq` | `sudo apt install jq` | `sudo dnf install jq` | `sudo pacman -S jq` |

## Verwandte Befehle

[grep](grep.md) · [awk](awk.md)
