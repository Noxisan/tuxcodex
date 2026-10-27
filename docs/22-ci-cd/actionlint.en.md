# actionlint

> Checks GitHub Actions workflow files for mistakes: wrong keys, unknown variables, outdated actions and shell errors in run steps.

![actionlint output](../assets/screenshots/22-ci-cd/actionlint.png)

## Syntax

```bash
actionlint [OPTIONS] [FILE...]
```

## Options

| Option | Description |
|--------|-------------|
| (none) | Check all files in `.github/workflows/` of the current repository |
| `FILE` | Only these workflow files |
| `-oneline` | One line per problem, for scripts and editors |
| `-ignore PATTERN` | Ignore messages that match the pattern |
| `-shellcheck=` | Don't check `run:` scripts with ShellCheck (it does so when installed) |
| `-color` | Colored output, also when piped |

## Examples

**Check all workflows of the repository:**

```bash
actionlint
```

```text
.github/workflows/deploy.yml:4:5: unexpected key "branch" for "push" section. expected one of "branches", "branches-ignore", "paths", "paths-ignore", "tags", "tags-ignore", "types", "workflows" [syntax-check]
  |
4 |     branch: main
  |     ^~~~~~~
.github/workflows/deploy.yml:9:15: the runner of "actions/checkout@v2" action is too old to run on GitHub Actions. update the action's version to fix this issue [action]
  |
9 |       - uses: actions/checkout@v2
  |               ^~~~~~~~~~~~~~~~~~~
.github/workflows/deploy.yml:13:22: undefined variable "secret". available variables are "env", "github", "inputs", "job", "matrix", "needs", "runner", "secrets", "steps", "strategy", "vars" [expression]
   |
13 |           TOKEN: ${{ secret.DEPLOY_TOKEN }}
   |                      ^~~~~~~~~~~~~~~~~~~
```

Three mistakes that GitHub would only report after the push, or not at all: `branch` instead of `branches` means the workflow silently never starts.

**One line per problem:**

```bash
actionlint -oneline
```

```text
.github/workflows/deploy.yml:4:5: unexpected key "branch" for "push" section. expected one of "branches", "branches-ignore", "paths", "paths-ignore", "tags", "tags-ignore", "types", "workflows" [syntax-check]
.github/workflows/deploy.yml:9:15: the runner of "actions/checkout@v2" action is too old to run on GitHub Actions. update the action's version to fix this issue [action]
.github/workflows/deploy.yml:13:22: undefined variable "secret". available variables are "env", "github", "inputs", "job", "matrix", "needs", "runner", "secrets", "steps", "strategy", "vars" [expression]
```

**No output means no problems:**

```bash
actionlint .github/workflows/ci.yml && echo OK
```

```text
OK
```

## When do I need it?

- Before every push that changes a workflow
- As a pre-commit hook, so that broken workflows don't even get committed
- To find outdated actions that GitHub will stop running

!!! tip "Uses ShellCheck automatically"
    If [`shellcheck`](../17-bash-scripting/shellcheck.md) is installed, actionlint also
    checks the shell code in every `run:` step, including quoting mistakes with `${{ }}`.

## Related commands

[act](act.md) · [yamllint](yamllint.md) · [pre-commit](pre-commit.md) · [shellcheck](../17-bash-scripting/shellcheck.md)
