# ncdu

> Eine interaktive Variante von `du`: zeigt die größten Verzeichnisse als Liste mit Balken, lässt dich hineinwechseln und Dateien direkt löschen.

![ncdu output](../assets/screenshots/13-disks-storage/ncdu.png)

## Syntax

```bash
ncdu [OPTION]... [VERZEICHNIS]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-x` | Auf diesem Dateisystem bleiben |
| `-o DATEI` | Scannen und das Ergebnis in eine Datei speichern |
| `-f DATEI` | Einen gespeicherten Scan anzeigen |
| `--exclude MUSTER` | Passende Dateien und Verzeichnisse überspringen |
| `-r` | Nur lesen: Löschen ist abgeschaltet |

Tasten in `ncdu`: ++arrow-up++ ++arrow-down++ auswählen, ++enter++ ein Verzeichnis öffnen, ++arrow-left++ zurück, ++d++ löschen, ++g++ Balken umschalten, ++q++ beenden.

## Beispiele

**Ein Verzeichnis untersuchen:**

```bash
sudo ncdu -x /var
```

```text
ncdu 1.22 ~ Use the arrow keys to navigate, press ? for help
--- /var ------------------------------------------------------------------------
    1.3 GiB [##########] /log
  612.4 MiB [####      ] /lib
  402.1 MiB [###       ] /cache
   48.2 MiB [          ] /backups
    1.1 MiB [          ] /spool
   16.0 KiB [          ] /tmp
e   4.0 KiB [          ] /opt
e   4.0 KiB [          ] /local
@   0.0   B [          ]  lock
@   0.0   B [          ]  run




 Total disk usage:   2.3 GiB  Apparent size:   2.2 GiB  Items: 18342
```

`e` markiert leere Verzeichnisse, `@` symbolische Links.

**Mit ++enter++ in ein Verzeichnis wechseln:**

```bash
sudo ncdu /var/log/nginx
```

```text
ncdu 1.22 ~ Use the arrow keys to navigate, press ? for help
--- /var/log/nginx --------------------------------------------------------------
/..
    4.0 GiB [##########]  access.log.1
    1.0 GiB [##        ]  access.log
   48.1 MiB [          ]  error.log
    3.2 MiB [          ]  access.log.2.gz




 Total disk usage:   5.1 GiB  Apparent size:   5.1 GiB  Items: 5
```

Ein altes Log mit 4 GiB, das logrotate nicht komprimiert hat. Ein guter Kandidat zum Löschen.

**Einen Scan speichern und später öffnen:**

```bash
sudo ncdu -x -o /tmp/root.ncdu /
ls -lh /tmp/root.ncdu
```

```text
-rw-r--r-- 1 root root 3.1M Oct 26 10:42 /tmp/root.ncdu
```

## Wann brauche ich das?

- Wenn eine Platte voll ist und du die Ursache schnell finden willst
- Zum interaktiven Aufräumen: in große Verzeichnisse wechseln und alte Dateien löschen
- Auf Servern, auf denen du das Ergebnis später wieder brauchst: einmal mit `-o` scannen

!!! tip "Einmal scannen, später ansehen"
    `sudo ncdu -x -o /tmp/root.ncdu /` scannt im Hintergrund. `ncdu -f /tmp/root.ncdu`
    öffnet das Ergebnis so oft du willst, ohne neu zu scannen.

!!! warning "Löschen mit ++d++"
    `ncdu` fragt vor dem Löschen nach, löscht dann aber wirklich. Mit `sudo` kann es auch
    Systemdateien löschen. Nimm `-r`, wenn du nur schauen willst.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Vorinstalliert | nein, `sudo apt install ncdu` | nein, `sudo apt install ncdu` | nein, aus EPEL | nein, `sudo pacman -S ncdu` |

## Verwandte Befehle

[du](du.md) · [df](df.md)
