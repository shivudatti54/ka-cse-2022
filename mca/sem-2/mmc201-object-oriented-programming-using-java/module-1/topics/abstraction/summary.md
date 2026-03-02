# Abstraction in Java - Summary

## Key Definitions and Concepts

- **Abstraction**: The process of hiding complex implementation details and showing only essential features to users
- **Abstract Class**: A class declared with the `abstract` keyword that cannot be instantiated; may contain abstract and concrete methods
- **Abstract Method**: A method without implementation (no body), declared with `abstract` keyword, must be overridden by subclasses
- **Interface**: A reference type in Java containing only method signatures, constants, default methods, and static methods; achieves full abstraction

## Important Formulas and Theorems

- A class can extend only one abstract class but can implement multiple interfaces
- Interface methods are implicitly abstract (unless default or static)
- Interface variables are implicitly `public static final`
- Abstract methods cannot be `private`, `final`, `static`, or `synchronized`
- Abstract class can have constructors; interfaces cannot

## Key Points

1. Abstraction manages complexity by focusing on "what" rather than "how"
2. Abstract classes use the `abstract` keyword declaration
3. Interfaces achieve 100% abstraction; abstract classes achieve partial abstraction
4. All methods in interfaces are public by default
5. A class implementing an interface must provide implementations for all abstract methods or be declared abstract
6. Default methods in interfaces (Java 8+) allow interfaces to provide concrete implementations
7. Abstract classes can have instance variables and concrete methods; interfaces cannot
8. Use abstract classes for IS-A relationships; use interfaces for CAN-DO relationships

## Common Mistakes to Avoid

1. Trying to instantiate an abstract class directly using `new AbstractClass()`
2. Declaring abstract methods as `private`, `final`, or `static` - these modifiers prevent overriding
3. Forgetting to implement all abstract methods in non-abstract subclasses
4. Confusing abstraction with encapsulation - they are different concepts
5. Using interfaces when an abstract class would be more appropriate (or vice versa)

## Revision Tips

1. Practice writing code for both abstract classes and interfaces to understand the syntax
2. Memorize the differences between abstract classes and interfaces as this is a frequent exam question
3. Remember the key constraint: a class can extend only one class but implement multiple interfaces
4. Review Java 8 features regarding default and static methods in interfaces
5. Practice identifying when to use abstract class vs interface in design scenarios
6. Go through previous year university exam questions on abstraction to understand the pattern
