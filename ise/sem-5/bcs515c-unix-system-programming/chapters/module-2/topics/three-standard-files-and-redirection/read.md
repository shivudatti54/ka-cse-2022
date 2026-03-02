# **Three Standard Files and Redirection**

## **Introduction**

In UNIX system programming, the three standard files, also known as the "special files" or "character devices," are used to redirect input/output operations. These files are:

- Standard Input (stdin)
- Standard Output (stdout)
- Standard Error (stderr)

Understanding how to use these files and redirection is crucial for effective programming in UNIX.

## **Standard Input (stdin)**

- Also known as the keyboard
- Used to receive input from the user
- File descriptor 0
- Can be redirected using the `<` symbol

**Example:**

```bash
echo "Hello, World!" > filename.txt
```

In this example, the output of the `echo` command is redirected to a file named `filename.txt`.

## **Standard Output (stdout)**

- Also known as the screen
- Used to display output to the user
- File descriptor 1
- Can be redirected using the `>` symbol

**Example:**

```bash
echo "Hello, World!" > filename.txt
```

In this example, the output of the `echo` command is displayed on the screen.

## **Standard Error (stderr)**

- Also known as the error message
- Used to display error messages
- File descriptor 2
- Can be redirected using the `2>` symbol

**Example:**

```bash
ls non-existent-file > filename.txt 2> error.txt
```

In this example, the output of the `ls` command is displayed on the screen, and any error messages are redirected to a file named `error.txt`.

## **Redirection Operators**

| Operator | Description     | Syntax                                |
| -------- | --------------- | ------------------------------------- |
| `<`      | Redirect input  | `input_file < filename.txt`           |
| `>`      | Redirect output | `echo "Hello, World!" > filename.txt` |
| `2>`     | Redirect error  | `ls non-existent-file 2> error.txt`   |

## **Pipe (|)**

- Used to redirect the output of one command as the input to another command
- Syntax: `command1 | command2`

**Example:**

```bash
ls -l | grep keyword
```

In this example, the output of the `ls -l` command is piped to the `grep` command, which searches for the keyword in the output.

## **Both Output and Input Redirection**

- Can be used together to redirect both output and input
- Syntax: `command < input_file > output_file`

**Example:**

```bash
cat input_file > output_file
```

In this example, the input from the `input_file` is redirected to the `output_file`.
