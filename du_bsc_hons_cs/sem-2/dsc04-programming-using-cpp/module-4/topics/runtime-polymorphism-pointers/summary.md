# Runtime Polymorphism Pointers

## Introduction

Runtime polymorphism in C++ enables dynamic method resolution during program execution, allowing a single interface to represent different underlying forms (data types). This is primarily achieved through **virtual functions** and **base class pointers**, forming a core component of the Delhi University B.Sc. (Hons) Computer Science syllabus under Object-Oriented Programming using C++.

---

## Key Concepts

### 1. Virtual Functions
- Declared using the `virtual` keyword in the base class
- Can be overridden in derived classes
- Enables runtime binding through pointer or reference
- Syntax: `virtual return_type function_name(parameters);`

### 2. Pure Virtual Functions & Abstract Classes
- Pure virtual function: `virtual return_type func() = 0;`
- Class containing at least one pure virtual function becomes **abstract**
- Cannot instantiate abstract class, but can create pointers to it
- Serves as a blueprint for derived classes

### 3. Virtual Function Table (vtable)
- Compiler-generated table for each class with virtual functions
- Contains pointers to virtual function implementations
- Each object contains a hidden **vptr** pointing to class vtable
- Used at runtime for dynamic function resolution

### 4. Base Class Pointers
- Base class pointer can hold addresses of derived class objects
- Enables accessing derived class methods through base interface
- Syntax: `BaseClass* ptr = &derivedObject;`
- Function call resolved at runtime based on actual object type

### 5. Dynamic Binding
- Also known as **late binding**
- Function to execute determined at runtime, not compile-time
- Only applies to `virtual` functions
- Default binding is static (compile-time) for non-virtual functions

### 6. Virtual Destructors
- Essential for proper cleanup when deleting derived object through base pointer
- Declared as `virtual ~BaseClass() { }`
- Ensures derived class destructor executes before base class destructor

### 7. Override Specifier (C++11)
- Used to explicitly indicate intention to override a virtual function
- Syntax: `void display() override;`
- Compiler catches errors if no matching virtual function exists in base class

### 8. Slicing Problem
- Occurs when object is passed by value (not pointer/reference)
- Object sliced to base type, losing derived class properties
- **Solution**: Use pointers or references to avoid slicing

---

## Conclusion

Runtime polymorphism through pointers is fundamental to achieving flexible and extensible code in C++. Mastery of virtual functions, pure virtual functions, vtable mechanism, and proper use of base class pointers is essential for the Delhi University exam. Remember: always use virtual destructors when dealing with inheritance hierarchies, and prefer pointers/references to avoid object slicing. This concept directly supports advanced topics like interfaces, design patterns, and framework development.