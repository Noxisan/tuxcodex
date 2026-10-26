# journalctl

> Liest das systemd-Journal: das zentrale Log aller Dienste, des Kernels und des Bootvorgangs, gefiltert nach Dienst, Zeit oder Priorität.

![journalctl output](../assets/screenshots/09-systemd/journalctl.png)

## Syntax

```bash
journalctl [OPTION]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-u UNIT` | Nur Meldungen dieser Unit, z. B. `-u nginx` |
| `-f` | Neue Meldungen live verfolgen, wie `tail -f` |
| `-n ANZAHL` | Nur die letzten `ANZAHL` Zeilen |
| `-e` | Ans Ende des Logs springen |
| `-b`, `-b -1` | Nur der aktuelle Bootvorgang oder der davor |
| `--since`, `--until` | Zeitraum, z. B. `--since "1 hour ago"` oder `--since today` |
| `-p PRIORITÄT` | Nur diese Priorität und wichtigere, z. B. `-p err` |
| `-k` | Nur Kernelmeldungen, wie `dmesg` |
| `-r` | Neueste Meldungen zuerst |
| `--no-pager` | Alles ausgeben, statt `less` zu öffnen |
| `--disk-usage` | Anzeigen, wie viel Platz das Journal belegt |

## Beispiele

**Herausfinden, warum ein Dienst fehlgeschlagen ist:**

```bash
journalctl -u backup -n 6
```

```text
Oct 26 03:00:01 tuxcodex-srv systemd[1]: Starting backup.service - Nightly backup...
Oct 26 03:00:01 tuxcodex-srv backup.sh[4102]: dumping database shop
Oct 26 03:00:02 tuxcodex-srv backup.sh[4102]: tar: /mnt/backup/www.tar.gz: Cannot open: No space left on device
Oct 26 03:00:02 tuxcodex-srv systemd[1]: backup.service: Main process exited, code=exited, status=2/INVALIDARGUMENT
Oct 26 03:00:02 tuxcodex-srv systemd[1]: backup.service: Failed with result 'exit-code'.
Oct 26 03:00:02 tuxcodex-srv systemd[1]: Failed to start backup.service - Nightly backup.
```

Die dritte Zeile zeigt die Ursache: Die Backup-Platte ist voll.

**Das Log eines Dienstes live verfolgen:**

```bash
journalctl -u nginx -f
```

```text
Oct 26 10:42:17 tuxcodex-srv systemd[1]: Reloading nginx.service - A high performance web server and a reverse proxy server...
Oct 26 10:42:17 tuxcodex-srv systemd[1]: Reloaded nginx.service - A high performance web server and a reverse proxy server.
```

Neue Zeilen erscheinen, sobald sie geschrieben werden. Beenden mit ++ctrl+c++.

**Nur Fehler seit dem letzten Booten:**

```bash
journalctl -p err -b
```

```text
Oct 14 07:37:09 tuxcodex-srv kernel: ACPI Error: AE_NOT_FOUND, While resolving a named reference package element (20240827/dspkginit-438)
Oct 26 03:00:02 tuxcodex-srv systemd[1]: Failed to start backup.service - Nightly backup.
```

**Meldungen der letzten Stunde:**

```bash
journalctl --since "1 hour ago" -u ssh
```

```text
Oct 26 09:58:31 tuxcodex-srv sshd-session[2190]: Accepted publickey for nox from 192.0.2.45 port 51732 ssh2: ED25519 SHA256:3qN8vY1oZkT6cW2xLr5bJ9dF0hG4mA7sE1uK8pQ2iVw
Oct 26 09:58:31 tuxcodex-srv sshd-session[2190]: pam_unix(sshd:session): session opened for user nox(uid=1000) by nox(uid=0)
```

**Die aufgezeichneten Bootvorgänge auflisten:**

```bash
journalctl --list-boots
```

```text
IDX BOOT ID                          FIRST ENTRY                  LAST ENTRY
 -2 6f1c0e9a2b7d4f3e8a5c1d9b0e7f2a64 Fri 2026-09-18 09:12:44 CEST Thu 2026-10-01 06:13:40 CEST
 -1 b3a8d2e4f6c14a9b8e7d5c3f1a2b0c96 Thu 2026-10-01 06:14:52 CEST Wed 2026-10-14 07:35:58 CEST
  0 2d9e4b7a1c3f4e8d9b6a5c0e7f1d3a28 Wed 2026-10-14 07:36:52 CEST Mon 2026-10-26 10:42:17 CET
```

Mit `journalctl -b -1` liest du das Log des vorherigen Bootvorgangs, etwa um
herauszufinden, warum der Server abgestürzt ist.

**Prüfen, wie viel Platz das Journal belegt:**

```bash
journalctl --disk-usage
```

```text
Archived and active journals take up 312.4M in the file system.
```

## Wann brauche ich das?

- Wenn ein Dienst nicht startet oder immer wieder abstürzt
- Nach einem unerwarteten Neustart: Was ist direkt davor passiert (`-b -1`)?
- Um einen Dienst zu beobachten, während du eine Änderung testest (`-f`)
- Um fehlgeschlagene SSH-Anmeldungen oder andere Sicherheitsereignisse zu finden

!!! tip "Filter kombinieren"
    Die Optionen lassen sich frei kombinieren: `journalctl -u nginx -p warning --since today`
    zeigt nur die heutigen Warnungen und Fehler von nginx.

!!! tip "Die Größe begrenzen"
    `sudo journalctl --vacuum-size=500M` löscht alte archivierte Journaldateien, bis
    höchstens 500 MB übrig sind. Für eine dauerhafte Grenze setzt du `SystemMaxUse=` in
    `/etc/systemd/journald.conf`.

!!! warning "Für Systemlogs `sudo` verwenden"
    Ohne Root-Rechte siehst du nur deine eigenen Meldungen, außer du bist Mitglied der
    Gruppe `adm` oder `systemd-journal`. Ohne sie wirkt das Log leerer, als es ist.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Klassisches Textlog über rsyslog | nicht installiert | `/var/log/syslog` | `/var/log/messages` | nicht installiert |
| SSH-Dienst für `-u` | `ssh` | `ssh` | `sshd` | `sshd` |

Auf Distributionen ohne rsyslog ist das Journal das einzige Systemlog.

## Verwandte Befehle

[systemctl](systemctl.md) · [tail](../04-viewing-files/tail.md) · [less](../04-viewing-files/less.md) · [grep](../05-text-processing/grep.md)
