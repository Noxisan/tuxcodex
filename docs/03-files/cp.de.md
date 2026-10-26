# cp

> Kopiert Dateien und Verzeichnisse.

![cp output](../assets/screenshots/03-files/cp.png)

## Syntax

```bash
cp [OPTION]... QUELLE... ZIEL
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-r`, `-R`, `--recursive` | Verzeichnisse mit ihrem ganzen Inhalt kopieren |
| `-a`, `--archive` | Rekursiv kopieren und Rechte, Besitzer, Zeitstempel und Links erhalten |
| `-p` | Rechte, Besitzer und Zeitstempel erhalten (ohne rekursiv zu kopieren) |
| `-i`, `--interactive` | Vor dem Überschreiben einer vorhandenen Datei nachfragen |
| `-u`, `--update` | Nur kopieren, wenn die Quelle neuer ist als das Ziel |
| `-v`, `--verbose` | Jede kopierte Datei anzeigen |
| `-b`, `--backup` | Eine vorhandene Zieldatei vor dem Überschreiben in `DATEI~` umbenennen |
| `-t`, `--target-directory=VERZ` | Alle Quellen nach `VERZ` kopieren |

## Beispiele

**Vor dem Bearbeiten einer Konfiguration eine Sicherungskopie anlegen:**

```bash
sudo cp -v /etc/ssh/sshd_config{,.bak}
```

```text
'/etc/ssh/sshd_config' -> '/etc/ssh/sshd_config.bak'
```

Bash macht aus `{,.bak}` die beiden Namen `sshd_config sshd_config.bak`. So musst du den
Pfad nur einmal tippen.

**Eine Datei unter neuem Namen kopieren:**

```bash
cp notes.txt notes-copy.txt
ls notes*
```

```text
notes-copy.txt  notes.txt
```

**Dateien in ein Verzeichnis kopieren:**

```bash
cp -v notes.txt scripts/backup.sh backup/
```

```text
'notes.txt' -> 'backup/notes.txt'
'scripts/backup.sh' -> 'backup/backup.sh'
```

**Ein Verzeichnis mit seinem ganzen Inhalt kopieren:**

```bash
cp -r scripts scripts-old
ls -d scripts*
```

```text
scripts  scripts-old
```

**Besitzer und Zeitstempel mit `-a` erhalten:**

```bash
sudo cp -r /var/www/example.com /tmp/copy-r
sudo cp -a /var/www/example.com /tmp/copy-a
ls -ld /var/www/example.com /tmp/copy-*
```

```text
drwxr-xr-x 4 www-data www-data 4096 Oct 20 09:30 /tmp/copy-a
drwxr-xr-x 4 root     root     4096 Oct 26 10:42 /tmp/copy-r
drwxr-xr-x 4 www-data www-data 4096 Oct 20 09:30 /var/www/example.com
```

Mit `-r` gehört die Kopie `root` und hat ein neues Datum. Mit `-a` ist sie eine exakte Kopie.

**Vor dem Überschreiben nachfragen:**

```bash
cp -i notes.txt notes-copy.txt
```

```text
cp: overwrite 'notes-copy.txt'?
```

Antworte mit `y`, um zu überschreiben, oder mit `n`, um abzubrechen.

## Wann brauche ich das?

- Vor jeder Änderung an einer Konfigurationsdatei: `cp datei{,.bak}` gibt dir einen Weg zurück
- Um Websites, Anwendungsdaten oder Konfigurationsverzeichnisse zu kopieren (`cp -a`)
- Um eine Konfigurationsdatei aus einer Vorlage auszurollen, etwa aus `/usr/share/doc`
  oder einem Git-Repository
- Um Dateien auf ein eingehängtes Backup-Laufwerk zu kopieren

!!! tip "Für Verzeichnisse `-a` nehmen"
    Für Backups und Umzüge ganzer Verzeichnisse ist `cp -a` fast immer die richtige Wahl.
    `cp -r` verliert Besitzer, Rechte und Zeitstempel, und Dienste können ihre Dateien
    danach unter Umständen nicht mehr lesen.

!!! warning "`cp` überschreibt ohne Nachfrage"
    Existiert die Zieldatei, ersetzt `cp` sie ohne Meldung. Nimm `-i`, wenn du dir nicht
    sicher bist, oder `-b`, um die alte Version als `DATEI~` zu behalten.

!!! warning "Vorhandenes Zielverzeichnis"
    `cp -r scripts scripts-old` legt beim ersten Mal `scripts-old` an. Führst du denselben
    Befehl noch einmal aus, existiert `scripts-old` schon, und die Kopie landet in
    `scripts-old/scripts`.

## Verwandte Befehle

[mkdir](mkdir.md) · [touch](touch.md) · [mv](mv.md)
