# Syntax and Semantics in Python

## Introduction

Python is a high-level, interpreted programming language known for its clean syntax and powerful semantics. Before diving into Object-Oriented Programming (OOP), it is essential to understand the fundamental syntax rules and semantic principles that govern how Python code is written and interpreted. This topic forms the foundation upon which all advanced Python programming, including OOP concepts like classes, objects, inheritance, and polymorphism, are built.

The distinction between syntax and semantics is crucial in programming languages. Syntax refers to the set of rules that define the structure of a valid Python program—what combinations of symbols and characters are considered合法 (valid). Semantics, on the other hand, deals with the meaning assigned to these syntactically correct constructs—what the program actually does when executed. Understanding this distinction helps programmers write code that is not only syntactically correct but also logically sound and efficient.

In the context of DU's Computer Science curriculum, a thorough grasp of Python syntax and semantics is mandatory as it appears frequently in internal assessments and end-semester examinations. This knowledge also serves as a prerequisite for understanding Object-Oriented Programming paradigms, which are central to modern software development.

## Key Concepts

### 1. Python Syntax Fundamentals

**Indentation**: Unlike other programming languages that use braces or keywords to define code blocks, Python uses indentation (whitespace at the beginning of a line) to denote blocks of code. This is a unique semantic feature of Python that enforces readable code structure. Typically, four spaces or one tab is used for each level of indentation.

```python
if condition:
    # This block is executed if condition is True
    statement1
    statement2
else:
    # This block is executed if condition is False
    statement3
```

**Statements**: In Python, a statement is a unit of code that the Python interpreter can execute. Simple statements fit on a single line, while compound statements (like if, for, while, function definitions) span multiple lines using indentation.

**Comments**: Comments are non-executable text used for documentation. Python uses the hash symbol (#) for single-line comments. For multi-line comments, Python programmers typically use triple quotes (''' or """) even though they technically create string literals.

```python
# This is a single-line comment

"""
This is a
multi-line comment
"""
```

**Variables and Assignment**: In Python, variables are created when assigned. There is no explicit declaration keyword. Python is dynamically typed, meaning the type is determined at runtime.

```python
x = 10          # Integer
name = "Alice"  # String
pi = 3.14159    # Float
is_active = True  # Boolean
```

### 2. Data Types and Objects

Python is an object-oriented language where everything is an object. Every value has a type, and types determine what operations can be performed.

**Basic Data Types**:
- **int**: Integer numbers (e.g., 42, -7, 0)
- **float**: Floating-point numbers (e.g., 3.14, -2.5)
- **str**: Strings (e.g., "Hello", 'Python')
- **bool**: Boolean values (True, False)
- **None**: Special null value

**Type Checking**: The `type()` function returns the data type of an object. The `isinstance()` function checks if an object belongs to a particular type.

```python
x = 10
print(type(x))           # Output: <class 'int'>
print(isinstance(x, int))  # Output: True
```

### 3. Operators and Expressions

Python supports various operators that perform operations on operands:

**Arithmetic Operators**: +, -, *, /, // (floor division), % (modulo), ** (exponentiation)

**Comparison Operators**: ==, !=, <, >, <=, >=

**Logical Operators**: and, or, not

**Assignment Operators**: =, +=, -=, *=, /=, //=, %=, **=

```python
# Example of operator precedence
result = 2 + 3 * 4    # Result is 14, not 20 (multiplication has higher precedence)
result = (2 + 3) * 4  # Result is 20 (parentheses override precedence)
```

### 4. Control Flow Structures

**Conditional Statements**: The if, elif, and else statements control program flow based on conditions.

```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
```

**Loops**: Python provides for and while loops for iteration. The for loop iterates over sequences (lists, strings, tuples, dictionaries).

```python
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

### 5. Input and Output

**print() Function**: Used to output data to the console. Supports string formatting.

```python
name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")  # f-string
print("My name is {} and I am {} years old.".format(name, age))
```

**input() Function**: Used to read user input from the console.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

### 6. Python Semantics: Namespaces and Scope

Understanding namespaces and scope is crucial for OOP. A namespace is a dictionary that maps names to objects. Python has several namespaces:

- **Built-in Namespace**: Contains built-in functions and exceptions
- **Global Namespace**: Module-level names
- **Local Namespace**: Function-level names

**LEGB Rule**: Python resolves names in this order: Local → Enclosing → Global → Built-in

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Prints "local"
    
    inner()
    print(x)  # Prints "enclosing"

outer()
print(x)  # Prints "global"
```

## Examples

### Example 1: Understanding Python Syntax Rules

**Problem**: Identify and correct syntax errors in the following code:

```python
if x > 0
    print("Positive")
else:
print("Non-positive")
```

**Solution**:
The code has two syntax errors:
1. Missing colon (:) after the condition in the if statement
2. The print statement under else is not indented

**Corrected Code**:
```python
if x > 0:
    print("Positive")
else:
    print("Non-positive")
```

### Example 2: Demonstrating Dynamic Typing

**Problem**: Write a program that demonstrates Python's dynamic typing by assigning different types to the same variable.

**Solution**:
```python
# Initially, x is an integer
x = 10
print(f"x = {x}, type = {type(x)}")

# Now x becomes a string
x = "Hello"
print(f"x = {x}, type = {type(x)}")

# Now x becomes a list
x = [1, 2, 3]
print(f"x = {x}, type = {type(x)}")

# Now x becomes a float
x = 3.14
print(f"x = {x}, type = {type(x)}")
```

**Output**:
```
x = 10, type = <class 'int'>
x = Hello, type = <class 'str'>
x = [1, 2, 3], type = <class 'list'>
x = 3.14, type = <class 'float'>
```

This demonstrates that Python variables can hold values of different types at different times during program execution.

### Example 3: Scope and Namespace Resolution

**Problem**: Predict the output of the following code and explain the LEGB rule:

```python
counter = 10  # Global variable

def update_counter():
    counter = 20  # Local variable
    print(f"Inside function: counter = {counter}")

update_counter()
print(f"Outside function: counter = {counter}")
```

**Solution**:
```
Inside function: counter = 20
Outside function: counter = 10
```

**Explanation**: The variable `counter` inside the function is a local variable that shadows the global variable. Changes to the local variable do not affect the global variable. To modify the global variable, we must use the `global` keyword:

```python
counter = 10

def update_counter():
    global counter
    counter = 20
    print(f"Inside function: counter = {counter}")

update_counter()
print(f"Outside function: counter = {counter}")
```

Now the output becomes:
```
Inside function: counter = 20
Outside function: counter = 20
```

## Exam Tips

1. **Remember Python's Indentation Rule**: Unlike C/C++ or Java, Python uses indentation to define code blocks. Missing colons (:) after control statements is a common syntax error that examiners frequently test.

2. **Know the Difference Between = and ==**: A single equals sign (=) is assignment, while double equals (==) is comparison. Using = in a conditional statement is a syntax error.

3. **Understand Dynamic Typing**: Be prepared for questions about Python being dynamically typed versus statically typed languages. Know how type() and isinstance() work.

4. **Master Operator Precedence**: Remember that ** has the highest precedence, followed by * / // %, then + -, then comparison operators, then logical operators. Use parentheses to make code clear.

5. **LEGB Rule is Crucial**: Questions on namespace resolution (Local, Enclosing, Global, Built-in) are common. Always identify which namespace a variable belongs to when answering.

6. **F-Strings for Output**: The modern way to format output in Python is using f-strings (formatted string literals). Know how to use them for the exam.

7. **Practice Debugging**: Examiners often ask to identify errors in given code snippets. Pay attention to indentation, colons, unclosed parentheses, and incorrect variable names.

8. **Understand Mutable vs Immutable**: This is a semantics concept—lists, dictionaries, and sets are mutable; integers, floats, strings, and tuples are immutable. This affects how arguments are passed to functions.