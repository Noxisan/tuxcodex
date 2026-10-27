# ansible-vault

> Verschlüsselt Dateien und Werte mit einem Passwort, damit Geheimnisse ins Git-Repository des Projekts dürfen.

![ansible-vault output](../assets/screenshots/21-ansible/ansible-vault.png)

## Syntax

```bash
ansible-vault create | encrypt | decrypt | view | edit | rekey DATEI
ansible-vault encrypt_string WERT --name VARIABLE
```

## Optionen

| Option | Beschreibung |
|--------|--------------|
| `create DATEI` | Eine neue verschlüsselte Datei im Editor anlegen |
| `encrypt DATEI` | Eine bestehende Datei verschlüsseln |
| `view DATEI` | Den Inhalt zeigen, ohne ihn entschlüsselt zu speichern |
| `edit DATEI` | Im Editor bearbeiten, danach wieder verschlüsseln |
| `decrypt DATEI` | Dauerhaft entschlüsseln |
| `rekey DATEI` | Das Vault-Passwort ändern |
| `encrypt_string` | Einen einzelnen Wert für eine normale YAML-Datei verschlüsseln |
| `--vault-password-file DATEI` | Das Passwort aus einer Datei lesen statt nachzufragen |

## Beispiele

**Eine Datei mit Passwörtern verschlüsseln:**

```bash
ansible-vault encrypt group_vars/secrets.yml
```

```text
New Vault password:
Confirm New Vault password:
Encryption successful
```

**Wie die Datei jetzt aussieht:**

```bash
head -3 group_vars/secrets.yml
```

```text
$ANSIBLE_VAULT;1.1;AES256
37626437363538343563666534313964333566323336393839383138626636376538383034656262
6463643237393466356266303034303132393431616464310a383131396365653136636362313431
```

**Den Inhalt lesen:**

```bash
ansible-vault view --vault-password-file ~/.vault_pass group_vars/secrets.yml
```

```text
db_password: S3cr3t-Pa55
```

**Einen einzelnen Wert verschlüsseln:**

```bash
ansible-vault encrypt_string --vault-password-file ~/.vault_pass 'S3cr3t-Pa55' --name db_password
```

```text
db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          39356637356462313933343739313665396566343538303430613339663830393138663233393730
          3361643539663062386234306235383966356231323939390a633932343230393339363466653938
          37633630653434326232636138376266653661653832363263663838663632336335386639383065
          3163316534616634360a303961373638323463643334373139303231613735666130333437643932
          6331
```

Füg die Ausgabe in eine normale Variablendatei ein. Der Rest der Datei bleibt lesbar.

**Ein Playbook mit verschlüsselten Variablen ausführen:**

```bash
ansible-playbook site.yml --ask-vault-pass --limit web01 --tags packages
```

```text
Vault password:

PLAY [Set up web servers] ******************************************************

TASK [Gathering Facts] *********************************************************
ok: [web01]

TASK [Install nginx] ***********************************************************
ok: [web01]

PLAY RECAP *********************************************************************
web01                      : ok=2    changed=0   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Wann brauche ich das?

- Für Passwörter, API-Schlüssel und private Schlüssel, die ein Playbook braucht
- Um ein ganzes Projekt in Git abzulegen, ohne Geheimnisse preiszugeben
- In CI-Pipelines, zusammen mit einer Passwortdatei, die nur die Pipeline kennt

!!! tip "Passwortdatei statt Eintippen"
    Leg das Vault-Passwort in `~/.vault_pass` mit den Rechten `600` ab und setze
    `vault_password_file = ~/.vault_pass` in der `ansible.cfg`. Committe diese Datei nie.

!!! danger "Passwort weg, Daten weg"
    Ohne das Passwort lässt sich eine Vault-Datei nicht entschlüsseln. Bewahre es in deinem
    Passwortmanager auf.

## Verwandte Befehle

[ansible-playbook](ansible-playbook.md) · [ansible-pull](ansible-pull.md) · [ansible-config](ansible-config.md)
