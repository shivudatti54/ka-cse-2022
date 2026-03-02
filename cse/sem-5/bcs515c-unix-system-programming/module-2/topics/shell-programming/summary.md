# Shell Programming - Summary

## Key Definitions and Concepts

- **Shell**: A command interpreter and programming language that provides interface to Unix/Linux kernel
- **Shell Script**: A text file containing a sequence of commands executed by the shell interpreter
- **Bash (Bourne Again Shell)**: Most widely used Linux shell, superset of Bourne Shell with enhanced features
- **Variable**: A named storage location containing data that can be accessed using $ prefix
- **Special Variables**: Predefined variables including $0 (script name), $1-$n (arguments), $? (exit status), $$ (PID)
- **Command Substitution**: Capturing command output as values using $(command) or backticks
- **Exit Status**: Numeric value returned by commands; 0 indicates success, non-zero indicates failure

## Important Formulas and Theorems

- **File Test Operators**: `-f` (file), `-d` (directory), `-r/w/x` (permissions), `-s` (size > 0), `-z` (empty)
- **String Operators**: `=` (equals), `!=` (not equals), `-z` (null), `-n` (non-null)
- **Numeric Operators**: `-eq` (equal), `-ne` (not equal), `-lt` (<), `-le` (<=), `-gt` (>), `-ge` (>=)
- **Arithmetic Expansion**: `$((expression))` for calculations like `$((a + b))`, `$((a * b))`
- **Array Access**: `${array[index]}`, `${array[@]}` for all elements, `${#array[@]}` for length

## Key Points

- Shell scripts must begin with shebang (#!/bin/bash) to specify the interpreter
- Always use spaces in conditional tests: `[ $a = $b ]` not `[$a=$b]`
- Quote variables to handle spaces: `"$var"` not `$var`
- Use `local` keyword in functions to restrict variable scope
- The `fi` keyword closes if statements, `esac` closes case statements
- Command exit status available via `$?` immediately after command execution
- For loops iterate over lists, while loops iterate based on conditions
- Pipes (|) connect commands, redirectors (>, >>, <) handle file I/O
- Use `chmod +x script.sh` to make scripts executable

## Common Mistakes to Avoid

1. **Missing spaces in brackets**: Writing `[$a=$b]` instead of `[ $a = $b ]` causes syntax errors
2. **Unquoted variables**: Variables with spaces break when not quoted, e.g., `$var` vs `"$var"`
3. **Using = for numbers**: String comparison operator `=` fails for numeric comparison; use `-eq`
4. **Forgetting fi/esac**: Incomplete conditional blocks cause parser errors
5. **Wrong exit codes**: Returning 1 for success or 0 for failure confuses calling programs

## Revision Tips

1. Practice writing at least 3-4 complete scripts covering variables, conditions, loops, and functions
2. Memorize test operators (file, string, numeric) as they form the basis of conditionals
3. Understand the difference between `$*` and `$@` for argument handling
4. Use `bash -x` to debug scripts and trace execution flow
5. Review previous question papers to understand the pattern and frequently asked concepts
6. Focus on command substitution and I/O redirection as they are commonly tested
