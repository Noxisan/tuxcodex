# systemd-run

> Führt einen Befehl als vorübergehende systemd-Unit aus: im Hintergrund mit eigenem Log, mit Ressourcengrenzen oder einmalig zu einem späteren Zeitpunkt.

![systemd-run output](../assets/screenshots/09-systemd/systemd-run.png)

## Syntax

```bash
systemd-run [OPTION]... BEFEHL [ARGUMENT]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--unit=NAME` | Name der Unit, statt eines erzeugten `run-…`-Namens |
| `--on-active=ZEIT` | Einmal nach `ZEIT` ausführen, z. B. `30min` |
| `--on-calendar=ZEIT` | Einmal zu diesem Zeitpunkt ausführen, z. B. `"2026-10-27 03:00"` |
| `-p EIGENSCHAFT=WERT` | Eine Unit-Eigenschaft setzen, z. B. `MemoryMax=500M` oder `CPUQuota=50%` |
| `--wait` | Warten, bis der Befehl fertig ist, dann eine Zusammenfassung zeigen |
| `-t`, `--pty` | Den Befehl mit deinem Terminal verbinden |
| `--user` | Im eigenen Benutzer-Manager statt im System ausführen |

## Beispiele

**Ein Skript als Dienst im Hintergrund ausführen:**

```bash
sudo systemd-run --unit=backup-now /usr/local/bin/backup.sh
```

```text
Running as unit: backup-now.service; invocation ID: 7c2e9f4a1b3d4e6f8a0b2c4d6e8f0a13
```

Das Skript läuft jetzt unabhängig von deiner SSH-Sitzung. Seine Ausgabe landet im
Journal: `journalctl -u backup-now`.

**Einen Dienst einmalig in 30 Minuten neu starten:**

```bash
sudo systemd-run --on-active=30min --unit=php-restart /usr/bin/systemctl restart php8.4-fpm
```

```text
Running timer as unit: php-restart.timer
Will run service as unit: php-restart.service
```

**Eine Migration heute Nacht um 3 Uhr ausführen:**

```bash
sudo systemd-run --on-calendar="2026-10-27 03:00" --unit=migrate /usr/local/bin/migrate.sh
```

```text
Running timer as unit: migrate.timer
Will run service as unit: migrate.service
```

`systemctl list-timers` zeigt, wann sie läuft.

**Speicher und CPU begrenzen und auf das Ergebnis warten:**

```bash
sudo systemd-run --wait -p MemoryMax=500M -p CPUQuota=50% --unit=import /usr/local/bin/import.sh
```

```text
Running as unit: import.service; invocation ID: 1f8b3d5c7e9a4b2d6f0e8c4a2b6d9e17
          Finished with result: success
Main processes terminated with: code=exited, status=0/SUCCESS
               Service runtime: 4min 12.304s
             CPU time consumed: 2min 3.871s
                   Memory peak: 486.2M (swap: 0B)
```

`CPUQuota=50%` erlaubt höchstens einen halben CPU-Kern. Braucht das Skript mehr
Arbeitsspeicher als `MemoryMax`, beendet der Kernel es.

## Wann brauche ich das?

- Um einen langen Job zu starten, der das Abmelden überleben muss, mit sauberem Log
- Um etwas einmalig zu einem späteren Zeitpunkt auszuführen, ohne Cron-Eintrag
- Um einen schweren Job auf einen Teil von Arbeitsspeicher und CPU zu begrenzen

!!! tip "Besser als `nohup` für lange Jobs"
    Im Vergleich zu [`nohup`](../08-processes/nohup.md) bekommst du ein sauberes Log im
    Journal, den Zustand mit `systemctl status`, und du kannst den Job mit
    `systemctl stop` beenden.

!!! warning "Die Unit ist vorübergehend"
    Ist der Befehl erfolgreich fertig, verschwindet die Unit. Nur fehlgeschlagene Units
    bleiben, bis du sie mit `sudo systemctl reset-failed` entfernst. Für Jobs, die
    regelmäßig laufen sollen, schreib eine richtige Unit mit Timer.

## Verwandte Befehle

[systemctl](systemctl.md) · [journalctl](journalctl.md) · [systemd-analyze](systemd-analyze.md) · [nohup](../08-processes/nohup.md)
