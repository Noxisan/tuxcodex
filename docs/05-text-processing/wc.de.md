# wc

> Zählt Zeilen, Wörter und Bytes in Dateien oder in der Ausgabe anderer Befehle.

![wc output](../assets/screenshots/05-text-processing/wc.png)

## Syntax

```bash
wc [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-l`, `--lines` | Zeilen zählen |
| `-w`, `--words` | Wörter zählen |
| `-c`, `--bytes` | Bytes zählen |
| `-m`, `--chars` | Zeichen zählen (weicht bei Umlauten und anderen UTF-8-Zeichen von den Bytes ab) |
| `-L`, `--max-line-length` | Länge der längsten Zeile anzeigen |

## Beispiele

**Zeilen, Wörter und Bytes zählen:**

```bash
wc /var/log/nginx/access.log
```

```text
  9 108 850 /var/log/nginx/access.log
```

Die drei Zahlen sind Zeilen, Wörter und Bytes.

**Nur Zeilen zählen:**

```bash
wc -l /var/log/nginx/access.log
```

```text
9 /var/log/nginx/access.log
```

**Mehrere Dateien auf einmal zählen:**

```bash
wc -l /var/log/nginx/access.log users.csv
```

```text
  9 /var/log/nginx/access.log
  4 users.csv
 13 total
```

**Die Ergebnisse eines anderen Befehls zählen:**

```bash
grep ' 404 ' /var/log/nginx/access.log | wc -l
```

```text
3
```

**Nur die Zahl ausgeben, ohne Dateinamen:**

```bash
wc -l < users.csv
```

```text
4
```

## Wann brauche ich das?

- Um herauszufinden, wie groß ein Log ist oder wie viele Anfragen ein Server bekommen hat
- Um zusammen mit `grep` Treffer zu zählen, etwa Fehler, Anmeldungen oder 404-Anfragen
- Um Dateien, Benutzer oder Prozesse zu zählen: `ls /etc/nginx/sites-enabled | wc -l`
- In Skripten, die eine Zahl zum Vergleichen brauchen, etwa „mehr als 100 Fehler“

!!! tip "Nur die Zahl für Skripte"
    Mit `wc -l < DATEI` liest `wc` von der Standardeingabe und gibt nur die Zahl aus. Das
    lässt sich in Skripten leichter verwenden als die Ausgabe mit Dateinamen.

!!! warning "Die letzte Zeile braucht einen Zeilenumbruch"
    `wc -l` zählt Zeilenumbrüche, nicht Zeilen. Fehlt am Ende der letzten Zeile einer
    Datei der Zeilenumbruch, wird sie nicht mitgezählt.

## Verwandte Befehle

[cat](../04-viewing-files/cat.md)
