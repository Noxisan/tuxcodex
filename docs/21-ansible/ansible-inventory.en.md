# ansible-inventory

> Shows the inventory as Ansible understands it: groups, servers and their variables.

![ansible-inventory output](../assets/screenshots/21-ansible/ansible-inventory.png)

## Syntax

```bash
ansible-inventory [-i INVENTORY] --graph | --list | --host HOST
```

## Options

| Option | Description |
|--------|-------------|
| `--graph [GROUP]` | Groups and servers as a tree |
| `--list` | Everything as JSON, including all variables |
| `--host HOST` | The variables of one server |
| `--vars` | With `--graph`: also show the variables |
| `-i FILE` | Use this inventory instead of the configured one |
| `-y`, `--yaml` | YAML instead of JSON |

## Examples

**Groups and servers as a tree:**

```bash
ansible-inventory --graph
```

```text
@all:
  |--@ungrouped:
  |--@db:
  |--@production:
  |  |--@web:
  |  |  |--web01
  |  |  |--web02
```

**The variables of one server:**

```bash
ansible-inventory --host web01
```

```text
{
    "ansible_host": "192.0.2.21",
    "nginx_worker_connections": 1024
}
```

`nginx_worker_connections` comes from `group_vars/web.yml`, because `web01` is in the group `web`.

**The whole inventory as JSON:**

```bash
ansible-inventory --list | head -20
```

```text
{
    "_meta": {
        "hostvars": {
            "web01": {
                "ansible_host": "192.0.2.21",
                "nginx_worker_connections": 1024
            },
            "web02": {
                "ansible_host": "192.0.2.22",
                "nginx_worker_connections": 1024
            }
        },
        "profile": "inventory_legacy"
    },
    "all": {
        "children": [
            "ungrouped",
            "db",
            "production"
        ]
```

## When do I need it?

- To check that new servers ended up in the right groups
- To find out which value a variable has on a server, and from which file
- To test a dynamic inventory, for example from a cloud provider

!!! tip "Patterns for targets"
    `web:db` means both groups, `web:!web02` the group without one server, `web:&production`
    only servers in both groups. The same patterns work with `ansible` and `--limit`.

## Related commands

[ansible](ansible.md) · [ansible-playbook](ansible-playbook.md) · [ansible-config](ansible-config.md)
