# Inheritance in C++ - Summary

## Key Definitions and Concepts

- **Inheritance:** A mechanism in OOP where a derived class inherits properties and behaviors (data members and member functions) from a base class, promoting code reusability and establishing "is-a" relationships.

- **Base Class (Superclass):** The class whose properties are inherited by another class.

- **Derived Class (Subclass):** The class that inherits properties from another class.

- **Virtual Function:** A member function declared with the `virtual` keyword that can be overridden in derived classes to achieve runtime polymorphism.

- **Pure Virtual Function:** A virtual function with `= 0` syntax that makes a class abstract and must be overridden by derived classes.

- **Polymorphism:** The ability of different classes to respond to the same function call in different ways, achieved through virtual functions.

## Important Formulas and Theorems

- **Constructor Execution Order:** Base class constructor → Derived class constructor
- **Destructor Execution Order:** Derived class destructor → Base class destructor (reverse of constructor order)

## Key Points

1. Inheritance enables code reusability by allowing derived classes to use base class members without redefinition.

2. Five types: Single (one base), Multiple (two+ bases), Multilevel (chain), Hierarchical (one base, many derived), Hybrid (combination).

3. Public inheritance maintains "is-a" relationship; protected/private inheritance represents "implemented in terms of."

4. Private and protected members cannot be accessed directly in derived classes—only through base class public/protected interface.

5. Virtual functions enable dynamic binding (runtime polymorphism) through vtable mechanism.

6. Abstract classes contain at least one pure virtual function and cannot be instantiated.

7. Without virtual destructor, only base class destructor is called when deleting through base pointer—causing memory leaks.

8. The diamond problem in multiple inheritance is solved using virtual inheritance.

## Common Mistakes to Avoid

- **Forgetting virtual destructor:** Leads to undefined behavior when deleting derived objects through base pointers.
- **Confusing access specifiers:** Protected doesn't mean public—it limits visibility to derived classes only.
- **Slicing objects:** Assigning derived object to base object (not pointer/reference) loses derived portion.
- **Not using override keyword:** Missing compile-time error detection for failed overrides.

## Revision Tips

1. Practice writing inheritance hierarchies with different access specifiers to understand member accessibility.

2. Create small programs to observe constructor/destructor execution order—always trace through mentally before running.

3. Remember: "Virtual for behavior, override for implementation, override keyword for safety."

4. Draw class diagrams for inheritance relationships to visualize the hierarchy clearly.

5. Solve previous year DU question papers to understand exam patterns and common question types.