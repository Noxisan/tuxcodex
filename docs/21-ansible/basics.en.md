# Understanding Ansible

Ansible configures servers over SSH. You describe the desired state once, for example
"nginx is installed and serves this page", and Ansible brings any number of servers to
that state. It doesn't need an agent on the servers: SSH access and Python are enough.

## Control node and managed servers

```text
          tuxdex-srv (control node)
          ansible, playbooks, inventory
                 │  SSH
        ┌────────┴────────┐
        ▼                 ▼
      web01             web02
   192.0.2.21        192.0.2.22
```

| Term | Meaning |
|------|---------|
| **Control node** | The machine where Ansible is installed and where you run it |
| **Managed node** | A server Ansible configures; it needs SSH and Python 3 |
| **Inventory** | The list of servers, sorted into groups |
| **Module** | A unit of work, such as `apt`, `copy`, `service` or `user` |
| **Task** | One call of a module with its parameters |
| **Playbook** | A YAML file with tasks for groups of servers |
| **Role** | A reusable bundle of tasks, files, templates and variables |
| **Handler** | A task that only runs when another task changed something, such as reloading nginx |

## What you need to install

Ansible is only installed on the control node. The managed servers need nothing but an
SSH server, Python 3 and your SSH key, see [`ssh-copy-id`](../12-ssh/ssh-copy-id.md).

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Ansible | `sudo apt install ansible` | `sudo apt install ansible` | `sudo dnf install ansible-core` (full `ansible` from EPEL) | `sudo pacman -S ansible` |
| ansible-lint | `sudo apt install ansible-lint` | `sudo apt install ansible-lint` | `pipx install ansible-lint` | `sudo pacman -S ansible-lint` |

`ansible` is `ansible-core` plus a large set of collections such as `community.general`.
With `ansible-core` alone, you install the collections you need with
[`ansible-galaxy`](ansible-galaxy.md). On any distribution, `pipx install --include-deps ansible`
gets the newest version.

## The inventory

`~/ansible/inventory.ini`:

```text
[web]
web01 ansible_host=192.0.2.21
web02 ansible_host=192.0.2.22

[db]

[production:children]
web
```

Groups like `web` let you address several servers at once. Variables for a group go into
`group_vars/web.yml`, for a single server into `host_vars/web01.yml`.

## A playbook

`~/ansible/site.yml` installs nginx on all web servers and puts a status page in place:

```text
- name: Set up web servers
  hosts: web
  become: true
  tasks:
    - name: Install nginx
      ansible.builtin.apt:
        name: nginx
        state: present
        update_cache: true
        cache_valid_time: 3600
      tags: packages

    - name: Deploy status page
      ansible.builtin.copy:
        content: "<h1>{{ inventory_hostname }}: all systems operational</h1>\n"
        dest: /var/www/html/index.html
        mode: "0644"
      notify: Reload nginx

  handlers:
    - name: Reload nginx
      ansible.builtin.service:
        name: nginx
        state: reloaded
```

`become: true` runs the tasks with `sudo`. Run it with
[`ansible-playbook`](ansible-playbook.md).

## Idempotency

Modules describe a state, not an action. `state: present` means "nginx must be installed",
not "install nginx". If it already is, nothing happens and the task reports `ok` instead of
`changed`. That's why you can run a playbook as often as you like: the second run changes
nothing.

## A project directory

```text
~/ansible/
├── ansible.cfg            # settings for this project
├── inventory.ini          # servers and groups
├── site.yml               # main playbook
├── group_vars/
│   ├── web.yml            # variables for the group web
│   └── secrets.yml        # passwords, encrypted with ansible-vault
└── roles/
    └── nginx/             # a role, created with ansible-galaxy role init
```

`~/ansible/ansible.cfg`:

```text
[defaults]
inventory = inventory.ini
remote_user = nox
interpreter_python = auto_silent
```

With this file, you no longer need `-i inventory.ini` on every command, as long as you run
Ansible in this directory. See [`ansible-config`](ansible-config.md).

!!! tip "Keep the project in Git"
    An Ansible project belongs in a Git repository, see the chapter [Git](../18-git/index.md).
    Then every change to your servers is documented, reviewable and can be undone.

!!! warning "Use modules, not shell commands"
    `ansible.builtin.shell: apt install nginx` works, but it reports `changed` on every run
    and can't be checked with `--check`. A module like `ansible.builtin.apt` knows the
    current state and only acts when needed.
