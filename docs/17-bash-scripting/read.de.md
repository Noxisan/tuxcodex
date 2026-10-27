# read

> Liest eine Zeile von der Tastatur oder aus einer Datei in Variablen. Für Fragen an den Benutzer und um Dateien Zeile für Zeile zu verarbeiten.

![read output](../assets/screenshots/17-bash-scripting/read.png)

## Syntax

```bash
read [OPTION]... [VARIABLE]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-p TEXT` | Eine Eingabeaufforderung zeigen |
| `-r` | Roh: Backslashes nicht als Escapes behandeln (immer nutzen) |
| `-s` | Still: die Eingabe nicht anzeigen, für Passwörter |
| `-t SEKUNDEN` | Nach dieser Zeit aufgeben |
| `-a ARRAY` | Die Wörter in ein Array lesen |
| `IFS=:` | Trennzeichen zum Aufteilen der Zeile, nur für `read` gesetzt |

## Beispiele

**Nach einem Wert fragen:**

```bash
read -r -p "Server name: " srv
echo "Connecting to $srv"
```

```text
Server name: web01
Connecting to web01
```

**Nach einer Bestätigung fragen:**

```bash
read -r -p "Really delete? [y/N] " answer
[[ "$answer" == [yY] ]] && echo "deleting" || echo "aborted"
```

```text
Really delete? [y/N] n
aborted
```

**Eine Datei Zeile für Zeile lesen:**

```bash
while read -r name ip; do
    echo "$name -> $ip"
done < hosts.txt
```

```text
web01 -> 192.0.2.10
web02 -> 192.0.2.11
```

**Zeilen an einem Trennzeichen aufteilen:**

```bash
while IFS=: read -r user _ uid _ _ home _; do
    (( uid >= 1000 && uid < 65534 )) && echo "$user $home"
done < /etc/passwd
```

```text
nox /home/nox
alice /home/alice
```

## Wann brauche ich das?

- Für Bestätigungen vor riskanten Schritten: „Wirklich löschen?“
- Um Dateien Zeile für Zeile zu verarbeiten, etwa eine Liste von Servern
- Um Zeilen in Felder aufzuteilen, etwa `/etc/passwd`

!!! tip "Immer `-r`"
    Ohne `-r` entfernt `read` Backslashes aus der Eingabe. Mit `-r` kommt jede Zeile genau so
    an, wie sie ist.

!!! warning "Nicht in unbeaufsichtigten Skripten"
    Ein Skript mit `read` wartet ewig auf eine Eingabe, wenn cron oder systemd es startet.
    Nutze `-t` oder frage nur, wenn die Standardeingabe ein Terminal ist: `[[ -t 0 ]]`.

## Verwandte Befehle

[while](while.md) · [echo](echo.md) · [cut](../05-text-processing/cut.md)
