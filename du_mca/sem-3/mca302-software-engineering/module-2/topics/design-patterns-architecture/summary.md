# Design Patterns and Software Architecture - Summary

## Key Definitions and Concepts

- **Design Pattern**: A proven solution to a recurring software design problem, providing a template that can be customized to solve particular design challenges in specific contexts.

- **Gang of Four (GoF)**: The four authors (Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides) of the seminal book "Design Patterns: Elements of Reusable Object-Oriented Software" (1994).

- **Singleton Pattern**: Ensures a class has only one instance with a global access point, used for logging, configuration managers, and connection pools.

- **Observer Pattern**: Defines a one-to-many dependency where subject state changes automatically notify all dependent observer objects.

- **Strategy Pattern**: Defines a family of algorithms, encapsulates each, and makes them interchangeable at runtime.

- **Adapter Pattern**: Converts incompatible interface into one that clients expect, enabling incompatible classes to work together.

- **Decorator Pattern**: Dynamically adds responsibilities to objects without modifying their classes.

- **Software Architecture**: The high-level structure of a software system defining components, their relationships, and principles governing design and evolution.

- **MVC Architecture**: Separates application into Model (data), View (presentation), and Controller (logic) components.

- **Clean Architecture**: Layered architecture where dependencies point inward, with business entities at the core.

## Important Formulas and Theorems

There are no specific formulas in design patterns, but the following principles guide pattern application:

- **Open/Closed Principle**: Open for extension, closed for modification
- **Dependency Inversion**: Depend on abstractions, not concrete implementations
- **Liskov Substitution**: Subtypes must be substitutable for their base types

## Key Points

- Design patterns are classified into three categories: Creational (object creation), Structural (object composition), and Behavioral (object interaction)

- Creational patterns include Singleton, Factory Method, Abstract Factory, Builder, and Prototype

- Structural patterns include Adapter, Bridge, Composite, Decorator, Facade, Flyweight, and Proxy

- Behavioral patterns include Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, and Visitor

- The Singleton pattern ensures exactly one instance exists throughout the application lifecycle

- The Observer pattern implements event-driven systems and is foundational to the publish-subscribe model

- Strategy pattern enables runtime algorithm selection, promoting flexibility and testability

- Layered architecture separates concerns into Presentation, Business, Data Access, and Database layers

- MVC architecture is predominant in web frameworks and separates concerns for maintainability

- Microservices architecture enables independent deployment and scaling of application components

- Clean Architecture enforces dependency rules where inner layers are independent of outer layers

## Common Mistakes to Avoid

- **Over-engineering**: Applying design patterns where simpler solutions suffice—patterns add complexity and should only be used when there's an actual need for flexibility or reuse

- **Pattern misuse**: Confusing similar patterns (e.g., using Decorator when Adapter is needed, or Strategy when State is more appropriate)

- **Ignoring context**: Design patterns are context-dependent; what works in one scenario may fail in another

- **Forgetting disadvantages**: Every pattern has trade-offs—Singletons complicate testing, Observers can cause memory leaks if not properly detached

## Revision Tips

1. Create a comparison table of all 23 GoF patterns with their category, purpose, and real-world examples

2. Practice implementing at least 5-6 key patterns (Singleton, Factory, Observer, Strategy, Adapter, Decorator) in code

3. Understand the problem each pattern solves before memorizing the solution—examiners often test understanding through scenario-based questions

4. Review UML class diagrams for major patterns to quickly identify patterns in exam questions

5. Link design patterns to SOLID principles—most patterns either implement or support these principles

6. Solve previous year DU question papers to understand the exam pattern and frequently asked questions