# Classes in C++ - Summary

## Key Definitions and Concepts

- **Class**: A user-defined data type that encapsulates data members and member functions into a single unit, serving as a blueprint for creating objects

- **Object**: An instance of a class that occupies memory and represents a concrete entity with state and behavior

- **Encapsulation**: The bundling of data and methods that operate on that data within a single unit (class), restricting direct access to some components

- **Access Specifiers**: Keywords (private, public, protected) that control the visibility and accessibility of class members

- **Constructor**: A special member function with the same name as the class, called automatically when an object is created for initialization

- **Destructor**: A special member function with the same name prefixed by ~, called automatically when an object is destroyed to release resources

- **this Pointer**: An implicit pointer available in non-static member functions that points to the object for which the function was called

- **Static Members**: Class-level variables and functions shared by all objects of the class, declared using the `static` keyword

- **Friend Function**: A non-member function granted access to private and protected members of a class using the `friend` keyword

## Important Formulas and Theorems

- **Object Size**: Total size = sum of all data members (may include padding for alignment)

- **Static Member Definition**: `return_type ClassName::static_member = initial_value;`

- **Scope Resolution Operator (::)**: Used to define member functions outside the class definition

- **Copy Constructor Signature**: `ClassName(const ClassName& object);`

- **Constructor Initialization List**: `ClassName(params) : member1(val1), member2(val2) { }`

## Key Points

1. Classes provide the foundation for Object-Oriented Programming in C++ through encapsulation

2. Private members are accessible only within the class; public members form the interface; protected members are accessible in derived classes

3. Constructors can be overloaded to provide multiple initialization options; the copy constructor creates a new object as a copy

4. Destructors are essential for resource management, especially when dealing with dynamic memory allocation

5. The this pointer allows member functions to identify the specific object they're operating on

6. Static members belong to the class rather than individual objects and must be defined outside the class declaration

7. Friend functions bypass encapsulation but serve important purposes in operator overloading and related class designs

## Common Mistakes to Avoid

- Forgetting to define static members outside the class (causes linker error)

- Not providing a copy constructor when the class contains pointer members (shallow copy problem)

- Using assignment operator instead of copy constructor for initialization: `MyClass obj2 = obj1;` (copy constructor)

- Confusing struct and class default access specifiers (public vs private)

- Declaring constructors and destructors with return types (they have none)

## Revision Tips

1. Practice writing complete class definitions with constructors, destructors, and member functions

2. Trace through code to understand when constructors and destructors are called in different scenarios

3. Create small programs to experiment with access specifiers and understand their effects

4. Review the difference between copy constructor and assignment operator through examples

5. Remember that static members are shared and can be accessed using ClassName::member syntax
