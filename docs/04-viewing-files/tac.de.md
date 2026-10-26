# tac

> Gibt Dateien in umgekehrter Reihenfolge aus: die letzte Zeile zuerst.

![tac output](../assets/screenshots/04-viewing-files/tac.png)

## Syntax

```bash
tac [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-s`, `--separator=TEXT` | `TEXT` als Trennzeichen statt eines Zeilenumbruchs verwenden |
| `-b`, `--before` | Trennzeichen vor jeden Datensatz setzen statt dahinter |
| `-r`, `--regex` | Trennzeichen als regulären Ausdruck behandeln |

## Beispiele

**Eine Datei von unten nach oben anzeigen:**

```bash
cat deploy.log
tac deploy.log
```

```text
2026-10-26 10:40:01 deploy started
2026-10-26 10:40:12 files copied
2026-10-26 10:40:15 service restarted
2026-10-26 10:40:15 service restarted
2026-10-26 10:40:12 files copied
2026-10-26 10:40:01 deploy started
```

**Die drei neuesten Einträge eines Logs anzeigen, neueste zuerst:**

```bash
tac /var/log/nginx/access.log | head -n 3
```

```text
192.0.2.55 - - [26/Oct/2026:10:41:58 +0100] "GET / HTTP/1.1" 200 6512 "-" "curl/8.14.1"
198.51.100.23 - - [26/Oct/2026:10:41:12 +0100] "GET /favicon.ico HTTP/1.1" 404 153 "-" "Mozilla/5.0"
198.51.100.23 - - [26/Oct/2026:10:41:11 +0100] "GET /login HTTP/1.1" 200 2841 "-" "Mozilla/5.0"
```

**Ein Log vom neuesten Eintrag rückwärts durchblättern:**

```bash
tac /var/log/nginx/access.log | less
```

```text
192.0.2.55 - - [26/Oct/2026:10:41:58 +0100] "GET / HTTP/1.1" 200 6512 "-" "curl/8.14.1"
198.51.100.23 - - [26/Oct/2026:10:41:12 +0100] "GET /favicon.ico HTTP/1.1" 404 153 "-" "Mozilla/5.0"
198.51.100.23 - - [26/Oct/2026:10:41:11 +0100] "GET /login HTTP/1.1" 200 2841 "-" "Mozilla/5.0"
:
```

## Wann brauche ich das?

- Um Logs vom neuesten Eintrag rückwärts zu lesen, denn meist zählen die neuesten
  Ereignisse am meisten
- Um das letzte Vorkommen von etwas in einer langen Datei schnell zu finden
- In Skripten, die Zeilen in umgekehrter Reihenfolge verarbeiten müssen

!!! tip "Leicht zu merken"
    `tac` ist `cat` rückwärts geschrieben, und genau das macht es: Es gibt eine Datei
    rückwärts aus, Zeile für Zeile.

!!! tip "Zeichen statt Zeilen umdrehen"
    `tac` dreht die Reihenfolge der Zeilen um. Um die Zeichen innerhalb jeder Zeile
    umzudrehen, nimm `rev`.

## Verwandte Befehle

[cat](cat.md) · [less](less.md)
