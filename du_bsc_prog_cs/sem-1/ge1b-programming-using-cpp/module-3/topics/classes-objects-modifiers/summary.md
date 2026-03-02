# Classes, Objects & Modifiers in C++

## Introduction

Object-Oriented Programming (OOP) is a fundamental paradigm in C++ that enables modular, reusable, and maintainable code. According to the Delhi University BSc (Hons) CS NEP 2024 syllabus, understanding classes, objects, and access modifiers is essential for building robust applications. This summary covers core OOP concepts for exam preparation.

---

## Key Concepts

### Classes and Objects

- **Class**: A user-defined data type that bundles data members (variables) and member functions (methods) together. It serves as a blueprint for creating objects.
- **Object**: An instance of a class. It occupies memory and can access class members.
- **Syntax**:
  ```cpp
  class ClassName {
      // members
  };
  ClassName obj;  // object creation
  ```

### Access Modifiers

C++ provides three access specifiers that control visibility of class members:

- **Public**: Members accessible from anywhere; used for interface functions.
- **Private**: Members accessible only within the class; used for data hiding (default for class members).
- **Protected**: Accessible within class and derived classes; used in inheritance.

### Constructors and Destructors

- **Constructor**: Special member function with same name as class, called automatically when object is created. Can be parameterized, copy, or default.
- **Destructor**: Named with tilde (~), automatically called when object goes out of scope; used for cleanup operations.

### Additional Core Concepts

- **Data Hiding**: Encapsulation achieved by making data members private and providing public getter/setter methods.
- **this Pointer**: Implicit pointer pointing to the current object instance.
- **Static Members**: Shared across all objects of a class (static data members and static member functions).

---

## Exam Tips (Delhi University)

- Remember: Class members are **private by default** in C++ (unlike struct).
- Constructor overloading and copy constructor are frequently asked.
- Know the difference between access modifiers—most common mistake is confusing private and protected.
- Draw class diagrams to visualize relationships.

---

## Conclusion

Classes and objects form the foundation of OOP in C++. Access modifiers enforce encapsulation, while constructors/destructors manage object lifecycle. Master these concepts to write modular, secure, and maintainable code—essential skills for the Delhi University B.Sc. CS practical and theory examinations.