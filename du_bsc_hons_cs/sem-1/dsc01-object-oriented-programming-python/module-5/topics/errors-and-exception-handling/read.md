# Errors And Exception Handling in Python

## Object Oriented Programming (Python) — BSc (Hons) Computer Science

### Delhi University, NEP 2024 UGCF

---

## 1. Introduction

Exception handling is a critical concept in Python programming that deals with the runtime errors that occur while a program is executing. In the context of Object-Oriented Programming (OOP), exception handling provides a structured mechanism to manage unexpected situations, making your code more robust, maintainable, and user-friendly.

### What is an Exception?

An **exception** is an event that disrupts the normal flow of the program's instructions during execution. When Python encounters an error, it creates an exception object. If not handled properly, the program terminates and displays an error message.

### Why Exception Handling Matters

In real-world software development, applications must handle various unexpected scenarios:

- **User Input Errors**: Users may enter invalid data (e.g., letters instead of numbers)
- **File Operations**: Files may not exist or may be inaccessible
- **Network Issues**: Connection timeouts or server unavailability
- **Mathematical Errors**: Division by zero or square root of negative numbers
- **Resource Limitations**: Memory exhaustion or disk full

Without proper exception handling, any error would crash the application. With exception handling, we can gracefully manage these situations, provide meaningful feedback to users, and ensure the program continues running or exits cleanly.

### Delhi University Syllabus Context

This topic aligns with the **NEP 2024 UGCF** curriculum for BSc (Hons) Computer Science, specifically covering:
- Exception handling mechanisms in Python
- Custom exception classes
- Best practices for error management
- Real-world application scenarios

---

## 2. Types of Errors in Python

### 2.1 Syntax Errors (Parsing Errors)

These occur when Python cannot parse the code due to incorrect syntax. The program cannot run until these are fixed.

```python
# Example of Syntax Error
def greet(name)  # Missing colon
    print(f"Hello, {name}")
```

**Error Message**: `SyntaxError: invalid syntax`

### 2.2 Runtime Errors (Logical Errors)

These occur during program execution after successful parsing. These are the errors that exception handling addresses.

```python
# Example of Runtime Error
result = 10 / 0  # ZeroDivisionError
```

### 2.3 Logical Errors (Semantic Errors)

These are the hardest to detect as the program runs but produces incorrect results.

```python
# Example of Logical Error
# Intent: Calculate average of three numbers
average = a + b + c / 3  # Wrong! Only c is divided by 3
# Correct: average = (a + b + c) / 3
```

---

## 3. Exception Handling Basics

### 3.1 The try-except Block

The fundamental structure for handling exceptions in Python:

```python
try:
    # Code that may raise an exception
    risky_operation()
except ExceptionType:
    # Code to handle the exception
    handle_error()
```

**Example 1: Basic Exception Handling**

```python
# Basic exception handling example
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

# Testing the function
divide_numbers(10, 2)    # Output: Result: 5.0
divide_numbers(10, 0)    # Output: Error: Division by zero is not allowed!
```

### 3.2 Multiple except Blocks

Python allows multiple `except` blocks to handle different exception types specifically:

```python
def process_input(value):
    try:
        number = int(value)
        result = 100 / number
        print(f"100 divided by {number} is {result}")
    except ValueError:
        print("Error: Input must be a valid integer!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid type for division!")

# Testing multiple exceptions
process_input("42")      # Works fine
process_input("hello")   # ValueError caught
process_input("0")       # ZeroDivisionError caught
process_input([1, 2])    # TypeError caught
```

### 3.3 Catching Multiple Exceptions in One Block

You can catch multiple exceptions together:

```python
try:
    # Risky operation
    value = int(input("Enter a number: "))
    result = 50 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")
    print("Please try again with valid input.")
```

### 3.4 The else Clause

The `else` block executes only if no exception was raised in the `try` block:

```python
def read_and_divide(filename, divisor):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            number = int(content.strip())
            result = number / divisor
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: File does not contain a valid integer.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        # This runs ONLY if no exception occurred
        print(f"Success! Result is {result}")
        return result

# If file exists and contains valid number, else block executes
```

### 3.5 The finally Clause

The `finally` block always executes, regardless of whether an exception occurred or not. It's used for cleanup operations:

```python
def file_operation(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"File content: {content}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    finally:
        # This ALWAYS executes
        if file:
            file.close()
            print("File closed successfully.")
```

**Use Cases for finally**:
- Closing database connections
- Closing file handles
- Releasing network sockets
- Cleaning up temporary resources

---

## 4. Common Built-in Exceptions in Python

Python provides numerous built-in exceptions. Here are the most commonly used:

| Exception | Description |
|-----------|-------------|
| `ZeroDivisionError` | Division or modulo by zero |
| `ValueError` | Operation receives inappropriate value |
| `TypeError` | Operation on incompatible type |
| `IndexError` | Sequence index out of range |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File or directory not found |
| `IOError` | Input/output operation failure |
| `AttributeError` | Attribute reference or assignment failure |
| `ImportError` | Import statement fails |
| `MemoryError` | Operation runs out of memory |
| `RuntimeError` | Generic runtime error |
| `KeyboardInterrupt` | User interrupts execution (Ctrl+C) |
| `Exception` | Base class for all exceptions |

**Example 2: Handling Multiple Common Exceptions**

```python
def demonstrate_exceptions():
    # Dictionary for demonstration
    my_dict = {"name": "Amit", "age": 21}
    
    # List for demonstration
    my_list = [10, 20, 30]
    
    # 1. IndexError
    try:
        print(my_list[10])
    except IndexError:
        print("Error: List index out of range")
    
    # 2. KeyError
    try:
        print(my_dict["address"])
    except KeyError:
        print("Error: Key 'address' not found in dictionary")
    
    # 3. TypeError
    try:
        result = "hello" + 5
    except TypeError:
        print("Error: Cannot concatenate string with integer")
    
    # 4. ValueError
    try:
        number = int("abc")
    except ValueError:
        print("Error: Invalid literal for int()")
    
    print("Program continues after handling all exceptions!")

demonstrate_exceptions()
```

---

## 5. Raising Exceptions (raise Keyword)

Python allows you to explicitly raise exceptions using the `raise` keyword:

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age cannot be greater than 150!")
    return f"Valid age: {age}"

# Testing raise
try:
    print(validate_age(25))
    print(validate_age(-5))
except ValueError as e:
    print(f"Validation Error: {e}")
```

### Re-raising Exceptions

You can catch an exception, perform some processing, and then re-raise it:

```python
def complex_operation():
    try:
        # Some operation that might fail
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Logging the error...")
        # Re-raise the exception
        raise

try:
    complex_operation()
except ZeroDivisionError:
    print("Exception was re-raised and caught here!")
```

---

## 6. Custom Exceptions (User-Defined Exceptions)

In OOP, you can create custom exception classes by inheriting from the built-in `Exception` class. This is particularly useful for application-specific error handling.

### Creating Custom Exceptions

```python
# Custom exception for insufficient balance
class InsufficientBalanceError(Exception):
    """Raised when account balance is insufficient for withdrawal"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient balance: Available {balance}, Requested {amount}"
        super().__init__(message)

# Custom exception for invalid age
class InvalidAgeError(Exception):
    """Raised when age is not within valid range"""
    def __init__(self, age, message="Age must be between 0 and 150"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}. Provided age: {self.age}"

# Custom exception for authentication failure
class AuthenticationError(Exception):
    """Raised when authentication fails"""
    pass
```

### Using Custom Exceptions

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawn: {amount}. New balance: {self.balance}")

# Testing custom exceptions
account = BankAccount("Rahul", 5000)

try:
    account.deposit(1000)
    account.withdraw(200)
    account.withdraw(10000)  # This will raise InsufficientBalanceError
except InsufficientBalanceError as e:
    print(f"Transaction Failed: {e}")
    print(f"Available balance: {e.balance}")
except ValueError as e:
    print(f"Invalid Input: {e}")
```

### Creating Exception Hierarchy

```python
# Base custom exception
class UniversityError(Exception):
    """Base exception for university-related errors"""
    pass

# Derived exceptions
class AdmissionError(UniversityError):
    """Raised when admission process fails"""
    pass

class GradeError(UniversityError):
    """Raised when grade-related operations fail"""
    pass

class InvalidGradeError(GradeError):
    """Raised when grade is invalid"""
    pass

class AttendanceError(UniversityError):
    """Raised when attendance is insufficient"""
    pass
```

---

## 7. Context Managers (with statement)

Context managers provide a clean way to handle resource management, ensuring proper acquisition and release of resources. The `with` statement automatically handles cleanup, even if exceptions occur.

### Using Context Managers

```python
# File handling with context manager (automatically closes file)
def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Exception can still occur here
            lines = content.split('\n')
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return 0

# The above is equivalent to:
def read_file_manual(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return len(content.split('\n'))
    finally:
        if file:
            file.close()
```

### Custom Context Manager using Class

```python
class DatabaseConnection:
    """Custom context manager for database connections"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        """Called when entering the context"""
        print(f"Connecting to database: {self.db_name}")
        self.connection = f"Connection to {self.db_name} established"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the context"""
        print(f"Closing connection to {self.db_name}")
        self.connection = None
        # Return True to suppress exceptions, False to propagate
        return False
    
    def execute(self, query):
        return f"Executed: {query}"

# Using custom context manager
with DatabaseConnection("StudentDB") as db:
    result = db.execute("SELECT * FROM students")
    print(result)
# Connection automatically closed here
```

### Custom Context Manager using Generator

```python
from contextlib import contextmanager

@contextmanager
def temporary_file(filename):
    """Context manager for temporary file operations"""
    print(f"Creating temporary file: {filename}")
    try:
        file = open(filename, 'w')
        yield file
    finally:
        file.close()
        print(f"Closed and cleaned up: {filename}")

# Usage
with temporary_file("temp.txt") as f:
    f.write("Hello, Delhi University!")
    print("Writing to temporary file")
```

---

## 8. Best Practices in Exception Handling

### 8.1 Do's and Don'ts

**Do's**:
- Be specific about exception types
- Use `finally` for cleanup operations
- Log exceptions for debugging
- Create custom exceptions for domain-specific errors
- Handle exceptions at the appropriate level

**Don'ts**:
- Don't use bare `except:` clauses (catches all exceptions including SystemExit)
- Don't suppress exceptions without proper handling
- Don't use exceptions for flow control (use if-else instead)
- Don't catch exceptions without doing anything useful

### 8.2 Proper Exception Handling Pattern

```python
def proper_exception_handling(data):
    """
    Demonstrates best practices in exception handling
    """
    # Use specific exception types
    try:
        result = int(data)
        
        if result < 0:
            # Raise specific exception with meaningful message
            raise ValueError(f"Negative value not allowed: {result}")
        
        return result / 2
    
    except ValueError as e:
        # Handle specific exception, log it
        print(f"Value Error: {e}")
        raise  # Re-raise if can't handle
    
    except TypeError as e:
        print(f"Type Error: {e}")
        raise
    
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"Unexpected error: {e}")
        raise
    
    finally:
        # Always execute cleanup
        print("Cleanup completed")
```

---

## 9. Real-World Application Example

```python
"""
Student Grade Management System
Demonstrates comprehensive exception handling in a real-world scenario
"""

class InvalidGradeError(Exception):
    """Raised when grade is not in valid range (0-100)"""
    def __init__(self, grade):
        self.grade = grade
        super().__init__(f"Invalid grade: {grade}. Must be between 0 and 100.")

class StudentNotFoundError(Exception):
    """Raised when student record not found"""
    def __init__(self, student_id):
        self.student_id = student_id
        super().__init__(f"Student with ID {student_id} not found.")

class Gradebook:
    """Student grade management system"""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name):
        """Add a new student"""
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists")
        self.students[student_id] = {"name": name, "grades": []}
        print(f"Student {name} added with ID: {student_id}")
    
    def add_grade(self, student_id, subject, grade):
        """Add grade for a student"""
        # Validate student exists
        if student_id not in self.students:
            raise StudentNotFoundError(student_id)
        
        # Validate grade range
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")
        
        if grade < 0 or grade > 100:
            raise InvalidGradeError(grade)
        
        self.students[student_id]["grades"].append({
            "subject": subject,
            "grade": grade
        })
        print(f"Grade added: {subject} = {grade}")
    
    def get_average(self, student_id):
        """Calculate average grade"""
        if student_id not in self.students:
            raise StudentNotFoundError(student_id)
        
        grades = self.students[student_id]["grades"]
        if not grades:
            return 0
        
        total = sum(g["grade"] for g in grades)
        return total / len(grades)
    
    def get_student_info(self, student_id):
        """Get student information"""
        if student_id not in self.students:
            raise StudentNotFoundError(student_id)
        return self.students[student_id]


# Demonstration
def main():
    gradebook = Gradebook()
    
    try:
        # Add students
        gradebook.add_student(101, "Amit Kumar")
        gradebook.add_student(102, "Priya Singh")
        
        # Add valid grades
        gradebook.add_grade(101, "Python", 85)
        gradebook.add_grade(101, "Data Structures", 78)
        gradebook.add_grade(102, "Python", 92)
        
        # Try invalid operations
        gradebook.add_grade(999, "Math", 90)  # Invalid student ID
        gradebook.add_grade(101, "Java", 150)  # Invalid grade
        
    except StudentNotFoundError as e:
        print(f"Student Error: {e}")
    except InvalidGradeError as e:
        print(f"Grade Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        print("\n--- Gradebook Operations Completed ---")

# Run the demonstration
main()
```

---

## 10. Multiple Choice Questions (MCQs)

### Question 1
What will be the output of the following code?

```python
try:
    print("Start")
    x = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
except Exception:
    print("Caught Exception")
finally:
    print("Finally block")
```

A) Start → Caught Exception → Finally block  
B) Start → Caught ZeroDivisionError → Finally block  
C) Start → Finally block → Caught ZeroDivisionError  
D) Start → Caught ZeroDivisionError

### Question 2
Which block is guaranteed to execute regardless of whether an exception occurs?

A) except  
B) else  
C) try  
D) finally

### Question 3
What is the correct way to create a custom exception in Python?

A) class MyException: pass  
B) class MyException(Exception): pass  
C) exception MyException: pass  
D) def MyException: pass

### Question 4
What does the `else` clause in exception handling do?

A) Executes when an exception occurs  
B) Executes only if no exception occurs in the try block  
C) Executes always  
D) Executes when specific condition is met

### Question 5
Which exception is raised when attempting to access a non-existent dictionary key?

A) IndexError  
B) KeyError  
C) AttributeError  
D) ValueError

### Question 6
What is the purpose of the `with` statement in Python?

A) Conditional execution  
B) Automatic resource management  
C) Exception suppression  
D) Loop control

### Question 7
What will be printed?

```python
try:
    raise ValueError("Test")
except ValueError as e:
    print(e)
```

A) Test  
B) ValueError: Test  
C) "Test"  
D) None

### Question 8
Which of the following is NOT a built-in Python exception?

A) ZeroDivisionError  
B) FileNotFoundError  
C) MyCustomError  
D) MemoryError

### Question 9
What happens if an exception is raised in the `finally` block?

A) It is ignored  
B) It replaces any exception from the try block  
C) It is caught by the except block  
D) It causes a syntax error

### Question 10
How do you catch multiple exceptions in a single except block?

A) except ValueError, TypeError:  
B) except (ValueError, TypeError):  
C) except ValueError or TypeError:  
D) except [ValueError, TypeError]:

---

## 11. Key Takeaways

1. **Exception Handling Fundamentals**: Exception handling in Python uses `try`, `except`, `else`, and `finally` blocks to manage runtime errors gracefully without crashing the program.

2. **Multiple Exception Handling**: Python supports multiple `except` blocks to handle different exception types specifically, improving error diagnosis and response.

3. **Control Flow**: The `else` block executes only when no exception occurs in the try block, while `finally` always executes for cleanup operations.

4. **Built-in Exceptions**: Python provides a comprehensive hierarchy of built-in exceptions including ZeroDivisionError, ValueError, TypeError, IndexError, KeyError, and FileNotFoundError.

5. **Custom Exceptions**: In OOP, custom exceptions are created by inheriting from the `Exception` class, enabling domain-specific error handling.

6. **Context Managers**: The `with` statement provides elegant resource management, automatically handling cleanup operations like closing files or releasing connections.

7. **Best Practices**: Always use specific exception types, avoid bare except clauses, use finally for cleanup, and don't use exceptions for normal flow control.

8. **Real-World Application**: Exception handling is essential for building robust applications that can gracefully handle user errors, file operations, network issues, and other unexpected situations.

9. **Raise Keyword**: The `raise` keyword allows programmers to explicitly trigger exceptions when validation fails or error conditions are detected.

10. **Delhi University Syllabus**: This topic forms a crucial part of the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science, testing students' understanding of error management in Python programs.

---

## Answer Key for MCQs

1. B | 2. D | 3. B | 4. B | 5. B | 6. B | 7. A | 8. C | 9. B | 10. B

---

*Generated for BSc (Hons) Computer Science - Delhi University, NEP 2024 UGCF*