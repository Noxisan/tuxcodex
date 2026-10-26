# cat

> Gibt den Inhalt einer oder mehrerer Dateien aus und fügt Dateien zusammen.

![cat output](../assets/screenshots/04-viewing-files/cat.png)

## Syntax

```bash
cat [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-n`, `--number` | Alle Zeilen nummerieren |
| `-b`, `--number-nonblank` | Nur nicht leere Zeilen nummerieren |
| `-A`, `--show-all` | Versteckte Zeichen zeigen: `^I` Tab, `$` Zeilenende, `^M` Windows-Zeilenende |
| `-s`, `--squeeze-blank` | Mehrere leere Zeilen hintereinander als eine zeigen |
| `-E`, `--show-ends` | `$` am Ende jeder Zeile zeigen |
| `-T`, `--show-tabs` | Tabs als `^I` zeigen |

## Beispiele

**Eine kurze Datei anzeigen:**

```bash
cat /etc/hostname
```

```text
tuxcodex-srv
```

**Eine Datei mit Zeilennummern anzeigen:**

```bash
cat -n /etc/hosts
```

```text
     1  127.0.0.1       localhost
     2  127.0.1.1       tuxcodex-srv.example.com        tuxcodex-srv
     3
     4  # The following lines are desirable for IPv6 capable hosts
     5  ::1     localhost ip6-localhost ip6-loopback
     6  ff02::1 ip6-allnodes
     7  ff02::2 ip6-allrouters
```

**Versteckte Zeichen sichtbar machen:**

```bash
cat -A site.conf
```

```text
server {$
^Ilisten 80;$
    server_name example.com; $
}^M$
```

Jetzt siehst du den Tab (`^I`), das Leerzeichen vor dem Zeilenende und das
Windows-Zeilenende (`^M`) in der letzten Zeile.

**Geteilte Dateien wieder zusammenfügen:**

```bash
cat backup.sql.part-aa backup.sql.part-ab > backup.sql
ls -lh backup.sql*
```

```text
-rw-r--r-- 1 nox nox 1.5G Oct 26 10:42 backup.sql
-rw-r--r-- 1 nox nox 1.0G Oct 26 10:30 backup.sql.part-aa
-rw-r--r-- 1 nox nox 512M Oct 26 10:30 backup.sql.part-ab
```

**Den öffentlichen SSH-Schlüssel zum Kopieren anzeigen:**

```bash
cat ~/.ssh/id_ed25519.pub
```

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIExampleKeyOnlyForThisHandbook0123456789ab nox@tuxcodex-srv
```

## Wann brauche ich das?

- Um kurze Konfigurationsdateien wie `/etc/hostname` oder `/etc/hosts` schnell anzusehen
- Um einen öffentlichen Schlüssel oder eine kurze Konfiguration in ein Ticket oder auf
  einen anderen Server zu kopieren
- Um unsichtbare Probleme wie Tabs, Leerzeichen am Zeilenende oder Windows-Zeilenenden
  zu finden (`-A`)
- Um Dateien zusammenzufügen, zum Beispiel geteilte Backups

!!! tip "Lange Dateien gehören in `less`"
    `cat` gibt alles auf einmal aus, lange Dateien rauschen einfach durch. Für alles, was
    länger als ein Bildschirm ist, nimm [`less`](less.md).

!!! warning "Binärdateien bringen das Terminal durcheinander"
    `cat` auf eine Binärdatei kann Steuerzeichen ausgeben, die das Terminal in einen
    seltsamen Zustand versetzen. Tippe `reset` und drücke ++enter++, auch wenn du nicht
    siehst, was du tippst. Prüfe unbekannte Dateien vorher mit [`file`](../03-files/file.md).

## Verwandte Befehle

[file](../03-files/file.md) · [tac](tac.md) · [nl](nl.md) · [less](less.md) · [head](head.md)
