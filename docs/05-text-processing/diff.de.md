# diff

> Vergleicht zwei Dateien Zeile für Zeile und zeigt genau, was sich unterscheidet.

![diff output](../assets/screenshots/05-text-processing/diff.png)

## Syntax

```bash
diff [OPTION]... DATEI1 DATEI2
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-u` | Unified-Format: Änderungen mit Kontext, `-` entfernt, `+` hinzugefügt |
| `-y`, `--side-by-side` | Beide Dateien nebeneinander anzeigen |
| `-q`, `--brief` | Nur melden, ob sich die Dateien unterscheiden |
| `-s` | Auch melden, wenn die Dateien identisch sind |
| `-r`, `--recursive` | Ganze Verzeichnisse vergleichen |
| `-i`, `--ignore-case` | Groß- und Kleinschreibung ignorieren |
| `-w`, `--ignore-all-space` | Alle Leerzeichen und Tabs ignorieren |
| `-B`, `--ignore-blank-lines` | Leere Zeilen ignorieren |
| `--color` | Entfernte Zeilen rot und hinzugefügte grün anzeigen |

## Beispiele

**Eine Konfiguration mit ihrer Sicherung vergleichen:**

```bash
diff -u /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
```

```text
--- /etc/ssh/sshd_config.bak    2026-10-26 09:58:12.000000000 +0100
+++ /etc/ssh/sshd_config        2026-10-26 10:42:03.000000000 +0100
@@ -1,5 +1,6 @@
 #Port 22
-PermitRootLogin yes
-PasswordAuthentication yes
+PermitRootLogin no
+PasswordAuthentication no
 # Logging
 LogLevel INFO
+MaxAuthTries 3
```

| Zeile | Bedeutung |
|-------|-----------|
| `---` / `+++` | Die alte und die neue Datei |
| `@@ -1,5 +1,6 @@` | Zeilen 1 bis 5 der alten Datei entsprechen Zeilen 1 bis 6 der neuen |
| `-` | Zeile wurde entfernt |
| `+` | Zeile wurde hinzugefügt |
| *(Leerzeichen)* | Unveränderte Zeile als Kontext |

**Das kurze Standardformat:**

```bash
diff /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
```

```text
2,3c2,3
< PermitRootLogin yes
< PasswordAuthentication yes
---
> PermitRootLogin no
> PasswordAuthentication no
5a6
> MaxAuthTries 3
```

`2,3c2,3` bedeutet: Zeilen 2 bis 3 wurden geändert. `5a6`: Nach Zeile 5 wurde Zeile 6
hinzugefügt.

**Beide Versionen nebeneinander anzeigen:**

```bash
diff -y -W 60 /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
```

```text
#Port 22                        #Port 22
PermitRootLogin yes          |  PermitRootLogin no
PasswordAuthentication yes   |  PasswordAuthentication no
# Logging                       # Logging
LogLevel INFO                   LogLevel INFO
                             >  MaxAuthTries 3
```

**Nur prüfen, ob sich zwei Dateien unterscheiden:**

```bash
diff -q /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
```

```text
Files /etc/ssh/sshd_config.bak and /etc/ssh/sshd_config differ
```

**Zwei Verzeichnisse vergleichen:**

```bash
diff -rq /etc/app /srv/backup/etc/app
```

```text
Files /etc/app/conf.d/app.conf and /srv/backup/etc/app/conf.d/app.conf differ
Only in /srv/backup/etc/app/conf.d: new.conf
```

**Die Ausgabe zweier Befehle vergleichen:**

```bash
diff <(ssh web1 dpkg-query -W -f='${Package}\n') <(ssh web2 dpkg-query -W -f='${Package}\n')
```

```text
2d1
< git
3a3
> rsync
```

`git` ist nur auf `web1` installiert, `rsync` nur auf `web2`. `<( )` übergibt die Ausgabe
eines Befehls an `diff`, als wäre sie eine Datei.

## Wann brauche ich das?

- Um zu prüfen, was du (oder ein Paket-Update) an einer Konfigurationsdatei geändert hast
- Um eine Konfiguration zwischen zwei Servern oder mit einem Backup zu vergleichen
- Um herauszufinden, welche Dateien in einem Verzeichnis von einem Backup abweichen
- Um Patches zu erstellen, die jemand anderes mit `patch` einspielen kann

!!! tip "Exit-Status für Skripte"
    `diff` liefert `0`, wenn die Dateien identisch sind, `1`, wenn sie sich unterscheiden,
    und `2` bei einem Fehler. Skripte können das nutzen:
    `diff -q a b > /dev/null || echo "changed"`.

!!! tip "Neue Konfigurationsdateien nach Updates"
    Hast du eine Konfiguration geändert und ein Paket-Update bringt eine neue Version mit,
    legt der Paketmanager die neue Datei neben deine (siehe Tabelle unten). Vergleiche sie
    mit `diff -u`, um zu sehen, was das Update geändert hätte.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Neue Version einer geänderten Konfiguration | `DATEI.dpkg-dist`, `DATEI.ucf-dist` | `DATEI.dpkg-dist`, `DATEI.ucf-dist` | `DATEI.rpmnew` | `DATEI.pacnew` |
| Deine alte Version nach dem Ersetzen | `DATEI.dpkg-old` | `DATEI.dpkg-old` | `DATEI.rpmsave` | `DATEI.pacsave` |

## Verwandte Befehle

[sed](sed.md) · [grep](grep.md)
