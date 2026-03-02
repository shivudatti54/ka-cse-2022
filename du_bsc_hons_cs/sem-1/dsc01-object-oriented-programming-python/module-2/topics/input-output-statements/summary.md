# Input-Output Statements in Python - Summary

## Key Definitions and Concepts

- **print()**: Built-in Python function for outputting data to standard output (console). Supports multiple arguments with customizable separators (sep) and endings (end).

- **input()**: Built-in function that reads a string from standard input, optionally displaying a prompt. Always returns string data—requires type conversion for numeric use.

- **F-strings**: Python 3.6+ formatted string literals prefixed with 'f' that embed expressions directly within curly braces: `f"Value: {variable}"`.

- **File I/O**: Operations for reading from/writing to files using open() function with modes: 'r' (read), 'w' (write), 'a' (append), 'b' (binary).

- **with statement**: Context manager that automatically closes files after operations complete, ensuring proper resource cleanup.

## Important Formulas and Techniques

- Type conversion: `int(input())`, `float(input())`, `str(value)`
- String formatting: `f"{value:specifier}"` where specifier includes alignment (`<`, `>`, `^`), width, and precision (`.2f`)
- File handling: `open("filename", "mode")` returning a file object

## Key Points

1. `input()` always returns a string—explicit type casting is mandatory for numeric operations

2. Default `sep` is single space; default `end` is newline character (`\n`)

3. F-strings are preferred over % formatting and format() method for readability and performance

4. File mode 'w' overwrites existing content; 'a' appends without modifying existing data

5. Always close files or use `with` statement to prevent data loss and resource leaks

6. Escape sequences (`\n`, `\t`, `\\`) control output formatting in print statements

7. The `flush` parameter in print() forces immediate output, useful for progress indicators

8. Binary mode ('rb', 'wb') is required for non-text files like images

## Common Mistakes to Avoid

- Forgetting to convert input() to numeric types before performing calculations
- Not closing file handles, leading to data not being written to disk
- Using 'w' mode when intending to preserve existing file content
- Confusing \n (newline) with \t (tab) in output formatting
- Using wrong file path (relative vs absolute) causing FileNotFoundError

## Revision Tips

1. Practice writing programs that accept user input, process it, and display formatted output

2. Memorize common format specifiers: `:d` (integer), `:f` (float), `:.2f` (2 decimal places), `:<15` (left-align width 15)

3. Always use `with` statement for file operations in exam code

4. Review previous years' DU question papers for input/output prediction questions

5. Understand the difference between all file modes before the exam