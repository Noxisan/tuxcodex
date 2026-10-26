# getent

> Looks up entries in the system databases: users, groups, hosts and services, from local files and from directory services like LDAP.

![getent output](../assets/screenshots/07-users-groups/getent.png)

## Syntax

```bash
getent [OPTION]... DATABASE [KEY]...
```

## Options

| Database | Contents |
|----------|----------|
| `passwd` | User accounts |
| `group` | Groups and their members |
| `shadow` | Password data (only as `root`) |
| `hosts` | Host names and IP addresses |
| `services` | Network services and their ports |

| Option | Description |
|--------|-------------|
| `-s SOURCE`, `--service=SOURCE` | Only ask a specific source, e.g. `files` or `ldap` |

Without a key, `getent` lists all entries of the database. The exit status is `0` if
something was found and `2` if not.

## Examples

**Look up a user:**

```bash
getent passwd nox
```

```text
nox:x:1000:1000:Nox,,,:/home/nox:/bin/bash
```

**Find the user for a UID:**

```bash
getent passwd 33
```

```text
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

**Show the members of a group:**

```bash
getent group sudo
```

```text
sudo:x:27:nox
```

**Check whether a user exists:**

```bash
getent passwd ghost
echo $?
```

```text
2
```

**Resolve a host name like the system does:**

```bash
getent hosts tuxcodex-srv
```

```text
127.0.1.1       tuxcodex-srv.example.com tuxcodex-srv
```

**Find the port of a service:**

```bash
getent services ssh
```

```text
ssh                   22/tcp
```

**Show the password data of a user:**

```bash
sudo getent shadow nox
```

```text
nox:$y$j9T$ExampleSaltOnly$ExampleHashOnlyNotARealPasswordHash:20752:0:99999:7:::
```

The fields after the hash: last change (days since 1970), minimum and maximum age and
warning period.

## When do I need it?

- To check in scripts whether a user or group exists, before creating it
- On servers with LDAP, Active Directory or SSSD, where users are not in `/etc/passwd`:
  `getent` asks all configured sources
- To test name resolution the way programs see it, including `/etc/hosts`

!!! tip "`getent` instead of `grep /etc/passwd`"
    `grep nox /etc/passwd` only finds local users and also matches `nox` inside other
    names. `getent passwd nox` searches exactly for this name in all sources.

!!! tip "Find the group for a GID"
    `getent group 1001` shows which group has GID 1001, for example when `ls -l` shows a
    number instead of a group name.

## Related commands

[groups](groups.md) · [id](../01-orientation/id.md)
