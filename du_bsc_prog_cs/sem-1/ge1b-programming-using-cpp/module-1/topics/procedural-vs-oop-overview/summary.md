# Procedural vs Object-Oriented Programming - Summary

## Key Definitions and Concepts

- **Procedural Programming**: A paradigm based on procedure calls, where programs are structured as sequences of functions operating on global data
- **Object-Oriented Programming**: A paradigm organizing code around objects that contain data (attributes) and methods (behaviors)
- **Class**: A blueprint for creating objects in OOP
- **Object**: An instance of a class
- **Encapsulation**: Bundling data and methods into a single unit with controlled access
- **Inheritance**: Mechanism where a derived class acquires properties of a base class
- **Polymorphism**: Ability of different objects to respond to the same message differently
- **Abstraction**: Hiding complex implementation details and showing only essential features

## Important Formulas and Concepts

- **Access Specifiers**: `public` (accessible everywhere), `private` (class only), `protected` (class + derived classes)
- **Virtual Functions**: Declared with `virtual` keyword, enable runtime polymorphism
- **Pure Virtual Function**: `virtual return_type function() = 0;` makes class abstract
- **Constructor**: Initializes objects; same name as class, no return type
- **Destructor**: Cleans up resources; `~ClassName()`, called automatically

## Key Points

- C++ supports both procedural and OOP paradigms—a unique advantage
- Procedural follows top-down approach; OOP follows bottom-up design
- OOP provides better data security through encapsulation
- Inheritance promotes code reusability but increases complexity
- Polymorphism enables one interface for different data types
- Abstract classes cannot be instantiated but can have concrete methods
- `this` pointer refers to the current object in member functions
- Use procedural for simple, sequential tasks; OOP for complex systems

## Common Mistakes to Avoid

1. **Confusing classes with objects**: A class is a blueprint; an object is its instance
2. **Forgetting access specifiers**: Default for class members is `private` in C++
3. **Not using `virtual` for polymorphic behavior**: Regular functions don't support runtime polymorphism
4. **Attempting to instantiate abstract classes**: Classes with pure virtual functions cannot be instantiated
5. **Confusing public vs private**: Private members cannot be accessed outside the class

## Revision Tips

1. Practice writing simple classes with constructors, setters, and getters
2. Create inheritance hierarchies (e.g., Vehicle → Car, Bike)
3. Trace through code with polymorphism to understand runtime behavior
4. Memorize key definitions and differences for theory questions
5. Review C++ syntax for access specifiers and virtual functions
6. Understand when to use procedural vs OOP—examiners test application sense