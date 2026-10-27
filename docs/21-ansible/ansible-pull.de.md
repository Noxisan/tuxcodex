# ansible-pull

> Dreht die Richtung um: Der Server holt sich ein Playbook aus einem Git-Repository und wendet es auf sich selbst an.

![ansible-pull output](../assets/screenshots/21-ansible/ansible-pull.png)

## Syntax

```bash
ansible-pull -U REPO_URL [OPTIONEN] [PLAYBOOK.yml]
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `-U URL` | Git-Repository mit den Playbooks |
| `PLAYBOOK.yml` | Auszuführendes Playbook; ohne Angabe `<hostname>.yml` oder `local.yml` |
| `-C BRANCH` | Auszucheckender Branch oder Tag |
| `-d VERZEICHNIS` | Wohin das Repository ausgecheckt wird (Standard `~/.ansible/pull/<hostname>`) |
| `-o`, `--only-if-changed` | Nur ausführen, wenn das Repository neue Commits hat |
| `-s SEKUNDEN` | Vorher eine zufällige Zeit bis zu so vielen Sekunden warten, damit nicht alle Server gleichzeitig starten |
| `--vault-password-file DATEI` | Passwort für verschlüsselte Dateien |

## Beispiele

**Die Konfiguration holen und anwenden:**

```bash
ansible-pull -U https://git.example.com/ops/config.git local.yml
```

```text
Starting Ansible Pull at 2026-10-26 10:42:17
/usr/bin/ansible-pull -U https://git.example.com/ops/config.git local.yml
localhost | CHANGED => {
    "after": "5c9bef1c4897f55aaf5a87f316a508f096778417",
    "before": null,
    "changed": true
}

PLAY [Base configuration] ******************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Message of the day] ******************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Der erste Block ist der `git`-Checkout, danach läuft das Playbook wie gewohnt. Je nach Playbook gibt Ansible zusätzlich Warnungen zum Host-Muster aus; die sind harmlos.

**Nur laufen, wenn sich etwas geändert hat:**

```bash
ansible-pull -U https://git.example.com/ops/config.git -o local.yml
```

```text
Starting Ansible Pull at 2026-10-26 11:12:17
/usr/bin/ansible-pull -U https://git.example.com/ops/config.git -o local.yml
localhost | SUCCESS => {
    "after": "5c9bef1c4897f55aaf5a87f316a508f096778417",
    "before": "5c9bef1c4897f55aaf5a87f316a508f096778417",
    "changed": false,
    "remote_url_changed": false
}
Repository has not changed, quitting: ...
```

**Das Playbook im Repository:**

```bash
cat ~/.ansible/pull/tuxdex-srv/local.yml
```

```text
- name: Base configuration
  hosts: localhost
  connection: local
  tasks:
    - name: Message of the day
      ansible.builtin.copy:
        content: "Managed by Ansible. Changes will be overwritten.\n"
        dest: ~/motd.txt
        mode: "0644"
```

## Wann brauche ich das?

- Für viele Server, die sich selbst konfigurieren sollen, etwa per Cronjob
- Für Server, die der Steuerrechner nicht erreicht, etwa Rechner hinter NAT
- Um einen neuen Server am Ende seiner Installation mit einem einzigen Befehl einzurichten

!!! tip "Als Cronjob oder Timer"
    `*/30 * * * * ansible-pull -U https://git.example.com/ops/config.git -o -s 300` prüft
    alle 30 Minuten, wendet nur Änderungen an und verteilt die Last. Siehe
    [`crontab`](../16-scheduling/crontab.md).

!!! warning "Das Repository hat Macht über den Server"
    Wer in das Repository pushen darf, kann auf jedem Server, der davon holt, beliebige
    Befehle ausführen. Schütze das Repository wie einen Root-Zugang.

## Verwandte Befehle

[ansible-playbook](ansible-playbook.md) · [ansible-vault](ansible-vault.md) · [git clone](../18-git/git-clone.md) · [crontab](../16-scheduling/crontab.md)
