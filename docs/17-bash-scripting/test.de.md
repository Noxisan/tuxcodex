# test

> Prüft eine Bedingung und liefert Exit-Code `0` (wahr) oder `1` (falsch). Meist geschrieben als `[ … ]` oder, in Bash, als `[[ … ]]`.

![test output](../assets/screenshots/17-bash-scripting/test.png)

## Syntax

```bash
[[ AUSDRUCK ]]
[ AUSDRUCK ]
test AUSDRUCK
```

`[[ ]]` ist die Bash-Variante: keine Probleme mit Worttrennung, Muster und `&&` innerhalb der Klammern. Nutze sie in Bash-Skripten. Die Leerzeichen nach `[[` und vor `]]` sind Pflicht.

## Optionen

| Ausdruck | Wahr, wenn |
|----------|------------|
| `-f DATEI` | Die Datei existiert und ist eine normale Datei |
| `-d VERZ` | Das Verzeichnis existiert |
| `-e PFAD` | Der Pfad existiert |
| `-x DATEI` | Die Datei ist ausführbar |
| `-z "$VAR"`, `-n "$VAR"` | Die Zeichenkette ist leer, nicht leer |
| `"$a" == "$b"`, `!=` | Zeichenketten sind gleich, verschieden |
| `$a -eq $b`, `-ne`, `-lt`, `-gt`, `-le`, `-ge` | Zahlenvergleiche |
| `[[ $a == muster* ]]` | Mustervergleich (nur `[[ ]]`) |
| `!`, `&&`, `\|\|` | Nicht, und, oder |

## Beispiele

**Prüfen, ob eine Datei existiert:**

```bash
[[ -f /etc/nginx/nginx.conf ]] && echo "config found"
```

```text
config found
```

**Ein Verzeichnis anlegen, falls es fehlt:**

```bash
[[ -d /mnt/backup/daily ]] || mkdir -p /mnt/backup/daily
ls -d /mnt/backup/daily
```

```text
/mnt/backup/daily
```

**Mit einem Muster vergleichen:**

```bash
host=web01
[[ $host == web* ]] && echo "$host is a web server"
```

```text
web01 is a web server
```

**Der Exit-Code einer falschen Bedingung:**

```bash
[[ "a" == "b" ]]; echo $?
```

```text
1
```

**Ein klassischer Fehler mit `[`:**

```bash
count=""
[ $count -gt 0 ]
```

```text
bash: [: -gt: unary operator expected
```

Die leere Variable verschwindet, und `[` sieht nur `-gt 0`. Mit `[[ ]]` oder Anführungszeichen
passiert das nicht.

## Wann brauche ich das?

- Bevor du eine Datei oder ein Verzeichnis nutzt: Gibt es sie?
- Um Argumente und Variablen am Anfang eines Skripts zu prüfen
- Zusammen mit [`if`](if.md), `&&` und `||`

!!! tip "Für Zahlen `-eq` nutzen"
    `==` vergleicht Zeichenketten: `[[ 10 == 10.0 ]]` ist falsch. Für Zahlen nimm `-eq`, `-lt`
    und Co. oder Arithmetik mit `(( a < b ))`.

!!! warning "Leerzeichen sind Pflicht"
    `[[$x == 1]]` scheitert mit `command not found`. Klammern und Operatoren müssen durch
    Leerzeichen getrennt sein: `[[ $x == 1 ]]`.

## Verwandte Befehle

[if](if.md) · [case](case.md) · [while](while.md) · [shellcheck](shellcheck.md)
