# Inheritance and Polymorphism in C++

## Introduction
Inheritance and polymorphism are fundamental Object-Oriented Programming (OOP) concepts essential for code reusability and flexibility. These topics are part of the Delhi University BSc Physical Science (CS) NEP 2024 syllabus under the Programming Using C++ paper.

## Inheritance

Inheritance allows a class (derived class) to acquire properties and behaviors of another class (base class), promoting code reuse.

- **Purpose**: Establishes "is-a" relationship between classes
- **Types of Inheritance**:
  - Single Inheritance (one base → one derived)
  - Multiple Inheritance (multiple bases → one derived)
  - Multilevel Inheritance (base → derived → further derived)
  - Hierarchical Inheritance (one base → multiple derived)
  - Hybrid Inheritance (combination of above types)
- **Access Specifiers**:
  - `public`: Public and protected members remain accessible; private members inaccessible
  - `protected`: Public and protected become protected
  - `private`: Both become private
- **Syntax**: `class DerivedClass : public BaseClass { };`
- **Member Overriding**: Derived class can redefine base class functions using same signature
- **Constructor/Destructor Execution**: Base constructor executes before derived constructor; destructors execute in reverse order

## Polymorphism

Polymorphism allows one interface to be used for different data types, enabling dynamic behavior.

### Compile-Time (Static) Polymorphism
- **Function Overloading**: Multiple functions with same name but different parameters
- **Operator Overloading**: Redefining operators for user-defined types

### Runtime (Dynamic) Polymorphism
- Achieved through **virtual functions** and inheritance
- **Virtual Functions**: Functions declared in base class and redefined in derived classes using `virtual` keyword
- **Pure Virtual Functions**: Functions with `= 0` syntax; make a class **abstract** (cannot instantiate)
- **Virtual Destructors**: Essential for proper cleanup when deleting base pointers to derived objects
- **Dynamic Binding**: Function call resolved at runtime using vtable (virtual function table)

### Key Relationships
- **Base Class Pointer**: Can point to derived class objects
- **Virtual Function Table (vtable)**: Compiler-generated table storing function pointers for runtime resolution

## Conclusion
Inheritance and polymorphism are crucial for designing extensible and maintainable C++ programs. Mastery of access specifiers, virtual functions, and abstract classes is essential for the Delhi University exam. Practice implementing inheritance hierarchies and runtime polymorphism to score well.

*Relevant as per GE1B: Programming Using C++ (NEP 2024)*