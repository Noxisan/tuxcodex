# chattr

> Setzt besondere Dateiattribute, zum Beispiel um eine Datei gegen jede Änderung zu schützen, auch durch `root`.

![chattr output](../assets/screenshots/06-permissions/chattr.png)

## Syntax

```bash
chattr [OPTION]... [+-=]ATTRIBUTE DATEI...
```

## Optionen

| Option / Form | Beschreibung |
|---------------|--------------|
| `+i` | Datei unveränderlich machen: kein Ändern, kein Umbenennen, kein Löschen |
| `-i` | Das Attribut „unveränderlich“ entfernen |
| `+a` | Nur anhängen: Daten können nur am Ende ergänzt werden |
| `-a` | Das Attribut „nur anhängen“ entfernen |
| `-R` | Auch alle Dateien und Verzeichnisse darunter ändern |
| `-V` | Anzeigen, was geändert wird |

Setzen und Entfernen von `i` und `a` erfordert `root`.

## Beispiele

**Eine Datei gegen jede Änderung schützen:**

```bash
sudo chattr +i /etc/resolv.conf
lsattr /etc/resolv.conf
```

```text
----i---------e------- /etc/resolv.conf
```

**Jetzt kann selbst `root` sie nicht löschen:**

```bash
sudo rm /etc/resolv.conf
```

```text
rm: cannot remove '/etc/resolv.conf': Operation not permitted
```

**Und auch nicht überschreiben:**

```bash
echo "nameserver 192.0.2.53" | sudo tee /etc/resolv.conf
```

```text
tee: /etc/resolv.conf: Operation not permitted
nameserver 192.0.2.53
```

`tee` gibt die Zeile zwar auf dem Bildschirm aus, die Datei bleibt aber unverändert.

**Den Schutz wieder entfernen:**

```bash
sudo chattr -i /etc/resolv.conf
lsattr /etc/resolv.conf
```

```text
--------------e------- /etc/resolv.conf
```

**Eine Logdatei auf „nur anhängen“ setzen:**

```bash
sudo chattr +a /var/log/app/audit.log
echo "test" | sudo tee /var/log/app/audit.log
echo "test" | sudo tee -a /var/log/app/audit.log
```

```text
tee: /var/log/app/audit.log: Operation not permitted
test
test
```

Überschreiben schlägt fehl, Anhängen mit `tee -a` funktioniert.

## Wann brauche ich das?

- Um zu verhindern, dass ein Programm eine Datei überschreibt, etwa `/etc/resolv.conf`
  durch einen DHCP-Client
- Um Audit-Logs zu schützen: Mit `+a` können Einträge ergänzt, aber nicht gelöscht oder
  geändert werden
- Um wichtige Konfigurationsdateien vor versehentlichen Änderungen zu schützen, auch
  durch Admins

!!! tip "Herausfinden, warum `root` eine Datei nicht ändern kann"
    Bekommt selbst `sudo` die Meldung `Operation not permitted`, prüfe die Attribute mit
    [`lsattr`](lsattr.md). Ein `i` ist oft ein Überbleibsel von jemandem, der die Datei
    vor Jahren geschützt hat.

!!! warning "Updates scheitern an geschützten Dateien"
    `apt` kann Dateien mit `+i` weder ersetzen noch löschen. Paket-Updates brechen dann
    mit einem Fehler ab. Entferne das Attribut vor Updates, oder schütze nur Dateien, die
    kein Paket verwaltet.

!!! warning "Logrotate und `+a`"
    Eine Datei mit `+a` lässt sich weder umbenennen noch leeren, deshalb scheitert die
    Logrotation. Nimm `+a` nur für Logs, die nicht rotiert werden, oder entferne das
    Attribut im Rotationsskript.

## Verwandte Befehle

[lsattr](lsattr.md) · [chmod](chmod.md)
