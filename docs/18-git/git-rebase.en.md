# git rebase

> Moves the commits of a branch onto the latest state of another branch, as if you had only started now.

![git-rebase output](../assets/screenshots/18-git/git-rebase.png)

## Syntax

```bash
git rebase [OPTIONS] [BRANCH]
```

## Options

| Option | Description |
|--------|-------------|
| `BRANCH` | Put the commits of the current branch on top of this branch |
| `-i`, `--interactive` | Edit the list of commits first: reorder, combine, reword or drop |
| `--continue` | Continue after resolving a conflict |
| `--skip` | Leave out the commit that causes the conflict |
| `--abort` | Cancel and restore the state before the rebase |

## Examples

**Bring a branch up to date with main:**

```bash
git switch fix-paths
git rebase main
```

```text
Switched to branch 'fix-paths'
Successfully rebased and updated refs/heads/fix-paths.
```

**The history before and after:**

```bash
git log --oneline --graph main fix-paths
```

```text
* 5f9cfee (HEAD -> fix-paths) Check /var too
* 6e6f0af (main) Show filesystem type
*   bdb6db4 Merge branch rotate-logs
```

Before the rebase, `fix-paths` branched off at `bdb6db4`. Now its commit sits on top of `main` with a new ID, and `git merge fix-paths` on `main` becomes a simple fast-forward.

**A conflict during the rebase:**

```bash
git rebase main
```

```text
Auto-merging check-disk.sh
CONFLICT (content): Merge conflict in check-disk.sh
error: could not apply 41c53d9... Check /var too
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
hint: Disable this message with "git config advice.mergeConflict false"
Could not apply 41c53d9... Check /var too
```

**Continue after resolving it:**

```bash
git add check-disk.sh
git rebase --continue
```

```text
[detached HEAD 5f9cfee] Check /var too
 1 file changed, 1 insertion(+), 1 deletion(-)
Successfully rebased and updated refs/heads/fix-paths.
```

**Tidy up the last commits before pushing:**

```bash
git rebase -i HEAD~3
```

```text
pick fcdca2b Add service check
pick b9d2121 Document check scripts
pick 599c398 Rotate logs after 14 days

# Rebase 5f9cfee..599c398 onto 5f9cfee (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
# ...
# d, drop <commit> = remove commit
```

The editor shows one line per commit, oldest first. Change `pick` to `squash` to combine a commit with the one above it, or to `drop` to remove it. Saving starts the rebase.

## When do I need it?

- To bring a branch you are working on up to date with `main`
- To tidy up your own commits before pushing, with `-i`
- Automatically with `git pull --rebase`, for a straight history without merge commits

!!! tip "Merge or rebase?"
    Both bring the same changes together. `git merge` keeps the history as it happened,
    `git rebase` makes it straight and easier to read. For your own, unpushed commits,
    rebase is a good choice.

!!! danger "Never rebase pushed commits"
    A rebase creates new commits with new IDs. If others have already pulled the old ones,
    their history no longer matches and you end up with duplicate commits. Only rebase
    commits that exist on your machine alone.

## Related commands

[git merge](git-merge.md) · [git branch](git-branch.md) · [git pull](git-pull.md) · [git log](git-log.md)
