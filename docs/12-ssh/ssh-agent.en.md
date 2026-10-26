# ssh-agent

> Keeps your unlocked SSH keys in memory, so you only enter the passphrase once per session instead of on every connection.

![ssh-agent output](../assets/screenshots/12-ssh/ssh-agent.png)

## Syntax

```bash
ssh-agent [OPTION]...
```

Usually you start it with `eval "$(ssh-agent)"`, so your shell gets its variables. The agent itself doesn't load keys. You add them with [`ssh-add`](ssh-add.md).

## Options

| Option | Description |
|--------|-------------|
| *(none)* | Start an agent and print the variables your shell needs |
| `-k` | Stop the running agent |
| `-t TIME` | Default lifetime for added keys, e.g. `1h` |
| `-s`, `-c` | Print the variables for `sh`/`bash` or for `csh` |

## Examples

**Start an agent in the current shell:**

```bash
eval "$(ssh-agent)"
```

```text
Agent pid 4365
```

`eval` sets the variables `SSH_AUTH_SOCK` and `SSH_AGENT_PID` in your shell. Every `ssh`
you start from it finds the agent through them.

**See what `ssh-agent` prints without `eval`:**

```bash
ssh-agent
```

```text
SSH_AUTH_SOCK=/tmp/ssh-pDL3fcapSHNe/agent.4364; export SSH_AUTH_SOCK;
SSH_AGENT_PID=4365; export SSH_AGENT_PID;
echo Agent pid 4365;
```

These are shell commands. Without `eval`, they are only printed and the agent can't be
found.

**No agent is running:**

```bash
ssh-add -l
```

```text
Could not open a connection to your authentication agent.
```

`SSH_AUTH_SOCK` isn't set in this shell. Start an agent first.

**Stop the agent when you are done:**

```bash
eval "$(ssh-agent -k)"
```

```text
Agent pid 4365 killed
```

## When do I need it?

- When you work with keys protected by a passphrase and connect to many servers
- In scripts that need several SSH connections in a row
- On servers where you need your key for further connections, via agent forwarding

!!! tip "Desktop systems start it for you"
    Most desktop environments and macOS start an agent at login. Check with
    `echo $SSH_AUTH_SOCK`: if it shows a path, an agent is already running.

!!! warning "Agent forwarding only to trusted servers"
    With `ssh -A`, the server can use your agent while you are connected. A root user on
    that server could then log in to other servers with your key. Prefer `ssh -J` for
    jump hosts.

## Related commands

[ssh-add](ssh-add.md) · [ssh](ssh.md) · [ssh-keygen](ssh-keygen.md) · [ssh-add](ssh-add.md)
