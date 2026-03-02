# Executing Simple Programs in Python

## Introduction

Python is a high-level, interpreted programming language that has become one of the most popular languages for beginners and professionals alike. Known for its simple syntax and readability, Python serves as an excellent entry point into the world of programming and object-oriented development. Before diving into complex object-oriented concepts, it is essential to understand how to execute simple programs in Python, as this forms the foundation upon which all advanced programming skills are built.

The process of executing simple Python programs involves understanding the Python interpreter, writing code in a text editor or IDE, and running that code to produce output. For students at the University of Delhi, mastering this process is crucial as it directly relates to internal assessments and end-semester examinations. Python's design philosophy emphasizes code readability with the use of significant indentation, making it particularly suitable for students transitioning from theoretical computer science concepts to practical programming implementations.

This module will cover the essential components of writing and executing simple Python programs, including setting up the development environment, understanding the program execution flow, working with variables and data types, using basic input/output operations, and implementing control structures. These fundamentals are critical as they underpin all subsequent topics in object-oriented programming with Python.

## Key Concepts

### 1. Python Interpreter and Execution Environment

The Python interpreter is the program that reads and executes Python code. When you run a Python program, the interpreter processes your source code line by line, converting it into bytecode that the Python Virtual Machine (PVM) can execute. Understanding this execution model is fundamental to debugging and optimizing your programs.

There are multiple ways to execute Python code:

- **Interactive Mode**: Using the Python shell (python or python3 in terminal) allows you to type and execute code line by line. This is excellent for experimentation and learning.
- **Script Mode**: Writing code in a file with .py extension and executing it using the python command. This is the standard approach for developing applications.
- **IDEs and Text Editors**: Tools like PyCharm, VS Code, Jupyter Notebook, and IDLE provide integrated environments for writing, testing, and debugging Python code.

### 2. Structure of a Simple Python Program

A basic Python program follows a specific structure. The interpreter executes code from the top of the file downward, with functions and classes defined but not executed until called. The execution flow begins with the first executable statement that is not inside a function definition.

```python
# This is a comment - ignored by the interpreter
"""
This is a multi-line string
also often used as documentation
"""

# Import statements (if any)
import math

# Function definitions
def greet(name):
    return f"Hello, {name}!"

# Main execution block
if __name__ == "__main__":
    message = greet("Student")
    print(message)
```

The `if __name__ == "__main__":` construct is crucial in Python. It allows a file to be imported as a module without executing the code meant only for direct execution. This is a key concept that students must understand for modular programming.

### 3. Variables and Data Types

Python is dynamically typed, meaning you don't need to declare variable types explicitly. The interpreter infers the type based on the assigned value. The fundamental data types include:

- **Integers (int)**: Whole numbers without decimal points (e.g., 42, -10, 0)
- **Floating-point numbers (float)**: Numbers with decimal points (e.g., 3.14, -2.5)
- **Strings (str)**: Sequence of characters enclosed in quotes (e.g., "Hello", 'Python')
- **Booleans (bool)**: True or False values

Python also supports complex numbers, lists, tuples, dictionaries, and sets, which will be covered in detail in subsequent modules.

### 4. Basic Input and Output

The `print()` function is used for output. It can handle multiple arguments and supports string formatting:

```python
# Basic output
print("Hello, World!")

# Multiple values
name = "Aditi"
age = 20
print(name, "is", age, "years old")

# Formatted output
print(f"{name} is {age} years old")  # f-string (Python 3.6+)
print("%s is %d years old" % (name, age))  # Old-style formatting
```

For input, Python 3 uses the `input()` function, which always returns a string:

```python
# Reading user input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))  # Convert string to integer

print(f"Welcome, {user_name}!")
print(f"You will be {user_age + 1} next year.")
```

### 5. Indentation and Code Blocks

Python uses indentation to define code blocks, unlike other languages that use curly braces. This is a distinctive feature that enforces readable code. The standard is to use four spaces per indentation level. Mixing tabs and spaces can cause errors, so most IDEs are configured to replace tabs with spaces.

```python
if temperature > 30:
    print("It's hot outside")
    if humidity > 80:
        print("And humid too")
else:
    print(" Pleasant weather")
```

### 6. Common Errors and Debugging

Understanding common errors is essential:

- **SyntaxError**: Code violates Python's syntax rules (missing colons, incorrect indentation, unmatched parentheses)
- **IndentationError**: Inconsistent indentation
- **NameError**: Using an undefined variable or function
- **TypeError**: Operations on incompatible data types
- **ValueError**: Correct type but invalid value

The process of debugging involves reading error messages carefully, which indicate the line number where the error occurred and the type of error.

## Examples

### Example 1: Simple Arithmetic Calculator

**Problem**: Write a program that accepts two numbers from the user and displays their sum, difference, product, and quotient.

**Solution**:

```python
# Simple Arithmetic Calculator
# This program demonstrates basic operations in Python

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Display results
print(f"\nResults for {num1} and {num2}:")
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Difference: {num1} - {num2} = {difference}")
print(f"Product: {num1} * {num2} = {product}")
print(f"Quotient: {num1} / {num2} = {quotient:.2f}")  # Round to 2 decimals
```

**Sample Output**:
```
Enter first number: 15
Enter second number: 4

Results for 15.0 and 4.0:
Sum: 15.0 + 4.0 = 19.0
Difference: 15.0 - 4.0 = 11.0
Product: 15.0 * 4.0 = 60.0
Quotient: 15.0 / 4.0 = 3.75
```

### Example 2: Temperature Converter

**Problem**: Write a program to convert temperature from Celsius to Fahrenheit and vice versa based on user's choice.

**Solution**:

```python
# Temperature Conversion Program

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Display menu
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Invalid choice!")
```

**Sample Output**:
```
Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter your choice (1 or 2): 1
Enter temperature in Celsius: 37
37.0°C = 98.6°F
```

### Example 3: Grade Calculator

**Problem**: Write a program that accepts marks in five subjects and calculates the average, then displays the grade based on the average.

**Solution**:

```python
# Grade Calculator
# Calculate average marks and assign grades

subjects = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]
marks = []

# Input marks for each subject
print("Enter marks for 5 subjects (out of 100):\n")
for subject in subjects:
    while True:
        try:
            mark = float(input(f"{subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Calculate average
average = sum(marks) / len(marks)

# Determine grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B+"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

# Display results
print(f"\n{'='*40}")
print("RESULT")
print(f"{'='*40}")
print(f"Total Marks: {sum(marks)}/500")
print(f"Average: {average:.2f}%")
print(f"Grade: {grade}")
print(f"{'='*40}")
```

**Sample Output**:
```
Enter marks for 5 subjects (out of 100):

Mathematics: 85
Physics: 90
Chemistry: 78
English: 88
Computer Science: 92

========================================
RESULT
========================================
Total Marks: 433.0/500
Average: 86.60%
Grade: A
========================================
```

## Exam Tips

1. **Understand the Execution Flow**: Be clear about how Python executes code from top to bottom, and how function calls create a new execution context that returns to the calling point.

2. **Know the Difference Between print() and return**: In exams, students often confuse print() (outputs to console) with return (passes value back from a function). Remember that print() is for display, return is for function output.

3. **Data Type Conversion**: Always remember that input() returns a string. Use int(), float(), or explicit type conversion when performing arithmetic operations. This is a common source of errors in exam programs.

4. **String Formatting**: Be familiar with f-strings (formatted string literals), format() method, and % formatting. F-strings are the modern and preferred approach in Python 3.6+.

5. **Indentation Matters**: In the exam, incorrect indentation can cause IndentationError. Practice writing properly indented code. Use 4 spaces consistently, not tabs.

6. **Error Handling**: Understand basic try-except blocks for handling ValueError when converting user input to numbers. This makes your programs robust.

7. **Variable Naming Conventions**: Follow Python naming conventions—use lowercase with underscores for variable names (e.g., student_name), and use meaningful names that describe the variable's purpose.

8. **The `if __name__ == "__main__":` Pattern**: This is frequently tested in DU exams. Understand why and when to use this construct in your programs.

9. **Practice Debugging**: Read error messages carefully. They indicate the line number and type of error. Common errors like SyntaxError, NameError, and TypeError should be instantly recognizable.

10. **Modular Code**: Break your solution into smaller functions. This makes code more readable, testable, and is often required in exam questions asking to "write a function to..."