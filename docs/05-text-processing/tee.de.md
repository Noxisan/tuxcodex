# tee

> Schreibt seine Eingabe in eine oder mehrere Dateien und gibt sie gleichzeitig auf dem Bildschirm aus.

![tee output](../assets/screenshots/05-text-processing/tee.png)

## Syntax

```bash
tee [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-a`, `--append` | An die Datei anhängen, statt sie zu überschreiben |
| `-i`, `--ignore-interrupts` | ++ctrl+c++ ignorieren, damit die Datei vollständig geschrieben wird |
| `-p` | Nicht abbrechen, wenn das Schreiben in eine der Ausgaben fehlschlägt |

## Beispiele

**Eine Datei schreiben, die nur `root` ändern darf:**

```bash
echo "vm.swappiness=10" | sudo tee /etc/sysctl.d/99-swappiness.conf
```

```text
vm.swappiness=10
```

**Warum die normale Umleitung mit `sudo` nicht funktioniert:**

```bash
sudo echo "vm.swappiness=10" > /etc/sysctl.d/99-swappiness.conf
```

```text
-bash: /etc/sysctl.d/99-swappiness.conf: Permission denied
```

`sudo` gilt nur für `echo`. Die Umleitung `>` erledigt deine eigene Shell, ohne
Root-Rechte. Mit `tee` läuft das Schreiben selbst mit `sudo`.

**Eine Zeile an eine Datei anhängen:**

```bash
echo "192.0.2.20  db1.example.com  db1" | sudo tee -a /etc/hosts
```

```text
192.0.2.20  db1.example.com  db1
```

**Die Ausgabe eines Skripts beobachten und gleichzeitig speichern:**

```bash
./backup.sh | tee backup.log
```

```text
Backup started: 2026-10-26 10:42:01
Dumping database ... done
Compressing ... done
Backup finished: 2026-10-26 10:44:37
```

Die Ausgabe erscheint auf dem Bildschirm und landet gleichzeitig in `backup.log`.

**Schreiben, ohne die Ausgabe anzuzeigen:**

```bash
echo "deb http://deb.debian.org/debian trixie-backports main" | sudo tee /etc/apt/sources.list.d/backports.list > /dev/null
cat /etc/apt/sources.list.d/backports.list
```

```text
deb http://deb.debian.org/debian trixie-backports main
```

## Wann brauche ich das?

- Um Konfigurationsdateien mit `sudo` von der Kommandozeile oder aus einem Skript zu
  schreiben oder zu ergänzen
- Um die Ausgabe lang laufender Befehle (Updates, Backups, Migrationen) zu speichern und
  trotzdem mitzulesen
- Um mitten in einer Pipeline die Rohdaten zu sichern: `BEFEHL | tee raw.txt | grep error`

!!! tip "Auch Fehler mitschreiben"
    `tee` bekommt nur die Standardausgabe. Um auch Fehlermeldungen zu speichern, leite sie
    vorher um: `./backup.sh 2>&1 | tee backup.log`.

!!! warning "Ohne `-a` wird die Datei überschrieben"
    `sudo tee /etc/hosts` ersetzt die ganze Datei durch die neue Zeile. Wenn du etwas an
    eine vorhandene Datei anhängen willst, nimm **immer** `tee -a`.

## Verwandte Befehle

[cat](../04-viewing-files/cat.md) · [grep](grep.md)
