# Introducing C++ Classes - Summary

## Key Definitions and Concepts

- **Class**: A user-defined data type that serves as a blueprint for creating objects, combining data members and member functions into a single unit.

- **Object**: An instance of a class that occupies memory and represents a specific entity.

- **Access Specifiers**: Keywords that control the visibility of class members—private (default for class), public, and protected.

- **Constructor**: A special member function with the same name as the class, automatically invoked during object creation to initialize objects.

- **Destructor**: A special member function with a tilde (~) prefix, automatically called when an object is destroyed to release resources.

- **this Pointer**: An implicit pointer pointing to the current object, available in non-static member functions.

- **Static Members**: Class members (data or functions) that belong to the class itself rather than any individual object, shared across all instances.

## Important Formulas and Theorems

- **Object Creation**: `ClassName objectName;` creates an object on the stack
- **Dynamic Object**: `ClassName* ptr = new ClassName();` creates object on heap
- **Static Member Access**: `ClassName::staticMember` (without object)
- **this Pointer**: `this->member` accesses current object's members

## Key Points

- Classes enable data abstraction and encapsulation, fundamental OOP principles
- Class members are private by default; struct members are public by default
- Constructors can be overloaded but destructors cannot
- Constructors initialize objects; destructors clean up resources
- The `this` pointer resolves ambiguity when parameter names match member names
- Static data members require external definition outside the class
- Static member functions can be called without creating any object
- Objects on stack are automatically destroyed when they go out of scope

## Common Mistakes to Avoid

1. Forgetting the semicolon after class definition (compilation error)
2. Trying to access private members directly from main() or other functions
3. Not providing external definition for static data members
4. Confusing constructor declaration with regular function declaration
5. Forgetting to use `delete` for dynamically allocated objects, causing memory leaks

## Revision Tips

1. Practice writing complete class definitions with all three access specifiers
2. Trace through constructor and destructor call sequences using example programs
3. Understand when copy constructor is invoked (pass by value, return by value, initialization)
4. Remember that static members exist in only one copy regardless of object count
5. Review the differences between class and structure—this is a common exam question
6. Write small programs to experiment with constructors, destructors, and object lifecycle
