# Shell Control Statements

## Introduction to Control Flow in Shell Scripting

Shell scripting is not just about executing commands sequentially. To create powerful and flexible scripts, you need the ability to make decisions, repeat actions, and control the flow of execution based on conditions. This is achieved using **shell control statements**. These statements allow your scripts to behave like real programs, responding dynamically to different inputs and system states.

Control statements in shell programming are broadly categorized into:

1.  **Conditional Statements**: Execute code blocks based on Boolean conditions (e.g., `if`, `case`).
2.  **Looping Statements**: Repeat a code block multiple times (e.g., `for`, `while`, `until`).

---

## Conditional Statements

Conditional statements allow your script to choose between different paths of execution.

### The `if` Statement

The `if` statement is the fundamental building block for decision-making. Its basic syntax is:

```bash
if [ condition ]
then
    # commands to execute if condition is true
fi
```

#### The Test Command `[ ]` and `test`

The square brackets `[ ]` are a shorthand for the `test` command. The space after `[` and before `]` is mandatory. This command evaluates the condition inside it and returns an exit status of 0 (true) or non-zero (false).

**Common File Test Operators:**
| Operator | Description |
| :--- | :--- |
| `-e file` | True if file exists. |
| `-f file` | True if file exists and is a regular file. |
| `-d file` | True if file exists and is a directory. |
| `-r file` | True if file exists and is readable. |
| `-w file` | True if file exists and is writable. |
| `-x file` | True if file exists and is executable. |
| `-s file` | True if file exists and has a size greater than zero. |

**Common String Test Operators:**
| Operator | Description |
| :--- | :--- |
| `-z "$str"` | True if the length of `$str` is zero. |
| `-n "$str"` | True if the length of `$str` is non-zero. |
| `"$str1" = "$str2"` | True if the strings are equal. |
| `"$str1" != "$str2"` | True if the strings are not equal. |

**Common Arithmetic Test Operators:**
| Operator | Description |
| :--- | :--- |
| `$a -eq $b` | True if `a` is equal to `b`. |
| `$a -ne $b` | True if `a` is not equal to `b`. |
| `$a -gt $b` | True if `a` is greater than `b`. |
| `$a -lt $b` | True if `a` is less than `b`. |
| `$a -ge $b` | True if `a` is greater than or equal to `b`. |
| `$a -le $b` | True if `a` is less than or equal to `b`. |

**Example: Checking if a file exists**

```bash
#!/bin/bash
filename="$1"

if [ -f "$filename" ]
then
    echo "File $filename exists."
fi
```

### The `if-else` Statement

The `if-else` structure provides an alternative branch of execution.

```bash
if [ condition ]
then
    # commands if condition is true
else
    # commands if condition is false
fi
```

**Example: Checking if a user is the root user**

```bash
#!/bin/bash
if [ "$(whoami)" = "root" ]
then
    echo "You are root. Be careful."
else
    echo "You are a regular user."
fi
```

### The `if-elif-else` Statement

For checking multiple conditions, use `elif` (else if).

```bash
if [ condition1 ]
then
    # commands if condition1 is true
elif [ condition2 ]
then
    # commands if condition2 is true
else
    # commands if all above conditions are false
fi
```

**Example: Comparing two numbers**

```bash
#!/bin/bash
read -p "Enter first number: " num1
read -p "Enter second number: " num2

if [ "$num1" -gt "$num2" ]
then
    echo "$num1 is greater than $num2"
elif [ "$num1" -lt "$num2" ]
then
    echo "$num1 is less than $num2"
else
    echo "$num1 is equal to $num2"
fi
```

### The `case` Statement

The `case` statement is used for multi-way branching based on the value of a variable. It is often cleaner and more efficient than a long `if-elif-elif-else` chain when comparing against fixed patterns or strings.

```bash
case $variable in
    pattern1)
        # commands if $variable matches pattern1
        ;;
    pattern2)
        # commands if $variable matches pattern2
        ;;
    pattern3|pattern4) # Multiple patterns separated by |
        # commands if $variable matches pattern3 OR pattern4
        ;;
    *) # The default case (matches anything)
        # commands if no pattern matches
        ;;
esac
```

**Example: Basic menu system**

```bash
#!/bin/bash
echo "Select an option: (s)how, (l)ist, (q)uit"
read -r option

case $option in
    s|S)
        echo "Showing files..."
        ls -l
        ;;
    l|L)
        echo "Listing processes..."
        ps aux
        ;;
    q|Q)
        echo "Quitting..."
        exit 0
        ;;
    *)
        echo "Invalid option."
        exit 1
        ;;
esac
```

---

## Looping Statements

Looping statements allow you to execute a block of code repeatedly.

### The `for` Loop

The `for` loop iterates over a list of items.

```bash
for variable in item1 item2 item3 ... itemN
do
    # commands to execute for each item
    # Use $variable to access the current item
done
```

**Example: Iterating over a list of names**

```bash
#!/bin/bash
for name in Alice Bob Charlie
do
    echo "Hello, $name!"
done
```

**Output:**

```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

A very common use is to iterate over all command-line arguments (`$@`).

```bash
#!/bin/bash
for file in "$@"
do
    if [ -f "$file" ]; then
        echo "$file is a valid file."
    else
        echo "$file is not a file."
    fi
done
```

### The `while` Loop

The `while` loop executes as long as the given condition is true.

```bash
while [ condition ]
do
    # commands to execute while condition is true
done
```

**Example: Reading a file line by line**

```bash
#!/bin/bash
while IFS= read -r line
do
    echo "Read: $line"
done < "$1" # Redirect the file into the loop
```

**Example: Countdown timer**

```bash
#!/bin/bash
count=5
while [ $count -gt 0 ]
do
    echo "$count..."
    sleep 1
    count=$((count - 1)) # Arithmetic expansion
done
echo "Blast off!"
```

### The `until` Loop

The `until` loop is the opposite of `while`. It executes as long as the given condition is _false_. It loops _until_ the condition becomes true.

```bash
until [ condition ]
do
    # commands to execute until condition becomes true
done
```

**Example: Wait for a user to log in**

```bash
#!/bin/bash
# This script waits until the user 'john' logs in.
until who | grep -q "john"
do
    echo "john is not logged in yet..."
    sleep 10
done
echo "john has just logged in!"
```

---

## Loop Control: `break` and `continue`

These statements give you finer control within loops.

- `break`: Immediately terminates the loop and transfers control to the line after `done`.
- `continue`: Skips the rest of the commands in the current iteration of the loop and begins the next iteration.

**Example: Using `break` and `continue`**

```bash
#!/bin/bash
for num in {1..10}
do
    if [ $num -eq 3 ]
    then
        continue # Skip the rest for number 3
    fi
    if [ $num -eq 8 ]
    then
        break # Exit the loop entirely at number 8
    fi
    echo "Number: $num"
done
echo "Loop finished."
```

**Output:**

```
Number: 1
Number: 2
        # Number 3 is skipped
Number: 4
Number: 5
Number: 6
Number: 7
        # Loop breaks before 8
Loop finished.
```

---

## Putting It All Together: A Practical Example

Let's create a script that backs up files from a source directory to a target directory, but only if they are newer than the existing backup or don't exist in the backup.

```bash
#!/bin/bash
# Simple incremental backup script
# Usage: ./backup.sh /path/to/source /path/to/backup

SOURCE_DIR="$1"
BACKUP_DIR="$2"

# Check if arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_dir> <backup_dir>" >&2
    exit 1
fi

# Check if source is a valid directory
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist." >&2
    exit 1
fi

# Create backup directory if it doesn't exist
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Created backup directory: $BACKUP_DIR"
fi

# Iterate through all files in the source directory
for file in "$SOURCE_DIR"/*
do
    if [ -f "$file" ]; then # Check if it's a regular file
        filename=$(basename "$file")
        backup_file="$BACKUP_DIR/$filename"

        # Copy file if it doesn't exist in backup or is newer
        if [ ! -f "$backup_file" ] || [ "$file" -nt "$backup_file" ]
        then
            cp -v "$file" "$BACKUP_DIR"
            echo "Copied: $filename"
        else
            echo "Skipped: $filename (already up-to-date)"
        fi
    fi
done

echo "Backup process completed."
```

This script combines:

1.  Checking arguments (`if`)
2.  Checking file and directory attributes (`-d`, `-f`, `-nt`)
3.  Iterating through a list of files (`for`)
4.  Making decisions on whether to copy (`if-else`)

---

## Exam Tips

1.  **Spacing is Crucial**: Remember the spaces in `[ $a -eq $b ]`. Writing `[$a -eq $b]` is a syntax error.
2.  **Quote Your Variables**: Always use double quotes around variables, especially in `[ ]` tests (e.g., `[ -f "$file" ]`). This prevents word splitting and errors with filenames containing spaces.
3.  **Use the Right Operator**: Don't confuse string comparison (`=`, `!=`) with arithmetic comparison (`-eq`, `-ne`). Using `=` for numbers might work but is not correct.
4.  **`case` Terminators**: Every block in a `case` statement must end with `;;`. The final `esac` is `case` spelled backwards.
5.  **Exit Status is Key**: Understand that `if` and loops check the _exit status_ of the command. `[ ]` is just a command that returns 0 (success) or 1 (failure). You can use any command, like `if grep -q "pattern" file.txt; then ...`.
6.  **`while read` Loop**: The pattern `while IFS= read -r line` is idiomatic for reading a file line by line. `IFS=` prevents leading/trailing whitespace trim, and `-r` prevents backslash interpretation.
7.  **Arithmetic in Loops**: Use `$(( ))` for arithmetic operations inside loops, e.g., `count=$((count + 1))`.
