# Skripte verstehen

Ein Shell-Skript ist eine Textdatei mit Befehlen, die Bash nacheinander ausführt, genau so,
als würdest du sie eintippen. Alles, was du öfter als zweimal von Hand machst, ist ein
Kandidat für ein Skript.

## Die ersten Zeilen

```bash
#!/usr/bin/env bash
set -euo pipefail
```

| Zeile | Bedeutung |
|-------|-----------|
| `#!/usr/bin/env bash` | Der **Shebang**: welches Programm das Skript ausführt. Immer die allererste Zeile |
| `set -euo pipefail` | Bei Fehlern und nicht gesetzten Variablen abbrechen, siehe [`set`](set.md) |

Mach das Skript ausführbar und starte es mit seinem Pfad:

```text
$ chmod +x backup.sh
$ ./backup.sh
```

`./` ist nötig, weil das aktuelle Verzeichnis nicht im `PATH` steht. Skripte für alle
gehören nach `/usr/local/bin/`, dann lassen sie sich über ihren Namen aufrufen.

## Variablen

```text
$ name="tuxdex-srv"
$ echo "Host: $name"
Host: tuxdex-srv
```

Keine Leerzeichen um `=`. Lies eine Variable mit `$name` oder `${name}`, und speichere die
Ausgabe eines Befehls mit `$(befehl)`: `heute=$(date +%F)`.

## Quoting

| Anführungszeichen | Wirkung | Beispiel | Ergebnis |
|-------------------|---------|----------|----------|
| `"…"` | Variablen werden ersetzt, Leerzeichen bleiben zusammen | `"Host: $name"` | `Host: tuxdex-srv` |
| `'…'` | Alles bleibt wörtlich | `'Host: $name'` | `Host: $name` |
| keine | Wörter werden an Leerzeichen getrennt | `ls $file` mit `file="old backup.tar.gz"` | `ls` bekommt zwei Argumente |

Setze Variablen immer in doppelte Anführungszeichen: `"$file"`. Das ist die häufigste
Fehlerquelle in Shell-Skripten.

## Argumente

| Variable | Inhalt |
|----------|--------|
| `$0` | Name des Skripts |
| `$1`, `$2`, … | Erstes, zweites, … Argument |
| `$#` | Anzahl der Argumente |
| `"$@"` | Alle Argumente, jedes so, wie es übergeben wurde |
| `$?` | Exit-Code des letzten Befehls |

```text
$ ./greet.sh web01 "two words" 3
Script: ./greet.sh
First argument: web01
Number of arguments: 3
All arguments: web01 two words 3
```

## Exit-Codes

Jeder Befehl endet mit einem Exit-Code: `0` heißt Erfolg, alles andere ein Fehler.
Bedingungen in Bash prüfen genau diesen Code.

```text
$ grep -q root /etc/passwd; echo $?
0
$ grep -q nosuchuser /etc/passwd; echo $?
1
```

Auch Skripte sollten mit einem aussagekräftigen Code enden: `exit 0` bei Erfolg, `exit 1`
oder höher bei Fehlern, siehe [`exit`](exit.md).

## Ein vollständiges Beispiel

`/usr/local/bin/backup-www`:

```bash
#!/usr/bin/env bash
# Back up a directory to /mnt/backup, keep 7 days.
set -euo pipefail

src="${1:-/srv/www}"
target="/mnt/backup/$(basename "$src")-$(date +%F).tar.zst"

log() {
    logger -t backup-www "$*"
    printf '%s %s\n' "$(date +%T)" "$*"
}

if [[ ! -d "$src" ]]; then
    log "Source $src does not exist"
    exit 1
fi

log "Starting backup of $src"
tar --zstd -cf "$target" -C "$(dirname "$src")" "$(basename "$src")"
log "Created $target ($(du -h "$target" | cut -f1))"

find /mnt/backup -name "$(basename "$src")-*.tar.zst" -mtime +7 -delete
log "Done"
```

```text
$ sudo backup-www
10:42:17 Starting backup of /srv/www
10:42:19 Created /mnt/backup/www-2026-10-26.tar.zst (48M)
10:42:19 Done
```

Die Seiten dieses Kapitels erklären jeden Baustein dieses Skripts.

!!! tip "Skripte mit ShellCheck prüfen"
    [`shellcheck`](shellcheck.md) findet fehlende Anführungszeichen, Tippfehler in Variablen
    und viele andere Fehler, bevor das Skript überhaupt läuft.

!!! warning "`sh` ist nicht `bash`"
    Unter Debian und Ubuntu ist `/bin/sh` die `dash`, eine kleinere Shell ohne `[[ ]]`,
    Arrays und andere Bash-Funktionen. Ein Skript mit `#!/bin/sh`, das sie nutzt, scheitert
    mit Fehlern wie `[[: not found`. Nimm `#!/usr/bin/env bash` für Bash-Skripte.
