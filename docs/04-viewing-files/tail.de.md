# tail

> Zeigt die letzten Zeilen einer Datei, standardmäßig die letzten 10, und kann neue Zeilen live verfolgen.

![tail output](../assets/screenshots/04-viewing-files/tail.png)

## Syntax

```bash
tail [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n N`, `--lines=N` | Die letzten `N` statt 10 Zeilen zeigen |
| `-n +N` | Alles ab Zeile `N` zeigen |
| `-f`, `--follow` | Datei offen halten und neue Zeilen zeigen, sobald sie geschrieben werden |
| `-F` | Wie `-f`, aber der Datei auch nach einer Logrotation folgen |
| `-c N`, `--bytes=N` | Die letzten `N` Bytes zeigen |
| `--pid=PID` | Das Verfolgen beenden, wenn Prozess `PID` endet |
| `-q`, `--quiet` | Bei mehreren Dateien keine Dateinamen ausgeben |

## Beispiele

**Die neuesten Einträge eines Logs anzeigen:**

```bash
tail -n 3 /var/log/nginx/access.log
```

```text
198.51.100.23 - - [26/Oct/2026:10:41:11 +0100] "GET /login HTTP/1.1" 200 2841 "-" "Mozilla/5.0"
198.51.100.23 - - [26/Oct/2026:10:41:12 +0100] "GET /favicon.ico HTTP/1.1" 404 153 "-" "Mozilla/5.0"
192.0.2.55 - - [26/Oct/2026:10:41:58 +0100] "GET / HTTP/1.1" 200 6512 "-" "curl/8.14.1"
```

**Ein Log live verfolgen:**

```bash
tail -f /var/log/nginx/error.log
```

```text
2026/10/26 10:41:12 [error] 1234#1234: *57 open() "/var/www/example.com/public/favicon.ico" failed (2: No such file or directory), client: 198.51.100.23, server: example.com, request: "GET /favicon.ico HTTP/1.1", host: "example.com"
```

`tail` läuft weiter und gibt jede neue Zeile sofort aus. Beenden mit ++ctrl+c++.

**Zwei Logs gleichzeitig verfolgen:**

```bash
tail -f /var/log/nginx/access.log /var/log/nginx/error.log
```

```text
==> /var/log/nginx/access.log <==
192.0.2.55 - - [26/Oct/2026:10:41:58 +0100] "GET / HTTP/1.1" 200 6512 "-" "curl/8.14.1"

==> /var/log/nginx/error.log <==
2026/10/26 10:41:12 [error] 1234#1234: *57 open() "/var/www/example.com/public/favicon.ico" failed (2: No such file or directory), client: 198.51.100.23, server: example.com, request: "GET /favicon.ico HTTP/1.1", host: "example.com"
```

**Nach einer Logrotation weiter verfolgen:**

```bash
tail -F /var/log/app/access.log
```

```text
tail: '/var/log/app/access.log' has become inaccessible: No such file or directory
tail: '/var/log/app/access.log' has appeared;  following new file
```

Mit `-F` merkt `tail`, dass die Datei rotiert wurde, und macht mit der neuen Datei weiter.

**Die Kopfzeile einer CSV-Datei überspringen:**

```bash
tail -n +2 users.csv
```

```text
1,nox
2,alice
```

## Wann brauche ich das?

- Um nach einem Problem die neuesten Fehler zu sehen
- Um ein Log live zu beobachten, während du einen Dienst neu startest oder eine Website
  testest (`tail -f`)
- Um mehrere Logs gleichzeitig zu beobachten, etwa Access- und Error-Log
- Um in Skripten Kopfzeilen zu überspringen (`tail -n +2`)

!!! tip "Gleichzeitig testen und beobachten"
    Öffne zwei SSH-Sitzungen: In der einen läuft `tail -f` auf dem Error-Log, in der
    anderen testest du. So siehst du jeden Fehler in dem Moment, in dem er passiert.

!!! warning "`-f` verliert die Datei nach der Logrotation"
    `tail -f` folgt der geöffneten Datei. Benennt `logrotate` sie nachts um, beobachtet
    `tail -f` weiter die alte, umbenannte Datei und zeigt nichts Neues mehr. Für Logs, die
    rotiert werden, nimm `tail -F`.

## Verwandte Befehle

[head](head.md) · [less](less.md)
