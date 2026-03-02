# Combining Commands - Meaning of Internal and External Commands - Summary

## Key Definitions and Concepts

- **Internal Commands (Built-in Commands):** Commands implemented within the shell itself, executed directly without creating a new process. Examples: cd, pwd, echo, export, read, alias, set, exit, source.

- **External Commands:** Standalone executable programs stored in the file system (in directories like /bin, /usr/bin) that require the shell to create a new process via fork-exec. Examples: ls, cp, mv, grep, cat, chmod.

- **Command Combination:** The process of chaining multiple commands to perform complex operations using operators like |, ;, &&, ||.

- **Piping (|):** Connects output of one command as input to another command.

- **Redirection:** Controls command input/output sources using >, >>, <, 2>, &>.

## Important Formulas and Theorems

- **Fork-Exec Process:** For external commands → fork() → exec() → wait() → exit status
- **Exit Status Convention:** 0 = success, non-zero = failure
- **AND Operator:** command1 && command2 → command2 executes only if command1 returns 0
- **OR Operator:** command1 || command2 → command2 executes only if command1 returns non-zero
- **Sequential Execution:** command1 ; command2 → always executes regardless of status

## Key Points

1. Internal commands execute within the shell's process; external commands create new child processes.

2. Internal commands are faster due to no process creation overhead.

3. The `type` command distinguishes between internal and external commands.

4. Piping creates a data stream between commands without temporary files.

5. The shell searches PATH directories to locate external command executables.

6. Command substitution using $(command) allows embedding command output as arguments.

7. Redirection operators control stdin, stdout, and stderr separately.

8. Compound commands can be built by combining multiple operators in a single expression.

## Common Mistakes to Avoid

- Confusing internal with external commands in exam questions (cd is internal, ls is external)
- Forgetting that && and || have short-circuit evaluation behavior
- Using > instead of >> when appending to files (which overwrites content)
- Not understanding that redirection operators have different precedence than logical operators

## Revision Tips

1. Practice identifying command types using the `type` command on common Unix/Linux commands.

2. Create small shell scripts combining multiple commands to reinforce pipeline concepts.

3. Remember the fork-exec sequence for external command execution.

4. Memorize 8-10 commonly used internal and external commands for quick identification.

5. Review exit status conventions and how they affect && and || operator behavior.
