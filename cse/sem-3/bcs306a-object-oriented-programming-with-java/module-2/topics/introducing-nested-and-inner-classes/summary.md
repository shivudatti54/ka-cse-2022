# Nested and Inner Classes in Java - Summary

## Key Definitions and Concepts

- **Nested Class**: A class defined within the body of another class in Java, providing logical grouping and enhanced encapsulation.
- **Static Nested Class**: A nested class declared with the static keyword that does not hold an implicit reference to the outer class.
- **Inner Class (Non-static)**: A nested class without the static modifier that holds an implicit reference to its outer class instance.
- **Local Inner Class**: A class defined within a method, constructor, or initializer block with limited scope.
- **Anonymous Inner Class**: An unnamed inner class defined and instantiated in a single expression, typically for quick interface implementation.
- **Effectively Final Variable**: A local variable whose value is not changed after initialization, allowing access from local/anonymous inner classes.

## Important Formulas and Syntax

```java
// Static nested class instantiation
OuterClass.StaticNestedClass obj = new OuterClass.StaticNestedClass();

// Member inner class instantiation
OuterClass outer = new OuterClass();
OuterClass.InnerClass inner = outer.new InnerClass();

// Anonymous inner class
InterfaceName obj = new InterfaceName() {
    // implementation
};
```

## Key Points

- Java supports four types of nested classes: static nested classes, member inner classes, local inner classes, and anonymous inner classes.

- Static nested classes can access only static members of the outer class directly, while non-static inner classes can access all members including private ones.

- Member inner classes require an instance of the outer class for instantiation using the syntax `outer.new InnerClass()`.

- Local inner classes are confined to the block in which they are defined and can only access final or effectively final local variables.

- Anonymous inner classes provide a concise way to implement interfaces or extend classes but cannot have explicit constructors.

- Nested classes improve code organization by grouping helper classes that are only used in one location.

- Inner classes hold an implicit reference to their outer class, which can impact memory usage if not managed properly.

- Static nested classes do not hold the implicit reference and can be instantiated without an outer class instance.

## Common Mistakes to Avoid

- Forgetting that static nested classes cannot access instance members of the outer class—only static members are accessible.

- Using incorrect instantiation syntax for inner classes; remember member inner classes require an outer class instance.

- Attempting to access non-final local variables from local inner classes or anonymous inner classes, which causes compile-time errors.

- Declaring anonymous inner classes incorrectly; they must implement an interface or extend a class in a single expression.

- Confusing anonymous inner classes with lambda expressions—lambdas can only be used for functional interfaces (single abstract method).

## Revision Tips

- Practice writing all four types of nested classes to reinforce syntax differences and instantiation patterns.

- Remember the key distinction: static nested classes don't need outer class instance; non-static inner classes do and hold a reference.

- For exams, focus on access control rules—what each type of nested class can and cannot access from the outer class.

- Review practical examples like event handling and iterator patterns where nested classes are commonly used.

- Understand the memory implications: inner classes add overhead due to the implicit reference to outer class objects.
