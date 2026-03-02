# Abstract Classes and Interfaces in Python - Summary

## Key Definitions and Concepts

- **Abstract Class**: A class that cannot be instantiated directly and serves as a blueprint for derived classes. Created by inheriting from `ABC` class in Python.
- **Abstract Method**: A method declared in an abstract class using `@abstractmethod` decorator that must be implemented by all concrete subclasses.
- **Abstract Base Class (ABC)**: Python's built-in mechanism for creating abstract classes, imported from the `abc` module.
- **Protocol**: A class from `typing` module (Python 3.8+) that enables structural subtyping, providing true interface functionality.

## Important Formulas and Theorems

- **ABC Creation**: `class ClassName(ABC):`
- **Abstract Method Declaration**: `@abstractmethod def method_name(self): pass`
- **Abstract Property**: `@property @abstractmethod def name(self): ...`
- **Protocol Definition**: `class InterfaceName(Protocol):`

## Key Points

- Abstract classes enforce a contract: all abstract methods must be implemented by subclasses or the class remains abstract (cannot be instantiated).
- Python's abstract classes can contain both abstract methods (no implementation) and concrete methods (with implementation).
- The `abc` module provides `ABC` as the metaclass and `@abstractmethod` as the decorator for creating abstract methods.
- Protocols use structural subtyping—if a class has the required methods, it satisfies the protocol without explicit inheritance.
- Abstract classes represent "is-a" relationships; interfaces (Protocols) represent "can-do" relationships.
- Multiple inheritance is supported in Python abstract classes, but all abstract methods from all parent classes must be implemented.
- The `@abstractmethod` can be combined with `@property` to create abstract read-only or read-write properties.

## Common Mistakes to Avoid

- Forgetting to import `ABC` and `abstractmethod` from the `abc` module before creating abstract classes.
- Attempting to instantiate an abstract class that hasn't implemented all abstract methods—this raises `TypeError`.
- Confusing abstract classes with interfaces; remember that abstract classes can have concrete method implementations.
- Not providing implementations for all abstract methods in concrete subclasses.
- Using `pass` in abstract methods when you intend to provide a default implementation (use a body instead).

## Revision Tips

- Practice creating at least three different abstract class hierarchies to reinforce the concept.
- Memorize the import statement: `from abc import ABC, abstractmethod`.
- Understand the difference between nominal subtyping (ABC) and structural subtyping (Protocol) through code examples.
- Review real-world analogies: PaymentProcessor, Shape, Animal, Vehicle hierarchies.
- Write small programs that demonstrate instantiation of abstract classes failing before complete implementation.