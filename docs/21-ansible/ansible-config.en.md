# ansible-config

> Shows which Ansible settings apply, where they come from, and creates a template for ansible.cfg.

![ansible-config output](../assets/screenshots/21-ansible/ansible-config.png)

## Syntax

```bash
ansible-config view | dump [--only-changed] | list | init [--disabled]
```

## Options

| Option | Description |
|--------|-------------|
| `view` | Show the active configuration file |
| `dump` | Show every setting with its current value |
| `dump --only-changed` | Only settings that differ from the default, with their source |
| `list` | All settings with description, default and environment variable |
| `init --disabled` | Print a complete `ansible.cfg` with every setting commented out |
| `-c FILE` | Use this configuration file |

Ansible uses the first file it finds: `$ANSIBLE_CONFIG`, then `ansible.cfg` in the current directory, then `~/.ansible.cfg`, then `/etc/ansible/ansible.cfg`.

## Examples

**Show the settings that differ from the default:**

```bash
ansible-config dump --only-changed
```

```text
CONFIG_FILE() = /home/nox/ansible/ansible.cfg
DEFAULT_HOST_LIST(/home/nox/ansible/ansible.cfg) = ['/home/nox/ansible/inventory.ini']
DEFAULT_REMOTE_USER(/home/nox/ansible/ansible.cfg) = nox
INTERPRETER_PYTHON(/home/nox/ansible/ansible.cfg) = auto_silent
```

In brackets is the source of each value: here the `ansible.cfg` of the project.

**The active configuration file:**

```bash
ansible-config view
```

```text
[defaults]
inventory = inventory.ini
remote_user = nox
interpreter_python = auto_silent
```

**Version and configuration file:**

```bash
ansible --version | head -3
```

```text
ansible [core 2.19.11]
  config file = /home/nox/ansible/ansible.cfg
  configured module search path = ['/home/nox/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
```

**A template with every setting:**

```bash
ansible-config init --disabled > ansible.cfg.example
grep -A2 '^# (integer) Maximum number of forks' ansible.cfg.example
```

```text
# (integer) Maximum number of forks Ansible will use to execute tasks on target hosts.
;forks=5

```

## When do I need it?

- To check why Ansible behaves differently in one directory than in another
- To start a new project with a documented `ansible.cfg`
- To find the name of a setting or its environment variable

!!! tip "ansible --version shows the file"
    The second line of `ansible --version` shows which configuration file is active, or
    `config file = None` if there is none.

!!! warning "ansible.cfg in a world-writable directory"
    Ansible ignores an `ansible.cfg` in a directory that anyone can write to, such as
    `/tmp`, and prints a warning. Keep projects in your home directory.

## Related commands

[ansible-inventory](ansible-inventory.md) · [ansible](ansible.md) · [ansible-playbook](ansible-playbook.md)
