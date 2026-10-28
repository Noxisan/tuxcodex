# Webserver verstehen

Fast jeder Server betreibt einen Webserver: für eine Website, als Vorderseite einer
Anwendung oder als Reverse Proxy vor Containern. Die beiden verbreitetsten sind **nginx** und
**Apache httpd**. Sie erledigen dieselbe Aufgabe mit unterschiedlichem Konfigurationsstil.

## nginx oder Apache?

| | nginx | Apache |
|---|-------|--------|
| Stärke | Schnell für statische Dateien und als Reverse Proxy, wenig Speicher | Sehr flexibel, viele Module, `.htaccess` pro Verzeichnis |
| Konfiguration | `server { … }`-Blöcke | `<VirtualHost>`-Abschnitte |
| Typischer Einsatz | Reverse Proxy, statische Seiten, vor PHP-FPM oder Containern | Klassisches PHP-Hosting, Anwendungen, die `.htaccess` brauchen |

## Wo die Konfiguration liegt

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| nginx-Paket | `nginx` | `nginx` | `nginx` | `nginx` |
| nginx-Seiten | `/etc/nginx/sites-available/`, Link in `sites-enabled/` | `/etc/nginx/sites-available/`, Link in `sites-enabled/` | `/etc/nginx/conf.d/*.conf` | `/etc/nginx/nginx.conf` (`include` nach Belieben) |
| Apache-Paket | `apache2` | `apache2` | `httpd` | `apache` |
| Apache-Seiten | `/etc/apache2/sites-available/`, aktivieren mit `a2ensite` | `/etc/apache2/sites-available/`, aktivieren mit `a2ensite` | `/etc/httpd/conf.d/*.conf` | `/etc/httpd/conf/extra/`, `Include` in `httpd.conf` |
| Apache-Dienst | `apache2` | `apache2` | `httpd` | `httpd` |
| Logs | `/var/log/nginx/`, `/var/log/apache2/` | `/var/log/nginx/`, `/var/log/apache2/` | `/var/log/nginx/`, `/var/log/httpd/` | `/var/log/nginx/`, `/var/log/httpd/` |
| Web-Benutzer | `www-data` | `www-data` | `nginx`, `apache` | `http` |

## Ein nginx-Server-Block

`/etc/nginx/sites-available/status`, aktiviert mit
`ln -s /etc/nginx/sites-available/status /etc/nginx/sites-enabled/`:

```text
server {
    listen 80;
    server_name status.example.com;
    root /srv/status;
    index index.html;

    location /admin/ {
        auth_basic "Admin";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

`location /api/` macht nginx zum **Reverse Proxy**: Anfragen gehen weiter an eine
Anwendung auf Port 3000, etwa einen Container, und die Antwort geht zurück an den Client.

## Ein Apache-Virtual-Host

`/etc/apache2/sites-available/wiki.conf`, aktiviert mit [`a2ensite`](a2ensite.md):

```text
<VirtualHost *:80>
    ServerName wiki.example.com
    DocumentRoot /srv/wiki
    <Directory /srv/wiki>
        Require all granted
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/wiki-error.log
    CustomLog ${APACHE_LOG_DIR}/wiki-access.log combined
</VirtualHost>
```

## Die Konfiguration sicher ändern

```text
$ sudo nano /etc/nginx/sites-available/status
$ sudo nginx -t                     # 1. test
$ sudo systemctl reload nginx       # 2. reload, running connections continue
$ curl -I https://status.example.com   # 3. check
```

Neu laden statt neu starten: Der Webserver übernimmt die neue Konfiguration, ohne
Verbindungen abzubrechen. Scheitert der Test, läuft die alte Konfiguration weiter.

## HTTPS

Zertifikate von Let's Encrypt richtest du mit
[`certbot --nginx`](../24-certificates/certbot.md) oder `certbot --apache` ein; certbot
ergänzt die TLS-Zeilen in der Konfiguration und erneuert die Zertifikate. Prüfe das
Ergebnis mit [`testssl.sh`](../24-certificates/testssl.md).

!!! tip "Immer testen, bevor du neu lädst"
    `nginx -t` und `apachectl configtest` finden Tippfehler, bevor sie die Seite lahmlegen.
    Mach das zur Gewohnheit, auch in Ansible-Handlern und Deploy-Skripten.

!!! warning "Logs wachsen schnell"
    Belebte Seiten schreiben Gigabytes an Zugriffslogs. Beide Pakete bringen eine
    `logrotate`-Regel mit, siehe [`logrotate`](../15-logs/logrotate.md); prüf sie, wenn du
    Log-Pfade änderst.
