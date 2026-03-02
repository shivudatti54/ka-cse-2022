# Functions and Type Casting (C++)

## Introduction
This topic is a fundamental pillar of C++ programming, covering modular code design through functions and data type management via type casting. As per the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus, these concepts are essential for building efficient and type-safe applications.

---

## Key Concepts

### 1. Functions
- **Definition**: A self-contained block of code that performs a specific task, promoting code reusability and modularity.
- **Components**:
  - *Function Declaration*: Informs the compiler about the function's name, return type, and parameters.
  - *Function Definition*: Contains the actual code.
  - *Function Call*: Invokes the function to execute.
- **Types of Functions**:
  - *Library Functions*: Pre-defined (e.g., `cin`, `cout`, `sqrt()`)
  - *User-defined Functions*: Created by the programmer (e.g., `int add(int a, int b)`)
- **Parameter Passing Techniques**:
  - *Pass by Value*: Copies the actual argument (changes don't affect original).
  - *Pass by Reference*: Uses memory address (`&`), allowing modification of original values.
  - *Default Arguments*: Parameters assume default values if not provided during the call.
- **Scope & Storage Classes**:
  - *Local Variables*: Declared inside function (auto by default).
  - *Global Variables*: Declared outside functions, accessible everywhere.
  - *Storage Classes*: `auto` (default for local), `static` (retains value), `extern` (global declaration), `register` (fast access).
- **Function Overloading**: Multiple functions with the same name but different parameter lists (compile-time polymorphism).

### 2. Type Casting (Type Conversion)
- **Definition**: Converting one data type to another, essential for type compatibility in operations.
- **Implicit Type Casting (Coercion)**:
  - Automatically performed by the compiler.
  - Occurs in assignments and expressions (e.g., `int + float` → `float`).
  - May lead to data loss (narrowing conversion).
- **Explicit Type Casting (C-style)**:
  - `(type) expression` — e.g., `(int) 3.14`
- **Functional Notation**:
  - `type(expression)` — e.g., `int(3.14)`
- **C++ Specific Cast Operators**:
  - `static_cast<type>`: For well-defined conversions (e.g., `void*` to `int*`).
  - `const_cast`: To add or remove `const` qualifier.
  - `reinterpret_cast`: For low-level reinterpretation of bit patterns (unsafe).
  - `dynamic_cast`: For safe downcasting in inheritance hierarchies (runtime check).

---

## Conclusion
Mastering functions enables writing modular, maintainable code, while type casting ensures proper data handling and type safety. These concepts form the backbone of intermediate C++ programming and are frequently tested in Delhi University examinations under the NEP 2024 framework. Focus on parameter passing mechanisms and the differences between implicit and explicit casting for quick revision.