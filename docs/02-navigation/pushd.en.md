# pushd

> Changes to a directory and remembers the previous one on a stack, so you can jump back later.

![pushd output](../assets/screenshots/02-navigation/pushd.png)

## Syntax

```bash
pushd [-n] [DIRECTORY | +N | -N]
```

## Options

| Option / argument | Description |
|-------------------|-------------|
| `DIRECTORY` | Put `DIRECTORY` on top of the stack and change to it |
| *(none)* | Swap the two top entries and change to the new top |
| `+N` | Rotate the stack so that entry `N` (counted from the left, starting at 0) is on top |
| `-N` | Same as `+N`, but counted from the right |
| `-n` | Only change the stack, do not change the directory |

The stack is shown with `dirs`: `dirs -v` numbers the entries, `dirs -c` clears the stack.

## Examples

**Change to a directory and remember where you came from:**

```bash
pushd /etc/nginx
```

```text
/etc/nginx ~
```

The output is the stack: the current directory on the left, the remembered ones to the
right of it.

**Add another directory:**

```bash
pushd /var/log/nginx
```

```text
/var/log/nginx /etc/nginx ~
```

**Show the stack with numbers:**

```bash
dirs -v
```

```text
 0  /var/log/nginx
 1  /etc/nginx
 2  ~
```

**Switch between the two top directories:**

```bash
pushd
```

```text
/etc/nginx /var/log/nginx ~
```

**Jump to a specific entry of the stack:**

```bash
pushd +2
```

```text
~ /etc/nginx /var/log/nginx
```

**Add a directory to the stack without changing into it:**

```bash
pushd -n /tmp
```

```text
~ /tmp /etc/nginx /var/log/nginx
```

## When do I need it?

- When you work in several places at once, for example editing a config in `/etc/nginx`
  and checking the result in `/var/log/nginx`
- In scripts that briefly work in another directory and then return to where they
  started (together with [`popd`](popd.md))
- When `cd -` is not enough because you need more than two directories

!!! tip "`pushd` without arguments"
    `pushd` alone swaps the two top directories. It works like `cd -`, but the other
    remembered directories stay on the stack.

!!! warning "The stack only lives in the current shell"
    The directory stack is lost when you close the shell or the SSH session. Every shell
    and every script has its own stack.

## Related commands

[cd](cd.md) · [pwd](pwd.md) · [popd](popd.md)
