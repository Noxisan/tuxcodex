# Working safely with files

Most mistakes with files happen in a second and can't be undone. These habits protect
you on every server:

| Habit | Example |
|-------|---------|
| Make a copy before you edit a configuration | `cp sshd_config{,.bak}` |
| Test wildcards with `ls` before using them with `rm` or `mv` | `ls *.log` → `rm *.log` |
| Let `cp`, `mv` and `rm` ask before overwriting or deleting | `cp -i`, `mv -i`, `rm -i` |
| Copy with permissions and timestamps | `cp -a` instead of `cp -r` |
| Check where you are before using relative paths | `pwd` |
| Use quotes for names with spaces | `rm "old backup.tar.gz"` |
