# git restore

> Discards changes in the working directory or takes files back out of the staging area.

![git-restore output](../assets/screenshots/18-git/git-restore.png)

## Syntax

```bash
git restore [--staged] [--source=COMMIT] PATH...
```

## Options

| Option | Description |
|--------|-------------|
| (none) | Reset the file in the working directory to the staged or committed state |
| `--staged`, `-S` | Take the file out of the staging area, the change in the file stays |
| `--source=COMMIT`, `-s` | Restore the file as it was in this commit, branch or tag |
| `-p`, `--patch` | Choose part by part which changes to discard |
| `--worktree --staged` | Both at once: unstage and discard |

## Examples

**Discard a failed change:**

```bash
git status -s
git restore backup.sh
git status -s
```

```text
 M backup.sh
```

The second `git status` shows nothing: `backup.sh` is back in the state of the last commit.

**Take a file out of the staging area:**

```bash
git restore --staged check-disk.sh
git status -s
```

```text
 M check-disk.sh
```

**Get the version from an older commit back:**

```bash
git restore --source=v1.0 check-disk.sh
git diff
```

```text
diff --git a/check-disk.sh b/check-disk.sh
index f12cb8f..0478c3c 100644
--- a/check-disk.sh
+++ b/check-disk.sh
@@ -1,2 +1,2 @@
 #!/usr/bin/env bash
-df -hT / /srv/data /mnt/backup /var
+df -h / /srv/data /mnt/backup
```

The old version is now a normal change in the working directory. Commit it, or discard it again with `git restore check-disk.sh`.

**Bring back a deleted file:**

```bash
rm rotate-logs.sh
git restore rotate-logs.sh
ls
```

```text
README.md  backup.sh  check-disk.sh  check-services.sh  rotate-logs.sh
```

## When do I need it?

- When an edit went wrong and you want the last working version back
- When you added a file by mistake
- To get an older version of a configuration file back, for example the one from before an update

!!! tip "Older commands for the same thing"
    Older guides use `git checkout -- FILE` instead of `git restore FILE` and
    `git reset HEAD FILE` instead of `git restore --staged FILE`. Both still work.

!!! danger "Discarded is gone"
    `git restore FILE` overwrites your uncommitted changes in that file without asking.
    Git can't bring them back, because they were never in a commit.

## Related commands

[git status](git-status.md) · [git diff](git-diff.md) · [git stash](git-stash.md) · [git log](git-log.md)
