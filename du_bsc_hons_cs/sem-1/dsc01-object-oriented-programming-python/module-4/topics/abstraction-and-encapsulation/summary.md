# Abstraction and Encapsulation

## Introduction

Abstraction and Encapsulation are fundamental Object-Oriented Programming (OOP) concepts that promote code reusability, maintainability, and security. As per Delhi University B.Sc. (Hons) Computer Science NEP 2024 UGCF syllabus, these concepts are essential for designing robust Python applications.

---

## Abstraction

**Definition:** Abstraction hides complex implementation details and shows only essential features of an object.

### Key Concepts:
- **Purpose:** Simplify complex systems by showing only necessary details
- **Implementation in Python:**
  - Abstract Base Classes (ABC) from `abc` module
  - Abstract methods using `@abstractmethod` decorator
  - Abstract classes cannot be instantiated directly
- **Benefits:**
  - Reduces code complexity
  - Focuses on "what" rather than "how"
  - Enables polymorphism
  - Facilitates maintenance and future changes

### Python Example:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

## Encapsulation

**Definition:** Encapsulation bundles data (variables) and methods (functions) together while restricting direct access to some components.

### Key Concepts:
- **Purpose:** Protect data and control access to internal state
- **Access Specifiers in Python:**
  - `public` - accessible everywhere (default)
  - `_protected` - accessible within class and subclasses
  - `__private` - name mangling, accessible within class only
- **Getters and Setters:** Control access to private attributes
- **Benefits:**
  - Data hiding and security
  - Prevents unintended modification
  - Easy maintenance and debugging
  - Modular code design

### Python Example:
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private
    
    def get_balance(self):  # getter
        return self.__balance
    
    def deposit(self, amount):  # setter with validation
        if amount > 0:
            self.__balance += amount
```

---

## Key Differences

| Aspect | Abstraction | Encapsulation |
|--------|-------------|---------------|
| **Focus** | Hides complexity | Hides data |
| **Level** | Design level | Implementation level |
| **Purpose** | Show essential features | Protect information |
| **Example** | Interface/Abstract class | Private variables |

---

## Conclusion

Abstraction and encapsulation are complementary OOP principles. Abstraction focuses on "what an object does" by hiding implementation details, while encapsulation focuses on "how data is protected" through access control. Together, they enable developers to build modular, secure, and maintainable Python applications—essential skills for the Delhi University B.Sc. Computer Science practical and theory examinations.