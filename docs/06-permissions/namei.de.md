# namei

> Verfolgt einen Pfad Schritt für Schritt und zeigt Typ, Rechte und Besitzer jedes Verzeichnisses auf dem Weg.

![namei output](../assets/screenshots/06-permissions/namei.png)

## Syntax

```bash
namei [OPTION]... PFAD...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-l`, `--long` | Langes Format: Rechte, Besitzer und Gruppe (wie `-m -o`) |
| `-m`, `--modes` | Rechte anzeigen |
| `-o`, `--owners` | Besitzer und Gruppe anzeigen |
| `-n`, `--nosymlinks` | Symbolischen Links nicht folgen |
| `-x`, `--mountpoints` | Einhängepunkte mit `D` markieren |

Typen in der Ausgabe: `d` Verzeichnis, `-` Datei, `l` symbolischer Link.

## Beispiele

**Herausfinden, warum der Webserver „Permission denied“ bekommt:**

```bash
namei -l /var/www/example.com/public/index.html
```

```text
f: /var/www/example.com/public/index.html
drwxr-xr-x root     root     /
drwxr-xr-x root     root     var
drwxr-xr-x root     root     www
drwxr-x--- nox      nox      example.com
drwxr-xr-x www-data www-data public
-rw-r--r-- www-data www-data index.html
```

Die Datei selbst ist lesbar, aber `www-data` darf `example.com` nicht betreten
(`rwxr-x---`, Besitzer und Gruppe `nox`). nginx antwortet mit `403 Forbidden`.

**Nur die Rechte anzeigen:**

```bash
namei -m /etc/ssl/private/example.com.key
```

```text
f: /etc/ssl/private/example.com.key
 drwxr-xr-x /
 drwxr-xr-x etc
 drwxr-xr-x ssl
 drwx--x--- private
 -rw-r----- example.com.key
```

**Einem symbolischen Link bis zu seinem Ziel folgen:**

```bash
namei /etc/nginx/sites-enabled/example.com
```

```text
f: /etc/nginx/sites-enabled/example.com
 d /
 d etc
 d nginx
 d sites-enabled
 l example.com -> /etc/nginx/sites-available/example.com
   d /
   d etc
   d nginx
   d sites-available
   - example.com
```

**Den Teil eines Pfads finden, der nicht existiert:**

```bash
namei -l /etc/nginx/sites-enabled/exmaple.com
```

```text
f: /etc/nginx/sites-enabled/exmaple.com
drwxr-xr-x root root /
drwxr-xr-x root root etc
drwxr-xr-x root root nginx
drwxr-xr-x root root sites-enabled
                      exmaple.com - No such file or directory
```

Der Tippfehler steckt im letzten Teil des Pfads.

## Wann brauche ich das?

- Wenn ein Dienst `Permission denied` oder `403 Forbidden` meldet, obwohl die Rechte der
  Datei richtig aussehen: Oft fehlt einem Verzeichnis auf dem Weg das `x`-Recht
- Um den ganzen Pfad zu Schlüsseln, Sockets oder Upload-Verzeichnissen auf einmal zu prüfen
- Um zu sehen, wohin eine Kette symbolischer Links wirklich führt

!!! tip "Als Dienstbenutzer testen"
    Um den Zugriff direkt zu testen, führe einen Befehl als Benutzer des Dienstes aus:
    `sudo -u www-data cat /var/www/example.com/public/index.html`. Schlägt das fehl,
    kann auch nginx die Datei nicht lesen.

!!! tip "Jedes Verzeichnis braucht `x`"
    Um an eine Datei zu kommen, braucht ein Benutzer das `x`-Recht auf **jedem**
    Verzeichnis des Pfads. `namei -l` zeigt sie alle auf einen Blick.

## Verwandte Befehle

[chmod](chmod.md) · [chown](chown.md) · [realpath](../02-navigation/realpath.md)
