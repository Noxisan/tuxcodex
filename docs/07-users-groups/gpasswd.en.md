# gpasswd

> Manages the members of a group: add, remove or set them all at once, and name group administrators.

![gpasswd output](../assets/screenshots/07-users-groups/gpasswd.png)

## Syntax

```bash
gpasswd [OPTION] GROUP
```

## Options

| Option | Description |
|--------|-------------|
| `-a USER`, `--add` | Add a user to the group |
| `-d USER`, `--delete` | Remove a user from the group |
| `-M USERS`, `--members` | Set the complete member list (separated by commas) |
| `-A USERS`, `--administrators` | Set group administrators who may manage members themselves |
| `-r`, `--remove-password` | Remove the group password |

## Examples

**Add a user to a group:**

```bash
sudo gpasswd -a alice developers
```

```text
Adding user alice to group developers
```

**Remove a user from a group:**

```bash
sudo gpasswd -d alice developers
```

```text
Removing user alice from group developers
```

**Set all members at once:**

```bash
sudo gpasswd -M alice,bob,nox developers
getent group developers
```

```text
developers:x:1005:alice,bob,nox
```

**Remove a user who is not a member:**

```bash
sudo gpasswd -d carol developers
```

```text
gpasswd: user 'carol' is not a member of 'developers'
```

**Let a team lead manage the group without `sudo`:**

```bash
sudo gpasswd -A alice developers
gpasswd -a bob developers
```

```text
Adding user bob to group developers
```

The second command was run by `alice`, without `sudo`.

## When do I need it?

- To add or remove a user from a group, on every distribution and with a clear message
- To give a team lead control over the members of a team group
- To set the members of a group exactly, for example from a script

!!! tip "`gpasswd -d` instead of `usermod -G`"
    To remove a user from a single group, `gpasswd -d` is the safe way. With `usermod -G`,
    you have to list all remaining groups and can easily forget one.

!!! warning "`-M` replaces all members"
    `gpasswd -M alice developers` makes `alice` the **only** member. Everyone else is
    removed from the group.

## Related commands

[groupadd](groupadd.md) · [usermod](usermod.md)
