# echo

> Gibt Text und Variablen aus. Der einfachste Weg, damit ein Skript meldet, was es gerade tut.

![echo output](../assets/screenshots/17-bash-scripting/echo.png)

## Syntax

```bash
echo [OPTION]... [TEXT]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n` | Kein Zeilenumbruch am Ende |
| `-e` | Escapes wie `\n` (neue Zeile) und `\t` (Tab) auswerten |
| `>&2` | Auf die Standardfehlerausgabe statt der Standardausgabe schreiben |

## Beispiele

**Text mit einer Variable ausgeben:**

```bash
echo "Hello, $USER"
```

```text
Hello, nox
```

**Mehrere Zeilen mit `-e`:**

```bash
echo -e "line 1\nline 2"
```

```text
line 1
line 2
```

**Eine Zeile an eine Datei anhängen:**

```bash
echo "192.0.2.20 db01" | sudo tee -a /etc/hosts
```

```text
192.0.2.20 db01
```

`sudo echo ... >> /etc/hosts` funktioniert nicht, weil die Umleitung als dein Benutzer läuft.
`tee -a` mit `sudo` schon.

**Eine Fehlermeldung auf der Standardfehlerausgabe:**

```bash
echo "backup failed: disk full" >&2
```

```text
backup failed: disk full
```

## Wann brauche ich das?

- Um in einem Skript den Fortschritt zu melden
- Um eine Zeile in eine Datei zu schreiben: `echo "text" >> datei`
- Um Fehlermeldungen auf die Standardfehlerausgabe zu schreiben, wo sie sich nicht mit der Ausgabe mischen

!!! tip "Fehler auf die Standardfehlerausgabe"
    `echo "Fehler" >&2` schreibt auf die Standardfehlerausgabe. Leitet jemand die Ausgabe deines
    Skripts in eine Datei um, erscheinen die Fehlermeldungen trotzdem auf dem Bildschirm.

!!! warning "`echo` ist nicht portabel"
    `echo -e` und `echo -n` verhalten sich in anderen Shells und mit `/bin/sh` unterschiedlich.
    Für formatierte oder exakte Ausgaben nimm [`printf`](printf.md).

## Verwandte Befehle

[printf](printf.md) · [read](read.md) · [tee](../05-text-processing/tee.md)
