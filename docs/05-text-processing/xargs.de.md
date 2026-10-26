# xargs

> Macht aus Eingabezeilen Argumente für einen anderen Befehl, zum Beispiel um eine Liste von Dateien zu löschen oder zu kopieren.

![xargs output](../assets/screenshots/05-text-processing/xargs.png)

## Syntax

```bash
BEFEHL | xargs [OPTION]... BEFEHL [ARGUMENTE]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-0`, `--null` | Eingabe ist durch Nullzeichen getrennt (für `find -print0`, sicher bei Leerzeichen) |
| `-n N` | Höchstens `N` Argumente pro Aufruf übergeben |
| `-I {}` | `{}` im Befehl durch jede Eingabezeile ersetzen (ein Aufruf pro Zeile) |
| `-P N` | Bis zu `N` Aufrufe parallel ausführen |
| `-r`, `--no-run-if-empty` | Den Befehl gar nicht starten, wenn die Eingabe leer ist |
| `-t`, `--verbose` | Jeden Befehl vor dem Ausführen anzeigen |
| `-p`, `--interactive` | Vor jedem Aufruf nachfragen |

## Beispiele

**Dateien aus einer Liste löschen, sicher bei Leerzeichen im Namen:**

```bash
find /tmp/app -name '*.tmp' -print0 | xargs -0 rm -v
```

```text
removed '/tmp/app/a.tmp'
removed '/tmp/app/b.tmp'
removed '/tmp/app/old report.tmp'
```

**Dasselbe ohne `-0`:**

```bash
find /tmp/app -name '*.tmp' | xargs rm -v
```

```text
removed '/tmp/app/a.tmp'
removed '/tmp/app/b.tmp'
rm: cannot remove '/tmp/app/old': No such file or directory
rm: cannot remove 'report.tmp': No such file or directory
```

Ohne `-0` trennt `xargs` an Leerzeichen, und aus `old report.tmp` werden zwei falsche Namen.

**Einen Befehl einmal pro Eintrag ausführen:**

```bash
echo "web1 web2" | xargs -t -n 1 echo Checking
```

```text
echo Checking web1
Checking web1
echo Checking web2
Checking web2
```

`-t` zeigt jeden Befehl, bevor er läuft.

**Das Argument an beliebiger Stelle im Befehl einsetzen:**

```bash
ls *.conf | xargs -I {} cp -v {} {}.bak
```

```text
'app.conf' -> 'app.conf.bak'
'db.conf' -> 'db.conf.bak'
```

**Einen Fehler bei leerer Liste vermeiden:**

```bash
find /tmp/app -name '*.tmp' | xargs rm
find /tmp/app -name '*.tmp' | xargs -r rm
```

```text
rm: missing operand
Try 'rm --help' for more information.
```

Ohne `-r` wird `rm` auch ohne Datei einmal gestartet. Mit `-r` passiert nichts.

## Wann brauche ich das?

- Um die Ergebnisse von `find`, `grep -l` oder `ls` mit einem anderen Befehl zu verarbeiten
- Um denselben Befehl auf vielen Servern, Dateien oder Benutzern auszuführen
- Um lange Aufgaben durch paralleles Ausführen (`-P`) zu beschleunigen, etwa das
  Komprimieren vieler Logdateien

!!! tip "Paralleles Arbeiten mit `-P`"
    `find /var/log/app -name '*.log' -print0 | xargs -0 -P 4 -n 1 gzip` komprimiert bis zu
    vier Dateien gleichzeitig. Auf Servern mit mehreren CPU-Kernen geht das deutlich
    schneller.

!!! warning "Immer `-print0` mit `-0`"
    Dateinamen können Leerzeichen und sogar Zeilenumbrüche enthalten. Kombiniere
    `find -print0` mit `xargs -0`, sonst werden Namen zerlegt, und der Befehl trifft die
    falschen Dateien.

!!! danger "`xargs rm` mit ungeprüfter Liste"
    Bevor du eine Liste in `xargs rm` leitest, schau sie dir an: Führe den Befehl erst
    ohne `| xargs rm` aus, oder nimm `xargs -p`, um jeden Aufruf zu bestätigen.

## Verwandte Befehle

[find](../02-navigation/find.md) · [grep](grep.md)
