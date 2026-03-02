# Shell Scripts and Functions

## Introduction to Shell Programming

Shell programming is the process of writing scripts using Unix shell commands to automate tasks and create powerful utilities. A shell script is essentially a program that contains a series of commands that the shell can execute. These scripts combine the power of Unix commands with programming constructs like variables, control statements, and functions.

### What is a Shell Script?

A shell script is a text file containing:

- Unix/Linux commands
- Programming constructs (loops, conditionals)
- Comments (lines starting with #)
- Shebang line (#!/bin/bash) to specify the interpreter

**Example of a simple shell script:**

```bash
#!/bin/bash
# This is a comment
echo "Hello, World!"
```

## Shell Variables

Variables in shell scripting are used to store data that can be referenced and manipulated throughout the script.

### Types of Variables

1. **System Variables**: Predefined by the system (e.g., $HOME, $PATH, $USER)
2. **User-defined Variables**: Created by the user

**Variable naming rules:**

- Variable names can contain letters, numbers, and underscores
- Cannot start with a number
- Case-sensitive

**Example:**

```bash
#!/bin/bash
name="John Doe"
age=30
echo "Name: $name, Age: $age"
```

## Command Line Arguments

Shell scripts can accept arguments when executed. These arguments are accessible through special variables:

| Variable     | Description                     |
| ------------ | ------------------------------- |
| `$0`         | Name of the script              |
| `$1` to `$9` | First 9 arguments               |
| `$#`         | Number of arguments             |
| `$@`         | All arguments as separate words |
| `$*`         | All arguments as a single word  |

**Example:**

```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Total arguments: $#"
echo "All arguments: $@"
```

## Positional Parameters

Positional parameters are the arguments passed to a script or function. They can be manipulated using various techniques:

**Shifting parameters:**

```bash
#!/bin/bash
echo "First argument: $1"
shift  # Shift arguments by one position
echo "After shift, first argument: $1"
```

**Using all parameters:**

```bash
#!/bin/bash
for param in "$@"
do
    echo "Parameter: $param"
done
```

## Control Statements

### Conditional Statements

**if-then-else:**

```bash
#!/bin/bash
if [ "$1" -gt 10 ]
then
    echo "$1 is greater than 10"
elif [ "$1" -eq 10 ]
then
    echo "$1 is equal to 10"
else
    echo "$1 is less than 10"
fi
```

**case statement:**

```bash
#!/bin/bash
case $1 in
    "start")
        echo "Starting service..."
        ;;
    "stop")
        echo "Stopping service..."
        ;;
    "restart")
        echo "Restarting service..."
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        ;;
esac
```

### Looping Statements

**for loop:**

```bash
#!/bin/bash
for i in 1 2 3 4 5
do
    echo "Number: $i"
done

# Using sequence
for i in {1..5}
do
    echo "Number: $i"
done

# C-style for loop
for ((i=1; i<=5; i++))
do
    echo "Number: $i"
done
```

**while loop:**

```bash
#!/bin/bash
count=1
while [ $count -le 5 ]
do
    echo "Count: $count"
    count=$((count + 1))
done
```

**until loop:**

```bash
#!/bin/bash
count=1
until [ $count -gt 5 ]
do
    echo "Count: $count"
    count=$((count + 1))
done
```

## Shell Functions

Functions allow you to group commands together and reuse them throughout your script.

### Function Syntax

**Basic function:**

```bash
function_name() {
    # Commands
    return value
}
```

**Example:**

```bash
#!/bin/bash

# Define function
greet() {
    echo "Hello, $1!"
    return 0
}

# Call function
greet "Alice"
greet "Bob"

# Capture return value
greet "Charlie"
echo "Return value: $?"
```

### Function Parameters

Functions can accept parameters just like scripts:

```bash
#!/bin/bash

calculate_sum() {
    local result=$(( $1 + $2 ))
    echo $result
    return 0
}

sum=$(calculate_sum 5 3)
echo "Sum: $sum"
```

### Variable Scope

- **Global variables**: Accessible throughout the script
- **Local variables**: Accessible only within the function (declared with `local` keyword)

```bash
#!/bin/bash

global_var="I'm global"

my_function() {
    local local_var="I'm local"
    echo "Inside function: $global_var"
    echo "Inside function: $local_var"
}

my_function
echo "Outside function: $global_var"
echo "Outside function: $local_var"  # This will be empty
```

## The Here Document

The here document (<<) allows you to redirect multiple lines of input to a command.

**Syntax:**

```bash
command << DELIMITER
input lines
DELIMITER
```

**Example:**

```bash
#!/bin/bash

cat << EOF
This is a multi-line
text block that will be
displayed as output.
EOF

# Using with variables
name="John"
cat << END
Hello $name,
This is a custom message
generated on $(date)
END
```

## The trap Command

The trap command allows you to specify actions to be taken when signals are received.

**Common signals:**

- SIGINT (2): Interrupt from keyboard (Ctrl+C)
- SIGTERM (15): Termination signal
- SIGKILL (9): Kill signal (cannot be trapped)

**Example:**

```bash
#!/bin/bash

cleanup() {
    echo "Cleaning up temporary files..."
    rm -f /tmp/tempfile*
    exit 1
}

# Set trap for SIGINT (Ctrl+C)
trap cleanup SIGINT

echo "Press Ctrl+C to test the trap"
sleep 10
```

## Advanced Scripting Techniques

### Error Handling

**Using set -e:**

```bash
#!/bin/bash
set -e  # Exit immediately if a command exits with non-zero status

# This script will exit if any command fails
command_that_might_fail
another_command
```

**Using set -u:**

```bash
#!/bin/bash
set -u  # Treat unset variables as an error

# This will cause an error if $undefined_var is not set
echo $undefined_var
```

### Debugging Scripts

**Using set -x:**

```bash
#!/bin/bash
set -x  # Print commands and their arguments as they are executed

# Debugging output will be shown
variable="test"
echo $variable
set +x  # Turn off debugging
```

### Process Substitution

```bash
#!/bin/bash
# Compare two files
diff <(sort file1.txt) <(sort file2.txt)
```

## Practical Examples

### File Backup Script

```bash
#!/bin/bash

backup_files() {
    local source_dir=$1
    local backup_dir=$2

    if [ ! -d "$source_dir" ]; then
        echo "Error: Source directory doesn't exist"
        return 1
    fi

    mkdir -p "$backup_dir"
    cp -r "$source_dir"/* "$backup_dir"/
    echo "Backup completed from $source_dir to $backup_dir"
    return 0
}

backup_files "/home/user/documents" "/backup/documents_$(date +%Y%m%d)"
```

### System Monitoring Script

```bash
#!/bin/bash

monitor_system() {
    echo "=== System Monitoring Report ==="
    echo "Date: $(date)"
    echo "Uptime: $(uptime)"
    echo "Memory Usage:"
    free -h
    echo "Disk Usage:"
    df -h
}

# Run monitoring every 5 minutes
while true; do
    monitor_system >> /var/log/system_monitor.log
    sleep 300
done
```

## Exam Tips

1. **Remember special variables**: $0, $1-$9, $#, $@, $\* are frequently tested
2. **Understand variable scope**: Global vs local variables in functions
3. **Practice control structures**: if-else, case, for, while loops are essential
4. **Learn function syntax**: Both traditional and modern function definitions
5. **Master here documents**: Understand the << syntax and its practical uses
6. **Know trap commands**: Understand how to handle signals in scripts
7. **Debug effectively**: Use set -x, set -e, and set -u for debugging
8. **Test edge cases**: Always test scripts with empty arguments, special characters
9. **Use proper quoting**: Understand when to use single vs double quotes
10. **Practice error handling**: Implement robust error checking in your scripts
