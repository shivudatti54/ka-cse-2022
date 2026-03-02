# Errors And Exception Handling in Python

## Introduction

Exception handling is a crucial mechanism in Python that allows programmers to manage runtime errors gracefully, preventing program crashes and enabling robust error recovery. In Object Oriented Programming, proper exception handling is essential for building reliable and maintainable applications.

## Key Concepts

### Types of Errors
- **Syntax Errors**: Parsing errors detected before execution (e.g., missing colons, invalid indentation)
- **Runtime Errors (Exceptions)**: Errors occurring during program execution (e.g., division by zero, file not found)
- **Logical Errors**: Flaws in program logic producing incorrect results

### Built-in Python Exceptions
Common exceptions include:
- `ZeroDivisionError` – division by zero
- `TypeError` – incompatible data types
- `ValueError` – inappropriate argument value
- `FileNotFoundError` – file doesn't exist
- `IndexError` – list index out of range
- `KeyError` – dictionary key not found
- `IOError` – input/output operations fail

### Exception Handling Mechanism

**try-except Block**
```python
try:
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Multiple Except Clauses**
```python
try:
    num = int(input())
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division by zero")
```

**try-except-else-finally**
- `try`: Code that may raise exceptions
- `except`: Handle specific exceptions
- `else`: Executes if no exception occurs
- `finally`: Always executes (cleanup operations)

### Raising Exceptions

**Using raise statement**
```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
```

### Custom Exceptions

Creating user-defined exception classes by inheriting from `Exception`:
```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: {amount} > {balance}")
```

### Exception Hierarchy
All exceptions inherit from `BaseException`. The main hierarchy includes:
- `BaseException` → `Exception` → `RuntimeError` → `StopIteration`, `ArithmeticError` → `ZeroDivisionError`, `FloatingPointError`, `OverflowError`

## Conclusion

Exception handling is fundamental to writing robust Python applications. Mastery of try-except blocks, custom exceptions, and proper error propagation enables developers to build fault-tolerant systems. For Delhi University exams, focus on syntax, common exceptions, and practical implementation of error handling patterns.