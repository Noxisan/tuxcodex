# addgroup

> Creates a new group on Debian, or adds an existing user to a group.

![addgroup output](../assets/screenshots/07-users-groups/addgroup.png)

## Syntax

```bash
addgroup [OPTION]... GROUP
addgroup USER GROUP
```

## Options

| Option | Description |
|--------|-------------|
| `--system` | Create a system group (GID below 1000) for a service |
| `--gid ID` | Use this GID |
| `--verbose` | Show every step |

## Examples

**Create a group and show every step:**

```bash
sudo addgroup --verbose developers
```

```text
info: Selecting GID from range 1000 to 59999 ...
info: Adding group `developers' (GID 1005) ...
```

**Check the new group:**

```bash
getent group developers
```

```text
developers:x:1005:
```

The group exists, but has no members yet.

**Add a user to the group:**

```bash
sudo addgroup alice developers
getent group developers
```

```text
developers:x:1005:alice
```

**Create a system group for a service:**

```bash
sudo addgroup --system myapp
getent group myapp
```

```text
myapp:x:108:
```

**Try to create a group that already exists:**

```bash
sudo addgroup developers
```

```text
fatal: The group `developers' already exists.
```

## When do I need it?

- To create a team group for a shared directory, for example `developers` or `deploy`
- To create a group for a service that several users or services share
- To add a user to a group with the Debian tools

!!! tip "Same as `adduser USER GROUP`"
    `addgroup alice developers` and `adduser alice developers` do exactly the same. Use
    whichever you find easier to remember.

!!! warning "Members need a new login"
    A user who was added to a group only gets the new rights in a new session. Log out
    and back in, or open a new SSH connection.

## Debian vs. Arch

| | Debian | Arch |
|---|--------|------|
| `addgroup` | installed | not available |
| Alternative | `groupadd` | `groupadd developers`, `gpasswd -a alice developers` |

## Related commands

[adduser](adduser.md) · [getent](getent.md)
