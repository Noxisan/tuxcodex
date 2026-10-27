# sha256sum

> Berechnet SHA-256-Prüfsummen und prüft Dateien dagegen. Belegt, dass eine Datei ohne jede Änderung angekommen ist oder gespeichert wurde.

![sha256sum output](../assets/screenshots/14-archives/sha256sum.png)

## Syntax

```bash
sha256sum [OPTION]... [DATEI]...
```

`md5sum` und `sha1sum` funktionieren genauso, gelten aber als unsicher. Nimm SHA-256.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Prüfsumme und Dateinamen ausgeben |
| `-c DATEI` | Die in `DATEI` aufgeführten Dateien prüfen |
| `--quiet` | Mit `-c`: nur Fehler melden |
| `--ignore-missing` | Mit `-c`: Dateien überspringen, die es nicht gibt |

## Beispiele

**Prüfsummen berechnen und speichern:**

```bash
sha256sum www.tar.gz db.sql.zst | tee backup.sha256
```

```text
3f8b2c9e71d4a6052be19f03c7d86a4e5b21f0c9d38e7a6b4c05f19e2d7a8b36  www.tar.gz
9c41e07b2a8d5f63e1b0c4a7d92f8e5b06a3c1d7e4f29b8a05c6d3e1f7a2b490  db.sql.zst
```

**Die Dateien auf dem Zielserver prüfen:**

```bash
sha256sum -c backup.sha256
```

```text
www.tar.gz: OK
db.sql.zst: OK
```

**Eine beschädigte Datei:**

```bash
sha256sum -c backup.sha256
```

```text
www.tar.gz: OK
db.sql.zst: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

`db.sql.zst` wurde beim Übertragen verändert oder beschädigt. Kopiere sie erneut.

## Wann brauche ich das?

- Nachdem ein Backup auf einen anderen Server kopiert wurde, um sicherzugehen, dass es heil ankam
- Um einen Download gegen die Prüfsumme zu prüfen, die der Hersteller veröffentlicht
- Um später zu bemerken, ob ein Archiv beschädigt wurde

!!! tip "Die Prüfsumme beim Backup aufbewahren"
    Schreib die Prüfsumme in eine Datei neben dem Archiv: `sha256sum www.tar.gz > www.tar.gz.sha256`.
    Vor dem Zurückspielen sagt dir `sha256sum -c`, ob das Archiv noch intakt ist.

!!! warning "Prüfsummen erkennen nur, sie schützen nicht"
    Wer die Datei ändern kann, kann auch die Prüfsummendatei daneben ändern. Vergleiche
    Downloads mit einer Prüfsumme aus vertrauenswürdiger Quelle, am besten mit GPG signiert.

## Verwandte Befehle

[tar](tar.md) · [rsync](../12-ssh/rsync.md) · [scp](../12-ssh/scp.md)
