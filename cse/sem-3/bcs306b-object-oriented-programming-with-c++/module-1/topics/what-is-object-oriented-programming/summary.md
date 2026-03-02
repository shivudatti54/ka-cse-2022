# What is Object-Oriented Programming - Summary

## Key Definitions and Concepts

- **Object-Oriented Programming (OOP)**: A programming paradigm that uses "objects" containing data (attributes) and behavior (methods) to design and implement software systems.

- **Class**: A blueprint/template for creating objects that defines attributes and methods; objects are instances of classes.

- **Encapsulation**: Bundling data and methods into a single unit (class) with controlled access through access specifiers (private, public, protected).

- **Abstraction**: Hiding complex implementation details and showing only essential features to the user.

- **Inheritance**: Mechanism where a derived class acquires properties and behaviors of a base class, promoting code reuse.

- **Polymorphism**: Ability of different objects to respond to the same message (function call) in different ways; achieved through function overloading and virtual functions.

## Important Formulas and Theorems

- **Access Specifiers Hierarchy**: `private < protected < public` (increasing accessibility)
- **Object Creation**: `ClassName objectName;` or `ClassName *ptr = new ClassName();`
- **Pure Virtual Function**: `virtual returnType functionName() = 0;` makes a class abstract
- **Virtual Function Syntax**: `virtual returnType functionName() { // implementation }`

## Key Points

1. OOP organizes code around objects rather than functions, modeling real-world entities
2. Four fundamental principles: Encapsulation, Inheritance, Polymorphism, Abstraction
3. Class is a blueprint; object is an instance of a class
4. Encapsulation achieves data hiding through private members with public getters/setters
5. Inheritance enables code reuse through parent-child relationship between classes
6. Polymorphism allows one interface for different data types (static: overloading, dynamic: overriding)
7. Access specifiers: private (class only), protected (class + derived), public (everywhere)
8. Abstract classes contain pure virtual functions and cannot be instantiated
9. Constructors have same name as class; destructors have ~ prefix
10. OOP provides better security, maintainability, and scalability than procedural programming

## Common Mistakes to Avoid

1. **Confusing class with object**: A class is abstract (blueprint), while an object is concrete (instance)
2. **Forgetting access specifiers**: Without specifiers, class members default to private in C++
3. **Incorrect inheritance visibility**: Using wrong access mode changes base class member visibility in derived class
4. **Not using virtual for runtime polymorphism**: Without virtual keyword, static binding occurs instead of dynamic dispatch
5. **Trying to instantiate abstract class**: Classes with pure virtual functions cannot be instantiated

## Revision Tips

1. Draw class diagrams to visualize relationships between classes
2. Write small C++ programs implementing each OOP concept separately
3. Practice identifying which OOP principle is demonstrated in given code
4. Memorize the four pillars and their purposes - this is almost always asked in exams
5. Review university past question papers on this module to understand the question pattern
6. Create quick reference notes for syntax of access specifiers, inheritance modes, and virtual functions
