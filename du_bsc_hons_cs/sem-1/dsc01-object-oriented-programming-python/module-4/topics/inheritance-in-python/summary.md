# Inheritance in Python — Quick Revision Notes

**Delhi University — BSc (Hons) Computer Science — NEP 2024 UGCF**

---

## Introduction

Inheritance is a fundamental **Object Oriented Programming** concept that allows a class (called *child* or *derived* class) to inherit attributes and methods from another class (called *parent* or *base* class). It promotes **code reusability** and establishes a natural hierarchy between classes.

---

## Key Concepts

### What is Inheritance?
- Enables a subclass to reuse, extend, or modify properties of an existing superclass
- The subclass inherits all non-private members (attributes and methods) of the parent class
- Represented as: `class ChildClass(ParentClass):`

### Types of Inheritance

- **Single Inheritance** — One parent, one child class
- **Multiple Inheritance** — One child inherits from multiple parents
- **Multilevel Inheritance** — Chain: Grandparent → Parent → Child
- **Hierarchical Inheritance** — One parent, multiple children
- **Hybrid Inheritance** — Combination of two or more inheritance types

### Important Methods & Functions

- **`super()`** — Used to call parent class constructors or methods
  ```python
  super().__init__()
  ```
- **Method Overriding** — Redefining a parent method in the child class
- **Method Resolution Order (MRO)** — Determines the order in which base classes are searched (use `ClassName.mro()` or `ClassName.__mro__`)

### Abstract Base Classes (ABC)
- Use `abc` module to define abstract methods
- Forces subclasses to implement specific methods
```python
from abc import ABC, abstractmethod
```

---

## Advantages

- Code reusability
- Logical class hierarchy
- Easier maintenance and extensibility
- Supports polymorphism

---

## Practical Example

```python
class Vehicle:           # Parent
    def __init__(self, brand):
        self.brand = brand
    
    def display(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):      # Child
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def display(self):
        super().display()
        print(f"Model: {self.model}")

c = Car("Toyota", "Innova")
c.display()
```

---

## Conclusion

Inheritance is essential for building scalable and maintainable Python applications. Understanding single, multiple, and multilevel inheritance — along with `super()`, method overriding, and MRO — is crucial for the Delhi University OOP Python syllabus and exams. Master these concepts to efficiently model real-world relationships in code.

---

*Prepared for BSc (Hons) CS — NEP 2024 UGCF Delhi University*