# **Three Standard Files and Redirection**

## **Introduction**

In UNIX system programming, three standard files and redirection are essential concepts that help you interact with files and execute commands efficiently. Understanding these concepts will enable you to write effective shell scripts and automate tasks.

## **Three Standard Files**

### 1. Standard Input (stdin)

- The standard input (stdin) is the file descriptor for the keyboard.
- It is designated by the file descriptor 0.
- Data is sent to the standard input when a user types commands or input data.

```bash
# Reading from standard input
echo "Enter your name:"
read name
echo "Hello, $name!"
```

### 2. Standard Output (stdout)

- The standard output (stdout) is the file descriptor for the display.
- It is designated by the file descriptor 1.
- Data is sent to the standard output when a command is executed.

```bash
# Writing to standard output
echo "Hello, World!"
```

### 3. Standard Error (stderr)

- The standard error (stderr) is the file descriptor for any error messages.
- It is designated by the file descriptor 2.
- Data is sent to the standard error when a command encounters errors.

```bash
# Writing to standard error
echo "Invalid input" >&2
```

## **Redirection**

Redirection is a powerful feature in UNIX that allows you to control the flow of data between files, commands, and the standard input/output streams.

### 1. Redirecting Input

Redirecting input with the `<` symbol:

```bash
# Redirecting input from a file
cat file.txt
```

### 2. Redirecting Output

Redirecting output with the `>` symbol:

```bash
# Redirecting output to a file
echo "Hello, World!" > hello.txt
```

### 3. Appending to a File

Redirecting output with the `>>` symbol:

```bash
# Appending to a file
echo "Hello, World!" >> hello.txt
```

### 4. Redirecting Both Input and Output

Redirecting both input and output with the `>>` symbol:

```bash
# Redirecting both input and output to a file
cat file.txt >> hello.txt
```

### 5. Using Redirectors

Using the `>` and `>>` symbols for redirection:

```bash
# Using the > symbol for overwriting
echo "Hello, World!" > hello.txt

# Using the >> symbol for appending
echo "Hello, World!" >> hello.txt
```

### 6. Redirecting Error Messages

Redirecting error messages with the `2>` symbol:

```bash
# Redirecting error messages to a file
ls -l 2> error.log
```

## **Best Practices**

- Use the `>` symbol to overwrite existing files.
- Use the `>>` symbol to append to existing files.
- Use the `<` symbol to redirect input from files.
- Use the `2>` symbol to redirect error messages to files.

## **Conclusion**

In this study material, we have covered the three standard files and redirection in UNIX system programming. Understanding these concepts is essential for writing effective shell scripts and automating tasks. Remember to use the correct redirection symbols and file descriptors to control the flow of data between files, commands, and the standard input/output streams.
