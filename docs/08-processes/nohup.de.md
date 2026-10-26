# nohup

> Startet einen Befehl so, dass er weiterläuft, wenn du dich abmeldest oder die SSH-Verbindung abbricht.

![nohup output](../assets/screenshots/08-processes/nohup.png)

## Syntax

```bash
nohup BEFEHL [ARGUMENT]... &
```

`nohup` sorgt dafür, dass der Befehl das Signal `HUP` ignoriert, das beim Schließen des
Terminals gesendet wird. Das `&` startet ihn im Hintergrund.

## Optionen

`nohup` selbst hat außer `--help` und `--version` keine Optionen. Wichtig ist die
Umleitung der Ausgabe:

| Form | Wohin die Ausgabe geht |
|------|------------------------|
| `nohup CMD &` | `nohup.out` im aktuellen Verzeichnis, oder `~/nohup.out` |
| `nohup CMD > DATEI 2>&1 &` | Ausgabe und Fehler in `DATEI` |
| `nohup CMD > /dev/null 2>&1 &` | Verworfen |

## Beispiele

**Ein Backup starten, das das Abmelden überlebt:**

```bash
nohup ./backup.sh &
```

```text
[1] 4410
nohup: ignoring input and appending output to 'nohup.out'
```

**Die Ausgabe in eine selbst gewählte Logdatei schreiben:**

```bash
nohup ./backup.sh > /var/tmp/backup.log 2>&1 &
```

```text
[1] 4410
```

Keine Meldung von `nohup`: Alles landet in der Logdatei.

**Nach dem erneuten Anmelden prüfen, ob es noch läuft:**

```bash
pgrep -a backup.sh
```

```text
4410 /bin/bash ./backup.sh
```

**Die Ausgabe verfolgen:**

```bash
tail -f /var/tmp/backup.log
```

```text
2026-10-26 10:42:17 dumping database shop
2026-10-26 10:44:51 compressing /srv/www
```

## Wann brauche ich das?

- Für lange Jobs über SSH: Backups, Importe, Datenmigrationen
- Wenn die Verbindung instabil ist und eine abgebrochene Sitzung den Job nicht beenden darf
- Um schnell einen einmaligen Job zu starten, ohne eine systemd-Unit zu schreiben

!!! tip "`tmux` für interaktive Arbeit"
    Mit `nohup` kommst du nicht mehr an das Terminal des Jobs heran. Willst du das
    Programm später sehen und bedienen, starte es in `tmux` oder `screen`, trenne dich
    und verbinde dich nach dem Anmelden wieder.

!!! warning "`nohup.out` wächst"
    Ohne Umleitung wird jede Ausgabe an `nohup.out` angehängt. Die Datei wird nie
    aufgeräumt und kann groß werden. Gib selbst eine Logdatei an, wie im zweiten Beispiel.

## Verwandte Befehle

[jobs](jobs.md) · [bg](bg.md) · [pgrep](pgrep.md) · [tail](../04-viewing-files/tail.md)
