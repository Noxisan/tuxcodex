# touch

> Legt eine leere Datei an oder aktualisiert die Zeitstempel einer vorhandenen Datei.

## Syntax

```bash
touch [OPTION]... DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-c`, `--no-create` | Datei nicht anlegen, wenn sie nicht existiert |
| `-a` | Nur die Zugriffszeit ändern |
| `-m` | Nur die Änderungszeit ändern |
| `-d`, `--date=TEXT` | Diese Zeit statt „jetzt“ verwenden (z. B. `"2026-10-01 12:00"`) |
| `-t ZEIT` | Diese Zeit im Format `[[CC]YY]MMDDhhmm[.ss]` verwenden |
| `-r`, `--reference=DATEI` | Die Zeitstempel von `DATEI` übernehmen |

## Beispiele

**Eine leere Datei anlegen:**

```bash
touch report.txt
ls -l report.txt
```

```text
-rw-r--r-- 1 nox nox 0 Oct 26 10:42 report.txt
```

**Mehrere Dateien auf einmal anlegen:**

```bash
touch app.log error.log access.log
ls *.log
```

```text
access.log  app.log  error.log
```

**Die Zeit einer vorhandenen Datei aktualisieren:**

```bash
ls -l notes.txt
touch notes.txt
ls -l notes.txt
```

```text
-rw-r--r-- 1 nox nox 812 Oct 26 09:15 notes.txt
-rw-r--r-- 1 nox nox 812 Oct 26 10:42 notes.txt
```

Der Inhalt bleibt gleich, nur der Zeitstempel ändert sich.

**Ein bestimmtes Datum setzen:**

```bash
touch -d "2026-10-01 12:00" old.txt
ls -l old.txt
```

```text
-rw-r--r-- 1 nox nox 0 Oct  1 12:00 old.txt
```

**Nur Dateien aktualisieren, die schon existieren:**

```bash
touch -c missing.txt
ls missing.txt
```

```text
ls: cannot access 'missing.txt': No such file or directory
```

![touch output](../assets/screenshots/03-files/touch.png)

## Wann brauche ich das?

- Um schnell eine leere Datei anzulegen, etwa eine Logdatei, die ein Dienst erwartet
- Um Schalterdateien anzulegen, die etwas aktivieren, zum Beispiel einen Wartungsmodus
  (`touch /var/www/example.com/maintenance.flag`)
- Um Aufräumskripte oder `find -mtime` mit Dateien eines bestimmten Alters zu testen
  (`touch -d`)
- Um zu prüfen, ob du in einem Verzeichnis Schreibrechte hast

!!! tip "Viele Dateien mit Brace Expansion"
    Bash macht aus `{1..3}` eine Liste: `touch test{1..3}.txt` legt `test1.txt`,
    `test2.txt` und `test3.txt` in einem Schritt an.

!!! warning "Keine Meldung bei vorhandenen Dateien"
    `touch` überschreibt nie den Inhalt. Es sagt dir aber auch nicht, dass eine Datei
    schon existierte, sondern ändert still den Zeitstempel. Backup-Tools, die mit
    Zeitstempeln arbeiten, kopieren die Datei dann eventuell erneut.

## Verwandte Befehle

[ls](../02-navigation/ls.md) · [find](../02-navigation/find.md) · [mkdir](mkdir.md)
