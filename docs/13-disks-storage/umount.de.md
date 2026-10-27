# umount

> Hängt ein Dateisystem aus, damit die Platte sicher entfernt, geprüft oder geändert werden kann.

![umount output](../assets/screenshots/13-disks-storage/umount.png)

## Syntax

```bash
umount [OPTION]... EINHÄNGEPUNKT | GERÄT
```

Der Befehl heißt `umount`, ohne das erste `n`.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `EINHÄNGEPUNKT` | Das dort eingehängte Dateisystem aushängen |
| `-l` | Lazy: jetzt lösen, aufräumen, sobald es nicht mehr benutzt wird |
| `-R` | Auch alles darunter Eingehängte aushängen |
| `-f` | Erzwingen, vor allem für unerreichbare Netzwerkdateisysteme |

## Beispiele

**Ein Dateisystem aushängen:**

```bash
sudo umount /mnt/archive && echo "unmounted"
```

```text
unmounted
```

**Das Dateisystem wird noch benutzt:**

```bash
sudo umount /mnt/backup
```

```text
umount: /mnt/backup: target is busy.
```

**Die blockierenden Prozesse finden:**

```bash
sudo fuser -vm /mnt/backup
```

```text
                     USER        PID ACCESS COMMAND
/mnt/backup:         root     kernel mount /mnt/backup
                     nox        2201 ..c.. bash
                     nox        4415 F.... rsync
```

`c` heißt: Die Shell hat dort ihr Arbeitsverzeichnis, `F`: `rsync` hat eine Datei offen.
Verlass das Verzeichnis und lass `rsync` fertig werden, dann klappt `umount`.

## Wann brauche ich das?

- Bevor du ein Dateisystem mit `fsck` prüfst oder verkleinerst
- Bevor du eine Platte entfernst oder abhängst
- Wenn ein Einhängepunkt für etwas anderes frei werden soll

!!! tip "Herausfinden, wer blockiert"
    `target is busy` heißt: Ein Prozess hat dort eine Datei offen, oder eine Shell steht im
    Verzeichnis. [`lsof +D`](../08-processes/lsof.md) oder `fuser -vm` zeigen, welcher.

!!! warning "`-l` verdeckt das Problem"
    Ein Lazy-Unmount löst den Einhängepunkt sofort, aber die Prozesse schreiben weiter auf
    die Platte. Entferne die Platte erst, wenn sie beendet sind.

## Verwandte Befehle

[mount](mount.md) · [lsof](../08-processes/lsof.md) · [fsck](fsck.md)
