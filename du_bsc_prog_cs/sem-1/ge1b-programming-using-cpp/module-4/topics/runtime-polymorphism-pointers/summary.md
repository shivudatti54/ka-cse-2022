# Runtime Polymorphism Using Pointers in C++ - Summary

## Key Definitions and Concepts

- **Runtime Polymorphism**: Resolving function calls at runtime based on the actual object type, not the pointer/reference type. Achieved through virtual functions.

- **Virtual Function**: A member function declared with `virtual` keyword in base class, allowing derived classes to override it. Called through base pointer invokes the derived version.

- **Pure Virtual Function**: A virtual function with `= 0` syntax, having no implementation in base class. Makes the class abstract.

- **Abstract Class**: A class containing at least one pure virtual function. Cannot be instantiated but can have pointers/references to it.

- **Virtual Destructor**: A destructor declared virtual to ensure proper cleanup when deleting derived objects through base pointers.

- **Vtable (Virtual Table)**: Internal data structure containing function pointers for virtual functions, used by the runtime for dynamic dispatch.

## Important Formulas and Theorems

- **Virtual Function Call Mechanism**: Object vptr → Class vtable → Function pointer → Execute function

- **Dynamic Cast**: `dynamic_cast<NewType*>(ptr)` returns nullptr if conversion is invalid (for pointers) or throws bad_cast (for references)

- **Slicing Rule**: Assigning derived object to base object (by value) causes object slicing, losing polymorphism

## Key Points

- Base class pointers can store addresses of derived class objects enabling polymorphic behavior

- The `virtual` keyword enables runtime resolution of function calls based on actual object type

- Pure virtual functions (`= 0`) create abstract classes that serve as interfaces

- Always use virtual destructors when a class contains virtual functions to prevent memory leaks

- Use `override` keyword when overriding virtual functions to catch compile-time errors

- Abstract classes cannot be instantiated but pointers/references to them are allowed

- Virtual functions add small runtime overhead due to vtable lookup

- Static functions cannot be virtual; they don't have access to `this` pointer

- Virtual functions in constructors don't behave polymorphically - only base class version executes

## Common Mistakes to Avoid

1. **Forgetting Virtual Destructor**: Causes memory leaks when deleting derived objects through base pointers

2. **Object Slicing**: Passing objects by value to functions loses polymorphic behavior

3. **Missing Override**: Accidentally creating a new virtual function instead of overriding (different parameter list)

4. **Instantiating Abstract Classes**: Attempting to create objects of classes with pure virtual functions

5. **Non-virtual Base Functions**: Calling non-virtual functions through base pointers always calls base version

## Revision Tips

1. Practice writing inheritance hierarchies with virtual functions and testing polymorphism with base pointers

2. Draw vtable diagrams to understand how virtual function calls are resolved at runtime

3. Memorize the rule: "If a class has virtual functions, make the destructor virtual"

4. Understand the difference between `new` (heap) and stack allocation when using polymorphism

5. Review past DU question papers to identify common exam patterns around virtual functions and abstract classes