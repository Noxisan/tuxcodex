# ansible-doc

> Shows the documentation of modules and plugins in the terminal, with all parameters and examples.

![ansible-doc output](../assets/screenshots/21-ansible/ansible-doc.png)

## Syntax

```bash
ansible-doc [-l | -s] [MODULE]
```

## Options

| Option | Description |
|--------|-------------|
| `MODULE` | Full documentation of a module, such as `ansible.builtin.copy` |
| `-l`, `--list` | List all installed modules with a short description |
| `-s`, `--snippet` | Only a short template for a task |
| `-t TYPE` | Other plugin types, such as `lookup`, `filter` or `callback` |
| `-F` | List the modules with the path to their file |

## Examples

**Find modules:**

```bash
ansible-doc -l | grep -E "^ansible.builtin.(apt|copy|service|template|user) "
```

```text
ansible.builtin.apt          Manages apt-packages
ansible.builtin.copy         Copy files to remote locations
ansible.builtin.service      Manage services
ansible.builtin.template     Template a file out to a target host
ansible.builtin.user         Manage user accounts
```

**A template for a task:**

```bash
ansible-doc -s ansible.builtin.service | head -12
```

```text
- name: Manage services
  service:
      arguments:             # Additional arguments provided on the command line.
                             # While using remote hosts with systemd this
                             # setting will be ignored.
      enabled:               # Whether the service should start on boot. At
                             # least one of `state' and `enabled' are required.
      name:                  # (required) Name of the service.
      pattern:               # If the service does not respond to the status
                             # command, name a substring to look for as would
                             # be found in the output of the `ps' command as a
                             # stand-in for a status result.
```

**The full documentation of a module:**

```bash
ansible-doc ansible.builtin.copy | head -9
```

```text
> MODULE ansible.builtin.copy (/usr/lib/python3/dist-packages/ansible/modules/copy.py)

  The ansible.builtin.copy module copies a file or a directory
  structure from the local or remote machine to a location on the
  remote machine. File system meta-information (permissions,
  ownership, etc.) may be set, even when the file or directory already
  exists on the target system. Some meta-information may be copied on
  request.
  Get meta-information with the ansible.builtin.stat module.
```

## When do I need it?

- To find out which parameters a module accepts, without a browser
- To find the right module for a task
- To check the documentation of the exact version installed on the control node

!!! tip "Jump to the examples"
    The documentation of every module ends with a section `EXAMPLES`. In the pager, type
    `/EXAMPLES` and press ++enter++ to jump there.

## Related commands

[ansible](ansible.md) · [ansible-galaxy](ansible-galaxy.md) · [ansible-playbook](ansible-playbook.md)
