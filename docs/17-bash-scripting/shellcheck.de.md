# shellcheck

> Prüft Shell-Skripte auf Fehler und riskante Konstrukte, bevor sie laufen: fehlende Anführungszeichen, nicht gesetzte Variablen, Tippfehler und viele klassische Fallen.

![shellcheck output](../assets/screenshots/17-bash-scripting/shellcheck.png)

## Syntax

```bash
shellcheck [OPTION]... SKRIPT...
```

Jeder Fund hat einen Code wie `SC2086`. `https://www.shellcheck.net/wiki/SC2086` erklärt ihn mit Beispielen.

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-f gcc` | Kurze Ausgabe, eine Zeile pro Fund |
| `-S warning` | Nur Warnungen und Fehler, keine Stilhinweise |
| `-e SC2086` | Diese Prüfung ignorieren |
| `-x` | Mit `source` geladenen Dateien folgen |

## Beispiele

**Ein Skript prüfen:**

```bash
shellcheck compress-logs.sh
```

```text

In compress-logs.sh line 3:
cd $dir
^-----^ SC2164 (warning): Use 'cd ... || exit' or 'cd ... || return' in case cd fails.
   ^--^ SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean:
cd "$dir" || exit


In compress-logs.sh line 4:
for f in $(ls *.log); do
         ^---------^ SC2045 (error): Iterating over ls output is fragile. Use globs.
              ^-- SC2035 (info): Use ./*glob* or -- *glob* so names with dashes won't become options.


In compress-logs.sh line 6:
  gzip $f
       ^-- SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean:
  gzip "$f"


In compress-logs.sh line 8:
if [ $count -gt 0 ]; then echo "finished"; fi
     ^----^ SC2154 (warning): count is referenced but not assigned.
     ^----^ SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean:
if [ "$count" -gt 0 ]; then echo "finished"; fi

For more information:
  https://www.shellcheck.net/wiki/SC2045 -- Iterating over ls output is fragi...
  https://www.shellcheck.net/wiki/SC2154 -- count is referenced but not assig...
  https://www.shellcheck.net/wiki/SC2164 -- Use 'cd ... || exit' or 'cd ... |...
```

**Das geprüfte Skript:**

```bash
cat compress-logs.sh
```

```text
#!/usr/bin/env bash
dir=$1
cd $dir
for f in $(ls *.log); do
  echo "Compressing $f"
  gzip $f
done
if [ $count -gt 0 ]; then echo "finished"; fi
```

**Kurze Ausgabe, eine Zeile pro Fund:**

```bash
shellcheck -f gcc compress-logs.sh
```

```text
compress-logs.sh:3:1: warning: Use 'cd ... || exit' or 'cd ... || return' in case cd fails. [SC2164]
compress-logs.sh:3:4: note: Double quote to prevent globbing and word splitting. [SC2086]
compress-logs.sh:4:10: error: Iterating over ls output is fragile. Use globs. [SC2045]
compress-logs.sh:4:15: note: Use ./*glob* or -- *glob* so names with dashes won't become options. [SC2035]
compress-logs.sh:6:8: note: Double quote to prevent globbing and word splitting. [SC2086]
compress-logs.sh:8:6: warning: count is referenced but not assigned. [SC2154]
compress-logs.sh:8:6: note: Double quote to prevent globbing and word splitting. [SC2086]
```

**Nur Warnungen und Fehler:**

```bash
shellcheck -S warning -f gcc compress-logs.sh
```

```text
compress-logs.sh:3:1: warning: Use 'cd ... || exit' or 'cd ... || return' in case cd fails. [SC2164]
compress-logs.sh:4:10: error: Iterating over ls output is fragile. Use globs. [SC2045]
compress-logs.sh:8:6: warning: count is referenced but not assigned. [SC2154]
```

## Wann brauche ich das?

- Bevor du ein neues Skript auf einem Server einsetzt
- In CI-Pipelines, damit fehlerhafte Skripte vor dem Ausrollen auffallen
- Wenn sich ein Skript seltsam verhält und du nicht weißt, warum

!!! tip "Einen Fund bewusst ignorieren"
    Ist ein Fund gewollt, schreib `# shellcheck disable=SC2086` in die Zeile darüber. Der Kommentar
    dokumentiert zugleich, dass es eine Entscheidung war und kein Versehen.

!!! tip "Im Editor"
    Plugins für VS Code, Vim und andere Editoren zeigen ShellCheck-Funde schon beim Tippen.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Paket | `shellcheck` | `shellcheck` | aus EPEL | `shellcheck` |

## Verwandte Befehle

[set](set.md) · [test](test.md) · [for](for.md)
