# The su Command in Linux - Summary

## Key Definitions and Concepts

- **su (Substitute User/Switch User)**: A Linux command that allows switching to another user account without logging out, providing temporary access to that user's privileges and environment.

- **Root User (Superuser)**: The administrator account with complete system control, identified by UID 0 and represented by the `#` prompt.

- **Login Shell**: A shell started as if the user had directly logged in, established using `su -` or `su -l`.

- **PAM (Pluggable Authentication Modules)**: System security framework that controls authentication for commands like `su`.

## Important Formulas and Theorems

The `su` command follows this general syntax:

```
su [options] [username]
```

Common options:

- `-` or `-l`: Start login shell
- `-c "command"`: Execute single command
- `-m` or `-p`: Preserve environment
- `-s shell`: Specify shell

## Key Points

1. `su` without username defaults to root user access
2. The `-` option (login shell) sets proper environment variables and changes to user's home directory
3. `su` requires target user's password for authentication
4. The `-c` option runs a single command without interactive shell
5. Root prompt is `#`, regular user prompt is `$`
6. Always use `exit` to return to original user
7. `/etc/pam.d/su` configures su security policies
8. Wheel group membership often restricts root access

## Common Mistakes to Avoid

- Forgetting to use `-` when a clean environment is needed, leading to PATH and permission issues
- Not exiting the su session and continuing as wrong user
- Confusing `su` with `su -` (one creates login shell, other doesn't)
- Using `su` without understanding security implications

## Revision Tips

1. Practice both `su` and `su -` to understand environment differences
2. Remember: `su` = current directory, `su -` = user's home directory
3. The `-c` option is essential for single-command execution in scripts
4. Always verify your current user with `whoami` command
5. Know the difference: `su` needs target password, `sudo` needs your own password
