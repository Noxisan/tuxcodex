# Understanding Git

Git records the state of a directory as a series of snapshots called **commits**. Every
commit says who changed what, when and why, and you can go back to any of them. For an
admin, that means: scripts and configuration files with a complete history, changes you
can undo, and the same files on several servers.

## The three areas

```text
working directory  ──git add──►  staging area  ──git commit──►  repository
       ▲                                                             │
       └────────────────── git restore / git switch ─────────────────┘
```

| Area | What it is |
|------|------------|
| **Working directory** | The files you see and edit |
| **Staging area** (index) | The changes you have marked for the next commit with [`git add`](git-add.md) |
| **Repository** | All commits, stored in the hidden `.git` directory |

You decide what goes into a commit: edit three files, add two of them, commit. The third
change stays in the working directory for a later commit.

## Setting up Git once

Every commit carries a name and an email address. Set them once per user:

```text
$ git config --global user.name "Nox"
$ git config --global user.email nox@example.com
$ git config --global init.defaultBranch main
```

The settings end up in `~/.gitconfig`, see [`git config`](git-config.md).

## Ignoring files

A `.gitignore` file in the repository lists files Git should never track: logs,
temporary files and, above all, secrets.

```text
# Logs and temporary files
*.log
*.swp
tmp/

# Secrets never belong in a repository
.env
*.key
```

[`git status`](git-status.md) doesn't show ignored files, and `git add .` skips them.
Add `.gitignore` itself to the repository, so that it applies everywhere.

## SSH keys for GitHub and GitLab

Git servers like GitHub, GitLab or Gitea use SSH keys for authentication. Create a key,
see [`ssh-keygen`](../12-ssh/ssh-keygen.md), and add the public key in your account:
on GitHub under *Settings › SSH and GPG keys*, on GitLab under *Preferences › SSH Keys*.

```text
$ ssh-keygen -t ed25519 -C "nox@tuxdex-srv"
$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK3vYf2mPqT8wZr5nB7dXc1hL0sQe9uJgN4aRtVy6oMp nox@tuxdex-srv
$ ssh -T git@github.com
Hi nox! You've successfully authenticated, but GitHub does not provide shell access.
```

Repository addresses then look like `git@github.com:nox/scripts.git`. The examples in this
chapter use the Git server `git.example.com`.

## The daily workflow

```text
$ git pull                       # get the latest state from the server
$ vim check-disk.sh              # change something
$ git status                     # what has changed?
$ git diff                       # what exactly?
$ git add check-disk.sh          # mark the change for the commit
$ git commit -m "Also check /var"
$ git push                       # send it to the server
```

For larger changes, work on a separate branch, see [`git switch`](git-switch.md) and
[`git merge`](git-merge.md).

## Good commit messages

| Do | Don't |
|----|-------|
| `Raise PHP memory limit to 256M` | `changes` |
| `Fix backup path for /srv/data` | `fix` |
| One logical change per commit | A week of work in a single commit |

The first line is a short summary (around 50 characters, imperative: "Add", "Fix",
"Remove"). If it needs more explanation, leave an empty line and write the details below.

## Distribution differences

| | Debian | Ubuntu | RHEL | Arch |
|---|--------|--------|------|------|
| Preinstalled | no | yes (server installation) | no | no |
| Install | `sudo apt install git` | `sudo apt install git` | `sudo dnf install git` | `sudo pacman -S git` |

!!! tip "Keep /etc under version control"
    The package `etckeeper` puts `/etc` into a Git repository and commits automatically
    before and after every package installation. That way you can see exactly which
    configuration file changed and when.

!!! danger "No passwords or keys in a repository"
    Whatever you commit stays in the history, even after you delete the file again. A
    password that was pushed once is compromised: change it. Keep secrets out with
    `.gitignore` from the start.
