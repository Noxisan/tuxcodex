# pre-commit

> Runs checks such as linters and formatters automatically before every Git commit, as configured in the project.

![pre-commit output](../assets/screenshots/22-ci-cd/pre-commit.png)

## Syntax

```bash
pre-commit install | run [--all-files] | autoupdate | uninstall
```

## Options

| Option | Description |
|--------|-------------|
| `install` | Set up the Git hook in `.git/hooks/pre-commit` |
| `run` | Run the checks on the staged files |
| `run --all-files` | Run them on all files, for example after setting it up |
| `run HOOK_ID` | Only one check, such as `shellcheck` |
| `autoupdate` | Update the versions of the hooks in the configuration |
| `uninstall` | Remove the Git hook |

The checks are listed in `.pre-commit-config.yaml` in the repository, each with a fixed version.

## Examples

**Set up the hook in a repository:**

```bash
pre-commit install
```

```text
pre-commit installed at .git/hooks/pre-commit
```

**The configuration:**

```bash
cat .pre-commit-config.yaml
```

```text
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
  - repo: https://github.com/shellcheck-py/shellcheck-py
    rev: v0.10.0.1
    hooks:
      - id: shellcheck
```

**Check all files once:**

```bash
pre-commit run --all-files
```

```text
trim trailing whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing scripts/deploy.sh

fix end of files.........................................................Passed
check yaml...............................................................Failed
- hook id: check-yaml
- exit code: 1

while constructing a mapping
  in "compose.yaml", line 3, column 5
found duplicate key "restart" with value "unless-stopped" (original value: "yes")
  in "compose.yaml", line 7, column 5

shellcheck...............................................................Failed
- hook id: shellcheck
- exit code: 1

In scripts/deploy.sh line 2:
rm -rf $TARGET/old
       ^-----^ SC2086 (info): Double quote to prevent globbing and word splitting.
```

The first run downloads the hooks into `~/.cache/pre-commit`, which takes a moment. The trailing spaces were fixed right away; the other two problems you fix yourself.

**A commit is stopped:**

```bash
git commit -m "Add deploy script"
```

```text
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check yaml...............................................................Passed
shellcheck...............................................................Failed
- hook id: shellcheck
- exit code: 1

In scripts/deploy.sh line 2:
rm -rf $TARGET/old
       ^-----^ SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean:
rm -rf "$TARGET"/old
```

The commit wasn't created. Fix the script, `git add` it again and commit.

## When do I need it?

- So that mistakes are caught on your machine instead of in the pipeline
- To give everyone in a team the same checks with one command
- To fix trailing spaces and missing line ends automatically

!!! tip "The same checks in the pipeline"
    Run `pre-commit run --all-files` as a step in CI too. Then nothing gets through that
    skipped the hook on someone's machine.

!!! warning "Hooks can be skipped"
    `git commit --no-verify` skips all hooks. pre-commit is a help, not a guarantee, which
    is why the pipeline should check as well.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Install | `sudo apt install pre-commit` | `sudo apt install pre-commit` | `pipx install pre-commit` | `sudo pacman -S pre-commit` |

## Related commands

[yamllint](yamllint.md) · [actionlint](actionlint.md) · [git commit](../18-git/git-commit.md) · [shellcheck](../17-bash-scripting/shellcheck.md)
