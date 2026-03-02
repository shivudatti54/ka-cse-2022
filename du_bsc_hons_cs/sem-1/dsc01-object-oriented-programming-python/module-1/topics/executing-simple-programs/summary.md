# Executing Simple Programs in Python - Summary

## Key Definitions and Concepts

- **Python Interpreter**: The program that reads and executes Python source code, converting it to bytecode for the Python Virtual Machine (PVM).

- **Interactive Mode**: Running Python commands directly in the shell for immediate execution and experimentation.

- **Script Mode**: Writing Python code in a .py file and executing it as a complete program.

- **Dynamic Typing**: Python's feature where variable types are determined at runtime based on assigned values.

- **F-string**: A formatted string literal (prefixed with 'f') that allows embedding expressions inside curly braces.

## Important Formulas and Theorems

- Temperature Conversion: `F = (C × 9/5) + 32` and `C = (F - 32) × 5/9`

- Average Calculation: `average = sum(marks) / len(marks)`

- String Formatting: `f"{variable}"` for f-strings, `"{}.format()"` for format method

## Key Points

- Python uses indentation (4 spaces) to define code blocks, unlike curly braces in other languages.

- The `input()` function always returns a string; use `int()` or `float()` for numeric operations.

- The `if __name__ == "__main__":` pattern allows a file to be both a module and an executable script.

- Common data types: int, float, str, bool—use `type()` to check a variable's type.

- f-strings (Python 3.6+) are the modern, preferred method for string formatting.

- Always validate user input, especially when converting strings to numbers.

- Python executes code sequentially from top to bottom unless control structures redirect flow.

## Common Mistakes to Avoid

- Forgetting to convert input() string to int/float before arithmetic operations, leading to unexpected string concatenation.

- Using tabs instead of spaces for indentation, causing IndentationError in some environments.

- Placing code outside proper blocks, causing logical errors rather than syntax errors.

- Not handling division by zero when the divisor could be zero.

## Revision Tips

- Practice writing at least 5-6 complete programs covering input, processing, and output before the exam.

- Memorize the syntax for f-strings and type conversion functions—they appear frequently in exam questions.

- Understand error messages by intentionally creating errors and running the code to see what happens.

- Review the temperature converter and grade calculator examples—they demonstrate all key concepts from this module.