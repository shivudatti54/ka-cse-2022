# Virtual Functions are Hierarchical - Summary

## Key Definitions and Concepts

- **Virtual Function**: A member function declared with the `virtual` keyword in a base class, which can be redefined in derived classes to achieve runtime polymorphism
- **Runtime Polymorphism**: The ability to determine which function to call at runtime based on the actual object type, not the pointer/reference type
- **VTABLE**: Virtual Function Table - a compiler-generated table containing function pointers for virtual functions of a class
- **VPTR**: Virtual Pointer - a hidden pointer in each object pointing to its class's VTABLE
- **Pure Virtual Function**: A virtual function declared with `= 0`, making the class abstract
- **Abstract Class**: A class containing at least one pure virtual function; cannot be instantiated
- **Object Slicing**: The problem where derived class portions are lost when assigning derived objects to base objects by value

## Important Formulas and Theorems

- Virtual function dispatch: `Object VPTR → Class VTABLE → Function Pointer → Actual Function`
- Dynamic binding occurs when virtual functions are called through pointers or references
- Static binding occurs for non-virtual functions and for default arguments in virtual functions

## Key Points

- Virtual functions create a hierarchy where the most derived implementation takes precedence
- VTABLE-VPTR mechanism enables runtime determination of function to be called
- Base class pointers/references can access derived class implementations through virtual functions
- Pure virtual functions enforce derived classes to provide implementations
- Virtual destructors ensure proper cleanup in polymorphic deletion scenarios
- The `override` specifier helps catch override errors at compile time
- Object slicing occurs with pass-by-value and destroys polymorphic behavior
- Constructors cannot be virtual, but destructors should be virtual in polymorphic classes

## Common Mistakes to Avoid

1. **Forgetting to declare base class destructor as virtual** - leads to resource leaks when deleting derived objects through base pointers

2. **Not using `override` specifier** - causes accidental function hiding instead of overriding

3. **Passing objects by value to virtual functions** - causes object slicing, losing polymorphic behavior

4. **Confusing function overloading with function overriding** - overloading occurs in same scope, overriding occurs across inheritance hierarchy

5. **Using static binding for default arguments** - default values are determined by pointer type, not object type

## Revision Tips

1. Draw the VTABLE-VPTR mechanism diagram to visualize how virtual function calls work

2. Practice with code examples: create a base class with virtual functions and override them in derived classes

3. Remember the golden rule: polymorphism requires pointers or references

4. Review the order of destructor calls in polymorphic hierarchies

5. Focus on understanding when and why object slicing occurs and how to prevent it
