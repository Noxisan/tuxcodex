# ansible-galaxy

> Creates roles and installs roles and collections from Ansible Galaxy or a Git repository.

![ansible-galaxy output](../assets/screenshots/21-ansible/ansible-galaxy.png)

## Syntax

```bash
ansible-galaxy role init | install | list ...
ansible-galaxy collection install | list ...
```

## Options

| Option | Description |
|--------|-------------|
| `role init NAME` | Create the directory structure for a new role |
| `role install NAME` | Install a role, such as `geerlingguy.ntp` |
| `collection install NAME` | Install a collection, such as `community.general` |
| `-r requirements.yml` | Install everything listed in a file |
| `list` | Show the installed roles or collections |
| `-p DIRECTORY` | Install into this directory instead of `~/.ansible` |
| `--force` | Install again, also to update |

## Examples

**Create a new role:**

```bash
ansible-galaxy role init roles/nginx
find roles/nginx -type f | sort
```

```text
- Role roles/nginx was created successfully
roles/nginx/README.md
roles/nginx/defaults/main.yml
roles/nginx/handlers/main.yml
roles/nginx/meta/main.yml
roles/nginx/tasks/main.yml
roles/nginx/tests/inventory
roles/nginx/tests/test.yml
roles/nginx/vars/main.yml
```

**Install a role from Galaxy:**

```bash
ansible-galaxy role install geerlingguy.ntp
```

```text
Starting galaxy role install process
- downloading role 'ntp', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-ntp/archive/4.0.1.tar.gz
- extracting geerlingguy.ntp to /home/nox/.ansible/roles/geerlingguy.ntp
- geerlingguy.ntp (4.0.1) was installed successfully
```

**Show the installed version of a collection:**

```bash
ansible-galaxy collection list community.general
```

```text
# /usr/lib/python3/dist-packages/ansible_collections
Collection        Version
----------------- -------
community.general 11.2.1
```

On Debian, the package `ansible` brings the collections along in `/usr/lib/python3/dist-packages/ansible_collections`.

**Install everything a project needs:**

```bash
cat requirements.yml
ansible-galaxy install -r requirements.yml
```

```text
roles:
  - name: geerlingguy.ntp
    version: 4.0.1
collections:
  - name: community.general
    version: ">=11.0.0"
Starting galaxy role install process
- geerlingguy.ntp (4.0.1) is already installed, skipping.
Starting galaxy collection install process
Nothing to do. All requested collections are already installed. If you want to reinstall them, consider using `--force`.
```

## When do I need it?

- To split your own tasks into reusable roles
- To use ready-made roles for common software instead of writing everything yourself
- To install the collections a project needs on a new control node

!!! tip "requirements.yml for every project"
    List the roles and collections of a project with fixed versions in
    `requirements.yml`. Then `ansible-galaxy install -r requirements.yml` sets up any control
    node the same way.

!!! warning "Roles from strangers run as root"
    A role from Galaxy runs on your servers with `become`. Read its tasks before you use it,
    and pin the version so that an update doesn't change things unnoticed.

## Related commands

[ansible-playbook](ansible-playbook.md) · [ansible-doc](ansible-doc.md) · [ansible-lint](ansible-lint.md)
