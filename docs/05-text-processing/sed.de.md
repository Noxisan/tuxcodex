# sed

> Bearbeitet Text Zeile für Zeile, ohne einen Editor zu öffnen: suchen und ersetzen, Zeilen löschen, Bereiche ausgeben.

![sed output](../assets/screenshots/05-text-processing/sed.png)

## Syntax

```bash
sed [OPTION]... 'BEFEHL' [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-i` | Datei direkt ändern, statt das Ergebnis auszugeben |
| `-i.bak` | Wie `-i`, aber das Original als `DATEI.bak` behalten |
| `-n` | Nur Zeilen ausgeben, die du ausdrücklich mit `p` ausgibst |
| `-E` | Erweiterte reguläre Ausdrücke verwenden (wie `grep -E`) |
| `-e BEFEHL` | Einen Befehl hinzufügen (für mehrere Befehle in einem Aufruf) |

Die wichtigsten `sed`-Befehle:

| Befehl | Bedeutung |
|--------|-----------|
| `s/ALT/NEU/` | Das erste `ALT` in jeder Zeile durch `NEU` ersetzen |
| `s/ALT/NEU/g` | **Alle** Vorkommen in jeder Zeile ersetzen |
| `/MUSTER/d` | Zeilen löschen, die auf `MUSTER` passen |
| `5d` / `2,4d` | Zeile 5 / Zeilen 2 bis 4 löschen |
| `-n '2,3p'` | Nur die Zeilen 2 bis 3 ausgeben |
| `/MUSTER/a TEXT` | Nach passenden Zeilen eine Zeile mit `TEXT` anhängen |
| `/MUSTER/i TEXT` | Vor passenden Zeilen eine Zeile mit `TEXT` einfügen |

## Beispiele

**Text in der Ausgabe ersetzen:**

```bash
sed 's/yes/no/' sshd_config
```

```text
#Port 22
PermitRootLogin no
PasswordAuthentication no
# Logging
LogLevel INFO
```

Die Datei selbst bleibt unverändert, `sed` gibt nur das Ergebnis aus.

**Eine Einstellung direkt in der Datei ändern, mit Sicherung:**

```bash
sudo sed -i.bak 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
grep PermitRootLogin /etc/ssh/sshd_config
```

```text
PermitRootLogin no
```

Das Original bleibt als `/etc/ssh/sshd_config.bak` erhalten.

**Alle Kommentarzeilen löschen:**

```bash
sed '/^#/d' sshd_config
```

```text
PermitRootLogin yes
PasswordAuthentication yes
LogLevel INFO
```

**Nur bestimmte Zeilen ausgeben:**

```bash
sed -n '2,3p' sshd_config
```

```text
PermitRootLogin yes
PasswordAuthentication yes
```

**Ein Zeitfenster aus einem Log ausschneiden:**

```bash
sed -n '/10:02:19/,/10:41:11/p' /var/log/nginx/access.log | cut -d' ' -f4,7
```

```text
[26/Oct/2026:10:02:19 /wp-login.php
[26/Oct/2026:10:02:20 /.env
[26/Oct/2026:10:41:11 /login
```

**Nach einer Einstellung eine Zeile einfügen:**

```bash
sed '/^LogLevel/a MaxAuthTries 3' sshd_config | tail -n 2
```

```text
LogLevel INFO
MaxAuthTries 3
```

**Pfade mit einem anderen Trennzeichen ersetzen:**

```bash
echo "root /var/www/old/public;" | sed 's|/var/www/old|/var/www/new|'
```

```text
root /var/www/new/public;
```

Statt `/` kann jedes Zeichen als Trenner dienen. Mit `|` musst du die Schrägstriche in
Pfaden nicht maskieren.

## Wann brauche ich das?

- Um Einstellungen in Konfigurationsdateien per Skript oder über SSH zu ändern, ohne Editor
- Um eine Domain, einen Pfad oder eine IP-Adresse in vielen Dateien auf einmal zu ersetzen
- Um Kommentare, Leerzeilen oder Windows-Zeilenenden zu entfernen (`sed -i 's/\r$//' DATEI`)
- Um ein Zeitfenster oder einen Block aus einem Log auszuschneiden

!!! tip "Erst testen, dann `-i`"
    Führe den Befehl immer zuerst ohne `-i` aus und prüfe die Ausgabe. Erst wenn sie
    stimmt, ergänze `-i` (besser `-i.bak`), um die Änderung in die Datei zu schreiben.

!!! warning "`g` für alle Vorkommen"
    Ohne `g` ersetzt `s/alt/neu/` nur den **ersten** Treffer in jeder Zeile. Mit
    `s/alt/neu/g` ersetzt du alle.

!!! danger "`sed -i` auf viele Dateien"
    `sed -i 's/.../.../g' *.conf` ändert alle Dateien auf einmal, ohne Nachfrage und ohne
    Rückgängig. Ein falsches Muster beschädigt jede Datei. Leg ein Backup an oder nimm
    `-i.bak`, und prüfe das Ergebnis mit [`diff`](diff.md).

## Verwandte Befehle

[grep](grep.md) · [tr](tr.md) · [awk](awk.md) · [diff](diff.md)
