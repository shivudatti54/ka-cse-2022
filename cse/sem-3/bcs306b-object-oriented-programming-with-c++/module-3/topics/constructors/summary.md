# Constructors in C++ - Summary

## Key Definitions and Concepts

- **Constructor**: A special member function with the same name as the class, no return type, automatically invoked during object creation to initialize objects.

- **Default Constructor**: Constructor with no parameters or all parameters having default values; provided by compiler if no constructors defined.

- **Copy Constructor**: Creates a new object as a copy of an existing object, invoked during pass-by-value, return-by-value, initialization, and explicit copying.

- **Move Constructor**: C++11 feature that transfers resource ownership from temporary objects, avoiding expensive deep copies.

- **Constructor Initializer List**: Initialization syntax using colon after constructor parameters, more efficient than assignment in constructor body.

## Important Formulas and Theorems

- **Rule of Three**: If a class requires either a custom copy constructor, copy assignment operator, or destructor, it likely requires all three.

- **Rule of Five**: In C++11+, move constructor and move assignment operator are added to Rule of Three.

- **Constructor Execution Order**: 1) Base class constructors (in declaration order), 2) Member object constructors (in declaration order), 3) Constructor body executes.

## Key Points

- Constructors cannot be virtual, cannot return values, and are not inherited.

- The `explicit` keyword prevents implicit conversions for single-parameter constructors.

- Private constructors implement Singleton pattern and factory methods.

- Copy constructor takes const reference parameter: `ClassName(const ClassName&)`.

- Move constructor takes rvalue reference: `ClassName(ClassName&&) noexcept`.

- Constructor initializer lists are mandatory for const members, references, and member objects without default constructors.

- Compiler-generated copy constructor performs shallow copy; user-defined version needed for deep copy.

## Common Mistakes to Avoid

- Forgetting to implement deep copy constructor when class contains pointer members, leading to double deletion and undefined behavior.

- Initializing members in wrong order in initializer list (should match declaration order).

- Using assignment instead of initialization for const and reference members (causes compilation error).

- Not marking move constructor as noexcept, preventing optimization in standard containers.

- Defining copy constructor that takes non-const reference (incorrect parameter type).

## Revision Tips

1. Practice writing all constructor types for a sample class with different members including pointers, const, and references.

2. Trace through code examples to identify when each constructor is invoked.

3. Remember the parameter passing conventions: copy constructor uses const reference, move constructor uses rvalue reference.

4. Understand shallow copy vs deep copy implications for memory management.

5. Review the Rule of Three/Five to determine when custom constructors/assignment operators are needed.
