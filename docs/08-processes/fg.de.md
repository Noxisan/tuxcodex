# fg

> Holt einen Hintergrund- oder angehaltenen Job in den Vordergrund zurück, damit du ihn siehst und bedienen kannst.

![fg output](../assets/screenshots/08-processes/fg.png)

## Syntax

```bash
fg [%JOB]
```

Ohne Job nimmt `fg` den aktuellen Job (`+` bei [`jobs`](jobs.md)).

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `%NUMMER` | Der Job mit dieser Nummer, z. B. `%2` |
| `%TEXT` | Der Job, dessen Befehl mit `TEXT` beginnt, z. B. `%vim` |

## Beispiele

**Zum angehaltenen Editor zurückkehren:**

```bash
fg
```

```text
vim /etc/nginx/nginx.conf
```

`fg` gibt den Befehl aus und setzt ihn fort. Der Editor füllt wieder das Terminal, genau
an der Stelle, an der du ihn verlassen hast.

**Einen Hintergrundjob in den Vordergrund holen:**

```bash
fg %1
```

```text
tar -czf /mnt/backup/www.tar.gz /srv/www
```

Die Shell wartet jetzt wieder auf den Job. Zum Abbrechen drücke ++ctrl+c++, zum erneuten
Anhalten ++ctrl+z++.

**Einen Job über seinen Befehl auswählen:**

```bash
fg %vim
```

```text
vim /etc/nginx/nginx.conf
```

**Eine Jobnummer, die es nicht gibt:**

```bash
fg %7
```

```text
bash: fg: %7: no such job
```

## Wann brauche ich das?

- Um zu einem Editor oder einem `less` zurückzukehren, das du mit ++ctrl+z++ angehalten hast
- Um die Ausgabe eines Hintergrundjobs zu sehen oder ihn mit ++ctrl+c++ abzubrechen
- Wenn ein Hintergrundjob angehalten hat, weil er auf eine Eingabe wartet

!!! tip "Beim Bearbeiten schnell etwas nachsehen"
    Drücke in `vim` ++ctrl+z++, prüfe etwas in der Shell und kehre mit `fg` zurück. Das
    geht schneller, als die Datei zu schließen und neu zu öffnen.

!!! warning "Vergessene angehaltene Jobs"
    Willst du dich mit angehaltenen Jobs abmelden, warnt die Bash einmal:
    `There are stopped jobs.` Meldest du dich trotzdem ab, werden sie beendet, und nicht
    gespeicherte Änderungen in einem Editor sind verloren.

## Verwandte Befehle

[jobs](jobs.md) · [bg](bg.md) · [kill](kill.md)
