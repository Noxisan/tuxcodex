# Understanding web servers

Almost every server runs a web server: for a website, as the front of an application or as
a reverse proxy in front of containers. The two most common ones are **nginx** and
**Apache httpd**. They do the same job with different configuration styles.

## nginx or Apache?

| | nginx | Apache |
|---|-------|--------|
| Strength | Fast for static files and as a reverse proxy, little memory | Very flexible, many modules, `.htaccess` per directory |
| Configuration | `server { … }` blocks | `<VirtualHost>` sections |
| Typical use | Reverse proxy, static sites, in front of PHP-FPM or containers | Classic PHP hosting, applications that need `.htaccess` |

## Where the configuration lives

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| nginx package | `nginx` | `nginx` | `nginx` | `nginx` |
| nginx sites | `/etc/nginx/sites-available/`, link in `sites-enabled/` | `/etc/nginx/sites-available/`, link in `sites-enabled/` | `/etc/nginx/conf.d/*.conf` | `/etc/nginx/nginx.conf` (`include` as you like) |
| Apache package | `apache2` | `apache2` | `httpd` | `apache` |
| Apache sites | `/etc/apache2/sites-available/`, enable with `a2ensite` | `/etc/apache2/sites-available/`, enable with `a2ensite` | `/etc/httpd/conf.d/*.conf` | `/etc/httpd/conf/extra/`, `Include` in `httpd.conf` |
| Apache service | `apache2` | `apache2` | `httpd` | `httpd` |
| Logs | `/var/log/nginx/`, `/var/log/apache2/` | `/var/log/nginx/`, `/var/log/apache2/` | `/var/log/nginx/`, `/var/log/httpd/` | `/var/log/nginx/`, `/var/log/httpd/` |
| Web user | `www-data` | `www-data` | `nginx`, `apache` | `http` |

## An nginx server block

`/etc/nginx/sites-available/status`, enabled with
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

`location /api/` makes nginx a **reverse proxy**: requests go on to an application on port
3000, for example a container, and the answer goes back to the client.

## An Apache virtual host

`/etc/apache2/sites-available/wiki.conf`, enabled with [`a2ensite`](a2ensite.md):

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

## Changing the configuration safely

```text
$ sudo nano /etc/nginx/sites-available/status
$ sudo nginx -t                     # 1. test
$ sudo systemctl reload nginx       # 2. reload, running connections continue
$ curl -I https://status.example.com   # 3. check
```

Reload instead of restart: the web server takes over the new configuration without
dropping connections. If the test fails, the old configuration keeps running.

## HTTPS

Certificates from Let's Encrypt are set up with [`certbot --nginx`](../24-certificates/certbot.md)
or `certbot --apache`; certbot adds the TLS lines to the configuration and renews the
certificates. Check the result with [`testssl.sh`](../24-certificates/testssl.md).

!!! tip "Always test before reloading"
    `nginx -t` and `apachectl configtest` find typos before they take the site down. Make
    it a habit, also in Ansible handlers and deploy scripts.

!!! warning "Logs grow quickly"
    Busy sites write gigabytes of access logs. Both packages bring a `logrotate` rule,
    see [`logrotate`](../15-logs/logrotate.md); check it if you change log paths.
