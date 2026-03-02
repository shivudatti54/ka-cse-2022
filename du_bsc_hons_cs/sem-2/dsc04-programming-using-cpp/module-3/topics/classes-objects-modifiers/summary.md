# Classes, Objects, and Modifiers in C++

## Introduction

Object-Oriented Programming (OOP) is a core paradigm in C++ that organizes software design around data and objects rather than functions. For BSc (Hons) Computer Science students under Delhi University's NEP 2024 UGCF syllabus, understanding classes, objects, and modifiers is essential for building robust C++ applications.

## Key Concepts

### Classes

- A **class** is a user-defined data type that acts as a blueprint for creating objects
- It **encapsulates** data (member variables) and functions (member methods) together
- Syntax: `class ClassName { access_specifier: members; };`
- Classes provide data hiding and abstraction

### Objects

- An **object** is an instance of a class that occupies memory
- Created using: `ClassName objectName;`
- Each object has its own copy of non-static member variables
- Objects interact through member functions

### Access Specifiers (Modifiers)

- **Private**: Members accessible only within the class (default for class)
- **Public**: Members accessible from anywhere in the program
- **Protected**: Accessible within class and derived classes (for inheritance)
- **Friend**: Grants specific functions or classes access to private members

### Constructors and Destructors

- **Constructor**: Special member function with same name as class, called automatically when object is created
  - Default constructor, Parameterized constructor, Copy constructor
- **Destructor**: Named with tilde (~), called automatically when object is destroyed
  - Used for cleanup operations (releasing memory, closing files)

### Additional Concepts

- **this Pointer**: Implicit pointer pointing to the current object
- **Static Members**: Shared among all objects of a class (declared with `static` keyword)
- **Member Initialization List**: Used for initializing const and reference members

## Conclusion

Classes, objects, and modifiers form the foundation of OOP in C++. Mastery of these concepts is crucial for understanding advanced topics like inheritance, polymorphism, and encapsulation—key requirements in the Delhi University BSc (Hons) Computer Science curriculum. Practice creating classes and objects to build strong programming fundamentals.