# git tag

> Gibt einem Commit einen festen Namen, meist eine Versionsnummer wie v1.0.

![git-tag output](../assets/screenshots/18-git/git-tag.png)

## Syntax

```bash
git tag [-a NAME [-m "NACHRICHT"] [COMMIT]]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| (keine) | Alle Tags auflisten |
| `-a NAME` | Einen annotierten Tag mit Autor, Datum und Nachricht anlegen |
| `-m NACHRICHT` | Nachricht des Tags |
| `COMMIT` | Diesen Commit taggen statt des aktuellen |
| `-l MUSTER` | Nur Tags auflisten, die zum Muster passen, etwa `"v1.*"` |
| `-n` | Auch die Nachricht jedes Tags zeigen |
| `-d NAME` | Einen lokalen Tag löschen |

## Beispiele

**Den aktuellen Stand als neue Version taggen:**

```bash
git tag -a v1.1 -m "Service check added"
git tag -n
```

```text
v1.0            First stable version
v1.1            Service check added
```

**Einen älteren Commit taggen:**

```bash
git tag -a v0.9 0487470 -m "First scripts"
git tag -l "v0*"
```

```text
v0.9
```

**Anzeigen, worauf ein Tag zeigt:**

```bash
git show --no-patch v1.0
```

```text
tag v1.0
Tagger: Nox <nox@example.com>
Date:   Thu Oct 22 11:05:13 2026 +0200

First stable version

commit 3fcc96a03d03b18b18a33eaf4ad512124ab1d11e (tag: v1.0)
Author: Nox <nox@example.com>
Date:   Thu Oct 22 11:05:13 2026 +0200

    Also check /mnt/backup
```

**Einen Tag auf den Server schicken:**

```bash
git push origin v1.1
```

```text
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 172 bytes | 172.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To git.example.com:nox/scripts.git
 * [new tag]         v1.1 -> v1.1
```

## Wann brauche ich das?

- Um den Stand zu markieren, der in Produktion läuft, damit du ihn jederzeit wiederfindest
- Um Skripten oder Rollen Versionsnummern zu geben, auf die sich andere beziehen können
- Um nach einer missglückten Änderung schnell zu einem bekannten guten Stand zurückzukehren

!!! warning "git push schickt keine Tags"
    Ein einfaches `git push` überträgt nur Branches. Push einen Tag mit
    `git push origin v1.1` oder alle annotierten Tags zusammen mit den Commits per
    `git push --follow-tags`.

## Verwandte Befehle

[git log](git-log.md) · [git push](git-push.md) · [git switch](git-switch.md) · [git diff](git-diff.md)
