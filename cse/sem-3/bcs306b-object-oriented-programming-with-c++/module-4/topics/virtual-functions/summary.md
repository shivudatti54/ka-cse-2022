# Virtual Functions in C++ - Summary

## Key Definitions and Concepts

- **Virtual Function**: A member function declared with the `virtual` keyword in a base class that can be overridden by derived classes to provide specific implementations. Enables runtime polymorphism.

- **Pure Virtual Function**: A virtual function with no implementation, declared by assigning `= 0`. Makes the class abstract.

- **Abstract Class**: A class containing at least one pure virtual function; cannot be instantiated but can serve as a base class.

- **Runtime Polymorphism**: Dynamic binding where the function to call is determined at runtime based on the actual object type.

- **vtable (Virtual Table)**: A lookup table used by C++ to implement dynamic dispatch of virtual functions.

- **vptr (Virtual Pointer)**: A hidden pointer in each object of a class with virtual functions, pointing to the class's vtable.

## Important Formulas and Theorems

- **Virtual Function Declaration**: `virtual return_type function_name(parameters);`

- **Pure Virtual Function**: `virtual return_type function_name(parameters) = 0;`

- **Virtual Destructor Rule**: `virtual ~ClassName() {}` - Always virtual in polymorphic base classes

## Key Points

1. Virtual functions enable dynamic binding - function call is resolved at runtime based on actual object type.

2. The `virtual` keyword must be used in the base class declaration; `override` is optional but recommended in derived classes.

3. Pure virtual functions (= 0) create abstract classes that define interfaces for derived classes.

4. Virtual destructors are essential to prevent memory leaks when deleting derived objects through base pointers.

5. Constructors cannot be virtual, but destructors should be virtual in polymorphic hierarchies.

6. Static members cannot be virtual because they don't belong to any object.

7. Default arguments use static binding (base class values) even with virtual functions.

8. Abstract classes cannot be instantiated but can have constructors for derived classes to call.

## Common Mistakes to Avoid

1. **Forgetting to declare the base class function as virtual**: Without the virtual keyword, static binding occurs even if the derived class overrides the function.

2. **Not using virtual destructor in polymorphic classes**: This leads to undefined behavior and memory leaks when deleting derived objects through base pointers.

3. **Trying to instantiate abstract classes**: Remember that classes with pure virtual functions cannot be instantiated.

4. **Signature mismatch in override**: Using different parameter types in derived class function will create a new function, not override the base virtual function.

## Revision Tips

1. Practice writing code with base and derived classes using virtual functions to reinforce the concept.

2. Remember the rule: "If a class has virtual functions, make the destructor virtual."

3. Understand that pure virtual functions force derived classes to provide implementations - they're like required methods.

4. Review the output of example programs to understand how runtime polymorphism works.

5. Focus on the difference between compile-time (overloading) and runtime (virtual functions) polymorphism.
