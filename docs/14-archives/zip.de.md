# zip

> Packt und komprimiert Dateien in ein ZIP-Archiv, das Format, das Windows und macOS ohne Zusatzsoftware öffnen.

![zip output](../assets/screenshots/14-archives/zip.png)

## Syntax

```bash
zip [OPTION]... ARCHIV DATEI...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-r` | Verzeichnisse rekursiv einbeziehen |
| `-q` | Still, keine Dateiliste |
| `-e` | Mit Passwort verschlüsseln (fragt danach) |
| `-x MUSTER` | Passende Dateien ausschließen |
| `-u` | Aktualisieren: nur neue und geänderte Dateien hinzufügen |
| `-9` | Stärkste Kompression |

## Beispiele

**Ein Verzeichnis packen:**

```bash
zip -r www.zip www
```

```text
  adding: www/ (stored 0%)
  adding: www/css/ (stored 0%)
  adding: www/css/style.css (deflated 53%)
  adding: www/img/ (stored 0%)
  adding: www/img/logo.png (deflated 0%)
  adding: www/index.html (deflated 76%)
```

`deflated 76%` heißt: Die Datei wurde um 76 % kleiner.

**Dateien auslassen:**

```bash
zip -r -q www-noimg.zip www -x "www/img/*"
ls -l www-noimg.zip
```

```text
-rw-r--r-- 1 nox nox 8634 Oct 26 10:42 www-noimg.zip
```

**Geänderte Dateien zu einem vorhandenen Archiv hinzufügen:**

```bash
zip -r -u www.zip www
```

```text
updating: www/index.html (deflated 76%)
```

## Wann brauche ich das?

- Um Dateien an Kunden oder Kollegen zu schicken, die mit Windows arbeiten
- Für Uploads an Systeme, die ZIP erwarten, etwa manche Webanwendungen
- Um schnell ein einzelnes Verzeichnis zu packen, ohne über tar-Optionen nachzudenken

!!! tip "Bereits komprimierte Dateien"
    `deflated 0%` bei `logo.png`: Bilder, Videos und Archive sind schon komprimiert. ZIP
    speichert sie einfach, das ist in Ordnung.

!!! tip "Nicht immer installiert"
    Fehlt der Befehl, installiere das Paket `zip` mit dem Paketmanager deiner Distribution.

!!! warning "Schwache Verschlüsselung"
    `zip -e` nutzt eine alte Verschlüsselung, die leicht zu knacken ist. Für vertrauliche Daten
    nimm `7z` mit AES oder verschlüssle das Archiv mit `gpg`.

## Verwandte Befehle

[unzip](unzip.md) · [tar](tar.md)
