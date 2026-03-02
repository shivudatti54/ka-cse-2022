# Abstraction and Encapsulation in Object-Oriented Programming (Python)

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction](#introduction)
2. [Understanding Abstraction](#understanding-abstraction)
3. [Understanding Encapsulation](#understanding-encapsulation)
4. [The @property Decorator](#the-property-decorator)
5. [Name Mangling in Python](#name-mangling-in-python)
6. [Data Classes](#data-classes)
7. [Abstraction vs Encapsulation: A Comparative Analysis](#abstraction-vs-encapsulation-a-comparative-analysis)
8. [Practical Use Cases](#practical-use-cases)
9. [Delhi University Syllabus Context](#delhi-university-syllabus-context)
10. [Key Takeaways](#key-takeaways)
11. [Multiple Choice Questions (MCQs)](#multiple-choice-questions-mcqs)
12. [Flashcards](#flashcards)

---

## Introduction

In the realm of Object-Oriented Programming (OOP), **Abstraction** and **Encapsulation** serve as fundamental pillars that enable developers to build maintainable, scalable, and reusable software systems. These concepts, while distinct, often work in tandem to create robust applications.

### Real-World Relevance

Consider a modern smartphone: you interact with a simplified interface (touchscreen, apps) without needing to understand the complex circuitry, processor architecture, or operating system internals. This is **abstraction** — hiding complexity behind a simple interface. Similarly, the internal components are protected within the phone's casing, preventing external interference — this exemplifies **encapsulation**.

In software development, these principles help us:

- **Manage complexity** by exposing only necessary details
- **Protect data integrity** through controlled access
- **Create reusable components** that can be easily maintained
- **Achieve loose coupling** between different parts of a system

For BSc (Hons) Computer Science students at Delhi University, mastering these concepts is essential for building enterprise-level applications and understanding modern software architecture patterns.

---

## Understanding Abstraction

### What is Abstraction?

**Abstraction** is the process of hiding complex implementation details and exposing only the essential features of an object. It focuses on **what** an object does rather than **how** it does it. In Python, abstraction is achieved through:

1. **Abstract Base Classes (ABC)** — Classes that cannot be instantiated directly and may contain abstract methods
2. **Abstract Methods** — Methods declared but not implemented; must be overridden by subclasses

### The ABC Module

Python provides the `abc` (Abstract Base Classes) module to implement abstraction. The key components are:

- `ABC` — A class that marks its subclasses as abstract
- `@abstractmethod` — A decorator that marks a method as abstract

### Example 1: Abstract Class for Payment Processing

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processing systems"""
    
    def __init__(self, amount: float):
        self.amount = amount
    
    @abstractmethod
    def process_payment(self) -> str:
        """Process the payment - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def refund_payment(self) -> str:
        """Refund the payment - must be implemented by subclasses"""
        pass
    
    def display_amount(self):
        """A concrete method - has default implementation"""
        return f"Amount: ${self.amount:.2f}"


class CreditCardPayment(PaymentProcessor):
    """Concrete implementation for credit card payments"""
    
    def __init__(self, amount: float, card_number: str):
        super().__init__(amount)
        self.card_number = card_number
    
    def process_payment(self) -> str:
        # Complex logic hidden behind simple interface
        return f"Processing credit card payment of ${self.amount:.2f} for card ending in {self.card_number[-4:]}"
    
    def refund_payment(self) -> str:
        return f"Refunding ${self.amount:.2f} to credit card ending in {self.card_number[-4:]}"


class UPIPayment(PaymentProcessor):
    """Concrete implementation for UPI payments"""
    
    def __init__(self, amount: float, upi_id: str):
        super().__init__(amount)
        self.upi_id = upi_id
    
    def process_payment(self) -> str:
        return f"Processing UPI payment of ${self.amount:.2f} via {self.upi_id}"
    
    def refund_payment(self) -> str:
        return f"Refunding ${self.amount:.2f} to {self.upi_id}"


# Usage
payments = [
    CreditCardPayment(1500.00, "4532123456789012"),
    UPIPayment(250.00, "john@upi")
]

for payment in payments:
    print(payment.process_payment())
    print(payment.display_amount())
    print("-" * 50)
```

**Output:**
```
Processing credit card payment of $1500.00 for card ending in 9012
Amount: $1500.00
--------------------------------------------------
Processing UPI payment of $250.00 via john@upi
Amount: $250.00
--------------------------------------------------
```

### Why Use Abstraction?

1. **Code Reusability**: Common interfaces can be shared across multiple implementations
2. **Loose Coupling**: Client code depends on abstraction, not concrete implementations
3. **Flexibility**: Easy to add new payment methods without changing existing code
4. **Enforcement**: Ensures subclasses implement required methods

---

## Understanding Encapsulation

### What is Encapsulation?

**Encapsulation** is the bundling of data (attributes) and methods (functions) into a single unit (class), while restricting direct access to some of an object's components. It protects the internal state of an object from unintended modifications and ensures data integrity.

### Access Modifiers in Python

Python uses **convention-based privacy** rather than strict access modifiers found in languages like Java or C++. This is a key distinction that students must understand:

| Modifier | Convention | Description |
|----------|------------|-------------|
| `public` | No underscore | Accessible everywhere (default) |
| `_protected` | Single underscore | Convention for internal use (name mangling applies in subclasses) |
| `__private` | Double underscore | Name mangling applied for strong privacy |

### Example 2: Bank Account with Encapsulation

```python
class BankAccount:
    """
    A class demonstrating encapsulation in Python.
    Shows different levels of data protection.
    """
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        # Public attributes
        self.account_holder = name
        self.account_number = self._generate_account_number()
        
        # Protected attribute (convention: internal use)
        self._transaction_history = []
        
        # Private attribute (name mangling applied)
        self.__balance = initial_balance
    
    def _generate_account_number(self) -> str:
        """Protected method to generate account number"""
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def deposit(self, amount: float) -> bool:
        """Public method to deposit money"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.__balance += amount
        self._transaction_history.append(f"Deposited: ${amount:.2f}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """Public method to withdraw money"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        
        self.__balance -= amount
        self._transaction_history.append(f"Withdrew: ${amount:.2f}")
        return True
    
    def get_balance(self) -> float:
        """Getter method to access private balance"""
        return self.__balance
    
    def get_transaction_history(self):
        """Getter for transaction history"""
        return self._transaction_history.copy()  # Return a copy for safety


# Create account
account = BankAccount("Rahul Sharma", 10000.00)

# Accessing public attributes
print(f"Account Holder: {account.account_holder}")
print(f"Account Number: {account.account_number}")

# Accessing through methods (controlled access)
print(f"Current Balance: ${account.get_balance():.2f}")

# Perform transactions
account.deposit(5000.00)
account.withdraw(2000.00)

print(f"New Balance: ${account.get_balance():.2f}")
print(f"Transaction History: {account.get_transaction_history()}")

# Attempting to access private attribute directly (will fail)
try:
    print(account.__balance)  # This raises AttributeError
except AttributeError as e:
    print(f"\nError: Cannot access private attribute directly - {e}")
```

---

## The @property Decorator

The `@property` decorator provides a Pythonic way to implement getters and setters while maintaining the simplicity of attribute access. This is essential for encapsulating data validation and computed properties.

### Example 3: Employee Class with @property

```python
class Employee:
    """Demonstrates the use of @property decorator for encapsulation"""
    
    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = salary  # Private attribute
    
    # Getter using @property
    @property
    def salary(self) -> float:
        """Get the employee's salary"""
        return self.__salary
    
    # Setter using @property.setter
    @salary.setter
    def salary(self, new_salary: float):
        """Set salary with validation"""
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        if new_salary > 10000000:  # 1 crore
            raise ValueError("Salary exceeds maximum allowed")
        self.__salary = new_salary
    
    # Deleter using @property.deleter
    @salary.deleter
    def salary(self):
        print("Deleting salary data...")
        del self.__salary
    
    # Computed property
    @property
    def annual_salary(self) -> float:
        """Calculate annual salary (computed property)"""
        return self.__salary * 12
    
    @property
    def tax(self) -> float:
        """Calculate tax (10% for demonstration)"""
        return self.__salary * 0.10


# Usage
emp = Employee("Priya Singh", 50000.00)

# Access like an attribute, but actually calls the getter
print(f"Monthly Salary: ₹{emp.salary:,.2f}")
print(f"Annual Salary: ₹{emp.annual_salary:,.2f}")
print(f"Tax Deduction: ₹{emp.tax:,.2f}")

# Update using setter (with validation)
emp.salary = 75000.00
print(f"Updated Monthly Salary: ₹{emp.salary:,.2f}")

# Attempting invalid salary
try:
    emp.salary = -10000
except ValueError as e:
    print(f"Error: {e}")

# Deleting salary
del emp.salary
```

### Benefits of @property Decorator

1. **Clean API**: Users access attributes naturally without knowing they're calling methods
2. **Validation**: Setter can enforce rules before modifying data
3. **Computed Properties**: Dynamically calculate values when accessed
4. **Backward Compatibility**: Convert attributes to properties without changing the API

---

## Name Mangling in Python

Python implements a form of privacy through **name mangling**. When you prefix an attribute with double underscores (`__`), Python automatically changes the name to include the class name.

### Example 4: Understanding Name Mangling

```python
class SecureData:
    """Class demonstrating name mangling"""
    
    def __init__(self):
        self.public_data = "Accessible anywhere"
        self._protected_data = "Internal use only"
        self.__private_data = "Hidden from outside"
    
    def reveal_private(self):
        """Method that can access private data"""
        return f"Private data: {self.__private_data}"
    
    def get_mangled_name(self):
        """Shows how Python mangles the name"""
        return f"Mangled name: {self.__private_data}"


obj = SecureData()

# Public access works
print(obj.public_data)
print(obj._protected_data)  # Warning, but accessible

# Accessing private directly - Python mangles the name
print(f"After name mangling: {obj._SecureData__private_data}")

# Through method
print(obj.reveal_private())

# What happens with inheritance?
class AdvancedSecureData(SecureData):
    """Inherited class - check if it can access private data"""
    
    def access_parent_private(self):
        # This will create its own __private_data, not access parent's
        # Each class gets its own mangled attribute
        try:
            return self.__private_data
        except AttributeError:
            return "Cannot access parent private data directly"


# Test inheritance
child = AdvancedSecureData()
print(f"\n{child.reveal_private()}")  # Parent's method still works
print(f"Child's own private: {child._AdvancedSecureData__private_data}")
```

### When to Use Name Mangling

- **Framework code**: Where you want to prevent accidental attribute access
- **API libraries**: To protect internal implementation details
- **Name collision prevention**: In complex inheritance hierarchies

**Note**: Name mangling is not a security feature; it's a convention to prevent accidental access. For true security, use different mechanisms.

---

## Data Classes

Introduced in Python 3.7, **Data Classes** provide a convenient way to create classes that primarily store data. They automatically generate special methods like `__init__`, `__repr__`, `__eq__`, and more.

### Example 5: Using Data Classes for Encapsulation

```python
from dataclasses import dataclass, field
from typing import List
import datetime

@dataclass
class Student:
    """
    Data class representing a student.
    Combines abstraction with clean data representation.
    """
    name: str
    roll_number: str
    marks: List[float] = field(default_factory=list)
    _attendance: int = 0  # Protected field
    
    @property
    def average_marks(self) -> float:
        """Calculate average marks (computed property)"""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)
    
    @property
    def grade(self) -> str:
        """Determine grade based on average"""
        avg = self.average_marks
        if avg >= 90: return 'A+'
        elif avg >= 80: return 'A'
        elif avg >= 70: return 'B+'
        elif avg >= 60: return 'B'
        elif avg >= 50: return 'C'
        else: return 'F'
    
    @property
    def attendance(self) -> int:
        return self._attendance
    
    @attendance.setter
    def attendance(self, value: int):
        if not 0 <= value <= 100:
            raise ValueError("Attendance must be between 0 and 100")
        self._attendance = value
    
    def add_marks(self, marks: float):
        """Add marks with validation"""
        if 0 <= marks <= 100:
            self.marks.append(marks)
        else:
            raise ValueError("Marks must be between 0 and 100")


# Usage
student = Student(
    name="Ananya Gupta",
    roll_number="CS/2024/001"
)

# Adding marks
student.add_marks(85.5)
student.add_marks(92.0)
student.add_marks(78.5)

# Setting attendance
student.attendance = 95

# Display
print(student)
print(f"Name: {student.name}")
print(f"Average Marks: {student.average_marks:.2f}")
print(f"Grade: {student.grade}")
print(f"Attendance: {student.attendance}%")

# Comparison works automatically
student2 = Student(
    name="Ananya Gupta",
    roll_number="CS/2024/001"
)

print(f"\nAre they equal? {student == student2}")  # True, because of __eq__
```

### Key Features of Data Classes

| Feature | Description |
|---------|-------------|
| `@dataclass` | Decorator that generates boilerplate code |
| `field(default=...)` | Default values for attributes |
| `field(default_factory=...)` | For mutable defaults (like lists) |
| `frozen=True` | Makes instances immutable |
| Auto `__repr__` | Nice string representation |
| Auto `__eq__` | Value-based equality |

---

## Abstraction vs Encapsulation: A Comparative Analysis

Understanding the difference between these two fundamental concepts is crucial:

| Aspect | Abstraction | Encapsulation |
|--------|-------------|---------------|
| **Focus** | Hiding complexity | Bundling data with methods |
| **Level** | Design level | Implementation level |
| **Purpose** | Show only necessary parts | Protect data and methods |
| **How** | Using abstract classes | Using access modifiers |
| **Example** | `PaymentProcessor` interface | `BankAccount.__balance` |
| **Question** | "What can an object do?" | "How is data protected?" |

### Analogy

- **Abstraction** is like the **blueprint** of a car — it shows what features the car will have
- **Encapsulation** is like the **engine compartment** — the engine is hidden and protected, but the car works as a complete unit

---

## Practical Use Cases

### Use Case 1: E-Commerce Platform

```python
from abc import ABC, abstractmethod

class Product(ABC):
    """Abstract representation of a product"""
    
    @abstractmethod
    def get_price(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass

class EncapsulatedProduct:
    """
    Encapsulated product with validation and logic
    """
    def __init__(self, name: str, base_price: float, category: str):
        self.name = name
        self.__base_price = base_price
        self.__category = category
        self.__discount = 0.0
    
    @property
    def final_price(self) -> float:
        """Calculate final price after discount"""
        return self.__base_price * (1 - self.__discount)
    
    @property
    def category(self) -> str:
        return self.__category
    
    def apply_discount(self, percentage: float):
        if 0 <= percentage <= 100:
            self.__discount = percentage / 100
        else:
            raise ValueError("Discount must be between 0 and 100")
```

### Use Case 2: Library Management System

```python
class LibraryMember:
    """Encapsulated member with controlled access"""
    
    def __init__(self, member_id: str, name: str):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_books = []
        self.__max_books = 5
    
    @property
    def can_borrow(self) -> bool:
        return len(self.__borrowed_books) < self.__max_books
    
    def borrow_book(self, book_title: str) -> bool:
        if self.can_borrow:
            self.__borrowed_books.append(book_title)
            return True
        return False
    
    def return_book(self, book_title: str) -> bool:
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            return True
        return False
    
    def get_borrowed_books(self):
        return self.__borrowed_books.copy()
```

---

## Delhi University Syllabus Context

This topic aligns with the **NEP 2024 UGCF** curriculum for BSc (Hons) Computer Science. Students should understand:

1. **Core Concepts**: Abstraction and Encapsulation in Python
2. **Implementation Details**: Abstract classes, @property, name mangling
3. **Practical Applications**: Building real-world Python applications
4. **Design Patterns**: Understanding when to apply each principle

**Recommended Reading**: 
- "Fluent Python" by Luciano Ramalho — for advanced Python concepts
- Official Python Documentation — dataclasses, abc module

---

## Key Takeaways

1. **Abstraction** hides complex implementation details behind a simple interface using abstract base classes and the `abc` module
2. **Encapsulation** bundles data and methods while restricting direct access using access modifiers
3. Python uses **convention-based privacy** — single underscore for protected, double underscore for private (name mangling)
4. **@property decorator** provides a clean way to implement getters, setters, and computed properties
5. **Name mangling** (`__attribute`) makes attributes harder to access accidentally but is not a security feature
6. **Data Classes** reduce boilerplate code for data-centric classes
7. Both concepts work together to create maintainable, scalable, and secure software
8. Understanding when to use each principle is crucial for good software design

---

## Multiple Choice Questions (MCQs)

### Level 1: Easy

1. **What is the primary purpose of abstraction in OOP?**
   - (a) To hide the implementation details
   - (b) To protect data from unauthorized access
   - (c) To combine multiple classes into one
   - (d) To speed up program execution
   
   **Answer: (a)** — Abstraction hides complexity behind simple interfaces

2. **Which module is used to create abstract classes in Python?**
   - (a) `abstract`
   - (b) `abc`
   - (c) `base`
   - (d) `abstractbase`
   
   **Answer: (b)** — The `abc` module provides Abstract Base Classes

3. **What does a single underscore prefix (e.g., `_name`) indicate in Python?**
   - (a) Private attribute
   - (b) Public attribute
   - (c) Protected attribute (convention)
   - (d) Static attribute
   
   **Answer: (c)** — Single underscore indicates protected by convention

### Level 2: Medium

4. **What is name mangling in Python?**
   - (a) A technique to hide variable names completely
   - (b) Automatic renaming of private attributes with class name prefix
   - (c) A security feature to encrypt data
   - (d) A way to generate random variable names
   
   **Answer: (b)** — Python automatically renames `__attr` to `_ClassName__attr`

5. **Which decorator is used to create a getter method in Python?**
   - (a) `@getter`
   - (b) `@property`
   - (c) `@access`
   - (d) `@retrieve`
   
   **Answer: (b)** — The `@property` decorator creates getter methods

6. **What is the output of the following code?**
   ```python
   class Test:
       def __init__(self):
           self.__value = 100
   
   obj = Test()
   print(obj._Test__value)
   ```
   - (a) Error
   - (b) 100
   - (c) None
   - (d) _Test__value
   
   **Answer: (b)** — Name mangling allows access via mangled name

### Level 3: Hard

7. **Which of the following statements is TRUE about data classes?**
   - (a) They cannot have methods
   - (b) They automatically generate `__init__`, `__repr__`, and `__eq__`
   - (c) They cannot have default values
   - (d) They are slower than regular classes
   
   **Answer: (b)** — Data classes automatically generate special methods

8. **In the context of encapsulation, what is the purpose of a setter method?**
   - (a) To read the value of a private attribute
   - (b) To modify private attributes with validation
   - (c) To delete a private attribute
   - (d) To create new private attributes
   
   **Answer: (b)** — Setters allow controlled modification with validation

9. **What happens when you try to instantiate an abstract class in Python?**
   - (a) It creates an empty object
   - (b) It raises a TypeError
   - (c) It works normally
   - (d) It raises a RuntimeError
   
   **Answer: (b)** — Cannot instantiate abstract classes; raises TypeError

10. **Which decorator is used to define an abstract method in Python?**
    - (a) `@abstract`
    - (b) `@abstractmethod`
    - (c) `@abstractmethod`
    - (d) `@abstra`
    
    **Answer: (b)** — `@abstractmethod` from the `abc` module

---

## Flashcards

### Flashcard 1: Definition of Abstraction
**Term:** Abstraction
**Definition:** The process of hiding complex implementation details and exposing only the essential features of an object. It focuses on "what" an object does rather than "how" it does it.
**Example:** Using `PaymentProcessor` abstract class without knowing how different payment methods are implemented.

---

### Flashcard 2: Definition of Encapsulation
**Term:** Encapsulation
**Definition:** The bundling of data (attributes) and methods (functions) into a single unit (class), while restricting direct access to some of the object's components to ensure data integrity and prevent unintended modifications.
**Example:** The `BankAccount` class with private `__balance` attribute accessed only through methods.

---

### Flashcard 3: Abstract Base Class
**Term:** Abstract Base Class (ABC)
**Definition:** A class in Python that cannot be instantiated directly and may contain abstract methods (methods without implementation). Used as blueprints for other classes. Created by inheriting from `ABC`.
**Code:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

### Flashcard 4: @property Decorator
**Term:** @property Decorator
**Definition:** A built-in decorator that allows methods to be accessed like attributes, enabling the implementation of getters, setters, and deleters with validation logic while maintaining a clean API.
**Code:**
```python
@property
def salary(self):
    return self.__salary

@salary.setter
def salary(self, value):
    if value < 0:
        raise ValueError("Salary cannot be negative")
    self.__salary = value
```

---

### Flashcard 5: Name Mangling
**Term:** Name Mangling
**Definition:** A Python feature where double-underscore prefixed attributes are automatically renamed to include the class name (e.g., `__attr` becomes `_ClassName__attr`), making them harder to access accidentally but not truly private.
**Code:**
```python
class MyClass:
    def __init__(self):
        self.__secret = 42

obj = MyClass()
print(obj._MyClass__secret)  # Outputs: 42
```

---

### Flashcard 6: Data Classes
**Term:** Data Classes
**Definition:** Classes introduced in Python 3.7 that are primarily used to store data. They automatically generate special methods like `__init__`, `__repr__`, `__eq__`, and `__hash__`, reducing boilerplate code.
**Code:**
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
point = Point(10, 20)
print(point)  # Point(x=10, y=20)
```

---

### Flashcard 7: Access Modifiers in Python
**Term:** Access Modifiers in Python
**Definition:** Python uses convention-based access control:
- `public`: No prefix (accessible everywhere)
- `_protected`: Single underscore (internal use)
- `__private`: Double underscore (name mangling applied)
Unlike Java/C++, these are conventions, not enforced restrictions.

---

### Flashcard 8: Difference Between Abstraction and Encapsulation
**Term:** Abstraction vs Encapsulation
**Definition:** 
- **Abstraction**: Hides complexity at the design level; "what" an object does
- **Encapsulation**: Protects data at implementation level; "how" data is protected
- Both work together: abstraction provides interfaces, encapsulation protects the implementation

---

*End of Study Material*