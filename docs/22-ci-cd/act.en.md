# act

> Runs GitHub Actions workflows locally in Docker containers, so you can test them before pushing.

![act output](../assets/screenshots/22-ci-cd/act.png)

## Syntax

```bash
act [EVENT] [-j JOB] [OPTIONS]
```

## Options

| Option | Description |
|--------|-------------|
| `EVENT` | Event to simulate, such as `push` (default) or `pull_request` |
| `-l`, `--list` | List the workflows and jobs |
| `-j JOB` | Only this job (plus the jobs it `needs`) |
| `-n`, `--dryrun` | Only show what would run |
| `-W FILE` | Only this workflow file |
| `-s NAME=VALUE`, `--secret-file FILE` | Secrets for the run |
| `-P LABEL=IMAGE` | Docker image for a runner label, such as `ubuntu-latest` |

On the first start, `act` asks which image size to use and saves the answer in `~/.config/act/actrc`.

## Examples

**Run one job locally:**

```bash
act -j lint
```

```text
[CI/lint] ⭐ Run Set up job
[CI/lint] 🚀  Start image=catthehacker/ubuntu:act-latest
[CI/lint]   🐳  docker pull image=catthehacker/ubuntu:act-latest platform= username= forcePull=true
[CI/lint]   ✅  Success - Set up job
[CI/lint] ⭐ Run Main actions/checkout@v4
[CI/lint]   ✅  Success - Main actions/checkout@v4 [14.629988ms]
[CI/lint] ⭐ Run Main Install ShellCheck (only for act)
[CI/lint]   | Setting up shellcheck (0.9.0-1) ...
[CI/lint]   ✅  Success - Main Install ShellCheck (only for act) [4.076535426s]
[CI/lint] ⭐ Run Main Check shell scripts
[CI/lint]   ✅  Success - Main Check shell scripts [45.057346ms]
[CI/lint] ⭐ Run Complete job
[CI/lint]   ✅  Success - Complete job
[CI/lint] 🏁  Job succeeded
```

Shortened; with every step, `act` also prints the Docker commands it runs.

**The jobs of all workflows:**

```bash
act -l
```

```text
Stage  Job ID  Job name  Workflow name  Workflow file  Events
0      lint    lint      CI             ci.yml         pull_request,push
1      build   build     CI             ci.yml         push,pull_request
```

**A tool missing in the act image:**

```bash
act -j lint
```

```text
[CI/lint] ⭐ Run Main Check shell scripts
[CI/lint]   🐳  docker exec cmd=[bash -e /var/run/act/workflow/1] user= workdir=
[CI/lint]   | /var/run/act/workflow/1: line 2: shellcheck: command not found
[CI/lint]   ❌  Failure - Main Check shell scripts [44.675812ms]
[CI/lint] exitcode '127': command not found, please refer to https://github.com/nektos/act/issues/107 for more information
[CI/lint] 🏁  Job failed
Error: Job 'lint' failed
```

On GitHub, `shellcheck` is preinstalled. The fix is the step with `if: ${{ env.ACT }}` from the tip below.

**Only show what would run:**

```bash
act -n | grep -E 'Run Main|Job succeeded'
```

```text
*DRYRUN* [CI/lint] ⭐ Run Main actions/checkout@v4
*DRYRUN* [CI/lint] ⭐ Run Main Check shell scripts
*DRYRUN* [CI/lint] 🏁  Job succeeded
*DRYRUN* [CI/build] ⭐ Run Main actions/checkout@v4
*DRYRUN* [CI/build] ⭐ Run Main Build image
*DRYRUN* [CI/build] 🏁  Job succeeded
```

## When do I need it?

- To test a change to a workflow without a series of "fix CI" commits
- To find out why a job fails, with direct access to the container
- To run checks of a project offline

!!! tip "Steps only for act"
    `act` sets the variable `ACT`. With `if: ${{ env.ACT }}` a step only runs locally, for
    example to install a tool that the GitHub runners already have.

!!! warning "The images aren't the GitHub runners"
    The default images of `act` are much smaller than the real `ubuntu-latest` runner. Tools
    like `shellcheck` may be missing, so a job can fail locally but pass on GitHub.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Install | install script from nektos/act | install script from nektos/act | install script from nektos/act | `sudo pacman -S act` |

## Related commands

[actionlint](actionlint.md) · [gh run](gh-run.md) · [docker run](../19-docker/docker-run.md)
