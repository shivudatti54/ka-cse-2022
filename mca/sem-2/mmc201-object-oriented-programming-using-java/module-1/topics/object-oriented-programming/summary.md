# Object-Oriented Programming - Summary

## Key Definitions and Concepts

- **Class**: A blueprint/template that defines properties (fields) and behaviors (methods) for objects
- **Object**: An instance of a class that occupies memory and represents a real-world entity
- **Encapsulation**: Bundling data and methods together while restricting direct access to data through access modifiers
- **Inheritance**: Mechanism where a subclass inherits properties and behaviors from a parent class
- **Polymorphism**: Ability of objects to take many forms—achieved through method overloading and overriding
- **Abstraction**: Hiding complex implementation details and showing only essential features through abstract classes and interfaces

## Important Formulas and Theorems

- **Constructor Syntax**: `ClassName(parameters) { initialization }`
- **Inheritance Declaration**: `class SubClass extends SuperClass`
- **Interface Implementation**: `class ClassName implements InterfaceName`
- **Method Overloading**: Same method name, different parameters within same class
- **Method Overriding**: Same method signature in subclass with different implementation

## Key Points

1. Java is a pure object-oriented language—everything revolves around classes and objects.

2. The four pillars of OOP are Encapsulation, Inheritance, Polymorphism, and Abstraction.

3. Access modifiers control visibility: private (class) < default < protected < public.

4. The `new` keyword creates objects and allocates memory in the heap.

5. Constructors are special methods called during object creation but are not inherited.

6. A class can extend only one class (single inheritance) but can implement multiple interfaces.

7. Runtime polymorphism is achieved through method overriding and upcasting (parent reference to child object).

8. Abstract classes cannot be instantiated but can have constructors; interfaces were pure abstraction before Java 8.

## Common Mistakes to Avoid

- Confusing method overloading with method overriding—they are fundamentally different concepts
- Forgetting to call `super()` in subclass constructors when needed
- Trying to access private members directly in subclasses
- Confusing abstract classes with interfaces—know when to use each
- Not providing implementations for all abstract methods in concrete subclasses

## Revision Tips

1. Practice writing small Java programs implementing each OOP concept separately.

2. Draw class diagrams to visualize relationships between classes (inheritance hierarchy).

3. Memorize the syntax for class creation, inheritance, and interface implementation.

4. Review previous university question papers to understand the pattern of questions on OOP concepts.

5. Focus on understanding "why" each concept exists and its practical applications rather than just memorizing definitions.
