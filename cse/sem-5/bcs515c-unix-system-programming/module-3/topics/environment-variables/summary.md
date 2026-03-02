# Environment Variables in Linux/Unix - Summary

## Key Definitions and Concepts

- **Environment Variables**: Dynamic name-value pairs that provide configuration information to processes running in an operating system
- **Shell Variables**: Variables local to the current shell session that are not inherited by child processes
- **Export**: Command used to convert shell variables to environment variables for process inheritance
- **PATH**: Colon-separated directory list that the shell searches for executable commands

## Important Formulas and Techniques

- Setting variable: `VARIABLE=value`
- Exporting variable: `export VARIABLE` or `export VARIABLE=value`
- Viewing variables: `printenv VARIABLE` or `echo $VARIABLE`
- Listing all: `env` or `printenv`
- Removing variable: `unset VARIABLE`
- Permanent setup: Add export statements to `~/.bashrc` or `~/.bash_profile`

## Key Points

- Environment variables enable process communication and system configuration without code modifications
- The PATH variable is crucial for command execution; directories are searched left to right
- Shell variables exist only in the current shell; environment variables are inherited by all child processes
- Configuration files like `/etc/profile`, `~/.bashrc`, and `~/.bash_profile` control variable persistence
- Common variables include HOME, SHELL, USER, PWD, TERM, LANG, and DISPLAY
- The `source` command executes scripts in the current shell, preserving variables
- Child processes cannot modify parent process environment
- System-wide variables are set in `/etc/environment` and `/etc/profile`

## Common Mistakes to Avoid

- Forgetting to export variables before expecting them to be available in child processes
- Confusing `~/.bashrc` (interactive non-login) with `~/.bash_profile` (login) configuration
- Using `$VARIABLE` in assignment statements (should be VARIABLE=value, not $VARIABLE=value)
- Modifying PATH incorrectly by replacing instead of appending: use `$PATH:/new/dir`

## Revision Tips

- Practice setting, viewing, and exporting variables in a Linux terminal
- Memorize the purpose of at least 5-6 common environment variables
- Understand the order in which bash reads configuration files
- Write small shell scripts demonstrating variable inheritance between processes
- Remember that PATH modification requires appending $PATH to preserve existing entries
