# mv

> Verschiebt Dateien und Verzeichnisse an einen anderen Ort oder benennt sie um.

![mv output](../assets/screenshots/03-files/mv.png)

## Syntax

```bash
mv [OPTION]... QUELLE... ZIEL
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-i`, `--interactive` | Vor dem Überschreiben einer vorhandenen Datei nachfragen |
| `-u`, `--update` | Nur verschieben, wenn die Quelle neuer ist als das Ziel |
| `-v`, `--verbose` | Jede verschobene Datei anzeigen |
| `-b`, `--backup` | Eine vorhandene Zieldatei vor dem Überschreiben in `DATEI~` umbenennen |
| `-t`, `--target-directory=VERZ` | Alle Quellen nach `VERZ` verschieben |
| `-T`, `--no-target-directory` | Ziel als normale Datei behandeln, nie als Verzeichnis |

## Beispiele

**Eine Datei umbenennen:**

```bash
mv notes-copy.txt notes-old.txt
ls notes*
```

```text
notes-old.txt  notes.txt
```

**Eine Datei in ein Verzeichnis verschieben:**

```bash
mv -v report.txt backup/
```

```text
renamed 'report.txt' -> 'backup/report.txt'
```

**Mehrere Dateien auf einmal verschieben:**

```bash
mv -v *.log /tmp/
```

```text
renamed 'access.log' -> '/tmp/access.log'
renamed 'app.log' -> '/tmp/app.log'
renamed 'error.log' -> '/tmp/error.log'
```

**Ein Verzeichnis umbenennen:**

```bash
mv scripts-old scripts-2026
ls -d scripts*
```

```text
scripts  scripts-2026
```

**Beim Überschreiben die alte Version behalten:**

```bash
mv -b app.conf.new app.conf
ls app.conf*
```

```text
app.conf  app.conf~
```

**Vor dem Überschreiben nachfragen:**

```bash
mv -i notes-old.txt notes.txt
```

```text
mv: overwrite 'notes.txt'?
```

## Wann brauche ich das?

- Um Dateien und Verzeichnisse umzubenennen (Linux hat dafür keinen eigenen Befehl)
- Um eine neue Konfiguration nach dem Testen an ihren Platz zu bringen
  (`mv app.conf.new app.conf`)
- Um alte Logdateien oder Backups in ein anderes Verzeichnis zu verschieben
- Um neue Versionen einer Website oder Anwendung durch Austauschen von Verzeichnissen
  auszurollen

!!! tip "Schnell innerhalb eines Dateisystems"
    Innerhalb desselben Dateisystems ändert `mv` nur den Namen im Verzeichnis. Selbst
    eine 100-GB-Datei ist sofort verschoben. Zwischen verschiedenen Dateisystemen (z. B.
    auf einen USB-Stick) muss `mv` die Daten kopieren und danach das Original löschen.

!!! warning "`mv` überschreibt ohne Nachfrage"
    Existiert eine Datei mit dem Zielnamen, wird sie ersetzt und lässt sich nicht
    wiederherstellen. Nimm `-i` oder `-b`, wenn du dir nicht sicher bist.

!!! warning "Vorhandenes Zielverzeichnis"
    `mv scripts-old scripts-2026` benennt das Verzeichnis um. Existiert `scripts-2026`
    schon, wird `scripts-old` **hinein** verschoben und landet als
    `scripts-2026/scripts-old`.

## Verwandte Befehle

[cp](cp.md) · [mkdir](mkdir.md) · [rm](rm.md)
