# **Three Standard Files and Redirection**

## **Introduction**

Redirection is a fundamental concept in UNIX system programming that allows you to manipulate input/output streams. The three standard files are:

- **Standard Input (STDIN)**: File descriptor 0 (0<>) - reads from the keyboard or a file.
- **Standard Output (STDOUT)**: File descriptor 1 (1>) - writes to the screen or a file.
- **Standard Error (STDERR)**: File descriptor 2 (2>) - writes error messages to the screen or a file.

## **Redirection Operators**

- **Greater-than (>)**: Redirects STDOUT to a file.
- **Less-than (<)**: Redirects STDIN from a file.
- **Double greater-than (>>)**: Appends to STDOUT.
- **Double less-than (<<)**: Prepends to STDIN.

## **Example Formulas and Theorems**

- `file redirection` = `old file descriptor` ` operator` `new file descriptor`
- `file redirection` = `old file` ` operator` `new file`

**Theorems**

- The `>>` operator will append to the end of the file, while `<` will overwrite the file.
- The `>&` operator can redirect both STDOUT and STDERR to the same file.

## **Revision Points**

- The three standard files are STDIN, STDOUT, and STDERR.
- The redirection operators are >, <, >>, and <<.
- The >> operator appends to STDOUT, while < overwrites the file.
- The `>&` operator can redirect both STDOUT and STDERR to the same file.
