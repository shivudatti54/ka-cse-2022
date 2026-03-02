# Shell Programming

## Introduction

Shell programming is a fundamental aspect of Unix and Linux systems that enables users to automate tasks, write scripts, and interact with the operating system at a higher level of abstraction. A shell is both a command interpreter and a programming language that provides interfaces to access operating system services. In the context of 's Operating Systems curriculum, shell programming forms an essential component that bridges the gap between command-line usage and system administration.

The shell acts as an intermediary between the user and the kernel, interpreting commands and executing them. Beyond simple command execution, modern shells support powerful scripting capabilities that allow programmers to write complex programs called shell scripts. These scripts can contain variables, control structures, functions, and I/O operations, making them comparable to high-level programming languages in terms of functionality. Popular shells in Unix/Linux environments include Bash (Bourne Again Shell), sh (Bourne Shell), csh (C Shell), and ksh (Korn Shell), with Bash being the most widely used in modern Linux distributions.

Understanding shell programming is crucial for system administrators, software developers, and IT professionals as it enables task automation, file processing, system monitoring, and software deployment. In examinations, this topic carries significant weightage with questions covering shell scripting constructs, command substitution, and practical script development.

## Key Concepts

### Types of Shells

There are several types of shells available in Unix/Linux systems, each with distinct features and syntax:

**Bourne Shell (sh)**: The original Unix shell written by Stephen Bourne. It provides basic functionality including input/output redirection, piping, variables, and control structures. Scripts written for sh are highly portable across different Unix systems.

**Bash (Bourne Again Shell)**: The default shell on most Linux distributions and macOS. It is a superset of the Bourne Shell with additional features like command history, tab completion, array support, and enhanced job control. Bash is backward compatible with sh.

**C Shell (csh)**: Designed with C-language-like syntax, making it familiar to programmers. It includes features like history substitution, aliases, and job control, though it is less commonly used for scripting today.

**Korn Shell (ksh)**: A commercial shell that combines features of both sh and csh. It offers better performance than Bash and includes advanced features like associative arrays and floating-point arithmetic.

### Shell Variables

Shell variables are used to store data that can be referenced and manipulated within scripts. Variables in shell programming are untyped by default and are treated as strings.

**Variable Declaration and Assignment**: Variables are assigned using the equals sign without spaces around the operator. For example: `NAME="John Doe"` and `AGE=25`.

**Accessing Variables**: Variables are accessed by prefixing the name with a dollar sign ($). For instance, `echo $NAME` displays the value of NAME.

**System Variables**: These are predefined variables set by the shell, including:

- `$HOME`: Current user's home directory
- `$PATH`: Directories searched for commands
- `$PWD`: Current working directory
- `$USER`: Current username
- `$SHELL`: Default shell
- `$?`: Exit status of the last command

**Environment Variables**: Variables that affect how processes run. The `export` command makes variables available to child processes.

### Special Variables

Shell programming includes special variables with predefined meanings:

- `$0`: Script name
- `$1, $2, ... $n`: Positional parameters (arguments passed to script)
- `$#`: Number of arguments
- `$*`: All arguments as a single string
- `$@`: All arguments as separate strings
- `$$`: Process ID of current script
- `$?`: Exit status of last executed command (0 for success, non-zero for failure)

### Control Structures

**If-Else Statement**: The basic conditional structure in shell programming:

```bash
if [ condition ]
then
 statements
elif [ condition ]
then
 statements
else
 statements
fi
```

Note the spaces around square brackets and the use of `fi` to close the if block.

**Case Statement**: Used for multi-way branching based on pattern matching:

```bash
case variable in
 pattern1)
 commands;;
 pattern2)
 commands;;
 *)
 default commands;;
esac
```

**Loops**: Shell supports three types of loops:

_For Loop_ - iterates over a list:

```bash
for var in list
do
 commands
done
```

_While Loop_ - executes while condition is true:

```bash
while [ condition ]
do
 commands
done
```

_Until Loop_ - executes until condition becomes true:

```bash
until [ condition ]
do
 commands
done
```

### Command Substitution

Command substitution allows capturing the output of a command as a value. Two syntaxes are supported:

- Backticks: `result=`ls -l``
- Dollar parentheses: `result=$(ls -l)`

Command substitution is frequently used to store command outputs in variables for further processing.

### Input/Output Redirection

Shell provides powerful I/O redirection capabilities:

- `>`: Redirect output to file (overwrite)
- `>>`: Redirect output to file (append)
- `<`: Redirect input from file
- `2>`: Redirect error output
- `&>`: Redirect both standard output and error

The pipe operator (`|`) connects the output of one command as input to another, enabling command chaining.

### Functions

Functions in shell programming allow code reusability and modularity:

```bash
function_name() {
 local var1=$1
 local var2=$2
 commands
 return value
}
```

The `local` keyword restricts variable scope to the function. Parameters are accessed using `$1, $2, etc.`

### Arithmetic Operations

Shell supports arithmetic operations using various methods:

- `expr`: External command for arithmetic
- `$((expression))`: Arithmetic expansion (most common)
- `let`: Built-in command for arithmetic

Examples: `result=$((a + b))`, `result=$((a * b))`

### Arrays

Bash supports one-dimensional arrays:

```bash
array=(value1 value2 value3)
echo ${array[0]} # First element
echo ${array[@]} # All elements
echo ${#array[@]} # Array length
```

## Examples

### Example 1: User Information Script

**Problem**: Write a shell script that accepts a username and displays whether the user exists in the system.

```bash
#!/bin/bash
# Script to check user existence

echo "Enter username:"
read username

if [ -z "$username" ]
then
 echo "Error: Please enter a username"
 exit 1
fi

if grep -q "^$username:" /etc/passwd
then
 echo "User '$username' exists in the system"
 echo "User details:"
 grep "^$username:" /etc/passwd
else
 echo "User '$username' does not exist"
 exit 1
fi
```

**Step-by-step solution**:

1. First, the script prompts for username input using `read`
2. The `-z` flag checks if the input string is empty
3. `grep -q` searches the /etc/passwd file quietly (no output)
4. If found, user details are displayed using grep
5. Exit codes indicate success (0) or failure (1)

**To execute**: Save as `checkuser.sh`, make executable with `chmod +x checkuser.sh`, run with `./checkuser.sh`

### Example 2: Grade Calculator

**Problem**: Write a script that accepts marks and displays the corresponding grade using case statement.

```bash
#!/bin/bash
# Script to calculate grade based on marks

echo "Enter marks (0-100):"
read marks

if [ $marks -lt 0 ] || [ $marks -gt 100 ]
then
 echo "Invalid marks. Enter between 0 and 100"
 exit 1
fi

case $marks in
 90|91|92|93|94|95|96|97|98|99|100)
 echo "Grade: S (Outstanding)";;
 80|81|82|83|84|85|86|87|88|89)
 echo "Grade: A (Excellent)";;
 70|71|72|73|74|75|76|77|78|79)
 echo "Grade: B (Very Good)";;
 60|61|62|63|64|65|66|67|68|69)
 echo "Grade: C (Good)";;
 50|51|52|53|54|55|56|57|58|59)
 echo "Grade: D (Pass)";;
 *)
 echo "Grade: F (Fail)";;
esac
```

**Step-by-step solution**:

1. Input validation ensures marks are within valid range (0-100)
2. The case statement uses pattern matching with pipe for multiple values
3. Each range maps to corresponding grade
4. The default case (\*) handles failing grades

### Example 3: File Operations with Loop

**Problem**: Write a script to display all files in a directory with their sizes in human-readable format.

```bash
#!/bin/bash
# Script to list files with sizes

echo "Files in current directory:"
echo "---------------------------"

count=0
total_size=0

for file in *
do
 if [ -f "$file" ]
 then
 size=$(stat -c%s "$file" 2>/dev/null)
 total_size=$((total_size + size))
 count=$((count + 1))
 echo "$file - $size bytes"
 fi
done

echo "---------------------------"
echo "Total files: $count"
echo "Total size: $total_size bytes"
```

**Step-by-step solution**:

1. The `*` wildcard matches all files in current directory
2. `-f` test checks if the item is a regular file
3. `stat -c%s` gets file size in bytes
4. Error output is redirected to `/dev/null`
5. Counters track total files and cumulative size
6. Arithmetic expansion `$(())` performs calculations

## Exam Tips

1. **Syntax Accuracy**: Remember that shell scripting is syntax-sensitive. Always include spaces in conditional tests: `[ $a = $b ]` not `[$a=$b]`. Missing spaces cause syntax errors.

2. **Understand Special Variables**: Questions frequently ask about `$?`, `$$`, `$#`, `$*`, and `$@`. Remember `$?` gives exit status of the previous command (0 for success).

3. **Exit Status Meaning**: A command returning 0 indicates success, while non-zero (typically 1) indicates failure. This is opposite to some programming languages.

4. **Test Operators**: Memorize file test operators: `-f` (regular file), `-d` (directory), `-r/w/x` (permissions), `-s` (non-empty file), `-z` (empty string).

5. **String Comparison**: Use `=` or `==` for string equality in Bash, and `-eq`, `-lt`, `-gt` for numeric comparisons. Don't interchange them.

6. **Quoting Rules**: Always quote variables containing spaces: `"$var"` not `$var`. Double quotes allow variable expansion, single quotes treat everything literally.

7. **Loop Constructs**: Know when to use each loop type—for loops iterate over lists, while loops continue while condition holds, until loops continue until condition becomes true.

8. **Debugging Scripts**: Use `bash -x script.sh` for debug mode that shows each command before execution. This helps identify errors in logic.

9. **Command Substitution**: Prefer `$(command)` over backticks for better readability and nested command support.

10. **Practice Common Patterns**: File existence checks, argument processing, arithmetic operations, and string manipulations are frequently asked in exams.
