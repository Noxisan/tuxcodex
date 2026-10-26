# delgroup

> Deletes a group on Debian and Ubuntu, or removes a user from a group.

![delgroup output](../assets/screenshots/07-users-groups/delgroup.png)

## Syntax

```bash
delgroup [OPTION]... GROUP
delgroup USER GROUP
```

## Options

| Option | Description |
|--------|-------------|
| `--only-if-empty` | Only delete the group if it has no members |
| `--system` | Only delete the group if it is a system group |
| `--verbose` | Show every step |

## Examples

**Delete a group:**

```bash
sudo delgroup --verbose developers
```

```text
info: Removing group `developers' ...
```

**Only delete a group if nobody is in it:**

```bash
sudo delgroup --only-if-empty developers
```

```text
fatal: The group `developers' is not empty!
```

The group still has members and stays.

**Remove a user from a group:**

```bash
sudo delgroup alice developers
getent group developers
```

```text
developers:x:1005:bob,nox
```

**Check that the group is gone:**

```bash
getent group developers
echo $?
```

```text
2
```

## When do I need it?

- To clean up team or project groups that are no longer needed
- To remove groups of uninstalled services
- To remove a user from a group with the Debian and Ubuntu tools

!!! tip "Use `--only-if-empty` for cleanups"
    In cleanup scripts, `--only-if-empty` prevents you from deleting a group that is
    still in use.

!!! warning "Files keep the GID"
    Files that belonged to the deleted group keep its GID. `ls -l` then shows a number
    instead of a name. Find them before deleting with `sudo find / -xdev -group developers`.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| `delgroup` | installed | installed | not available | not available |
| Alternative | | | `groupdel developers`, `gpasswd -d alice developers` | `groupdel developers`, `gpasswd -d alice developers` |

## Related commands

[addgroup](addgroup.md) · [gpasswd](gpasswd.md)
