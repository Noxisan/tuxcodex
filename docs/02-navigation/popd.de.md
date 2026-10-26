# popd

> Nimmt das oberste Verzeichnis vom Stapel und wechselt zurück ins nächste.

## Syntax

```bash
popd [-n] [+N | -N]
```

## Optionen

| Option / Argument | Beschreibung |
|-------------------|--------------|
| *(keins)* | Obersten Eintrag entfernen und ins neue oberste Verzeichnis wechseln |
| `+N` | Eintrag `N` (von links gezählt, ab 0) entfernen, ohne das Verzeichnis zu wechseln |
| `-N` | Wie `+N`, aber von rechts gezählt |
| `-n` | Nur den Stapel ändern, nicht das Verzeichnis wechseln |

Den Stapel füllst du mit [`pushd`](pushd.md), anzeigen lässt er sich mit `dirs`.

## Beispiele

**Dorthin zurückkehren, wo du hergekommen bist:**

```bash
pushd /etc/nginx
popd
```

```text
/etc/nginx ~
~
```

**Den Stapel Schritt für Schritt zurückgehen:**

```bash
dirs
popd
popd
```

```text
/var/log/nginx /etc/nginx ~
/etc/nginx ~
~
```

**Einen Eintrag vom Stapel entfernen, ohne das Verzeichnis zu wechseln:**

```bash
dirs
popd +1
```

```text
/var/log/nginx /etc/nginx ~
/var/log/nginx ~
```

**`popd` bei leerem Stapel aufrufen:**

```bash
popd
```

```text
-bash: popd: directory stack empty
```

**In einem Skript in einem anderen Verzeichnis arbeiten und danach zurückkehren:**

```bash
pushd /var/www/example.com > /dev/null || exit 1
git pull
popd > /dev/null
```

```text
Already up to date.
```

![popd output](../assets/screenshots/02-navigation/popd.png)

## Wann brauche ich das?

- Um nach der Arbeit in mehreren Verzeichnissen mit `pushd` zum Ausgangspunkt
  zurückzukehren
- In Skripten, die einen Befehl in einem anderen Verzeichnis ausführen und danach dort
  weitermachen, wo sie waren
- Um den Verzeichnisstapel aufzuräumen (`popd +N`)

!!! tip "Die Ausgabe in Skripten unterdrücken"
    `pushd` und `popd` geben immer den Stapel aus. Leite ihn in Skripten mit
    `> /dev/null` um, damit nur die Ausgabe deiner eigenen Befehle sichtbar ist.

!!! warning "`popd` ohne passendes `pushd`"
    Ist der Stapel leer, schlägt `popd` fehl, und das Verzeichnis bleibt gleich. In
    Skripten sollte zu jedem `pushd` genau ein `popd` gehören.

## Verwandte Befehle

[pushd](pushd.md) · [cd](cd.md)
