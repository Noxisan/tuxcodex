# id

> Zeigt Benutzer-ID, Gruppen-ID und alle Gruppenmitgliedschaften eines Benutzers an.

## Syntax

```bash
id [OPTION]... [BENUTZER]...
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-u`, `--user` | Nur die effektive Benutzer-ID ausgeben |
| `-g`, `--group` | Nur die effektive Gruppen-ID ausgeben |
| `-G`, `--groups` | Alle Gruppen-IDs ausgeben |
| `-n`, `--name` | Namen statt Zahlen ausgeben (zusammen mit `-u`, `-g` oder `-G`) |
| `-r`, `--real` | Die reale statt der effektiven ID ausgeben (zusammen mit `-u`, `-g` oder `-G`) |

## Beispiele

**Alles über den eigenen Benutzer anzeigen:**

```bash
id
```

```text
uid=1000(nox) gid=1000(nox) groups=1000(nox),27(sudo),100(users)
```

**Einen anderen Benutzer prüfen, zum Beispiel den Webserver-Benutzer:**

```bash
id www-data
```

```text
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

**Nur die Gruppennamen ausgeben:**

```bash
id -Gn
```

```text
nox sudo users
```

**Nur die numerische Benutzer-ID ausgeben (praktisch in Skripten):**

```bash
id -u
```

```text
1000
```

**Prüfen, ob ein Benutzer existiert:**

```bash
id backup-user
```

```text
id: ‘backup-user’: no such user
```

<!-- SCREENSHOT: assets/screenshots/01-orientation/id.png -->

## Wann brauche ich das?

- Um zu prüfen, ob ein Benutzer in der Gruppe `sudo` ist (oder `docker`, `www-data`, …)
- Um UID/GID herauszufinden, wenn Dateien Zahlen statt Namen zeigen oder wenn
  Volumes und NFS-Freigaben passende IDs brauchen
- Um vor dem Anlegen eines Dienstkontos zu prüfen, ob es schon existiert
- In Skripten: `[ "$(id -u)" -eq 0 ]` ist der zuverlässige Weg, auf root zu prüfen

!!! tip "Gut zu wissen"
    `id -un` liefert dasselbe wie `whoami`. Ein `id` ohne Benutzer zeigt die Gruppen
    deiner **aktuellen Sitzung**, `id nox` liest dagegen die Gruppendatenbank.

!!! warning "Neue Gruppen brauchen eine neue Anmeldung"
    Nach `usermod -aG sudo nox` zeigt `id nox` die neue Gruppe sofort, ein einfaches `id`
    in deiner offenen Sitzung aber nicht. Erst nach Ab- und wieder Anmelden (oder in
    einer neuen SSH-Sitzung) greift die neue Gruppenmitgliedschaft.

## Verwandte Befehle

[whoami](whoami.md)
