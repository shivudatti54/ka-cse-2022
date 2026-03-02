# Becoming the Super User (Root User) in Linux - Summary

## Key Definitions and Concepts

- **Root User (Super User):** The most privileged account in Linux with UID 0, having unrestricted access to all system resources, files, and commands.
- **su (Substitute User):** A command that allows switching to another user account, typically used to become root by entering the root password.
- **sudo (Super User Do):** A command that executes commands with elevated privileges using the current user's own password, configured in `/etc/sudoers`.
- **/etc/sudoers:** The configuration file that defines which users can use sudo and what commands they are authorized to execute.
- **visudo:** A safe editing tool for `/etc/sudoers` that performs syntax validation before saving.

## Important Formulas and Syntax

- `su -` : Switch to root with full login environment
- `su - username` : Switch to specific user
- `sudo command` : Execute command as root
- `sudo -u user command` : Execute command as specific user
- `sudo -i` : Open interactive root shell
- Sudoers format: `username ALL=(ALL:ALL) ALL`

## Key Points

- The root account has UID 0 and can bypass all permission restrictions in Linux.
- The `$` prompt indicates a regular user; the `#` prompt indicates root privileges.
- `su` requires the root password; `sudo` uses the user's own password for authentication.
- `sudo` provides better security through timeout mechanisms and command logging.
- The `visudo` command should always be used to edit `/etc/sudoers` to prevent syntax errors.
- Using `su -` initializes a complete login shell environment, while `su` preserves the current environment.
- Sudo maintains an audit trail by logging all commands to system log files.
- Production systems should prefer `sudo` over direct root login for security.

## Common Mistakes to Avoid

1. **Editing sudoers directly:** Never use a text editor directly on `/etc/sudoers`; always use `visudo` to prevent syntax errors that can lock you out.

2. **Forgetting to exit root shell:** Forgetting that you are root and accidentally executing destructive commands can harm the system.

3. **Sharing root password:** The root password should never be shared; use sudo with individual user accounts instead.

4. **Not understanding environment differences:** Using `su` without `-` can lead to unexpected behavior due to preserved environment variables.

## Revision Tips

1. **Practice both commands:** Create a virtual machine and practice switching between users using both `su` and `sudo` commands.

2. **Remember visual cues:** The prompt symbol (`$` vs `#`) is the quickest way to verify your current privilege level.

3. **Focus on security differences:** Understanding why `sudo` is preferred over `su` in modern systems is crucial for exams.

4. **Review sudoers syntax:** Be familiar with the basic structure of sudoers entries as this commonly appears in practical exams.
