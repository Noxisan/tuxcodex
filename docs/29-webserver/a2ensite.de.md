# a2ensite

> Unter Debian und Ubuntu: aktiviert und deaktiviert Apache-Seiten, indem es sie von sites-available nach sites-enabled verlinkt.

![a2ensite output](../assets/screenshots/29-webserver/a2ensite.png)

## Syntax

```bash
a2ensite SEITE...
a2dissite SEITE...
a2query -s
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `a2ensite SEITE` | Eine Seite aktivieren (Datei `sites-available/SEITE.conf`) |
| `a2dissite SEITE` | Eine Seite deaktivieren |
| `a2query -s` | Die aktivierten Seiten auflisten |
| `-q`, `--quiet` | Keine Hinweise |
| `a2enconf`, `a2disconf` | Dasselbe für Schnipsel in `conf-available/` |

Nach dem Aktivieren oder Deaktivieren lädst du Apache neu: `sudo systemctl reload apache2`.

## Beispiele

**Eine Seite aktivieren und neu laden:**

```bash
sudo a2ensite wiki
sudo systemctl reload apache2
```

```text
Enabling site wiki.
To activate the new configuration, you need to run:
  service apache2 reload
```

**Die Standardseite abschalten:**

```bash
sudo a2dissite 000-default
```

```text
Site 000-default disabled.
To activate the new configuration, you need to run:
  service apache2 reload
```

**Die aktiven Seiten auflisten:**

```bash
a2query -s
```

```text
wiki (enabled by site administrator)
```

**Doppeltes Aktivieren schadet nicht:**

```bash
sudo a2ensite wiki
```

```text
Site wiki already enabled
```

## Wann brauche ich das?

- Um eine neue Website online zu nehmen
- Um eine Seite vom Netz zu nehmen, ohne ihre Konfiguration zu löschen
- Um auf einem Produktionsserver die Standardseite `000-default` abzuschalten

!!! tip "nginx hat kein a2ensite"
    Mit nginx unter Debian erledigt ein symbolischer Link dasselbe:
    `sudo ln -s /etc/nginx/sites-available/status /etc/nginx/sites-enabled/`, und `rm` des Links
    deaktiviert die Seite.

## Unterschiede zwischen Distributionen

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Vorhanden | ja (`apache2`) | ja (`apache2`) | nein: Dateien nach `/etc/httpd/conf.d/` legen | nein: `Include`-Zeilen in `httpd.conf` |

## Verwandte Befehle

[a2enmod](a2enmod.md) · [apachectl](apachectl.md) · [ln](../03-files/ln.md)
