# Polymorphism and Overloading in Python

## Introduction

Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. This concept is essential in creating flexible and reusable code. In Python, polymorphism is achieved through method overriding and method overloading. In this topic, we will explore the concept of polymorphism and overloading in Python, and how it can be used to create more robust and maintainable software systems.

Python is a dynamically-typed language, which means that it does not support method overloading in the classical sense. However, Python provides several ways to achieve method overloading, including default arguments, variable-length argument lists, and function wrappers.

## Key Concepts

### Polymorphism

Polymorphism is the ability of an object to take on multiple forms. In Python, polymorphism is achieved through method overriding and method overloading. Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. Method overloading, on the other hand, occurs when multiple methods with the same name can be defined, but with different parameter lists.

### Method Overloading

Method overloading is a technique where multiple methods with the same name can be defined, but with different parameter lists. In Python, method overloading is not directly supported, but it can be achieved using default arguments, variable-length argument lists, and function wrappers.

### Default Arguments

Default arguments are used to provide a default value for a parameter when it is not passed to the function. In Python, default arguments can be used to achieve method overloading. For example, a function can be defined with a default argument, and then called with or without that argument.

### Variable-Length Argument Lists

Variable-length argument lists are used to pass a variable number of arguments to a function. In Python, variable-length argument lists can be used to achieve method overloading. For example, a function can be defined with a variable-length argument list, and then called with a different number of arguments.

### Function Wrappers

Function wrappers are used to wrap a function with another function. In Python, function wrappers can be used to achieve method overloading. For example, a function can be defined with a wrapper that checks the type of the arguments and calls the appropriate function.

## Examples

### Example 1: Method Overloading using Default Arguments

```python
class Calculator:
    def calculate(self, x, y, operation='add'):
        if operation == 'add':
            return x + y
        elif operation == 'subtract':
            return x - y
        else:
            raise ValueError("Invalid operation")

calculator = Calculator()
print(calculator.calculate(5, 3))  # Output: 8
print(calculator.calculate(5, 3, 'subtract'))  # Output: 2
```

### Example 2: Method Overloading using Variable-Length Argument Lists

```python
class Printer:
    def print(self, *args):
        for arg in args:
            print(arg)

printer = Printer()
printer.print("Hello", "World")  # Output: Hello World
printer.print("Hello", "World", "Python")  # Output: Hello World Python
```

### Example 3: Method Overloading using Function Wrappers

```python
class Converter:
    def convert(self, value):
        if isinstance(value, int):
            return self.convert_int(value)
        elif isinstance(value, str):
            return self.convert_str(value)
        else:
            raise ValueError("Invalid type")

    def convert_int(self, value):
        return value * 2

    def convert_str(self, value):
        return value.upper()

converter = Converter()
print(converter.convert(5))  # Output: 10
print(converter.convert("hello"))  # Output: HELLO
```

## Exam Tips

1. Understand the concept of polymorphism and how it is achieved in Python.
2. Know how to use default arguments, variable-length argument lists, and function wrappers to achieve method overloading.
3. Be able to define and use methods with default arguments.
4. Be able to define and use methods with variable-length argument lists.
5. Be able to define and use function wrappers to achieve method overloading.
6. Understand the importance of polymorphism in creating flexible and reusable code.
7. Be able to apply polymorphism and method overloading to real-world problems.