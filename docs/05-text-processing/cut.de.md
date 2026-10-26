# cut

> Schneidet Spalten oder Zeichenbereiche aus jeder Zeile heraus.

![cut output](../assets/screenshots/05-text-processing/cut.png)

## Syntax

```bash
cut OPTION... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-d ZEICHEN`, `--delimiter=ZEICHEN` | Spaltentrenner (Standard: Tab) |
| `-f LISTE`, `--fields=LISTE` | Zu behaltende Spalten: `1`, `1,3`, `2-4`, `3-` |
| `-c LISTE`, `--characters=LISTE` | Zu behaltende Zeichenpositionen: `1-10`, `5-` |
| `--complement` | Alles **außer** den gewählten Spalten behalten |
| `--output-delimiter=TEXT` | Trenner zwischen den Spalten in der Ausgabe |

## Beispiele

**Alle Benutzernamen anzeigen:**

```bash
cut -d: -f1 /etc/passwd | head -n 3
```

```text
root
daemon
bin
```

**Benutzername und Login-Shell anzeigen:**

```bash
cut -d: -f1,7 /etc/passwd | grep bash
```

```text
root:/bin/bash
nox:/bin/bash
```

**Spalten aus einer CSV-Datei nehmen:**

```bash
cut -d, -f2,3 users.csv
```

```text
name,email
nox,nox@example.com
alice,alice@example.com
bob,bob@example.com
```

**Nur die IP-Adressen eines Logs anzeigen:**

```bash
cut -d' ' -f1 /var/log/nginx/access.log | head -n 3
```

```text
192.0.2.10
192.0.2.10
198.51.100.23
```

**Den Zeitstempel nach Zeichenposition ausschneiden:**

```bash
cut -c1-19 deploy.log
```

```text
2026-10-26 10:40:01
2026-10-26 10:40:12
2026-10-26 10:40:15
```

**Nur die Pfade aus der Ausgabe von `du` anzeigen:**

```bash
du -sh /srv/* | cut -f2
```

```text
/srv/README
/srv/backup
/srv/logs
/srv/www
```

`du` trennt seine Spalten mit einem Tab, und das ist der Standardtrenner von `cut`.

## Wann brauche ich das?

- Um einzelne Spalten aus `/etc/passwd`, CSV-Exporten oder der Ausgabe anderer Befehle
  zu holen
- Um IP-Adressen, Statuscodes oder Zeitstempel aus Logs zur Weiterverarbeitung
  herauszuziehen
- In Skripten, die einen einzelnen Wert aus einer Zeile brauchen

!!! tip "Mehrere Leerzeichen hintereinander: `awk` nehmen"
    `cut -d' '` behandelt jedes einzelne Leerzeichen als Trenner. Sind Spalten mit
    mehreren Leerzeichen ausgerichtet, gerät die Zählung durcheinander. `awk` kommt damit
    richtig zurecht.

!!! warning "CSV-Dateien mit Kommas in Werten"
    Ein Wert wie `"Smith, John"` enthält ein Komma, und `cut -d,` teilt ihn in zwei. Für
    echte CSV-Daten mit Anführungszeichen nimm ein Werkzeug, das CSV versteht.

## Verwandte Befehle

[sort](sort.md) · [uniq](uniq.md) · [tr](tr.md)
