# Environment Variables and List Command - Summary

## Key Definitions and Concepts

- **Environment Variables**: Named values that store configuration information, inherited by all child processes from parent processes
- **Shell Variables**: Local variables confined to the current shell session, not inherited by child processes
- **export command**: Used to convert shell variables into environment variables
- **PATH**: System-defined variable containing colon-separated directories searched for executable files

## Important Formulas and Techniques

- **Setting temporary variable**: `VAR_NAME=value command` (applies only to the command)
- **Setting persistent variable**: Add `export VAR_NAME=value` to `.bashrc` or `.profile`
- **Viewing all variables**: `env` or `printenv`
- **Viewing specific variable**: `printenv VARIABLE_NAME`
- **Removing variable**: `unset VARIABLE_NAME`
- **Clean environment execution**: `env -i command` (starts with no inherited variables)

## Key Points

1. Environment variables control system behavior, user preferences, and application configurations

2. The `env` command displays all current environment variables when used without arguments

3. PATH variable determines where the shell searches for executable commands

4. Child processes inherit a copy of parent environment but cannot modify parent's environment

5. The `-i` flag with `env` creates an empty environment, useful for testing and security

6. Variables like HOME, USER, SHELL, PWD, TERM are automatically set at login

7. Shebang `#!/usr/bin/env` provides portability for finding interpreters across systems

8. Environment variables set in terminal are session-specific; add to shell config files for persistence

## Common Mistakes to Avoid

1. Confusing shell variables with environment variables - remember to use `export`

2. Forgetting that PATH uses colons (:), not semicolons, to separate directories

3. Assuming changes to environment variables in child processes affect the parent

4. Not understanding that variable assignments before commands only affect that specific command

5. Modifying PATH without backing up the original value first

## Revision Tips

1. Practice setting, viewing, and unsetting environment variables in a Linux terminal

2. Check your own system's environment using `env` and identify common variables

3. Understand the order of precedence when multiple directories in PATH contain executables with the same name

4. Review shell configuration files to see how persistent environment variables are set
