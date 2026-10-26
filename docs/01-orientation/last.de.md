# last

> Zeigt die Anmelde-Historie: wer sich wann, von wo und wie lange angemeldet hat, dazu die Neustarts.

## Syntax

```bash
last [OPTION]... [BENUTZER]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n`, `--limit ANZAHL` | Nur die letzten `ANZAHL` Einträge anzeigen |
| `-s`, `--since ZEIT` | Nur Einträge seit `ZEIT` anzeigen (z. B. `2026-10-25`) |
| `-t`, `--until ZEIT` | Nur Einträge bis `ZEIT` anzeigen |
| `-p`, `--present ZEIT` | Anzeigen, wer zur `ZEIT` angemeldet war |
| `-F`, `--fulltimes` | Vollständige An- und Abmeldezeiten samt Jahr ausgeben |
| `-i`, `--ip` | IP-Adressen statt Hostnamen anzeigen |
| `-x`, `--system` | Zusätzlich Einträge zum Herunterfahren anzeigen |
| `-R`, `--nohostname` | Spalte mit dem Hostnamen ausblenden |
| `--time-format FORMAT` | Zeitformat: `notime`, `short`, `full` oder `iso` |

## Beispiele

**Die Anmelde-Historie anzeigen:**

```bash
last
```

```text
nox      pts/1        198.51.100.23    Mon Oct 26 10:30 - still logged in
nox      pts/0        192.0.2.10       Mon Oct 26 09:12 - still logged in
nox      pts/0        192.0.2.10       Sun Oct 25 18:03 - 19:47  (01:44)
reboot   system boot  6.12.48+deb13-am Wed Oct 14 07:37 - still running

wtmpdb begins Tue Sep  9 14:20:11 2025
```

Die neuesten Einträge stehen oben. Bei `reboot` zeigt die dritte Spalte den Kernel, mit
dem gestartet wurde.

**Nur die letzten 3 Einträge anzeigen:**

```bash
last -n 3
```

```text
nox      pts/1        198.51.100.23    Mon Oct 26 10:30 - still logged in
nox      pts/0        192.0.2.10       Mon Oct 26 09:12 - still logged in
nox      pts/0        192.0.2.10       Sun Oct 25 18:03 - 19:47  (01:44)

wtmpdb begins Tue Sep  9 14:20:11 2025
```

**Nur die Anmeldungen eines Benutzers anzeigen:**

```bash
last nox
```

```text
nox      pts/1        198.51.100.23    Mon Oct 26 10:30 - still logged in
nox      pts/0        192.0.2.10       Mon Oct 26 09:12 - still logged in
nox      pts/0        192.0.2.10       Sun Oct 25 18:03 - 19:47  (01:44)

wtmpdb begins Tue Sep  9 14:20:11 2025
```

**Nur die Neustarts anzeigen:**

```bash
last reboot
```

```text
reboot   system boot  6.12.48+deb13-am Wed Oct 14 07:37 - still running
reboot   system boot  6.12.43+deb13-am Thu Oct  1 06:15 - 07:35 (13+01:20)

wtmpdb begins Tue Sep  9 14:20:11 2025
```

![last output](../assets/screenshots/01-orientation/last.png)

## Wann brauche ich das?

- Nach einem Vorfall: Wer war zu dem Zeitpunkt angemeldet, und von welcher Adresse?
- Um zu prüfen, wann der Server zuletzt neu gestartet wurde und mit welchem Kernel
- Um Anmeldungen zu ungewöhnlichen Zeiten oder von unbekannten Adressen zu entdecken
- Um Wartungsarbeiten zu dokumentieren: Wann hat sich ein Kollege angemeldet, und wie
  lange war er da?

!!! tip "Gut zu wissen"
    `last` erfasst nur **erfolgreiche** Anmeldungen. Fehlgeschlagene SSH-Anmeldeversuche
    findest du im Journal: `journalctl -u ssh`.

!!! warning "`last: command not found` unter Debian 13"
    Seit Debian 13 gehört `last` nicht mehr zu `util-linux` (siehe unten). Fehlt der
    Befehl, installiere `wtmpdb`. Anmeldungen von vor der Installation werden nicht
    erfasst.

## Debian vs. Arch

Seit Debian 13 „trixie“ ist die alte Datei `/var/log/wtmp` ersetzt, weil ihr Format
keine Zeitangaben nach 2038 speichern kann.

| | Debian 13 | Arch |
|---|-----------|------|
| Paket | `wtmpdb` + `libpam-wtmpdb` (bei Bedarf installieren) | `util-linux` (vorinstalliert) |
| Datendatei | `/var/log/wtmp.db` (SQLite-Datenbank) | `/var/log/wtmp` |
| Letzte Zeile der Ausgabe | `wtmpdb begins …` | `wtmp begins …` |

Installation unter Debian:

```bash
sudo apt install wtmpdb libpam-wtmpdb
```

Danach funktioniert `last` wie gewohnt. Die Optionen aus der Tabelle oben gelten für
beide Varianten.

## Verwandte Befehle

[who](who.md) · [w](w.md) · [uptime](uptime.md)
