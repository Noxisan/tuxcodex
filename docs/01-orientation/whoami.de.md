# whoami

> Zeigt den Namen des Benutzers an, als der du gerade angemeldet bist.

## Syntax

```bash
whoami
```

## Beispiel

```bash
whoami
```

```text
nox
```

![whoami im Terminal](../assets/screenshots/whoami.png)

## Wann brauche ich das?

- Nach `su` oder `sudo -i`, um zu prüfen, als welcher Benutzer du arbeitest
- In Skripten, um sicherzustellen, dass sie nicht versehentlich als root laufen

!!! tip "Gut zu wissen"
    `whoami` zeigt den **effektiven** Benutzer. Bei `sudo whoami` lautet die Ausgabe `root`.

## Verwandte Befehle

[id](id.md) · [hostname](hostname.md)
