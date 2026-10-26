# groups

> Shows the groups a user belongs to.

![groups output](../assets/screenshots/07-users-groups/groups.png)

## Syntax

```bash
groups [USER]...
```

## Options

`groups` has no options of its own.

| Option | Description |
|--------|-------------|
| `--help` | Show the help text and exit |
| `--version` | Show version information and exit |

## Examples

**Show your own groups:**

```bash
groups
```

```text
nox sudo users
```

**Show the groups of another user:**

```bash
groups alice
```

```text
alice : alice users
```

With a user name, the output starts with the name and a colon.

**Check several users at once:**

```bash
groups nox alice www-data
```

```text
nox : nox sudo users
alice : alice users
www-data : www-data
```

**After adding a group, compare the session with the database:**

```bash
sudo usermod -aG docker nox
groups
groups nox
```

```text
nox sudo users
nox : nox sudo users docker
```

`groups` without a name shows the groups of your current session. The new group `docker`
only appears there after you log in again.

## When do I need it?

- To check whether a user is in `sudo`, `docker`, `www-data` or another group that grants
  access
- To find out why a user can't access a shared directory
- To verify that `usermod -aG` or `gpasswd -a` worked

!!! tip "`groups` or `id`?"
    `groups` only shows the names. [`id`](../01-orientation/id.md) also shows the
    numbers (UID and GIDs), which helps when files show numbers instead of names.

!!! warning "New groups need a new login"
    A group you were added to only applies to new sessions. Log out and back in, or open
    a new SSH connection, before you test the new access.

## Related commands

[id](../01-orientation/id.md) · [whoami](../01-orientation/whoami.md) · [getent](getent.md)
