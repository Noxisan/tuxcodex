# apachectl

> Controls the Apache web server: test the configuration, reload it gracefully and show virtual hosts and modules.

![apachectl output](../assets/screenshots/29-webserver/apachectl.png)

## Syntax

```bash
apachectl configtest | graceful | restart | -S | -M | -v
```

## Options

| Option | Description |
|--------|-------------|
| `configtest`, `-t` | Test the configuration |
| `graceful` | Reload: running requests are finished first |
| `restart` | Restart immediately |
| `-S` | Show all virtual hosts with file and line |
| `-M` | List the loaded modules |
| `-v`, `-V` | Version, or version with build settings |

On Debian and Ubuntu the program is `apache2` and `apache2ctl`; `apachectl` exists there as well. On RHEL and Arch it's `httpd`.

## Examples

**Test the configuration:**

```bash
sudo apachectl configtest
```

```text
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 192.0.2.10. Set the 'ServerName' directive globally to suppress this message
Syntax OK
```

**All virtual hosts at a glance:**

```bash
sudo apachectl -S 2>/dev/null | head -5
```

```text
VirtualHost configuration:
*:80                   is a NameVirtualHost
         default server 192.0.2.10 (/etc/apache2/sites-enabled/000-default.conf:1)
         port 80 namevhost 192.0.2.10 (/etc/apache2/sites-enabled/000-default.conf:1)
         port 80 namevhost wiki.example.com (/etc/apache2/sites-enabled/wiki.conf:1)
```

**An error in a virtual host:**

```bash
sudo apachectl configtest
```

```text
AH00526: Syntax error on line 10 of /etc/apache2/sites-enabled/wiki.conf:
DocumentRoot takes one argument, Root directory of the document tree
```

**Reload gracefully after a test:**

```bash
sudo apachectl configtest 2>/dev/null && sudo apachectl graceful 2>/dev/null
systemctl is-active apache2
```

```text
Syntax OK
active
```

**Check whether modules are loaded:**

```bash
sudo apachectl -M 2>/dev/null | grep -E 'rewrite|ssl'
```

```text
 rewrite_module (shared)
 ssl_module (shared)
```

## When do I need it?

- After every change of a virtual host, before reloading
- To find out which virtual host answers for a domain (`-S`)
- To check whether a module like `rewrite` or `ssl` is loaded (`-M`)

!!! tip "Silence AH00558"
    The warning `Could not reliably determine the server's fully qualified domain name` is
    harmless. `ServerName tuxdex-srv.example.com` in `/etc/apache2/conf-available/servername.conf`
    plus `a2enconf servername` makes it go away.

!!! warning "The first virtual host is the default"
    Requests for unknown names end up at the first virtual host of a port. `apachectl -S`
    shows it as `default server`. Make sure that's a harmless page, not an application.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Package | `apache2` | `apache2` | `httpd` | `apache` |
| Service | `apache2` | `apache2` | `httpd` | `httpd` |
| Configuration | `/etc/apache2/` | `/etc/apache2/` | `/etc/httpd/` | `/etc/httpd/` |

## Related commands

[a2ensite](a2ensite.md) · [a2enmod](a2enmod.md) · [nginx](nginx.md) · [systemctl](../09-systemd/systemctl.md)
