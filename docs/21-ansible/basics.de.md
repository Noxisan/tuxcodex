# Ansible verstehen

Ansible konfiguriert Server über SSH. Du beschreibst einmal den gewünschten Zustand, etwa
„nginx ist installiert und liefert diese Seite aus“, und Ansible bringt beliebig viele
Server in diesen Zustand. Auf den Servern braucht es keinen Agenten: SSH-Zugang und Python
reichen.

## Steuerrechner und verwaltete Server

```text
          tuxdex-srv (Steuerrechner)
          ansible, Playbooks, Inventar
                 │  SSH
        ┌────────┴────────┐
        ▼                 ▼
      web01             web02
   192.0.2.21        192.0.2.22
```

| Begriff | Bedeutung |
|---------|-----------|
| **Control Node** (Steuerrechner) | Der Rechner, auf dem Ansible installiert ist und von dem aus du es startest |
| **Managed Node** (verwalteter Server) | Ein Server, den Ansible konfiguriert; er braucht SSH und Python 3 |
| **Inventar** | Die Liste der Server, in Gruppen sortiert |
| **Modul** | Ein Arbeitsschritt, etwa `apt`, `copy`, `service` oder `user` |
| **Task** | Ein Aufruf eines Moduls mit seinen Parametern |
| **Playbook** | Eine YAML-Datei mit Tasks für Gruppen von Servern |
| **Rolle** | Ein wiederverwendbares Paket aus Tasks, Dateien, Vorlagen und Variablen |
| **Handler** | Ein Task, der nur läuft, wenn ein anderer Task etwas geändert hat, etwa nginx neu laden |

## Was du installieren musst

Ansible wird nur auf dem Steuerrechner installiert. Die verwalteten Server brauchen nur
einen SSH-Server, Python 3 und deinen SSH-Schlüssel, siehe
[`ssh-copy-id`](../12-ssh/ssh-copy-id.md).

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Ansible | `sudo apt install ansible` | `sudo apt install ansible` | `sudo dnf install ansible-core` (volles `ansible` aus EPEL) | `sudo pacman -S ansible` |
| ansible-lint | `sudo apt install ansible-lint` | `sudo apt install ansible-lint` | `pipx install ansible-lint` | `sudo pacman -S ansible-lint` |

`ansible` ist `ansible-core` plus eine große Sammlung von Collections wie
`community.general`. Mit `ansible-core` allein installierst du die nötigen Collections mit
[`ansible-galaxy`](ansible-galaxy.md). Auf jeder Distribution holt
`pipx install --include-deps ansible` die neueste Version.

## Das Inventar

`~/ansible/inventory.ini`:

```text
[web]
web01 ansible_host=192.0.2.21
web02 ansible_host=192.0.2.22

[db]

[production:children]
web
```

Über Gruppen wie `web` sprichst du mehrere Server auf einmal an. Variablen für eine Gruppe
kommen nach `group_vars/web.yml`, für einen einzelnen Server nach `host_vars/web01.yml`.

## Ein Playbook

`~/ansible/site.yml` installiert nginx auf allen Webservern und legt eine Statusseite ab:

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

`become: true` führt die Tasks mit `sudo` aus. Gestartet wird das Ganze mit
[`ansible-playbook`](ansible-playbook.md).

## Idempotenz

Module beschreiben einen Zustand, keine Handlung. `state: present` heißt „nginx muss
installiert sein“, nicht „installiere nginx“. Ist es das schon, passiert nichts, und der Task
meldet `ok` statt `changed`. Deshalb kannst du ein Playbook beliebig oft ausführen: Der
zweite Lauf ändert nichts mehr.

## Ein Projektverzeichnis

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

Mit dieser Datei brauchst du kein `-i inventory.ini` mehr bei jedem Befehl, solange du
Ansible in diesem Verzeichnis startest. Siehe [`ansible-config`](ansible-config.md).

!!! tip "Das Projekt in Git ablegen"
    Ein Ansible-Projekt gehört in ein Git-Repository, siehe das Kapitel
    [Git](../18-git/index.md). Dann ist jede Änderung an deinen Servern dokumentiert,
    nachvollziehbar und lässt sich zurücknehmen.

!!! warning "Module statt Shell-Befehle"
    `ansible.builtin.shell: apt install nginx` funktioniert, meldet aber bei jedem Lauf
    `changed` und lässt sich nicht mit `--check` prüfen. Ein Modul wie `ansible.builtin.apt`
    kennt den aktuellen Zustand und handelt nur, wenn es nötig ist.
