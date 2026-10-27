# atq

> Listet die Jobs auf, die in der Warteschlange von `at` warten, mit Jobnummer, Zeit, Warteschlange und Benutzer.

![atq output](../assets/screenshots/16-scheduling/atq.png)

## Syntax

```bash
atq [OPTION]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| *(keine)* | Die eigenen Jobs; als root die Jobs aller Benutzer |
| `-q WARTESCHLANGE` | Nur eine Warteschlange, z. B. `a` für `at` oder `b` für `batch` |
| `at -c NUMMER` | Den vollständigen Inhalt eines Jobs zeigen |

## Beispiele

**Alle wartenden Jobs anzeigen:**

```bash
sudo atq
```

```text
5       Mon Oct 26 22:00:00 2026 a nox
6       Mon Oct 26 12:42:00 2026 a root
7       Tue Oct 27 09:00:00 2026 a nox
```

Die Spalten: Jobnummer, Zeit, Warteschlange (`a` für `at`), Benutzer.

**Den Befehl eines Jobs anzeigen:**

```bash
at -c 5 | tail -n 2
```

```text
}
/usr/local/bin/report.sh
```

**Keine wartenden Jobs:**

```bash
atq | wc -l
```

```text
0
```

## Wann brauche ich das?

- Um zu prüfen, ob ein geplanter Job in der Warteschlange steht
- Bevor du einen Job mit `atrm` entfernst, um seine Nummer zu finden
- Um zu sehen, was andere Admins eingeplant haben (als root)

!!! tip "Sehen, was ein Job wirklich tut"
    `at -c` zeigt den ganzen Job, samt aller Umgebungsvariablen, die `at` gespeichert hat. Der
    eigentliche Befehl steht ganz am Ende.

## Verwandte Befehle

[at](at.md) · [atrm](atrm.md) · [batch](batch.md)
