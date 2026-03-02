# Polymorphism in C++

## Introduction
Polymorphism is one of the fundamental pillars of Object-Oriented Programming (OOP), along with encapsulation, inheritance, and abstraction. The term "polymorphism" is derived from Greek words meaning "many forms." In C++, polymorphism allows a single interface to be used for different underlying data types, enabling code reusability and flexibility. This topic is a crucial part of the Delhi University BSc (Hons) Computer Science syllabus under the NEP 2024 UGCF curriculum.

---

## Key Concepts

### Definition
- **Polymorphism** enables one interface to be used for a general class of actions, where the specific action is determined by the exact nature of the situation.

### Types of Polymorphism

#### 1. Compile-Time (Static) Polymorphism
- Achieved through **function overloading** and **operator overloading**
- Resolution happens at compile time
- Also known as early binding or static binding

**Function Overloading:**
- Multiple functions with the same name but different parameters
- Distinguishing factors: number of arguments, type of arguments, or order of arguments

**Operator Overloading:**
- Redefining existing operators to work with user-defined data types
- Example: Overloading `+` operator for a `Complex` class

#### 2. Runtime (Dynamic) Polymorphism
- Achieved through **virtual functions** and **inheritance**
- Resolution happens at runtime
- Also known as late binding or dynamic binding
- Uses the concept of **virtual functions**

---

## Important Topics for Exams

### Virtual Functions
- Member function declared in base class and overridden in derived class
- Declared using `virtual` keyword
- Achieved through **pointer to base class** referring to derived class objects
- Uses **Virtual Function Table (vtable)** for runtime resolution

### Pure Virtual Functions
- Virtual function with no implementation: `virtual void display() = 0;`
- Used to create **abstract base classes**
- Forces derived classes to provide their own implementation

### Abstract Classes
- Class containing at least one pure virtual function
- Cannot be instantiated directly
- Used as base classes for inheritance
- Derived classes must override all pure virtual functions

### Virtual Destructors
- Essential when deleting derived class objects through base class pointers
- Syntax: `virtual ~BaseClass() { }`
- Ensures proper cleanup of derived class destructors

### Key Keywords
- `virtual` - declares a virtual function
- `override` - (C++11) explicitly declares overriding (optional but recommended)
- `final` - (C++11) prevents further overriding

---

## Conclusion
Polymorphism is essential for writing flexible and extensible C++ programs. It allows developers to create code that can work with objects of different classes through a common interface. Mastery of both compile-time and runtime polymorphism is crucial for exam success and practical software development. Remember: compile-time polymorphism offers speed, while runtime polymorphism offers flexibility.

---

*Revision Tip: Focus on virtual functions, pure virtual functions, and the difference between compile-time and runtime polymorphism—these are frequently examined topics.*