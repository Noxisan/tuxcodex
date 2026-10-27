# run-parts

> Führt alle ausführbaren Skripte in einem Verzeichnis nacheinander aus. So funktionieren `/etc/cron.daily/` und die anderen Zeitraum-Verzeichnisse.

![run-parts output](../assets/screenshots/16-scheduling/run-parts.png)

## Syntax

```bash
run-parts [OPTION]... VERZEICHNIS
```

`run-parts` ignoriert Dateinamen mit Punkt, `backup.sh` wird also übersprungen. Benenne Skripte in diesen Verzeichnissen ohne Endung, z. B. `backup-check`.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `--test` | Nur zeigen, welche Skripte laufen würden |
| `--list` | Alle Skripte auflisten, die den Namensregeln entsprechen |
| `--report` | Vor der Ausgabe eines Skripts seinen Namen ausgeben |
| `--exit-on-error` | Beim ersten fehlgeschlagenen Skript aufhören |

## Beispiele

**Anzeigen, welche täglichen Skripte laufen würden:**

```bash
run-parts --test /etc/cron.daily
```

```text
/etc/cron.daily/apt-compat
/etc/cron.daily/backup-check
/etc/cron.daily/dpkg
```

**Ein Skript mit Endung wird ignoriert:**

```bash
ls /etc/cron.daily
run-parts --test /etc/cron.daily
```

```text
apt-compat  backup-check  cleanup.sh  dpkg
/etc/cron.daily/apt-compat
/etc/cron.daily/backup-check
/etc/cron.daily/dpkg
```

`cleanup.sh` fehlt in der Liste. Benenne es in `cleanup` um.

**Alle täglichen Skripte jetzt ausführen:**

```bash
sudo run-parts --report /etc/cron.daily
```

```text
/etc/cron.daily/backup-check:
last backup: 2026-10-26 03:30, 48 MiB, OK
```

## Wann brauche ich das?

- Um zu prüfen, welche täglichen, wöchentlichen oder monatlichen Skripte laufen
- Wenn ein Skript in `/etc/cron.daily/` nicht läuft: Ist es ausführbar, und ist der Name gültig?
- Um die täglichen Skripte von Hand zu testen

!!! warning "Keine Punkte im Namen"
    Ein Skript namens `backup-check.sh` ignoriert `run-parts` unter Debian und Ubuntu
    kommentarlos. `run-parts --test` zeigt, ob ein Skript erfasst wird.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Ignoriert Namen mit Punkt | ja | ja | nein | nein |

## Verwandte Befehle

[crontab](crontab.md) · [anacron](anacron.md)
