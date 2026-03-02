# Exit Status and Exit Command - Summary

## Key Definitions and Concepts

- **Exit Status**: A numerical code (0-255) returned by a process to its parent indicating completion status
- **Exit Command**: A shell builtin that terminates the current shell script and returns an exit status
- **$?**: A special shell variable that stores the exit status of the most recently executed command

## Important Formulas and Theorems

- `exit [n]` - Terminates script with status n (0-255); if n is omitted, uses last command's status
- Exit status is modulo 256: values outside 0-255 wrap around
- Standard codes: 0=success, 1=general error, 2=misuse, 126=not executable, 127=not found

## Key Points

- Exit status 0 always indicates successful execution; non-zero indicates failure
- The `$?` variable holds exit status but is overwritten by the next command
- Use `>&2` to redirect error messages to standard error
- The `trap` command ensures cleanup code runs on any script termination
- Functions should use `return` for status, not `exit` (unless terminating entire script)
- Exit codes 126-128 have specific Unix system meanings beyond user-defined errors

## Common Mistakes to Avoid

- Forgetting that `$?` is overwritten immediately - capture it before running another command
- Using exit inside a sourced script without realizing it terminates the sourcing shell
- Not distinguishing between function returns and script exit statements
- Forgetting that exit codes greater than 255 are reduced modulo 256

## Revision Tips

- Practice writing scripts with proper error handling using exit codes
- Remember the standard exit code meanings as they frequently appear in exams
- Review the relationship between trap, EXIT signal, and script termination
- Understand how parent scripts can use child script exit statuses for decision making
