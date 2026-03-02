# The Virtual Attribute is Inherited - Summary

## Key Definitions and Concepts

- **Virtual Function**: A member function declared with the `virtual` keyword in a base class, allowing derived classes to override it for runtime polymorphism.
- **Virtual Attribute Inheritance**: The property whereby all overriding functions in derived classes automatically inherit the virtual attribute from base class virtual functions.
- **Pure Virtual Function**: A virtual function declared with `= 0` that has no implementation, forcing derived classes to provide their own version.
- **Abstract Class**: A class containing at least one pure virtual function; cannot be instantiated but can serve as a base class.
- **Override Specifier**: C++11 keyword that explicitly indicates a function intends to override a virtual function, enabling compile-time error detection.

## Important Formulas and Theorems

- **Virtual Table (vtable)**: Each class with virtual functions has a vtable containing pointers to the virtual function implementations. Objects contain a hidden vptr pointing to this table.
- **Dynamic Dispatch**: The runtime mechanism that uses the vtable to resolve virtual function calls to the appropriate derived class implementation.

## Key Points

- Once a function is declared virtual in a base class, all overriding functions in derived classes are automatically virtual regardless of whether `virtual` keyword is used.
- Always declare destructors as virtual in base classes with virtual functions to prevent resource leaks.
- Use `override` specifier (C++11) to catch override errors at compile-time.
- Pure virtual functions (`= 0`) create abstract classes that define interfaces without implementations.
- Object slicing occurs when objects are passed by value, losing polymorphic behavior.
- During construction, virtual calls resolve to the class being constructed, not derived classes.
- Covariant return types allow overriding functions to return pointers/references to more derived types.

## Common Mistakes to Forget

- Forgetting to make destructors virtual in polymorphic base classes
- Not using `override` and missing override errors that cause unexpected behavior
- Attempting to instantiate abstract classes
- Passing objects by value when polymorphism is needed (causes slicing)
- Assuming default argument values follow virtual function dispatch

## Revision Tips

1. **Practice Writing Code**: Implement class hierarchies with virtual functions to reinforce the concepts.

2. **Remember the Golden Rule**: Virtual attribute is inherited - always keep this in mind when overriding functions.

3. **Draw vtables**: Visualize how vtables work for classes with virtual inheritance to understand dynamic binding.

4. **Always Virtual Destructor**: Make it a habit to always declare virtual destructors in polymorphic base classes.
