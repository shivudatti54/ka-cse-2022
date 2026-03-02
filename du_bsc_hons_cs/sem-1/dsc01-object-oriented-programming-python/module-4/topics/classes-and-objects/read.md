# Classes and Objects in Python: Comprehensive Study Material

## Object Oriented Programming Python — BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around **data** (objects) rather than functions and logic. Python, as a multi-paradigm programming language, provides robust support for OOP through its class mechanism.

### Why OOP Matters in the Real World?

Consider the following real-world scenarios where classes and objects are fundamental:

- **Banking Systems**: A `BankAccount` class encapsulates account balance, transaction history, and operations like deposit/withdrawal. Each customer's account is an individual object with its own state.

- **E-commerce Platforms**: Products, customers, orders, and carts are all represented as classes with specific attributes and behaviors.

- **Game Development**: Characters, weapons, and game environments are modeled as classes, where each instance (object) has unique properties while sharing common behaviors.

- **Social Media**: User profiles, posts, and comments are objects of respective classes, enabling modular and maintainable code.

### Delhi University Syllabus Context

This topic aligns with the **NEP 2024 UGCF** curriculum for BSc (Hons) Computer Science, specifically covering:
- Understanding classes and objects
- Implementing encapsulation, abstraction, and polymorphism
- Working with inheritance and method types
- Using special/dunder methods

---

## 2. Fundamental Concepts: Classes and Objects

### 2.1 What is a Class?

A **class** is a blueprint or template for creating objects. It defines a set of attributes (variables) and methods (functions) that characterize any object instantiated from it.

### 2.2 What is an Object?

An **object** (also called an instance) is a concrete entity created from a class blueprint. Each object has:
- **Identity**: Unique identifier (memory address)
- **State**: Values of attributes at any point
- **Behavior**: Methods that can be invoked

### 2.3 Class Definition in Python

```python
class Student:
    """A class to represent a student"""
    
    # Class attribute (shared by all instances)
    institution = "Delhi University"
    
    # Constructor / Initializer
    def __init__(self, name, roll_no, course):
        # Instance attributes (unique to each object)
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.grades = []
    
    # Instance method
    def add_grade(self, grade):
        self.grades.append(grade)
    
    # Instance method
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")
        print(f"Institution: {self.institution}")
    
    # Special method (dunder method)
    def __str__(self):
        return f"Student: {self.name} ({self.roll_no})"
```

### 2.4 Creating Objects

```python
# Creating objects (instances)
student1 = Student("Aisha Khan", "CS/2024/001", "BSc CS Hons")
student2 = Student("Rahul Sharma", "CS/2024/002", "BSc CS Hons")

# Accessing attributes
print(student1.name)          # Output: Aisha Khan
print(student2.institution)   # Output: Delhi University (class attribute)

# Calling methods
student1.add_grade(85)
student1.add_grade(90)
student1.display_info()
```

### 2.5 The `self` Parameter

The `self` parameter refers to the **current instance** of the class. It allows access to the object's attributes and methods within the class. When you call `student1.display_info()`, Python automatically passes `student1` as `self`.

---

## 3. Types of Attributes

### 3.1 Instance Attributes

Attributes defined inside `__init__` with `self` prefix are **instance attributes**. Each object has its own copy.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand    # Instance attribute
        self.model = model    # Instance attribute

car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")

print(car1.brand)  # Toyota
print(car2.brand)  # Honda
```

### 3.2 Class Attributes

Attributes defined directly inside the class (outside any method) are **class attributes**. They are shared by all instances.

```python
class Bank:
    bank_name = "State Bank of India"  # Class attribute
    branch = "Delhi Main Branch"
    
    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance attribute

# Accessing class attributes
print(Bank.bank_name)  # State Bank of India
```

### 3.3 Difference Between Instance and Class Attributes

| Aspect | Instance Attribute | Class Attribute |
|--------|-------------------|-----------------|
| Definition | Inside `__init__` with `self` | Outside all methods |
| Scope | Specific to each object | Shared by all objects |
| Memory | Separate copy per object | Single copy for all objects |
| Access | `self.attribute` or `obj.attribute` | `ClassName.attribute` or `self.attribute` |

---

## 4. Types of Methods

Python supports three types of methods, each serving a distinct purpose:

### 4.1 Instance Methods

The most common type. They operate on instance attributes and require `self` as the first parameter.

```python
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):  # Instance method
        return self.length * self.breadth
    
    def perimeter(self):  # Instance method
        return 2 * (self.length + self.breadth)

rect = Rectangle(10, 5)
print(f"Area: {rect.area()}")        # Output: Area: 50
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30
```

### 4.2 Class Methods

Defined with `@classmethod` decorator. They operate on class attributes and receive `cls` as the first parameter. Useful for factory methods or modifying class-level state.

```python
class Employee:
    company = "Tech Solutions Pvt Ltd"
    employees = []
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees.append(self)
    
    @classmethod
    def total_employees(cls):
        return f"Total Employees: {len(cls.employees)}"
    
    @classmethod
    def company_info(cls):
        return f"Company: {cls.company}"

# Creating employees
emp1 = Employee("Priya Singh", 50000)
emp2 = Employee("Amit Kumar", 55000)

print(Employee.total_employees())  # Total Employees: 2
print(Employee.company_info())     # Company: Tech Solutions Pvt Ltd
```

### 4.3 Static Methods

Defined with `@staticmethod` decorator. They don't require `self` or `cls`. They behave like regular functions but belong to the class namespace. Used for utility functions logically related to the class.

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# No need to create an instance
print(MathOperations.add(10, 20))           # 30
print(MathOperations.is_even(15))           # False
```

---

## 5. Encapsulation

**Encapsulation** is the bundling of data (attributes) and methods that operate on that data into a single unit (class). It also restricts direct access to some of an object's components, which is a means of preventing accidental interference and misuse of data.

### 5.1 Access Specifiers in Python

Python uses naming conventions (not strict access modifiers like Java/C++) to indicate access levels:

| Type | Convention | Description |
|------|-------------|-------------|
| Public | `name` | Accessible from anywhere |
| Protected | `_name` | Accessible within class and subclasses |
| Private | `__name` | Accessible only within the class |

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public
        self._account_number = "1234567890"   # Protected (convention)
        self.__balance = balance              # Private (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

# Creating object
account = BankAccount("Rohit Verma", 10000)

print(account.account_holder)     # Rohit Verma (accessible)
print(account._account_number)    # 1234567890 (accessible by convention)
# print(account.__balance)        # AttributeError (not accessible directly)

# Using public methods
account.deposit(5000)
print(account.get_balance())      # 15000
```

### 5.2 Property Decorators (Getters and Setters)

Python provides the `@property` decorator to create managed attributes, enabling getter and setter functionality while maintaining encapsulation.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    
    # Getter
    @property
    def marks(self):
        return self.__marks
    
    # Setter
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks! Must be between 0 and 100")
    
    # Deleter
    @marks.deleter
    def marks(self):
        print("Marks deleted")
        del self.__marks

# Using properties
s = Student("Anjali", 85)
print(s.marks)        # 85 (calls getter)

s.marks = 95          # Calls setter
print(s.marks)        # 95

s.marks = 150         # Invalid marks! Must be between 0 and 100
```

---

## 6. Abstraction

**Abstraction** is the concept of hiding complex implementation details and showing only the necessary features of an object. It helps in reducing programming complexity and effort.

### 6.1 Abstract Classes and Methods

In Python, we use the `abc` module (Abstract Base Classes) to implement abstraction.

```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    # Concrete method
    def display_color(self):
        return f"Color: {self.color}"

# Concrete classes
class Rectangle(Shape):
    def __init__(self, length, breadth, color):
        super().__init__(color)
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Using abstraction
rect = Rectangle(10, 5, "Blue")
circle = Circle(7, "Red")

print(f"Rectangle Area: {rect.area()}")         # 50
print(f"Circle Area: {circle.area():.2f}")      # 153.94
print(rect.display_color())                     # Color: Blue
```

**Note**: Abstract classes cannot be instantiated directly. They serve as blueprints for derived classes.

---

## 7. Polymorphism

**Polymorphism** (meaning "many forms") allows objects of different classes to be treated as objects of a common superclass. It enables one interface to be used for a general class of actions.

### 7.1 Method Overriding

When a subclass provides a specific implementation of a method already defined in its superclass.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Polymorphism in action
animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Gita")]

for animal in animals:
    print(animal.speak())

# Output:
# Buddy says Woof!
# Whiskers says Meow!
# Gita says Moo!
```

### 7.2 Duck Typing

Python's philosophy: "If it walks like a duck and quacks like a duck, then it's a duck." Polymorphism works based on methods rather than class inheritance.

```python
class Duck:
    def speak(self):
        return "Quack Quack!"

class Person:
    def speak(self):
        return "Hello!"

def make_speak(obj):
    return obj.speak()

# Both objects have speak() method - polymorphism works!
print(make_speak(Duck()))     # Quack Quack!
print(make_speak(Person()))   # Hello!
```

### 7.3 Operator Overloading

Python allows operators to be overloaded using special (dunder) methods.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):  # Overloading + operator
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):  # Overloading * operator
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):  # String representation
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2          # Calls __add__
v4 = v2 * 3           # Calls __mul__

print(v3)             # Vector(6, 8)
print(v4)            # Vector(12, 15)
```

---

## 8. Inheritance

**Inheritance** is a mechanism where a class (derived/child class) inherits attributes and methods from another class (base/parent class).

### 8.1 Single Inheritance

```python
# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # Call parent's constructor
        self.subject = subject
    
    def display(self):
        super().display()  # Call parent's display
        print(f"Subject: {self.subject}")

teacher = Teacher("Dr. Sharma", 45, "Computer Science")
teacher.display()
```

### 8.2 Multiple Inheritance

A class can inherit from more than one class.

```python
class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id
    
    def emp_info(self):
        print(f"Employee ID: {self.emp_id}")

class Manager:
    def __init__(self, department):
        self.department = department
    
    def dept_info(self):
        print(f"Department: {self.department}")

class TeamLead(Employee, Manager):
    def __init__(self, emp_id, department, team_size):
        Employee.__init__(self, emp_id)
        Manager.__init__(self, department)
        self.team_size = team_size
    
    def display(self):
        self.emp_info()
        self.dept_info()
        print(f"Team Size: {self.team_size}")

tl = TeamLead("E001", "Development", 10)
tl.display()
```

### 8.3 Method Resolution Order (MRO)

MRO determines the order in which base classes are searched when executing a method. Use `ClassName.mro()` or `ClassName.__mro__` to view the order.

```python
class A:
    def process(self):
        print("A process")

class B(A):
    def process(self):
        print("B process")

class C(A):
    def process(self):
        print("C process")

class D(B, C):
    pass

# MRO for D
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

d = D()
d.process()  # Output: B process (B is searched first)
```

---

## 9. Special Methods (Dunder/Magic Methods)

Special methods (double underscore methods, also called "dunder" methods) enable custom behavior in Python classes.

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # Called when object is created
    def __str__(self):           # Informal string representation
        return f"{self.title} by {self.author}"
    
    def __repr__(self):          # Formal string representation (for developers)
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):           # Custom length
        return self.pages
    
    def __eq__(self, other):     # Equality comparison
        return self.title == other.title and self.author == other.author
    
    def __add__(self, other):    # Addition operator
        return self.pages + other.pages
    
    def __lt__(self, other):     # Less than comparison
        return self.pages < other.pages

book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Python Basics", "John Doe", 250)

print(str(book1))           # Python Basics by John Doe
print(repr(book1))          # Book('Python Basics', 'John Doe', 300)
print(len(book1))          # 300
print(book1 == book2)      # True (same title and author)
print(book1 + book2)       # 550 (total pages)
print(book1 < book2)       # False (300 > 250)
```

### Commonly Used Dunder Methods

| Method | Purpose |
|--------|---------|
| `__init__` | Constructor, called when object is created |
| `__str__` | Informal string representation |
| `__repr__` | Formal string representation |
| `__len__` | Custom length (called by `len()`) |
| `__eq__` | Equality comparison (`==`) |
| `__lt__`, `__gt__` | Comparison operators (`<`, `>`) |
| `__add__`, `__sub__` | Arithmetic operators (`+`, `-`) |
| `__del__` | Destructor, called when object is deleted |

---

## 10. Constructors and Destructors

### 10.1 Constructors

The `__init__` method is called a constructor. It initializes the object's attributes.

```python
class Car:
    def __init__(self, brand, model):
        print("Constructor called!")
        self.brand = brand
        self.model = model

car = Car("Toyota", "Innova")  # Constructor called!
```

### 10.2 Destructors

The `__del__` method is called a destructor. It's invoked when an object is about to be destroyed.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
        print(f"{self.brand} car created")
    
    def __del__(self):
        print(f"{self.brand} car destroyed")

car1 = Car("Honda")    # Honda car created
car2 = car1
del car1               # Nothing printed yet (car2 still references it)
del car2               # Honda car destroyed
```

---

## 11. Comprehensive Example

Here's a complete example integrating all OOP concepts:

```python
from abc import ABC, abstractmethod

# Abstract base class (Abstraction)
class Employee(ABC):
    def __init__(self, emp_id, name, base_salary):
        self._emp_id = emp_id      # Protected attribute
        self.__name = name         # Private attribute
        self._base_salary = base_salary
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name:
            self.__name = new_name
    
    @abstractmethod
    def calculate_salary(self):    # Abstract method
        pass
    
    def display(self):
        return f"ID: {self._emp_id}, Name: {self.__name}"


# Regular employee (Inheritance)
class RegularEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, bonus):
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus
    
    def calculate_salary(self):    # Polymorphism (method overriding)
        return self._base_salary + self.bonus


# Contract employee (Inheritance)
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):    # Polymorphism
        return self.hourly_rate * self.hours_worked


# Using the classes
emp1 = RegularEmployee("E001", "Ankit", 50000, 10000)
emp2 = ContractEmployee("E002", "Sneha", 500, 80)

print(emp1.display())                     # Encapsulation via property
print(f"Salary: ₹{emp1.calculate_salary()}")  # ₹60000
print(emp2.display())
print(f"Salary: ₹{emp2.calculate_salary()}")  # ₹40000

# Demonstrating polymorphism
employees = [emp1, emp2]
print("\n--- All Employee Salaries ---")
for emp in employees:
    print(f"{emp.name}: ₹{emp.calculate_salary()}")
```

---

## 12. Exam Tips

1. **Understand the difference between class and instance attributes** — This is frequently tested in examinations.

2. **Know when to use instance, class, and static methods**:
   - Use instance methods when you need to work with instance data
   - Use class methods for factory methods or modifying class state
   - Use static methods for utility functions related to the class

3. **Encapsulation implementation** — Remember Python's naming conventions for private (`__`) and protected (`_`) members.

4. **Abstract classes cannot be instantiated** — Always remember this key point when answering questions about abstraction.

5. **MRO in multiple inheritance** — Understand how Python resolves method calls in complex inheritance hierarchies.

6. **Practice dunder methods** — Questions often ask about the output of code using special methods like `__str__`, `__repr__`, `__add__`, etc.

7. **super() function** — Know how to use `super()` to call parent class methods.

---

## 13. Multiple Choice Questions

### Question 1
What is the correct way to create a class named `Student` in Python?

a) `class Student:`
b) `class Student():`
c) `class Student:`
d) All of the above are correct

**Answer**: d) All of the above are correct. In Python, all three syntaxes create a class named Student.

---

### Question 2
Which method is called automatically when an object is created?

a) `__start__`
b) `__create__`
c) `__init__`
d) `__new__`

**Answer**: c) `__init__`

---

### Question 3
What is the output of the following code?

```python
class Test:
    x = 10
    
    def __init__(self):
        self.y = 20

obj1 = Test()
obj2 = Test()
obj1.y = 30
print(obj1.y, obj2.y)
```

a) `10 10`
b) `20 20`
c) `30 20`
d) `30 30`

**Answer**: c) `30 20` — `y` is an instance attribute, so changes to `obj1.y` don't affect `obj2.y`.

---

### Question 4
Which decorator is used to create a static method in Python?

a) `@static`
b) `@staticmethod`
c) `@static_method`
d) `@stat`

**Answer**: b) `@staticmethod`

---

### Question 5
What is the correct syntax to inherit class `B` from class `A`?

a) `class B inherits A:`
b) `class B(A):`
c) `class B extends A:`
d) `class B from A:`

**Answer**: b) `class B(A):`

---

## 14. Flashcards

### Flashcard 1
**Term**: Encapsulation
**Definition**: The bundling of data and methods into a single unit (class) while restricting direct access to some components using access specifiers.

---

### Flashcard 2
**Term**: Abstraction
**Definition**: The concept of hiding complex implementation details and showing only the necessary interface to the user, achieved through abstract classes and methods.

---

### Flashcard 3
**Term**: Polymorphism
**Definition**: The ability of objects of different classes to respond to the same method call in different ways. In Python, achieved through method overriding and duck typing.

---

### Flashcard 4
**Term**: Method Resolution Order (MRO)
**Definition**: The order in which Python searches for a method in the inheritance hierarchy when that method is called on an object.

---

### Flashcard 5
**Term**: Dunder Methods
**Definition**: Special methods in Python (like `__init__`, `__str__`, `__add__`) that begin and end with double underscores, used to define custom behavior for built-in operations.

---

## 15. Key Takeaways

1. **Classes and Objects**: Classes are blueprints; objects are concrete instances with identity, state, and behavior.

2. **Types of Attributes**: Instance attributes (unique per object) vs. class attributes (shared by all objects).

3. **Types of Methods**: Instance methods (use `self`), class methods (use `@classmethod` and `cls`), and static methods (use `@staticmethod`).

4. **Encapsulation**: Use `_protected` and `__private` conventions; implement getters/setters with `@property`.

5. **Abstraction**: Use `ABC` module and `@abstractmethod` to create abstract classes that cannot be instantiated.

6. **Polymorphism**: Achieved through method overriding and duck typing; operator overloading uses dunder methods.

7. **Inheritance**: Enables code reuse; understand single, multiple, and multilevel inheritance along with MRO.

8. **Special Methods**: `__init__`, `__str__`, `__repr__`, and other dunder methods customize object behavior.

9. **Best Practices**: Follow naming conventions, use encapsulation appropriately, and prefer composition over inheritance when appropriate.

10. **Real-world Application**: OOP principles are fundamental to building maintainable, scalable, and reusable software systems used in industry-standard applications.

---

*Prepared for BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*