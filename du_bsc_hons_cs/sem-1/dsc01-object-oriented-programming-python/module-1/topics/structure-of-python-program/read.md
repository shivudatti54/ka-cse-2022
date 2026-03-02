# Structure of Python Program

## Introduction

Python is a high-level, interpreted programming language that emphasizes code readability and simplicity. Unlike languages such as C++ or Java, Python uses indentation to define code blocks rather than curly braces or keywords, giving Python programs a distinctive and clean appearance. Understanding the structure of a Python program is fundamental to writing effective and error-free code, especially for students at the University of Delhi who are beginning their journey in object-oriented programming.

The structure of a Python program encompasses several key elements: how the Python interpreter reads and executes code, the role of indentation and whitespace, the organization of statements and blocks, the use of modules and packages, and the special `__name__` construct that controls program execution. This topic forms the foundation upon which all subsequent programming concepts in Python are built, making it essential for students to master these fundamentals before proceeding to more advanced topics like functions, classes, and object-oriented design patterns.

In the context of DU's DSC01 course under the NEP 2024 framework, a thorough understanding of Python program structure is crucial for both internal assessments and end-semester examinations. Students must be able to not only write syntactically correct Python programs but also explain why Python programs are structured the way they are, demonstrating a conceptual understanding that goes beyond mere syntax memorization.

## Key Concepts

### Python Interpreter and Execution Model

Python is an interpreted language, which means that the Python interpreter executes code line by line, translating each statement into machine-readable instructions on the fly. When you run a Python script, the interpreter performs several steps: it first compiles the source code into bytecode (a lower-level, platform-independent representation), and then executes this bytecode in the Python Virtual Machine (PVM). This compilation happens automatically and transparently, so as a programmer, you typically don't notice this intermediate step.

The `.py` file extension indicates a Python source file. When the interpreter encounters a Python file, it reads it from top to bottom, executing statements in sequence. However, unlike traditional procedural languages, Python's dynamic nature allows variables to be created and used throughout the program without explicit declaration.

### Indentation and Whitespace

One of the most distinctive features of Python is its use of indentation to define code blocks. In languages like C or Java, code blocks are delimited by curly braces `{}`, but Python uses consistent indentation (typically 4 spaces or a tab). This is not merely a stylistic convention—incorrect indentation will result in an `IndentationError` and the program will not run.

Consider the following example that demonstrates proper indentation:

```python
if temperature > 30:
    print("It's hot outside")  # This is inside the if block
    print("Stay hydrated")     # This is also inside the if block
print("Program continues")    # This is outside the if block
```

The indentation level tells Python exactly which statements belong to which control structure. This feature makes Python code inherently readable and forces programmers to write well-structured code.

### Statements and Expressions

In Python, a statement is an instruction that the Python interpreter can execute. Statements can be simple (like assignment or function calls) or compound (like loops and conditionals). Python statements typically occupy one line, though you can use a backslash `\` or parentheses to continue a statement across multiple lines.

An expression is a combination of values, variables, operators, and function calls that evaluates to a single value. The distinction is important: a statement performs an action, while an expression produces a value.

```python
# Statement - performs an action
x = 5

# Expression - produces a value
y = x + 10  # The right side is an expression that evaluates to 15

# Print is a function call (statement)
print(y)
```

### Comments in Python

Comments are crucial for code documentation and are ignored by the Python interpreter. Python supports two types of comments:

1. **Single-line comments**: Start with the `#` character and extend to the end of the line
2. **Multi-line strings (docstrings)**: Enclosed in triple quotes `"""` or `'''`, used for module, function, or class documentation

```python
# This is a single-line comment
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
        radius (float): The radius of the circle
    
    Returns:
        float: The area of the circle
    """
    pi = 3.14159
    return pi * radius * radius
```

### Modules and the `import` Statement

Python programs are typically organized into modules—files containing Python definitions and statements. The `import` statement is used to bring functionality from one module into another, enabling code reuse and modular programming.

```python
import math          # Import the math module
import os, sys       # Import multiple modules
from datetime import datetime  # Import specific components
import numpy as np   # Import with an alias
```

When you import a module, Python searches for it in a specific order: first the current directory, then the standard library directories, and finally the site-packages directories.

### The `if __name__ == "__main__"` Construct

This is one of the most important concepts in Python program structure. Every Python module has a built-in attribute called `__name__`. When a Python file is run directly (not imported as a module), Python sets `__name__` to `"__main__"`. When the file is imported as a module, `__name__` is set to the module's name.

This construct allows you to write code that runs only when the file is executed directly, not when it's imported:

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This code runs only when the file is executed directly
    print(greet("Student"))
    # Additional test code can go here
```

This pattern is essential for creating reusable modules that can also be run as standalone programs.

### Dynamic Typing and Variable Declaration

Python is dynamically typed, meaning variables don't need explicit type declaration. The type is inferred at runtime based on the assigned value. Variables are created when first assigned and cease to exist when they go out of scope.

```python
x = 10          # x is an integer
x = "Hello"     # Now x is a string - Python allows this
x = [1, 2, 3]   # Now x is a list
```

While this flexibility is powerful, it also requires careful attention to variable types during program execution.

### Input and Output in Python

Python provides simple mechanisms for input and output. The `print()` function outputs text to the console, while the `input()` function reads user input as a string.

```python
# Output
print("Welcome to Python Programming")
print("Value:", 42)

# Input
name = input("Enter your name: ")
print(f"Hello, {name}")
```

## Examples

### Example 1: Basic Program Structure

Let's examine a complete Python program that calculates the factorial of a number:

```python
# factorial.py
# A program to calculate factorial of a number

def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Parameters:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n
    """
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    print("Factorial Calculator")
    print("-" * 20)
    
    try:
        number = int(input("Enter a non-negative integer: "))
        result = calculate_factorial(number)
        print(f"The factorial of {number} is: {result}")
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()
```

This example demonstrates several key structural elements:
- Module-level comments describing the program
- Function definitions with proper indentation
- Docstrings for documentation
- The `if __name__ == "__main__"` block
- Exception handling
- Multiple functions organizing the code

### Example 2: Understanding Indentation and Blocks

Consider this program that demonstrates proper indentation in nested conditions:

```python
# Demonstrating proper indentation

score = 85

if score >= 90:
    grade = "A"
    print("Excellent performance!")
elif score >= 80:
    grade = "B"
    print("Good performance!")
    if score >= 85:
        print("You are eligible for honors")
elif score >= 70:
    grade = "C"
    print("Satisfactory performance")
else:
    grade = "D"
    print("Need improvement")

print(f"Your grade is: {grade}")

# Notice how the inner if (score >= 85) is indented
# within the elif block (score >= 80)
```

The output would be:
```
Good performance!
You are eligible for honors
Your grade is: B
```

### Example 3: Module Structure with Imports

Here's a program that demonstrates modular structure:

```python
# main_program.py
import math
from datetime import datetime

def calculate_circle_properties(radius):
    """Calculate area and circumference of a circle."""
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

def display_properties(radius):
    """Display circle properties in a formatted manner."""
    area, circumference = calculate_circle_properties(radius)
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Circle Properties (Radius: {radius})")
    print("=" * 35)
    print(f"Area:         {area:.2f} square units")
    print(f"Circumference: {circumference:.2f} units")
    print(f"Calculated at: {current_time}")

if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    display_properties(r)
```

This demonstrates importing modules, using module functions (math.pi), handling multiple return values, and using the datetime module.

## Exam Tips

For DU's Computer Science examinations on Python program structure, keep these essential points in mind:

1. **Remember that indentation is mandatory in Python** - Unlike C++ or Java where indentation is for readability, Python requires consistent indentation. Missing indentation or mixing tabs with spaces will cause an IndentationError.

2. **Understand the `__name__` == "__main__" construct thoroughly** - This is frequently tested in exams. Remember that when a file is run directly, `__name__` equals `"__main__"`, but when imported, it equals the module name.

3. **Know the difference between statements and expressions** - An expression evaluates to a value; a statement performs an action. This distinction is fundamental and often tested.

4. **Remember the import search path order** - First current directory, then standard library, then site-packages. This helps understand import errors.

5. **Python uses dynamic typing** - Variables are not declared with types, and the same variable can hold different types at different times during execution.

6. **Docstrings use triple quotes** - Unlike comments (which use #), documentation strings use triple quotes and are accessible at runtime through the `__doc__` attribute.

7. **Multi-line statements** - Use parentheses, brackets, or braces for implicit continuation, or backslash for explicit line continuation.

8. **Python is case-sensitive** - `Print` and `print` are different. This is a common source of errors for beginners.

9. **Every Python file is a module** - The filename (without .py extension) becomes the module name. This is why module names should follow Python identifier rules.

10. **Practice writing clean, properly indented code** - Examiners often check for proper indentation even in pseudo-code answers.