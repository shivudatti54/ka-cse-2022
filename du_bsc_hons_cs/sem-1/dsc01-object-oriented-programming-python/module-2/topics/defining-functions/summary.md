# Defining Functions — Object Oriented Programming Python

## Introduction

In Python, a **function** is a reusable block of code that performs a specific task. In the context of Object Oriented Programming (OOP), functions become **methods** when defined inside a class. Understanding function definition is essential for the Delhi University B.Sc. (Hons) Computer Science NEP 2024 UGCF syllabus, as it forms the foundation for implementing encapsulation, abstraction, and modular design in Python programs.

---

## Key Concepts

### 1. Function Definition Syntax
```python
def function_name(parameters):
    """Docstring - describes function purpose"""
    # function body
    return value  # optional
```

### 2. Function Parameters & Arguments
- **Parameters**: Variables listed in function definition
- **Arguments**: Actual values passed when calling function

### 3. Types of Arguments (Delhi University Syllabus Focus)
- **Positional Arguments**: Passed in order
- **Keyword Arguments**: Passed with parameter names
- **Default Arguments**: Have default values
- **`*args`**: Variable positional arguments (tuple)
- **`**kwargs`**: Variable keyword arguments (dictionary)

### 4. Return Values
- Functions can return single or multiple values using tuples
- `return None` is implicit if no return statement specified

### 5. Variable Scope
- **Local**: Defined inside function
- **Global**: Defined outside function
- Use `global` keyword to modify global variables

### 6. Lambda Functions (Anonymous Functions)
```python
square = lambda x: x ** 2
```
- Single-expression functions
- Used with `map()`, `filter()`, `sorted()`

### 7. Functions in OOP Context
- **Methods**: Functions defined inside a class
- **`self` parameter**: Reference to instance (first parameter)
- **`__init__`**: Constructor method (initializes objects)
- **`__del__`**: Destructor method (cleans up)

### 8. Access Modifiers (Python Convention)
- **Public**: `self.variable`
- **Protected**: `self._variable` (convention)
- **Private**: `self.__variable` (name mangling)

---

## Important Exam Points

- Function definition begins with `def` keyword
- Indentation is mandatory in Python
- Docstrings improve code documentation
- *args and **kwargs provide flexibility
- `self` distinguishes methods from regular functions

---

## Conclusion

Mastering function definition is crucial for OOP in Python. It enables code reusability, modularity, and proper encapsulation—key objectives in the Delhi University B.Sc. Computer Science curriculum. Practice defining functions with various parameter types and understanding the OOP method structure for exam success.