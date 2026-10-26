# sort

> Sortiert Zeilen alphabetisch, nach Zahlen, nach Größe oder nach einer bestimmten Spalte.

![sort output](../assets/screenshots/05-text-processing/sort.png)

## Syntax

```bash
sort [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n`, `--numeric-sort` | Nach Zahlen sortieren (`9` vor `10`) |
| `-h`, `--human-numeric-sort` | Größen wie `4.0K`, `98M`, `1.2G` richtig sortieren |
| `-r`, `--reverse` | Reihenfolge umkehren |
| `-u`, `--unique` | Jede Zeile nur einmal ausgeben |
| `-t ZEICHEN` | `ZEICHEN` als Spaltentrenner verwenden (Standard: Leerzeichen) |
| `-k N` | Nach Spalte `N` sortieren |
| `-f`, `--ignore-case` | Groß- und Kleinschreibung ignorieren |
| `-o DATEI` | Ergebnis in `DATEI` schreiben (darf die Eingabedatei sein) |

## Beispiele

**Zeilen alphabetisch sortieren:**

```bash
sort servers.txt
```

```text
db1
db1
web1
web1
web1
web2
```

**Beim Sortieren Duplikate entfernen:**

```bash
sort -u servers.txt
```

```text
db1
web1
web2
```

**Zahlen richtig sortieren:**

```bash
sort ports.txt
sort -n ports.txt
```

```text
22
443
80
8080
22
80
443
8080
```

Ohne `-n` vergleicht `sort` Zeichen für Zeichen, deshalb landet `443` vor `80`. Mit `-n`
werden die Werte als Zahlen verglichen.

**Die größten Verzeichnisse finden:**

```bash
du -sh /srv/* | sort -hr
```

```text
1.2G    /srv/backup
512M    /srv/www
98M     /srv/logs
4.0K    /srv/README
```

**Nach einer Spalte sortieren:**

```bash
sort -t: -k3 -n /etc/passwd | cut -d: -f1,3
```

```text
root:0
daemon:1
bin:2
www-data:33
nox:1000
```

`-t:` trennt die Zeilen an `:`, `-k3 -n` sortiert numerisch nach der dritten Spalte, der
Benutzer-ID.

**Eine CSV-Datei nach Namen sortieren, ohne Kopfzeile:**

```bash
tail -n +2 users.csv | sort -t, -k2
```

```text
2,alice,alice@example.com,user
3,bob,bob@example.com,user
1,nox,nox@example.com,admin
```

## Wann brauche ich das?

- Um die größten Dateien und Verzeichnisse zu finden, wenn die Platte voll ist
  (`du -sh * | sort -h`)
- Um Listen für `uniq` vorzubereiten, das nur direkt aufeinanderfolgende Duplikate findet
- Um Logeinträge, Benutzer oder IP-Adressen nach einer Spalte zu sortieren
- Um Listen zu vergleichen, etwa installierte Pakete auf zwei Servern

!!! tip "`-u` statt `sort | uniq`"
    `sort -u` liefert dasselbe Ergebnis wie `sort | uniq`, in einem Schritt.

!!! warning "Die Reihenfolge hängt von der Spracheinstellung ab"
    Mit deutscher oder englischer Locale mischt `sort` Groß- und Kleinbuchstaben und
    ignoriert manche Sonderzeichen. Skripte, die ein stabiles Ergebnis brauchen, sollten
    `LC_ALL=C sort` verwenden.

!!! danger "`sort datei > datei` leert die Datei"
    Die Shell leert die Zieldatei, **bevor** `sort` sie überhaupt liest. Das Ergebnis ist
    eine leere Datei. Um eine Datei an Ort und Stelle zu sortieren, nimm
    `sort -o datei datei`.

## Verwandte Befehle

[wc](wc.md) · [tail](../04-viewing-files/tail.md)
