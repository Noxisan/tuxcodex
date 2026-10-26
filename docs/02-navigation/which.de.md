# which

> Zeigt, welche Programmdatei ausgeführt wird, wenn du einen Befehl eingibst.

![which output](../assets/screenshots/02-navigation/which.png)

## Syntax

```bash
which [-as] BEFEHL...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-a` | Alle passenden Programme in `$PATH` zeigen, nicht nur das erste |
| `-s` | Nichts ausgeben, nur den Exit-Status liefern (`0` gefunden, `1` nicht gefunden) |

## Beispiele

**Herausfinden, wo ein Programm liegt:**

```bash
which python3
```

```text
/usr/bin/python3
```

**Alle Treffer im Suchpfad anzeigen:**

```bash
which -a ls
```

```text
/usr/bin/ls
/bin/ls
```

Unter Debian ist `/bin` ein Link auf `/usr/bin`, und beide stehen in `$PATH`. Deshalb
taucht dasselbe Programm zweimal auf.

**Mehrere Befehle auf einmal prüfen:**

```bash
which git curl rsync
```

```text
/usr/bin/git
/usr/bin/curl
/usr/bin/rsync
```

**Ein Befehl, der nicht installiert ist:**

```bash
which nmap
echo $?
```

```text
1
```

**Herausfinden, was ein Befehl wirklich ist (mit `type`):**

```bash
which cd
type cd
type ls
```

```text
cd is a shell builtin
ls is aliased to `ls --color=auto'
```

`which` sucht nur nach Programmdateien. `cd` ist in die Shell eingebaut, deshalb findet
`which` nichts. Das Shell-Builtin `type` kennt auch Builtins, Aliase und Funktionen.

## Wann brauche ich das?

- Um zu prüfen, ob ein Programm installiert ist und in deinem `$PATH` liegt
- Wenn mehrere Versionen installiert sind (z. B. in `/usr/local/bin` und `/usr/bin`)
  und du wissen willst, welche ausgeführt wird
- Um den vollständigen Pfad für einen Cronjob, eine systemd-Unit oder eine
  `sudoers`-Regel zu bekommen, denn dort solltest du immer absolute Pfade verwenden

!!! tip "In Skripten: `command -v`"
    Um in einem Skript zu prüfen, ob ein Programm existiert, nimm das Shell-Builtin
    `command -v`. Es funktioniert auf jedem System gleich:

    ```bash
    if command -v docker > /dev/null; then echo "Docker is installed"; fi
    ```

!!! warning "Befehle in `/usr/sbin`"
    `which` sucht nur in den Verzeichnissen aus deinem `$PATH`. Admin-Programme wie
    `nginx` oder `sshd` liegen in `/usr/sbin`, das nicht immer im `$PATH` normaler
    Benutzer steht. `which` findet dann nichts, obwohl das Programm installiert ist.
    [`whereis`](whereis.md) findet es trotzdem.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| Programm | `which` aus `debianutils` | GNU `which` (Paket `which`) |
| Optionen | nur `-a` und `-s` | viele weitere, z. B. `--skip-alias`, `--read-functions` |
| Nicht gefunden | keine Ausgabe, Exit-Status `1` | Meldung `which: no nmap in (...)` |

## Verwandte Befehle

[find](find.md) · [locate](locate.md) · [whereis](whereis.md)
