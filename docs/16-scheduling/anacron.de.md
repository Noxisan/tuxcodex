# anacron

> Führt tägliche, wöchentliche und monatliche Jobs auch dann aus, wenn der Server zur geplanten Zeit aus war: Verpasste Läufe werden nach dem Booten nachgeholt.

![anacron output](../assets/screenshots/16-scheduling/anacron.png)

## Syntax

```bash
anacron [OPTION]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-T` | `/etc/anacrontab` auf Fehler prüfen |
| `-f` | Erzwingen: alle Jobs jetzt ausführen, egal wann sie zuletzt liefen |
| `-n` | Sofort: nicht auf die Verzögerung warten |
| `-d` | Im Vordergrund laufen und Meldungen ausgeben |

Jede Zeile in `/etc/anacrontab`: Zeitraum in Tagen, Verzögerung in Minuten, ein Name, der Befehl. Wann ein Job zuletzt lief, steht in `/var/spool/anacron/`.

## Beispiele

**Die Konfiguration anzeigen:**

```bash
grep -v '^#' /etc/anacrontab | grep .
```

```text
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
HOME=/root
LOGNAME=root
1       5       cron.daily      run-parts --report /etc/cron.daily
7       10      cron.weekly     run-parts --report /etc/cron.weekly
@monthly        15      cron.monthly    run-parts --report /etc/cron.monthly
```

`cron.daily` läuft, wenn es einen Tag lang nicht gelaufen ist, 5 Minuten nach dem Start von
anacron.

**Die Konfiguration auf Fehler prüfen:**

```bash
sudo anacron -T && echo "anacrontab ok"
```

```text
anacrontab ok
```

**Anzeigen, wann die Jobs zuletzt liefen:**

```bash
sudo head /var/spool/anacron/*
```

```text
==> /var/spool/anacron/cron.daily <==
20261026

==> /var/spool/anacron/cron.monthly <==
20261001

==> /var/spool/anacron/cron.weekly <==
20261026
```

## Wann brauche ich das?

- Auf Servern und VMs, die nicht immer laufen, etwa Testsysteme
- Damit wöchentliche und monatliche Jobs nach einer Ausfallzeit nicht verloren gehen
- Um herauszufinden, warum tägliche Jobs zu einer unerwarteten Zeit laufen

!!! tip "Prüfen, wann ein Job zuletzt lief"
    `cat /var/spool/anacron/cron.daily` zeigt das Datum des letzten täglichen Laufs, z. B.
    `20261026`.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Vorinstalliert | nein, Paket `anacron` | nein, Paket `anacron` | ja, `cronie-anacron` | mit dem Paket `cronie` |

## Verwandte Befehle

[crontab](crontab.md) · [run-parts](run-parts.md) · [systemctl](../09-systemd/systemctl.md)
