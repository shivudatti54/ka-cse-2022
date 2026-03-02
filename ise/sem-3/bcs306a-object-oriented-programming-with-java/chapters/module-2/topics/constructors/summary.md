# Constructors in Java - Summary

## Key Definitions and Concepts

- **Constructor**: A special method invoked automatically when an object is created using the `new` keyword; initializes the object's instance variables
- **Default Constructor**: Compiler-provided constructor with no parameters; initializes variables to default values (0, null, false)
- **Parameterized Constructor**: Constructor accepting arguments to initialize objects with specific values
- **Constructor Overloading**: Defining multiple constructors with different parameter lists in the same class
- **Constructor Chaining**: Using `this()` to call another constructor in the same class, reducing code duplication

## Important Formulas and Techniques

- Constructor signature: `ClassName(parameter1, parameter2, ...)` — no return type, not even void
- Constructor chaining: `this(arg1, arg2)` must be the first statement in the constructor
- Default values: numeric types → 0, reference types → null, boolean → false, char → '\u0000'

## Key Points

- Constructors share the same name as the class and are distinguished from methods by having no return type
- If no constructor is explicitly defined, Java provides a default constructor automatically
- Once any constructor is defined, the default constructor is no longer provided by the compiler
- Constructor overloading relies on parameter lists (number, type, order)—return type is not considered
- The `this()` keyword enables constructor chaining to avoid duplicating initialization code
- Constructors can be overloaded with different access modifiers (public, private, protected, default)
- Private constructors implement design patterns like Singleton and prevent direct object creation
- Constructors are NOT inherited by subclasses and cannot be overridden

## Common Mistakes to Avoid

- Adding a return type to constructors (this creates a regular method, not a constructor)
- Forgetting that defining a parameterized constructor removes the default constructor
- Placing `this()` or `super()` somewhere other than the first statement in the constructor
- Not initializing all instance variables, leading to working with default values
- Confusing constructor overloading with method overloading (same principle, different context)

## Revision Tips

- Practice writing classes with multiple constructors and test object creation with different constructor calls
- Remember the rule: constructors have no return type—they are not methods
- Use the acronym NOVO (No OVerload Option) to remember constructors cannot be overloaded by return type
- Trace through code examples to understand constructor execution order and initialization flow
- Review how constructors differ from methods: initialization vs. computation, invocation timing, inheritance