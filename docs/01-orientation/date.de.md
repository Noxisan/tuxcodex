# date

> Zeigt das aktuelle Datum und die Uhrzeit in beliebigem Format an und rechnet mit Zeitpunkten.

## Syntax

```bash
date [OPTION]... [+FORMAT]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `+FORMAT` | Datum im eigenen Format ausgeben (siehe unten) |
| `-d`, `--date=TEXT` | Statt „jetzt“ den in `TEXT` beschriebenen Zeitpunkt zeigen (`yesterday`, `+30 days`, `@1793007737`) |
| `-u`, `--utc` | Zeit in UTC anzeigen |
| `-I[FMT]`, `--iso-8601[=FMT]` | ISO-8601-Format; `FMT` ist `date`, `hours`, `minutes`, `seconds` oder `ns` |
| `-R`, `--rfc-email` | Format aus E-Mail-Headern (`Mon, 26 Oct 2026 10:42:17 +0100`) |
| `-r`, `--reference=DATEI` | Zeitpunkt der letzten Änderung von `DATEI` anzeigen |
| `-s`, `--set=TEXT` | Systemzeit setzen (nur root) |

Die wichtigsten Formatangaben:

| Angabe | Bedeutung | Beispiel |
|--------|-----------|----------|
| `%Y` / `%m` / `%d` | Jahr / Monat / Tag | `2026` / `10` / `26` |
| `%H` / `%M` / `%S` | Stunde / Minute / Sekunde | `10` / `42` / `17` |
| `%F` | Datum, wie `%Y-%m-%d` | `2026-10-26` |
| `%T` | Uhrzeit, wie `%H:%M:%S` | `10:42:17` |
| `%a` / `%A` | Wochentag, kurz / lang | `Mon` / `Monday` |
| `%Z` / `%z` | Name / Versatz der Zeitzone | `CET` / `+0100` |
| `%s` | Sekunden seit 1970-01-01 UTC (Unix-Zeit) | `1793007737` |

## Beispiele

**Aktuelles Datum und Uhrzeit anzeigen:**

```bash
date
```

```text
Mon Oct 26 10:42:17 CET 2026
```

**Die Uhrzeit in UTC anzeigen:**

```bash
date -u
```

```text
Mon Oct 26 09:42:17 UTC 2026
```

**Das Datum in einem Dateinamen verwenden:**

```bash
echo "backup-$(date +%F).tar.gz"
```

```text
backup-2026-10-26.tar.gz
```

**Einen Zeitstempel für Logmeldungen erzeugen:**

```bash
date '+%F %T'
```

```text
2026-10-26 10:42:17
```

**Ein Datum in der Vergangenheit oder Zukunft berechnen:**

```bash
date -d yesterday +%F
date -d '+30 days'
```

```text
2026-10-25
Wed Nov 25 10:42:17 CET 2026
```

**Einen Unix-Zeitstempel in ein lesbares Datum umwandeln:**

```bash
date -d @1793007737
```

```text
Mon Oct 26 10:42:17 CET 2026
```

![date output](../assets/screenshots/01-orientation/date.png)

## Wann brauche ich das?

- Um Uhrzeit und Zeitzone des Servers zu prüfen, bevor du Logeinträge vergleichst
- Für Dateinamen von Backups und Exporten (`backup-2026-10-26.tar.gz`) – mit `%F`
  werden sie richtig sortiert
- Für Zeitstempel in eigenen Skripten und Logmeldungen
- Um Unix-Zeitstempel aus Logs, Datenbanken oder APIs in ein lesbares Datum umzuwandeln
- Um mit Daten zu rechnen, etwa „alles löschen, was älter als 30 Tage ist“

!!! tip "`%F` für Dateinamen"
    `%F` (`2026-10-26`) wird von `ls` richtig sortiert und enthält weder Leerzeichen
    noch Doppelpunkte. Formate wie `26.10.2026` landen in der falschen Reihenfolge.

!!! warning "`%` in der crontab maskieren"
    In einer crontab hat `%` eine Sonderbedeutung und beginnt eine neue Zeile. Schreib
    dort `\%`: `tar -czf /backup/etc-$(date +\%F).tar.gz /etc`

!!! warning "Die Zeit nicht mit `date -s` setzen"
    Auf Servern hält NTP die Uhrzeit korrekt. Zeitzone und Synchronisation stellst du mit
    `timedatectl` ein, statt die Uhr von Hand zu verstellen.

## Verwandte Befehle

[uptime](uptime.md)
