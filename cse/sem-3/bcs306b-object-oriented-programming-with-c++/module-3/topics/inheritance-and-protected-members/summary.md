# Inheritance and Protected Members - Summary

## Key Definitions and Concepts

- **Inheritance**: A mechanism in OOP where a derived class acquires the properties and behaviors of an existing base class, promoting code reusability.

- **Base Class (Superclass)**: The existing class from which other classes inherit properties and methods.

- **Derived Class (Subclass)**: A new class that inherits properties and methods from an existing base class.

- **Protected Members**: Class members accessible within the class and its derived classes but not from outside the class hierarchy.

- **Single Inheritance**: One base class inherited by one derived class.

- **Multiple Inheritance**: A derived class inheriting from more than one base class.

- **Multilevel Inheritance**: Inheritance chain where a class is derived from a class that is already derived from another class.

## Important Formulas and Theorems

- **Constructor Execution Order**: Base constructor → Derived constructor
- **Destructor Execution Order**: Derived destructor → Base destructor (reverse of construction)
- **Access Control in Public Inheritance**: Public → Public, Protected → Protected, Private → Not accessible
- **Access Control in Protected Inheritance**: Public → Protected, Protected → Protected, Private → Not accessible
- **Access Control in Private Inheritance**: Public → Private, Protected → Private, Private → Not accessible

## Key Points

1. Protected members provide a middle ground between public (fully accessible) and private (fully encapsulated) members.

2. In public inheritance, the derived class IS-A base class, establishing an "is-a" relationship.

3. Private inheritance makes the derived class have a base class but hides the relationship from external code.

4. Constructors cannot be inherited but can be called from derived class constructors using initializer lists.

5. The diamond problem in hybrid inheritance is solved using virtual base classes.

6. A derived class can override base class methods through function overriding.

7. Protected data members allow derived classes to access internal state while maintaining encapsulation from outside code.

8. Multiple inheritance requires careful design to avoid ambiguity in member access.

## Common Mistakes to Avoid

1. **Assuming private members are accessible in derived classes**: Remember that private members of base class are never directly accessible in derived classes.

2. **Forgetting destructor virtuality**: When using polymorphism, always make base class destructors virtual to ensure proper cleanup.

3. **Constructor call order confusion**: Always remember base class constructor executes before derived class constructor.

4. **Slicing**: Assigning derived class object to base class object causes slicing; use pointers or references to avoid this.

## Revision Tips

1. Practice drawing inheritance hierarchy diagrams to visualize class relationships.

2. Write small programs to test different access specifier combinations and inheritance modes.

3. Memorize the access control table for all three inheritance types.

4. Trace through code examples to understand constructor/destructor execution order.

5. Review previous year questions on inheritance and protected members for exam pattern.
