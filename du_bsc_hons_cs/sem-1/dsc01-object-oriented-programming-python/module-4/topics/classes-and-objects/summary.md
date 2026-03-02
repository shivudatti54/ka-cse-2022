# Classes And Objects — OOP Python

## Introduction

Object-Oriented Programming (OOP) is a fundamental paradigm in Python that organizes software design around **data** (objects) rather than **functions** and **logic**. For Delhi University's NEP 2024 UGCF syllabus, understanding Classes and Objects is essential as they form the backbone of Python's OOP concepts.

---

## Key Concepts

### Class
- A **blueprint** for creating objects
- Defines attributes (variables) and methods (functions)
- Syntax: `class ClassName:`

### Object
- An **instance** of a class
- Represents a real-world entity
- Created by calling the class name as a function: `obj = ClassName()`

### Methods
- Functions defined inside a class
- **Instance methods**: Operate on object instances (require `self`)
- **Class methods**: Operate on class itself (`@classmethod`)
- **Static methods**: Independent functions (`@staticmethod`)

### Constructor (`__init__`)
- Special method called automatically when an object is created
- Initializes object attributes
- Syntax: `def __init__(self, parameters):`

### `self` Parameter
- Reference to the **current instance** of the class
- Used to access variables and methods within the class

### Attributes
- **Instance attributes**: Unique to each object (defined in `__init__`)
- **Class attributes**: Shared across all instances (defined outside methods)

### Destructor (`__del__`)
- Called when an object is destroyed
- Used for cleanup operations

### Access Modifiers
- **Public**: `self.name` — accessible everywhere
- **Private**: `self.__name` — name mangling (accessible as `_ClassName__name`)
- **Protected**: `self._name` — convention for subclass access

---

## Example Code

```python
class Student:
    university = "Delhi University"  # Class attribute
    
    def __init__(self, name, roll):
        self.name = name              # Instance attribute
        self.__roll = roll            # Private attribute
    
    def display(self):
        print(f"Name: {self.name}, Roll: {self.__roll}")

# Creating object
s1 = Student("Amit", 101)
s1.display()
```

---

## Conclusion

Classes and Objects are the foundation of Python's OOP approach. Mastery of **defining classes**, **creating objects**, **using constructors/destructors**, and **managing access modifiers** is crucial for exam success and practical programming. These concepts enable modular, reusable, and maintainable code development — essential skills for any computer science professional.