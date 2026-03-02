# Using Virtual Functions in C++ - Summary

## Key Definitions and Concepts

- **Virtual Function**: A member function declared with the `virtual` keyword in a base class that can be overridden in derived classes, enabling runtime polymorphism through dynamic binding.

- **Pure Virtual Function**: A virtual function declared with `= 0` that has no implementation in the base class, forcing derived classes to provide their own implementation.

- **Abstract Class**: A class containing at least one pure virtual function; cannot be instantiated but can serve as a base class for polymorphism.

- **Vtable (Virtual Function Table)**: A runtime data structure containing function pointers to the most derived implementations of virtual functions for a class.

- **Vptr (Virtual Table Pointer)**: A hidden pointer in each object pointing to the class's vtable, used for runtime virtual function dispatch.

## Important Formulas and Theorems

- **Pure Virtual Declaration**: `virtual return_type function_name() = 0;`
- **Virtual Destructor Rule**: If a class has virtual functions, its destructor must be virtual
- **Dynamic Binding**: Resolved at runtime based on actual object type, not pointer/reference type

## Key Points

- Virtual functions enable runtime polymorphism through late binding
- The `override` keyword (C++11) helps catch signature mismatches when overriding
- Abstract classes with pure virtual functions define interfaces for derived classes
- Virtual destructors ensure proper cleanup when deleting derived objects through base pointers
- Object slicing occurs when derived objects are assigned to base objects (not pointers/references)
- Virtual function calls cannot be made from constructors (derived portion doesn't exist yet)
- Multiple inheritance results in multiple vtables for each base class with virtual functions
- Default arguments in virtual functions use base class values, not derived class values
- Private and protected virtual functions can still be overridden in derived classes
- Virtual functions have minimal runtime overhead due to vtable indirection

## Common Mistakes to Avoid

1. Forgetting to declare base class destructor as virtual, causing resource leaks
2. Forgetting to make base class destructor virtual is a critical error in polymorphic deletion
3. Calling virtual functions from constructors leads to base class version being called
4. Object slicing when passing objects by value instead of by reference or pointer
5. Incorrect function signature when overriding (missing const, wrong parameters) without using override

## Revision Tips

1. Practice writing class hierarchies with virtual functions and pure virtual functions
2. Trace through code with different object types accessed through base class pointers
3. Remember the rule: virtual functions in base → virtual destructor in base
4. Understand that abstract classes cannot be instantiated but pointers to them can be created
5. Use the override keyword always when overriding virtual functions to avoid subtle bugs
