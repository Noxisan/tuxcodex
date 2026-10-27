# ansible-lint

> Checks playbooks and roles for errors, bad practices and style problems before they run.

![ansible-lint output](../assets/screenshots/21-ansible/ansible-lint.png)

## Syntax

```bash
ansible-lint [OPTIONS] [FILE|DIRECTORY...]
```

## Options

| Option | Description |
|--------|-------------|
| (none) | Check the whole project in the current directory |
| `FILE` | Only check these playbooks or roles |
| `--fix` | Fix what can be fixed automatically, such as FQCN and YAML formatting |
| `--profile NAME` | Strictness: `min`, `basic`, `moderate`, `safety`, `shared`, `production` |
| `-x RULE` | Skip a rule |
| `-L` | List all rules |
| `-p` | Compact output, one line per problem |

## Examples

**Check a playbook with problems:**

```bash
cat lint-bad.yml
ansible-lint -p lint-bad.yml
```

```text
- hosts: web
  become: yes
  tasks:
    - apt: name=nginx state=latest
    - shell: systemctl restart nginx
lint-bad.yml:1:3: name[play]: All plays should be named.
lint-bad.yml:2: yaml[truthy]: Truthy value should be one of [false, true]
lint-bad.yml:4:7: fqcn[action-core]: Use FQCN for builtin module actions (apt).
lint-bad.yml:4: name[missing]: All tasks should be named.
lint-bad.yml:4: no-free-form: Avoid using free-form when calling module actions. (apt)
lint-bad.yml:4: package-latest: Package installs should not use latest.
lint-bad.yml:5: command-instead-of-module: systemctl used in place of systemd module
lint-bad.yml:5: command-instead-of-shell: Use shell only when shell functionality is required.
lint-bad.yml:5:7: fqcn[action-core]: Use FQCN for builtin module actions (shell).
lint-bad.yml:5: name[missing]: All tasks should be named.
lint-bad.yml:5: no-changed-when: Commands should not change things if nothing needs doing.
```

**The full output with a summary:**

```bash
ansible-lint lint-bad.yml | tail -15
```

```text
# Rule Violation Summary

  1 command-instead-of-module profile:basic tags:command-shell,idiom
  1 command-instead-of-shell profile:basic tags:command-shell,idiom
  1 no-free-form profile:basic tags:syntax,risk
  2 name profile:basic tags:idiom
  1 name profile:basic tags:idiom
  1 yaml profile:basic tags:formatting,yaml
  1 package-latest profile:basic tags:idempotency
  1 no-changed-when profile:basic tags:command-shell,idempotency
  2 fqcn profile:basic tags:formatting

Failed: 11 failure(s), 0 warning(s) on 1 files. Last profile that met the validation criteria was 'min'.
```

**A clean playbook:**

```bash
ansible-lint site.yml
```

```text
Passed: 0 failure(s), 0 warning(s) on 1 files. Last profile that met the validation criteria was 'production'.
```

`site.yml` from the [basics](basics.md) even meets `production`, the strictest profile.

## When do I need it?

- Before every commit of an Ansible project
- In a CI pipeline, so that faulty playbooks never reach the servers
- To learn good habits: every rule explains what's wrong and why

!!! tip "Configuration per project"
    A file `.ansible-lint` in the project sets the profile and rules to skip, for example
    `profile: production` and `skip_list: [yaml[line-length]]`.

!!! warning "Fix the reason, not the message"
    `# noqa` at the end of a line hides a finding. Use it only when you have a good reason,
    and write the reason next to it.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Install | `sudo apt install ansible-lint` | `sudo apt install ansible-lint` | `pipx install ansible-lint` | `sudo pacman -S ansible-lint` |

## Related commands

[ansible-playbook](ansible-playbook.md) · [ansible-galaxy](ansible-galaxy.md) · [shellcheck](../17-bash-scripting/shellcheck.md)
