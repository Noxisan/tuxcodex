# less

> Zeigt Dateien seitenweise an, lässt dich vor- und zurückblättern, suchen und ein wachsendes Log live verfolgen.

![less output](../assets/screenshots/04-viewing-files/less.png)

## Syntax

```bash
less [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-N` | Zeilennummern anzeigen |
| `-S` | Lange Zeilen abschneiden statt umbrechen (seitlich blättern mit den Pfeiltasten) |
| `-i` | Bei der Suche Groß- und Kleinschreibung ignorieren (außer die Suche enthält Großbuchstaben) |
| `-R` | Farben von Programmen richtig darstellen |
| `+F` | Im Verfolgungsmodus starten, wie `tail -f` |
| `+G` | Am Ende der Datei starten |
| `+/MUSTER` | Beim ersten Treffer von `MUSTER` starten |

Tasten innerhalb von `less`:

| Taste | Aktion |
|-------|--------|
| ++space++ / ++b++ | Eine Seite vor / zurück |
| ++g++ / ++shift+g++ | Zum Anfang / zum Ende springen |
| ++slash++ `MUSTER` | Vorwärts suchen |
| ++question++ `MUSTER` | Rückwärts suchen |
| ++n++ / ++shift+n++ | Nächster / vorheriger Treffer |
| ++shift+f++ | Verfolgungsmodus: neue Zeilen live anzeigen, beenden mit ++ctrl+c++ |
| `&` `MUSTER` | Nur Zeilen mit `MUSTER` anzeigen |
| ++h++ | Hilfe mit allen Tasten |
| ++q++ | Beenden |

## Beispiele

**Eine Logdatei öffnen:**

```bash
less /var/log/nginx/access.log
```

```text
192.0.2.10 - - [26/Oct/2026:09:12:03 +0100] "GET / HTTP/1.1" 200 6512 "-" "Mozilla/5.0"
192.0.2.10 - - [26/Oct/2026:09:12:03 +0100] "GET /style.css HTTP/1.1" 200 1840 "-" "Mozilla/5.0"
198.51.100.23 - - [26/Oct/2026:09:15:44 +0100] "GET /login HTTP/1.1" 200 2841 "-" "Mozilla/5.0"
198.51.100.23 - - [26/Oct/2026:09:15:51 +0100] "POST /login HTTP/1.1" 302 0 "-" "Mozilla/5.0"
/var/log/nginx/access.log
```

Die unterste Zeile zeigt den Dateinamen. Mit ++space++ blätterst du weiter, mit ++q++
beendest du `less`.

**Zeilennummern anzeigen:**

```bash
less -N /etc/hosts
```

```text
      1 127.0.0.1       localhost
      2 127.0.1.1       tuxcodex-srv.example.com        tuxcodex-srv
      3
      4 # The following lines are desirable for IPv6 capable hosts
      5 ::1     localhost ip6-localhost ip6-loopback
      6 ff02::1 ip6-allnodes
      7 ff02::2 ip6-allrouters
/etc/hosts (END)
```

**Direkt beim ersten Treffer starten:**

```bash
less +/' 404 ' /var/log/nginx/access.log
```

```text
198.51.100.23 - - [26/Oct/2026:10:41:12 +0100] "GET /favicon.ico HTTP/1.1" 404 153 "-" "Mozilla/5.0"
192.0.2.55 - - [26/Oct/2026:10:41:58 +0100] "GET / HTTP/1.1" 200 6512 "-" "curl/8.14.1"
(END)
```

**Ein Log live verfolgen:**

```bash
less +F /var/log/nginx/error.log
```

```text
2026/10/26 10:41:12 [error] 1234#1234: *57 open() "/var/www/example.com/public/favicon.ico" failed (2: No such file or directory), client: 198.51.100.23, server: example.com, request: "GET /favicon.ico HTTP/1.1", host: "example.com"
Waiting for data... (interrupt to abort)
```

Mit ++ctrl+c++ hörst du auf zu verfolgen und kannst blättern oder suchen. Mit
++shift+f++ geht das Verfolgen weiter.

**Die Ausgabe eines anderen Befehls durchblättern:**

```bash
dpkg -l | less -S
```

```text
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                    Version                  Architecture Description
:
```

## Wann brauche ich das?

- Um lange Konfigurationsdateien und Logs zu lesen, ohne dass sie durchrauschen
- Um in einem großen Log nach einem Fehler zu suchen und zwischen den Treffern zu springen
- Um ein Log live zu verfolgen (`+F`) und trotzdem zurückblättern und suchen zu können
- Um die lange Ausgabe anderer Befehle durchzublättern (`BEFEHL | less`)

!!! tip "`less` statt `more`"
    `more` ist der ältere Pager und kann nur vorwärts blättern. `less` kann alles, was
    `more` kann, und noch viel mehr. Daher kommt auch der Name: „less is more“.

!!! tip "Filtern wie mit `grep`"
    Tippe in `less` ein `&` und danach ein Wort, dann werden nur passende Zeilen
    angezeigt. Mit `&` und ++enter++ siehst du wieder alle Zeilen.

!!! warning "Der Verfolgungsmodus blockiert die Tasten"
    Im Verfolgungsmodus (`+F` oder ++shift+f++) wartet `less` nur auf neue Zeilen.
    Blättern und Suchen funktionieren erst, wenn du ++ctrl+c++ drückst. Das beendet
    nicht `less`, sondern nur das Verfolgen.

## Verwandte Befehle

[cat](cat.md) · [tac](tac.md) · [tail](tail.md) · [zless](zless.md)
