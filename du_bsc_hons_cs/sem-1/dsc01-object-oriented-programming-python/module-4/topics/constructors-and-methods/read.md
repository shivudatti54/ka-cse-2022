# Constructors and Methods in Object-Oriented Programming (Python)

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Understanding Constructors in Python](#2-understanding-constructors-in-python)
3. [The `__init__` Method: Initialization with Default Parameters](#3-the-__init__-method-initialization-with-default-parameters)
4. [The `__new__` Method: Object Creation Mechanism](#4-the-__new__-method-object-creation-mechanism)
5. [Instance Methods, Class Methods, and Static Methods](#5-instance-methods-class-methods-and-static-methods)
6. [Method Overriding and Inheritance](#6-method-overriding-and-inheritance)
7. [Property Decorators and Getters/Setters](#7-property-decorators-and-getterssetters)
8. [Practical Examples and Real-World Applications](#8-practical-examples-and-real-world-applications)
9. [Self-Assessment: Multiple Choice Questions](#9-self-assessment-multiple-choice-questions)
10. [Flashcards for Quick Revision](#10-flashcards-for-quick-revision)
11. [Practice Exercises and Code Challenges](#11-practice-exercises-and-code-challenges)
12. [Key Takeaways](#12-key-takeaways)

---

## 1. Introduction and Real-World Relevance

### What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **objects** — data structures that contain both **data (attributes)** and **behavior (methods)**. Python, as a multi-paradigm language, fully supports OOP principles, making it essential for students to master these concepts.

### Why Constructors and Methods Matter

In real-world software development, constructors and methods form the backbone of any class-based system:

- **Constructors** ensure objects are properly initialized with valid state from the moment they are created
- **Methods** define the behavior that objects can perform, encapsulating business logic
- Together, they enable **encapsulation**, **abstraction**, and **code reusability** — fundamental OOP principles

### Real-World Analogy

Consider a **Bank Account** system:

- The **constructor** (`__init__`) is like opening a new account — it sets up the initial balance, account holder name, and account number
- **Methods** like `deposit()`, `withdraw()`, and `check_balance()` define what operations can be performed on the account
- **Class methods** might be used for operations that apply to all accounts (e.g., calculating total interest rate)
- **Static methods** might perform utility functions like validating account numbers

This unit aligns with **Unit-III: Object-Oriented Programming** of the Delhi University NEP 2024 syllabus for BSc (Hons) Computer Science.

---

## 2. Understanding Constructors in Python

### What is a Constructor?

A **constructor** is a special method that is automatically invoked when an object (instance) of a class is created. Its primary purpose is to **initialize the object's attributes** and set up the initial state.

In Python, the constructor is defined using the `__init__` method (also called the **initializer**).

### Syntax of `__init__`

```python
class ClassName:
    def __init__(self, parameters):
        # Initialization code
        self.attribute = parameters
```

### Key Points About `__init__`

- `__init__` is **not** the actual constructor (it's the initializer)
- The actual constructor in Python is `__new__` (covered in Section 4)
- `__init__` **cannot** return a value other than `None`
- The first parameter is always `self`, which refers to the newly created instance
- It is automatically called after `__new__` completes object creation

### Example 1: Basic Constructor

```python
class Student:
    """A class to represent a student at Delhi University"""
    
    def __init__(self, name, roll_number, course):
        # Initialize instance attributes
        self.name = name
        self.roll_number = roll_number
        self.course = course
        self.attendance = 0
    
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Course: {self.course}")
        print(f"Attendance: {self.attendance}%")

# Creating objects
student1 = Student("Aisha Khan", "DU/2024/CS/001", "BSc Hons Computer Science")
student2 = Student("Rahul Sharma", "DU/2024/CS/002", "BSc Hons Mathematics")

student1.display_info()
```

**Output:**
```
Student Name: Aisha Khan
Roll Number: DU/2024/CS/001
Course: BSc Hons Computer Science
Attendance: 0%
```

---

## 3. The `__init__` Method: Initialization with Default Parameters

### Default Parameters in Constructors

Python allows constructors to have **default parameter values**, which provide fallback values when arguments are not explicitly provided. This adds flexibility and makes code more robust.

### Example 2: Constructor with Default Parameters

```python
class BankAccount:
    """A class representing a bank account with default parameters"""
    
    def __init__(self, account_holder, account_number, balance=0.0, account_type="Savings"):
        # Required parameters
        self.account_holder = account_holder
        self.account_number = account_number
        
        # Default parameters
        self.balance = balance
        self.account_type = account_type
        self.transaction_history = []
    
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ₹{self.balance:.2f}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ₹{amount}")
            print(f"Successfully deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: ₹{amount}")
            print(f"Successfully withdrawn ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount!")

# Creating accounts with different parameter combinations
account1 = BankAccount("Priya Singh", "SB1234567890")  # Uses all defaults
account2 = BankAccount("Amit Kumar", "SB9876543210", 50000, "Current")  # No defaults
account3 = BankAccount("Neha Reddy", "SB5555555555", balance=25000)  # Only balance specified

print("=== Account 1 (All defaults) ===")
account1.display_account_info()

print("\n=== Account 2 (No defaults) ===")
account2.display_account_info()

print("\n=== Account 3 (Partial defaults) ===")
account3.display_account_info()

# Performing transactions
account1.deposit(10000)
account1.withdraw(2500)
```

### Constructor Overloading in Python

Python does not support **true constructor overloading** (multiple `__init__` methods with different signatures) like Java or C++. However, we can achieve similar functionality using:

1. **Default arguments**
2. **`*args` and `**kwargs`**
3. **Class methods as alternative constructors**

### Example 3: Simulating Constructor Overloading

```python
class Rectangle:
    """A class demonstrating flexible initialization"""
    
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            # No arguments: create a default square
            self.length = 1
            self.width = 1
        elif len(args) == 1:
            # Single argument: create a square
            self.length = args[0]
            self.width = args[0]
        elif len(args) == 2:
            # Two arguments: create rectangle
            self.length = args[0]
            self.width = args[1]
        else:
            raise ValueError("Rectangle accepts 0, 1, or 2 arguments")
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Using different "overloaded" forms
rect1 = Rectangle()           # Default square
rect2 = Rectangle(5)           # Square with side 5
rect3 = Rectangle(4, 6)        # Rectangle 4x6

print(f"rect1 area: {rect1.area()}, perimeter: {rect1.perimeter()}")
print(f"rect2 area: {rect2.area()}, perimeter: {rect2.perimeter()}")
print(f"rect3 area: {rect3.area()}, perimeter: {rect3.perimeter()}")
```

---

## 4. The `__new__` Method: Object Creation Mechanism

### Understanding `__new__`

The `__new__` method is the **actual constructor** in Python. It is responsible for **creating and returning a new instance** of the class. While `__init__` initializes the instance, `__new__` creates it.

### When to Use `__new__`

- Implementing **Singleton pattern**
- Creating **immutable classes**
- Subclassing **immutable types** (str, int, tuple)
- Customizing object creation process

### Example 4: Singleton Pattern with `__new__`

```python
class DatabaseConnection:
    """Singleton pattern implementation using __new__"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection_string = "localhost:5432/mydb"
            cls._instance.connected = False
        else:
            print("Using existing database connection...")
        return cls._instance
    
    def connect(self):
        if not self.connected:
            print(f"Connecting to: {self.connection_string}")
            self.connected = True
        else:
            print("Already connected!")
    
    def disconnect(self):
        if self.connected:
            print("Disconnecting from database...")
            self.connected = False
        else:
            print("Not connected!")

# Testing singleton behavior
conn1 = DatabaseConnection()
conn2 = DatabaseConnection()

print(f"conn1 is conn2: {conn1 is conn2}")  # True - same instance

conn1.connect()
conn2.connect()  # Will show "Already connected!"
```

### Example 5: Subclassing Immutable Types

```python
class TripledNumber(int):
    """A custom integer that triples its value"""
    
    def __new__(cls, value):
        # Multiply the value by 3 for immutable types
        instance = super(TripledNumber, cls).__new__(cls, value * 3)
        return instance

# Creating tripled numbers
num1 = TripledNumber(5)    # Results in 15
num2 = TripledNumber(10)   # Results in 30

print(f"TripledNumber(5): {num1}")    # 15
print(f"TripledNumber(10): {num2}")   # 30
print(f"Type: {type(num1)}")          # <class '__main__.TripledNumber'>
```

---

## 5. Instance Methods, Class Methods, and Static Methods

### Overview of Method Types

Python supports three types of methods within classes:

| Method Type | Decorator | First Parameter | Called On |
|-------------|-----------|-----------------|-----------|
| Instance Method | None | `self` | Instance (object) |
| Class Method | `@classmethod` | `cls` | Class itself |
| Static Method | `@staticmethod` | None | Class or instance |

### Instance Methods

Instance methods are the most common type. They operate on **instance attributes** and require `self` as the first parameter.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, increment):
        """Instance method: operates on instance data"""
        self.speed += increment
        return self.speed
    
    def brake(self, decrement):
        """Instance method: modifies instance state"""
        self.speed = max(0, self.speed - decrement)
        return self.speed
```

### Class Methods

Class methods receive the **class itself** as the first parameter (`cls`). They can:

- Access or modify class-level attributes
- Create alternative constructors
- Provide factory methods

### Example 6: Class Method as Alternative Constructor

```python
class Employee:
    """Class demonstrating class methods and alternative constructors"""
    
    # Class variable (shared by all instances)
    company_name = "Tech Solutions Pvt Ltd"
    employee_count = 0
    
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self):
        print(f"Employee: {self.name}, ID: {self.emp_id}, Salary: ₹{self.salary}")
    
    @classmethod
    def from_string(cls, emp_string):
        """Alternative constructor: creates Employee from string"""
        name, emp_id, salary = emp_string.split(",")
        return cls(name.strip(), emp_id.strip(), float(salary.strip()))
    
    @classmethod
    def update_company_name(cls, new_name):
        """Class method: modifies class-level attribute"""
        cls.company_name = new_name
    
    @classmethod
    def get_employee_count(cls):
        """Class method: accesses class-level attribute"""
        return cls.employee_count

# Using normal constructor
emp1 = Employee("Dr. Sarah Johnson", "DU/EMP/001", 75000)

# Using class method as alternative constructor
emp2 = Employee.from_string("Prof. Amit Singh, DU/EMP/002, 85000")

print(f"Company: {Employee.company_name}")
print(f"Total Employees: {Employee.get_employee_count()}")

emp1.display_info()
emp2.display_info()
```

### Static Methods

Static methods don't receive `self` or `cls` as the first parameter. They are essentially **regular functions** that are logically related to the class. Use them when:

- The method doesn't need access to class or instance data
- The method is a utility function related to the class

### Example 7: Static Methods for Validation

```python
class BankAccount:
    """Class demonstrating static methods for validation"""
    
    MINIMUM_BALANCE = 500
    MAX_WITHDRAWAL = 100000
    
    def __init__(self, account_number, holder_name, initial_balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
    
    @staticmethod
    def validate_account_number(account_number):
        """Static method: validates account number format"""
        if len(account_number) == 12 and account_number.isdigit():
            return True
        return False
    
    @staticmethod
    def validate_amount(amount):
        """Static method: validates transaction amount"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return True
    
    def withdraw(self, amount):
        self.validate_amount(amount)  # Can call static method on instance
        if amount > self.MAX_WITHDRAWAL:
            raise ValueError(f"Cannot withdraw more than ₹{self.MAX_WITHDRAWAL}")
        if self.balance - amount < self.MINIMUM_BALANCE:
            raise ValueError(f"Cannot withdraw. Minimum balance of ₹{self.MINIMUM_BALANCE} required")
        self.balance -= amount
        return self.balance

# Using static methods
print(f"Valid account number: {BankAccount.validate_account_number('123456789012')}")
print(f"Invalid account number: {BankAccount.validate_account_number('12345')}")
```

---

## 6. Method Overriding and Inheritance

### Understanding Inheritance

**Inheritance** is an OOP principle where a class (child/subclass) can inherit attributes and methods from another class (parent/superclass). This promotes code reusability and establishes a natural hierarchy.

### Method Overriding

**Method overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. The overriding method must have the **same signature** as the parent method.

### Example 8: Inheritance and Method Overriding

```python
# Parent class
class Person:
    """Base class for all people at the university"""
    
    def __init__(self, name, age, university="Delhi University"):
        self.name = name
        self.age = age
        self.university = university
    
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, studying at {self.university}"
    
    def study(self):
        return f"{self.name} is studying..."

# Child class 1: Student
class Student(Person):
    """Student class inheriting from Person"""
    
    def __init__(self, name, age, course, year):
        # Call parent constructor using super()
        super().__init__(name, age)
        self.course = course
        self.year = year
        self.grades = {}
    
    # Method overriding
    def introduce(self):
        return f"I am {self.name}, a {self.year} year {self.course} student"
    
    # Specific to Student class
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
    
    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

# Child class 2: Professor
class Professor(Person):
    """Professor class inheriting from Person"""
    
    def __init__(self, name, age, department, specialization):
        super().__init__(name, age)
        self.department = department
        self.specialization = specialization
        self.publications = 0
    
    # Method overriding
    def introduce(self):
        return f"I am Prof. {self.name}, teaching at the Department of {self.department}"
    
    # Specific to Professor class
    def publish_research(self):
        self.publications += 1
        return f"{self.name} published a paper! Total: {self.publications}"

# Demonstrating polymorphism
people = [
    Student("Aisha", 20, "BSc Hons Computer Science", 2),
    Professor("Dr. Sharma", 45, "Computer Science", "Machine Learning"),
    Person("Guest", 30)
]

for person in people:
    print(person.introduce())
    print(person.study() if isinstance(person, Student) else f"{person.name} teaches...")
    print("-" * 50)
```

### The `super()` Function

The `super()` function is crucial for:

- Calling parent class constructors
- Calling parent class methods
- Avoiding directly referencing the parent class

### Example 9: Multi-Level Inheritance

```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor: {name}")

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)  # Call Person's __init__
        self.roll_no = roll_no
        print(f"Student constructor: {roll_no}")

class ResearchStudent(Student):
    def __init__(self, name, roll_no, thesis_topic):
        super().__init__(name, roll_no)  # Call Student's __init__
        self.thesis_topic = thesis_topic
        print(f"ResearchStudent constructor: {thesis_topic}")

# Multi-level inheritance demonstration
researcher = ResearchStudent("Karthik", "DU/PHD/2024/001", "Quantum Computing")
print(f"\nName: {researcher.name}")
print(f"Roll No: {researcher.roll_no}")
print(f"Thesis: {researcher.thesis_topic}")
```

---

## 7. Property Decorators and Getters/Setters

### The `@property` Decorator

In Python, the `@property` decorator allows you to define methods that behave like **attributes**. This provides a cleaner way to implement getters and setters compared to traditional approaches.

### Why Use Properties?

- **Encapsulation**: Control access to private attributes
- **Validation**: Add validation logic when setting values
- **Computed Attributes**: Calculate values on-the-fly
- **Backward Compatibility**: Change internal implementation without breaking existing code

### Example 10: Property Decorators

```python
class Temperature:
    """Class demonstrating property decorators"""
    
    def __init__(self, celsius=0):
        # Private attribute (by convention, using underscore)
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property: converts Celsius to Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for Fahrenheit (converts to Celsius)"""
        self._celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Computed property: converts Celsius to Kelvin"""
        return self._celsius + 273.15

# Using properties
temp = Temperature(25)

print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

# Using setter
temp.celsius = 30
print(f"\nAfter setting celsius to 30:")
print(f"Fahrenheit: {temp.fahrenheit}°F")

# Using fahrenheit setter
temp.fahrenheit = 212
print(f"\nAfter setting fahrenheit to 212:")
print(f"Celsius: {temp.celsius}°C")

# Validation example
try:
    temp.celsius = -300
except ValueError as e:
    print(f"\nError: {e}")
```

---

## 8. Practical Examples and Real-World Applications

### Example 11: Complete E-Commerce System

```python
class Product:
    """Base class for products in an e-commerce system"""
    
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self._name = name
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    def apply_discount(self, percentage):
        """Apply discount to the product"""
        discount_amount = self._price * (percentage / 100)
        self._price -= discount_amount
        return self._price

class ElectronicProduct(Product):
    """Electronic products with warranty"""
    
    def __init__(self, product_id, name, price, warranty_months):
        super().__init__(product_id, name, price)
        self.warranty_months = warranty_months
    
    def get_warranty_status(self):
        return f"Warranty: {self.warranty_months} months"

class ShoppingCart:
    """Shopping cart to manage products"""
    
    def __init__(self):
        self._items = {}  # product_id: quantity
    
    def add_item(self, product, quantity=1):
        if product.product_id in self._items:
            self._items[product.product_id]['quantity'] += quantity
        else:
            self._items[product.product_id] = {'product': product, 'quantity': quantity}
    
    def remove_item(self, product_id):
        if product_id in self._items:
            del self._items[product_id]
    
    def calculate_total(self):
        total = 0
        for item in self._items.values():
            total += item['product'].price * item['quantity']
        return total
    
    def display_cart(self):
        print("\n=== Shopping Cart ===")
        for item in self._items.values():
            p = item['product']
            q = item['quantity']
            print(f"{p.name} x {q} = ₹{p.price * q}")
        print(f"Total: ₹{self.calculate_total()}")

# Creating products
laptop = ElectronicProduct("ELEC001", "Dell Laptop", 50000, 24)
phone = ElectronicProduct("ELEC002", "iPhone 15", 80000, 12)

# Using the shopping cart
cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(phone, 2)

cart.display_cart()

# Applying discount on one item
laptop.apply_discount(10)
print(f"\nAfter 10% discount on laptop:")
cart.display_cart()
```

---

## 9. Self-Assessment: Multiple Choice Questions

### Section A: Basic Concepts

**Question 1:** What is the primary purpose of the `__init__` method in Python?

- (a) To create a new instance of a class
- (b) To initialize the instance attributes
- (c) To delete the object
- (d) To inherit from another class

**Question 2:** Which method is the actual constructor in Python?

- (a) `__init__`
- (b) `__new__`
- (c) `__create__`
- (d) `__construct__`

**Question 3:** What does `self` refer to in an instance method?

- (a) The class itself
- (b) The current instance
- (c) The parent class
- (d) A global variable

**Question 4:** Which decorator is used to define a class method?

- (a) `@staticmethod`
- (b) `@property`
- (c) `@classmethod`
- (d) `@instance`

### Section B: Intermediate Concepts

**Question 5:** What is the first parameter of a class method?

- (a) `self`
- (b) `this`
- (c) `cls`
- (d) `class`

**Question 6:** In method overriding, the overriding method must have:

- (a) Different parameters
- (b) The same name and parameters
- (c) No parameters
- (d) Only `self` parameter

**Question 7:** What is the purpose of the `super()` function?

- (a) To create a super object
- (b) To call parent class methods
- (c) To define a superclass
- (d) To make a class superior

**Question 8:** Which method is called when you access an attribute using `@property`?

- (a) setter
- (b) deleter
- (c) getter
- (d) accessor

### Section C: Advanced Concepts

**Question 9:** What design pattern is commonly implemented using `__new__`?

- (a) Observer Pattern
- (b) Factory Pattern
- (c) Singleton Pattern
- (d) Adapter Pattern

**Question 10:** Static methods in Python:

- (a) Receive `self` as parameter
- (b) Receive `cls` as parameter
- (c) Cannot access class attributes
- (d) Are called on the class itself

**Question 11:** What is polymorphism in OOP?

- (a) Multiple inheritance
- (b) Methods with same name doing different things
- (c) Creating multiple objects
- (d) Hiding implementation details

**Question 12:** Which method is automatically called when an object is created?

- (a) `__new__` only
- (b) `__init__` only
- (c) Both `__new__` and `__init__`
- (d) Neither

**Question 13:** What happens if a subclass defines `__init__` without calling `super().__init__`?

- (a) The parent initialization is automatically called
- (b) The parent initialization is skipped
- (c) An error occurs
- (d) The class cannot be instantiated

**Question 14:** The `@property` decorator allows:

- (a) Making attributes read-only
- (b) Adding validation logic
- (c) Computing values dynamically
- (d) All of the above

**Question 15:** Default parameters in `__init__` are evaluated:

- (a) At function definition time
- (b) At function call time
- (c) Never
- (d) At class definition time

---

### Answer Key

1. (b) 2. (b) 3. (b) 4. (c) 5. (c) 6. (b) 7. (b) 8. (c)
9. (c) 10. (c) 11. (b) 12. (c) 13. (b) 14. (d) 15. (a)

---

## 10. Flashcards for Quick Revision

### Flashcard Set 1: Constructor Concepts

| Term | Definition |
|------|------------|
| **Constructor** | Special method called automatically when an object is created to initialize the object's state |
| **`__init__`** | Initializer method in Python that sets up instance attributes (not a true constructor) |
| **`__new__`** | The actual constructor method that creates and returns a new instance |
| **`self`** | Reference to the current instance of the class within instance methods |
| **Default Parameters** | Predefined values in constructor that are used when no argument is provided |

### Flashcard Set 2: Method Types

| Term | Definition |
|------|------------|
| **Instance Method** | Method that operates on instance attributes; first parameter is `self` |
| **Class Method** | Method that operates on class-level attributes; first parameter is `cls`; decorated with `@classmethod` |
| **Static Method** | Utility function related to the class but doesn't access class/instance data; decorated with `@staticmethod` |
| **Method Overriding** | When a subclass provides a specific implementation of a method already defined in its parent class |
| **`super()`** | Built-in function that allows calling methods from the parent class |

### Flashcard Set 3: Advanced Concepts

| Term | Definition |
|------|------------|
| **Singleton Pattern** | Design pattern ensuring only one instance of a class exists; implemented using `__new__` |
| **Property Decorator** | `@property` decorator that allows methods to be accessed like attributes |
| **Getter** | Method that returns the value of a private attribute |
| **Setter** | Method that sets the value of a private attribute, often with validation |
| **Encapsulation** | OOP principle of bundling data and methods that operate on data within a single unit |

### Flashcard Set 4: Inheritance

| Term | Definition |
|------|------------|
| **Inheritance** | OOP concept where a class inherits attributes and methods from another class |
| **Subclass/Child Class** | Class that inherits from another class |
| **Superclass/Parent Class** | Class whose attributes and methods are inherited |
| **Multi-level Inheritance** | Inheritance chain where a class inherits from a class that itself inherits from another |
| **Polymorphism** | Ability of different classes to respond to the same method call in different ways |

---

## 11. Practice Exercises and Code Challenges

### Exercise 1: University Management System

**Problem:** Create a class hierarchy for a university system with `Person` → `Student` → `ResearchStudent`. Include:

- Constructor with default parameters for optional fields
- Instance methods for common operations
- Class methods for statistics
- Static methods for validation

```python
# Starter code
class Person:
    def __init__(self, name, age, email=None):
        # Implement
        pass

# Your task: Complete Student and ResearchStudent
```

### Exercise 2: Library Book Management

**Problem:** Implement a `Book` class with:

- Properties for title, author, and ISBN
- Validation in setters (ISBN must be 10 or 13 digits)
- Class method to count total books
- Static method to validate ISBN format

### Exercise 3: Bank Account with Inheritance

**Problem:** Create a banking system with:

- Base `Account` class with basic operations
- `SavingsAccount` with interest calculation
- `CurrentAccount` with overdraft facility
- Method overriding for withdrawal logic

### Code Challenge: Implement a Singleton Logger

**Challenge:** Create a Logger class using `__new__` that:

- Ensures only one instance exists
- Tracks all log messages with timestamps
- Provides methods for different log levels (INFO, WARNING, ERROR)

### Code Challenge: Flexible Employee Factory

**Challenge:** Create an Employee system where:

- Regular employees are created with normal constructor
- Contract employees are created via class method
- Interns are created via static method
- All return the same type of object but with different default values

---

## 12. Key Takeaways

### Constructors

1. **`__init__`** is the initializer, not the true constructor
2. **`__new__`** is the actual constructor that creates objects
3. Default parameters provide flexibility and backward compatibility
4. `__init__` cannot return a value (except `None`)

### Methods

5. **Instance methods** operate on instance data via `self`
6. **Class methods** operate on class data via `cls`; use `@classmethod`
7. **Static methods** are utility functions; use `@staticmethod`
8. **Properties** (`@property`) provide controlled access to attributes

### Inheritance & Polymorphism

9. **Inheritance** promotes code reuse through parent-child relationships
10. **Method overriding** allows subclasses to provide specific implementations
11. **`super()`** is essential for accessing parent class functionality
12. **Polymorphism** enables the same interface for different object types

### Best Practices

13. Use meaningful names for attributes and methods
14. Validate input in setters and constructors
15. Prefer composition over inheritance when appropriate
16. Document your classes with docstrings
17. Use properties for encapsulation rather than direct attribute access

### Delhi University Syllabus Alignment

This content covers:
- Unit-III: Object-Oriented Programming concepts
- Constructor and method types
- Inheritance and polymorphism
- Practical implementation patterns
- Preparation for practical examinations and theory papers

---

*Study material prepared for BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*