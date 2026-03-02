# Defining Functions in Python

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

Functions are the foundational building blocks of modular, maintainable, and reusable code in Python. In the context of Object-Oriented Programming (OOP), functions serve as methods within classes, enabling encapsulation and behavior definition. Understanding how to define, call, and manipulate functions is essential for any computer science student, particularly those pursuing the Delhi University curriculum under NEP 2024.

In the real world, functions mirror the concept of factory machines: they take raw materials (inputs), process them according to specific instructions (logic), and produce finished products (outputs). For instance, a banking application uses functions to calculate interest, validate user credentials, and process transactions — each function performing a dedicated task that can be reused across different parts of the application.

This study material covers all aspects of defining functions as prescribed in the Delhi University syllabus, including advanced topics like *args, **kwargs, recursion, lambda functions, decorators, and variable scope — areas previously identified as requiring deeper coverage.

---

## 2. Function Definition and Calling

A function is a reusable block of code that performs a specific task. In Python, we define a function using the `def` keyword, followed by the function name and parentheses.

### Syntax

```python
def function_name(parameters):
    """Docstring - describes what the function does"""
    # Function body
    # Statements
    return value  # Optional
```

### Example 1: Basic Function Definition

```python
def greet_student(name):
    """This function greets a student by name."""
    return f"Welcome to Delhi University, {name}!"

# Calling the function
message = greet_student("Aarav")
print(message)
```

**Output:**
```
Welcome to Delhi University, Aarav!
```

### Key Components:
- **Function Name**: Should follow Python naming conventions (lowercase with underscores)
- **Parameters**: Variables that accept input values
- **Docstring**: Documentation string explaining the function's purpose
- **Return Statement**: Sends back a value to the caller (if none specified, returns `None`)

---

## 3. Parameters and Arguments

Python offers multiple ways to pass arguments to functions, providing flexibility in function design.

### 3.1 Positional Arguments
Arguments passed in the order of parameters.

```python
def calculate_area(length, breadth):
    return length * breadth

area = calculate_area(10, 5)  # length=10, breadth=5
print(area)  # Output: 50
```

### 3.2 Keyword Arguments
Arguments passed with parameter names, allowing any order.

```python
area = calculate_area(breadth=5, length=10)  # Order doesn't matter
print(area)  # Output: 50
```

### 3.3 Default Parameters
Parameters with predefined values used when no argument is provided.

```python
def calculate_grade(score, passing_score=40):
    return "Pass" if score >= passing_score else "Fail"

print(calculate_grade(75))       # Uses default passing_score=40
print(calculate_grade(35, 30))   # Overrides default to 30
```

**Important Note**: Default parameters must always come after non-default parameters in the function definition.

---

## 4. *args and **kwargs

These are special syntax elements that allow functions to accept variable numbers of arguments.

### 4.1 *args (Non-Keyword Arguments)
Allows passing a variable number of positional arguments, stored as a tuple.

```python
def sum_all(*numbers):
    """Calculate sum of any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))          # Output: 6
print(sum_all(10, 20, 30, 40))   # Output: 100
print(sum_all())                 # Output: 0
```

### 4.2 **kwargs (Keyword Arguments)
Allows passing a variable number of keyword arguments, stored as a dictionary.

```python
def display_student_info(**details):
    """Display student information"""
    for key, value in details.items():
        print(f"{key}: {value}")

display_student_info(
    name="Priya Sharma",
    roll_no=101,
    course="BSc CS",
    year=2
)
```

**Output:**
```
name: Priya Sharma
roll_no: 101
course: BSc CS
year: 2
```

### Example 2: Combining All Parameter Types

```python
def flexible_function(positional_arg, *args, default="default", **kwargs):
    print(f"Positional: {positional_arg}")
    print(f"*args: {args}")
    print(f"Default: {default}")
    print(f"**kwargs: {kwargs}")

flexible_function("mandatory", 1, 2, 3, default="custom", key="value")
```

---

## 5. Lambda Functions (Anonymous Functions)

Lambda functions are small, anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression.

### Syntax

```python
lambda arguments: expression
```

### Examples

```python
# Basic lambda
square = lambda x: x ** 2
print(square(7))  # Output: 49

# Lambda with multiple arguments
addition = lambda a, b: a + b
print(addition(15, 25))  # Output: 40

# Using lambda with built-in functions
marks = [85, 90, 78, 92, 88]
sorted_marks = sorted(marks, reverse=True)
print(sorted_marks)  # Output: [92, 90, 88, 85, 78]

# Lambda with filter
passing_marks = list(filter(lambda x: x >= 60, marks))
print(passing_marks)  # Output: [85, 90, 78, 92, 88]
```

Lambda functions are extensively used with `map()`, `filter()`, and `reduce()` functions, which are common in data processing tasks.

---

## 6. Variable Scope

Understanding variable scope is crucial for avoiding bugs and writing predictable code.

### 6.1 Local Scope
Variables defined inside a function are local to that function.

```python
def local_scope_demo():
    local_var = "I am local"
    print(local_var)

local_scope_demo()
# print(local_var)  # NameError: name 'local_var' is not defined
```

### 6.2 Global Scope
Variables defined at the module level are global and accessible anywhere.

```python
global_var = "I am global"

def access_global():
    print(global_var)

access_global()  # Output: I am global
print(global_var)  # Output: I am global
```

### 6.3 The global Keyword
Used to modify global variables from within a function.

```python
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment()  # Counter: 1
increment()  # Counter: 2
print(counter)  # 2
```

### 6.4 The nonlocal Keyword
Used to modify variables in an enclosing (non-global) scope, typically in nested functions.

```python
def outer_function():
    outer_var = "outer"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "modified"
        print(f"Inner: {outer_var}")
    
    inner_function()
    print(f"Outer: {outer_var}")

outer_function()
```

**Output:**
```
Inner: modified
Outer: modified
```

---

## 7. Recursion

Recursion occurs when a function calls itself to solve a problem by breaking it into smaller subproblems.

### Example: Factorial Calculation

```python
def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # Output: 120
print(factorial(0))   # Output: 1
```

### Example: Fibonacci Sequence

```python
def fibonacci(n):
    """Return nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ")
```

**Output:**
```
0 1 1 2 3 5 8 13 21 34
```

**Important**: Always include a base case to prevent infinite recursion, which would cause a `RecursionError`.

---

## 8. Decorators

Decorators are a powerful feature that allows modifying the behavior of functions or methods. They wrap one function inside another, adding functionality without modifying the original function's code.

### Basic Decorator

```python
def timing_decorator(func):
    """Decorator to measure execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Function completed"

result = slow_function()
print(result)
```

**Output:**
```
slow_function took 1.001234 seconds
Function completed
```

### Decorator with Arguments

```python
def repeat(times):
    """Decorator factory that repeats function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Delhi University Student")
```

### Practical Use Cases:
- Authentication and authorization
- Logging and debugging
- Performance timing
- Caching results

---

## 9. Nested Functions

Functions defined inside other functions are called nested functions. They have access to the enclosing function's variables (closure).

```python
def outer_function(message):
    def inner_function():
        print(f"Inner function says: {message}")
    
    return inner_function

closure = outer_function("Hello from closure!")
closure()  # Output: Inner function says: Hello from closure!
```

---

## 10. Important Built-in Functions for Functions

| Function | Description |
|----------|-------------|
| `callable()` | Returns True if the object appears callable |
| `help()` | Displays documentation |
| `vars()` | Returns the `__dict__` attribute |
| `map(func, iter)` | Applies function to all items |
| `filter(func, iter)` | Filters items based on function |
| `reduce(func, iter)` | Reduces iterable to single value |

---

## 11. Key Takeaways

1. **Functions** are reusable blocks of code that promote modularity and code reusability.
2. **Parameters** can be positional, keyword, or have default values.
3. ***args** allows variable positional arguments (tuple), while ****kwargs** allows variable keyword arguments (dictionary).
4. **Lambda functions** are anonymous functions useful for short, simple operations.
5. **Variable scope** (local, global, nonlocal) determines where variables are accessible.
6. **Recursion** enables elegant solutions but requires a base case to prevent infinite loops.
7. **Decorators** extend function behavior without modifying the original function code.
8. **Docstrings** should be written for all functions to improve code documentation.

---

## 12. Multiple Choice Questions (MCQs)

### Level 1: Basic Understanding

1. **What keyword is used to define a function in Python?**
   - (a) `function`
   - (b) `def`
   - (c) `func`
   - (d) `define`
   
   **Answer: (b) `def`**

2. **What does a lambda function return?**
   - (a) Nothing
   - (b) The result of its expression
   - (c) A function object
   - (d) An error
   
   **Answer: (b) The result of its expression**

### Level 2: Intermediate

3. **What will be the output of the following code?**
   ```python
   def func(*args, **kwargs):
       print(args, kwargs)
   
   func(1, 2, a=3, b=4)
   ```
   - (a) `(1, 2) {'a': 3, 'b': 4}`
   - (b) `[1, 2] {a: 3, b: 4}`
   - (c) `1 2 a=3 b=4`
   - (d) Error
   
   **Answer: (a) `(1, 2) {'a': 3, 'b': 4}`**

4. **Which keyword is used to modify a global variable from within a function?**
   - (a) `global`
   - (b) `nonlocal`
   - (c) `modify`
   - (d) `outer`
   
   **Answer: (a) `global`**

### Level 3: Advanced

5. **What is the correct way to create a decorator that accepts arguments?**
   - (a) A function that returns a decorator
   - (b) A decorator that accepts *args
   - (c) Using @ before function definition
   - (d) Cannot be done
   
   **Answer: (a) A function that returns a decorator**

6. **What is the output of this recursion?**
   ```python
   def mystery(n):
       if n <= 0:
           return 0
       return n + mystery(n - 2)
   
   print(mystery(5))
   ```
   - (a) 5
   - (b) 9
   - (c) 15
   - (d) Infinite recursion
   
   **Answer: (b) 9** (5 + 3 + 1 + 0)

7. **What does `nonlocal` keyword do?**
   - (a) References global variables
   - (b) References variables in the nearest enclosing scope
   - (c) Creates a new variable
   - (d) None of the above
   
   **Answer: (b) References variables in the nearest enclosing scope**

---

## 13. Exam Tips and Important Questions

### Short Answer Questions (2-3 marks)
1. Differentiate between positional and keyword arguments.
2. Write a lambda function to check if a number is even.
3. Explain the purpose of `*args` and `**kwargs`.
4. What is recursion? Write a recursive function to find the sum of digits of a number.

### Long Answer Questions (5-6 marks)
1. Explain variable scope in Python with examples of local, global, and nonlocal variables.
2. What are decorators? Create a decorator that logs function calls with timestamps.
3. Write a Python program using recursion to calculate the power of a number.
4. Explain lambda functions with at least three practical examples.

### Practical/Lab Questions
1. Write a function that accepts variable number of arguments and returns their average.
2. Create a decorator to count how many times a function has been called.
3. Implement a recursive binary search function.

### Common Mistakes to Avoid
- Forgetting to include a return statement (functions return `None` by default)
- Not providing a base case in recursive functions
- Mixing default and non-default parameters incorrectly
- Modifying global variables without using the `global` keyword

### Time Management for Exams
- Read all questions carefully before attempting
- Start with short answer questions (easier marks)
- For long answer questions, first write the algorithm/pseudocode, then the code
- Always test your code with sample inputs if time permits

---

## 14. Conclusion

Mastering function definitions is fundamental to Python programming and object-oriented design. This topic forms the backbone of modular code development and is essential for the Delhi University BSc (Hons) Computer Science curriculum. Practice these concepts extensively through lab sessions and self-study to achieve excellence in your examinations.

---

*Reference: Delhi University NEP 2024 UGCF Syllabus - Object Oriented Programming Using Python*