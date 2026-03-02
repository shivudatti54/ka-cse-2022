# Shell Variables and Environment

## Introduction to Shell Variables

In Unix shell programming, variables are fundamental building blocks used to store data and control script behavior. Shell variables can be categorized into two main types: **local variables** (also called shell variables) and **environment variables**. Understanding the distinction between these types and how they work is crucial for effective shell programming and system administration.

### What are Shell Variables?

A shell variable is a named storage location in memory that can hold data. Variables allow you to:

- Store temporary data for use in scripts
- Control script behavior through configuration values
- Pass information between different parts of a program
- Customize the shell environment

## Types of Variables

### 1. Local Variables (Shell Variables)

Local variables are only available within the current shell instance. They are not inherited by child processes.

**Syntax for setting local variables:**

```bash
variable_name=value
```

**Example:**

```bash
name="John Doe"
count=25
```

### 2. Environment Variables

Environment variables are available to the current shell and all child processes (subshells, commands, and scripts). They form the "environment" in which processes run.

**Syntax for setting environment variables:**

```bash
export VARIABLE_NAME=value
```

**Or:**

```bash
VARIABLE_NAME=value
export VARIABLE_NAME
```

**Example:**

```bash
export PATH="/usr/local/bin:$PATH"
```

## Important Built-in Environment Variables

Unix systems come with several predefined environment variables that control system behavior:

| Variable | Purpose                              | Example Value                  |
| -------- | ------------------------------------ | ------------------------------ |
| `PATH`   | Directories searched for executables | `/usr/bin:/bin:/usr/local/bin` |
| `HOME`   | User's home directory                | `/home/username`               |
| `USER`   | Current username                     | `john`                         |
| `SHELL`  | Current shell                        | `/bin/bash`                    |
| `PWD`    | Present working directory            | `/home/john/documents`         |
| `PS1`    | Primary prompt string                | `\u@\h:\w\$ `                  |
| `TERM`   | Terminal type                        | `xterm-256color`               |
| `LANG`   | Language/locale setting              | `en_US.UTF-8`                  |

## Working with Variables

### Setting and Accessing Variables

**Setting a variable:**

```bash
my_var="Hello World"
```

**Accessing a variable (using $ prefix):**

```bash
echo $my_var
```

**Using curly braces for clarity:**

```bash
echo ${my_var}
```

**Example with string concatenation:**

```bash
filename="report"
extension=".txt"
fullname="${filename}${extension}"
echo $fullname  # Output: report.txt
```

### Variable Scope and Inheritance

```
+-----------------------+
|   Parent Shell        |
|   LOCAL_VAR="local"   |
|   export ENV_VAR="env"|
+-----------------------+
         |
         | forks
         |
+-----------------------+
|   Child Shell         |
|   Can access:         |
|   - ENV_VAR           |
|   Cannot access:      |
|   - LOCAL_VAR         |
+-----------------------+
```

Environment variables are inherited by child processes, while local variables are not. This is a fundamental concept in Unix process management.

### The export Command

The `export` command makes a variable available to child processes. Without export, variables remain local to the current shell.

**Example demonstrating export:**

```bash
# Terminal 1: Set local variable
local_var="local value"

# Terminal 1: Set and export environment variable
export env_var="environment value"

# Terminal 1: Create a script
echo 'echo "Local: $local_var"' > test.sh
echo 'echo "Environment: $env_var"' >> test.sh
chmod +x test.sh

# Terminal 1: Run the script
./test.sh
# Output:
# Local:
# Environment: environment value
```

## Special Variables

Shell provides several special variables with predefined meanings:

| Variable        | Description                                   |
| --------------- | --------------------------------------------- |
| `$0`            | Name of the script                            |
| `$1`, `$2`, ... | Positional parameters                         |
| `$#`            | Number of positional parameters               |
| `$*`            | All positional parameters as a single string  |
| `$@`            | All positional parameters as separate strings |
| `$?`            | Exit status of last command                   |
| `$$`            | Process ID of current shell                   |
| `$!`            | Process ID of last background command         |

**Example using special variables:**

```bash
#!/bin/bash
# script.sh
echo "Script name: $0"
echo "First argument: $1"
echo "Number of arguments: $#"
echo "All arguments: $@"
```

```bash
$ ./script.sh hello world
# Output:
# Script name: ./script.sh
# First argument: hello
# Number of arguments: 2
# All arguments: hello world
```

## Variable Manipulation Techniques

### String Operations

**Length of a string:**

```bash
name="Unix"
echo ${#name}  # Output: 4
```

**Substring extraction:**

```bash
text="Hello World"
echo ${text:6:5}  # Output: World
```

**Pattern matching:**

```bash
filename="document.txt"
echo ${filename%.*}  # Remove shortest .* from end: document
echo ${filename%%.*} # Remove longest .* from end: document
echo ${filename#*.}  # Remove shortest * from start: txt
echo ${filename##*.} # Remove longest * from start: txt
```

### Default Values

**Using default values if variable is unset:**

```bash
echo ${undefined_var:-"default"}  # Output: default
```

**Using default values and assigning if unset:**

```bash
unset my_var
echo ${my_var:="default"}  # Output: default, and sets my_var to "default"
```

## Environment Management Commands

### printenv

Display all environment variables:

```bash
printenv
```

Display specific environment variable:

```bash
printenv HOME
```

### env

Run a command in a modified environment:

```bash
env VAR=value command
```

### set

Display all variables (both local and environment):

```bash
set
```

### unset

Remove a variable:

```bash
unset VARIABLE_NAME
```

## The .bashrc and .profile Files

Shell configuration files allow you to set variables automatically when a shell starts:

- **.profile**: Executed at login for Bourne-compatible shells
- **.bashrc**: Executed for interactive non-login shells in Bash
- **.bash_profile**: Executed at login for Bash

**Example .bashrc snippet:**

```bash
# Custom prompt
PS1='\u@\h:\w\$ '

# Add to PATH
export PATH="$HOME/bin:$PATH"

# Editor preference
export EDITOR=vim

# Aliases
alias ll='ls -la'
```

## Process Environment in C Programming

In C programs, environment variables can be accessed through:

**Using environ variable:**

```c
#include <stdio.h>

extern char **environ;

int main() {
    for (char **env = environ; *env != NULL; env++) {
        printf("%s\n", *env);
    }
    return 0;
}
```

**Using getenv():**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    char *home = getenv("HOME");
    if (home != NULL) {
        printf("Home directory: %s\n", home);
    }
    return 0;
}
```

**Using setenv() and unsetenv():**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    setenv("MY_VAR", "my_value", 1);  // 1 = overwrite if exists
    printf("MY_VAR=%s\n", getenv("MY_VAR"));

    unsetenv("MY_VAR");
    return 0;
}
```

## Best Practices for Using Variables

1. **Use uppercase for environment variables**: `export DATABASE_URL="..."`
2. **Use lowercase for local variables**: `local_var="value"`
3. **Quote variable assignments**: `name="John Smith"` instead of `name=John Smith`
4. **Use curly braces for clarity**: `${variable}` instead of `$variable`
5. **Validate important variables**: Check if critical environment variables are set
6. **Document variable usage**: Comment the purpose of important variables

## Common Pitfalls and Solutions

**Problem: Spaces around equals sign**

```bash
# Wrong:
var = value  # Causes error

# Correct:
var=value
```

**Problem: Forgetting to export**

```bash
# Variable not available in child processes:
MY_VAR=value
./script.sh  # Cannot access MY_VAR

# Solution:
export MY_VAR=value
```

**Problem: Variable expansion in strings**

```bash
name="John"
# Wrong:
echo "Hello $nameDoe"  # Looks for variable 'nameDoe'

# Correct:
echo "Hello ${name}Doe"  # Output: Hello JohnDoe
```

## Exam Tips

1. **Remember the difference**: Local variables vs. environment variables - the key distinction is inheritance by child processes.
2. **Export syntax**: Know both forms: `export VAR=value` and `VAR=value; export VAR`.
3. **Special variables**: Memorize `$0`, `$1`, `$#`, `$?`, `$$` and their purposes.
4. **String operations**: Understand how `${var%pattern}`, `${var#pattern}`, and `${var:-default}` work.
5. **Configuration files**: Know when .profile, .bashrc, and .bash_profile are executed.
6. **C programming**: Understand how to use getenv(), setenv(), and the environ pointer.
7. **Common pitfalls**: Be aware of spacing issues in variable assignment and the need for curly braces in certain contexts.
