# nl

> Gibt eine Datei mit Zeilennummern aus und lässt dich genau festlegen, welche Zeilen wie nummeriert werden.

![nl output](../assets/screenshots/04-viewing-files/nl.png)

## Syntax

```bash
nl [OPTION]... [DATEI]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-b a` | Alle Zeilen nummerieren, auch leere |
| `-b t` | Nur Zeilen mit Text nummerieren (Standard) |
| `-n ln` / `rn` / `rz` | Format der Nummer: linksbündig, rechtsbündig (Standard), rechtsbündig mit führenden Nullen |
| `-w N` | Breite der Zeilennummer (Standard `6`) |
| `-s TEXT` | Text zwischen Nummer und Zeile (Standard ein Tab) |
| `-v N` | Mit `N` zu zählen beginnen |

## Beispiele

**Alle Zeilen mit Text nummerieren:**

```bash
nl /etc/hosts
```

```text
     1  127.0.0.1       localhost
     2  127.0.1.1       tuxcodex-srv.example.com        tuxcodex-srv

     3  # The following lines are desirable for IPv6 capable hosts
     4  ::1     localhost ip6-localhost ip6-loopback
     5  ff02::1 ip6-allnodes
     6  ff02::2 ip6-allrouters
```

Anders als `cat -n` überspringt `nl` leere Zeilen standardmäßig.

**Auch leere Zeilen nummerieren:**

```bash
nl -b a /etc/hosts
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

**Ein kompaktes Format wählen:**

```bash
nl -w 2 -s ': ' deploy.log
```

```text
 1: 2026-10-26 10:40:01 deploy started
 2: 2026-10-26 10:40:12 files copied
 3: 2026-10-26 10:40:15 service restarted
```

**Nummern mit führenden Nullen:**

```bash
nl -n rz -w 3 -s ' ' deploy.log
```

```text
001 2026-10-26 10:40:01 deploy started
002 2026-10-26 10:40:12 files copied
003 2026-10-26 10:40:15 service restarted
```

## Wann brauche ich das?

- Wenn eine Fehlermeldung eine Zeilennummer nennt, zum Beispiel
  `nginx: [emerg] ... in /etc/nginx/sites-enabled/example.com:12`, und du diese Zeile
  finden willst
- Um bei der Besprechung einer Konfiguration auf genaue Zeilen zu verweisen
- Um Listen oder Log-Ausschnitte für einen Bericht zu nummerieren

!!! tip "Dieselben Nummern wie in der Fehlermeldung"
    Fehlermeldungen zählen **alle** Zeilen, auch leere. Nimm `nl -b a` oder `cat -n`,
    damit die Nummern übereinstimmen.

!!! tip "Zeilennummern in `less`"
    `less -N DATEI` zeigt ebenfalls Zeilennummern, und du kannst gleichzeitig blättern
    und suchen.

## Verwandte Befehle

[cat](cat.md) · [less](less.md)
