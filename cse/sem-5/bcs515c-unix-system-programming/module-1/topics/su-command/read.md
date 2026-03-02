# The su Command in Linux

## Introduction

The `su` (Substitute User or Switch User) command is one of the most fundamental and frequently used commands in Linux and Unix-like operating systems. It allows a user to temporarily switch to another user account without logging out and logging back in, providing a way to execute commands with elevated privileges or access resources belonging to other users. This command is essential for system administrators, developers, and power users who need to perform tasks that require different user permissions.

In the context of 's Computer Science and Engineering curriculum, understanding the `su` command is crucial because it forms the foundation of user management and security in Linux systems. The command plays a vital role in multi-user environments where proper privilege separation is necessary for system security. Whether you need to perform administrative tasks using root privileges or switch to another user's account to access their files, the `su` command provides the necessary mechanism. This topic is particularly important for practical examinations and laboratory sessions where students must demonstrate proficiency in Linux command-line operations.

## Key Concepts

### Basic Syntax of su Command

The general syntax of the `su` command is:

```
su [options] [username]
```

When executed without specifying a username, `su` defaults to switching to the root user (superuser). This is the most common usage pattern, especially when administrative tasks need to be performed.

### Common Options Used with su

The `su` command provides several options that modify its behavior:

- **`-` or `-l` or --login**: Starts a login shell. This option simulates a real login by setting up the environment as if the user had directly logged in. The user's home directory becomes the current directory, and environment variables like PATH, HOME, and USER are set according to the target user's profile.

- **-c command**: Executes a specific command as the target user without starting an interactive shell. This is useful for running a single command with elevated privileges.

- **-m or -p or --preserve-environment**: Preserves the current environment variables when switching users.

- **-s shell**: Specifies a particular shell to use instead of the default shell defined in `/etc/passwd`.

### Understanding the Difference Between su and sudo

While both `su` and `sudo` are used for privilege elevation, they work differently. The `su` command requires the target user's password, whereas `sudo` requires the current user's password. Additionally, `sudo` can be configured to allow specific users to run certain commands without sharing root password, providing better audit trails and security.

### Working with Root User

The root user, also known as the superuser, has complete control over the system. Using `su` to become root is a common practice for performing system administration tasks. When you switch to root, the command prompt typically changes from `$` (dollar sign) to `#` (hash symbol), indicating elevated privileges.

### Environment Variables and Shell Behavior

When using `su`, it's important to understand how environment variables are handled. Without the `-` option, the current environment is largely preserved, which can lead to unexpected behavior. Using `su -` ensures a clean environment appropriate for the target user, which is why it's generally recommended for interactive use.

### PAM and su

Pluggable Authentication Modules (PAM) play a crucial role in the `su` command's security. The `/etc/pam.d/su` configuration file controls who can use `su` and how. System administrators can configure PAM to restrict `su` access to specific groups, enabling wheel group membership as a common security practice.

## Examples

### Example 1: Switching to Root User (Interactive)

**Command:**

```
su -
```

**Explanation:** This command prompts for the root user's password. Upon successful authentication, it starts a login shell as root. The user gains full administrative privileges, and the working directory changes to root's home directory (/root).

**Step-by-step:**

1. User types `su -` and presses Enter
2. System prompts for root password (password is not displayed while typing)
3. User enters the root password
4. If authenticated, the shell changes to root's environment
5. Command prompt changes from `$` to `#`
6. User can now execute any command with root privileges

### Example 2: Running a Single Command as Another User

**Command:**

```
su -c "ls -la /var/log" username
```

**Explanation:** This command runs the `ls -la /var/log` command as the specified username without starting an interactive shell. After executing the command, control returns to the original user. This is particularly useful for scripts and one-time administrative tasks.

**Step-by-step:**

1. User types the command with `-c` option specifying the command
2. System prompts for the target user's password (or root password if running from root)
3. The specified command executes with the target user's permissions
4. Output is displayed to the terminal
5. Shell returns to the original user

### Example 3: Switching to Another Regular User

**Command:**

```
su - john
```

**Explanation:** This command switches to the user account named "john". The user must enter john's password to authenticate. This is useful when you need to troubleshoot issues in a user's environment or access files owned by that user.

**Step-by-step:**

1. User types `su - john`
2. System prompts for john's password
3. Upon successful authentication, a login shell starts as john
4. Environment is set up according to john's profile
5. Current directory changes to john's home directory
6. All commands now run with john's permissions

### Example 4: Using su in a Script

**Command:**

```
#!/bin/bash
su -c "/opt/application/bin/backup.sh" appuser
```

**Explanation:** This bash script snippet demonstrates using `su` within a script to run a backup script as a different user. This is common in automation where certain operations need to be performed with specific user permissions.

**Step-by-step:**

1. The script executes and reaches the `su` command
2. It authenticates as appuser
3. Runs the backup.sh script with appuser's permissions
4. After completion, control returns to the script
5. Script continues execution if needed

## Exam Tips

1. **Remember the syntax**: The basic syntax is `su [options] [username]`. Without a username, it defaults to root.

2. **Understand the difference between `su` and `su -`**: The hyphen (`-`) is crucial—it creates a login shell with proper environment setup, while without it, you keep the current environment.

3. **Password requirements**: `su` requires the target user's password, not the current user's password (unlike sudo).

4. **Command prompt indicator**: When switched to root, the prompt changes from `$` to `#`.

5. **The `-c` option**: Remember that `-c` allows executing a single command as another user without starting an interactive shell.

6. **Security consideration**: In production systems, prefer `sudo` over `su` for better security and audit trails.

7. **Exit the su session**: Always use the `exit` command to return to your original user account after using `su`.

8. **PAM configuration**: Know that `/etc/pam.d/su` controls `su` access permissions.

9. **Wheel group**: The wheel group is often used to restrict who can use `su` to become root.

10. **Home directory**: Using `su - username` changes to the target user's home directory; without the dash, you stay in the current directory.
