# Constructors And Methods — OOP Python

## Introduction

In Object-Oriented Programming with Python, **constructors** and **methods** form the backbone of class behavior. Constructors initialize objects, while methods define the functionality. This topic is essential for Delhi University's NEP 2024 OOP Python syllabus (Paper: OOP through Python, Unit-III).

---

## Constructors

A **constructor** is a special method that initializes an object when created.

- **`__init__()` method**: The default constructor in Python
  ```python
  class Student:
      def __init__(self, name, roll_no):
          self.name = name
          self.roll_no = roll_no
  ```
- **`self` parameter**: Reference to the current instance; must be the first parameter
- **Types of Constructors**:
  - *Default*: No parameters (uses predefined values)
  - *Parameterized*: Accepts arguments for initialization
- **Purpose**: Allocate memory, initialize attributes, establish object state

---

## Methods

Methods are functions defined inside a class that operate on objects.

### Types of Methods

- **Instance Methods**: Access/modify instance variables; first parameter is `self`
  ```python
  def display(self):
      print(f"Name: {self.name}")
  ```

- **Class Methods** (`@classmethod`): Operate on class variables; first parameter is `cls`
  ```python
  @classmethod
  def get_count(cls):
      return cls.count
  ```

- **Static Methods** (`@staticmethod`): No access to class/instance variables; acts like regular function
  ```python
  @staticmethod
  def validate(roll):
      return roll > 0
  ```

### Special Methods (Magic/Dunder Methods)

- `__str__()`: Returns string representation (user-friendly)
- `__repr__()`: Returns official representation (developer-friendly)
- `__add__()`, `__sub__()`: Operator overloading
- `__len__()`, `__getitem__()`: Container behavior

### Access Modifiers (Python Convention)

- `self.var`: Public
- `self._var`: Protected (convention)
- `self.__var`: Private (name mangling)

---

## Constructor Overloading & Method Overriding

- **Python does NOT support multiple constructors**; use default arguments or `*args` instead
- **Method overriding**: Redefining parent class method in child class

---

## Key Differences

| Aspect | Constructor | Method |
|--------|-------------|--------|
| Purpose | Initialize object | Define behavior |
| Name | Always `__init__` | User-defined |
| Call | Automatic on object creation | Explicitly called |

---

## Conclusion

Understanding constructors and methods is vital for exam success. Master `__init__()`, instance/class/static methods, and magic methods as per Delhi University syllabus. Practice writing classes to reinforce concepts—these are frequently tested in practical exams and theory questions.