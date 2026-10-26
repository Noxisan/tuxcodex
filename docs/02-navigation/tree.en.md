# tree

> Shows the contents of a directory and all its subdirectories as a tree.

![tree output](../assets/screenshots/02-navigation/tree.png)

## Syntax

```bash
tree [OPTION]... [DIRECTORY]...
```

## Options

| Option | Description |
|--------|-------------|
| `-L LEVEL` | Only show `LEVEL` levels deep |
| `-d` | Show directories only |
| `-a` | Also show hidden files |
| `-I PATTERN` | Hide files matching `PATTERN` (e.g. `'*.gz'`) |
| `-P PATTERN` | Only show files matching `PATTERN` |
| `-f` | Show the full path of every entry |
| `-h` | Show file sizes in K, M, G |
| `-p` | Show permissions like `ls -l` |
| `-u` | Show the owner |
| `--dirsfirst` | Show directories before files |
| `--du` | Show the total size of each directory |

## Examples

**Show the current directory as a tree:**

```bash
tree
```

```text
.
├── backup
│   ├── db-2026-10-20.sql.gz
│   └── etc-2026-10-20.tar.gz
├── notes.txt
└── scripts
    ├── backup.sh
    └── cleanup.sh

2 directories, 5 files
```

**Only show the first level:**

```bash
tree -L 1
```

```text
.
├── backup
├── notes.txt
└── scripts

2 directories, 1 file
```

**Show directories only:**

```bash
tree -d
```

```text
.
├── backup
└── scripts

2 directories
```

**Also show hidden files:**

```bash
tree -a -L 1
```

```text
.
├── .bash_history
├── .bash_logout
├── .bashrc
├── .profile
├── backup
├── notes.txt
└── scripts

2 directories, 5 files
```

**Hide certain files:**

```bash
tree -I '*.gz'
```

```text
.
├── backup
├── notes.txt
└── scripts
    ├── backup.sh
    └── cleanup.sh

2 directories, 3 files
```

## When do I need it?

- To get an overview of an unknown directory, for example a web project in `/var/www`
  or a configuration directory like `/etc/nginx`
- To document the structure of a project or a backup in a README or a ticket
- To quickly check whether a deployment put all files in the right place

!!! tip "Always limit the depth on large directories"
    `tree /` or `tree /usr` prints hundreds of thousands of lines. Use `-L 2` or `-d` to
    keep the output readable.

!!! warning "Not installed by default"
    `tree` is not part of a minimal Debian installation. Install it with:

    ```bash
    sudo apt install tree
    ```

## Related commands

[ls](ls.md) · [cd](cd.md) · [find](find.md)
